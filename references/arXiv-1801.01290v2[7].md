---
abstract: |
  Model-free deep reinforcement learning (RL) algorithms have been
  demonstrated on a range of challenging decision making and control
  tasks. However, these methods typically suffer from two major
  challenges: very high sample complexity and brittle convergence
  properties, which necessitate meticulous hyperparameter tuning. Both
  of these challenges severely limit the applicability of such methods
  to complex, real-world domains. In this paper, we propose soft
  actor-critic, an off-policy actor-critic deep RL algorithm based on
  the maximum entropy reinforcement learning framework. In this
  framework, the actor aims to maximize expected reward while also
  maximizing entropy. That is, to succeed at the task while acting as
  randomly as possible. Prior deep RL methods based on this framework
  have been formulated as Q-learning methods. By combining off-policy
  updates with a stable stochastic actor-critic formulation, our method
  achieves state-of-the-art performance on a range of continuous control
  benchmark tasks, outperforming prior on-policy and off-policy methods.
  Furthermore, we demonstrate that, in contrast to other off-policy
  algorithms, our approach is very stable, achieving very similar
  performance across different random seeds.
bibliography:
- refs.bib
---

# Introduction

Model-free deep reinforcement learning (RL) algorithms have been applied
in a range of challenging domains, from
games [@mnih2013playing; @silver2016mastering] to robotic
control [@schulman2015trust]. The combination of RL and high-capacity
function approximators such as neural networks holds the promise of
automating a wide range of decision making and control tasks, but
widespread adoption of these methods in real-world domains has been
hampered by two major challenges. First, model-free deep RL methods are
notoriously expensive in terms of their sample complexity. Even
relatively simple tasks can require millions of steps of data
collection, and complex behaviors with high-dimensional observations
might need substantially more. Second, these methods are often brittle
with respect to their hyperparameters: learning rates, exploration
constants, and other settings must be set carefully for different
problem settings to achieve good results. Both of these challenges
severely limit the applicability of model-free deep RL to real-world
tasks.

One cause for the poor sample efficiency of deep RL methods is on-policy
learning: some of the most commonly used deep RL algorithms, such as
TRPO [@schulman2015trust], PPO [@schulman2017proximal] or
A3C [@mnih2016asynchronous], require new samples to be collected for
each gradient step. This quickly becomes extravagantly expensive, as the
number of gradient steps and samples per step needed to learn an
effective policy increases with task complexity. Off-policy algorithms
aim to reuse past experience. This is not directly feasible with
conventional policy gradient formulations, but is relatively
straightforward for Q-learning based methods [@mnih2015human].
Unfortunately, the combination of off-policy learning and
high-dimensional, nonlinear function approximation with neural networks
presents a major challenge for stability and
convergence [@bhatnagar2009convergent]. This challenge is further
exacerbated in continuous state and action spaces, where a separate
actor network is often used to perform the maximization in Q-learning. A
commonly used algorithm in such settings, deep deterministic policy
gradient (DDPG) [@lillicrap2015continuous], provides for
sample-efficient learning but is notoriously challenging to use due to
its extreme brittleness and hyperparameter
sensitivity [@duan2016benchmarking; @henderson2017deep].

We explore how to design an efficient and stable model-free deep RL
algorithm for continuous state and action spaces. To that end, we draw
on the maximum entropy framework, which augments the standard maximum
reward reinforcement learning objective with an entropy maximization
term [@ziebart2008maximum; @toussaint2009robot; @rawlik2012stochastic; @fox2015taming; @haarnoja2017reinforcement].
Maximum entropy reinforcement learning alters the RL objective, though
the original objective can be recovered using a temperature
parameter [@haarnoja2017reinforcement]. More importantly, the maximum
entropy formulation provides a substantial improvement in exploration
and robustness: as discussed by @ziebart2010modeling, maximum entropy
policies are robust in the face of model and estimation errors, and as
demonstrated by [@haarnoja2017reinforcement], they improve exploration
by acquiring diverse behaviors. Prior work has proposed model-free deep
RL algorithms that perform on-policy learning with entropy
maximization [@o2016pgq], as well as off-policy methods based on soft
Q-learning and its
variants [@schulman2017equivalence; @nachum2017bridging; @haarnoja2017reinforcement].
However, the on-policy variants suffer from poor sample complexity for
the reasons discussed above, while the off-policy variants require
complex approximate inference procedures in continuous action spaces.

In this paper, we demonstrate that we can devise an off-policy maximum
entropy actor-critic algorithm, which we call soft actor-critic (SAC),
which provides for both sample-efficient learning and stability. This
algorithm extends readily to very complex, high-dimensional tasks, such
as the Humanoid benchmark [@duan2016benchmarking] with 21 action
dimensions, where off-policy methods such as DDPG typically struggle to
obtain good results [@gu2016q]. SAC also avoids the complexity and
potential instability associated with approximate inference in prior
off-policy maximum entropy algorithms based on soft
Q-learning [@haarnoja2017reinforcement]. We present a convergence proof
for policy iteration in the maximum entropy framework, and then
introduce a new algorithm based on an approximation to this procedure
that can be practically implemented with deep neural networks, which we
call soft actor-critic. We present empirical results that show that soft
actor-critic attains a substantial improvement in both performance and
sample efficiency over both off-policy and on-policy prior methods. We
also compare to twin delayed deep deterministic (TD3) policy gradient
algorithm [@fujimoto2018addressing], which is a concurrent work that
proposes a deterministic algorithm that substantially improves on DDPG.

# Related Work

Our soft actor-critic algorithm incorporates three key ingredients: an
actor-critic architecture with separate policy and value function
networks, an off-policy formulation that enables reuse of previously
collected data for efficiency, and entropy maximization to enable
stability and exploration. We review prior works that draw on some of
these ideas in this section. Actor-critic algorithms are typically
derived starting from policy iteration, which alternates between *policy
evaluation*---computing the value function for a policy---and *policy
improvement*---using the value function to obtain a better
policy [@barto1983neuronlike; @sutton1998reinforcement]. In large-scale
reinforcement learning problems, it is typically impractical to run
either of these steps to convergence, and instead the value function and
policy are optimized jointly. In this case, the policy is referred to as
the actor, and the value function as the critic. Many actor-critic
algorithms build on the standard, on-policy policy gradient formulation
to update the actor [@peters2008reinforcement], and many of them also
consider the entropy of the policy, but instead of maximizing the
entropy, they use it as an regularizer
[@schulman2017proximal; @schulman2015trust; @mnih2016asynchronous; @gruslys2017reactor].
On-policy training tends to improve stability but results in poor sample
complexity.

There have been efforts to increase the sample efficiency while
retaining robustness by incorporating off-policy samples and by using
higher order variance reduction techniques [@o2016pgq; @gu2016q].
However, fully off-policy algorithms still attain better efficiency. A
particularly popular off-policy actor-critic method,
DDPG [@lillicrap2015continuous], which is a deep variant of the
deterministic policy gradient [@silver2014deterministic] algorithm, uses
a Q-function estimator to enable off-policy learning, and a
deterministic actor that maximizes this Q-function. As such, this method
can be viewed both as a deterministic actor-critic algorithm and an
approximate Q-learning algorithm. Unfortunately, the interplay between
the deterministic actor network and the Q-function typically makes DDPG
extremely difficult to stabilize and brittle to hyperparameter
settings [@duan2016benchmarking; @henderson2017deep]. As a consequence,
it is difficult to extend DDPG to complex, high-dimensional tasks, and
on-policy policy gradient methods still tend to produce the best results
in such settings [@gu2016q]. Our method instead combines off-policy
actor-critic training with a *stochastic* actor, and further aims to
maximize the entropy of this actor with an entropy maximization
objective. We find that this actually results in a considerably more
stable and scalable algorithm that, in practice, exceeds both the
efficiency and final performance of DDPG. A similar method can be
derived as a zero-step special case of stochastic value gradients
(SVG(0)) [@heess2015learning]. However, SVG(0) differs from our method
in that it optimizes the standard maximum expected return objective, and
it does not make use of a separate value network, which we found to make
training more stable.

