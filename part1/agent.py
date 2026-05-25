import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Normal


def discount_rewards(r, gamma, done=None):
    discounted_r = torch.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size(-1))):
        if done is not None and done[t]:
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r


def _standardize(advantage, eps=1e-8):
    """Zero-mean, unit-variance advantage.

    Falls back to mean-centring when the batch has near-zero variance
    (e.g. single-step rollouts early in training) — dividing by a tiny std
    would otherwise blow the gradient up.
    """
    mean = advantage.mean()
    std = advantage.std()
    if std < eps:
        return advantage - mean
    return (advantage - mean) / (std + eps)

def _scale_only(advantage, eps=1e-8):
    """Normalize advantage SCALE without re-centering.

    Constant-baseline variants (reinforce_ema / reinforce_fixed) must NOT be
    run through _standardize: subtracting the batch mean cancels the constant
    baseline entirely (std(G-b)==std(G)), collapsing them into reinforce_batch.
    Dividing by std alone fixes the scale (the cause of LR-sensitivity)
    while preserving each baseline's distinct centering.
    """
    std = advantage.std()
    if std < eps:
        return advantage
    return advantage / (std + eps)


VALID_ALGORITHMS = ['reinforce', 'reinforce_batch', 'reinforce_ema', 'reinforce_fixed', 'ac_mc', 'ac_td']


class Policy(torch.nn.Module):
    def __init__(self, state_space, action_space):
        super().__init__()
        self.state_space = state_space
        self.action_space = action_space
        self.hidden = 64
        self.tanh = torch.nn.Tanh()

        """
            Actor network
        """
        self.fc1_actor = torch.nn.Linear(state_space, self.hidden)
        self.fc2_actor = torch.nn.Linear(self.hidden, self.hidden)
        self.fc3_actor_mean = torch.nn.Linear(self.hidden, action_space)
        
        # Learned standard deviation for exploration at training time 
        self.sigma_activation = F.softplus
        init_sigma = 0.5
        self.sigma = torch.nn.Parameter(torch.zeros(self.action_space)+init_sigma)


        """
            Critic network
        """
        self.fc1_critic = torch.nn.Linear(state_space, self.hidden)
        self.fc2_critic = torch.nn.Linear(self.hidden, self.hidden)
        self.fc3_critic = torch.nn.Linear(self.hidden, 1)


        self.init_weights()


    def init_weights(self):
        # The original template used normal_(std=1.0). With 64 hidden units
        # and tanh activations, this produces pre-activation variance ≈ fan_in
        # (≈64), driving tanh into saturation and causing vanishing gradients.
        # Xavier uniform (Glorot & Bengio, 2010) keeps the signal variance
        # ≈1 across layers, which is the standard init for tanh networks.
        for m in self.modules():
            if type(m) is torch.nn.Linear:
                torch.nn.init.xavier_uniform_(m.weight)
                torch.nn.init.zeros_(m.bias)
        # Critic head: smaller init to prevent wild initial value predictions
        torch.nn.init.normal_(self.fc3_critic.weight, std=0.1)
        torch.nn.init.zeros_(self.fc3_critic.bias)


    def forward(self, x):
        """
            Actor
        """
        x_actor = self.tanh(self.fc1_actor(x))
        x_actor = self.tanh(self.fc2_actor(x_actor))
        action_mean = self.fc3_actor_mean(x_actor)

        sigma = self.sigma_activation(self.sigma)
        normal_dist = Normal(action_mean, sigma)

        return normal_dist


    def critic_forward(self, x):
        """
            Critic — separate from forward() to preserve get_action signature.
        """
        x_critic = self.tanh(self.fc1_critic(x))
        x_critic = self.tanh(self.fc2_critic(x_critic))
        value = self.fc3_critic(x_critic)
        return value.squeeze(-1)


    def actor_parameters(self):
        """Return only the actor network parameters (including sigma)."""
        return (list(self.fc1_actor.parameters()) +
                list(self.fc2_actor.parameters()) +
                list(self.fc3_actor_mean.parameters()) +
                [self.sigma])

    def critic_parameters(self):
        """Return only the critic network parameters."""
        return (list(self.fc1_critic.parameters()) +
                list(self.fc2_critic.parameters()) +
                list(self.fc3_critic.parameters()))


