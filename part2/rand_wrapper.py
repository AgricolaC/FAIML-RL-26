import numpy as np
import gymnasium as gym
import os
from torch.utils.tensorboard import SummaryWriter

class RandomizationWrapper(gym.Wrapper):
    """
    Wrapper that applies randomization to the environment.
    """
    def __init__(
        self,
        env,
        mass_range=(1.0, 1.0),
        mode="none",
        shared_phi_L=None,
        shared_phi_H=None,
        log_path=None,
        tb_log_dir=None,
    ):
        super().__init__(env)

        self.mode = mode
        self.mass_range = mass_range

        # global limits
        self.mass_min_limit, self.mass_max_limit = mass_range
        
        # ADR specific state
        self.p_b = 0.5
        self.m = 50
        self.t_H = 0.7
        self.t_L = 0.2
        self.delta = 0.1
        
        self.shared_phi_L = shared_phi_L
        self.shared_phi_H = shared_phi_H
        
        # We need local buffers for performance tracking
        self.buffer_L = []
        self.buffer_H = []
        self.last_sample_type = "interior"
        self.current_mass = None
        
        self.log_path = log_path
        self.total_steps = 0
        if self.log_path is not None and not os.path.exists(self.log_path):
            with open(self.log_path, "w") as f:
                f.write("step,phi_L,phi_H,perf,bound_updated\n")
                
        self.writer = SummaryWriter(log_dir=tb_log_dir) if tb_log_dir else None

    @property
    def phi_L(self):
        return self.shared_phi_L.value if self.shared_phi_L else 0.9
        
    @phi_L.setter
    def phi_L(self, value):
        if self.shared_phi_L:
            with self.shared_phi_L.get_lock():
                self.shared_phi_L.value = float(value)

    @property
    def phi_H(self):
        return self.shared_phi_H.value if self.shared_phi_H else 1.1
        
    @phi_H.setter
    def phi_H(self, value):
        if self.shared_phi_H:
            with self.shared_phi_H.get_lock():
                self.shared_phi_H.value = float(value)

    # -----------------------
    # Mass Sampling
    # -----------------------

    def _sample_mass(self):
        if self.mode == "none":
            self.last_sample_type = "none"
            return None
            
        elif self.mode == "udr":
            self.last_sample_type = "udr"
            return np.random.uniform(self.mass_min_limit, self.mass_max_limit)
            
        elif self.mode == "adr":
            if np.random.rand() < self.p_b:
                if np.random.rand() < 0.5:
                    self.last_sample_type = "boundary_L"
                    return self.phi_L
                else:
                    self.last_sample_type = "boundary_H"
                    return self.phi_H
            else:
                self.last_sample_type = "interior"
                return np.random.uniform(self.phi_L, self.phi_H)
        else:
            raise NotImplementedError(f"Sampling strategy '{self.mode}' is not implemented yet.")

    def step(self, action):
        self.total_steps += 1
        obs, reward, terminated, truncated, info = self.env.step(action)
        done = terminated or truncated

        if done and self.mode == "adr" and self.last_sample_type in ["boundary_L", "boundary_H"]:
            perf = float(info.get("is_success", 0))
            MIN_RANGE = 0.2
            if self.last_sample_type == "boundary_L":
                self.buffer_L.append(perf)
                if len(self.buffer_L) >= self.m:
                    mean_perf = sum(self.buffer_L) / len(self.buffer_L)
                    if mean_perf >= self.t_H:
                        new_phi_L = max(self.mass_min_limit, self.phi_L - self.delta)
                        if abs(new_phi_L - self.phi_L) > 1e-6:
                            print(f"[ADR] Expanded lower bound: {self.phi_L:.2f} -> {new_phi_L:.2f} (perf: {mean_perf:.2f})")
                            self.phi_L = new_phi_L
                            self._log_boundary(mean_perf, "L")
                    elif mean_perf <= self.t_L:
                        new_phi_L = min(self.phi_H - MIN_RANGE, self.phi_L + self.delta)
                        if abs(new_phi_L - self.phi_L) > 1e-6:
                            print(f"[ADR] Contracted lower bound: {self.phi_L:.2f} -> {new_phi_L:.2f} (perf: {mean_perf:.2f})")
                            self.phi_L = new_phi_L
                            self._log_boundary(mean_perf, "L")
                    self.buffer_L.clear()
            elif self.last_sample_type == "boundary_H":
                self.buffer_H.append(perf)
                if len(self.buffer_H) >= self.m:
                    mean_perf = sum(self.buffer_H) / len(self.buffer_H)
                    if mean_perf >= self.t_H:
                        new_phi_H = min(self.mass_max_limit, self.phi_H + self.delta)
                        if abs(new_phi_H - self.phi_H) > 1e-6:
                            print(f"[ADR] Expanded upper bound: {self.phi_H:.2f} -> {new_phi_H:.2f} (perf: {mean_perf:.2f})")
                            self.phi_H = new_phi_H
                            self._log_boundary(mean_perf, "H")
                    elif mean_perf <= self.t_L:
                        new_phi_H = max(self.phi_L + MIN_RANGE, self.phi_H - self.delta)
                        if abs(new_phi_H - self.phi_H) > 1e-6:
                            print(f"[ADR] Contracted upper bound: {self.phi_H:.2f} -> {new_phi_H:.2f} (perf: {mean_perf:.2f})")
                            self.phi_H = new_phi_H
                            self._log_boundary(mean_perf, "H")
                    self.buffer_H.clear()

        return obs, reward, terminated, truncated, info

    def _log_boundary(self, mean_perf, bound_updated):
        if self.log_path is not None:
            with open(self.log_path, "a") as f:
                f.write(f"{self.total_steps},{self.phi_L:.3f},{self.phi_H:.3f},{mean_perf:.2f},{bound_updated}\n")
                
        if self.writer is not None:
            self.writer.add_scalar("adr/phi_L", self.phi_L, self.total_steps)
            self.writer.add_scalar("adr/phi_H", self.phi_H, self.total_steps)
            self.writer.add_scalar("adr/range_width", self.phi_H - self.phi_L, self.total_steps)
            self.writer.add_scalar(f"adr/buf_{bound_updated}_perf", mean_perf, self.total_steps)

    # -----------------------
    # Reset
    # -----------------------

    def reset(self, **kwargs):
        new_mass = self._sample_mass()
        self.current_mass = new_mass

        if new_mass is not None:
            sim = self.env.unwrapped.task.sim
            object_body_id = sim._bodies_idx["object"]

            sim.physics_client.changeDynamics(
                bodyUniqueId=object_body_id,
                linkIndex=-1,
                mass=float(new_mass),
            )

        return super().reset(**kwargs)