Maximum entropy reinforcement learning optimizes policies to maximize
both the expected return and the expected entropy of the policy. This
framework has been used in many contexts, from inverse reinforcement
learning [@ziebart2008maximum] to optimal
control [@todorov2008general; @toussaint2009robot; @rawlik2012stochastic].
In guided policy search [@levine2013guided; @levine2016end], the maximum
entropy distribution is used to guide policy learning towards
high-reward regions. More recently, several papers have noted the
connection between Q-learning and policy gradient methods in the
framework of maximum entropy
learning [@o2016pgq; @haarnoja2017reinforcement; @nachum2017bridging; @schulman2017equivalence].
While most of the prior model-free works assume a discrete action space,
@nachum2017trust approximate the maximum entropy distribution with a
Gaussian and @haarnoja2017reinforcement with a sampling network trained
to draw samples from the optimal policy. Although the soft Q-learning
algorithm proposed by @haarnoja2017reinforcement has a value function
and actor network, it is not a true actor-critic algorithm: the
Q-function is estimating the optimal Q-function, and the actor does not
directly affect the Q-function except through the data distribution.
Hence, @haarnoja2017reinforcement motivates the actor network as an
approximate sampler, rather than the actor in an actor-critic algorithm.
Crucially, the convergence of this method hinges on how well this
sampler approximates the true posterior. In contrast, we prove that our
method converges to the optimal policy from a given policy class,
regardless of the policy parameterization. Furthermore, these prior
maximum entropy methods generally do not exceed the performance of
state-of-the-art off-policy algorithms, such as DDPG, when learning from
scratch, though they may have other benefits, such as improved
exploration and ease of fine-tuning. In our experiments, we demonstrate
that our soft actor-critic algorithm does in fact exceed the performance
of prior state-of-the-art off-policy deep RL methods by a wide margin.

# Preliminaries {#sec:preliminaries}

We first introduce notation and summarize the standard and maximum
entropy reinforcement learning frameworks.

## Notation

We address policy learning in continuous action spaces. We consider an
infinite-horizon Markov decision process (MDP), defined by the tuple
$(\mathcal{S}, \mathcal{A}, p, r)$, where the state space $\mathcal{S}$
and the action space $\mathcal{A}$ are continuous, and the unknown state
transition probability
$p:\ \mathcal{S}\times \mathcal{S}\times \mathcal{A}\rightarrow [0,\, \infty)$
represents the probability density of the next state
${\mathbf{s}_{t+1}}\in\mathcal{S}$ given the current state
${\mathbf{s}_t}\in\mathcal{S}$ and action
${\mathbf{a}_t}\in\mathcal{A}$. The environment emits a bounded reward
$r: \mathcal{S}\times \mathcal{A}\rightarrow  [r_\mathrm{min},r_\mathrm{max}]$
on each transition. We will use $\rho_\pi({\mathbf{s}_t})$ and
$\rho_\pi({\mathbf{s}_t},{\mathbf{a}_t})$ to denote the state and
state-action marginals of the trajectory distribution induced by a
policy $\pi({\mathbf{a}_t}|{\mathbf{s}_t})$.

## Maximum Entropy Reinforcement Learning

Standard RL maximizes the expected sum of rewards
$\sum_t \operatorname{\mathbb{E}}_{({\mathbf{s}_t},{\mathbf{a}_t})\sim\rho_\pi}\left[r({\mathbf{s}_t},{\mathbf{a}_t})\right]$.
We will consider a more general maximum entropy objective (see
e.g. @ziebart2010modeling), which favors stochastic policies by
augmenting the objective with the expected entropy of the policy over
$\rho_\pi({\mathbf{s}_t})$: $$\begin{align}
\label{eq:maxent_objective}
J(\pi)  = \sum_{t=0}^{T} \operatorname{\mathbb{E}}_{({\mathbf{s}_t}, {\mathbf{a}_t}) \sim \rho_\pi}\left[r({\mathbf{s}_t},{\mathbf{a}_t}) + \alpha\mathcal{H}(\pi({\,\cdot\,}|{\mathbf{s}_t}))\right].
\end{align}$$ The temperature parameter $\alpha$ determines the relative
importance of the entropy term against the reward, and thus controls the
stochasticity of the optimal policy. The maximum entropy objective
differs from the standard maximum expected reward objective used in
conventional reinforcement learning, though the conventional objective
can be recovered in the limit as $\alpha \rightarrow 0$. For the rest of
this paper, we will omit writing the temperature explicitly, as it can
always be subsumed into the reward by scaling it by $\alpha^{-1}$.

This objective has a number of conceptual and practical advantages.
First, the policy is incentivized to explore more widely, while giving
up on clearly unpromising avenues. Second, the policy can capture
multiple modes of near-optimal behavior. In problem settings where
multiple actions seem equally attractive, the policy will commit equal
probability mass to those actions. Lastly, prior work has observed
improved exploration with this
objective [@haarnoja2017reinforcement; @schulman2017equivalence], and in
our experiments, we observe that it considerably improves learning speed
over state-of-art methods that optimize the conventional RL objective
function. We can extend the objective to infinite horizon problems by
introducing a discount factor $\gamma$ to ensure that the sum of
expected rewards and entropies is finite. Writing down the maximum
entropy objective for the infinite horizon discounted case is more
involved [@thomas2014bias] and is deferred to
[Appendix [7](#app:objective){reference-type="ref"
reference="app:objective"}](#app:objective).

Prior methods have proposed directly solving for the optimal Q-function,
from which the optimal policy can be
recovered [@ziebart2008maximum; @fox2015taming; @haarnoja2017reinforcement].
We will discuss how we can devise a soft actor-critic algorithm through
a policy iteration formulation, where we instead evaluate the Q-function
of the current policy and update the policy through an *off-policy*
gradient update. Though such algorithms have previously been proposed
for conventional reinforcement learning, our method is, to our
knowledge, the first off-policy actor-critic method in the maximum
entropy reinforcement learning framework.

# From Soft Policy Iteration to Soft Actor-Critic {#sec:soft_policy_iteration}

Our off-policy soft actor-critic algorithm can be derived starting from
a maximum entropy variant of the policy iteration method. We will first
present this derivation, verify that the corresponding algorithm
converges to the optimal policy from its density class, and then present
a practical deep reinforcement learning algorithm based on this theory.

## Derivation of Soft Policy Iteration

We will begin by deriving soft policy iteration, a general algorithm for
learning optimal maximum entropy policies that alternates between policy
evaluation and policy improvement in the maximum entropy framework. Our
derivation is based on a tabular setting, to enable theoretical analysis
and convergence guarantees, and we extend this method into the general
continuous setting in the next section. We will show that soft policy
iteration converges to the optimal policy within a set of policies which
might correspond, for instance, to a set of parameterized densities.

In the policy evaluation step of soft policy iteration, we wish to
compute the value of a policy $\pi$ according to the maximum entropy
objective
in [\[eq:maxent_objective\]](#eq:maxent_objective){reference-type="ref+label"
reference="eq:maxent_objective"}. For a fixed policy, the soft Q-value
can be computed iteratively, starting from any function
$Q: \mathcal{S}\times \mathcal{A}\rightarrow \mathbb{R}$ and repeatedly
applying a modified Bellman backup operator $\mathcal{T}^\pi$ given by
$$\begin{align}
\label{eq:soft_bellman_backup_op}
\mathcal{T}^\pi Q({\mathbf{s}_t}, {\mathbf{a}_t}) \triangleq  r({\mathbf{s}_t}, {\mathbf{a}_t}) + \gamma\operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p}\left[V({\mathbf{s}_{t+1}})\right],
\end{align}$$ where $$\begin{align}
V({\mathbf{s}_t}) = \operatorname{\mathbb{E}}_{{\mathbf{a}_t}\sim\pi}\left[Q({\mathbf{s}_t}, {\mathbf{a}_t}) - \log\pi({\mathbf{a}_t}|{\mathbf{s}_t})\right]
\label{eq:soft_value_function}
\end{align}$$ is the soft state value function. We can obtain the soft
value function for any policy $\pi$ by repeatedly applying
$\mathcal{T}^\pi$ as formalized below.