class Agent(object):
    def __init__(self, policy, algorithm='reinforce', device='cpu',
                 lr=1e-3, critic_lr=3e-3, gamma=0.99, ema_alpha=0.05,
                 fixed_baseline=20.0):
        self.train_device = device
        self.policy = policy.to(self.train_device)

        assert algorithm in VALID_ALGORITHMS, f"Unknown algorithm: {algorithm}"
        self.algorithm = algorithm
        self.gamma = gamma

        # Actor optimizer — scoped to actor parameters only
        self.actor_optimizer = torch.optim.Adam(policy.actor_parameters(), lr=lr)

        # Critic optimizer — only for actor-critic variants
        self.critic_optimizer = None
        if algorithm in ('ac_mc', 'ac_td'):
            self.critic_optimizer = torch.optim.Adam(
                policy.critic_parameters(), lr=critic_lr)

        # EMA baseline state (used only by reinforce_ema).
        # None sentinel triggers lazy init to G.mean() on the first update —
        # avoids the cold-start where advantage = G - 0 in the first few
        # episodes (returns 1-5 vs baseline 0 = no variance reduction when
        # it matters most).
        self._ema_baseline = None
        self.ema_alpha = ema_alpha

        # Fixed baseline (used only by reinforce_fixed)
        self.fixed_baseline = fixed_baseline

        self.states = []
        self.next_states = []
        self.action_log_probs = []
        self.rewards = []
        self.done = []          # MDP termination only (for TD bootstrap)
        self.episode_done = []  # episode boundary: terminated OR truncated
                                # (for discount_rewards return reset)


    @property
    def ema_baseline(self):
        """Read-only accessor (None until the first reinforce_ema update)."""
        return self._ema_baseline

    def _update_ema(self, g_mean):
        """Update EMA baseline; lazy-init to g_mean on the first call."""
        if self._ema_baseline is None:
            self._ema_baseline = g_mean
        else:
            self._ema_baseline = ((1 - self.ema_alpha) * self._ema_baseline
                                  + self.ema_alpha * g_mean)
        return self._ema_baseline


    def update_policy(self):
        action_log_probs = torch.stack(self.action_log_probs, dim=0).to(self.train_device).squeeze(-1)
        states = torch.stack(self.states, dim=0).to(self.train_device).squeeze(-1)
        next_states = torch.stack(self.next_states, dim=0).to(self.train_device).squeeze(-1)
        rewards = torch.stack(self.rewards, dim=0).to(self.train_device).squeeze(-1)
        done = torch.Tensor(self.done).to(self.train_device)
        episode_done = torch.Tensor(self.episode_done).to(self.train_device)

        self.states, self.next_states, self.action_log_probs, self.rewards, self.done, self.episode_done = [], [], [], [], [], []

        # Dispatch to the appropriate variant
        # REINFORCE variants use episode_done (terminated|truncated) for
        # discount_rewards so returns don't bleed across episodes when
        # update_every > 1.  ac_mc also uses episode_done for MC returns.
        # ac_td uses the MDP-only 'done' for the bootstrap mask (truncation
        # is NOT a true terminal state for the value function).
        if self.algorithm == 'reinforce':
            return self._update_reinforce(action_log_probs, rewards, episode_done)
        elif self.algorithm == 'reinforce_batch':
            return self._update_reinforce_batch(action_log_probs, rewards, episode_done)
        elif self.algorithm == 'reinforce_ema':
            return self._update_reinforce_ema(action_log_probs, rewards, episode_done)
        elif self.algorithm == 'reinforce_fixed':
            return self._update_reinforce_fixed(action_log_probs, rewards, episode_done)
        elif self.algorithm == 'ac_mc':
            return self._update_ac_mc(action_log_probs, states, rewards, episode_done)
        elif self.algorithm == 'ac_td':
            return self._update_ac_td(action_log_probs, states, next_states,
                                      rewards, done)


    # ------------------------------------------------------------------
    #  REINFORCE variants
    # ------------------------------------------------------------------

    def _update_reinforce(self, action_log_probs, rewards, done):
        """Vanilla REINFORCE — no baseline."""
        G = discount_rewards(rewards, self.gamma, done)

        # Policy gradient loss (negative sign: PyTorch minimises)
        actor_loss = -(action_log_probs * G).mean()

        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': None,
            'baseline': None,
            'mean_value': None,
            'mean_td_error': None,
        }


    def _update_reinforce_batch(self, action_log_probs, rewards, done):
        """REINFORCE + per-batch mean baseline."""
        G = discount_rewards(rewards, self.gamma, done)
        baseline = G.mean()
        advantage = _standardize(G - baseline)

        actor_loss = -(action_log_probs * advantage).mean()

        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': None,
            'baseline': baseline.item(),
            'mean_value': None,
            'mean_td_error': None,
        }


    def _update_reinforce_ema(self, action_log_probs, rewards, done):
        """REINFORCE + EMA constant baseline (tracks discounted-return mean)."""
        G = discount_rewards(rewards, self.gamma, done)

        # Lazy init on first call; standard EMA thereafter.
        baseline = self._update_ema(G.mean().item())
        advantage = _scale_only(G - baseline)

        actor_loss = -(action_log_probs * advantage).mean()

        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': None,
            'baseline': baseline,
            'mean_value': None,
            'mean_td_error': None,
        }

    def _update_reinforce_fixed(self, action_log_probs, rewards, done):
        """REINFORCE + constant baseline (set once at construction)."""
        G = discount_rewards(rewards, self.gamma, done)
        advantage = _scale_only(G - self.fixed_baseline)

        actor_loss = -(action_log_probs * advantage).mean()

        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': None,
            'baseline': self.fixed_baseline,
            'mean_value': None,
            'mean_td_error': None,
        }

    # ------------------------------------------------------------------
    #  Actor-Critic variants
    # ------------------------------------------------------------------

    def _update_ac_mc(self, action_log_probs, states, rewards, done):
        """Actor-Critic with Monte-Carlo return as critic target."""
        G = discount_rewards(rewards, self.gamma, done)
        values = self.policy.critic_forward(states)

        # Advantage — detach so actor update only touches actor params.
        # Standardize for actor loss only (critic target G stays raw); the
        # _standardize helper falls back to mean-centring when std≈0.
        advantage = _standardize((G - values).detach())

        # Critic update: push V(s) toward Monte-Carlo return G
        critic_loss = F.mse_loss(values, G)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.critic_parameters(), max_norm=0.5)
        self.critic_optimizer.step()

        # Actor update
        actor_loss = -(action_log_probs * advantage).mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': critic_loss.item(),
            'baseline': None,
            'mean_value': values.mean().item(),
            'mean_td_error': None,
        }


    def _update_ac_td(self, action_log_probs, states, next_states,
                      rewards, done):
        """Actor-Critic with bootstrapped TD target."""
        values = self.policy.critic_forward(states)
        next_values = self.policy.critic_forward(next_states)

        # TD target — next_values detached so gradients don't flow through
        # both sides of the MSE (constraint #8)
        td_target = rewards + self.gamma * next_values.detach() * (1 - done)

        # Advantage — detach so actor update only touches actor params.
        # Standardize for actor loss only (critic target td_target stays raw);
        # the _standardize helper falls back to mean-centring when std≈0.
        advantage_raw = (td_target - values).detach()
        advantage = _standardize(advantage_raw)

        # Critic update: push V(s) toward TD target
        critic_loss = F.mse_loss(values, td_target)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.critic_parameters(), max_norm=0.5)
        self.critic_optimizer.step()

        # Actor update
        actor_loss = -(action_log_probs * advantage).mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.actor_parameters(), max_norm=0.5)
        self.actor_optimizer.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': critic_loss.item(),
            'baseline': None,
            'mean_value': values.mean().item(),
            # Log the pre-standardization TD error — the standardized one is
            # ~0 by construction and uninformative.
            'mean_td_error': advantage_raw.mean().item(),
        }


    def get_action(self, state, evaluation=False):
        """ state -> action (3-d), action_log_densities """
        x = torch.from_numpy(state).float().to(self.train_device)

        if evaluation:  # Return mean — no graph needed
            with torch.no_grad():
                normal_dist = self.policy(x)
            return normal_dist.mean, None

        else:   # Sample from the distribution
            normal_dist = self.policy(x)
            action = normal_dist.sample()

            # Compute Log probability of the action [ log(p(a[0] AND a[1] AND a[2])) = log(p(a[0])*p(a[1])*p(a[2])) = log(p(a[0])) + log(p(a[1])) + log(p(a[2])) ]
            action_log_prob = normal_dist.log_prob(action).sum()

            return action, action_log_prob


    def store_outcome(self, state, next_state, action_log_prob, reward,
                      done, episode_done):
        self.states.append(torch.from_numpy(state).float())
        self.next_states.append(torch.from_numpy(next_state).float())
        self.action_log_probs.append(action_log_prob)
        self.rewards.append(torch.Tensor([reward]))
        self.done.append(done)                # MDP termination (for TD bootstrap)
        self.episode_done.append(episode_done) # episode boundary (for return reset)