:::: {#lem:soft_policy_evaluation .lemma}
**Lemma 1** (Soft Policy Evaluation). *Consider the soft Bellman backup
operator $\mathcal{T}^\pi$ in
[\[eq:soft_bellman_backup_op\]](#eq:soft_bellman_backup_op){reference-type="ref+label"
reference="eq:soft_bellman_backup_op"} and a mapping
$Q^0: \mathcal{S}\times \mathcal{A}\rightarrow \mathbb{R}$ with
$|\mathcal{A}|<\infty$, and define $Q^{k+1} = \mathcal{T}^\pi Q^k$. Then
the sequence $Q^k$ will converge to the soft Q-value of $\pi$ as
$k\rightarrow \infty$.*

::: proof
**Proof.* See
[Appendix [8.1](#app:lem_soft_policy_evaluation){reference-type="ref"
reference="app:lem_soft_policy_evaluation"}](#app:lem_soft_policy_evaluation). ◻*
:::
::::

In the policy improvement step, we update the policy towards the
exponential of the new Q-function. This particular choice of update can
be guaranteed to result in an improved policy in terms of its soft
value. Since in practice we prefer policies that are tractable, we will
additionally restrict the policy to some set of policies $\Pi$, which
can correspond, for example, to a parameterized family of distributions
such as Gaussians. To account for the constraint that $\pi\in \Pi$, we
project the improved policy into the desired set of policies. While in
principle we could choose any projection, it will turn out to be
convenient to use the information projection defined in terms of the
Kullback-Leibler divergence. In the other words, in the policy
improvement step, for each state, we update the policy according to
$$\begin{align}
%
%
%
\pi_\mathrm{new} = \arg\underset{\pi'\in \Pi}{\min}\mathrm{D_{KL}}\left(\pi'({\,\cdot\,}|{\mathbf{s}_t})\;\middle\|\;\frac{\exp\left(Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\,\cdot\,})\right)}{Z^{\pi_\mathrm{old}}({\mathbf{s}_t})}\right).
%
\label{eq:constrainted_policy_fitting}
\end{align}$$ The partition function
$Z^{\pi_\mathrm{old}}({\mathbf{s}_t})$ normalizes the distribution, and
while it is intractable in general, it does not contribute to the
gradient with respect to the new policy and can thus be ignored, as
noted in the next section. For this projection, we can show that the
new, projected policy has a higher value than the old policy with
respect to the objective
in [\[eq:maxent_objective\]](#eq:maxent_objective){reference-type="ref+label"
reference="eq:maxent_objective"}. We formalize this result in
[2](#lem:policy_improvement){reference-type="ref+label"
reference="lem:policy_improvement"}.

:::: {#lem:policy_improvement .lemma}
**Lemma 2** (Soft Policy Improvement). *Let $\pi_\mathrm{old} \in \Pi$
and let $\pi_\mathrm{new}$ be the optimizer of the minimization problem
defined in
[\[eq:constrainted_policy_fitting\]](#eq:constrainted_policy_fitting){reference-type="ref+label"
reference="eq:constrainted_policy_fitting"}. Then
$Q^{\pi_\mathrm{new}}({\mathbf{s}_t}, {\mathbf{a}_t}) \geq Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\mathbf{a}_t})$
for all
$({\mathbf{s}_t}, {\mathbf{a}_t}) \in \mathcal{S}\times\mathcal{A}$ with
$|\mathcal{A}|<\infty$.*

::: proof
**Proof.* See
[Appendix [8.2](#app:lem_policy_improvement){reference-type="ref"
reference="app:lem_policy_improvement"}](#app:lem_policy_improvement). ◻*
:::
::::

The full soft policy iteration algorithm alternates between the soft
policy evaluation and the soft policy improvement steps, and it will
provably converge to the optimal maximum entropy policy among the
policies in $\Pi$
([1](#the:soft_policy_iteration){reference-type="ref+label"
reference="the:soft_policy_iteration"}). Although this algorithm will
provably find the optimal solution, we can perform it in its exact form
only in the tabular case. Therefore, we will next approximate the
algorithm for continuous domains, where we need to rely on a function
approximator to represent the Q-values, and running the two steps until
convergence would be computationally too expensive. The approximation
gives rise to a new practical algorithm, called soft actor-critic.

:::: {#the:soft_policy_iteration .theorem}
**Theorem 1** (Soft Policy Iteration). *Repeated application of soft
policy evaluation and soft policy improvement from any $\pi\in\Pi$
converges to a policy $\pi^*$ such that
$Q^{\pi^*}({\mathbf{s}_t}, {\mathbf{a}_t}) \geq Q^{\pi}({\mathbf{s}_t}, {\mathbf{a}_t})$
for all $\pi\in \Pi$ and
$({\mathbf{s}_t}, {\mathbf{a}_t}) \in \mathcal{S}\times\mathcal{A}$,
assuming $|\mathcal{A}|<\infty$.*

::: proof
**Proof.* See
[Appendix [8.3](#app:the_soft_policy_iteration){reference-type="ref"
reference="app:the_soft_policy_iteration"}](#app:the_soft_policy_iteration). ◻*
:::
::::

## Soft Actor-Critic

As discussed above, large continuous domains require us to derive a
practical approximation to soft policy iteration. To that end, we will
use function approximators for both the Q-function and the policy, and
instead of running evaluation and improvement to convergence, alternate
between optimizing both networks with stochastic gradient descent. We
will consider a parameterized state value function
$V_{\psi}({\mathbf{s}_t})$, soft Q-function
$Q_\theta({\mathbf{s}_t}, {\mathbf{a}_t})$, and a tractable policy
$\pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t})$. The parameters of these
networks are ${\psi},\ \theta$, and ${\phi}$. For example, the value
functions can be modeled as expressive neural networks, and the policy
as a Gaussian with mean and covariance given by neural networks. We will
next derive update rules for these parameter vectors.

The state value function approximates the soft value. There is no need
in principle to include a separate function approximator for the state
value, since it is related to the Q-function and policy according to
[\[eq:soft_value_function\]](#eq:soft_value_function){reference-type="ref+label"
reference="eq:soft_value_function"}. This quantity can be estimated from
a single action sample from the current policy without introducing a
bias, but in practice, including a separate function approximator for
the soft value can stabilize training and is convenient to train
simultaneously with the other networks. The soft value function is
trained to minimize the squared residual error $$\begin{align}
\label{eq:v_cost}
\resizebox{\columnwidth}{!}{$
J_V({\psi}) = \operatorname{\mathbb{E}}_{{\mathbf{s}_t}\sim \mathcal{D}}\left[\frac{1}{2}\left(V_{\psi}({\mathbf{s}_t}) - \operatorname{\mathbb{E}}_{{\mathbf{a}_t}\sim\pi_{\phi}}\left[Q_\theta({\mathbf{s}_t}, {\mathbf{a}_t}) - \log \pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t})\right]\right)^2\right]\,$}
\end{align}$$ where $\mathcal{D}$ is the distribution of previously
sampled states and actions, or a replay buffer. The gradient of
[\[eq:v_cost\]](#eq:v_cost){reference-type="ref+label"
reference="eq:v_cost"} can be estimated with an unbiased estimator
$$\begin{align}
\resizebox{\columnwidth}{!}{$
\hat \nabla_{\psi}J_V({\psi}) = \nabla_{\psi}V_{\psi}({\mathbf{s}_t}) \left(V_{\psi}({\mathbf{s}_t}) - Q_\theta({\mathbf{s}_t}, {\mathbf{a}_t}) + \log \pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t})\right),$}
\label{eq:v_gradient}
\end{align}$$ where the actions are sampled according to the current
policy, instead of the replay buffer. The soft Q-function parameters can
be trained to minimize the soft Bellman residual $$\begin{align}
J_Q(\theta) = \operatorname{\mathbb{E}}_{({\mathbf{s}_t}, {\mathbf{a}_t})\sim\mathcal{D}}\left[\frac{1}{2}\left(Q_\theta({\mathbf{s}_t}, {\mathbf{a}_t}) - \hat Q({\mathbf{s}_t}, {\mathbf{a}_t})\right)^2\right],
\label{eq:q_cost}
\end{align}$$ with $$\begin{align}
\hat Q({\mathbf{s}_t}, {\mathbf{a}_t}) = r({\mathbf{s}_t}, {\mathbf{a}_t}) + \gamma\operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p}\left[V_{\bar\psi}({\mathbf{s}_{t+1}})\right],
\end{align}$$ which again can be optimized with stochastic gradients
$$\begin{align}
\resizebox{\columnwidth}{!}{$
\hat \nabla_\theta J_Q(\theta) =  \nabla_\theta Q_\theta({\mathbf{a}_t}, {\mathbf{s}_t}) \left(Q_\theta({\mathbf{s}_t}, {\mathbf{a}_t}) - r({\mathbf{s}_t}, {\mathbf{a}_t}) - \gamma V_{\bar\psi}({\mathbf{s}_{t+1}})\right)$}.
\end{align}$$ The update makes use of a target value network
$V_{\bar\psi}$, where $\bar\psi$ can be an exponentially moving average
of the value network weights, which has been shown to stabilize
training [@mnih2015human]. Alternatively, we can update the target
weights to match the current value function weights periodically (see
[11](#app:benchmarks){reference-type="ref+label"
reference="app:benchmarks"}). Finally, the policy parameters can be
learned by directly minimizing the expected KL-divergence in
[\[eq:constrainted_policy_fitting\]](#eq:constrainted_policy_fitting){reference-type="ref+label"
reference="eq:constrainted_policy_fitting"}: $$\begin{align}
J_\pi({\phi}) = \operatorname{\mathbb{E}}_{{\mathbf{s}_t}\sim\mathcal{D}}\left[\mathrm{D_{KL}}\left(\pi_{\phi}({\,\cdot\,}|{\mathbf{s}_t})\;\middle\|\;\frac{\exp\left(Q_\theta({\mathbf{s}_t}, {\,\cdot\,})\right)}{Z_\theta({\mathbf{s}_t})}\right)\right].
\label{eq:policy_objective}
\end{align}$$ There are several options for minimizing $J_\pi$. A
typical solution for policy gradient methods is to use the likelihood
ratio gradient estimator [@williams1992simple], which does not require
backpropagating the gradient through the policy and the target density
networks. However, in our case, the target density is the Q-function,
which is represented by a neural network an can be differentiated, and
it is thus convenient to apply the reparameterization trick instead,
resulting in a lower variance estimator. To that end, we reparameterize
the policy using a neural network transformation $$\begin{align}
{\mathbf{a}_t}= f_{\phi}(\epsilon_t; {\mathbf{s}_t}),
\end{align}$$ where $\epsilon_t$ is an input noise vector, sampled from
some fixed distribution, such as a spherical Gaussian. We can now
rewrite the objective
in [\[eq:policy_objective\]](#eq:policy_objective){reference-type="ref+label"
reference="eq:policy_objective"} as $$\begin{align}
\resizebox{\columnwidth}{!}{$
J_\pi({\phi}) = \operatorname{\mathbb{E}}_{{\mathbf{s}_t}\sim\mathcal{D},\epsilon_t\sim\mathcal{N}}\left[\log \pi_{\phi}(f_{\phi}(\epsilon_t;{\mathbf{s}_t})|{\mathbf{s}_t}) - Q_\theta({\mathbf{s}_t}, f_{\phi}(\epsilon_t;{\mathbf{s}_t}))\right],$}
\label{eq:reparam_objective}
\end{align}$$ where $\pi_{\phi}$ is defined implicitly in terms of
$f_{\phi}$, and we have noted that the partition function is independent
of ${\phi}$ and can thus be omitted. We can approximate the gradient
of [\[eq:reparam_objective\]](#eq:reparam_objective){reference-type="ref+label"
reference="eq:reparam_objective"} with $$\begin{align}
&\hat\nabla_{\phi}J_\pi({\phi}) = \nabla_{\phi}\log \pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t}) \notag\\
&\ \ \ \ \ \ \ + (\nabla_{\mathbf{a}_t}\log \pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t})
- \nabla_{\mathbf{a}_t}Q({\mathbf{s}_t}, {\mathbf{a}_t}))\nabla_{\phi}f_{\phi}(\epsilon_t;{\mathbf{s}_t}),
\label{eq:policy_gradient}
\end{align}$$ where ${\mathbf{a}_t}$ is evaluated at
$f_{\phi}(\epsilon_t; {\mathbf{s}_t})$. This unbiased gradient estimator
extends the DDPG style policy gradients [@lillicrap2015continuous] to
any tractable stochastic policy.

:::: algorithm
::: algorithmic
Initialize parameter vectors ${\psi}$, ${\bar\psi}$, $\theta$, ${\phi}$.
${\mathbf{a}_t}\sim \pi_{\phi}({\mathbf{a}_t}|{\mathbf{s}_t})$
${\mathbf{s}_{t+1}}\sim p({\mathbf{s}_{t+1}}| {\mathbf{s}_t}, {\mathbf{a}_t})$
$\mathcal{D} \leftarrow \mathcal{D} \cup \left\{({\mathbf{s}_t}, {\mathbf{a}_t}, r({\mathbf{s}_t}, {\mathbf{a}_t}), {\mathbf{s}_{t+1}})\right\}$

${\psi}\leftarrow {\psi}- \lambda_V \hat \nabla_{\psi}J_V({\psi})$
$\theta_i \leftarrow \theta_i - \lambda_Q \hat \nabla_{\theta_i} J_Q(\theta_i)$
for $i\in\{1, 2\}$
${\phi}\leftarrow {\phi}- \lambda_\pi\hat \nabla_{\phi}J_\pi({\phi})$
${\bar\psi}\leftarrow \tau {\psi}+ (1-\tau){\bar\psi}$
:::
::::

<figure id="fig:training_curves" data-latex-placement="t">

<figcaption>Training curves on continuous control benchmarks. Soft
actor-critic (yellow) performs consistently across all tasks and
outperforming both on-policy and off-policy methods in the most
challenging tasks.</figcaption>
</figure>

Our algorithm also makes use of two Q-functions to mitigate positive
bias in the policy improvement step that is known to degrade performance
of value based methods [@hasselt2010double; @fujimoto2018addressing]. In
particular, we parameterize two Q-functions, with parameters $\theta_i$,
and train them independently to optimize $J_Q(\theta_i)$. We then use
the minimum of the Q-functions for the value gradient in
[\[eq:v_gradient\]](#eq:v_gradient){reference-type="ref+label"
reference="eq:v_gradient"} and policy gradient in
[\[eq:policy_gradient\]](#eq:policy_gradient){reference-type="ref+label"
reference="eq:policy_gradient"}, as proposed by @fujimoto2018addressing.
Although our algorithm can learn challenging tasks, including a
21-dimensional Humanoid, using just a single Q-function, we found two
Q-functions significantly speed up training, especially on harder tasks.
The complete algorithm is described in
[\[alg:soft_actor_critic\]](#alg:soft_actor_critic){reference-type="ref+label"
reference="alg:soft_actor_critic"}. The method alternates between
collecting experience from the environment with the current policy and
updating the function approximators using the stochastic gradients from
batches sampled from a replay buffer. In practice, we take a single
environment step followed by one or several gradient steps (see
[Appendix [10](#app:hypers){reference-type="ref"
reference="app:hypers"}](#app:hypers) for all hyperparameter). Using
off-policy data from a replay buffer is feasible because both value
estimators and the policy can be trained entirely on off-policy data.
The algorithm is agnostic to the parameterization of the policy, as long
as it can be evaluated for any arbitrary state-action tuple.

# Experiments {#sec:experiments}

The goal of our experimental evaluation is to understand how the sample
complexity and stability of our method compares with prior off-policy
and on-policy deep reinforcement learning algorithms. We compare our
method to prior techniques on a range of challenging continuous control
tasks from the OpenAI gym benchmark suite [@brockman2016openai] and also
on the rllab implementation of the Humanoid
task [@duan2016benchmarking]. Although the easier tasks can be solved by
a wide range of different algorithms, the more complex benchmarks, such
as the 21-dimensional Humanoid (rllab), are exceptionally difficult to
solve with off-policy algorithms [@duan2016benchmarking]. The stability
of the algorithm also plays a large role in performance: easier tasks
make it more practical to tune hyperparameters to achieve good results,
while the already narrow basins of effective hyperparameters become
prohibitively small for the more sensitive algorithms on the hardest
benchmarks, leading to poor performance [@gu2016q].

We compare our method to deep deterministic policy gradient
(DDPG) [@lillicrap2015continuous], an algorithm that is regarded as one
of the more efficient off-policy deep RL
methods [@duan2016benchmarking]; proximal policy optimization
(PPO) [@schulman2017proximal], a stable and effective on-policy policy
gradient algorithm; and soft Q-learning
(SQL) [@haarnoja2017reinforcement], a recent off-policy algorithm for
learning maximum entropy policies. Our SQL implementation also includes
two Q-functions, which we found to improve its performance in most
environments. We additionally compare to twin delayed deep deterministic
policy gradient algorithm (TD3) [@fujimoto2018addressing], using the
author-provided implementation. This is an extension to DDPG, proposed
concurrently to our method, that first applied the double Q-learning
trick to continuous control along with other improvements. We have
included trust region path consistency learning
(Trust-PCL) [@nachum2017trust] and two other variants of SAC in
[11](#app:benchmarks){reference-type="ref+label"
reference="app:benchmarks"}. We turned off the exploration noise for
evaluation for DDPG and PPO. For maximum entropy algorithms, which do
not explicitly inject exploration noise, we either evaluated with the
exploration noise (SQL) or use the mean action (SAC). The source code of
our SAC implementation[^1] and videos[^2] are available online.

## Comparative Evaluation {#sec:evaluation}

[1](#fig:training_curves){reference-type="ref+label"
reference="fig:training_curves"} shows the total average return of
evaluation rollouts during training for DDPG, PPO, and TD3. We train
five different instances of each algorithm with different random seeds,
with each performing one evaluation rollout every 1000 environment
steps. The solid curves corresponds to the mean and the shaded region to
the minimum and maximum returns over the five trials.

The results show that, overall, SAC performs comparably to the baseline
methods on the easier tasks and outperforms them on the harder tasks
with a large margin, both in terms of learning speed and the final
performance. For example, DDPG fails to make any progress on Ant-v1,
Humanoid-v1, and Humanoid (rllab), a result that is corroborated by
prior work [@gu2016q; @duan2016benchmarking]. SAC also learns
considerably faster than PPO as a consequence of the large batch sizes
PPO needs to learn stably on more high-dimensional and complex tasks.
Another maximum entropy RL algorithm, SQL, can also learn all tasks, but
it is slower than SAC and has worse asymptotic performance. The
quantitative results attained by SAC in our experiments also compare
very favorably to results reported by other methods in prior
work [@duan2016benchmarking; @gu2016q; @henderson2017deep], indicating
that both the sample efficiency and final performance of SAC on these
benchmark tasks exceeds the state of the art. All hyperparameters used
in this experiment for SAC are listed in
[Appendix [10](#app:hypers){reference-type="ref"
reference="app:hypers"}](#app:hypers).

## Ablation Study {#sec:ablations}

The results in the previous section suggest that algorithms based on the
maximum entropy principle can outperform conventional RL methods on
challenging tasks such as the humanoid tasks. In this section, we
further examine which particular components of SAC are important for
good performance. We also examine how sensitive SAC is to some of the
most important hyperparameters, namely reward scaling and target value
update smoothing constant.

<figure id="fig:humanoid_seeds">
<div class="centering">
<embed src="figures/benchmarks/seeds-humanoid-rllab.pdf" />
</div>
<figcaption>Comparison of SAC (blue) and a deterministic variant of SAC
(red) in terms of the stability of individual random seeds on the
Humanoid (rllab) benchmark. The comparison indicates that stochasticity
can stabilize training as the variability between the seeds becomes much
higher with a deterministic policy.</figcaption>
</figure>

#### Stochastic vs. deterministic policy.

Soft actor-critic learns stochastic policies via a maximum entropy
objective. The entropy appears in both the policy and value function. In
the policy, it prevents premature convergence of the policy variance
([\[eq:policy_objective\]](#eq:policy_objective){reference-type="ref+label"
reference="eq:policy_objective"}). In the value function, it encourages
exploration by increasing the value of regions of state space that lead
to high-entropy behavior
([\[eq:v_cost\]](#eq:v_cost){reference-type="ref+label"
reference="eq:v_cost"}). To compare how the stochasticity of the policy
and entropy maximization affects the performance, we compare to a
deterministic variant of SAC that does not maximize the entropy and that
closely resembles DDPG, with the exception of having two Q-functions,
using hard target updates, not having a separate target actor, and using
fixed rather than learned exploration noise.
[2](#fig:humanoid_seeds){reference-type="ref+label"
reference="fig:humanoid_seeds"} compares five individual runs with both
variants, initialized with different random seeds. Soft actor-critic
performs much more consistently, while the deterministic variant
exhibits very high variability across seeds, indicating substantially
worse stability. As evident from the figure, learning a stochastic
policy with entropy maximization can drastically stabilize training.
This becomes especially important with harder tasks, where tuning
hyperparameters is challenging. In this comparison, we updated the
target value network weights with hard updates, by periodically
overwriting the target network parameters to match the current value
network (see [11](#app:benchmarks){reference-type="ref+label"
reference="app:benchmarks"} for a comparison of average performance on
all benchmark tasks).

<figure id="fig:sweeps" data-latex-placement="t">

<figcaption>Sensitivity of soft actor-critic to selected hyperparameters
on Ant-v1 task. (a) Evaluating the policy using the mean action
generally results in a higher return. Note that the policy is trained to
maximize also the entropy, and the mean action does not, in general,
correspond the optimal action for the maximum return objective. (b) Soft
actor-critic is sensitive to reward scaling since it is related to the
temperature of the optimal policy. The optimal reward scale varies
between environments, and should be tuned for each task separately. (c)
Target value smoothing coefficient <span
class="math inline"><em>τ</em></span> is used to stabilize training.
Fast moving target (large <span class="math inline"><em>τ</em></span>)
can result in instabilities (red), whereas slow moving target (small
<span class="math inline"><em>τ</em></span>) makes training slower
(blue).</figcaption>
</figure>

#### Policy evaluation.

Since SAC converges to stochastic policies, it is often beneficial to
make the final policy deterministic at the end for best performance. For
evaluation, we approximate the maximum a posteriori action by choosing
the mean of the policy distribution.
[\[fig:evaluation_ant\]](#fig:evaluation_ant){reference-type="ref+label"
reference="fig:evaluation_ant"} compares training returns to evaluation
returns obtained with this strategy indicating that deterministic
evaluation can yield better performance. It should be noted that all of
the training curves depict the sum of rewards, which is different from
the objective optimized by SAC and other maximum entropy RL algorithms,
including SQL and Trust-PCL, which maximize also the entropy of the
policy.

#### Reward scale.

Soft actor-critic is particularly sensitive to the scaling of the reward
signal, because it serves the role of the temperature of the
energy-based optimal policy and thus controls its stochasticity. Larger
reward magnitudes correspond to lower entries.
[\[fig:reward_scale_ant\]](#fig:reward_scale_ant){reference-type="ref+label"
reference="fig:reward_scale_ant"} shows how learning performance changes
when the reward scale is varied: For small reward magnitudes, the policy
becomes nearly uniform, and consequently fails to exploit the reward
signal, resulting in substantial degradation of performance. For large
reward magnitudes, the model learns quickly at first, but the policy
then becomes nearly deterministic, leading to poor local minima due to
lack of adequate exploration. With the right reward scaling, the model
balances exploration and exploitation, leading to faster learning and
better asymptotic performance. In practice, we found reward scale to be
the only hyperparameter that requires tuning, and its natural
interpretation as the inverse of the temperature in the maximum entropy
framework provides good intuition for how to adjust this parameter.

#### Target network update.

It is common to use a separate target value network that slowly tracks
the actual value function to improve stability. We use an exponentially
moving average, with a smoothing constant $\tau$, to update the target
value network weights as common in the prior
work [@lillicrap2015continuous; @mnih2015human]. A value of one
corresponds to a hard update where the weights are copied directly at
every iteration and zero to not updating the target at all. In
[\[fig:soft_target_ant\]](#fig:soft_target_ant){reference-type="ref+label"
reference="fig:soft_target_ant"}, we compare the performance of SAC when
$\tau$ varies. Large $\tau$ can lead to instabilities while small $\tau$
can make training slower. However, we found the range of suitable values
of $\tau$ to be relatively wide and we used the same value (0.005)
across all of the tasks. In
[4](#fig:training_curves_all){reference-type="ref+label"
reference="fig:training_curves_all"}
([11](#app:benchmarks){reference-type="ref+label"
reference="app:benchmarks"}) we also compare to another variant of SAC,
where instead of using exponentially moving average, we copy over the
current network weights directly into the target network every 1000
gradient steps. We found this variant to benefit from taking more than
one gradient step between the environment steps, which can improve
performance but also increases the computational cost.

# Conclusion

We present soft actor-critic (SAC), an off-policy maximum entropy deep
reinforcement learning algorithm that provides sample-efficient learning
while retaining the benefits of entropy maximization and stability. Our
theoretical results derive soft policy iteration, which we show to
converge to the optimal policy. From this result, we can formulate a
soft actor-critic algorithm, and we empirically show that it outperforms
state-of-the-art model-free deep RL methods, including the off-policy
DDPG algorithm and the on-policy PPO algorithm. In fact, the sample
efficiency of this approach actually exceeds that of DDPG by a
substantial margin. Our results suggest that stochastic, entropy
maximizing reinforcement learning algorithms can provide a promising
avenue for improved robustness and stability, and further exploration of
maximum entropy methods, including methods that incorporate second order
information (e.g., trust regions [@schulman2015trust]) or more
expressive policy classes is an exciting avenue for future work.

# Acknowledgments {#acknowledgments .unnumbered}

We would like to thank Vitchyr Pong for insightful discussions and help
in implementing our algorithm as well as providing the DDPG baseline
code; Ofir Nachum for offering support in running Trust-PCL experiments;
and George Tucker for his valuable feedback on an early version of this
paper. This work was supported by Siemens and Berkeley DeepDrive.

# Maximum Entropy Objective {#app:objective}

The exact definition of the discounted maximum entropy objective is
complicated by the fact that, when using a discount factor for policy
gradient methods, we typically do not discount the state distribution,
only the rewards. In that sense, discounted policy gradients typically
do not optimize the true discounted objective. Instead, they optimize
average reward, with the discount serving to reduce variance, as
discussed by @thomas2014bias. However, we can define the objective that
*is* optimized under a discount factor as $$\begin{align}
J(\pi) = \sum_{t=0}^\infty \operatorname{\mathbb{E}}_{({\mathbf{s}_t},{\mathbf{a}_t}) \sim \rho_\pi}\left[ \sum_{l=t}^\infty \gamma^{l-t} \operatorname{\mathbb{E}}_{\mathbf{s}_l\sim p,\mathbf{a}_l\sim\pi}\left[ r({\mathbf{s}_t},{\mathbf{a}_t}) + \alpha \mathcal{H}(\pi({\,\cdot\,}|{\mathbf{s}_t}))|{\mathbf{s}_t},{\mathbf{a}_t}\right]\right].
\end{align}$$ This objective corresponds to maximizing the discounted
expected reward and entropy for future states originating from every
state-action tuple $({\mathbf{s}_t},{\mathbf{a}_t})$ weighted by its
probability $\rho_\pi$ under the current policy.

# Proofs

## [1](#lem:soft_policy_evaluation){reference-type="ref+label" reference="lem:soft_policy_evaluation"} {#app:lem_soft_policy_evaluation}

**[1](#lem:soft_policy_evaluation){reference-type="ref+label"
reference="lem:soft_policy_evaluation"}** (Soft Policy Evaluation).
*Consider the soft Bellman backup operator $\mathcal{T}^\pi$ in
[\[eq:soft_bellman_backup_op\]](#eq:soft_bellman_backup_op){reference-type="ref+label"
reference="eq:soft_bellman_backup_op"} and a mapping
$Q^0: \mathcal{S}\times \mathcal{A}\rightarrow \mathbb{R}$ with
$|\mathcal{A}|<\infty$, and define $Q^{k+1} = \mathcal{T}^\pi Q^k$. Then
the sequence $Q^k$ will converge to the soft Q-value of $\pi$ as
$k\rightarrow \infty$.*

::: proof
*Proof.* Define the entropy augmented reward as
$r_\pi({\mathbf{s}_t}, {\mathbf{a}_t}) \triangleq r({\mathbf{s}_t}, {\mathbf{a}_t})  + \operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p}\left[\mathcal{H}\left(\pi({\,\cdot\,}|{\mathbf{s}_{t+1}})\right)\right]$
and rewrite the update rule as $$\begin{align}
Q({\mathbf{s}_t}, {\mathbf{a}_t}) \leftarrow r_\pi({\mathbf{s}_t}, {\mathbf{a}_t}) + \gamma\operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p,{\mathbf{a}_{t+1}}\sim \pi}\left[Q({\mathbf{s}_{t+1}}, {\mathbf{a}_{t+1}})\right]
\end{align}$$ and apply the standard convergence results for policy
evaluation [@sutton1998reinforcement]. The assumption
$|\mathcal{A}|<\infty$ is required to guarantee that the entropy
augmented reward is bounded. ◻
:::

## [2](#lem:policy_improvement){reference-type="ref+label" reference="lem:policy_improvement"} {#app:lem_policy_improvement}

**[2](#lem:policy_improvement){reference-type="ref+label"
reference="lem:policy_improvement"}** (Soft Policy Improvement). *Let
$\pi_\mathrm{old} \in \Pi$ and let $\pi_\mathrm{new}$ be the optimizer
of the minimization problem defined in
[\[eq:constrainted_policy_fitting\]](#eq:constrainted_policy_fitting){reference-type="ref+label"
reference="eq:constrainted_policy_fitting"}. Then
$Q^{\pi_\mathrm{new}}({\mathbf{s}_t}, {\mathbf{a}_t}) \geq Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\mathbf{a}_t})$
for all
$({\mathbf{s}_t}, {\mathbf{a}_t}) \in \mathcal{S}\times\mathcal{A}$ with
$|\mathcal{A}|<\infty$.*

::: proof
*Proof.* Let ${\pi_\mathrm{old}}\in \Pi$ and let $Q^{\pi_\mathrm{old}}$
and $V^{\pi_\mathrm{old}}$ be the corresponding soft state-action value
and soft state value, and let ${\pi_\mathrm{new}}$ be defined as
$$\begin{align}
{\pi_\mathrm{new}}({\,\cdot\,}|{\mathbf{s}_t}) &= \arg \min_{\pi' \in \Pi}\mathrm{D_{KL}}\left(\pi'({\,\cdot\,}|{\mathbf{s}_t})\;\middle\|\;\exp\left(Q^{\pi_\mathrm{old}}({\mathbf{s}_t},{\,\cdot\,}) - \log Z^{\pi_\mathrm{old}}({\mathbf{s}_t})\right)\right)\notag\\
 &= \arg\min_{\pi'\in\Pi}J_{\pi_\mathrm{old}}(\pi'({\,\cdot\,}|{\mathbf{s}_t})).
\end{align}$$ It must be the case that
$J_{\pi_\mathrm{old}}({\pi_\mathrm{new}}({\,\cdot\,}|{\mathbf{s}_t})) \leq J_{\pi_\mathrm{old}}({\pi_\mathrm{old}}({\,\cdot\,}|{\mathbf{s}_t}))$,
since we can always choose
${\pi_\mathrm{new}}= {\pi_\mathrm{old}}\in\Pi$. Hence $$\begin{align}
\resizebox{1\textwidth}{!}{$
\operatorname{\mathbb{E}}_{{\mathbf{a}_t}\sim{\pi_\mathrm{new}}}\left[\log {\pi_\mathrm{new}}({\mathbf{a}_t}|{\mathbf{s}_t}) - Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\mathbf{a}_t}) + \log Z^{\pi_\mathrm{old}}({\mathbf{s}_t})\right]
\leq \operatorname{\mathbb{E}}_{{\mathbf{a}_t}\sim{\pi_\mathrm{old}}}\left[\log {\pi_\mathrm{old}}({\mathbf{a}_t}|{\mathbf{s}_t}) - Q^{\pi_\mathrm{old}}({\mathbf{s}_t},{\mathbf{a}_t}) + \log Z^{\pi_\mathrm{old}}({\mathbf{s}_t})\right]$},
\end{align}$$ and since partition function $Z^{\pi_\mathrm{old}}$
depends only on the state, the inequality reduces to $$\begin{align}
\operatorname{\mathbb{E}}_{{\mathbf{a}_t}\sim{\pi_\mathrm{new}}}\left[Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\mathbf{a}_t}) - \log {\pi_\mathrm{new}}({\mathbf{a}_t}|{\mathbf{s}_t})\right] \geq V^{\pi_\mathrm{old}}({\mathbf{s}_t}).
\label{eq:soft_value_bound}
\end{align}$$ Next, consider the soft Bellman equation: $$\begin{align}
Q^{\pi_\mathrm{old}}({\mathbf{s}_t}, {\mathbf{a}_t}) &= r({\mathbf{s}_t}, {\mathbf{a}_t}) + \gamma\operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p}\left[V^{\pi_\mathrm{old}}({\mathbf{s}_{t+1}})\right]\notag\\
&\leq r({\mathbf{s}_t}, {\mathbf{a}_t}) + \gamma\operatorname{\mathbb{E}}_{{\mathbf{s}_{t+1}}\sim p}\left[\operatorname{\mathbb{E}}_{{\mathbf{a}_{t+1}}\sim{\pi_\mathrm{new}}}\left[Q^{\pi_\mathrm{old}}({\mathbf{s}_{t+1}}, {\mathbf{a}_{t+1}}) - \log {\pi_\mathrm{new}}({\mathbf{a}_{t+1}}|{\mathbf{s}_{t+1}})\right]\right]\notag\\
&\ \  \vdots\notag\\
& \leq Q^{\pi_\mathrm{new}}({\mathbf{s}_t}, {\mathbf{a}_t}),
\end{align}$$ where we have repeatedly expanded $Q^{\pi_\mathrm{old}}$
on the RHS by applying the soft Bellman equation and the bound in
[\[eq:soft_value_bound\]](#eq:soft_value_bound){reference-type="ref+label"
reference="eq:soft_value_bound"}. Convergence to $Q^{\pi_\mathrm{new}}$
follows from [1](#lem:soft_policy_evaluation){reference-type="ref+label"
reference="lem:soft_policy_evaluation"}. ◻
:::

## [1](#the:soft_policy_iteration){reference-type="ref+label" reference="the:soft_policy_iteration"} {#app:the_soft_policy_iteration}

**[1](#the:soft_policy_iteration){reference-type="ref+label"
reference="the:soft_policy_iteration"}** (Soft Policy Iteration).
*Repeated application of soft policy evaluation and soft policy
improvement to any $\pi\in\Pi$ converges to a policy $\pi^*$ such that
$Q^{\pi^*}({\mathbf{s}_t}, {\mathbf{a}_t}) \geq Q^{\pi}({\mathbf{s}_t}, {\mathbf{a}_t})$
for all $\pi\in \Pi$ and
$({\mathbf{s}_t}, {\mathbf{a}_t}) \in \mathcal{S}\times\mathcal{A}$,
assuming $|\mathcal{A}|<\infty$.*

::: proof
*Proof.* Let $\pi_i$ be the policy at iteration $i$. By
[2](#lem:policy_improvement){reference-type="ref+label"
reference="lem:policy_improvement"}, the sequence $Q^{\pi_i}$ is
monotonically increasing. Since $Q^\pi$ is bounded above for
$\pi\in \Pi$ (both the reward and entropy are bounded), the sequence
converges to some $\pi^*$. We will still need to show that $\pi^*$ is
indeed optimal. At convergence, it must be case that
$J_{\pi^*}({\pi^*}({\,\cdot\,}|{\mathbf{s}_t})) < J_{\pi^*}(\pi({\,\cdot\,}|{\mathbf{s}_t}))$
for all $\pi\in\Pi$, $\pi\neq \pi^*$. Using the same iterative argument
as in the proof of
[2](#lem:policy_improvement){reference-type="ref+label"
reference="lem:policy_improvement"}, we get
$Q^{\pi^*}({\mathbf{s}_t}, {\mathbf{a}_t}) > Q^\pi({\mathbf{s}_t}, {\mathbf{a}_t})$
for all
$({\mathbf{s}_t}, {\mathbf{a}_t})\in \mathcal{S}\times\mathcal{A}$, that
is, the soft value of any other policy in $\Pi$ is lower than that of
the converged policy. Hence ${\pi^*}$ is optimal in $\Pi$. ◻
:::

# Enforcing Action Bounds {#app:action_bounds}

We use an unbounded Gaussian as the action distribution. However, in
practice, the actions needs to be bounded to a finite interval. To that
end, we apply an invertible squashing function ($\tanh$) to the Gaussian
samples, and employ the change of variables formula to compute the
likelihoods of the bounded actions. In the other words, let
$\mathbf{u}\in\mathbb{R}^D$ be a random variable and
$\mu(\mathbf{u}|\mathbf{s})$ the corresponding density with infinite
support. Then $\mathbf{a}= \tanh(\mathbf{u})$, where $\tanh$ is applied
elementwise, is a random variable with support in $(-1, 1)$ with a
density given by $$\begin{align}
\pi(\mathbf{a}|\mathbf{s}) &= \mu(\mathbf{u}|\mathbf{s})\left|\det \left(\frac{\mathrm{d}\mathbf{a}}{\mathrm{d}\mathbf{u}} \right)\right|^{-1}.
\end{align}$$ Since the Jacobian
$\nicefrac{\mathrm{d}\mathbf{a}}{\mathrm{d}\mathbf{u}} = \mathrm{diag}(1 - \tanh^2(\mathbf{u}))$
is diagonal, the log-likelihood has a simple form $$\begin{align}
\log\pi(\mathbf{a}|\mathbf{s}) &= \log \mu(\mathbf{u}|\mathbf{s}) - \sum_{i=1}^D\log\left(1 - \tanh^2(u_i)\right),
\end{align}$$ where $u_i$ is the $i^\mathrm{th}$ element of
$\mathbf{u}$.

# Hyperparameters {#app:hypers}

[1](#tab:shared_params){reference-type="ref+label"
reference="tab:shared_params"} lists the common SAC parameters used in
the comparative evaluation in
[1](#fig:training_curves){reference-type="ref+label"
reference="fig:training_curves"} and
[4](#fig:training_curves_all){reference-type="ref+label"
reference="fig:training_curves_all"}.
[2](#tab:env_params){reference-type="ref+label"
reference="tab:env_params"} lists the reward scale parameter that was
tuned for each environment.

::: {#tab:shared_params}
+------------------------------------------+--------------------------+
| Parameter                                | Value                    |
+:==============+:=========================+:=========================+
| *Shared*                                 |                          |
+---------------+--------------------------+--------------------------+
|               | optimizer                | Adam [@kingma2014adam]   |
+---------------+--------------------------+--------------------------+
|               | learning rate            | $3 \cdot 10^{-4}$        |
+---------------+--------------------------+--------------------------+
|               | discount ($\gamma$)      | 0.99                     |
+---------------+--------------------------+--------------------------+
|               | replay buffer size       | $10^6$                   |
+---------------+--------------------------+--------------------------+
|               | number of hidden layers  | 2                        |
|               | (all networks)           |                          |
+---------------+--------------------------+--------------------------+
|               | number of hidden units   | 256                      |
|               | per layer                |                          |
+---------------+--------------------------+--------------------------+
|               | number of samples per    | 256                      |
|               | minibatch                |                          |
+---------------+--------------------------+--------------------------+
|               | nonlinearity             | ReLU                     |
+---------------+--------------------------+--------------------------+
| *SAC*                                    |                          |
+---------------+--------------------------+--------------------------+
|               | target smoothing         | 0.005                    |
|               | coefficient ($\tau$)     |                          |
+---------------+--------------------------+--------------------------+
|               | target update interval   | 1                        |
+---------------+--------------------------+--------------------------+
|               | gradient steps           | 1                        |
+---------------+--------------------------+--------------------------+
| *SAC (hard target update)*               |                          |
+---------------+--------------------------+--------------------------+
|               | target smoothing         | 1                        |
|               | coefficient ($\tau$)     |                          |
+---------------+--------------------------+--------------------------+
|               | target update interval   | 1000                     |
+---------------+--------------------------+--------------------------+
|               | gradient steps (except   | 4                        |
|               | humanoids)               |                          |
+---------------+--------------------------+--------------------------+
|               | gradient steps           | 1                        |
|               | (humanoids)              |                          |
+---------------+--------------------------+--------------------------+

: SAC Hyperparameters
:::

::: {#tab:env_params}
  Environment        Action Dimensions   Reward Scale      
  ------------------ ------------------- -------------- -- --
  Hopper-v1          3                   5                 
  Walker2d-v1        6                   5                 
  HalfCheetah-v1     6                   5                 
  Ant-v1             8                   5                 
  Humanoid-v1        17                  20                
  Humanoid (rllab)   21                  10                

  : SAC Environment Specific Parameters
:::

# Additional Baseline Results {#app:benchmarks}

[4](#fig:training_curves_all){reference-type="ref+label"
reference="fig:training_curves_all"} compares SAC to Trust-PCL
([4](#fig:training_curves_all){reference-type="ref+label"
reference="fig:training_curves_all"}. Trust-PC fails to solve most of
the task within the given number of environment steps, although it can
eventually solve the easier tasks [@nachum2017trust] if ran longer. The
figure also includes two variants of SAC: a variant that periodically
copies the target value network weights directly instead of using
exponentially moving average, and a deterministic ablation which assumes
a deterministic policy in the value update
([\[eq:v_gradient\]](#eq:v_gradient){reference-type="ref+label"
reference="eq:v_gradient"}) and the policy update
([\[eq:policy_gradient\]](#eq:policy_gradient){reference-type="ref+label"
reference="eq:policy_gradient"}), and thus strongly resembles DDPG with
the exception of having two Q-functions, using hard target updates, not
having a separate target actor, and using fixed exploration noise rather
than learned. Both of these methods can learn all of the tasks and they
perform comparably to SAC on all but Humanoid (rllab) task, on which SAC
is the fastest.

<figure id="fig:training_curves_all" data-latex-placement="h">

<figcaption>Training curves for additional baseline (Trust-PCL) and for
two SAC variants. Soft actor-critic with hard target update (blue)
differs from standard SAC in that it copies the value function network
weights directly every 1000 iterations, instead of using exponentially
smoothed average of the weights. The deterministic ablation (red) uses a
deterministic policy with fixed Gaussian exploration noise, does not use
a value function, drops the entropy terms in the actor and critic
function updates, and uses hard target updates for the target
Q-functions. It is equivalent to DDPG that uses two Q-functions, hard
target updates, and removes the target actor.</figcaption>
</figure>

[^1]: [github.com/haarnoja/sac](http://github.com/haarnoja/sac)

[^2]: [sites.google.com/view/soft-actor-critic](sites.google.com/view/soft-actor-critic)
