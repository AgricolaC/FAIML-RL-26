[]{#index.xhtml}

::::::::::: {.body role="main"}
::::::::: {#index.xhtml_welcome-to-spinning-up-in-deep-rl .section}
# Welcome to Spinning Up in Deep RL!

![](_images/spinning-up-in-rl.png)

::: {.toctree-wrapper .compound}
[User Documentation]{.caption-text}

- [Introduction](user/introduction.xhtml){.reference .internal}
  - [What This Is](#introduction.xhtml_what-this-is){.reference
    .internal}
  - [Why We Built
    This](#introduction.xhtml_why-we-built-this){.reference .internal}
  - [How This Serves Our
    Mission](#introduction.xhtml_how-this-serves-our-mission){.reference
    .internal}
  - [Code Design
    Philosophy](#introduction.xhtml_code-design-philosophy){.reference
    .internal}
  - [Long-Term Support and Support
    History](#introduction.xhtml_long-term-support-and-support-history){.reference
    .internal}
- [Installation](user/installation.xhtml){.reference .internal}
  - [Installing
    Python](#installation.xhtml_installing-python){.reference .internal}
  - [Installing
    OpenMPI](#installation.xhtml_installing-openmpi){.reference
    .internal}
  - [Installing Spinning
    Up](#installation.xhtml_installing-spinning-up){.reference
    .internal}
  - [Check Your
    Install](#installation.xhtml_check-your-install){.reference
    .internal}
  - [Installing MuJoCo
    (Optional)](#installation.xhtml_installing-mujoco-optional){.reference
    .internal}
- [Algorithms](user/algorithms.xhtml){.reference .internal}
  - [What's Included](#algorithms.xhtml_what-s-included){.reference
    .internal}
  - [Why These
    Algorithms?](#algorithms.xhtml_why-these-algorithms){.reference
    .internal}
  - [Code Format](#algorithms.xhtml_code-format){.reference .internal}
- [Running Experiments](user/running.xhtml){.reference .internal}
  - [Launching from the Command
    Line](#running.xhtml_launching-from-the-command-line){.reference
    .internal}
  - [Launching from
    Scripts](#running.xhtml_launching-from-scripts){.reference
    .internal}
- [Experiment Outputs](user/saving_and_loading.xhtml){.reference
  .internal}
  - [Algorithm
    Outputs](#saving_and_loading.xhtml_algorithm-outputs){.reference
    .internal}
  - [Save Directory
    Location](#saving_and_loading.xhtml_save-directory-location){.reference
    .internal}
  - [Loading and Running Trained
    Policies](#saving_and_loading.xhtml_loading-and-running-trained-policies){.reference
    .internal}
- [Plotting Results](user/plotting.xhtml){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Introduction to RL]{.caption-text}

- [Part 1: Key Concepts in RL](spinningup/rl_intro.xhtml){.reference
  .internal}
  - [What Can RL Do?](#rl_intro.xhtml_what-can-rl-do){.reference
    .internal}
  - [Key Concepts and
    Terminology](#rl_intro.xhtml_key-concepts-and-terminology){.reference
    .internal}
  - [(Optional)
    Formalism](#rl_intro.xhtml_optional-formalism){.reference .internal}
- [Part 2: Kinds of RL
  Algorithms](spinningup/rl_intro2.xhtml){.reference .internal}
  - [A Taxonomy of RL
    Algorithms](#rl_intro2.xhtml_a-taxonomy-of-rl-algorithms){.reference
    .internal}
  - [Links to Algorithms in
    Taxonomy](#rl_intro2.xhtml_links-to-algorithms-in-taxonomy){.reference
    .internal}
- [Part 3: Intro to Policy
  Optimization](spinningup/rl_intro3.xhtml){.reference .internal}
  - [Deriving the Simplest Policy
    Gradient](#rl_intro3.xhtml_deriving-the-simplest-policy-gradient){.reference
    .internal}
  - [Implementing the Simplest Policy
    Gradient](#rl_intro3.xhtml_implementing-the-simplest-policy-gradient){.reference
    .internal}
  - [Expected Grad-Log-Prob
    Lemma](#rl_intro3.xhtml_expected-grad-log-prob-lemma){.reference
    .internal}
  - [Don't Let the Past Distract
    You](#rl_intro3.xhtml_don-t-let-the-past-distract-you){.reference
    .internal}
  - [Implementing Reward-to-Go Policy
    Gradient](#rl_intro3.xhtml_implementing-reward-to-go-policy-gradient){.reference
    .internal}
  - [Baselines in Policy
    Gradients](#rl_intro3.xhtml_baselines-in-policy-gradients){.reference
    .internal}
  - [Other Forms of the Policy
    Gradient](#rl_intro3.xhtml_other-forms-of-the-policy-gradient){.reference
    .internal}
  - [Recap](#rl_intro3.xhtml_recap){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Resources]{.caption-text}

- [Spinning Up as a Deep RL
  Researcher](spinningup/spinningup.xhtml){.reference .internal}
  - [The Right
    Background](#spinningup.xhtml_the-right-background){.reference
    .internal}
  - [Learn by Doing](#spinningup.xhtml_learn-by-doing){.reference
    .internal}
  - [Developing a Research
    Project](#spinningup.xhtml_developing-a-research-project){.reference
    .internal}
  - [Doing Rigorous Research in
    RL](#spinningup.xhtml_doing-rigorous-research-in-rl){.reference
    .internal}
  - [Closing Thoughts](#spinningup.xhtml_closing-thoughts){.reference
    .internal}
  - [PS: Other
    Resources](#spinningup.xhtml_ps-other-resources){.reference
    .internal}
  - [References](#spinningup.xhtml_references){.reference .internal}
- [Key Papers in Deep RL](spinningup/keypapers.xhtml){.reference
  .internal}
  - [1. Model-Free RL](#keypapers.xhtml_model-free-rl){.reference
    .internal}
  - [2. Exploration](#keypapers.xhtml_exploration){.reference .internal}
  - [3. Transfer and Multitask
    RL](#keypapers.xhtml_transfer-and-multitask-rl){.reference
    .internal}
  - [4. Hierarchy](#keypapers.xhtml_hierarchy){.reference .internal}
  - [5. Memory](#keypapers.xhtml_memory){.reference .internal}
  - [6. Model-Based RL](#keypapers.xhtml_model-based-rl){.reference
    .internal}
  - [7. Meta-RL](#keypapers.xhtml_meta-rl){.reference .internal}
  - [8. Scaling RL](#keypapers.xhtml_scaling-rl){.reference .internal}
  - [9. RL in the Real
    World](#keypapers.xhtml_rl-in-the-real-world){.reference .internal}
  - [10. Safety](#keypapers.xhtml_safety){.reference .internal}
  - [11. Imitation Learning and Inverse Reinforcement
    Learning](#keypapers.xhtml_imitation-learning-and-inverse-reinforcement-learning){.reference
    .internal}
  - [12. Reproducibility, Analysis, and
    Critique](#keypapers.xhtml_reproducibility-analysis-and-critique){.reference
    .internal}
  - [13. Bonus: Classic Papers in RL Theory or
    Review](#keypapers.xhtml_bonus-classic-papers-in-rl-theory-or-review){.reference
    .internal}
- [Exercises](spinningup/exercises.xhtml){.reference .internal}
  - [Problem Set 1: Basics of
    Implementation](#exercises.xhtml_problem-set-1-basics-of-implementation){.reference
    .internal}
  - [Problem Set 2: Algorithm Failure
    Modes](#exercises.xhtml_problem-set-2-algorithm-failure-modes){.reference
    .internal}
  - [Challenges](#exercises.xhtml_challenges){.reference .internal}
- [Benchmarks for Spinning Up
  Implementations](spinningup/bench.xhtml){.reference .internal}
  - [Performance in Each
    Environment](#bench.xhtml_performance-in-each-environment){.reference
    .internal}
  - [Experiment Details](#bench.xhtml_experiment-details){.reference
    .internal}
  - [PyTorch vs
    Tensorflow](#bench.xhtml_pytorch-vs-tensorflow){.reference
    .internal}
:::

::: {.toctree-wrapper .compound}
[Algorithms Docs]{.caption-text}

- [Vanilla Policy Gradient](algorithms/vpg.xhtml){.reference .internal}
  - [Background](#vpg.xhtml_background){.reference .internal}
  - [Documentation](#vpg.xhtml_documentation){.reference .internal}
  - [References](#vpg.xhtml_references){.reference .internal}
- [Trust Region Policy Optimization](algorithms/trpo.xhtml){.reference
  .internal}
  - [Background](#trpo.xhtml_background){.reference .internal}
  - [Documentation](#trpo.xhtml_documentation){.reference .internal}
  - [References](#trpo.xhtml_references){.reference .internal}
- [Proximal Policy Optimization](algorithms/ppo.xhtml){.reference
  .internal}
  - [Background](#ppo.xhtml_background){.reference .internal}
  - [Documentation](#ppo.xhtml_documentation){.reference .internal}
  - [References](#ppo.xhtml_references){.reference .internal}
- [Deep Deterministic Policy Gradient](algorithms/ddpg.xhtml){.reference
  .internal}
  - [Background](#ddpg.xhtml_background){.reference .internal}
  - [Documentation](#ddpg.xhtml_documentation){.reference .internal}
  - [References](#ddpg.xhtml_references){.reference .internal}
- [Twin Delayed DDPG](algorithms/td3.xhtml){.reference .internal}
  - [Background](#td3.xhtml_background){.reference .internal}
  - [Documentation](#td3.xhtml_documentation){.reference .internal}
  - [References](#td3.xhtml_references){.reference .internal}
- [Soft Actor-Critic](algorithms/sac.xhtml){.reference .internal}
  - [Background](#sac.xhtml_background){.reference .internal}
  - [Documentation](#sac.xhtml_documentation){.reference .internal}
  - [References](#sac.xhtml_references){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Utilities Docs]{.caption-text}

- [Logger](utils/logger.xhtml){.reference .internal}
  - [Using a Logger](#logger.xhtml_using-a-logger){.reference .internal}
  - [Logger Classes](#logger.xhtml_logger-classes){.reference .internal}
  - [Loading Saved Models (PyTorch
    Only)](#logger.xhtml_loading-saved-models-pytorch-only){.reference
    .internal}
  - [Loading Saved Graphs (Tensorflow
    Only)](#logger.xhtml_loading-saved-graphs-tensorflow-only){.reference
    .internal}
- [Plotter](utils/plotter.xhtml){.reference .internal}
- [MPI Tools](utils/mpi.xhtml){.reference .internal}
  - [Core MPI
    Utilities](#mpi.xhtml_module-spinup.utils.mpi_tools){.reference
    .internal}
  - [MPI + PyTorch
    Utilities](#mpi.xhtml_mpi-pytorch-utilities){.reference .internal}
  - [MPI + Tensorflow
    Utilities](#mpi.xhtml_mpi-tensorflow-utilities){.reference
    .internal}
- [Run Utils](utils/run_utils.xhtml){.reference .internal}
  - [ExperimentGrid](#run_utils.xhtml_experimentgrid){.reference
    .internal}
  - [Calling
    Experiments](#run_utils.xhtml_calling-experiments){.reference
    .internal}
:::

::: {.toctree-wrapper .compound}
[Etc.]{.caption-text}

- [Acknowledgements](etc/acknowledgements.xhtml){.reference .internal}
- [About the Author](etc/author.xhtml){.reference .internal}
:::
:::::::::

::: {#index.xhtml_indices-and-tables .section}
# Indices and tables

- [[Index]{.std .std-ref}](#genindex.xhtml){.reference .internal}
- [[Module Index]{.std .std-ref}](#py-modindex.xhtml){.reference
  .internal}
- [[Search Page]{.std .std-ref}](search.xhtml){.reference .internal}
:::
:::::::::::

[]{#introduction.xhtml}

:::::::::: {.body role="main"}
::::::::: {#introduction.xhtml_introduction .section}
# [Introduction](#introduction.xhtml_id2){.toc-backref}

::: {#introduction.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Introduction](#introduction.xhtml_introduction){#introduction.xhtml_id2
  .reference .internal}
  - [What This
    Is](#introduction.xhtml_what-this-is){#introduction.xhtml_id3
    .reference .internal}
  - [Why We Built
    This](#introduction.xhtml_why-we-built-this){#introduction.xhtml_id4
    .reference .internal}
  - [How This Serves Our
    Mission](#introduction.xhtml_how-this-serves-our-mission){#introduction.xhtml_id5
    .reference .internal}
  - [Code Design
    Philosophy](#introduction.xhtml_code-design-philosophy){#introduction.xhtml_id6
    .reference .internal}
  - [Long-Term Support and Support
    History](#introduction.xhtml_long-term-support-and-support-history){#introduction.xhtml_id7
    .reference .internal}
:::

::: {#introduction.xhtml_what-this-is .section}
## [What This Is](#introduction.xhtml_id3){.toc-backref}

Welcome to Spinning Up in Deep RL! This is an educational resource
produced by OpenAI that makes it easier to learn about deep
reinforcement learning (deep RL).

For the unfamiliar: [reinforcement
learning](https://en.wikipedia.org/wiki/Reinforcement_learning){.reference
.external}[
\[https://en.wikipedia.org/wiki/Reinforcement_learning\]]{.link-target}
(RL) is a machine learning approach for teaching agents how to solve
tasks by trial and error. Deep RL refers to the combination of RL with
[deep learning](http://ufldl.stanford.edu/tutorial/){.reference
.external}[ \[http://ufldl.stanford.edu/tutorial/\]]{.link-target}.

This module contains a variety of helpful resources, including:

- a short [introduction](../spinningup/rl_intro.html){.reference
  .external} to RL terminology, kinds of algorithms, and basic theory,
- an [essay](../spinningup/spinningup.html){.reference .external} about
  how to grow into an RL research role,
- a [curated list](../spinningup/keypapers.html){.reference .external}
  of important papers organized by topic,
- a well-documented [code
  repo](https://github.com/openai/spinningup){.reference .external}[
  \[https://github.com/openai/spinningup\]]{.link-target} of short,
  standalone implementations of key algorithms,
- and a few [exercises](../spinningup/exercises.html){.reference
  .external} to serve as warm-ups.
:::

::: {#introduction.xhtml_why-we-built-this .section}
## [Why We Built This](#introduction.xhtml_id4){.toc-backref}

One of the single most common questions that we hear is

> ::::: {}
> :::: line-block
> ::: line
> If I want to contribute to AI safety, how do I get started?
> :::
> ::::
> :::::

At OpenAI, we believe that deep learning generally---and deep
reinforcement learning specifically---will play central roles in the
development of powerful AI technology. To ensure that AI is safe, we
have to come up with safety strategies and algorithms that are
compatible with this paradigm. As a result, we encourage everyone who
asks this question to study these fields.

However, while there are many resources to help people quickly ramp up
on deep learning, deep reinforcement learning is more challenging to
break into. To begin with, a student of deep RL needs to have some
background in math, coding, and regular deep learning. Beyond that, they
need both a high-level view of the field---an awareness of what topics
are studied in it, why they matter, and what's been done already---and
careful instruction on how to connect algorithm theory to algorithm
code.

The high-level view is hard to come by because of how new the field is.
There is not yet a standard deep RL textbook, so most of the knowledge
is locked up in either papers or lecture series, which can take a long
time to parse and digest. And learning to implement deep RL algorithms
is typically painful, because either

- the paper that publishes an algorithm omits or inadvertently obscures
  key design details,
- or widely-public implementations of an algorithm are hard to read,
  hiding how the code lines up with the algorithm.

While fantastic repos like
[garage](https://github.com/rlworkgroup/garage){.reference .external}[
\[https://github.com/rlworkgroup/garage\]]{.link-target},
[Baselines](https://github.com/openai/baselines){.reference .external}[
\[https://github.com/openai/baselines\]]{.link-target}, and
[rllib](https://github.com/ray-project/ray/tree/master/python/ray/rllib){.reference
.external}[
\[https://github.com/ray-project/ray/tree/master/python/ray/rllib\]]{.link-target}
make it easier for researchers who are already in the field to make
progress, they build algorithms into frameworks in ways that involve
many non-obvious choices and trade-offs, which makes them hard to learn
from. Consequently, the field of deep RL has a pretty high barrier to
entry---for new researchers as well as practitioners and hobbyists.

So our package here is designed to serve as the missing middle step for
people who are excited by deep RL, and would like to learn how to use it
or make a contribution, but don't have a clear sense of what to study or
how to transmute algorithms into code. We've tried to make this as
helpful a launching point as possible.

That said, practitioners aren't the only people who can (or should)
benefit from these materials. Solving AI safety will require people with
a wide range of expertise and perspectives, and many relevant
professions have no connection to engineering or computer science at
all. Nonetheless, everyone involved will need to learn enough about the
technology to make informed decisions, and several pieces of Spinning Up
address that need.
:::

::: {#introduction.xhtml_how-this-serves-our-mission .section}
## [How This Serves Our Mission](#introduction.xhtml_id5){.toc-backref}

OpenAI's [mission](https://blog.openai.com/openai-charter/){.reference
.external}[ \[https://blog.openai.com/openai-charter/\]]{.link-target}
is to ensure the safe development of AGI and the broad distribution of
benefits from AI more generally. Teaching tools like Spinning Up help us
make progress on both of these objectives.

To begin with, we move closer to broad distribution of benefits any time
we help people understand what AI is and how it works. This empowers
people to think critically about the many issues we anticipate will
arise as AI becomes more sophisticated and important in our lives.

Also, critically, [we need people to
help](https://jobs.lever.co/openai){.reference .external}[
\[https://jobs.lever.co/openai\]]{.link-target} us work on making sure
that AGI is safe. This requires a skill set which is currently in short
supply because of how new the field is. We know that many people are
interested in helping us, but don't know how---here is what you should
study! If you can become an expert on this material, you can make a
difference on AI safety.
:::

::: {#introduction.xhtml_code-design-philosophy .section}
## [Code Design Philosophy](#introduction.xhtml_id6){.toc-backref}

The algorithm implementations in the Spinning Up repo are designed to be

> ::: {}
> - as simple as possible while still being reasonably good,
> - and highly-consistent with each other to expose fundamental
>   similarities between algorithms.
> :::

They are almost completely self-contained, with virtually no common code
shared between them (except for logging, saving, loading, and
[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface){.reference
.external}[
\[https://en.wikipedia.org/wiki/Message_Passing_Interface\]]{.link-target}
utilities), so that an interested person can study each algorithm
separately without having to dig through an endless chain of
dependencies to see how something is done. The implementations are
patterned so that they come as close to pseudocode as possible, to
minimize the gap between theory and code.

Importantly, they're all structured similarly, so if you clearly
understand one, jumping into the next is painless.

We tried to minimize the number of tricks used in each algorithm's
implementation, and minimize the differences between otherwise-similar
algorithms. To give some examples of removed tricks: we omit
[regularization](https://github.com/haarnoja/sac/blob/108a4229be6f040360fcca983113df9c4ac23a6a/sac/distributions/normal.py#L69){.reference
.external}[
\[https://github.com/haarnoja/sac/blob/108a4229be6f040360fcca983113df9c4ac23a6a/sac/distributions/normal.py#L69\]]{.link-target}
terms present in the original Soft-Actor Critic code, as well as
[observation
normalization](https://github.com/openai/baselines/blob/28aca637d0f13f4415cc5ebb778144154cff3110/baselines/run.py#L131){.reference
.external}[
\[https://github.com/openai/baselines/blob/28aca637d0f13f4415cc5ebb778144154cff3110/baselines/run.py#L131\]]{.link-target}
from all algorithms. For an example of where we've removed differences
between algorithms: our implementations of DDPG, TD3, and SAC all follow
a convention of running gradient descent updates after fixed intervals
of environment interaction. (By contrast, other public implementations
of these algorithms usually take slightly different approaches from each
other, making them a little bit harder to compare.)

All algorithms are "reasonably good" in the sense that they achieve
roughly the intended performance, but don't necessarily match the best
reported results in the literature on every task. Consequently, be
careful if using any of these implementations for scientific
benchmarking comparisons. Details on each implementation's specific
performance level can be found on our
[benchmarks](../spinningup/bench.html){.reference .external} page.
:::

::: {#introduction.xhtml_long-term-support-and-support-history .section}
## [Long-Term Support and Support History](#introduction.xhtml_id7){.toc-backref}

Spinning Up is currently in maintenance mode. If there are any breaking
bugs, we'll repair them to ensure that Spinning Up can continue to help
people study deep RL.

Support history so far:

- **Nov 8, 2018:** Initial release!

- **Nov, 2018:** Release was followed by a three-week period of
  high-bandwidth support.

- **April, 2019:** Approximately six months after release, we conducted
  an internal review of Spinning Up based on feedback from the
  community. The review surfaced interest in a few key features:

  > ::: {}
  > - **Implementations in Other Neural Network Libraries.** Several
  >   people expressed interest in seeing Spinning Up use alternatives
  >   to Tensorflow v1 for the RL implementations. A few members of the
  >   community even developed their own PyTorch versions of Spinning Up
  >   algorithms, such as Kashif Rasul's [Fired
  >   Up](https://github.com/kashif/firedup){.reference .external}[
  >   \[https://github.com/kashif/firedup\]]{.link-target}, Kai
  >   Arulkumaran's [Spinning Up
  >   Basic](https://github.com/Kaixhin/spinning-up-basic){.reference
  >   .external}[
  >   \[https://github.com/Kaixhin/spinning-up-basic\]]{.link-target},
  >   and Misha Laskin's [Torching
  >   Up](https://github.com/MishaLaskin/torchingup){.reference
  >   .external}[
  >   \[https://github.com/MishaLaskin/torchingup\]]{.link-target}. As a
  >   result, making this kind of "Rosetta Stone" for deep RL became a
  >   high priority for future work.
  > - **Open Source RL Environments.** Many people expressed an interest
  >   in seeing Spinning Up use more open source RL environments (eg
  >   [PyBullet](https://pybullet.org/wordpress/){.reference .external}[
  >   \[https://pybullet.org/wordpress/\]]{.link-target}) for
  >   benchmarks, examples, and exercises.
  > - **More Algorithms.** There was some interest in seeing other
  >   algorithms included in Spinning Up, especially Deep Q-Networks.
  > :::

- **Jan, 2020:** The PyTorch update to Spinning Up was released!

- **Future:** No major updates are currently planned for Spinning Up. In
  the event it makes sense for us to release an additional update,
  following what we found in the 6-month review, the next-highest
  priority features are to focus more on open source RL environments and
  adding algorithms.

Additionally, as discussed in the blog post, Spinning Up has been
integrated into the curriculum for our
[Scholars](https://openai.com/blog/openai-scholars-spring-2020/){.reference
.external}[
\[https://openai.com/blog/openai-scholars-spring-2020/\]]{.link-target}
and
[Fellows](https://openai.com/blog/openai-fellows-fall-2018/){.reference
.external}[
\[https://openai.com/blog/openai-fellows-fall-2018/\]]{.link-target}
programs.
:::
:::::::::
::::::::::

[]{#installation.xhtml}

:::::::::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::::::::: {#installation.xhtml_installation .section}
# [Installation](#installation.xhtml_id3){.toc-backref}

::: {#installation.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Installation](#installation.xhtml_installation){#installation.xhtml_id3
  .reference .internal}
  - [Installing
    Python](#installation.xhtml_installing-python){#installation.xhtml_id4
    .reference .internal}
  - [Installing
    OpenMPI](#installation.xhtml_installing-openmpi){#installation.xhtml_id5
    .reference .internal}
    - [Ubuntu](#installation.xhtml_ubuntu){#installation.xhtml_id6
      .reference .internal}
    - [Mac OS X](#installation.xhtml_mac-os-x){#installation.xhtml_id7
      .reference .internal}
  - [Installing Spinning
    Up](#installation.xhtml_installing-spinning-up){#installation.xhtml_id8
    .reference .internal}
  - [Check Your
    Install](#installation.xhtml_check-your-install){#installation.xhtml_id9
    .reference .internal}
  - [Installing MuJoCo
    (Optional)](#installation.xhtml_installing-mujoco-optional){#installation.xhtml_id10
    .reference .internal}
:::

Spinning Up requires Python3, OpenAI Gym, and OpenMPI.

Spinning Up is currently only supported on Linux and OSX. It may be
possible to install on Windows, though this hasn't been extensively
tested. [\[1\]](#installation.xhtml_id2){#installation.xhtml_id1
.footnote-reference}

::: {.admonition-you-should-know .admonition}
You Should Know

Many examples and benchmarks in Spinning Up refer to RL environments
that use the [MuJoCo](http://www.mujoco.org/index.html){.reference
.external}[ \[http://www.mujoco.org/index.html\]]{.link-target} physics
engine. MuJoCo is a proprietary software that requires a license, which
is free to trial and free for students, but otherwise is not free. As a
result, installing it is optional, but because of its importance to the
research community---it is the de facto standard for benchmarking deep
RL algorithms in continuous control---it is preferred.

Don't worry if you decide not to install MuJoCo, though. You can
definitely get started in RL by running RL algorithms on the [Classic
Control](https://gym.openai.com/envs/#classic_control){.reference
.external}[
\[https://gym.openai.com/envs/#classic_control\]]{.link-target} and
[Box2d](https://gym.openai.com/envs/#box2d){.reference .external}[
\[https://gym.openai.com/envs/#box2d\]]{.link-target} environments in
Gym, which are totally free to use.
:::

  ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#installation.xhtml_id1){.fn-backref}   It looks like at least one person has figured out [a workaround for running on Windows](https://github.com/openai/spinningup/issues/23){.reference .external}[ \[https://github.com/openai/spinningup/issues/23\]]{.link-target}. If you try another way and succeed, please let us know how you did it!
  ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

:::::::: {#installation.xhtml_installing-python .section}
## [Installing Python](#installation.xhtml_id4){.toc-backref}

We recommend installing Python through Anaconda. Anaconda is a library
that includes Python and many useful packages for Python, as well as an
environment manager called conda that makes package management simple.

Follow [the installation
instructions](https://docs.continuum.io/anaconda/install/){.reference
.external}[
\[https://docs.continuum.io/anaconda/install/\]]{.link-target} for
Anaconda here. Download and install Anaconda3 (at time of writing,
[Anaconda3-5.3.0](https://repo.anaconda.com/archive/){.reference
.external}[ \[https://repo.anaconda.com/archive/\]]{.link-target}). Then
create a conda Python 3.6 env for organizing packages used in Spinning
Up:

:::: highlight-default
::: highlight
    conda create -n spinningup python=3.6
:::
::::

To use Python from the environment you just created, activate the
environment with:

:::: highlight-default
::: highlight
    conda activate spinningup
:::
::::

::: {.admonition-you-should-know .admonition}
You Should Know

If you're new to python environments and package management, this stuff
can quickly get confusing or overwhelming, and you'll probably hit some
snags along the way. (Especially, you should expect problems like, "I
just installed this thing, but it says it's not found when I try to use
it!") You may want to read through some clean explanations about what
package management is, why it's a good idea, and what commands you'll
typically have to execute to correctly use it.

[FreeCodeCamp](https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c){.reference
.external}[
\[https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c\]]{.link-target}
has a good explanation worth reading. There's a shorter description on
[Towards Data
Science](https://towardsdatascience.com/environment-management-with-conda-python-2-3-b9961a8a5097){.reference
.external}[
\[https://towardsdatascience.com/environment-management-with-conda-python-2-3-b9961a8a5097\]]{.link-target}
which is also helpful and informative. Finally, if you're an extremely
patient person, you may want to read the (dry, but very informative)
[documentation page from
Conda](https://conda.io/docs/user-guide/tasks/manage-environments.html){.reference
.external}[
\[https://conda.io/docs/user-guide/tasks/manage-environments.html\]]{.link-target}.
:::
::::::::

::::::::: {#installation.xhtml_installing-openmpi .section}
## [Installing OpenMPI](#installation.xhtml_id5){.toc-backref}

::::: {#installation.xhtml_ubuntu .section}
### [Ubuntu](#installation.xhtml_id6){.toc-backref}

:::: highlight-default
::: highlight
    sudo apt-get update && sudo apt-get install libopenmpi-dev
:::
::::
:::::

::::: {#installation.xhtml_mac-os-x .section}
### [Mac OS X](#installation.xhtml_id7){.toc-backref}

Installation of system packages on Mac requires
[Homebrew](https://brew.sh){.reference .external}[
\[https://brew.sh\]]{.link-target}. With Homebrew installed, run the
follwing:

:::: highlight-default
::: highlight
    brew install openmpi
:::
::::
:::::
:::::::::

:::::: {#installation.xhtml_installing-spinning-up .section}
## [Installing Spinning Up](#installation.xhtml_id8){.toc-backref}

:::: highlight-default
::: highlight
    git clone https://github.com/openai/spinningup.git
    cd spinningup
    pip install -e .
:::
::::

::: {.admonition-you-should-know .admonition}
You Should Know

Spinning Up defaults to installing everything in Gym **except** the
MuJoCo environments. In case you run into any trouble with the Gym
installation, check out the
[Gym](https://github.com/openai/gym){.reference .external}[
\[https://github.com/openai/gym\]]{.link-target} github page for help.
If you want the MuJoCo environments, see the optional installation
section below.
:::
::::::

::::::::: {#installation.xhtml_check-your-install .section}
## [Check Your Install](#installation.xhtml_id9){.toc-backref}

To see if you've successfully installed Spinning Up, try running PPO in
the LunarLander-v2 environment with

:::: highlight-default
::: highlight
    python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999
:::
::::

This might run for around 10 minutes, and you can leave it going in the
background while you continue reading through documentation. This won't
train the agent to completion, but will run it for long enough that you
can see *some* learning progress when the results come in.

After it finishes training, watch a video of the trained policy with

:::: highlight-default
::: highlight
    python -m spinup.run test_policy data/installtest/installtest_s0
:::
::::

And plot the results with

:::: highlight-default
::: highlight
    python -m spinup.run plot data/installtest/installtest_s0
:::
::::
:::::::::

:::::::: {#installation.xhtml_installing-mujoco-optional .section}
## [Installing MuJoCo (Optional)](#installation.xhtml_id10){.toc-backref}

First, go to the
[mujoco-py](https://github.com/openai/mujoco-py){.reference .external}[
\[https://github.com/openai/mujoco-py\]]{.link-target} github page.
Follow the installation instructions in the README, which describe how
to install the MuJoCo physics engine and the mujoco-py package (which
allows the use of MuJoCo from Python).

::: {.admonition-you-should-know .admonition}
You Should Know

In order to use the MuJoCo simulator, you will need to get a [MuJoCo
license](https://www.roboti.us/license.html){.reference .external}[
\[https://www.roboti.us/license.html\]]{.link-target}. Free 30-day
licenses are available to anyone, and free 1-year licenses are available
to full-time students.
:::

Once you have installed MuJoCo, install the corresponding Gym
environments with

:::: highlight-default
::: highlight
    pip install gym[mujoco,robotics]
:::
::::

And then check that things are working by running PPO in the Walker2d-v2
environment with

:::: highlight-default
::: highlight
    python -m spinup.run ppo --hid "[32,32]" --env Walker2d-v2 --exp_name mujocotest
:::
::::
::::::::
:::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::

[]{#algorithms.xhtml}

::::::::::::: {.body role="main"}
:::::::::::: {#algorithms.xhtml_algorithms .section}
# [Algorithms](#algorithms.xhtml_id1){.toc-backref}

::: {#algorithms.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Algorithms](#algorithms.xhtml_algorithms){#algorithms.xhtml_id1
  .reference .internal}
  - [What's
    Included](#algorithms.xhtml_what-s-included){#algorithms.xhtml_id2
    .reference .internal}
  - [Why These
    Algorithms?](#algorithms.xhtml_why-these-algorithms){#algorithms.xhtml_id3
    .reference .internal}
    - [The On-Policy
      Algorithms](#algorithms.xhtml_the-on-policy-algorithms){#algorithms.xhtml_id4
      .reference .internal}
    - [The Off-Policy
      Algorithms](#algorithms.xhtml_the-off-policy-algorithms){#algorithms.xhtml_id5
      .reference .internal}
  - [Code Format](#algorithms.xhtml_code-format){#algorithms.xhtml_id6
    .reference .internal}
    - [The Algorithm Function: PyTorch
      Version](#algorithms.xhtml_the-algorithm-function-pytorch-version){#algorithms.xhtml_id7
      .reference .internal}
    - [The Algorithm Function: Tensorflow
      Version](#algorithms.xhtml_the-algorithm-function-tensorflow-version){#algorithms.xhtml_id8
      .reference .internal}
    - [The Core
      File](#algorithms.xhtml_the-core-file){#algorithms.xhtml_id9
      .reference .internal}
:::

::: {#algorithms.xhtml_what-s-included .section}
## [What's Included](#algorithms.xhtml_id2){.toc-backref}

The following algorithms are implemented in the Spinning Up package:

- [Vanilla Policy Gradient](../algorithms/vpg.html){.reference
  .external} (VPG)
- [Trust Region Policy Optimization](../algorithms/trpo.html){.reference
  .external} (TRPO)
- [Proximal Policy Optimization](../algorithms/ppo.html){.reference
  .external} (PPO)
- [Deep Deterministic Policy
  Gradient](../algorithms/ddpg.html){.reference .external} (DDPG)
- [Twin Delayed DDPG](../algorithms/td3.html){.reference .external}
  (TD3)
- [Soft Actor-Critic](../algorithms/sac.html){.reference .external}
  (SAC)

They are all implemented with
[MLP](https://en.wikipedia.org/wiki/Multilayer_perceptron){.reference
.external}[
\[https://en.wikipedia.org/wiki/Multilayer_perceptron\]]{.link-target}
(non-recurrent) actor-critics, making them suitable for fully-observed,
non-image-based RL environments, e.g. the [Gym
Mujoco](https://gym.openai.com/envs/#mujoco){.reference .external}[
\[https://gym.openai.com/envs/#mujoco\]]{.link-target} environments.

Spinning Up has two implementations for each algorithm (except for
TRPO): one that uses [PyTorch](https://pytorch.org/){.reference
.external}[ \[https://pytorch.org/\]]{.link-target} as the neural
network library, and one that uses [Tensorflow
v1](https://www.tensorflow.org/versions/r1.15/api_docs){.reference
.external}[
\[https://www.tensorflow.org/versions/r1.15/api_docs\]]{.link-target} as
the neural network library. (TRPO is currently only available in
Tensorflow.)
:::

::::: {#algorithms.xhtml_why-these-algorithms .section}
## [Why These Algorithms?](#algorithms.xhtml_id3){.toc-backref}

We chose the core deep RL algorithms in this package to reflect useful
progressions of ideas from the recent history of the field, culminating
in two algorithms in particular---PPO and SAC---which are close to state
of the art on reliability and sample efficiency among policy-learning
algorithms. They also expose some of the trade-offs that get made in
designing and using algorithms in deep RL.

::: {#algorithms.xhtml_the-on-policy-algorithms .section}
### [The On-Policy Algorithms](#algorithms.xhtml_id4){.toc-backref}

Vanilla Policy Gradient is the most basic, entry-level algorithm in the
deep RL space because it completely predates the advent of deep RL
altogether. The core elements of VPG go all the way back to the late 80s
/ early 90s. It started a trail of research which ultimately led to
stronger algorithms such as TRPO and then PPO soon after.

A key feature of this line of work is that all of these algorithms are
*on-policy*: that is, they don't use old data, which makes them weaker
on sample efficiency. But this is for a good reason: these algorithms
directly optimize the objective you care about---policy
performance---and it works out mathematically that you need on-policy
data to calculate the updates. So, this family of algorithms trades off
sample efficiency in favor of stability---but you can see the
progression of techniques (from VPG to TRPO to PPO) working to make up
the deficit on sample efficiency.
:::

::: {#algorithms.xhtml_the-off-policy-algorithms .section}
### [The Off-Policy Algorithms](#algorithms.xhtml_id5){.toc-backref}

DDPG is a similarly foundational algorithm to VPG, although much
younger---the theory of deterministic policy gradients, which led to
DDPG, wasn't published until 2014. DDPG is closely connected to
Q-learning algorithms, and it concurrently learns a Q-function and a
policy which are updated to improve each other.

Algorithms like DDPG and Q-Learning are *off-policy*, so they are able
to reuse old data very efficiently. They gain this benefit by exploiting
Bellman's equations for optimality, which a Q-function can be trained to
satisfy using *any* environment interaction data (as long as there's
enough experience from the high-reward areas in the environment).

But problematically, there are no guarantees that doing a good job of
satisfying Bellman's equations leads to having great policy performance.
*Empirically* one can get great performance---and when it happens, the
sample efficiency is wonderful---but the absence of guarantees makes
algorithms in this class potentially brittle and unstable. TD3 and SAC
are descendants of DDPG which make use of a variety of insights to
mitigate these issues.
:::
:::::

:::::: {#algorithms.xhtml_code-format .section}
## [Code Format](#algorithms.xhtml_id6){.toc-backref}

All implementations in Spinning Up adhere to a standard template. They
are split into two files: an algorithm file, which contains the core
logic of the algorithm, and a core file, which contains various
utilities needed to run the algorithm.

The algorithm file always starts with a class definition for an
experience buffer object, which is used to store information from
agent-environment interactions. Next, there is a single function which
runs the algorithm. The algorithm function follows a template that is
roughly the same across the PyTorch and Tensorflow versions, but we'll
break it down for each separately below. Finally, there's some support
in each algorithm file for directly running the algorithm in Gym
environments from the command line (though this is not the recommended
way to run the algorithms---we'll describe how to do that on the
[Running Experiments](../user/running.html){.reference .external} page).

::: {#algorithms.xhtml_the-algorithm-function-pytorch-version .section}
### [The Algorithm Function: PyTorch Version](#algorithms.xhtml_id7){.toc-backref}

The algorithm function for a PyTorch implementation performs the
following tasks in (roughly) this order:

> ::: {}
> 1.  Logger setup
> 2.  Random seed setting
> 3.  Environment instantiation
> 4.  Constructing the actor-critic PyTorch module via the
>     [`actor_critic`{.docutils .literal}]{.pre} function passed to the
>     algorithm function as an argument
> 5.  Instantiating the experience buffer
> 6.  Setting up callable loss functions that also provide diagnostics
>     specific to the algorithm
> 7.  Making PyTorch optimizers
> 8.  Setting up model saving through the logger
> 9.  Setting up an update function that runs one epoch of optimization
>     or one step of descent
> 10. Running the main loop of the algorithm:
>     1.  Run the agent in the environment
>     2.  Periodically update the parameters of the agent according to
>         the main equations of the algorithm
>     3.  Log key performance metrics and save agent
> :::
:::

::: {#algorithms.xhtml_the-algorithm-function-tensorflow-version .section}
### [The Algorithm Function: Tensorflow Version](#algorithms.xhtml_id8){.toc-backref}

The algorithm function for a Tensorflow implementation performs the
following tasks in (roughly) this order:

> ::: {}
> 1.  Logger setup
> 2.  Random seed setting
> 3.  Environment instantiation
> 4.  Making placeholders for the computation graph
> 5.  Building the actor-critic computation graph via the
>     [`actor_critic`{.docutils .literal}]{.pre} function passed to the
>     algorithm function as an argument
> 6.  Instantiating the experience buffer
> 7.  Building the computation graph for loss functions and diagnostics
>     specific to the algorithm
> 8.  Making training ops
> 9.  Making the TF Session and initializing parameters
> 10. Setting up model saving through the logger
> 11. Defining functions needed for running the main loop of the
>     algorithm (e.g. the core update function, get action function, and
>     test agent function, depending on the algorithm)
> 12. Running the main loop of the algorithm:
>     1.  Run the agent in the environment
>     2.  Periodically update the parameters of the agent according to
>         the main equations of the algorithm
>     3.  Log key performance metrics and save agent
> :::
:::

::: {#algorithms.xhtml_the-core-file .section}
### [The Core File](#algorithms.xhtml_id9){.toc-backref}

The core files don't adhere as closely as the algorithms files to a
template, but do have some approximate structure:

> ::: {}
> 1.  **Tensorflow only:** Functions related to making and managing
>     placeholders
> 2.  Functions for building sections of computation graph relevant to
>     the [`actor_critic`{.docutils .literal}]{.pre} method for a
>     particular algorithm
> 3.  Any other useful functions
> 4.  Implementations for an MLP actor-critic compatible with the
>     algorithm, where both the policy and the value function(s) are
>     represented by simple MLPs
> :::
:::
::::::
::::::::::::
:::::::::::::

[]{#running.xhtml}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#running.xhtml_running-experiments .section}
# [Running Experiments](#running.xhtml_id3){.toc-backref}

::: {#running.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Running
  Experiments](#running.xhtml_running-experiments){#running.xhtml_id3
  .reference .internal}
  - [Launching from the Command
    Line](#running.xhtml_launching-from-the-command-line){#running.xhtml_id4
    .reference .internal}
    - [Choosing PyTorch or Tensorflow from the Command
      Line](#running.xhtml_choosing-pytorch-or-tensorflow-from-the-command-line){#running.xhtml_id5
      .reference .internal}
    - [Setting Hyperparameters from the Command
      Line](#running.xhtml_setting-hyperparameters-from-the-command-line){#running.xhtml_id6
      .reference .internal}
    - [Launching Multiple Experiments at
      Once](#running.xhtml_launching-multiple-experiments-at-once){#running.xhtml_id7
      .reference .internal}
    - [Special Flags](#running.xhtml_special-flags){#running.xhtml_id8
      .reference .internal}
      - [Environment
        Flag](#running.xhtml_environment-flag){#running.xhtml_id9
        .reference .internal}
      - [Shortcut
        Flags](#running.xhtml_shortcut-flags){#running.xhtml_id10
        .reference .internal}
      - [Config Flags](#running.xhtml_config-flags){#running.xhtml_id11
        .reference .internal}
    - [Where Results are
      Saved](#running.xhtml_where-results-are-saved){#running.xhtml_id12
      .reference .internal}
      - [How is Suffix
        Determined?](#running.xhtml_how-is-suffix-determined){#running.xhtml_id13
        .reference .internal}
    - [Extra](#running.xhtml_extra){#running.xhtml_id14 .reference
      .internal}
  - [Launching from
    Scripts](#running.xhtml_launching-from-scripts){#running.xhtml_id15
    .reference .internal}
    - [Using
      ExperimentGrid](#running.xhtml_using-experimentgrid){#running.xhtml_id16
      .reference .internal}
:::

One of the best ways to get a feel for deep RL is to run the algorithms
and see how they perform on different tasks. The Spinning Up code
library makes small-scale (local) experiments easy to do, and in this
section, we'll discuss two ways to run them: either from the command
line, or through function calls in scripts.

:::::::::::::::::::::::::::::::::::::::::::::: {#running.xhtml_launching-from-the-command-line .section}
## [Launching from the Command Line](#running.xhtml_id4){.toc-backref}

Spinning Up ships with [`spinup/run.py`{.docutils .literal}]{.pre}, a
convenient tool that lets you easily launch any algorithm (with any
choices of hyperparameters) from the command line. It also serves as a
thin wrapper over the utilities for watching trained policies and
plotting, although we will not discuss that functionality on this page
(for those details, see the pages on [experiment
outputs](../user/saving_and_loading.html){.reference .external} and
[plotting](../user/plotting.html){.reference .external}).

The standard way to run a Spinning Up algorithm from the command line is

:::: highlight-default
::: highlight
    python -m spinup.run [algo name] [experiment flags]
:::
::::

eg:

:::: highlight-default
::: highlight
    python -m spinup.run ppo --env Walker2d-v2 --exp_name walker
:::
::::

::: {.admonition-you-should-know .admonition}
You Should Know

If you are using ZShell: ZShell interprets square brackets as special
characters. Spinning Up uses square brackets in a few ways for command
line arguments; make sure to escape them, or try the solution
recommended
[here](http://kinopyo.com/en/blog/escape-square-bracket-by-default-in-zsh){.reference
.external}[
\[http://kinopyo.com/en/blog/escape-square-bracket-by-default-in-zsh\]]{.link-target}
if you want to escape them by default.
:::

::::::: {.admonition-detailed-quickstart-guide .admonition}
Detailed Quickstart Guide

:::: highlight-default
::: highlight
    python -m spinup.run ppo --exp_name ppo_ant --env Ant-v2 --clip_ratio 0.1 0.2
        --hid[h] [32,32] [64,32] --act torch.nn.Tanh --seed 0 10 20 --dt
        --data_dir path/to/data
:::
::::

runs PPO in the [`Ant-v2`{.docutils .literal}]{.pre} Gym environment,
with various settings controlled by the flags.

By default, the PyTorch version will run (except for with TRPO, since
Spinning Up doesn't have a PyTorch TRPO yet). Substitute
[`ppo`{.docutils .literal}]{.pre} with [`ppo_tf1`{.docutils
.literal}]{.pre} for the Tensorflow version.

[`clip_ratio`{.docutils .literal}]{.pre}, [`hid`{.docutils
.literal}]{.pre}, and [`act`{.docutils .literal}]{.pre} are flags to set
some algorithm hyperparameters. You can provide multiple values for
hyperparameters to run multiple experiments. Check the docs to see what
hyperparameters you can set (click here for the [PPO
documentation](ppo.html_spinup.ppo){.reference .external}).

[`hid`{.docutils .literal}]{.pre} and [`act`{.docutils .literal}]{.pre}
are [special shortcut flags](running.html_shortcut-flags){.reference
.external} for setting the hidden sizes and activation function for the
neural networks trained by the algorithm.

The [`seed`{.docutils .literal}]{.pre} flag sets the seed for the random
number generator. RL algorithms have high variance, so try multiple
seeds to get a feel for how performance varies.

The [`dt`{.docutils .literal}]{.pre} flag ensures that the save
directory names will have timestamps in them (otherwise they don't,
unless you set [`FORCE_DATESTAMP=True`{.docutils .literal}]{.pre} in
[`spinup/user_config.py`{.docutils .literal}]{.pre}).

The [`data_dir`{.docutils .literal}]{.pre} flag allows you to set the
save folder for results. The default value is set by
[`DEFAULT_DATA_DIR`{.docutils .literal}]{.pre} in
[`spinup/user_config.py`{.docutils .literal}]{.pre}, which will be a
subfolder [`data`{.docutils .literal}]{.pre} in the
[`spinningup`{.docutils .literal}]{.pre} folder (unless you change it).

[Save directory names](running.html_where-results-are-saved){.reference
.external} are based on [`exp_name`{.docutils .literal}]{.pre} and any
flags which have multiple values. Instead of the full flag, a shorthand
will appear in the directory name. Shorthands can be provided by the
user in square brackets after the flag, like [`--hid[h]`{.docutils
.literal}]{.pre}; otherwise, shorthands are substrings of the flag
([`clip_ratio`{.docutils .literal}]{.pre} becomes [`cli`{.docutils
.literal}]{.pre}). To illustrate, the save directory for the run with
[`clip_ratio=0.1`{.docutils .literal}]{.pre}, [`hid=[32,32]`{.docutils
.literal}]{.pre}, and [`seed=10`{.docutils .literal}]{.pre} will be:

:::: {.last .highlight-default}
::: highlight
    path/to/data/YY-MM-DD_ppo_ant_cli0-1_h32-32/YY-MM-DD_HH-MM-SS-ppo_ant_cli0-1_h32-32_seed10
:::
::::
:::::::

::::::: {#running.xhtml_choosing-pytorch-or-tensorflow-from-the-command-line .section}
### [Choosing PyTorch or Tensorflow from the Command Line](#running.xhtml_id5){.toc-backref}

To use a PyTorch version of an algorithm, run with

:::: highlight-default
::: highlight
    python -m spinup.run [algo]_pytorch
:::
::::

To use a Tensorflow version of an algorithm, run with

:::: highlight-default
::: highlight
    python -m spinup.run [algo]_tf1
:::
::::

If you run [`python`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`-m`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`spinup.run`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`[algo]`{.docutils .literal}]{.pre} without
[`_pytorch`{.docutils .literal}]{.pre} or [`_tf1`{.docutils
.literal}]{.pre}, the runner will look in
[`spinup/user_config.py`{.docutils .literal}]{.pre} for which version it
should default to for that algorithm.
:::::::

::::::::::::: {#running.xhtml_setting-hyperparameters-from-the-command-line .section}
### [Setting Hyperparameters from the Command Line](#running.xhtml_id6){.toc-backref}

Every hyperparameter in every algorithm can be controlled directly from
the command line. If [`kwarg`{.docutils .literal}]{.pre} is a valid
keyword arg for the function call of an algorithm, you can set values
for it with the flag [`--kwarg`{.docutils .literal}]{.pre}. To find out
what keyword args are available, see either the docs page for an
algorithm, or try

:::: highlight-default
::: highlight
    python -m spinup.run [algo name] --help
:::
::::

to see a readout of the docstring.

::::: {.admonition-you-should-know .admonition}
You Should Know

Values pass through [`eval()`{.docutils .literal}]{.pre} before being
used, so you can describe some functions and objects directly from the
command line. For example:

:::: highlight-default
::: highlight
    python -m spinup.run ppo --env Walker2d-v2 --exp_name walker --act torch.nn.ELU
:::
::::

sets [`torch.nn.ELU`{.docutils .literal}]{.pre} as the activation
function. (Tensorflow equivalent: run [`ppo_tf1`{.docutils
.literal}]{.pre} with [`--act`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`tf.nn.elu`{.docutils .literal}]{.pre}.)
:::::

::::::: {.admonition-you-should-know .admonition}
You Should Know

There's some nice handling for kwargs that take dict values. Instead of
having to provide

:::: highlight-default
::: highlight
    --key dict(v1=value_1, v2=value_2)
:::
::::

you can give

:::: highlight-default
::: highlight
    --key:v1 value_1 --key:v2 value_2
:::
::::

to get the same result.
:::::::
:::::::::::::

::::: {#running.xhtml_launching-multiple-experiments-at-once .section}
### [Launching Multiple Experiments at Once](#running.xhtml_id7){.toc-backref}

You can launch multiple experiments, to be executed **in series**, by
simply providing more than one value for a given argument. (An
experiment for each possible combination of values will be launched.)

For example, to launch otherwise-equivalent runs with different random
seeds (0, 10, and 20), do:

:::: highlight-default
::: highlight
    python -m spinup.run ppo --env Walker2d-v2 --exp_name walker --seed 0 10 20
:::
::::

Experiments don't launch in parallel because they soak up enough
resources that executing several at the same time wouldn't get a
speedup.
:::::

:::::: {#running.xhtml_special-flags .section}
### [Special Flags](#running.xhtml_id8){.toc-backref}

A few flags receive special treatment.

::: {#running.xhtml_environment-flag .section}
#### [Environment Flag](#running.xhtml_id9){.toc-backref}

`--env`{.descname}`, `{.descclassname}`--env_name`{.descname}

:   *string*. The name of an environment in the OpenAI Gym. All Spinning
    Up algorithms are implemented as functions that accept
    [`env_fn`{.docutils .literal}]{.pre} as an argument, where
    [`env_fn`{.docutils .literal}]{.pre} must be a callable function
    that builds a copy of the RL environment. Since the most common use
    case is Gym environments, though, all of which are built through
    [`gym.make(env_name)`{.docutils .literal}]{.pre}, we allow you to
    just specify [`env_name`{.docutils .literal}]{.pre} (or
    [`env`{.docutils .literal}]{.pre} for short) at the command line,
    which gets converted to a lambda-function that builds the correct
    gym environment.
:::

::: {#running.xhtml_shortcut-flags .section}
#### [Shortcut Flags](#running.xhtml_id10){.toc-backref}

Some algorithm arguments are relatively long, and we enabled shortcuts
for them:

`--hid`{.descname}`, `{.descclassname}`--ac_kwargs`{.descname}`:hidden_sizes`{.descclassname}

:   *list of ints*. Sets the sizes of the hidden layers in the neural
    networks (policies and value functions).

<!-- -->

`--act`{.descname}`, `{.descclassname}`--ac_kwargs`{.descname}`:activation`{.descclassname}

:   *tf op*. The activation function for the neural networks in the
    actor and critic.

These flags are valid for all current Spinning Up algorithms.
:::

::: {#running.xhtml_config-flags .section}
#### [Config Flags](#running.xhtml_id11){.toc-backref}

These flags are not hyperparameters of any algorithm, but change the
experimental configuration in some way.

`--cpu`{.descname}`, `{.descclassname}`--num_cpu`{.descname}

:   *int*. If this flag is set, the experiment is launched with this
    many processes, one per cpu, connected by MPI. Some algorithms are
    amenable to this sort of parallelization but not all. An error will
    be raised if you try setting [`num_cpu`{.docutils .literal}]{.pre}
    \> 1 for an incompatible algorithm. You can also set
    [`--num_cpu`{.docutils .literal}]{.pre}` `{.docutils
    .literal}[`auto`{.docutils .literal}]{.pre}, which will
    automatically use as many CPUs as are available on the machine.

<!-- -->

`--exp_name`{.descname}

:   *string*. The experiment name. This is used in naming the save
    directory for each experiment. The default is "cmd" + \[algo name\].

<!-- -->

`--data_dir`{.descname}

:   *path*. Set the base save directory for this experiment or set of
    experiments. If none is given, the [`DEFAULT_DATA_DIR`{.docutils
    .literal}]{.pre} in [`spinup/user_config.py`{.docutils
    .literal}]{.pre} will be used.

<!-- -->

`--datestamp`{.descname}

:   *bool*. Include date and time in the name for the save directory of
    the experiment.
:::
::::::

:::::::::: {#running.xhtml_where-results-are-saved .section}
### [Where Results are Saved](#running.xhtml_id12){.toc-backref}

Results for a particular experiment (a single run of a configuration of
hyperparameters) are stored in

:::: highlight-default
::: highlight
    data_dir/[outer_prefix]exp_name[suffix]/[inner_prefix]exp_name[suffix]_s[seed]
:::
::::

where

- [`data_dir`{.docutils .literal}]{.pre} is the value of the
  [`--data_dir`{.docutils .literal}]{.pre} flag (defaults to
  [`DEFAULT_DATA_DIR`{.docutils .literal}]{.pre} from
  [`spinup/user_config.py`{.docutils .literal}]{.pre} if
  [`--data_dir`{.docutils .literal}]{.pre} is not given),
- the [`outer_prefix`{.docutils .literal}]{.pre} is a
  [`YY-MM-DD_`{.docutils .literal}]{.pre} timestamp if the
  [`--datestamp`{.docutils .literal}]{.pre} flag is raised, otherwise
  nothing,
- the [`inner_prefix`{.docutils .literal}]{.pre} is a
  [`YY-MM-DD_HH-MM-SS-`{.docutils .literal}]{.pre} timestamp if the
  [`--datestamp`{.docutils .literal}]{.pre} flag is raised, otherwise
  nothing,
- and [`suffix`{.docutils .literal}]{.pre} is a special string based on
  the experiment hyperparameters.

::::::: {#running.xhtml_how-is-suffix-determined .section}
#### [How is Suffix Determined?](#running.xhtml_id13){.toc-backref}

Suffixes are only included if you run multiple experiments at once, and
they only include references to hyperparameters that differ across
experiments, except for random seed. The goal is to make sure that
results for similar experiments (ones which share all params except
seed) are grouped in the same folder.

Suffixes are constructed by combining *shorthands* for hyperparameters
with their values, where a shorthand is either 1) constructed
automatically from the hyperparameter name or 2) supplied by the user.
The user can supply a shorthand by writing in square brackets after the
kwarg flag.

For example, consider:

:::: highlight-default
::: highlight
    python -m spinup.run ddpg_tf1 --env Hopper-v2 --hid[h] [300] [128,128] --act tf.nn.tanh tf.nn.relu
:::
::::

Here, the [`--hid`{.docutils .literal}]{.pre} flag is given a
**user-supplied shorthand**, [`h`{.docutils .literal}]{.pre}. The
[`--act`{.docutils .literal}]{.pre} flag is not given a shorthand by the
user, so one will be constructed for it automatically.

The suffixes produced in this case are:

:::: highlight-default
::: highlight
    _h128-128_ac-actrelu
    _h128-128_ac-acttanh
    _h300_ac-actrelu
    _h300_ac-acttanh
:::
::::

Note that the [`h`{.docutils .literal}]{.pre} was given by the user. the
[`ac-act`{.docutils .literal}]{.pre} shorthand was constructed from
[`ac_kwargs:activation`{.docutils .literal}]{.pre} (the true name for
the [`act`{.docutils .literal}]{.pre} flag).
:::::::
::::::::::

:::: {#running.xhtml_extra .section}
### [Extra](#running.xhtml_id14){.toc-backref}

::: {.admonition-you-don-t-actually-need-to-know-this-one .admonition}
You Don't Actually Need to Know This One

Each individual algorithm is located in a file
[`spinup/algos/BACKEND/ALGO_NAME/ALGO_NAME.py`{.docutils
.literal}]{.pre}, and these files can be run directly from the command
line with a limited set of arguments (some of which differ from what's
available to [`spinup/run.py`{.docutils .literal}]{.pre}). The command
line support in the individual algorithm files is essentially vestigial,
however, and this is **not** a recommended way to perform experiments.

This documentation page will not describe those command line calls, and
will *only* describe calls through [`spinup/run.py`{.docutils
.literal}]{.pre}.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::: {#running.xhtml_launching-from-scripts .section}
## [Launching from Scripts](#running.xhtml_id15){.toc-backref}

Each algorithm is implemented as a python function, which can be
imported directly from the [`spinup`{.docutils .literal}]{.pre} package,
eg

:::: highlight-default
::: highlight
    >>> from spinup import ppo_pytorch as ppo
:::
::::

See the documentation page for each algorithm for a complete account of
possible arguments. These methods can be used to set up specialized
custom experiments, for example:

:::: highlight-python
::: highlight
    from spinup import ppo_tf1 as ppo
    import tensorflow as tf
    import gym

    env_fn = lambda : gym.make('LunarLander-v2')

    ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)

    logger_kwargs = dict(output_dir='path/to/output_dir', exp_name='experiment_name')

    ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=250, logger_kwargs=logger_kwargs)
:::
::::

:::::::: {#running.xhtml_using-experimentgrid .section}
### [Using ExperimentGrid](#running.xhtml_id16){.toc-backref}

It's often useful in machine learning research to run the same algorithm
with many possible hyperparameters. Spinning Up ships with a simple tool
for facilitating this, called
[ExperimentGrid](run_utils.html_experimentgrid){.reference .external}.

Consider the example in
[`spinup/examples/pytorch/bench_ppo_cartpole.py`{.docutils
.literal}]{.pre}:

::: highlight-python
+-----------------------------------+-----------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                               |
|      1                            |      from spinup.utils.run_utils import ExperimentGrid                      |
|      2                            |      from spinup import ppo_pytorch                                         |
|      3                            |      import torch                                                           |
|      4                            |                                                                             |
|      5                            |      if __name__ == '__main__':                                             |
|      6                            |          import argparse                                                    |
|      7                            |          parser = argparse.ArgumentParser()                                 |
|      8                            |          parser.add_argument('--cpu', type=int, default=4)                  |
|      9                            |          parser.add_argument('--num_runs', type=int, default=3)             |
|     10                            |          args = parser.parse_args()                                         |
|     11                            |                                                                             |
|     12                            |          eg = ExperimentGrid(name='ppo-pyt-bench')                          |
|     13                            |          eg.add('env_name', 'CartPole-v0', '', True)                        |
|     14                            |          eg.add('seed', [10*i for i in range(args.num_runs)])               |
|     15                            |          eg.add('epochs', 10)                                               |
|     16                            |          eg.add('steps_per_epoch', 4000)                                    |
|     17                            |          eg.add('ac_kwargs:hidden_sizes', [(32,), (64,64)], 'hid')          |
|     18                            |          eg.add('ac_kwargs:activation', [torch.nn.Tanh, torch.nn.ReLU], '') |
|     19                            |          eg.run(ppo_pytorch, num_cpu=args.cpu)                              |
| :::                               | :::                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------+
:::

(An equivalent Tensorflow example is available in
[`spinup/examples/tf1/bench_ppo_cartpole.py`{.docutils
.literal}]{.pre}.)

After making the ExperimentGrid object, parameters are added to it with

:::: highlight-default
::: highlight
    eg.add(param_name, values, shorthand, in_name)
:::
::::

where [`in_name`{.docutils .literal}]{.pre} forces a parameter to appear
in the experiment name, even if it has the same value across all
experiments.

After all parameters have been added,

:::: highlight-default
::: highlight
    eg.run(thunk, **run_kwargs)
:::
::::

runs all experiments in the grid (one experiment per valid
configuration), by providing the configurations as kwargs to the
function [`thunk`{.docutils .literal}]{.pre}.
[`ExperimentGrid.run`{.docutils .literal}]{.pre} uses a function named
[call_experiment](run_utils.html_spinup.utils.run_utils.call_experiment){.reference
.external} to launch [`thunk`{.docutils .literal}]{.pre}, and
[`**run_kwargs`{.docutils .literal}]{.pre} specify behaviors for
[`call_experiment`{.docutils .literal}]{.pre}. See [the documentation
page](run_utils.html_experimentgrid){.reference .external} for details.

Except for the absence of shortcut kwargs (you can't use
[`hid`{.docutils .literal}]{.pre} for
[`ac_kwargs:hidden_sizes`{.docutils .literal}]{.pre} in
[`ExperimentGrid`{.docutils .literal}]{.pre}), the basic behavior of
[`ExperimentGrid`{.docutils .literal}]{.pre} is the same as running
things from the command line. (In fact, [`spinup.run`{.docutils
.literal}]{.pre} uses an [`ExperimentGrid`{.docutils .literal}]{.pre}
under the hood.)
::::::::
:::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#saving_and_loading.xhtml}

::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::: {#saving_and_loading.xhtml_experiment-outputs .section}
# [Experiment Outputs](#saving_and_loading.xhtml_id1){.toc-backref}

::: {#saving_and_loading.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Experiment
  Outputs](#saving_and_loading.xhtml_experiment-outputs){#saving_and_loading.xhtml_id1
  .reference .internal}
  - [Algorithm
    Outputs](#saving_and_loading.xhtml_algorithm-outputs){#saving_and_loading.xhtml_id2
    .reference .internal}
    - [PyTorch Save Directory
      Info](#saving_and_loading.xhtml_pytorch-save-directory-info){#saving_and_loading.xhtml_id3
      .reference .internal}
    - [Tensorflow Save Directory
      Info](#saving_and_loading.xhtml_tensorflow-save-directory-info){#saving_and_loading.xhtml_id4
      .reference .internal}
  - [Save Directory
    Location](#saving_and_loading.xhtml_save-directory-location){#saving_and_loading.xhtml_id5
    .reference .internal}
  - [Loading and Running Trained
    Policies](#saving_and_loading.xhtml_loading-and-running-trained-policies){#saving_and_loading.xhtml_id6
    .reference .internal}
    - [If Environment Saves
      Successfully](#saving_and_loading.xhtml_if-environment-saves-successfully){#saving_and_loading.xhtml_id7
      .reference .internal}
    - [Environment Not Found
      Error](#saving_and_loading.xhtml_environment-not-found-error){#saving_and_loading.xhtml_id8
      .reference .internal}
    - [Using Trained Value
      Functions](#saving_and_loading.xhtml_using-trained-value-functions){#saving_and_loading.xhtml_id9
      .reference .internal}
:::

In this section we'll cover

- what outputs come from Spinning Up algorithm implementations,
- what formats they're stored in and how they're organized,
- where they are stored and how you can change that,
- and how to load and run trained policies.

::: {.admonition-you-should-know .admonition}
You Should Know

Spinning Up implementations currently have no way to resume training for
partially-trained agents. If you consider this feature important, please
let us know---or consider it a hacking project!
:::

:::::::: {#saving_and_loading.xhtml_algorithm-outputs .section}
## [Algorithm Outputs](#saving_and_loading.xhtml_id2){.toc-backref}

Each algorithm is set up to save a training run's hyperparameter
configuration, learning progress, trained agent and value functions, and
a copy of the environment if possible (to make it easy to load up the
agent and environment simultaneously). The output directory contains the
following:

+-------------------------------------+----------------------------------------------------------------------------------+
| **Output Directory Structure**                                                                                         |
+-------------------------------------+----------------------------------------------------------------------------------+
| [`pyt_save/`{.docutils              | :::::: {.first .last .line-block}                                                |
| .literal}]{.pre}                    | ::: line                                                                         |
|                                     | **PyTorch implementations only.** A directory containing                         |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | everything needed to restore the trained agent and value                         |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | functions. ([Details for PyTorch saves                                           |
|                                     | below.](#saving_and_loading.xhtml_details-for-pytorch-saves-below){.reference    |
|                                     | .internal})                                                                      |
|                                     | :::                                                                              |
|                                     | ::::::                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------+
| [`tf1_save/`{.docutils              | :::::: {.first .last .line-block}                                                |
| .literal}]{.pre}                    | ::: line                                                                         |
|                                     | **Tensorflow implementations only.** A directory containing                      |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | everything needed to restore the trained agent and value                         |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | functions. ([Details for Tensorflow saves                                        |
|                                     | below.](#saving_and_loading.xhtml_details-for-tensorflow-saves-below){.reference |
|                                     | .internal})                                                                      |
|                                     | :::                                                                              |
|                                     | ::::::                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------+
| [`config.json`{.docutils            | :::::::::: {.first .last .line-block}                                            |
| .literal}]{.pre}                    | ::: line                                                                         |
|                                     | A dict containing an as-complete-as-possible description                         |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | of the args and kwargs you used to launch the training                           |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | function. If you passed in something which can't be                              |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | serialized to JSON, it should get handled gracefully by the                      |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | logger, and the config file will represent it with a string.                     |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | Note: this is meant for record-keeping only. Launching an                        |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | experiment from a config file is not currently supported.                        |
|                                     | :::                                                                              |
|                                     | ::::::::::                                                                       |
+-------------------------------------+----------------------------------------------------------------------------------+
| [`progress.txt`{.docutils           | :::::: {.first .last .line-block}                                                |
| .literal}]{.pre}                    | ::: line                                                                         |
|                                     | A tab-separated value file containing records of the metrics                     |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | recorded by the logger throughout training. eg, [`Epoch`{.docutils               |
|                                     | .literal}]{.pre},                                                                |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | [`AverageEpRet`{.docutils .literal}]{.pre}, etc.                                 |
|                                     | :::                                                                              |
|                                     | ::::::                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------+
| [`vars.pkl`{.docutils               | :::::: {.first .last .line-block}                                                |
| .literal}]{.pre}                    | ::: line                                                                         |
|                                     | A pickle file containing anything about the algorithm state                      |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | which should get stored. Currently, all algorithms only use                      |
|                                     | :::                                                                              |
|                                     |                                                                                  |
|                                     | ::: line                                                                         |
|                                     | this to save a copy of the environment.                                          |
|                                     | :::                                                                              |
|                                     | ::::::                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------+

::: {.admonition-you-should-know .admonition}
You Should Know

Sometimes environment-saving fails because the environment can't be
pickled, and [`vars.pkl`{.docutils .literal}]{.pre} is empty. This is
known to be a problem for Gym Box2D environments in older versions of
Gym, which can't be saved in this manner.
:::

::: {.admonition-you-should-know .admonition}
You Should Know

As of 1/30/20, the save directory structure has changed slightly.
Previously, Tensorflow graphs were saved in the
[`simple_save/`{.docutils .literal}]{.pre} folder; this has been
replaced with [`tf1_save/`{.docutils .literal}]{.pre}.
:::

::: {.admonition-you-should-know .admonition}
You Should Know

The only file in here that you should ever have to use "by hand" is the
[`config.json`{.docutils .literal}]{.pre} file. Our agent testing
utility will load things from the [`tf1_save/`{.docutils
.literal}]{.pre} or [`pyt_save/`{.docutils .literal}]{.pre} directory,
and our plotter interprets the contents of [`progress.txt`{.docutils
.literal}]{.pre}, and those are the correct tools for interfacing with
these outputs. But there is no tooling for [`config.json`{.docutils
.literal}]{.pre}---it's just there so that if you forget what
hyperparameters you ran an experiment with, you can double-check.
:::

::: {#saving_and_loading.xhtml_pytorch-save-directory-info .section}
### [PyTorch Save Directory Info](#saving_and_loading.xhtml_id3){.toc-backref}

The [`pyt_save`{.docutils .literal}]{.pre} directory contains:

+-------------------------------------+-------------------------------------------------------+
| **Pyt_Save Directory Structure**                                                            |
+-------------------------------------+-------------------------------------------------------+
| [`model.pt`{.docutils               | ::::::: {.first .last .line-block}                    |
| .literal}]{.pre}                    | ::: line                                              |
|                                     | A file created with [`torch.save`{.docutils           |
|                                     | .literal}]{.pre}, essentially just a                  |
|                                     | :::                                                   |
|                                     |                                                       |
|                                     | ::: line                                              |
|                                     | pickled PyTorch [`nn.Module`{.docutils                |
|                                     | .literal}]{.pre}. Loading it will restore             |
|                                     | :::                                                   |
|                                     |                                                       |
|                                     | ::: line                                              |
|                                     | a trained agent as an ActorCritic object with an      |
|                                     | [`act`{.docutils .literal}]{.pre}                     |
|                                     | :::                                                   |
|                                     |                                                       |
|                                     | ::: line                                              |
|                                     | method.                                               |
|                                     | :::                                                   |
|                                     | :::::::                                               |
+-------------------------------------+-------------------------------------------------------+
:::

::: {#saving_and_loading.xhtml_tensorflow-save-directory-info .section}
### [Tensorflow Save Directory Info](#saving_and_loading.xhtml_id4){.toc-backref}

The [`tf1_save`{.docutils .literal}]{.pre} directory contains:

+-------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **TF1_Save Directory Structure**                                                                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| [`variables/`{.docutils             | ::::: {.first .last .line-block}                                                                                     |
| .literal}]{.pre}                    | ::: line                                                                                                             |
|                                     | A directory containing outputs from the Tensorflow Saver.                                                            |
|                                     | :::                                                                                                                  |
|                                     |                                                                                                                      |
|                                     | ::: line                                                                                                             |
|                                     | See documentation for [Tensorflow                                                                                    |
|                                     | SavedModel](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md){.reference |
|                                     | .external}[                                                                                                          |
|                                     | \[https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md\]]{.link-target}.     |
|                                     | :::                                                                                                                  |
|                                     | :::::                                                                                                                |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| [`model_info.pkl`{.docutils         | ::::: {.first .last .line-block}                                                                                     |
| .literal}]{.pre}                    | ::: line                                                                                                             |
|                                     | A dict containing information (map from key to tensor name)                                                          |
|                                     | :::                                                                                                                  |
|                                     |                                                                                                                      |
|                                     | ::: line                                                                                                             |
|                                     | which helps us unpack the saved model after loading.                                                                 |
|                                     | :::                                                                                                                  |
|                                     | :::::                                                                                                                |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| [`saved_model.pb`{.docutils         | :::: {.first .last .line-block}                                                                                      |
| .literal}]{.pre}                    | ::: line                                                                                                             |
|                                     | A protocol buffer, needed for a [Tensorflow                                                                          |
|                                     | SavedModel](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md){.reference |
|                                     | .external}[                                                                                                          |
|                                     | \[https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md\]]{.link-target}.     |
|                                     | :::                                                                                                                  |
|                                     | ::::                                                                                                                 |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------+
:::
::::::::

::: {#saving_and_loading.xhtml_save-directory-location .section}
## [Save Directory Location](#saving_and_loading.xhtml_id5){.toc-backref}

Experiment results will, by default, be saved in the same directory as
the Spinning Up package, in a folder called [`data`{.docutils
.literal}]{.pre}:

``` literal-block

spinningup/
    data/
        ...
    docs/
        ...
    spinup/
        ...
    LICENSE
    setup.py
```

You can change the default results directory by modifying
[`DEFAULT_DATA_DIR`{.docutils .literal}]{.pre} in
[`spinup/user_config.py`{.docutils .literal}]{.pre}.
:::

:::::::::: {#saving_and_loading.xhtml_loading-and-running-trained-policies .section}
## [Loading and Running Trained Policies](#saving_and_loading.xhtml_id6){.toc-backref}

::::: {#saving_and_loading.xhtml_if-environment-saves-successfully .section}
### [If Environment Saves Successfully](#saving_and_loading.xhtml_id7){.toc-backref}

For cases where the environment is successfully saved alongside the
agent, it's a cinch to watch the trained agent act in the environment
using:

:::: highlight-default
::: highlight
    python -m spinup.run test_policy path/to/output_directory
:::
::::

There are a few flags for options:

`-l`{.descname}` L`{.descclassname}`, `{.descclassname}`--len`{.descname}`=L`{.descclassname}`, `{.descclassname}`default`{.descname}`=0`{.descclassname}

:   *int*. Maximum length of test episode / trajectory / rollout. The
    default of 0 means no maximum episode length---episodes only end
    when the agent has reached a terminal state in the environment.
    (Note: setting L=0 will not prevent Gym envs wrapped by TimeLimit
    wrappers from ending when they reach their pre-set maximum episode
    length.)

<!-- -->

`-n`{.descname}` N`{.descclassname}`, `{.descclassname}`--episodes`{.descname}`=N`{.descclassname}`, `{.descclassname}`default`{.descname}`=100`{.descclassname}

:   *int*. Number of test episodes to run the agent for.

<!-- -->

`-nr`{.descname}`, `{.descclassname}`--norender`{.descname}

:   Do not render the test episodes to the screen. In this case,
    [`test_policy`{.docutils .literal}]{.pre} will only print the
    episode returns and lengths. (Use case: the renderer slows down the
    testing process, and you just want to get a fast sense of how the
    agent is performing, so you don't particularly care to watch it.)

<!-- -->

`-i`{.descname}` I`{.descclassname}`, `{.descclassname}`--itr`{.descname}`=I`{.descclassname}`, `{.descclassname}`default`{.descname}`=-1`{.descclassname}

:   *int*. This is an option for a special case which is not supported
    by algorithms in this package as-shipped, but which they are easily
    modified to do. Use case: Sometimes it's nice to watch trained
    agents from many different points in training (eg watch at iteration
    50, 100, 150, etc.). The logger can do this---save snapshots of the
    agent from those different points, so they can be run and watched
    later. In this case, you use this flag to specify which iteration to
    run. But again: spinup algorithms by default only save snapshots of
    the most recent agent, overwriting the old snapshots.

    The default value of this flag means "use the latest snapshot."

    To modify an algo so it does produce multiple snapshots, find the
    following line (which is present in all of the algorithms):

    :::: highlight-python
    ::: highlight
        logger.save_state({'env': env}, None)
    :::
    ::::

    and tweak it to

    :::: highlight-python
    ::: highlight
        logger.save_state({'env': env}, epoch)
    :::
    ::::

    Make sure to then also set [`save_freq`{.docutils .literal}]{.pre}
    to something reasonable (because if it defaults to 1, for instance,
    you'll flood your output directory with one [`save`{.docutils
    .literal}]{.pre} folder for each snapshot---which adds up fast).

<!-- -->

`-d`{.descname}`, `{.descclassname}`--deterministic`{.descname}

:   Another special case, which is only used for SAC. The Spinning Up
    SAC implementation trains a stochastic policy, but is evaluated
    using the deterministic *mean* of the action distribution.
    [`test_policy`{.docutils .literal}]{.pre} will default to using the
    stochastic policy trained by SAC, but you should set the
    deterministic flag to watch the deterministic mean policy (the
    correct evaluation policy for SAC). This flag is not used for any
    other algorithms.
:::::

::::: {#saving_and_loading.xhtml_environment-not-found-error .section}
### [Environment Not Found Error](#saving_and_loading.xhtml_id8){.toc-backref}

If the environment wasn't saved successfully, you can expect
[`test_policy.py`{.docutils .literal}]{.pre} to crash with something
that looks like

``` literal-block

Traceback (most recent call last):
  File "spinup/utils/test_policy.py", line 153, in <module>
    run_policy(env, get_action, args.len, args.episodes, not(args.norender))
  File "spinup/utils/test_policy.py", line 114, in run_policy
    "and we can't run the agent in it. :( nn Check out the readthedocs " +
AssertionError: Environment not found!

 It looks like the environment wasn't saved, and we can't run the agent in it. :(

 Check out the readthedocs page on Experiment Outputs for how to handle this situation.
```

In this case, watching your agent perform is slightly more of a pain but
not impossible, as long as you can recreate your environment easily. Try
the following in IPython:

:::: highlight-default
::: highlight
    >>> from spinup.utils.test_policy import load_policy_and_env, run_policy
    >>> import your_env
    >>> _, get_action = load_policy_and_env('/path/to/output_directory')
    >>> env = your_env.make()
    >>> run_policy(env, get_action)
    Logging data to /tmp/experiments/1536150702/progress.txt
    Episode 0    EpRet -163.830      EpLen 93
    Episode 1    EpRet -346.164      EpLen 99
    ...
:::
::::
:::::

::: {#saving_and_loading.xhtml_using-trained-value-functions .section}
### [Using Trained Value Functions](#saving_and_loading.xhtml_id9){.toc-backref}

The [`test_policy.py`{.docutils .literal}]{.pre} tool doesn't help you
look at trained value functions, and if you want to use those, you will
have to do some digging by hand. For the PyTorch case, load the saved
model file with [`torch.load`{.docutils .literal}]{.pre} and check the
documentation for each algorithm to see what modules the ActorCritic
object has. For the Tensorflow case, load the saved computation graph
with the
[restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
.external} function, and check the documentation for each algorithm to
see what functions were saved.
:::
::::::::::
::::::::::::::::::::
:::::::::::::::::::::

[]{#plotting.xhtml}

:::::: {.body role="main"}
::::: {#plotting.xhtml_plotting-results .section}
# Plotting Results

Spinning Up ships with a simple plotting utility for interpreting
results. Run it with:

:::: highlight-default
::: highlight
    python -m spinup.run plot [path/to/output_directory ...] [--legend [LEGEND ...]]
        [--xaxis XAXIS] [--value [VALUE ...]] [--count] [--smooth S]
        [--select [SEL ...]] [--exclude [EXC ...]]
:::
::::

**Positional Arguments:**

`logdir`{.descname}

:   *strings*. As many log directories (or prefixes to log directories,
    which the plotter will autocomplete internally) as you'd like to
    plot from. Logdirs will be searched recursively for experiment
    outputs.

    ::::::: {.admonition-you-should-know .admonition}
    You Should Know

    The internal autocompleting is really handy! Suppose you have run
    several experiments, with the aim of comparing performance between
    different algorithms, resulting in a log directory structure of:

    :::: highlight-default
    ::: highlight
        data/
            bench_algo1/
                bench_algo1-seed0/
                bench_algo1-seed10/
            bench_algo2/
                bench_algo2-seed0/
                bench_algo2-seed10/
    :::
    ::::

    You can easily produce a graph comparing algo1 and algo2 with:

    :::: highlight-default
    ::: highlight
        python spinup/utils/plot.py data/bench_algo
    :::
    ::::

    relying on the autocomplete to find both
    [`data/bench_algo1`{.docutils .literal}]{.pre} and
    [`data/bench_algo2`{.docutils .literal}]{.pre}.
    :::::::

**Optional Arguments:**

`-l`{.descname}`, `{.descclassname}`--legend`{.descname}`=[LEGEND ...]`{.descclassname}

:   *strings*. Optional way to specify legend for the plot. The plotter
    legend will automatically use the [`exp_name`{.docutils
    .literal}]{.pre} from the [`config.json`{.docutils .literal}]{.pre}
    file, unless you tell it otherwise through this flag. This only
    works if you provide a name for each directory that will get
    plotted. (Note: this may not be the same as the number of logdir
    args you provide! Recall that the plotter looks for autocompletes of
    the logdir args: there may be more than one match for a given logdir
    prefix, and you will need to provide a legend string for each one of
    those matches---unless you have removed some of them as candidates
    via selection or exclusion rules (below).)

<!-- -->

`-x`{.descname}`, `{.descclassname}`--xaxis`{.descname}`=XAXIS`{.descclassname}`, `{.descclassname}`default`{.descname}`='TotalEnvInteracts'`{.descclassname}

:   *string*. Pick what column from data is used for the x-axis.

<!-- -->

`-y`{.descname}`, `{.descclassname}`--value`{.descname}`=[VALUE ...]`{.descclassname}`, `{.descclassname}`default`{.descname}`='Performance'`{.descclassname}

:   *strings*. Pick what columns from data to graph on the y-axis.
    Submitting multiple values will produce multiple graphs. Defaults to
    [`Performance`{.docutils .literal}]{.pre}, which is not an actual
    output of any algorithm. Instead, [`Performance`{.docutils
    .literal}]{.pre} refers to either [`AverageEpRet`{.docutils
    .literal}]{.pre}, the correct performance measure for the on-policy
    algorithms, or [`AverageTestEpRet`{.docutils .literal}]{.pre}, the
    correct performance measure for the off-policy algorithms. The
    plotter will automatically figure out which of
    [`AverageEpRet`{.docutils .literal}]{.pre} or
    [`AverageTestEpRet`{.docutils .literal}]{.pre} to report for each
    separate logdir.

<!-- -->

`--count`{.descname}

:   Optional flag. By default, the plotter shows y-values which are
    averaged across all results that share an [`exp_name`{.docutils
    .literal}]{.pre}, which is typically a set of identical experiments
    that only vary in random seed. But if you'd like to see all of those
    curves separately, use the [`--count`{.docutils .literal}]{.pre}
    flag.

<!-- -->

`-s`{.descname}`, `{.descclassname}`--smooth`{.descname}`=S`{.descclassname}`, `{.descclassname}`default`{.descname}`=1`{.descclassname}

:   *int*. Smooth data by averaging it over a fixed window. This
    parameter says how wide the averaging window will be.

<!-- -->

`--select`{.descname}`=[SEL ...]`{.descclassname}

:   *strings*. Optional selection rule: the plotter will only show
    curves from logdirs that contain all of these substrings.

<!-- -->

`--exclude`{.descname}`=[EXC ...]`{.descclassname}

:   *strings*. Optional exclusion rule: plotter will only show curves
    from logdirs that do not contain these substrings.
:::::
::::::

[]{#rl_intro.xhtml}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#rl_intro.xhtml_part-1-key-concepts-in-rl .section}
# [Part 1: Key Concepts in RL](#rl_intro.xhtml_id2){.toc-backref}

::: {#rl_intro.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Part 1: Key Concepts in
  RL](#rl_intro.xhtml_part-1-key-concepts-in-rl){#rl_intro.xhtml_id2
  .reference .internal}
  - [What Can RL
    Do?](#rl_intro.xhtml_what-can-rl-do){#rl_intro.xhtml_id3 .reference
    .internal}
  - [Key Concepts and
    Terminology](#rl_intro.xhtml_key-concepts-and-terminology){#rl_intro.xhtml_id4
    .reference .internal}
  - [(Optional)
    Formalism](#rl_intro.xhtml_optional-formalism){#rl_intro.xhtml_id5
    .reference .internal}
:::

Welcome to our introduction to reinforcement learning! Here, we aim to
acquaint you with

- the language and notation used to discuss the subject,
- a high-level explanation of what RL algorithms do (although we mostly
  avoid the question of *how* they do it),
- and a little bit of the core math that underlies the algorithms.

In a nutshell, RL is the study of agents and how they learn by trial and
error. It formalizes the idea that rewarding or punishing an agent for
its behavior makes it more likely to repeat or forego that behavior in
the future.

:::: {#rl_intro.xhtml_what-can-rl-do .section}
## [What Can RL Do?](#rl_intro.xhtml_id3){.toc-backref}

RL methods have recently enjoyed a wide variety of successes. For
example, it's been used to teach computers to control robots in
simulation\...

<video autoplay src="https://d4mucfpksywv.cloudfront.net/openai-baselines-ppo/knocked-over-stand-up.mp4" loop controls style="display: block; margin-left: auto; margin-right: auto; margin-bottom:1.5em; width: 100%; max-width: 720px; max-height: 80vh;">
</video>

\...and in the real world\...

::: {style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;"}
<iframe src="https://www.youtube.com/embed/jwSbzNHGflM?ecver=1" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
</iframe>
:::

\

It's also famously been used to create breakthrough AIs for
sophisticated strategy games, most notably
[Go](https://deepmind.com/research/alphago/){.reference .external}[
\[https://deepmind.com/research/alphago/\]]{.link-target} and
[Dota](https://blog.openai.com/openai-five/){.reference .external}[
\[https://blog.openai.com/openai-five/\]]{.link-target}, taught
computers to [play Atari
games](https://deepmind.com/research/dqn/){.reference .external}[
\[https://deepmind.com/research/dqn/\]]{.link-target} from raw pixels,
and trained simulated robots [to follow human
instructions](https://blog.openai.com/deep-reinforcement-learning-from-human-preferences/){.reference
.external}[
\[https://blog.openai.com/deep-reinforcement-learning-from-human-preferences/\]]{.link-target}.
::::

:::::::::::::::::::::::::::::::::::::::::::::::::::: {#rl_intro.xhtml_key-concepts-and-terminology .section}
## [Key Concepts and Terminology](#rl_intro.xhtml_id4){.toc-backref}

::: {#rl_intro.xhtml_id1 .figure .align-center}
![../\_images/rl_diagram_transparent_bg.png](_images/rl_diagram_transparent_bg.png)

[Agent-environment interaction loop.]{.caption-text}
:::

The main characters of RL are the **agent** and the **environment**. The
environment is the world that the agent lives in and interacts with. At
every step of interaction, the agent sees a (possibly partial)
observation of the state of the world, and then decides on an action to
take. The environment changes when the agent acts on it, but may also
change on its own.

The agent also perceives a **reward** signal from the environment, a
number that tells it how good or bad the current world state is. The
goal of the agent is to maximize its cumulative reward, called
**return**. Reinforcement learning methods are ways that the agent can
learn behaviors to achieve its goal.

To talk more specifically what RL does, we need to introduce additional
terminology. We need to talk about

- states and observations,
- action spaces,
- policies,
- trajectories,
- different formulations of return,
- the RL optimization problem,
- and value functions.

:::: {#rl_intro.xhtml_states-and-observations .section}
### States and Observations

A **state**
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}
is a complete description of the state of the world. There is no
information about the world which is hidden from the state. An
**observation**
![o](_images/math/ca2d5053d03bd8fd9f399e5afbb834202e2d2f2d.svg){.math}
is a partial description of a state, which may omit information.

In deep RL, we almost always represent states and observations by a
[real-valued vector, matrix, or higher-order
tensor](https://en.wikipedia.org/wiki/Real_coordinate_space){.reference
.external}[
\[https://en.wikipedia.org/wiki/Real_coordinate_space\]]{.link-target}.
For instance, a visual observation could be represented by the RGB
matrix of its pixel values; the state of a robot might be represented by
its joint angles and velocities.

When the agent is able to observe the complete state of the environment,
we say that the environment is **fully observed**. When the agent can
only see a partial observation, we say that the environment is
**partially observed**.

::: {.admonition-you-should-know .admonition}
You Should Know

Reinforcement learning notation sometimes puts the symbol for state,
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math},
in places where it would be technically more appropriate to write the
symbol for observation,
![o](_images/math/ca2d5053d03bd8fd9f399e5afbb834202e2d2f2d.svg){.math}.
Specifically, this happens when talking about how the agent decides an
action: we often signal in notation that the action is conditioned on
the state, when in practice, the action is conditioned on the
observation because the agent does not have access to the state.

In our guide, we'll follow standard conventions for notation, but it
should be clear from context which is meant. If something is unclear,
though, please raise an issue! Our goal is to teach, not to confuse.
:::
::::

::: {#rl_intro.xhtml_action-spaces .section}
### Action Spaces

Different environments allow different kinds of actions. The set of all
valid actions in a given environment is often called the **action
space**. Some environments, like Atari and Go, have **discrete action
spaces**, where only a finite number of moves are available to the
agent. Other environments, like where the agent controls a robot in a
physical world, have **continuous action spaces**. In continuous spaces,
actions are real-valued vectors.

This distinction has some quite-profound consequences for methods in
deep RL. Some families of algorithms can only be directly applied in one
case, and would have to be substantially reworked for the other.
:::

:::::::::::::::::: {#rl_intro.xhtml_policies .section}
### Policies

A **policy** is a rule used by an agent to decide what actions to take.
It can be deterministic, in which case it is usually denoted by
![\\mu](_images/math/123eb57279cfbea38a65e8e129bda64972fedc3d.svg){.math}:

::: math
![a_t =
\\mu(s_t),](_images/math/73fcacd255a221d20d5d9300acf86e4d3bf5ea1b.svg)
:::

or it may be stochastic, in which case it is usually denoted by
![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}:

::: math
![a_t \\sim \\pi(\\cdot \|
s_t).](_images/math/89757355805c4084ac93610e9581c060f2e61610.svg)
:::

Because the policy is essentially the agent's brain, it's not uncommon
to substitute the word "policy" for "agent", eg saying "The policy is
trying to maximize reward."

In deep RL, we deal with **parameterized policies**: policies whose
outputs are computable functions that depend on a set of parameters (eg
the weights and biases of a neural network) which we can adjust to
change the behavior via some optimization algorithm.

We often denote the parameters of such a policy by
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math}
or
![\\phi](_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg){.math},
and then write this as a subscript on the policy symbol to highlight the
connection:

::: math
![a_t &= \\mu\_{\\theta}(s_t) \\\\ a_t &\\sim \\pi\_{\\theta}(\\cdot \|
s_t).](_images/math/831f731859658682b2af7e217a76648697c9de46.svg)
:::

:::::::: {#rl_intro.xhtml_deterministic-policies .section}
#### Deterministic Policies

**Example: Deterministic Policies.** Here is a code snippet for building
a simple deterministic policy for a continuous action space in PyTorch,
using the [`torch.nn`{.docutils .literal}]{.pre} package:

:::: highlight-python
::: highlight
    pi_net = nn.Sequential(
                  nn.Linear(obs_dim, 64),
                  nn.Tanh(),
                  nn.Linear(64, 64),
                  nn.Tanh(),
                  nn.Linear(64, act_dim)
                )
:::
::::

This builds a multi-layer perceptron (MLP) network with two hidden
layers of size 64 and
![\\tanh](_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg){.math}
activation functions. If [`obs`{.docutils .literal}]{.pre} is a Numpy
array containing a batch of observations, [`pi_net`{.docutils
.literal}]{.pre} can be used to obtain a batch of actions as follows:

:::: highlight-python
::: highlight
    obs_tensor = torch.as_tensor(obs, dtype=torch.float32)
    actions = pi_net(obs_tensor)
:::
::::

::: {.admonition-you-should-know .admonition}
You Should Know

Don't worry about it if this neural network stuff is unfamiliar to
you---this tutorial will focus on RL, and not on the neural network side
of things. So you can skip this example and come back to it later. But
we figured that if you already knew, it could be helpful.
:::
::::::::

:::::::: {#rl_intro.xhtml_stochastic-policies .section}
#### Stochastic Policies

The two most common kinds of stochastic policies in deep RL are
**categorical policies** and **diagonal Gaussian policies**.

[Categorical](https://en.wikipedia.org/wiki/Categorical_distribution){.reference
.external}[
\[https://en.wikipedia.org/wiki/Categorical_distribution\]]{.link-target}
policies can be used in discrete action spaces, while diagonal
[Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution){.reference
.external}[
\[https://en.wikipedia.org/wiki/Multivariate_normal_distribution\]]{.link-target}
policies are used in continuous action spaces.

Two key computations are centrally important for using and training
stochastic policies:

- sampling actions from the policy,
- and computing log likelihoods of particular actions, ![\\log
  \\pi\_{\\theta}(a\|s)](_images/math/cc2095cba170e09137c55cb4f1786955b3174336.svg){.math}.

In what follows, we'll describe how to do these for both categorical and
diagonal Gaussian policies.

:::: {.admonition-categorical-policies .admonition}
Categorical Policies

A categorical policy is like a classifier over discrete actions. You
build the neural network for a categorical policy the same way you would
for a classifier: the input is the observation, followed by some number
of layers (possibly convolutional or densely-connected, depending on the
kind of input), and then you have one final linear layer that gives you
logits for each action, followed by a
[softmax](https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax){.reference
.external}[
\[https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax\]]{.link-target}
to convert the logits into probabilities.

**Sampling.** Given the probabilities for each action, frameworks like
PyTorch and Tensorflow have built-in tools for sampling. For example,
see the documentation for [Categorical distributions in
PyTorch](https://pytorch.org/docs/stable/distributions.html#categorical){.reference
.external}[
\[https://pytorch.org/docs/stable/distributions.html#categorical\]]{.link-target},
[torch.multinomial](https://pytorch.org/docs/stable/torch.html#torch.multinomial){.reference
.external}[
\[https://pytorch.org/docs/stable/torch.html#torch.multinomial\]]{.link-target},
[tf.distributions.Categorical](https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/distributions/Categorical){.reference
.external}[
\[https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/distributions/Categorical\]]{.link-target},
or
[tf.multinomial](https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/random/multinomial){.reference
.external}[
\[https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/random/multinomial\]]{.link-target}.

**Log-Likelihood.** Denote the last layer of probabilities as
![P\_{\\theta}(s)](_images/math/5364a8661022d60da78f14c9bd33124118719454.svg){.math}.
It is a vector with however many entries as there are actions, so we can
treat the actions as indices for the vector. The log likelihood for an
action
![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math}
can then be obtained by indexing into the vector:

::: {.last .math}
![\\log \\pi\_{\\theta}(a\|s) = \\log
\\left\[P\_{\\theta}(s)\\right\]\_a.](_images/math/ab8f7f4aaa7f1a3d1039ebdee058f297ed712c5a.svg)
:::
::::

::::: {.admonition-diagonal-gaussian-policies .admonition}
Diagonal Gaussian Policies

A multivariate Gaussian distribution (or multivariate normal
distribution, if you prefer) is described by a mean vector,
![\\mu](_images/math/123eb57279cfbea38a65e8e129bda64972fedc3d.svg){.math},
and a covariance matrix,
![\\Sigma](_images/math/f03ec2afde0e994f47df68b273d86e3afbfdce80.svg){.math}.
A diagonal Gaussian distribution is a special case where the covariance
matrix only has entries on the diagonal. As a result, we can represent
it by a vector.

A diagonal Gaussian policy always has a neural network that maps from
observations to mean actions,
![\\mu\_{\\theta}(s)](_images/math/6923cb2043e84ea05d3eddbb7436c60659243cb9.svg){.math}.
There are two different ways that the covariance matrix is typically
represented.

**The first way:** There is a single vector of log standard deviations,
![\\log
\\sigma](_images/math/3276548e12065a40224719e967e02b1538d3c6b2.svg){.math},
which is **not** a function of state: the ![\\log
\\sigma](_images/math/3276548e12065a40224719e967e02b1538d3c6b2.svg){.math}
are standalone parameters. (You Should Know: our implementations of VPG,
TRPO, and PPO do it this way.)

**The second way:** There is a neural network that maps from states to
log standard deviations, ![\\log
\\sigma\_{\\theta}(s)](_images/math/4015c2b584427ca2a76f50ed03b2c8d0b5b3b350.svg){.math}.
It may optionally share some layers with the mean network.

Note that in both cases we output log standard deviations instead of
standard deviations directly. This is because log stds are free to take
on any values in ![(-\\infty,
\\infty)](_images/math/9954b39a284ca1aa0aed2dc3f769404cc4e9f397.svg){.math},
while stds must be nonnegative. It's easier to train parameters if you
don't have to enforce those kinds of constraints. The standard
deviations can be obtained immediately from the log standard deviations
by exponentiating them, so we do not lose anything by representing them
this way.

**Sampling.** Given the mean action
![\\mu\_{\\theta}(s)](_images/math/6923cb2043e84ea05d3eddbb7436c60659243cb9.svg){.math}
and standard deviation
![\\sigma\_{\\theta}(s)](_images/math/cd6cc1a1e8ed7fc447a2ea0e59ad848707631c94.svg){.math},
and a vector
![z](_images/math/886f88801abbe687ef8480ddd980f4215d2aaa17.svg){.math}
of noise from a spherical Gaussian (![z \\sim \\mathcal{N}(0,
I)](_images/math/a5a922f10e8b343418b1600a9a1601183673d126.svg){.math}),
an action sample can be computed with

::: math
![a = \\mu\_{\\theta}(s) + \\sigma\_{\\theta}(s) \\odot
z,](_images/math/b18a4163a861b1fc18c6a6824af3f5540d4e2468.svg)
:::

where
![\\odot](_images/math/77c323f00609b53862181c31bf0d045c75b29440.svg){.math}
denotes the elementwise product of two vectors. Standard frameworks have
built-in ways to generate the noise vectors, such as
[torch.normal](https://pytorch.org/docs/stable/torch.html#torch.normal){.reference
.external}[
\[https://pytorch.org/docs/stable/torch.html#torch.normal\]]{.link-target}
or
[tf.random_normal](https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/random/normal){.reference
.external}[
\[https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/random/normal\]]{.link-target}.
Alternatively, you can build distribution objects, eg through
[torch.distributions.Normal](https://pytorch.org/docs/stable/distributions.html#normal){.reference
.external}[
\[https://pytorch.org/docs/stable/distributions.html#normal\]]{.link-target}
or
[tf.distributions.Normal](https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/distributions/Normal){.reference
.external}[
\[https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/distributions/Normal\]]{.link-target},
and use them to generate samples. (The advantage of the latter approach
is that those objects can also calculate log-likelihoods for you.)

**Log-Likelihood.** The log-likelihood of a
![k](_images/math/a29aa94bd66ac7a6bb3195233fd9a9df8575af86.svg){.math}
-dimensional action
![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math},
for a diagonal Gaussian with mean ![\\mu =
\\mu\_{\\theta}(s)](_images/math/0b9672dcfd65483d710b61a359dcabea32dab1f6.svg){.math}
and standard deviation ![\\sigma =
\\sigma\_{\\theta}(s)](_images/math/20acc318d574242ee023ecdb36f3651847016480.svg){.math},
is given by

::: {.last .math}
![\\log \\pi\_{\\theta}(a\|s) = -\\frac{1}{2}\\left(\\sum\_{i=1}\^k
\\left(\\frac{(a_i - \\mu_i)\^2}{\\sigma_i\^2} + 2 \\log \\sigma_i
\\right) + k \\log 2\\pi
\\right).](_images/math/26f82323a4055444b30fa791238ec90913a12d7b.svg)
:::
:::::
::::::::
::::::::::::::::::

:::::::: {#rl_intro.xhtml_trajectories .section}
### Trajectories

A trajectory
![\\tau](_images/math/67a5412645decf6424bdd97aed3e9e7601bd784f.svg){.math}
is a sequence of states and actions in the world,

::: math
![\\tau = (s_0, a_0, s_1, a_1,
\...).](_images/math/8337d86159a1cd98dfcd0601993d7b6b2fbb54d9.svg)
:::

The very first state of the world,
![s_0](_images/math/bf047f4b5c542c1bfbaf4bf411919f5e1f7ecba8.svg){.math},
is randomly sampled from the **start-state distribution**, sometimes
denoted by
![\\rho_0](_images/math/2d44ad6f01d4e56266daa8e3b35bd4f298e25788.svg){.math}:

::: math
![s_0 \\sim
\\rho_0(\\cdot).](_images/math/eef23a6502b9cec4bc399bcbce93547c3723643c.svg)
:::

State transitions (what happens to the world between the state at time
![t](_images/math/7ed8f1921a380f7a5f45b87825838fdced658554.svg){.math},
![s_t](_images/math/4fcf0bf03c2a691496ce04ade269159d8b89caa5.svg){.math},
and the state at
![t+1](_images/math/55c6e4a64640ac5e7b4da87ff4bcf12da93ef252.svg){.math},
![s\_{t+1}](_images/math/4b669c18a22476afbab2c49bb68525256b416cff.svg){.math}),
are governed by the natural laws of the environment, and depend on only
the most recent action,
![a_t](_images/math/39079fcebc9eb2aba4ab3fe7359b34807ceccc0e.svg){.math}.
They can be either deterministic,

::: math
![s\_{t+1} = f(s_t,
a_t)](_images/math/16da6346104894fb6a673473cbfc9ffeba6471fa.svg)
:::

or stochastic,

::: math
![s\_{t+1} \\sim P(\\cdot\|s_t,
a_t).](_images/math/872390af4f5b2541d17e7ef2bfaecbe1e9746d94.svg)
:::

Actions come from an agent according to its policy.

::: {.admonition-you-should-know .admonition}
You Should Know

Trajectories are also frequently called **episodes** or **rollouts**.
:::
::::::::

::::::: {#rl_intro.xhtml_reward-and-return .section}
### Reward and Return

The reward function
![R](_images/math/1f9d30d011e9fe548e999c9bfcf3fccfa27ec3ff.svg){.math}
is critically important in reinforcement learning. It depends on the
current state of the world, the action just taken, and the next state of
the world:

::: math
![r_t = R(s_t, a_t,
s\_{t+1})](_images/math/6ed565b0911f12c8ef64d93a617d8bb30380d5d5.svg)
:::

although frequently this is simplified to just a dependence on the
current state, ![r_t =
R(s_t)](_images/math/4befde40a79499d3655bebda93423e2661036f0d.svg){.math},
or state-action pair ![r_t =
R(s_t,a_t)](_images/math/3a66e4711a16a69ca64bd10d96985363d6e4bc5c.svg){.math}.

The goal of the agent is to maximize some notion of cumulative reward
over a trajectory, but this actually can mean a few things. We'll notate
all of these cases with
![R(\\tau)](_images/math/c2d6738c058406ade40dcf870311db157ed80e0f.svg){.math},
and it will either be clear from context which case we mean, or it won't
matter (because the same equations will apply to all cases).

One kind of return is the **finite-horizon undiscounted return**, which
is just the sum of rewards obtained in a fixed window of steps:

::: math
![R(\\tau) = \\sum\_{t=0}\^T
r_t.](_images/math/b2466507811fc9b9cbe2a0a51fd36034e16f2780.svg)
:::

Another kind of return is the **infinite-horizon discounted return**,
which is the sum of all rewards *ever* obtained by the agent, but
discounted by how far off in the future they're obtained. This
formulation of reward includes a discount factor ![\\gamma \\in
(0,1)](_images/math/7c0000152970a235979a501b70bd05c781a8b1ec.svg){.math}:

::: math
![R(\\tau) = \\sum\_{t=0}\^{\\infty} \\gamma\^t
r_t.](_images/math/bf49428c66c91a45d7b66a432450ee49a3622348.svg)
:::

Why would we ever want a discount factor, though? Don't we just want to
get *all* rewards? We do, but the discount factor is both intuitively
appealing and mathematically convenient. On an intuitive level: cash now
is better than cash later. Mathematically: an infinite-horizon sum of
rewards [may not
converge](https://en.wikipedia.org/wiki/Convergent_series){.reference
.external}[
\[https://en.wikipedia.org/wiki/Convergent_series\]]{.link-target} to a
finite value, and is hard to deal with in equations. But with a discount
factor and under reasonable conditions, the infinite sum converges.

::: {.admonition-you-should-know .admonition}
You Should Know

While the line between these two formulations of return are quite stark
in RL formalism, deep RL practice tends to blur the line a fair
bit---for instance, we frequently set up algorithms to optimize the
undiscounted return, but use discount factors in estimating **value
functions**.
:::
:::::::

:::::: {#rl_intro.xhtml_the-rl-problem .section}
### The RL Problem

Whatever the choice of return measure (whether infinite-horizon
discounted, or finite-horizon undiscounted), and whatever the choice of
policy, the goal in RL is to select a policy which maximizes **expected
return** when the agent acts according to it.

To talk about expected return, we first have to talk about probability
distributions over trajectories.

Let's suppose that both the environment transitions and the policy are
stochastic. In this case, the probability of a
![T](_images/math/844fe92e58a680253626f9b0706a06c578a4e040.svg){.math}
-step trajectory is:

::: math
![P(\\tau\|\\pi) = \\rho_0 (s_0) \\prod\_{t=0}\^{T-1} P(s\_{t+1} \| s_t,
a_t) \\pi(a_t \|
s_t).](_images/math/69369e7fae3098a2f05a79680fbecbf48a4e7f66.svg)
:::

The expected return (for whichever measure), denoted by
![J(\\pi)](_images/math/89397c4cc47a40c3466507e1330dc380458f762e.svg){.math},
is then:

::: math
![J(\\pi) = \\int\_{\\tau} P(\\tau\|\\pi) R(\\tau) = \\underE{\\tau\\sim
\\pi}{R(\\tau)}.](_images/math/f0d6e3879540e318df14d2c8b68af828b1b350da.svg)
:::

The central optimization problem in RL can then be expressed by

::: math
![\\pi\^\* = \\arg \\max\_{\\pi}
J(\\pi),](_images/math/2de61070bf8758d03104b4f15df45c8ff5a86f5a.svg)
:::

with
![\\pi\^\*](_images/math/1fbf259ac070c92161e32b93c0f64705a8f18f0a.svg){.math}
being the **optimal policy**.
::::::

::::::: {#rl_intro.xhtml_value-functions .section}
### Value Functions

It's often useful to know the **value** of a state, or state-action
pair. By value, we mean the expected return if you start in that state
or state-action pair, and then act according to a particular policy
forever after. **Value functions** are used, one way or another, in
almost every RL algorithm.

There are four main functions of note here.

1.  The **On-Policy Value Function**,
    ![V\^{\\pi}(s)](_images/math/a81303323c25fc13cd0652ca46d7596276e5cb7e.svg){.math},
    which gives the expected return if you start in state
    ![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}
    and always act according to policy
    ![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}:

    > :::: {}
    > ::: math
    > ![V\^{\\pi}(s) = \\underE{\\tau \\sim \\pi}{R(\\tau)\\left\| s_0 =
    > s\\right.}](_images/math/e043709b46c9aa6811953dabd82461db6308fe19.svg)
    > :::
    > ::::

2.  The **On-Policy Action-Value Function**,
    ![Q\^{\\pi}(s,a)](_images/math/86549c5748a6fdd134970fd88f4842bd862a8b25.svg){.math},
    which gives the expected return if you start in state
    ![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math},
    take an arbitrary action
    ![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math}
    (which may not have come from the policy), and then forever after
    act according to policy
    ![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}:

    > :::: {}
    > ::: math
    > ![Q\^{\\pi}(s,a) = \\underE{\\tau \\sim \\pi}{R(\\tau)\\left\| s_0
    > = s, a_0 =
    > a\\right.}](_images/math/85d41c8c383a96e1ed34fc66f14abd61b132dd28.svg)
    > :::
    > ::::

3.  The **Optimal Value Function**,
    ![V\^\*(s)](_images/math/6159ad57fb5294b812e76c6260a65dc5ffa2a5f7.svg){.math},
    which gives the expected return if you start in state
    ![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}
    and always act according to the *optimal* policy in the environment:

    > :::: {}
    > ::: math
    > ![V\^\*(s) = \\max\_{\\pi} \\underE{\\tau \\sim
    > \\pi}{R(\\tau)\\left\| s_0 =
    > s\\right.}](_images/math/01d48ea453ecb7b560ea7d42144ae24422fbd0eb.svg)
    > :::
    > ::::

4.  The **Optimal Action-Value Function**,
    ![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math},
    which gives the expected return if you start in state
    ![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math},
    take an arbitrary action
    ![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math},
    and then forever after act according to the *optimal* policy in the
    environment:

    > :::: {}
    > ::: math
    > ![Q\^\*(s,a) = \\max\_{\\pi} \\underE{\\tau \\sim
    > \\pi}{R(\\tau)\\left\| s_0 = s, a_0 =
    > a\\right.}](_images/math/bc92e8ce1cf0aaa212e144d5ed74e3b115453cb6.svg)
    > :::
    > ::::

::: {.admonition-you-should-know .admonition}
You Should Know

When we talk about value functions, if we do not make reference to
time-dependence, we only mean expected **infinite-horizon discounted
return**. Value functions for finite-horizon undiscounted return would
need to accept time as an argument. Can you think about why? Hint: what
happens when time's up?
:::

::::: {.admonition-you-should-know .admonition}
You Should Know

There are two key connections between the value function and the
action-value function that come up pretty often:

::: math
![V\^{\\pi}(s) = \\underE{a\\sim
\\pi}{Q\^{\\pi}(s,a)},](_images/math/5151391b2cd2bfa909a3b5a057b6c93d4191790b.svg)
:::

and

::: math
![V\^\*(s) = \\max_a Q\^\*
(s,a).](_images/math/4cbd255e1ecc9f7083034be12148e8b98cefc2ee.svg)
:::

These relations follow pretty directly from the definitions just given:
can you prove them?
:::::
:::::::

:::: {#rl_intro.xhtml_the-optimal-q-function-and-the-optimal-action .section}
### The Optimal Q-Function and the Optimal Action

There is an important connection between the optimal action-value
function
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}
and the action selected by the optimal policy. By definition,
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}
gives the expected return for starting in state
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math},
taking (arbitrary) action
![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math},
and then acting according to the optimal policy forever after.

The optimal policy in
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}
will select whichever action maximizes the expected return from starting
in
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}.
As a result, if we have
![Q\^\*](_images/math/c2e969d09ae88d847429eac9a8494cc89cabe4bd.svg){.math},
we can directly obtain the optimal action,
![a\^\*(s)](_images/math/baf715aa6a295b7b7d85e1e1123552c5ae705756.svg){.math},
via

::: math
![a\^\*(s) = \\arg \\max_a Q\^\*
(s,a).](_images/math/42490c4d812c9ca1fc226684577900bc8bdd609b.svg)
:::

Note: there may be multiple actions which maximize
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math},
in which case, all of them are optimal, and the optimal policy may
randomly select any of them. But there is always an optimal policy which
deterministically selects an action.
::::

:::::: {#rl_intro.xhtml_bellman-equations .section}
### Bellman Equations

All four of the value functions obey special self-consistency equations
called **Bellman equations**. The basic idea behind the Bellman
equations is this:

> ::: {}
> The value of your starting point is the reward you expect to get from
> being there, plus the value of wherever you land next.
> :::

The Bellman equations for the on-policy value functions are

::: math
![\\begin{align\*} V\^{\\pi}(s) &= \\underE{a \\sim \\pi \\\\ s\'\\sim
P}{r(s,a) + \\gamma V\^{\\pi}(s\')}, \\\\ Q\^{\\pi}(s,a) &=
\\underE{s\'\\sim P}{r(s,a) + \\gamma \\underE{a\'\\sim
\\pi}{Q\^{\\pi}(s\',a\')}},
\\end{align\*}](_images/math/7e4a2964e190104a669406ca5e1e320a5da8bae0.svg)
:::

where ![s\' \\sim
P](_images/math/411171ab57c4bec0d86c9f4b495106ba5d73decc.svg){.math} is
shorthand for ![s\' \\sim P(\\cdot
\|s,a)](_images/math/ed45f9d37dbb092727104773ca3a464d46f892b8.svg){.math},
indicating that the next state
![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math}
is sampled from the environment's transition rules; ![a \\sim
\\pi](_images/math/e87025074e03131c69c6c5758e873a6224ea5d3a.svg){.math}
is shorthand for ![a \\sim
\\pi(\\cdot\|s)](_images/math/35c684d9cc672fd0bbacd896f49abdd986f40b02.svg){.math};
and ![a\' \\sim
\\pi](_images/math/b3f46cc6cd6c2fa9068013fafbe1b4b029bb8a58.svg){.math}
is shorthand for ![a\' \\sim
\\pi(\\cdot\|s\')](_images/math/6eb25f9175aa0471d7a7728ab237a92fef5009e9.svg){.math}.

The Bellman equations for the optimal value functions are

::: math
![\\begin{align\*} V\^\*(s) &= \\max_a \\underE{s\'\\sim P}{r(s,a) +
\\gamma V\^\*(s\')}, \\\\ Q\^\*(s,a) &= \\underE{s\'\\sim P}{r(s,a) +
\\gamma \\max\_{a\'} Q\^\*(s\',a\')}.
\\end{align\*}](_images/math/f8ab9b211bc9bb91cde189360051e3bd1f896afa.svg)
:::

The crucial difference between the Bellman equations for the on-policy
value functions and the optimal value functions, is the absence or
presence of the
![\\max](_images/math/a52117d0fa54eb8449482447cad9c0ab54c757cc.svg){.math}
over actions. Its inclusion reflects the fact that whenever the agent
gets to choose its action, in order to act optimally, it has to pick
whichever action leads to the highest value.

::: {.admonition-you-should-know .admonition}
You Should Know

The term "Bellman backup" comes up quite frequently in the RL
literature. The Bellman backup for a state, or state-action pair, is the
right-hand side of the Bellman equation: the reward-plus-next-value.
:::
::::::

::::: {#rl_intro.xhtml_advantage-functions .section}
### Advantage Functions

Sometimes in RL, we don't need to describe how good an action is in an
absolute sense, but only how much better it is than others on average.
That is to say, we want to know the relative **advantage** of that
action. We make this concept precise with the **advantage function.**

The advantage function
![A\^{\\pi}(s,a)](_images/math/09f82f133e9f89a59ba22266639c4968b5641c28.svg){.math}
corresponding to a policy
![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}
describes how much better it is to take a specific action
![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math}
in state
![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math},
over randomly selecting an action according to
![\\pi(\\cdot\|s)](_images/math/8d2c2c23f74e7a0cf98b0ee1de016825eb50e2d4.svg){.math},
assuming you act according to
![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}
forever after. Mathematically, the advantage function is defined by

::: math
![A\^{\\pi}(s,a) = Q\^{\\pi}(s,a) -
V\^{\\pi}(s).](_images/math/3748974cc061fb4065fa46dd6271395d59f22040.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

We'll discuss this more later, but the advantage function is crucially
important to policy gradient methods.
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#rl_intro.xhtml_optional-formalism .section}
## [(Optional) Formalism](#rl_intro.xhtml_id5){.toc-backref}

So far, we've discussed the agent's environment in an informal way, but
if you try to go digging through the literature, you're likely to run
into the standard mathematical formalism for this setting: **Markov
Decision Processes** (MDPs). An MDP is a 5-tuple, ![\\langle S, A, R, P,
\\rho_0
\\rangle](_images/math/a7e1a4549f45dc56849b1ff857a19a71f9cc02a6.svg){.math},
where

- ![S](_images/math/bbe16bfd192df4894eaef8bfe3133325ba462202.svg){.math}
  is the set of all valid states,
- ![A](_images/math/a236fe76423c33d18465350c1c36cef9aa8fdc31.svg){.math}
  is the set of all valid actions,
- ![R : S \\times A \\times S \\to
  \\mathbb{R}](_images/math/eac18a6e37a9272c1458d3086adb317ecda571e8.svg){.math}
  is the reward function, with ![r_t = R(s_t, a_t,
  s\_{t+1})](_images/math/444ffe3079b81e8b1c42e462f0b6d63fbeeec6c6.svg){.math},
- ![P : S \\times A \\to
  \\mathcal{P}(S)](_images/math/3923c00b0df8f8c1003312d5c125275bd10598ba.svg){.math}
  is the transition probability function, with
  ![P(s\'\|s,a)](_images/math/655bf048edfc8ffd3b4655504e874a622ed888ce.svg){.math}
  being the probability of transitioning into state
  ![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math}
  if you start in state
  ![s](_images/math/96ac51b9afe79581e48f2f3f0ad3faa0f4402cc7.svg){.math}
  and take action
  ![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math},
- and
  ![\\rho_0](_images/math/2d44ad6f01d4e56266daa8e3b35bd4f298e25788.svg){.math}
  is the starting state distribution.

The name Markov Decision Process refers to the fact that the system
obeys the [Markov
property](https://en.wikipedia.org/wiki/Markov_property){.reference
.external}[
\[https://en.wikipedia.org/wiki/Markov_property\]]{.link-target}:
transitions only depend on the most recent state and action, and no
prior history.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#rl_intro2.xhtml}

::::::::::::: {.body role="main"}
:::::::::::: {#rl_intro2.xhtml_part-2-kinds-of-rl-algorithms .section}
# [Part 2: Kinds of RL Algorithms](#rl_intro2.xhtml_id19){.toc-backref}

::: {#rl_intro2.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Part 2: Kinds of RL
  Algorithms](#rl_intro2.xhtml_part-2-kinds-of-rl-algorithms){#rl_intro2.xhtml_id19
  .reference .internal}
  - [A Taxonomy of RL
    Algorithms](#rl_intro2.xhtml_a-taxonomy-of-rl-algorithms){#rl_intro2.xhtml_id20
    .reference .internal}
  - [Links to Algorithms in
    Taxonomy](#rl_intro2.xhtml_links-to-algorithms-in-taxonomy){#rl_intro2.xhtml_id21
    .reference .internal}
:::

Now that we've gone through the basics of RL terminology and notation,
we can cover a little bit of the richer material: the landscape of
algorithms in modern RL, and a description of the kinds of trade-offs
that go into algorithm design.

::::::::: {#rl_intro2.xhtml_a-taxonomy-of-rl-algorithms .section}
## [A Taxonomy of RL Algorithms](#rl_intro2.xhtml_id20){.toc-backref}

::: {#rl_intro2.xhtml_id18 .figure .align-center}
![../\_images/rl_algorithms_9_15.svg](_images/rl_algorithms_9_15.svg)

[A non-exhaustive, but useful taxonomy of algorithms in modern RL.
[Citations below.](#rl_intro2.xhtml_citations-below){.reference
.internal}]{.caption-text}
:::

We'll start this section with a disclaimer: it's really quite hard to
draw an accurate, all-encompassing taxonomy of algorithms in the modern
RL space, because the modularity of algorithms is not well-represented
by a tree structure. Also, to make something that fits on a page and is
reasonably digestible in an introduction essay, we have to omit quite a
bit of more advanced material (exploration, transfer learning, meta
learning, etc). That said, our goals here are

- to highlight the most foundational design choices in deep RL
  algorithms about what to learn and how to learn it,
- to expose the trade-offs in those choices,
- and to place a few prominent modern algorithms into context with
  respect to those choices.

::: {#rl_intro2.xhtml_model-free-vs-model-based-rl .section}
### Model-Free vs Model-Based RL

One of the most important branching points in an RL algorithm is the
question of **whether the agent has access to (or learns) a model of the
environment**. By a model of the environment, we mean a function which
predicts state transitions and rewards.

The main upside to having a model is that **it allows the agent to
plan** by thinking ahead, seeing what would happen for a range of
possible choices, and explicitly deciding between its options. Agents
can then distill the results from planning ahead into a learned policy.
A particularly famous example of this approach is
[AlphaZero](https://arxiv.org/abs/1712.01815){.reference .external}[
\[https://arxiv.org/abs/1712.01815\]]{.link-target}. When this works, it
can result in a substantial improvement in sample efficiency over
methods that don't have a model.

The main downside is that **a ground-truth model of the environment is
usually not available to the agent.** If an agent wants to use a model
in this case, it has to learn the model purely from experience, which
creates several challenges. The biggest challenge is that bias in the
model can be exploited by the agent, resulting in an agent which
performs well with respect to the learned model, but behaves
sub-optimally (or super terribly) in the real environment.
Model-learning is fundamentally hard, so even intense effort---being
willing to throw lots of time and compute at it---can fail to pay off.

Algorithms which use a model are called **model-based** methods, and
those that don't are called **model-free**. While model-free methods
forego the potential gains in sample efficiency from using a model, they
tend to be easier to implement and tune. As of the time of writing this
introduction (September 2018), model-free methods are more popular and
have been more extensively developed and tested than model-based
methods.
:::

::::: {#rl_intro2.xhtml_what-to-learn .section}
### What to Learn

Another critical branching point in an RL algorithm is the question of
**what to learn.** The list of usual suspects includes

- policies, either stochastic or deterministic,
- action-value functions (Q-functions),
- value functions,
- and/or environment models.

:::: {#rl_intro2.xhtml_what-to-learn-in-model-free-rl .section}
#### What to Learn in Model-Free RL

There are two main approaches to representing and training agents with
model-free RL:

**Policy Optimization.** Methods in this family represent a policy
explicitly as
![\\pi\_{\\theta}(a\|s)](_images/math/400068784a9d13ffe96c61f29b4ab26ad5557376.svg){.math}.
They optimize the parameters
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math}
either directly by gradient ascent on the performance objective
![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math},
or indirectly, by maximizing local approximations of
![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math}.
This optimization is almost always performed **on-policy**, which means
that each update only uses data collected while acting according to the
most recent version of the policy. Policy optimization also usually
involves learning an approximator
![V\_{\\phi}(s)](_images/math/693bb706835fbd5903ad9758837acecd07ef13b1.svg){.math}
for the on-policy value function
![V\^{\\pi}(s)](_images/math/a81303323c25fc13cd0652ca46d7596276e5cb7e.svg){.math},
which gets used in figuring out how to update the policy.

A couple of examples of policy optimization methods are:

- [A2C / A3C](https://arxiv.org/abs/1602.01783){.reference .external}[
  \[https://arxiv.org/abs/1602.01783\]]{.link-target}, which performs
  gradient ascent to directly maximize performance,
- and [PPO](https://arxiv.org/abs/1707.06347){.reference .external}[
  \[https://arxiv.org/abs/1707.06347\]]{.link-target}, whose updates
  indirectly maximize performance, by instead maximizing a *surrogate
  objective* function which gives a conservative estimate for how much
  ![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math}
  will change as a result of the update.

**Q-Learning.** Methods in this family learn an approximator
![Q\_{\\theta}(s,a)](_images/math/de947d14fdcfaa155ef3301fc39efcf9e6c9449c.svg){.math}
for the optimal action-value function,
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}.
Typically they use an objective function based on the [Bellman
equation](rl_intro.html_bellman-equations){.reference .external}. This
optimization is almost always performed **off-policy**, which means that
each update can use data collected at any point during training,
regardless of how the agent was choosing to explore the environment when
the data was obtained. The corresponding policy is obtained via the
connection between
![Q\^\*](_images/math/c2e969d09ae88d847429eac9a8494cc89cabe4bd.svg){.math}
and
![\\pi\^\*](_images/math/1fbf259ac070c92161e32b93c0f64705a8f18f0a.svg){.math}:
the actions taken by the Q-learning agent are given by

::: math
![a(s) = \\arg \\max_a
Q\_{\\theta}(s,a).](_images/math/d353412962e458573b92aac78df3fbe0a10d998d.svg)
:::

Examples of Q-learning methods include

- [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf){.reference
  .external}[
  \[https://www.cs.toronto.edu/\~vmnih/docs/dqn.pdf\]]{.link-target}, a
  classic which substantially launched the field of deep RL,
- and [C51](https://arxiv.org/abs/1707.06887){.reference .external}[
  \[https://arxiv.org/abs/1707.06887\]]{.link-target}, a variant that
  learns a distribution over return whose expectation is
  ![Q\^\*](_images/math/c2e969d09ae88d847429eac9a8494cc89cabe4bd.svg){.math}.

**Trade-offs Between Policy Optimization and Q-Learning.** The primary
strength of policy optimization methods is that they are principled, in
the sense that *you directly optimize for the thing you want.* This
tends to make them stable and reliable. By contrast, Q-learning methods
only *indirectly* optimize for agent performance, by training
![Q\_{\\theta}](_images/math/713b5ea31ad66705079ea5786dd84e06944402b7.svg){.math}
to satisfy a self-consistency equation. There are many failure modes for
this kind of learning, so it tends to be less stable.
[\[1\]](#rl_intro2.xhtml_id2){#rl_intro2.xhtml_id1 .footnote-reference}
But, Q-learning methods gain the advantage of being substantially more
sample efficient when they do work, because they can reuse data more
effectively than policy optimization techniques.

**Interpolating Between Policy Optimization and Q-Learning.**
Serendipitously, policy optimization and Q-learning are not incompatible
(and under some circumstances, it turns out,
[equivalent](https://arxiv.org/abs/1704.06440){.reference .external}[
\[https://arxiv.org/abs/1704.06440\]]{.link-target}), and there exist a
range of algorithms that live in between the two extremes. Algorithms
that live on this spectrum are able to carefully trade-off between the
strengths and weaknesses of either side. Examples include

- [DDPG](https://arxiv.org/abs/1509.02971){.reference .external}[
  \[https://arxiv.org/abs/1509.02971\]]{.link-target}, an algorithm
  which concurrently learns a deterministic policy and a Q-function by
  using each to improve the other,
- and [SAC](https://arxiv.org/abs/1801.01290){.reference .external}[
  \[https://arxiv.org/abs/1801.01290\]]{.link-target}, a variant which
  uses stochastic policies, entropy regularization, and a few other
  tricks to stabilize learning and score higher than DDPG on standard
  benchmarks.

  -------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#rl_intro2.xhtml_id1){.fn-backref}   For more information about how and why Q-learning methods can fail, see 1) this classic paper by [Tsitsiklis and van Roy](http://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf){.reference .external}[ \[http://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf\]]{.link-target}, 2) the (much more recent) [review by Szepesvari](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf){.reference .external}[ \[https://sites.ualberta.ca/\~szepesva/papers/RLAlgsInMDPs.pdf\]]{.link-target} (in section 4.3.2), and 3) chapter 11 of [Sutton and Barto](https://drive.google.com/file/d/1xeUDVGWGUUv1-ccUMAZHJLej2C7aAFWY/view){.reference .external}[ \[https://drive.google.com/file/d/1xeUDVGWGUUv1-ccUMAZHJLej2C7aAFWY/view\]]{.link-target}, especially section 11.3 (on "the deadly triad" of function approximation, bootstrapping, and off-policy data, together causing instability in value-learning algorithms).
  -------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
::::
:::::

::: {#rl_intro2.xhtml_what-to-learn-in-model-based-rl .section}
### What to Learn in Model-Based RL

Unlike model-free RL, there aren't a small number of easy-to-define
clusters of methods for model-based RL: there are many orthogonal ways
of using models. We'll give a few examples, but the list is far from
exhaustive. In each case, the model may either be given or learned.

**Background: Pure Planning.** The most basic approach *never*
explicitly represents the policy, and instead, uses pure planning
techniques like [model-predictive
control](https://en.wikipedia.org/wiki/Model_predictive_control){.reference
.external}[
\[https://en.wikipedia.org/wiki/Model_predictive_control\]]{.link-target}
(MPC) to select actions. In MPC, each time the agent observes the
environment, it computes a plan which is optimal with respect to the
model, where the plan describes all actions to take over some fixed
window of time after the present. (Future rewards beyond the horizon may
be considered by the planning algorithm through the use of a learned
value function.) The agent then executes the first action of the plan,
and immediately discards the rest of it. It computes a new plan each
time it prepares to interact with the environment, to avoid using an
action from a plan with a shorter-than-desired planning horizon.

- The [MBMF](https://sites.google.com/view/mbmf){.reference .external}[
  \[https://sites.google.com/view/mbmf\]]{.link-target} work explores
  MPC with learned environment models on some standard benchmark tasks
  for deep RL.

**Expert Iteration.** A straightforward follow-on to pure planning
involves using and learning an explicit representation of the policy,
![\\pi\_{\\theta}(a\|s)](_images/math/400068784a9d13ffe96c61f29b4ab26ad5557376.svg){.math}.
The agent uses a planning algorithm (like Monte Carlo Tree Search) in
the model, generating candidate actions for the plan by sampling from
its current policy. The planning algorithm produces an action which is
better than what the policy alone would have produced, hence it is an
"expert" relative to the policy. The policy is afterwards updated to
produce an action more like the planning algorithm's output.

- The [ExIt](https://arxiv.org/abs/1705.08439){.reference .external}[
  \[https://arxiv.org/abs/1705.08439\]]{.link-target} algorithm uses
  this approach to train deep neural networks to play Hex.
- [AlphaZero](https://arxiv.org/abs/1712.01815){.reference .external}[
  \[https://arxiv.org/abs/1712.01815\]]{.link-target} is another example
  of this approach.

**Data Augmentation for Model-Free Methods.** Use a model-free RL
algorithm to train a policy or Q-function, but either 1) augment real
experiences with fictitious ones in updating the agent, or 2) use *only*
fictitous experience for updating the agent.

- See [MBVE](https://arxiv.org/abs/1803.00101){.reference .external}[
  \[https://arxiv.org/abs/1803.00101\]]{.link-target} for an example of
  augmenting real experiences with fictitious ones.
- See [World Models](https://worldmodels.github.io/){.reference
  .external}[ \[https://worldmodels.github.io/\]]{.link-target} for an
  example of using purely fictitious experience to train the agent,
  which they call "training in the dream."

**Embedding Planning Loops into Policies.** Another approach embeds the
planning procedure directly into a policy as a subroutine---so that
complete plans become side information for the policy---while training
the output of the policy with any standard model-free algorithm. The key
concept is that in this framework, the policy can learn to choose how
and when to use the plans. This makes model bias less of a problem,
because if the model is bad for planning in some states, the policy can
simply learn to ignore it.

- See [I2A](https://arxiv.org/abs/1707.06203){.reference .external}[
  \[https://arxiv.org/abs/1707.06203\]]{.link-target} for an example of
  agents being endowed with this style of imagination.
:::
:::::::::

::: {#rl_intro2.xhtml_links-to-algorithms-in-taxonomy .section}
## [Links to Algorithms in Taxonomy](#rl_intro2.xhtml_id21){.toc-backref}

[]{#rl_intro2.xhtml_citations-below .target}

  ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[2\]   [A2C / A3C](https://arxiv.org/abs/1602.01783){.reference .external}[ \[https://arxiv.org/abs/1602.01783\]]{.link-target} (Asynchronous Advantage Actor-Critic): Mnih et al, 2016
  ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[3\]   [PPO](https://arxiv.org/abs/1707.06347){.reference .external}[ \[https://arxiv.org/abs/1707.06347\]]{.link-target} (Proximal Policy Optimization): Schulman et al, 2017
  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[4\]   [TRPO](https://arxiv.org/abs/1502.05477){.reference .external}[ \[https://arxiv.org/abs/1502.05477\]]{.link-target} (Trust Region Policy Optimization): Schulman et al, 2015
  ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[5\]   [DDPG](https://arxiv.org/abs/1509.02971){.reference .external}[ \[https://arxiv.org/abs/1509.02971\]]{.link-target} (Deep Deterministic Policy Gradient): Lillicrap et al, 2015
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[6\]   [TD3](https://arxiv.org/abs/1802.09477){.reference .external}[ \[https://arxiv.org/abs/1802.09477\]]{.link-target} (Twin Delayed DDPG): Fujimoto et al, 2018
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[7\]   [SAC](https://arxiv.org/abs/1801.01290){.reference .external}[ \[https://arxiv.org/abs/1801.01290\]]{.link-target} (Soft Actor-Critic): Haarnoja et al, 2018
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[8\]   [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf){.reference .external}[ \[https://www.cs.toronto.edu/\~vmnih/docs/dqn.pdf\]]{.link-target} (Deep Q-Networks): Mnih et al, 2013
  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[9\]   [C51](https://arxiv.org/abs/1707.06887){.reference .external}[ \[https://arxiv.org/abs/1707.06887\]]{.link-target} (Categorical 51-Atom DQN): Bellemare et al, 2017
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[10\]   [QR-DQN](https://arxiv.org/abs/1710.10044){.reference .external}[ \[https://arxiv.org/abs/1710.10044\]]{.link-target} (Quantile Regression DQN): Dabney et al, 2017
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[11\]   [HER](https://arxiv.org/abs/1707.01495){.reference .external}[ \[https://arxiv.org/abs/1707.01495\]]{.link-target} (Hindsight Experience Replay): Andrychowicz et al, 2017
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  \[12\]   [World Models](https://worldmodels.github.io/){.reference .external}[ \[https://worldmodels.github.io/\]]{.link-target}: Ha and Schmidhuber, 2018
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[13\]   [I2A](https://arxiv.org/abs/1707.06203){.reference .external}[ \[https://arxiv.org/abs/1707.06203\]]{.link-target} (Imagination-Augmented Agents): Weber et al, 2017
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[14\]   [MBMF](https://sites.google.com/view/mbmf){.reference .external}[ \[https://sites.google.com/view/mbmf\]]{.link-target} (Model-Based RL with Model-Free Fine-Tuning): Nagabandi et al, 2017
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[15\]   [MBVE](https://arxiv.org/abs/1803.00101){.reference .external}[ \[https://arxiv.org/abs/1803.00101\]]{.link-target} (Model-Based Value Expansion): Feinberg et al, 2018
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------
  \[16\]   [AlphaZero](https://arxiv.org/abs/1712.01815){.reference .external}[ \[https://arxiv.org/abs/1712.01815\]]{.link-target}: Silver et al, 2017
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------
:::
::::::::::::
:::::::::::::

[]{#rl_intro3.xhtml}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#rl_intro3.xhtml_part-3-intro-to-policy-optimization .section}
# [Part 3: Intro to Policy Optimization](#rl_intro3.xhtml_id7){.toc-backref}

::: {#rl_intro3.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Part 3: Intro to Policy
  Optimization](#rl_intro3.xhtml_part-3-intro-to-policy-optimization){#rl_intro3.xhtml_id7
  .reference .internal}
  - [Deriving the Simplest Policy
    Gradient](#rl_intro3.xhtml_deriving-the-simplest-policy-gradient){#rl_intro3.xhtml_id8
    .reference .internal}
  - [Implementing the Simplest Policy
    Gradient](#rl_intro3.xhtml_implementing-the-simplest-policy-gradient){#rl_intro3.xhtml_id9
    .reference .internal}
  - [Expected Grad-Log-Prob
    Lemma](#rl_intro3.xhtml_expected-grad-log-prob-lemma){#rl_intro3.xhtml_id10
    .reference .internal}
  - [Don't Let the Past Distract
    You](#rl_intro3.xhtml_don-t-let-the-past-distract-you){#rl_intro3.xhtml_id11
    .reference .internal}
  - [Implementing Reward-to-Go Policy
    Gradient](#rl_intro3.xhtml_implementing-reward-to-go-policy-gradient){#rl_intro3.xhtml_id12
    .reference .internal}
  - [Baselines in Policy
    Gradients](#rl_intro3.xhtml_baselines-in-policy-gradients){#rl_intro3.xhtml_id13
    .reference .internal}
  - [Other Forms of the Policy
    Gradient](#rl_intro3.xhtml_other-forms-of-the-policy-gradient){#rl_intro3.xhtml_id14
    .reference .internal}
  - [Recap](#rl_intro3.xhtml_recap){#rl_intro3.xhtml_id15 .reference
    .internal}
:::

In this section, we'll discuss the mathematical foundations of policy
optimization algorithms, and connect the material to sample code. We
will cover three key results in the theory of **policy gradients**:

- [the simplest
  equation](rl_intro3.html_deriving-the-simplest-policy-gradient){.reference
  .external} describing the gradient of policy performance with respect
  to policy parameters,
- a rule which allows us to [drop useless
  terms](rl_intro3.html_don-t-let-the-past-distract-you){.reference
  .external} from that expression,
- and a rule which allows us to [add useful
  terms](rl_intro3.html_baselines-in-policy-gradients){.reference
  .external} to that expression.

In the end, we'll tie those results together and describe the
advantage-based expression for the policy gradient---the version we use
in our [Vanilla Policy Gradient](../algorithms/vpg.html){.reference
.external} implementation.

::::::::::: {#rl_intro3.xhtml_deriving-the-simplest-policy-gradient .section}
## [Deriving the Simplest Policy Gradient](#rl_intro3.xhtml_id8){.toc-backref}

Here, we consider the case of a stochastic, parameterized policy,
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}.
We aim to maximize the expected return ![J(\\pi\_{\\theta}) =
\\underE{\\tau \\sim
\\pi\_{\\theta}}{R(\\tau)}](_images/math/42bfa236d63e32e501baf89345748061540e102d.svg){.math}.
For the purposes of this derivation, we'll take
![R(\\tau)](_images/math/c2d6738c058406ade40dcf870311db157ed80e0f.svg){.math}
to give the [finite-horizon undiscounted
return](rl_intro.html_reward-and-return){.reference .external}, but the
derivation for the infinite-horizon discounted return setting is almost
identical.

We would like to optimize the policy by gradient ascent, eg

::: math
![\\theta\_{k+1} = \\theta_k + \\alpha \\left. \\nabla\_{\\theta}
J(\\pi\_{\\theta})
\\right\|\_{\\theta_k}.](_images/math/595de3acc68fed2ec24c11420d9abbee013497ac.svg)
:::

The gradient of policy performance, ![\\nabla\_{\\theta}
J(\\pi\_{\\theta})](_images/math/fdc185c68404ece5c4deef076c9713af689421a2.svg){.math},
is called the **policy gradient**, and algorithms that optimize the
policy this way are called **policy gradient algorithms.** (Examples
include Vanilla Policy Gradient and TRPO. PPO is often referred to as a
policy gradient algorithm, though this is slightly inaccurate.)

To actually use this algorithm, we need an expression for the policy
gradient which we can numerically compute. This involves two steps: 1)
deriving the analytical gradient of policy performance, which turns out
to have the form of an expected value, and then 2) forming a sample
estimate of that expected value, which can be computed with data from a
finite number of agent-environment interaction steps.

In this subsection, we'll find the simplest form of that expression. In
later subsections, we'll show how to improve on the simplest form to get
the version we actually use in standard policy gradient implementations.

We'll begin by laying out a few facts which are useful for deriving the
analytical gradient.

**1. Probability of a Trajectory.** The probability of a trajectory
![\\tau = (s_0, a_0, \...,
s\_{T+1})](_images/math/59f955ca56f900cb9be25620d7c974afc0e77f32.svg){.math}
given that actions come from
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}
is

::: math
![P(\\tau\|\\theta) = \\rho_0 (s_0) \\prod\_{t=0}\^{T} P(s\_{t+1}\|s_t,
a_t) \\pi\_{\\theta}(a_t
\|s_t).](_images/math/cbc185e90569437c9216ea06df6e91244df1972b.svg)
:::

**2. The Log-Derivative Trick.** The log-derivative trick is based on a
simple rule from calculus: the derivative of ![\\log
x](_images/math/fe3fe64e081ed066a8e6a1719b6f3fc8ed9b98dc.svg){.math}
with respect to
![x](_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg){.math}
is
![1/x](_images/math/37ea41f23266fbdbb332134f34f65bc547e3601d.svg){.math}.
When rearranged and combined with chain rule, we get:

::: math
![\\nabla\_{\\theta} P(\\tau \| \\theta) = P(\\tau \| \\theta)
\\nabla\_{\\theta} \\log P(\\tau \|
\\theta).](_images/math/8025b1c01b73e7f373fa438c15743c5391e2f28f.svg)
:::

**3. Log-Probability of a Trajectory.** The log-prob of a trajectory is
just

::: math
![\\log P(\\tau\|\\theta) = \\log \\rho_0 (s_0) + \\sum\_{t=0}\^{T}
\\bigg( \\log P(s\_{t+1}\|s_t, a_t) + \\log \\pi\_{\\theta}(a_t
\|s_t)\\bigg).](_images/math/2c8b420444accb2f54391017f28ab21b97bab0ee.svg)
:::

**4. Gradients of Environment Functions.** The environment has no
dependence on
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math},
so gradients of
![\\rho_0(s_0)](_images/math/cd870494ffa26602c4ede5257356d572045ebb9e.svg){.math},
![P(s\_{t+1}\|s_t,
a_t)](_images/math/d5f6af878d6a1071f29a9dda286b52ef53ece0e3.svg){.math},
and
![R(\\tau)](_images/math/c2d6738c058406ade40dcf870311db157ed80e0f.svg){.math}
are zero.

**5. Grad-Log-Prob of a Trajectory.** The gradient of the log-prob of a
trajectory is thus

::: math
![\\nabla\_{\\theta} \\log P(\\tau \| \\theta) &=
\\cancel{\\nabla\_{\\theta} \\log \\rho_0 (s_0)} + \\sum\_{t=0}\^{T}
\\bigg( \\cancel{\\nabla\_{\\theta} \\log P(s\_{t+1}\|s_t, a_t)} +
\\nabla\_{\\theta} \\log \\pi\_{\\theta}(a_t \|s_t)\\bigg) \\\\ &=
\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log \\pi\_{\\theta}(a_t
\|s_t).](_images/math/3ef66d94ee26cfa69015915dbd112ea78fb5e7ba.svg)
:::

Putting it all together, we derive the following:

:::: {.admonition-derivation-for-basic-policy-gradient .admonition}
Derivation for Basic Policy Gradient

::: {.last .math}
![\\begin{align\*} \\nabla\_{\\theta} J(\\pi\_{\\theta}) &=
\\nabla\_{\\theta} \\underE{\\tau \\sim \\pi\_{\\theta}}{R(\\tau)} &
\\\\ &= \\nabla\_{\\theta} \\int\_{\\tau} P(\\tau\|\\theta) R(\\tau) &
\\text{Expand expectation} \\\\ &= \\int\_{\\tau} \\nabla\_{\\theta}
P(\\tau\|\\theta) R(\\tau) & \\text{Bring gradient under integral} \\\\
&= \\int\_{\\tau} P(\\tau\|\\theta) \\nabla\_{\\theta} \\log
P(\\tau\|\\theta) R(\\tau) & \\text{Log-derivative trick} \\\\ &=
\\underE{\\tau \\sim \\pi\_{\\theta}}{\\nabla\_{\\theta} \\log
P(\\tau\|\\theta) R(\\tau)} & \\text{Return to expectation form} \\\\
\\therefore \\nabla\_{\\theta} J(\\pi\_{\\theta}) &= \\underE{\\tau
\\sim \\pi\_{\\theta}}{\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t) R(\\tau)} & \\text{Expression for
grad-log-prob}
\\end{align\*}](_images/math/b5e135d2ae389147267372abc1c5b20e644ec881.svg)
:::
::::

This is an expectation, which means that we can estimate it with a
sample mean. If we collect a set of trajectories ![\\mathcal{D} =
\\{\\tau_i\\}\_{i=1,\...,N}](_images/math/fcfe0c7093afb2538a298abf5bf8dc0bc435fbb0.svg){.math}
where each trajectory is obtained by letting the agent act in the
environment using the policy
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math},
the policy gradient can be estimated with

::: math
![\\hat{g} = \\frac{1}{\|\\mathcal{D}\|} \\sum\_{\\tau \\in
\\mathcal{D}} \\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t)
R(\\tau),](_images/math/3d29a18c0f98b1cdb656ecdf261ee37ffe8bb74b.svg)
:::

where
![\|\\mathcal{D}\|](_images/math/9818d8f4b97ecbea56ebfb3c0a8890faca55c4de.svg){.math}
is the number of trajectories in
![\\mathcal{D}](_images/math/8c5790e22c3e4fca88012b71d8b024c66699cba5.svg){.math}
(here,
![N](_images/math/9d2283e49e17a5e18105bf77e0cc9382192d2510.svg){.math}).

This last expression is the simplest version of the computable
expression we desired. Assuming that we have represented our policy in a
way which allows us to calculate ![\\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a\|s)](_images/math/0a5342e24606940a10098d0cdf85d5e5e346ed72.svg){.math},
and if we are able to run the policy in the environment to collect the
trajectory dataset, we can compute the policy gradient and take an
update step.
:::::::::::

:::::::::::::: {#rl_intro3.xhtml_implementing-the-simplest-policy-gradient .section}
## [Implementing the Simplest Policy Gradient](#rl_intro3.xhtml_id9){.toc-backref}

We give a short PyTorch implementation of this simple version of the
policy gradient algorithm in
[`spinup/examples/pytorch/pg_math/1_simple_pg.py`{.docutils
.literal}]{.pre}. (It can also be viewed [on
github](https://github.com/openai/spinningup/blob/master/spinup/examples/pytorch/pg_math/1_simple_pg.py){.reference
.external}[
\[https://github.com/openai/spinningup/blob/master/spinup/examples/pytorch/pg_math/1_simple_pg.py\]]{.link-target}.)
It is only 128 lines long, so we highly recommend reading through it in
depth. While we won't go through the entirety of the code here, we'll
highlight and explain a few important pieces.

::: {.admonition-you-should-know .admonition}
You Should Know

This section was previously written with a Tensorflow example. The old
Tensorflow section can be found
[here](extra_tf_pg_implementation.html_implementing-the-simplest-policy-gradient){.reference
.external}.
:::

**1. Making the Policy Network.**

::: highlight-python
+-----------------------------------+---------------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                                   |
|     30                            |     # make core of policy network                                               |
|     31                            |     logits_net = mlp(sizes=[obs_dim]+hidden_sizes+[n_acts])                     |
|     32                            |                                                                                 |
|     33                            |     # make function to compute action distribution                              |
|     34                            |     def get_policy(obs):                                                        |
|     35                            |         logits = logits_net(obs)                                                |
|     36                            |         return Categorical(logits=logits)                                       |
|     37                            |                                                                                 |
|     38                            |     # make action selection function (outputs int actions, sampled from policy) |
|     39                            |     def get_action(obs):                                                        |
|     40                            |         return get_policy(obs).sample().item()                                  |
| :::                               | :::                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------+
:::

This block builds modules and functions for using a feedforward neural
network categorical policy. (See the [Stochastic
Policies](rl_intro.html_stochastic-policies){.reference .external}
section in Part 1 for a refresher.) The output from the
[`logits_net`{.docutils .literal}]{.pre} module can be used to construct
log-probabilities and probabilities for actions, and the
[`get_action`{.docutils .literal}]{.pre} function samples actions based
on probabilities computed from the logits. (Note: this particular
[`get_action`{.docutils .literal}]{.pre} function assumes that there
will only be one [`obs`{.docutils .literal}]{.pre} provided, and
therefore only one integer action output. That's why it uses
[`.item()`{.docutils .literal}]{.pre}, which is used to [get the
contents of a Tensor with only one
element](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.item){.reference
.external}[
\[https://pytorch.org/docs/stable/tensors.html#torch.Tensor.item\]]{.link-target}.)

A lot of work in this example is getting done by the
[`Categorical`{.docutils .literal}]{.pre} object on L36. This is a
PyTorch [`Distribution`{.docutils .literal}]{.pre} object that wraps up
some mathematical functions associated with probability distributions.
In particular, it has a method for sampling from the distribution (which
we use on L40) and a method for computing log probabilities of given
samples (which we use later). Since PyTorch distributions are really
useful for RL, check out [their
documentation](https://pytorch.org/docs/stable/distributions.html){.reference
.external}[
\[https://pytorch.org/docs/stable/distributions.html\]]{.link-target} to
get a feel for how they work.

:::: {.admonition-you-should-know .admonition}
You Should Know

Friendly reminder! When we talk about a categorical distribution having
"logits," what we mean is that the probabilities for each outcome are
given by the Softmax function of the logits. That is, the probability
for action
![j](_images/math/b42a5fa0aad66603180aff0fc5e346e98a2364ca.svg){.math}
under a categorical distribution with logits
![x_j](_images/math/3292288e05ddeecc31b25cde7cc7aeafff61bf43.svg){.math}
is:

::: {.last .math}
![p_j = \\frac{\\exp(x_j)}{\\sum\_{i}
\\exp(x_i)}](_images/math/54e96f0cfda9010b97808eae635a2200e1482829.svg)
:::
::::

**2. Making the Loss Function.**

::: highlight-python
+-----------------------------------+---------------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                                   |
|     42                            |     # make loss function whose gradient, for the right data, is policy gradient |
|     43                            |     def compute_loss(obs, act, weights):                                        |
|     44                            |         logp = get_policy(obs).log_prob(act)                                    |
|     45                            |         return -(logp * weights).mean()                                         |
| :::                               | :::                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------+
:::

In this block, we build a "loss" function for the policy gradient
algorithm. When the right data is plugged in, the gradient of this loss
is equal to the policy gradient. The right data means a set of (state,
action, weight) tuples collected while acting according to the current
policy, where the weight for a state-action pair is the return from the
episode to which it belongs. (Although as we will show in later
subsections, there are other values you can plug in for the weight which
also work correctly.)

::: {.admonition-you-should-know .admonition}
You Should Know

Even though we describe this as a loss function, it is **not** a loss
function in the typical sense from supervised learning. There are two
main differences from standard loss functions.

**1. The data distribution depends on the parameters.** A loss function
is usually defined on a fixed data distribution which is independent of
the parameters we aim to optimize. Not so here, where the data must be
sampled on the most recent policy.

**2. It doesn't measure performance.** A loss function usually evaluates
the performance metric that we care about. Here, we care about expected
return,
![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math},
but our "loss" function does not approximate this at all, even in
expectation. This "loss" function is only useful to us because, when
evaluated at the current parameters, with data generated by the current
parameters, it has the negative gradient of performance.

But after that first step of gradient descent, there is no more
connection to performance. This means that minimizing this "loss"
function, for a given batch of data, has *no* guarantee whatsoever of
improving expected return. You can send this loss to
![-\\infty](_images/math/5d7bd7abcf6c1c07becaa8b5fe1a2a000e559a50.svg){.math}
and policy performance could crater; in fact, it usually will. Sometimes
a deep RL researcher might describe this outcome as the policy
"overfitting" to a batch of data. This is descriptive, but should not be
taken literally because it does not refer to generalization error.

We raise this point because it is common for ML practitioners to
interpret a loss function as a useful signal during training---"if the
loss goes down, all is well." In policy gradients, this intuition is
wrong, and you should only care about average return. The loss function
means nothing.
:::

::::: {.admonition-you-should-know .admonition}
You Should Know

The approach used here to make the [`logp`{.docutils .literal}]{.pre}
tensor--calling the [`log_prob`{.docutils .literal}]{.pre} method of a
PyTorch [`Categorical`{.docutils .literal}]{.pre} object--may require
some modification to work with other kinds of distribution objects.

For example, if you are using a [Normal
distribution](https://pytorch.org/docs/stable/distributions.html#normal){.reference
.external}[
\[https://pytorch.org/docs/stable/distributions.html#normal\]]{.link-target}
(for a diagonal Gaussian policy), the output from calling
[`policy.log_prob(act)`{.docutils .literal}]{.pre} will give you a
Tensor containing separate log probabilities for each component of each
vector-valued action. That is to say, you put in a Tensor of shape
[`(batch,`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`act_dim)`{.docutils .literal}]{.pre}, and get out a Tensor of
shape [`(batch,`{.docutils .literal}]{.pre}` `{.docutils
.literal}[`act_dim)`{.docutils .literal}]{.pre}, when what you need for
making an RL loss is a Tensor of shape [`(batch,)`{.docutils
.literal}]{.pre}. In that case, you would sum up the log probabilities
of the action components to get the log probabilities of the actions.
That is, you would compute:

:::: {.last .highlight-python}
::: highlight
    logp = get_policy(obs).log_prob(act).sum(axis=-1)
:::
::::
:::::

**3. Running One Epoch of Training.**

::: highlight-python
+-----------------------------------+-----------------------------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                                                 |
|      50                           |     # for training policy                                                                     |
|      51                           |     def train_one_epoch():                                                                    |
|      52                           |         # make some empty lists for logging.                                                  |
|      53                           |         batch_obs = []          # for observations                                            |
|      54                           |         batch_acts = []         # for actions                                                 |
|      55                           |         batch_weights = []      # for R(tau) weighting in policy gradient                     |
|      56                           |         batch_rets = []         # for measuring episode returns                               |
|      57                           |         batch_lens = []         # for measuring episode lengths                               |
|      58                           |                                                                                               |
|      59                           |         # reset episode-specific variables                                                    |
|      60                           |         obs = env.reset()       # first obs comes from starting distribution                  |
|      61                           |         done = False            # signal from environment that episode is over                |
|      62                           |         ep_rews = []            # list for rewards accrued throughout ep                      |
|      63                           |                                                                                               |
|      64                           |         # render first episode of each epoch                                                  |
|      65                           |         finished_rendering_this_epoch = False                                                 |
|      66                           |                                                                                               |
|      67                           |         # collect experience by acting in the environment with current policy                 |
|      68                           |         while True:                                                                           |
|      69                           |                                                                                               |
|      70                           |             # rendering                                                                       |
|      71                           |             if (not finished_rendering_this_epoch) and render:                                |
|      72                           |                 env.render()                                                                  |
|      73                           |                                                                                               |
|      74                           |             # save obs                                                                        |
|      75                           |             batch_obs.append(obs.copy())                                                      |
|      76                           |                                                                                               |
|      77                           |             # act in the environment                                                          |
|      78                           |             act = get_action(torch.as_tensor(obs, dtype=torch.float32))                       |
|      79                           |             obs, rew, done, _ = env.step(act)                                                 |
|      80                           |                                                                                               |
|      81                           |             # save action, reward                                                             |
|      82                           |             batch_acts.append(act)                                                            |
|      83                           |             ep_rews.append(rew)                                                               |
|      84                           |                                                                                               |
|      85                           |             if done:                                                                          |
|      86                           |                 # if episode is over, record info about episode                               |
|      87                           |                 ep_ret, ep_len = sum(ep_rews), len(ep_rews)                                   |
|      88                           |                 batch_rets.append(ep_ret)                                                     |
|      89                           |                 batch_lens.append(ep_len)                                                     |
|      90                           |                                                                                               |
|      91                           |                 # the weight for each logprob(a|s) is R(tau)                                  |
|      92                           |                 batch_weights += [ep_ret] * ep_len                                            |
|      93                           |                                                                                               |
|      94                           |                 # reset episode-specific variables                                            |
|      95                           |                 obs, done, ep_rews = env.reset(), False, []                                   |
|      96                           |                                                                                               |
|      97                           |                 # won't render again this epoch                                               |
|      98                           |                 finished_rendering_this_epoch = True                                          |
|      99                           |                                                                                               |
|     100                           |                 # end experience loop if we have enough of it                                 |
|     101                           |                 if len(batch_obs) > batch_size:                                               |
|     102                           |                     break                                                                     |
|     103                           |                                                                                               |
|     104                           |         # take a single policy gradient update step                                           |
|     105                           |         optimizer.zero_grad()                                                                 |
|     106                           |         batch_loss = compute_loss(obs=torch.as_tensor(batch_obs, dtype=torch.float32),        |
|     107                           |                                   act=torch.as_tensor(batch_acts, dtype=torch.int32),         |
|     108                           |                                   weights=torch.as_tensor(batch_weights, dtype=torch.float32) |
|     109                           |                                   )                                                           |
|     110                           |         batch_loss.backward()                                                                 |
|     111                           |         optimizer.step()                                                                      |
|     112                           |         return batch_loss, batch_rets, batch_lens                                             |
| :::                               | :::                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------+
:::

The [`train_one_epoch()`{.docutils .literal}]{.pre} function runs one
"epoch" of policy gradient, which we define to be

1.  the experience collection step (L67-102), where the agent acts for
    some number of episodes in the environment using the most recent
    policy, followed by
2.  a single policy gradient update step (L104-111).

The main loop of the algorithm just repeatedly calls
[`train_one_epoch()`{.docutils .literal}]{.pre}.

::: {.admonition-you-should-know .admonition}
You Should Know

If you aren't already familiar with optimization in PyTorch, observe the
pattern for taking one gradient descent step as shown in lines 104-111.
First, clear the gradient buffers. Then, compute the loss function.
Then, compute a backward pass on the loss function; this accumulates
fresh gradients into the gradient buffers. Finally, take a step with the
optimizer.
:::
::::::::::::::

:::::::: {#rl_intro3.xhtml_expected-grad-log-prob-lemma .section}
## [Expected Grad-Log-Prob Lemma](#rl_intro3.xhtml_id10){.toc-backref}

In this subsection, we will derive an intermediate result which is
extensively used throughout the theory of policy gradients. We will call
it the Expected Grad-Log-Prob (EGLP) lemma.
[\[1\]](#rl_intro3.xhtml_id2){#rl_intro3.xhtml_id1 .footnote-reference}

**EGLP Lemma.** Suppose that
![P\_{\\theta}](_images/math/9c44674c334586fd6d417281ea223857ea3ee0d6.svg){.math}
is a parameterized probability distribution over a random variable,
![x](_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg){.math}.
Then:

::: math
![\\underE{x \\sim P\_{\\theta}}{\\nabla\_{\\theta} \\log
P\_{\\theta}(x)} =
0.](_images/math/f7a02965e7c07537dfb98391da78ab7613e887f7.svg)
:::

:::::: {.admonition-proof .admonition}
Proof

Recall that all probability distributions are *normalized*:

::: math
![\\int_x P\_{\\theta}(x) =
1.](_images/math/cc70eeb5c704222ca73cf6d2a7b28b8ae2f2e2aa.svg)
:::

Take the gradient of both sides of the normalization condition:

::: math
![\\nabla\_{\\theta} \\int_x P\_{\\theta}(x) = \\nabla\_{\\theta} 1 =
0.](_images/math/acde4d18e221ccd91e93e6ca4e25ae84d05f29d8.svg)
:::

Use the log derivative trick to get:

::: {.last .math}
![0 &= \\nabla\_{\\theta} \\int_x P\_{\\theta}(x) \\\\ &= \\int_x
\\nabla\_{\\theta} P\_{\\theta}(x) \\\\ &= \\int_x P\_{\\theta}(x)
\\nabla\_{\\theta} \\log P\_{\\theta}(x) \\\\ \\therefore 0 &=
\\underE{x \\sim P\_{\\theta}}{\\nabla\_{\\theta} \\log
P\_{\\theta}(x)}.](_images/math/479e34ecc40103079f87e46e47837f3c066d30bd.svg)
:::
::::::

  -------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#rl_intro3.xhtml_id1){.fn-backref}   The author of this article is not aware of this lemma being given a standard name anywhere in the literature. But given how often it comes up, it seems pretty worthwhile to give it some kind of name for ease of reference.
  -------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
::::::::

::::::: {#rl_intro3.xhtml_don-t-let-the-past-distract-you .section}
## [Don't Let the Past Distract You](#rl_intro3.xhtml_id11){.toc-backref}

Examine our most recent expression for the policy gradient:

::: math
![\\nabla\_{\\theta} J(\\pi\_{\\theta}) = \\underE{\\tau \\sim
\\pi\_{\\theta}}{\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t)
R(\\tau)}.](_images/math/e8b721fa0eb7fa2aa4b088106518b3ee88ff7707.svg)
:::

Taking a step with this gradient pushes up the log-probabilities of each
action in proportion to
![R(\\tau)](_images/math/c2d6738c058406ade40dcf870311db157ed80e0f.svg){.math},
the sum of *all rewards ever obtained*. But this doesn't make much
sense.

Agents should really only reinforce actions on the basis of their
*consequences*. Rewards obtained before taking an action have no bearing
on how good that action was: only rewards that come *after*.

It turns out that this intuition shows up in the math, and we can show
that the policy gradient can also be expressed by

::: math
![\\nabla\_{\\theta} J(\\pi\_{\\theta}) = \\underE{\\tau \\sim
\\pi\_{\\theta}}{\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t) \\sum\_{t\'=t}\^T R(s\_{t\'}, a\_{t\'},
s\_{t\'+1})}.](_images/math/62e6b4e06a1c35fac29e94103988cdc6e940660b.svg)
:::

In this form, actions are only reinforced based on rewards obtained
after they are taken.

We'll call this form the "reward-to-go policy gradient," because the sum
of rewards after a point in a trajectory,

::: math
![\\hat{R}\_t \\doteq \\sum\_{t\'=t}\^T R(s\_{t\'}, a\_{t\'},
s\_{t\'+1}),](_images/math/d299609cb8b73f294e77708f9cdc6ea0024b6c6c.svg)
:::

is called the **reward-to-go** from that point, and this policy gradient
expression depends on the reward-to-go from state-action pairs.

::: {.admonition-you-should-know .admonition}
You Should Know

**But how is this better?** A key problem with policy gradients is how
many sample trajectories are needed to get a low-variance sample
estimate for them. The formula we started with included terms for
reinforcing actions proportional to past rewards, all of which had zero
mean, but nonzero variance: as a result, they would just add noise to
sample estimates of the policy gradient. By removing them, we reduce the
number of sample trajectories needed.
:::

An (optional) proof of this claim can be found
[[\`here\`\_]{#rl_intro3.xhtml_id17
.problematic}](#rl_intro3.xhtml_id16), and it ultimately depends on the
EGLP lemma.
:::::::

::::::: {#rl_intro3.xhtml_implementing-reward-to-go-policy-gradient .section}
## [Implementing Reward-to-Go Policy Gradient](#rl_intro3.xhtml_id12){.toc-backref}

We give a short PyTorch implementation of the reward-to-go policy
gradient in [`spinup/examples/pytorch/pg_math/2_rtg_pg.py`{.docutils
.literal}]{.pre}. (It can also be viewed [on
github](https://github.com/openai/spinningup/blob/master/spinup/examples/pytorch/pg_math/2_rtg_pg.py){.reference
.external}[
\[https://github.com/openai/spinningup/blob/master/spinup/examples/pytorch/pg_math/2_rtg_pg.py\]]{.link-target}.)

The only thing that has changed from [`1_simple_pg.py`{.docutils
.literal}]{.pre} is that we now use different weights in the loss
function. The code modification is very slight: we add a new function,
and change two other lines. The new function is:

::: highlight-python
+-----------------------------------+---------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                 |
|     17                            |     def reward_to_go(rews):                                   |
|     18                            |         n = len(rews)                                         |
|     19                            |         rtgs = np.zeros_like(rews)                            |
|     20                            |         for i in reversed(range(n)):                          |
|     21                            |             rtgs[i] = rews[i] + (rtgs[i+1] if i+1 < n else 0) |
|     22                            |         return rtgs                                           |
| :::                               | :::                                                           |
+-----------------------------------+---------------------------------------------------------------+
:::

And then we tweak the old L91-92 from:

::: highlight-python
+-----------------------------------+------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                    |
|     91                            |                     # the weight for each logprob(a|s) is R(tau) |
|     92                            |                     batch_weights += [ep_ret] * ep_len           |
| :::                               | :::                                                              |
+-----------------------------------+------------------------------------------------------------------+
:::

to:

::: highlight-python
+-----------------------------------+-----------------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                                     |
|     98                            |                     # the weight for each logprob(a_t|s_t) is reward-to-go from t |
|     99                            |                     batch_weights += list(reward_to_go(ep_rews))                  |
| :::                               | :::                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------+
:::

::: {.admonition-you-should-know .admonition}
You Should Know

This section was previously written with a Tensorflow example. The old
Tensorflow section can be found
[here](extra_tf_pg_implementation.html_implementing-reward-to-go-policy-gradient){.reference
.external}.
:::
:::::::

::::::::: {#rl_intro3.xhtml_baselines-in-policy-gradients .section}
## [Baselines in Policy Gradients](#rl_intro3.xhtml_id13){.toc-backref}

An immediate consequence of the EGLP lemma is that for any function
![b](_images/math/99ac829ad51642abad0797da299214e7ce1da722.svg){.math}
which only depends on state,

::: math
![\\underE{a_t \\sim \\pi\_{\\theta}}{\\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t\|s_t) b(s_t)} =
0.](_images/math/3bedd2ab2262f396f232d49c8c85621ce5397955.svg)
:::

This allows us to add or subtract any number of terms like this from our
expression for the policy gradient, without changing it in expectation:

::: math
![\\nabla\_{\\theta} J(\\pi\_{\\theta}) = \\underE{\\tau \\sim
\\pi\_{\\theta}}{\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t) \\left(\\sum\_{t\'=t}\^T R(s\_{t\'},
a\_{t\'}, s\_{t\'+1}) -
b(s_t)\\right)}.](_images/math/3a111dcb6e04aa632bd69e9a7e769e06e2530a0a.svg)
:::

Any function
![b](_images/math/99ac829ad51642abad0797da299214e7ce1da722.svg){.math}
used in this way is called a **baseline**.

The most common choice of baseline is the [on-policy value
function](rl_intro.html_value-functions){.reference .external}
![V\^{\\pi}(s_t)](_images/math/263857fcb5eaaf46a4e9a5e6ce2be414d95748aa.svg){.math}.
Recall that this is the average return an agent gets if it starts in
state
![s_t](_images/math/4fcf0bf03c2a691496ce04ade269159d8b89caa5.svg){.math}
and then acts according to policy
![\\pi](_images/math/1ae2bd722da01b3a89ffc139af2437c28364a966.svg){.math}
for the rest of its life.

Empirically, the choice ![b(s_t) =
V\^{\\pi}(s_t)](_images/math/67567dbe29590f80b62fd2221481df61e502a450.svg){.math}
has the desirable effect of reducing variance in the sample estimate for
the policy gradient. This results in faster and more stable policy
learning. It is also appealing from a conceptual angle: it encodes the
intuition that if an agent gets what it expected, it should "feel"
neutral about it.

:::::: {.admonition-you-should-know .admonition}
You Should Know

In practice,
![V\^{\\pi}(s_t)](_images/math/263857fcb5eaaf46a4e9a5e6ce2be414d95748aa.svg){.math}
cannot be computed exactly, so it has to be approximated. This is
usually done with a neural network,
![V\_{\\phi}(s_t)](_images/math/d313ca98e5fb043c581841a09ea19bce2ce53b04.svg){.math},
which is updated concurrently with the policy (so that the value network
always approximates the value function of the most recent policy).

The simplest method for learning
![V\_{\\phi}](_images/math/4be08f55c234dcd60641540fb682afc3e988ae17.svg){.math},
used in most implementations of policy optimization algorithms
(including VPG, TRPO, PPO, and A2C), is to minimize a mean-squared-error
objective:

::: math
![\\phi_k = \\arg \\min\_{\\phi} \\underE{s_t, \\hat{R}\_t \\sim
\\pi_k}{\\left( V\_{\\phi}(s_t) - \\hat{R}\_t
\\right)\^2},](_images/math/a82208dd637243514710948c4ebbc3c59e9a2e57.svg)
:::

:::: line-block
::: line
\
:::
::::

where
![\\pi_k](_images/math/35e7c0260233cac2eb0745c92a34cfaa21e558cb.svg){.math}
is the policy at epoch
![k](_images/math/a29aa94bd66ac7a6bb3195233fd9a9df8575af86.svg){.math}.
This is done with one or more steps of gradient descent, starting from
the previous value parameters
![\\phi\_{k-1}](_images/math/ba40df6b8d4ee942c6856a8d919ce01fc92096f6.svg){.math}.
::::::
:::::::::

::::::::::: {#rl_intro3.xhtml_other-forms-of-the-policy-gradient .section}
## [Other Forms of the Policy Gradient](#rl_intro3.xhtml_id14){.toc-backref}

What we have seen so far is that the policy gradient has the general
form

::: math
![\\nabla\_{\\theta} J(\\pi\_{\\theta}) = \\underE{\\tau \\sim
\\pi\_{\\theta}}{\\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t \|s_t)
\\Phi_t},](_images/math/eb524fc4ce3052c9058d2221471ac8b302c9c023.svg)
:::

where
![\\Phi_t](_images/math/7bec6ad1be0afd7200e874effc2db6d9cafb3ea4.svg){.math}
could be any of

::: math
![\\Phi_t &=
R(\\tau),](_images/math/cecde3d5124076dfc773c8fa658e61f41cb3efc2.svg)
:::

or

::: math
![\\Phi_t &= \\sum\_{t\'=t}\^T R(s\_{t\'}, a\_{t\'},
s\_{t\'+1}),](_images/math/02a2c10508e4a4c018634a2ba03384350faa7cab.svg)
:::

or

::: math
![\\Phi_t &= \\sum\_{t\'=t}\^T R(s\_{t\'}, a\_{t\'}, s\_{t\'+1}) -
b(s_t).](_images/math/65fd02144cdac143a61396dc8fe585e8db5f7d81.svg)
:::

All of these choices lead to the same expected value for the policy
gradient, despite having different variances. It turns out that there
are two more valid choices of weights
![\\Phi_t](_images/math/7bec6ad1be0afd7200e874effc2db6d9cafb3ea4.svg){.math}
which are important to know.

**1. On-Policy Action-Value Function.** The choice

::: math
![\\Phi_t = Q\^{\\pi\_{\\theta}}(s_t,
a_t)](_images/math/90381ce64af2629806c052198d4a0851ff6be36b.svg)
:::

is also valid. See [this
page](../spinningup/extra_pg_proof2.html){.reference .external} for an
(optional) proof of this claim.

**2. The Advantage Function.** Recall that the [advantage of an
action](rl_intro.html_advantage-functions){.reference .external},
defined by ![A\^{\\pi}(s_t,a_t) = Q\^{\\pi}(s_t,a_t) -
V\^{\\pi}(s_t)](_images/math/e2d2e497244979ed8fe62fe2e994a6b49039580c.svg){.math},
describes how much better or worse it is than other actions on average
(relative to the current policy). This choice,

::: math
![\\Phi_t = A\^{\\pi\_{\\theta}}(s_t,
a_t)](_images/math/e67e0f92306202526b49c7d0a7a6239ba68a7abc.svg)
:::

is also valid. The proof is that it's equivalent to using ![\\Phi_t =
Q\^{\\pi\_{\\theta}}(s_t,
a_t)](_images/math/71febd8462276063cccd137802934788492dc5f1.svg){.math}
and then using a value function baseline, which we are always free to
do.

::: {.admonition-you-should-know .admonition}
You Should Know

The formulation of policy gradients with advantage functions is
extremely common, and there are many different ways of estimating the
advantage function used by different algorithms.
:::

::: {.admonition-you-should-know .admonition}
You Should Know

For a more detailed treatment of this topic, you should read the paper
on [Generalized Advantage
Estimation](https://arxiv.org/abs/1506.02438){.reference .external}[
\[https://arxiv.org/abs/1506.02438\]]{.link-target} (GAE), which goes
into depth about different choices of
![\\Phi_t](_images/math/7bec6ad1be0afd7200e874effc2db6d9cafb3ea4.svg){.math}
in the background sections.

That paper then goes on to describe GAE, a method for approximating the
advantage function in policy optimization algorithms which enjoys
widespread use. For instance, Spinning Up's implementations of VPG,
TRPO, and PPO make use of it. As a result, we strongly advise you to
study it.
:::
:::::::::::

::: {#rl_intro3.xhtml_recap .section}
## [Recap](#rl_intro3.xhtml_id15){.toc-backref}

In this chapter, we described the basic theory of policy gradient
methods and connected some of the early results to code examples. The
interested student should continue from here by studying how the later
results (value function baselines and the advantage formulation of
policy gradients) translate into Spinning Up's implementation of
[Vanilla Policy Gradient](../algorithms/vpg.html){.reference .external}.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#spinningup.xhtml}

:::::::::::: {.body role="main"}
::::::::::: {#spinningup.xhtml_spinning-up-as-a-deep-rl-researcher .section}
# [Spinning Up as a Deep RL Researcher](#spinningup.xhtml_id49){.toc-backref}

By Joshua Achiam, October 13th, 2018

::: {#spinningup.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Spinning Up as a Deep RL
  Researcher](#spinningup.xhtml_spinning-up-as-a-deep-rl-researcher){#spinningup.xhtml_id49
  .reference .internal}
  - [The Right
    Background](#spinningup.xhtml_the-right-background){#spinningup.xhtml_id50
    .reference .internal}
  - [Learn by
    Doing](#spinningup.xhtml_learn-by-doing){#spinningup.xhtml_id51
    .reference .internal}
  - [Developing a Research
    Project](#spinningup.xhtml_developing-a-research-project){#spinningup.xhtml_id52
    .reference .internal}
  - [Doing Rigorous Research in
    RL](#spinningup.xhtml_doing-rigorous-research-in-rl){#spinningup.xhtml_id53
    .reference .internal}
  - [Closing
    Thoughts](#spinningup.xhtml_closing-thoughts){#spinningup.xhtml_id54
    .reference .internal}
  - [PS: Other
    Resources](#spinningup.xhtml_ps-other-resources){#spinningup.xhtml_id55
    .reference .internal}
  - [References](#spinningup.xhtml_references){#spinningup.xhtml_id56
    .reference .internal}
:::

If you're an aspiring deep RL researcher, you've probably heard all
kinds of things about deep RL by this point. You know that [it's hard
and it doesn't always
work](https://www.alexirpan.com/2018/02/14/rl-hard.html){.reference
.external}[
\[https://www.alexirpan.com/2018/02/14/rl-hard.html\]]{.link-target}.
That even when you're following a recipe,
[reproducibility](https://arxiv.org/abs/1708.04133){.reference
.external}[ \[https://arxiv.org/abs/1708.04133\]]{.link-target} [is a
challenge](https://arxiv.org/abs/1709.06560){.reference .external}[
\[https://arxiv.org/abs/1709.06560\]]{.link-target}. And that if you're
starting from scratch, [the learning curve is incredibly
steep](http://amid.fish/reproducing-deep-rl){.reference .external}[
\[http://amid.fish/reproducing-deep-rl\]]{.link-target}. It's also the
case that there are a lot of
[great](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html){.reference
.external}[
\[http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html\]]{.link-target}
[resources](http://rll.berkeley.edu/deeprlcourse/){.reference
.external}[ \[http://rll.berkeley.edu/deeprlcourse/\]]{.link-target}
[out](https://sites.google.com/view/deep-rl-bootcamp/lectures){.reference
.external}[
\[https://sites.google.com/view/deep-rl-bootcamp/lectures\]]{.link-target}
[there](http://joschu.net/docs/nuts-and-bolts.pdf){.reference
.external}[
\[http://joschu.net/docs/nuts-and-bolts.pdf\]]{.link-target}, but the
material is new enough that there's not a clear, well-charted path to
mastery. The goal of this column is to help you get past the initial
hurdle, and give you a clear sense of how to spin up as a deep RL
researcher. In particular, this will outline a useful curriculum for
increasing raw knowledge, while interleaving it with the odds and ends
that lead to better research.

::: {#spinningup.xhtml_the-right-background .section}
## [The Right Background](#spinningup.xhtml_id50){.toc-backref}

**Build up a solid mathematical background.** From probability and
statistics, feel comfortable with random variables, Bayes' theorem,
chain rule of probability, expected values, standard deviations, and
importance sampling. From multivariate calculus, understand gradients
and (optionally, but it'll help) Taylor series expansions.

**Build up a general knowledge of deep learning.** You don't need to
know every single special trick and architecture, but the basics help.
Know about standard architectures
([MLP](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/){.reference
.external}[
\[http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/\]]{.link-target},
[vanilla
RNN](http://karpathy.github.io/2015/05/21/rnn-effectiveness/){.reference
.external}[
\[http://karpathy.github.io/2015/05/21/rnn-effectiveness/\]]{.link-target},
[LSTM](https://arxiv.org/abs/1503.04069){.reference .external}[
\[https://arxiv.org/abs/1503.04069\]]{.link-target} ([also see this
blog](http://colah.github.io/posts/2015-08-Understanding-LSTMs/){.reference
.external}[
\[http://colah.github.io/posts/2015-08-Understanding-LSTMs/\]]{.link-target}),
[GRU](https://arxiv.org/abs/1412.3555v1){.reference .external}[
\[https://arxiv.org/abs/1412.3555v1\]]{.link-target},
[conv](http://colah.github.io/posts/2014-07-Conv-Nets-Modular/){.reference
.external}[
\[http://colah.github.io/posts/2014-07-Conv-Nets-Modular/\]]{.link-target}
[layers](https://cs231n.github.io/convolutional-networks/){.reference
.external}[
\[https://cs231n.github.io/convolutional-networks/\]]{.link-target},
[resnets](https://arxiv.org/abs/1512.03385){.reference .external}[
\[https://arxiv.org/abs/1512.03385\]]{.link-target},
[attention](https://arxiv.org/abs/1409.0473){.reference .external}[
\[https://arxiv.org/abs/1409.0473\]]{.link-target}
[mechanisms](https://arxiv.org/abs/1706.03762){.reference .external}[
\[https://arxiv.org/abs/1706.03762\]]{.link-target}), common
regularizers ([weight
decay](https://papers.nips.cc/paper/563-a-simple-weight-decay-can-improve-generalization.pdf){.reference
.external}[
\[https://papers.nips.cc/paper/563-a-simple-weight-decay-can-improve-generalization.pdf\]]{.link-target},
[dropout](http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf){.reference
.external}[
\[http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf\]]{.link-target}),
normalization ([batch norm](https://arxiv.org/abs/1502.03167){.reference
.external}[ \[https://arxiv.org/abs/1502.03167\]]{.link-target}, [layer
norm](https://arxiv.org/abs/1607.06450){.reference .external}[
\[https://arxiv.org/abs/1607.06450\]]{.link-target}, [weight
norm](https://arxiv.org/abs/1602.07868){.reference .external}[
\[https://arxiv.org/abs/1602.07868\]]{.link-target}), and optimizers
([SGD, momentum
SGD](http://ufldl.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/){.reference
.external}[
\[http://ufldl.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/\]]{.link-target},
[Adam](https://arxiv.org/abs/1412.6980){.reference .external}[
\[https://arxiv.org/abs/1412.6980\]]{.link-target},
[others](https://arxiv.org/abs/1609.04747){.reference .external}[
\[https://arxiv.org/abs/1609.04747\]]{.link-target}). Know what the
[reparameterization trick](https://arxiv.org/abs/1312.6114){.reference
.external}[ \[https://arxiv.org/abs/1312.6114\]]{.link-target} is.

**Become familiar with at least one deep learning library.**
[Tensorflow](https://www.tensorflow.org/){.reference .external}[
\[https://www.tensorflow.org/\]]{.link-target} or
[PyTorch](http://pytorch.org/){.reference .external}[
\[http://pytorch.org/\]]{.link-target} would be a good place to start.
You don't need to know how to do everything, but you should feel pretty
confident in implementing a simple program to do supervised learning.

**Get comfortable with the main concepts and terminology in RL.** Know
what states, actions, trajectories, policies, rewards, value functions,
and action-value functions are. If you're unfamiliar, Spinning Up ships
with [an introduction](../spinningup/rl_intro.html){.reference
.external} to this material; it's also worth checking out the
[RL-Intro](https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf){.reference
.external}[
\[https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf\]]{.link-target}
from the OpenAI Hackathon, or the exceptional and thorough [overview by
Lilian
Weng](https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html){.reference
.external}[
\[https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html\]]{.link-target}.
Optionally, if you're the sort of person who enjoys mathematical theory,
study up on the math of [monotonic improvement
theory](http://joschu.net/docs/thesis.pdf){.reference .external}[
\[http://joschu.net/docs/thesis.pdf\]]{.link-target} (which forms the
basis for advanced policy gradient algorithms), or [classical RL
algorithms](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf){.reference
.external}[
\[https://sites.ualberta.ca/\~szepesva/papers/RLAlgsInMDPs.pdf\]]{.link-target}
(which despite being superseded by deep RL algorithms, contain valuable
insights that sometimes drive new research).
:::

::: {#spinningup.xhtml_learn-by-doing .section}
## [Learn by Doing](#spinningup.xhtml_id51){.toc-backref}

**Write your own implementations.** You should implement as many of the
core deep RL algorithms from scratch as you can, with the aim of writing
the shortest correct implementation of each. This is by far the best way
to develop an understanding of how they work, as well as intuitions for
their specific performance characteristics.

**Simplicity is critical.** You should organize your efforts so that you
implement the simplest algorithms first, and only gradually introduce
complexity. If you start off trying to build something with too many
moving parts, odds are good that it will break and you'll lose weeks
trying to debug it. This is a common failure mode for people who are new
to deep RL, and if you find yourself stuck in it, don't be
discouraged---but do try to change tack and work on a simpler algorithm
instead, before returning to the more complex thing later.

**Which algorithms?** You should probably start with vanilla policy
gradient (also called
[REINFORCE](https://arxiv.org/abs/1604.06778){.reference .external}[
\[https://arxiv.org/abs/1604.06778\]]{.link-target}),
[DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf){.reference
.external}[
\[https://www.cs.toronto.edu/\~vmnih/docs/dqn.pdf\]]{.link-target},
[A2C](https://blog.openai.com/baselines-acktr-a2c/){.reference
.external}[
\[https://blog.openai.com/baselines-acktr-a2c/\]]{.link-target} (the
synchronous version of
[A3C](https://arxiv.org/abs/1602.01783){.reference .external}[
\[https://arxiv.org/abs/1602.01783\]]{.link-target}),
[PPO](https://arxiv.org/abs/1707.06347){.reference .external}[
\[https://arxiv.org/abs/1707.06347\]]{.link-target} (the variant with
the clipped objective), and
[DDPG](https://arxiv.org/abs/1509.02971){.reference .external}[
\[https://arxiv.org/abs/1509.02971\]]{.link-target}, approximately in
that order. The simplest versions of all of these can be written in just
a few hundred lines of code (ballpark 250-300), and some of them even
less (for example, [a no-frills version of
VPG](https://github.com/jachiam/rl-intro/blob/master/pg_cartpole.py){.reference
.external}[
\[https://github.com/jachiam/rl-intro/blob/master/pg_cartpole.py\]]{.link-target}
can be written in about 80 lines). Write single-threaded code before you
try writing parallelized versions of these algorithms. (Do try to
parallelize at least one.)

**Focus on understanding.** Writing working RL code requires clear,
detail-oriented understanding of the algorithms. This is because
**broken RL code almost always fails silently,** where the code appears
to run fine except that the agent never learns how to solve the task.
Usually the problem is that something is being calculated with the wrong
equation, or on the wrong distribution, or data is being piped into the
wrong place. Sometimes the only way to find these bugs is to read the
code with a critical eye, know exactly what it should be doing, and find
where it deviates from the correct behavior. Developing that knowledge
requires you to engage with both academic literature and other existing
implementations (when possible), so a good amount of your time should be
spent on that reading.

**What to look for in papers:** When implementing an algorithm based on
a paper, scour that paper, especially the ablation analyses and
supplementary material (where available). The ablations will give you an
intuition for what parameters or subroutines have the biggest impact on
getting things to work, which will help you diagnose bugs. Supplementary
material will often give information about specific details like network
architecture and optimization hyperparameters, and you should try to
align your implementation to these details to improve your chances of
getting it working.

**But don't overfit to paper details.** Sometimes, the paper prescribes
the use of more tricks than are strictly necessary, so be a bit wary of
this, and try out simplifications where possible. For example, the
original DDPG paper suggests a complex neural network architecture and
initialization scheme, as well as batch normalization. These aren't
strictly necessary, and some of the best-reported results for DDPG use
simpler networks. As another example, the original A3C paper uses
asynchronous updates from the various actor-learners, but it turns out
that synchronous updates work about as well.

**Don't overfit to existing implementations either.** Study
[existing](https://github.com/openai/baselines){.reference .external}[
\[https://github.com/openai/baselines\]]{.link-target}
[implementations](https://github.com/rll/rllab){.reference .external}[
\[https://github.com/rll/rllab\]]{.link-target} for inspiration, but be
careful not to overfit to the engineering details of those
implementations. RL libraries frequently make choices for abstraction
that are good for code reuse between algorithms, but which are
unnecessary if you're only writing a single algorithm or supporting a
single use case.

**Iterate fast in simple environments.** To debug your implementations,
try them with simple environments where learning should happen quickly,
like CartPole-v0, InvertedPendulum-v0, FrozenLake-v0, and HalfCheetah-v2
(with a short time horizon---only 100 or 250 steps instead of the full
1000) from the [OpenAI Gym](https://gym.openai.com/){.reference
.external}[ \[https://gym.openai.com/\]]{.link-target}. Don't try to run
an algorithm in Atari or a complex Humanoid environment if you haven't
first verified that it works on the simplest possible toy task. Your
ideal experiment turnaround-time at the debug stage is \<5 minutes (on
your local machine) or slightly longer but not much. These small-scale
experiments don't require any special hardware, and can be run without
too much trouble on CPUs.

**If it doesn't work, assume there's a bug.** Spend a lot of effort
searching for bugs before you resort to tweaking hyperparameters:
usually it's a bug. Bad hyperparameters can significantly degrade RL
performance, but if you're using hyperparameters similar to the ones in
papers and standard implementations, those will probably not be the
issue. Also worth keeping in mind: sometimes things will work in one
environment even when you have a breaking bug, so make sure to test in
more than one environment once your results look promising.

**Measure everything.** Do a lot of instrumenting to see what's going on
under-the-hood. The more stats about the learning process you read out
at each iteration, the easier it is to debug---after all, you can't tell
it's broken if you can't see that it's breaking. I personally like to
look at the mean/std/min/max for cumulative rewards, episode lengths,
and value function estimates, along with the losses for the objectives,
and the details of any exploration parameters (like mean entropy for
stochastic policy optimization, or current epsilon for epsilon-greedy as
in DQN). Also, watch videos of your agent's performance every now and
then; this will give you some insights you wouldn't get otherwise.

**Scale experiments when things work.** After you have an implementation
of an RL algorithm that seems to work correctly in the simplest
environments, test it out on harder environments. Experiments at this
stage will take longer---on the order of somewhere between a few hours
and a couple of days, depending. Specialized hardware---like a beefy GPU
or a 32-core machine---might be useful at this point, and you should
consider looking into cloud computing resources like AWS or GCE.

**Keep these habits!** These habits are worth keeping beyond the stage
where you're just learning about deep RL---they will accelerate your
research!
:::

::: {#spinningup.xhtml_developing-a-research-project .section}
## [Developing a Research Project](#spinningup.xhtml_id52){.toc-backref}

Once you feel reasonably comfortable with the basics in deep RL, you
should start pushing on the boundaries and doing research. To get there,
you'll need an idea for a project.

**Start by exploring the literature to become aware of topics in the
field.** There are a wide range of topics you might find interesting:
sample efficiency, exploration, transfer learning, hierarchy, memory,
model-based RL, meta learning, and multi-agent, to name a few. If you're
looking for inspiration, or just want to get a rough sense of what's out
there, check out Spinning Up's [key
papers](../spinningup/keypapers.html){.reference .external} list. Find a
paper that you enjoy on one of these subjects---something that inspires
you---and read it thoroughly. Use the related work section and citations
to find closely-related papers and do a deep dive in the literature.
You'll start to figure out where the unsolved problems are and where you
can make an impact.

**Approaches to idea-generation:** There are a many different ways to
start thinking about ideas for projects, and the frame you choose
influences how the project might evolve and what risks it will face.
Here are a few examples:

**Frame 1: Improving on an Existing Approach.** This is the
incrementalist angle, where you try to get performance gains in an
established problem setting by tweaking an existing algorithm.
Reimplementing prior work is super helpful here, because it exposes you
to the ways that existing algorithms are brittle and could be improved.
A novice will find this the most accessible frame, but it can also be
worthwhile for researchers at any level of experience. While some
researchers find incrementalism less exciting, some of the most
impressive achievements in machine learning have come from work of this
nature.

Because projects like these are tied to existing methods, they are by
nature narrowly scoped and can wrap up quickly (a few months), which may
be desirable (especially when starting out as a researcher). But this
also sets up the risks: it's possible that the tweaks you have in mind
for an algorithm may fail to improve it, in which case, unless you come
up with more tweaks, the project is just over and you have no clear
signal on what to do next.

**Frame 2: Focusing on Unsolved Benchmarks.** Instead of thinking about
how to improve an existing method, you aim to succeed on a task that no
one has solved before. For example: achieving perfect generalization
from training levels to test levels in the [Sonic
domain](https://contest.openai.com/2018-1/){.reference .external}[
\[https://contest.openai.com/2018-1/\]]{.link-target} or [Gym
Retro](https://blog.openai.com/gym-retro/){.reference .external}[
\[https://blog.openai.com/gym-retro/\]]{.link-target}. When you hammer
away at an unsolved task, you might try a wide variety of methods,
including prior approaches and new ones that you invent for the project.
It is possible for a novice to approch this kind of problem, but there
will be a steeper learning curve.

Projects in this frame have a broad scope and can go on for a while
(several months to a year-plus). The main risk is that the benchmark is
unsolvable without a substantial breakthrough, meaning that it would be
easy to spend a lot of time without making any progress on it. But even
if a project like this fails, it often leads the researcher to many new
insights that become fertile soil for the next project.

**Frame 3: Create a New Problem Setting.** Instead of thinking about
existing methods or current grand challenges, think of an entirely
different conceptual problem that hasn't been studied yet. Then, figure
out how to make progress on it. For projects along these lines, a
standard benchmark probably doesn't exist yet, and you will have to
design one. This can be a huge challenge, but it's worth
embracing---great benchmarks move the whole field forward.

Problems in this frame come up when they come up---it's hard to go
looking for them.

**Avoid reinventing the wheel.** When you come up with a good idea that
you want to start testing, that's great! But while you're still in the
early stages with it, do the most thorough check you can to make sure it
hasn't already been done. It can be pretty disheartening to get halfway
through a project, and only then discover that there's already a paper
about your idea. It's especially frustrating when the work is
concurrent, which happens from time to time! But don't let that deter
you---and definitely don't let it motivate you to plant flags with
not-quite-finished research and over-claim the merits of the partial
work. Do good research and finish out your projects with complete and
thorough investigations, because that's what counts, and by far what
matters most in the long run.
:::

::: {#spinningup.xhtml_doing-rigorous-research-in-rl .section}
## [Doing Rigorous Research in RL](#spinningup.xhtml_id53){.toc-backref}

Now you've come up with an idea, and you're fairly certain it hasn't
been done. You use the skills you've developed to implement it and you
start testing it out on standard domains. It looks like it works! But
what does that mean, and how well does it have to work to be important?
This is one of the hardest parts of research in deep RL. In order to
validate that your proposal is a meaningful contribution, you have to
rigorously prove that it actually gets a performance benefit over the
strongest possible baseline algorithm---whatever currently achieves SOTA
(state of the art) on your test domains. If you've invented a new test
domain, so there's no previous SOTA, you still need to try out whatever
the most reliable algorithm in the literature is that could plausibly do
well in the new test domain, and then you have to beat that.

**Set up fair comparisons.** If you implement your baseline from
scratch---as opposed to comparing against another paper's numbers
directly---it's important to spend as much time tuning your baseline as
you spend tuning your own algorithm. This will make sure that
comparisons are fair. Also, do your best to hold "all else equal" even
if there are substantial differences between your algorithm and the
baseline. For example, if you're investigating architecture variants,
keep the number of model parameters approximately equal between your
model and the baseline. Under no circumstances handicap the baseline! It
turns out that the baselines in RL are pretty strong, and getting big,
consistent wins over them can be tricky or require some good insight in
algorithm design.

**Remove stochasticity as a confounder.** Beware of random seeds making
things look stronger or weaker than they really are, so run everything
for many random seeds (at least 3, but if you want to be thorough, do 10
or more). This is really important and deserves a lot of emphasis: deep
RL seems fairly brittle with respect to random seed in a lot of common
use cases. There's potentially enough variance that two different groups
of random seeds can yield learning curves with differences so
significant that they look like they don't come from the same
distribution at all (see [figure 10
here](https://arxiv.org/pdf/1708.04133.pdf){.reference .external}[
\[https://arxiv.org/pdf/1708.04133.pdf\]]{.link-target}).

**Run high-integrity experiments.** Don't just take the results from the
best or most interesting runs to use in your paper. Instead, launch new,
final experiments---for all of the methods that you intend to compare
(if you are comparing against your own baseline implementations)---and
precommit to report on whatever comes out of that. This is to enforce a
weak form of [preregistration](https://cos.io/prereg/){.reference
.external}[ \[https://cos.io/prereg/\]]{.link-target}: you use the
tuning stage to come up with your hypotheses, and you use the final runs
to come up with your conclusions.

**Check each claim separately.** Another critical aspect of doing
research is to run an ablation analysis. Any method you propose is
likely to have several key design decisions---like architecture choices
or regularization techniques, for instance---each of which could
separately impact performance. The claim you'll make in your work is
that those design decisions collectively help, but this is really a
bundle of several claims in disguise: one for each such design element.
By systematically evaluating what would happen if you were to swap them
out with alternate design choices, or remove them entirely, you can
figure out how to correctly attribute credit for the benefits your
method confers. This lets you make each separate claim with a measure of
confidence, and increases the overall strength of your work.
:::

::: {#spinningup.xhtml_closing-thoughts .section}
## [Closing Thoughts](#spinningup.xhtml_id54){.toc-backref}

Deep RL is an exciting, fast-moving field, and we need as many people as
possible to go through the open problems and make progress on them.
Hopefully, you feel a bit more prepared to be a part of it after reading
this! And whenever you're ready, [let us
know](https://jobs.lever.co/openai){.reference .external}[
\[https://jobs.lever.co/openai\]]{.link-target}.
:::

::: {#spinningup.xhtml_ps-other-resources .section}
## [PS: Other Resources](#spinningup.xhtml_id55){.toc-backref}

Consider reading through these other informative articles about growing
as a researcher or engineer in this field:

[Advice for Short-term Machine Learning Research
Projects](https://rockt.github.io/2018/08/29/msc-advice){.reference
.external}[
\[https://rockt.github.io/2018/08/29/msc-advice\]]{.link-target}, by Tim
Rocktäschel, Jakob Foerster and Greg Farquhar.

[ML Engineering for AI Safety & Robustness: a Google Brain Engineer's
Guide to Entering the
Field](https://80000hours.org/articles/ml-engineering-career-transition-guide/){.reference
.external}[
\[https://80000hours.org/articles/ml-engineering-career-transition-guide/\]]{.link-target},
by Catherine Olsson and 80,000 Hours.
:::

::: {#spinningup.xhtml_references .section}
## [References](#spinningup.xhtml_id56){.toc-backref}

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[1\]   [Deep Reinforcement Learning Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html){.reference .external}[ \[https://www.alexirpan.com/2018/02/14/rl-hard.html\]]{.link-target}, Alex Irpan, 2018
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[2\]   [Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control](https://arxiv.org/abs/1708.04133){.reference .external}[ \[https://arxiv.org/abs/1708.04133\]]{.link-target}, Islam et al, 2017
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[3\]   [Deep Reinforcement Learning that Matters](https://arxiv.org/abs/1709.06560){.reference .external}[ \[https://arxiv.org/abs/1709.06560\]]{.link-target}, Henderson et al, 2017
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[4\]   [Lessons Learned Reproducing a Deep Reinforcement Learning Paper](http://amid.fish/reproducing-deep-rl){.reference .external}[ \[http://amid.fish/reproducing-deep-rl\]]{.link-target}, Matthew Rahtz, 2018
  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[5\]   [UCL Course on RL](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html){.reference .external}[ \[http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html\]]{.link-target}
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------
  \[6\]   [Berkeley Deep RL Course](http://rll.berkeley.edu/deeprlcourse/){.reference .external}[ \[http://rll.berkeley.edu/deeprlcourse/\]]{.link-target}
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[7\]   [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures){.reference .external}[ \[https://sites.google.com/view/deep-rl-bootcamp/lectures\]]{.link-target}
  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[8\]   [Nuts and Bolts of Deep RL](http://joschu.net/docs/nuts-and-bolts.pdf){.reference .external}[ \[http://joschu.net/docs/nuts-and-bolts.pdf\]]{.link-target}, John Schulman
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[9\]   [Stanford Deep Learning Tutorial: Multi-Layer Neural Network](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/){.reference .external}[ \[http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/\]]{.link-target}
  ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[10\]   [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/){.reference .external}[ \[http://karpathy.github.io/2015/05/21/rnn-effectiveness/\]]{.link-target}, Andrej Karpathy, 2015
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[11\]   [LSTM: A Search Space Odyssey](https://arxiv.org/abs/1503.04069){.reference .external}[ \[https://arxiv.org/abs/1503.04069\]]{.link-target}, Greff et al, 2015
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[12\]   [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/){.reference .external}[ \[http://colah.github.io/posts/2015-08-Understanding-LSTMs/\]]{.link-target}, Chris Olah, 2015
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[13\]   [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/abs/1412.3555v1){.reference .external}[ \[https://arxiv.org/abs/1412.3555v1\]]{.link-target}, Chung et al, 2014 (GRU paper)
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[14\]   [Conv Nets: A Modular Perspective](http://colah.github.io/posts/2014-07-Conv-Nets-Modular/){.reference .external}[ \[http://colah.github.io/posts/2014-07-Conv-Nets-Modular/\]]{.link-target}, Chris Olah, 2014
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[15\]   [Stanford CS231n, Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/convolutional-networks/){.reference .external}[ \[https://cs231n.github.io/convolutional-networks/\]]{.link-target}
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[16\]   [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385){.reference .external}[ \[https://arxiv.org/abs/1512.03385\]]{.link-target}, He et al, 2015 (ResNets)
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[17\]   [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473){.reference .external}[ \[https://arxiv.org/abs/1409.0473\]]{.link-target}, Bahdanau et al, 2014 (Attention mechanisms)
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[18\]   [Attention Is All You Need](https://arxiv.org/abs/1706.03762){.reference .external}[ \[https://arxiv.org/abs/1706.03762\]]{.link-target}, Vaswani et al, 2017
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[19\]   [A Simple Weight Decay Can Improve Generalization](https://papers.nips.cc/paper/563-a-simple-weight-decay-can-improve-generalization.pdf){.reference .external}[ \[https://papers.nips.cc/paper/563-a-simple-weight-decay-can-improve-generalization.pdf\]]{.link-target}, Krogh and Hertz, 1992
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[20\]   [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf){.reference .external}[ \[http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf\]]{.link-target}, Srivastava et al, 2014
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[21\]   [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167){.reference .external}[ \[https://arxiv.org/abs/1502.03167\]]{.link-target}, Ioffe and Szegedy, 2015
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  \[22\]   [Layer Normalization](https://arxiv.org/abs/1607.06450){.reference .external}[ \[https://arxiv.org/abs/1607.06450\]]{.link-target}, Ba et al, 2016
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[23\]   [Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks](https://arxiv.org/abs/1602.07868){.reference .external}[ \[https://arxiv.org/abs/1602.07868\]]{.link-target}, Salimans and Kingma, 2016
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[24\]   [Stanford Deep Learning Tutorial: Stochastic Gradient Descent](http://ufldl.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/){.reference .external}[ \[http://ufldl.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/\]]{.link-target}
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[25\]   [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980){.reference .external}[ \[https://arxiv.org/abs/1412.6980\]]{.link-target}, Kingma and Ba, 2014
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[26\]   [An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747){.reference .external}[ \[https://arxiv.org/abs/1609.04747\]]{.link-target}, Sebastian Ruder, 2016
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[27\]   [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114){.reference .external}[ \[https://arxiv.org/abs/1312.6114\]]{.link-target}, Kingma and Welling, 2013 (Reparameterization trick)
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------
  \[28\]   [Tensorflow](https://www.tensorflow.org/){.reference .external}[ \[https://www.tensorflow.org/\]]{.link-target}
  -------- -----------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------
  \[29\]   [PyTorch](http://pytorch.org/){.reference .external}[ \[http://pytorch.org/\]]{.link-target}
  -------- ----------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------
  \[30\]   [Spinning Up in Deep RL: Introduction to RL, Part 1](../spinningup/rl_intro.html){.reference .external}
  -------- ---------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[31\]   [RL-Intro](https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf){.reference .external}[ \[https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf\]]{.link-target} Slides from OpenAI Hackathon, Josh Achiam, 2018
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[32\]   [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html){.reference .external}[ \[https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html\]]{.link-target}, Lilian Weng, 2018
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[33\]   [Optimizing Expectations](http://joschu.net/docs/thesis.pdf){.reference .external}[ \[http://joschu.net/docs/thesis.pdf\]]{.link-target}, John Schulman, 2016 (Monotonic improvement theory)
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[34\]   [Algorithms for Reinforcement Learning](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf){.reference .external}[ \[https://sites.ualberta.ca/\~szepesva/papers/RLAlgsInMDPs.pdf\]]{.link-target}, Csaba Szepesvari, 2009 (Classic RL Algorithms)
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[35\]   [Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778){.reference .external}[ \[https://arxiv.org/abs/1604.06778\]]{.link-target}, Duan et al, 2016
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[36\]   [Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf){.reference .external}[ \[https://www.cs.toronto.edu/\~vmnih/docs/dqn.pdf\]]{.link-target}, Mnih et al, 2013 (DQN)
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[37\]   [OpenAI Baselines: ACKTR & A2C](https://blog.openai.com/baselines-acktr-a2c/){.reference .external}[ \[https://blog.openai.com/baselines-acktr-a2c/\]]{.link-target}
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[38\]   [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783){.reference .external}[ \[https://arxiv.org/abs/1602.01783\]]{.link-target}, Mnih et al, 2016 (A3C)
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[39\]   [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347){.reference .external}[ \[https://arxiv.org/abs/1707.06347\]]{.link-target}, Schulman et al, 2017 (PPO)
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[40\]   [Continuous Control with Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971){.reference .external}[ \[https://arxiv.org/abs/1509.02971\]]{.link-target}, Lillicrap et al, 2015 (DDPG)
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[41\]   [RL-Intro Policy Gradient Sample Code](https://github.com/jachiam/rl-intro/blob/master/pg_cartpole.py){.reference .external}[ \[https://github.com/jachiam/rl-intro/blob/master/pg_cartpole.py\]]{.link-target}, Josh Achiam, 2018
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------
  \[42\]   [OpenAI Baselines](https://github.com/openai/baselines){.reference .external}[ \[https://github.com/openai/baselines\]]{.link-target}
  -------- ---------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------
  \[43\]   [rllab](https://github.com/rll/rllab){.reference .external}[ \[https://github.com/rll/rllab\]]{.link-target}
  -------- --------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------
  \[44\]   [OpenAI Gym](https://gym.openai.com/){.reference .external}[ \[https://gym.openai.com/\]]{.link-target}
  -------- ---------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------
  \[45\]   [OpenAI Retro Contest](https://contest.openai.com/2018-1/){.reference .external}[ \[https://contest.openai.com/2018-1/\]]{.link-target}
  -------- -----------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------
  \[46\]   [OpenAI Gym Retro](https://blog.openai.com/gym-retro/){.reference .external}[ \[https://blog.openai.com/gym-retro/\]]{.link-target}
  -------- -------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[47\]   [Center for Open Science](https://cos.io/prereg/){.reference .external}[ \[https://cos.io/prereg/\]]{.link-target}, explaining what preregistration means in the context of scientific experiments.
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::::::::
::::::::::::

[]{#keypapers.xhtml}

:::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::: {#keypapers.xhtml_key-papers-in-deep-rl .section}
# [Key Papers in Deep RL](#keypapers.xhtml_id106){.toc-backref}

What follows is a list of papers in deep RL that are worth reading. This
is *far* from comprehensive, but should provide a useful starting point
for someone looking to do research in the field.

::: {#keypapers.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Key Papers in Deep
  RL](#keypapers.xhtml_key-papers-in-deep-rl){#keypapers.xhtml_id106
  .reference .internal}
  - [1. Model-Free
    RL](#keypapers.xhtml_model-free-rl){#keypapers.xhtml_id107
    .reference .internal}
  - [2.
    Exploration](#keypapers.xhtml_exploration){#keypapers.xhtml_id108
    .reference .internal}
  - [3. Transfer and Multitask
    RL](#keypapers.xhtml_transfer-and-multitask-rl){#keypapers.xhtml_id109
    .reference .internal}
  - [4. Hierarchy](#keypapers.xhtml_hierarchy){#keypapers.xhtml_id110
    .reference .internal}
  - [5. Memory](#keypapers.xhtml_memory){#keypapers.xhtml_id111
    .reference .internal}
  - [6. Model-Based
    RL](#keypapers.xhtml_model-based-rl){#keypapers.xhtml_id112
    .reference .internal}
  - [7. Meta-RL](#keypapers.xhtml_meta-rl){#keypapers.xhtml_id113
    .reference .internal}
  - [8. Scaling RL](#keypapers.xhtml_scaling-rl){#keypapers.xhtml_id114
    .reference .internal}
  - [9. RL in the Real
    World](#keypapers.xhtml_rl-in-the-real-world){#keypapers.xhtml_id115
    .reference .internal}
  - [10. Safety](#keypapers.xhtml_safety){#keypapers.xhtml_id116
    .reference .internal}
  - [11. Imitation Learning and Inverse Reinforcement
    Learning](#keypapers.xhtml_imitation-learning-and-inverse-reinforcement-learning){#keypapers.xhtml_id117
    .reference .internal}
  - [12. Reproducibility, Analysis, and
    Critique](#keypapers.xhtml_reproducibility-analysis-and-critique){#keypapers.xhtml_id118
    .reference .internal}
  - [13. Bonus: Classic Papers in RL Theory or
    Review](#keypapers.xhtml_bonus-classic-papers-in-rl-theory-or-review){#keypapers.xhtml_id119
    .reference .internal}
:::

::::::::::: {#keypapers.xhtml_model-free-rl .section}
## [1. Model-Free RL](#keypapers.xhtml_id107){.toc-backref}

::: {#keypapers.xhtml_a-deep-q-learning .section}
### a. Deep Q-Learning

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[1\]   [Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf){.reference .external}[ \[https://www.cs.toronto.edu/\~vmnih/docs/dqn.pdf\]]{.link-target}, Mnih et al, 2013. **Algorithm: DQN.**
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[2\]   [Deep Recurrent Q-Learning for Partially Observable MDPs](https://arxiv.org/abs/1507.06527){.reference .external}[ \[https://arxiv.org/abs/1507.06527\]]{.link-target}, Hausknecht and Stone, 2015. **Algorithm: Deep Recurrent Q-Learning.**
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[3\]   [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581){.reference .external}[ \[https://arxiv.org/abs/1511.06581\]]{.link-target}, Wang et al, 2015. **Algorithm: Dueling DQN.**
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[4\]   [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461){.reference .external}[ \[https://arxiv.org/abs/1509.06461\]]{.link-target}, Hasselt et al 2015. **Algorithm: Double DQN.**
  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[5\]   [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952){.reference .external}[ \[https://arxiv.org/abs/1511.05952\]]{.link-target}, Schaul et al, 2015. **Algorithm: Prioritized Experience Replay (PER).**
  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[6\]   [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298){.reference .external}[ \[https://arxiv.org/abs/1710.02298\]]{.link-target}, Hessel et al, 2017. **Algorithm: Rainbow DQN.**
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_b-policy-gradients .section}
### b. Policy Gradients

  ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[7\]   [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783){.reference .external}[ \[https://arxiv.org/abs/1602.01783\]]{.link-target}, Mnih et al, 2016. **Algorithm: A3C.**
  ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[8\]   [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477){.reference .external}[ \[https://arxiv.org/abs/1502.05477\]]{.link-target}, Schulman et al, 2015. **Algorithm: TRPO.**
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[9\]   [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438){.reference .external}[ \[https://arxiv.org/abs/1506.02438\]]{.link-target}, Schulman et al, 2015. **Algorithm: GAE.**
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[10\]   [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347){.reference .external}[ \[https://arxiv.org/abs/1707.06347\]]{.link-target}, Schulman et al, 2017. **Algorithm: PPO-Clip, PPO-Penalty.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[11\]   [Emergence of Locomotion Behaviours in Rich Environments](https://arxiv.org/abs/1707.02286){.reference .external}[ \[https://arxiv.org/abs/1707.02286\]]{.link-target}, Heess et al, 2017. **Algorithm: PPO-Penalty.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[12\]   [Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/abs/1708.05144){.reference .external}[ \[https://arxiv.org/abs/1708.05144\]]{.link-target}, Wu et al, 2017. **Algorithm: ACKTR.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[13\]   [Sample Efficient Actor-Critic with Experience Replay](https://arxiv.org/abs/1611.01224){.reference .external}[ \[https://arxiv.org/abs/1611.01224\]]{.link-target}, Wang et al, 2016. **Algorithm: ACER.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[14\]   [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://arxiv.org/abs/1801.01290){.reference .external}[ \[https://arxiv.org/abs/1801.01290\]]{.link-target}, Haarnoja et al, 2018. **Algorithm: SAC.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_c-deterministic-policy-gradients .section}
### c. Deterministic Policy Gradients

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[15\]   [Deterministic Policy Gradient Algorithms](http://proceedings.mlr.press/v32/silver14.pdf){.reference .external}[ \[http://proceedings.mlr.press/v32/silver14.pdf\]]{.link-target}, Silver et al, 2014. **Algorithm: DPG.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[16\]   [Continuous Control With Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971){.reference .external}[ \[https://arxiv.org/abs/1509.02971\]]{.link-target}, Lillicrap et al, 2015. **Algorithm: DDPG.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[17\]   [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477){.reference .external}[ \[https://arxiv.org/abs/1802.09477\]]{.link-target}, Fujimoto et al, 2018. **Algorithm: TD3.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_d-distributional-rl .section}
### d. Distributional RL

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[18\]   [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887){.reference .external}[ \[https://arxiv.org/abs/1707.06887\]]{.link-target}, Bellemare et al, 2017. **Algorithm: C51.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[19\]   [Distributional Reinforcement Learning with Quantile Regression](https://arxiv.org/abs/1710.10044){.reference .external}[ \[https://arxiv.org/abs/1710.10044\]]{.link-target}, Dabney et al, 2017. **Algorithm: QR-DQN.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[20\]   [Implicit Quantile Networks for Distributional Reinforcement Learning](https://arxiv.org/abs/1806.06923){.reference .external}[ \[https://arxiv.org/abs/1806.06923\]]{.link-target}, Dabney et al, 2018. **Algorithm: IQN.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[21\]   [Dopamine: A Research Framework for Deep Reinforcement Learning](https://openreview.net/forum?id=ByG_3s09KX){.reference .external}[ \[https://openreview.net/forum?id=ByG_3s09KX\]]{.link-target}, Anonymous, 2018. **Contribution:** Introduces Dopamine, a code repository containing implementations of DQN, C51, IQN, and Rainbow. [Code link.](https://github.com/google/dopamine){.reference .external}[ \[https://github.com/google/dopamine\]]{.link-target}
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_e-policy-gradients-with-action-dependent-baselines .section}
### e. Policy Gradients with Action-Dependent Baselines

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[22\]   [Q-Prop: Sample-Efficient Policy Gradient with An Off-Policy Critic](https://arxiv.org/abs/1611.02247){.reference .external}[ \[https://arxiv.org/abs/1611.02247\]]{.link-target}, Gu et al, 2016. **Algorithm: Q-Prop.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[23\]   [Action-depedent Control Variates for Policy Optimization via Stein's Identity](https://arxiv.org/abs/1710.11198){.reference .external}[ \[https://arxiv.org/abs/1710.11198\]]{.link-target}, Liu et al, 2017. **Algorithm: Stein Control Variates.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[24\]   [The Mirage of Action-Dependent Baselines in Reinforcement Learning](https://arxiv.org/abs/1802.10031){.reference .external}[ \[https://arxiv.org/abs/1802.10031\]]{.link-target}, Tucker et al, 2018. **Contribution:** interestingly, critiques and reevaluates claims from earlier papers (including Q-Prop and stein control variates) and finds important methodological errors in them.
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_f-path-consistency-learning .section}
### f. Path-Consistency Learning

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[25\]   [Bridging the Gap Between Value and Policy Based Reinforcement Learning](https://arxiv.org/abs/1702.08892){.reference .external}[ \[https://arxiv.org/abs/1702.08892\]]{.link-target}, Nachum et al, 2017. **Algorithm: PCL.**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[26\]   [Trust-PCL: An Off-Policy Trust Region Method for Continuous Control](https://arxiv.org/abs/1707.01891){.reference .external}[ \[https://arxiv.org/abs/1707.01891\]]{.link-target}, Nachum et al, 2017. **Algorithm: Trust-PCL.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_g-other-directions-for-combining-policy-learning-and-q-learning .section}
### g. Other Directions for Combining Policy-Learning and Q-Learning

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[27\]   [Combining Policy Gradient and Q-learning](https://arxiv.org/abs/1611.01626){.reference .external}[ \[https://arxiv.org/abs/1611.01626\]]{.link-target}, O'Donoghue et al, 2016. **Algorithm: PGQL.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[28\]   [The Reactor: A Fast and Sample-Efficient Actor-Critic Agent for Reinforcement Learning](https://arxiv.org/abs/1704.04651){.reference .external}[ \[https://arxiv.org/abs/1704.04651\]]{.link-target}, Gruslys et al, 2017. **Algorithm: Reactor.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[29\]   [Interpolated Policy Gradient: Merging On-Policy and Off-Policy Gradient Estimation for Deep Reinforcement Learning](http://papers.nips.cc/paper/6974-interpolated-policy-gradient-merging-on-policy-and-off-policy-gradient-estimation-for-deep-reinforcement-learning){.reference .external}[ \[http://papers.nips.cc/paper/6974-interpolated-policy-gradient-merging-on-policy-and-off-policy-gradient-estimation-for-deep-reinforcement-learning\]]{.link-target}, Gu et al, 2017. **Algorithm: IPG.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[30\]   [Equivalence Between Policy Gradients and Soft Q-Learning](https://arxiv.org/abs/1704.06440){.reference .external}[ \[https://arxiv.org/abs/1704.06440\]]{.link-target}, Schulman et al, 2017. **Contribution:** Reveals a theoretical link between these two families of RL algorithms.
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_h-evolutionary-algorithms .section}
### h. Evolutionary Algorithms

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[31\]   [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864){.reference .external}[ \[https://arxiv.org/abs/1703.03864\]]{.link-target}, Salimans et al, 2017. **Algorithm: ES.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::::::::

::::: {#keypapers.xhtml_exploration .section}
## [2. Exploration](#keypapers.xhtml_id108){.toc-backref}

::: {#keypapers.xhtml_a-intrinsic-motivation .section}
### a. Intrinsic Motivation

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[32\]   [VIME: Variational Information Maximizing Exploration](https://arxiv.org/abs/1605.09674){.reference .external}[ \[https://arxiv.org/abs/1605.09674\]]{.link-target}, Houthooft et al, 2016. **Algorithm: VIME.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[33\]   [Unifying Count-Based Exploration and Intrinsic Motivation](https://arxiv.org/abs/1606.01868){.reference .external}[ \[https://arxiv.org/abs/1606.01868\]]{.link-target}, Bellemare et al, 2016. **Algorithm: CTS-based Pseudocounts.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[34\]   [Count-Based Exploration with Neural Density Models](https://arxiv.org/abs/1703.01310){.reference .external}[ \[https://arxiv.org/abs/1703.01310\]]{.link-target}, Ostrovski et al, 2017. **Algorithm: PixelCNN-based Pseudocounts.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[35\]   [#Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning](https://arxiv.org/abs/1611.04717){.reference .external}[ \[https://arxiv.org/abs/1611.04717\]]{.link-target}, Tang et al, 2016. **Algorithm: Hash-based Counts.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[36\]   [EX2: Exploration with Exemplar Models for Deep Reinforcement Learning](https://arxiv.org/abs/1703.01260){.reference .external}[ \[https://arxiv.org/abs/1703.01260\]]{.link-target}, Fu et al, 2017. **Algorithm: EX2.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[37\]   [Curiosity-driven Exploration by Self-supervised Prediction](https://arxiv.org/abs/1705.05363){.reference .external}[ \[https://arxiv.org/abs/1705.05363\]]{.link-target}, Pathak et al, 2017. **Algorithm: Intrinsic Curiosity Module (ICM).**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[38\]   [Large-Scale Study of Curiosity-Driven Learning](https://arxiv.org/abs/1808.04355){.reference .external}[ \[https://arxiv.org/abs/1808.04355\]]{.link-target}, Burda et al, 2018. **Contribution:** Systematic analysis of how surprisal-based intrinsic motivation performs in a wide variety of environments.
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[39\]   [Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894){.reference .external}[ \[https://arxiv.org/abs/1810.12894\]]{.link-target}, Burda et al, 2018. **Algorithm: RND.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_b-unsupervised-rl .section}
### b. Unsupervised RL

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[40\]   [Variational Intrinsic Control](https://arxiv.org/abs/1611.07507){.reference .external}[ \[https://arxiv.org/abs/1611.07507\]]{.link-target}, Gregor et al, 2016. **Algorithm: VIC.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[41\]   [Diversity is All You Need: Learning Skills without a Reward Function](https://arxiv.org/abs/1802.06070){.reference .external}[ \[https://arxiv.org/abs/1802.06070\]]{.link-target}, Eysenbach et al, 2018. **Algorithm: DIAYN.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[42\]   [Variational Option Discovery Algorithms](https://arxiv.org/abs/1807.10299){.reference .external}[ \[https://arxiv.org/abs/1807.10299\]]{.link-target}, Achiam et al, 2018. **Algorithm: VALOR.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::

::: {#keypapers.xhtml_transfer-and-multitask-rl .section}
## [3. Transfer and Multitask RL](#keypapers.xhtml_id109){.toc-backref}

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[43\]   [Progressive Neural Networks](https://arxiv.org/abs/1606.04671){.reference .external}[ \[https://arxiv.org/abs/1606.04671\]]{.link-target}, Rusu et al, 2016. **Algorithm: Progressive Networks.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[44\]   [Universal Value Function Approximators](http://proceedings.mlr.press/v37/schaul15.pdf){.reference .external}[ \[http://proceedings.mlr.press/v37/schaul15.pdf\]]{.link-target}, Schaul et al, 2015. **Algorithm: UVFA.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[45\]   [Reinforcement Learning with Unsupervised Auxiliary Tasks](https://arxiv.org/abs/1611.05397){.reference .external}[ \[https://arxiv.org/abs/1611.05397\]]{.link-target}, Jaderberg et al, 2016. **Algorithm: UNREAL.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[46\]   [The Intentional Unintentional Agent: Learning to Solve Many Continuous Control Tasks Simultaneously](https://arxiv.org/abs/1707.03300){.reference .external}[ \[https://arxiv.org/abs/1707.03300\]]{.link-target}, Cabi et al, 2017. **Algorithm: IU Agent.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[47\]   [PathNet: Evolution Channels Gradient Descent in Super Neural Networks](https://arxiv.org/abs/1701.08734){.reference .external}[ \[https://arxiv.org/abs/1701.08734\]]{.link-target}, Fernando et al, 2017. **Algorithm: PathNet.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[48\]   [Mutual Alignment Transfer Learning](https://arxiv.org/abs/1707.07907){.reference .external}[ \[https://arxiv.org/abs/1707.07907\]]{.link-target}, Wulfmeier et al, 2017. **Algorithm: MATL.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[49\]   [Learning an Embedding Space for Transferable Robot Skills](https://openreview.net/forum?id=rk07ZXZRb&noteId=rk07ZXZRb){.reference .external}[ \[https://openreview.net/forum?id=rk07ZXZRb&noteId=rk07ZXZRb\]]{.link-target}, Hausman et al, 2018.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[50\]   [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495){.reference .external}[ \[https://arxiv.org/abs/1707.01495\]]{.link-target}, Andrychowicz et al, 2017. **Algorithm: Hindsight Experience Replay (HER).**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_hierarchy .section}
## [4. Hierarchy](#keypapers.xhtml_id110){.toc-backref}

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[51\]   [Strategic Attentive Writer for Learning Macro-Actions](https://arxiv.org/abs/1606.04695){.reference .external}[ \[https://arxiv.org/abs/1606.04695\]]{.link-target}, Vezhnevets et al, 2016. **Algorithm: STRAW.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[52\]   [FeUdal Networks for Hierarchical Reinforcement Learning](https://arxiv.org/abs/1703.01161){.reference .external}[ \[https://arxiv.org/abs/1703.01161\]]{.link-target}, Vezhnevets et al, 2017. **Algorithm: Feudal Networks**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[53\]   [Data-Efficient Hierarchical Reinforcement Learning](https://arxiv.org/abs/1805.08296){.reference .external}[ \[https://arxiv.org/abs/1805.08296\]]{.link-target}, Nachum et al, 2018. **Algorithm: HIRO.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_memory .section}
## [5. Memory](#keypapers.xhtml_id111){.toc-backref}

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[54\]   [Model-Free Episodic Control](https://arxiv.org/abs/1606.04460){.reference .external}[ \[https://arxiv.org/abs/1606.04460\]]{.link-target}, Blundell et al, 2016. **Algorithm: MFEC.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[55\]   [Neural Episodic Control](https://arxiv.org/abs/1703.01988){.reference .external}[ \[https://arxiv.org/abs/1703.01988\]]{.link-target}, Pritzel et al, 2017. **Algorithm: NEC.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[56\]   [Neural Map: Structured Memory for Deep Reinforcement Learning](https://arxiv.org/abs/1702.08360){.reference .external}[ \[https://arxiv.org/abs/1702.08360\]]{.link-target}, Parisotto and Salakhutdinov, 2017. **Algorithm: Neural Map.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[57\]   [Unsupervised Predictive Memory in a Goal-Directed Agent](https://arxiv.org/abs/1803.10760){.reference .external}[ \[https://arxiv.org/abs/1803.10760\]]{.link-target}, Wayne et al, 2018. **Algorithm: MERLIN.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[58\]   [Relational Recurrent Neural Networks](https://arxiv.org/abs/1806.01822){.reference .external}[ \[https://arxiv.org/abs/1806.01822\]]{.link-target}, Santoro et al, 2018. **Algorithm: RMC.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::::: {#keypapers.xhtml_model-based-rl .section}
## [6. Model-Based RL](#keypapers.xhtml_id112){.toc-backref}

::: {#keypapers.xhtml_a-model-is-learned .section}
### a. Model is Learned

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[59\]   [Imagination-Augmented Agents for Deep Reinforcement Learning](https://arxiv.org/abs/1707.06203){.reference .external}[ \[https://arxiv.org/abs/1707.06203\]]{.link-target}, Weber et al, 2017. **Algorithm: I2A.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[60\]   [Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning](https://arxiv.org/abs/1708.02596){.reference .external}[ \[https://arxiv.org/abs/1708.02596\]]{.link-target}, Nagabandi et al, 2017. **Algorithm: MBMF.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[61\]   [Model-Based Value Expansion for Efficient Model-Free Reinforcement Learning](https://arxiv.org/abs/1803.00101){.reference .external}[ \[https://arxiv.org/abs/1803.00101\]]{.link-target}, Feinberg et al, 2018. **Algorithm: MVE.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[62\]   [Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion](https://arxiv.org/abs/1807.01675){.reference .external}[ \[https://arxiv.org/abs/1807.01675\]]{.link-target}, Buckman et al, 2018. **Algorithm: STEVE.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[63\]   [Model-Ensemble Trust-Region Policy Optimization](https://openreview.net/forum?id=SJJinbWRZ&noteId=SJJinbWRZ){.reference .external}[ \[https://openreview.net/forum?id=SJJinbWRZ&noteId=SJJinbWRZ\]]{.link-target}, Kurutach et al, 2018. **Algorithm: ME-TRPO.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[64\]   [Model-Based Reinforcement Learning via Meta-Policy Optimization](https://arxiv.org/abs/1809.05214){.reference .external}[ \[https://arxiv.org/abs/1809.05214\]]{.link-target}, Clavera et al, 2018. **Algorithm: MB-MPO.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[65\]   [Recurrent World Models Facilitate Policy Evolution](https://arxiv.org/abs/1809.01999){.reference .external}[ \[https://arxiv.org/abs/1809.01999\]]{.link-target}, Ha and Schmidhuber, 2018.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_b-model-is-given .section}
### b. Model is Given

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[66\]   [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815){.reference .external}[ \[https://arxiv.org/abs/1712.01815\]]{.link-target}, Silver et al, 2017. **Algorithm: AlphaZero.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[67\]   [Thinking Fast and Slow with Deep Learning and Tree Search](https://arxiv.org/abs/1705.08439){.reference .external}[ \[https://arxiv.org/abs/1705.08439\]]{.link-target}, Anthony et al, 2017. **Algorithm: ExIt.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::

::: {#keypapers.xhtml_meta-rl .section}
## [7. Meta-RL](#keypapers.xhtml_id113){.toc-backref}

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[68\]   [RL\^2: Fast Reinforcement Learning via Slow Reinforcement Learning](https://arxiv.org/abs/1611.02779){.reference .external}[ \[https://arxiv.org/abs/1611.02779\]]{.link-target}, Duan et al, 2016. **Algorithm: RL\^2.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[69\]   [Learning to Reinforcement Learn](https://arxiv.org/abs/1611.05763){.reference .external}[ \[https://arxiv.org/abs/1611.05763\]]{.link-target}, Wang et al, 2016.
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[70\]   [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/abs/1703.03400){.reference .external}[ \[https://arxiv.org/abs/1703.03400\]]{.link-target}, Finn et al, 2017. **Algorithm: MAML.**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[71\]   [A Simple Neural Attentive Meta-Learner](https://openreview.net/forum?id=B1DmUzWAW&noteId=B1DmUzWAW){.reference .external}[ \[https://openreview.net/forum?id=B1DmUzWAW&noteId=B1DmUzWAW\]]{.link-target}, Mishra et al, 2018. **Algorithm: SNAIL.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_scaling-rl .section}
## [8. Scaling RL](#keypapers.xhtml_id114){.toc-backref}

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[72\]   [Accelerated Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1803.02811){.reference .external}[ \[https://arxiv.org/abs/1803.02811\]]{.link-target}, Stooke and Abbeel, 2018. **Contribution:** Systematic analysis of parallelization in deep RL across algorithms.
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[73\]   [IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures](https://arxiv.org/abs/1802.01561){.reference .external}[ \[https://arxiv.org/abs/1802.01561\]]{.link-target}, Espeholt et al, 2018. **Algorithm: IMPALA.**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[74\]   [Distributed Prioritized Experience Replay](https://openreview.net/forum?id=H1Dy---0Z){.reference .external}[ \[https://openreview.net/forum?id=H1Dy---0Z\]]{.link-target}, Horgan et al, 2018. **Algorithm: Ape-X.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[75\]   [Recurrent Experience Replay in Distributed Reinforcement Learning](https://openreview.net/forum?id=r1lyTjAqYX){.reference .external}[ \[https://openreview.net/forum?id=r1lyTjAqYX\]]{.link-target}, Anonymous, 2018. **Algorithm: R2D2.**
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[76\]   [RLlib: Abstractions for Distributed Reinforcement Learning](https://arxiv.org/abs/1712.09381){.reference .external}[ \[https://arxiv.org/abs/1712.09381\]]{.link-target}, Liang et al, 2017. **Contribution:** A scalable library of RL algorithm implementations. [Documentation link.](https://ray.readthedocs.io/en/latest/rllib.html){.reference .external}[ \[https://ray.readthedocs.io/en/latest/rllib.html\]]{.link-target}
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_rl-in-the-real-world .section}
## [9. RL in the Real World](#keypapers.xhtml_id115){.toc-backref}

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[77\]   [Benchmarking Reinforcement Learning Algorithms on Real-World Robots](https://arxiv.org/abs/1809.07731){.reference .external}[ \[https://arxiv.org/abs/1809.07731\]]{.link-target}, Mahmood et al, 2018.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[78\]   [Learning Dexterous In-Hand Manipulation](https://arxiv.org/abs/1808.00177){.reference .external}[ \[https://arxiv.org/abs/1808.00177\]]{.link-target}, OpenAI, 2018.
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[79\]   [QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation](https://arxiv.org/abs/1806.10293){.reference .external}[ \[https://arxiv.org/abs/1806.10293\]]{.link-target}, Kalashnikov et al, 2018. **Algorithm: QT-Opt.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[80\]   [Horizon: Facebook's Open Source Applied Reinforcement Learning Platform](https://arxiv.org/abs/1811.00260){.reference .external}[ \[https://arxiv.org/abs/1811.00260\]]{.link-target}, Gauci et al, 2018.
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_safety .section}
## [10. Safety](#keypapers.xhtml_id116){.toc-backref}

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[81\]   [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565){.reference .external}[ \[https://arxiv.org/abs/1606.06565\]]{.link-target}, Amodei et al, 2016. **Contribution:** establishes a taxonomy of safety problems, serving as an important jumping-off point for future research. We need to solve these!
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[82\]   [Deep Reinforcement Learning From Human Preferences](https://arxiv.org/abs/1706.03741){.reference .external}[ \[https://arxiv.org/abs/1706.03741\]]{.link-target}, Christiano et al, 2017. **Algorithm: LFP.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[83\]   [Constrained Policy Optimization](https://arxiv.org/abs/1705.10528){.reference .external}[ \[https://arxiv.org/abs/1705.10528\]]{.link-target}, Achiam et al, 2017. **Algorithm: CPO.**
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[84\]   [Safe Exploration in Continuous Action Spaces](https://arxiv.org/abs/1801.08757){.reference .external}[ \[https://arxiv.org/abs/1801.08757\]]{.link-target}, Dalal et al, 2018. **Algorithm: DDPG+Safety Layer.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[85\]   [Trial without Error: Towards Safe Reinforcement Learning via Human Intervention](https://arxiv.org/abs/1707.05173){.reference .external}[ \[https://arxiv.org/abs/1707.05173\]]{.link-target}, Saunders et al, 2017. **Algorithm: HIRL.**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[86\]   [Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning](https://arxiv.org/abs/1711.06782){.reference .external}[ \[https://arxiv.org/abs/1711.06782\]]{.link-target}, Eysenbach et al, 2017. **Algorithm: Leave No Trace.**
  -------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_imitation-learning-and-inverse-reinforcement-learning .section}
## [11. Imitation Learning and Inverse Reinforcement Learning](#keypapers.xhtml_id117){.toc-backref}

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[87\]   [Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy](http://www.cs.cmu.edu/~bziebart/publications/thesis-bziebart.pdf){.reference .external}[ \[http://www.cs.cmu.edu/\~bziebart/publications/thesis-bziebart.pdf\]]{.link-target}, Ziebart 2010. **Contributions:** Crisp formulation of maximum entropy IRL.
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[88\]   [Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization](https://arxiv.org/abs/1603.00448){.reference .external}[ \[https://arxiv.org/abs/1603.00448\]]{.link-target}, Finn et al, 2016. **Algorithm: GCL.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[89\]   [Generative Adversarial Imitation Learning](https://arxiv.org/abs/1606.03476){.reference .external}[ \[https://arxiv.org/abs/1606.03476\]]{.link-target}, Ho and Ermon, 2016. **Algorithm: GAIL.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[90\]   [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://xbpeng.github.io/projects/DeepMimic/2018_TOG_DeepMimic.pdf){.reference .external}[ \[https://xbpeng.github.io/projects/DeepMimic/2018_TOG_DeepMimic.pdf\]]{.link-target}, Peng et al, 2018. **Algorithm: DeepMimic.**
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[91\]   [Variational Discriminator Bottleneck: Improving Imitation Learning, Inverse RL, and GANs by Constraining Information Flow](https://arxiv.org/abs/1810.00821){.reference .external}[ \[https://arxiv.org/abs/1810.00821\]]{.link-target}, Peng et al, 2018. **Algorithm: VAIL.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[92\]   [One-Shot High-Fidelity Imitation: Training Large-Scale Deep Nets with RL](https://arxiv.org/abs/1810.05017){.reference .external}[ \[https://arxiv.org/abs/1810.05017\]]{.link-target}, Le Paine et al, 2018. **Algorithm: MetaMimic.**
  -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_reproducibility-analysis-and-critique .section}
## [12. Reproducibility, Analysis, and Critique](#keypapers.xhtml_id118){.toc-backref}

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[93\]   [Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778){.reference .external}[ \[https://arxiv.org/abs/1604.06778\]]{.link-target}, Duan et al, 2016. **Contribution: rllab.**
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[94\]   [Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control](https://arxiv.org/abs/1708.04133){.reference .external}[ \[https://arxiv.org/abs/1708.04133\]]{.link-target}, Islam et al, 2017.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[95\]   [Deep Reinforcement Learning that Matters](https://arxiv.org/abs/1709.06560){.reference .external}[ \[https://arxiv.org/abs/1709.06560\]]{.link-target}, Henderson et al, 2017.
  -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[96\]   [Where Did My Optimum Go?: An Empirical Analysis of Gradient Descent Optimization in Policy Gradient Methods](https://arxiv.org/abs/1810.02525){.reference .external}[ \[https://arxiv.org/abs/1810.02525\]]{.link-target}, Henderson et al, 2018.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[97\]   [Are Deep Policy Gradient Algorithms Truly Policy Gradient Algorithms?](https://arxiv.org/abs/1811.02553){.reference .external}[ \[https://arxiv.org/abs/1811.02553\]]{.link-target}, Ilyas et al, 2018.
  -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[98\]   [Simple Random Search Provides a Competitive Approach to Reinforcement Learning](https://arxiv.org/abs/1803.07055){.reference .external}[ \[https://arxiv.org/abs/1803.07055\]]{.link-target}, Mania et al, 2018.
  -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[99\]   [Benchmarking Model-Based Reinforcement Learning](https://arxiv.org/abs/1907.02057){.reference .external}[ \[https://arxiv.org/abs/1907.02057\]]{.link-target}, Wang et al, 2019.
  -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {#keypapers.xhtml_bonus-classic-papers-in-rl-theory-or-review .section}
## [13. Bonus: Classic Papers in RL Theory or Review](#keypapers.xhtml_id119){.toc-backref}

  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[100\]   [Policy Gradient Methods for Reinforcement Learning with Function Approximation](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf){.reference .external}[ \[https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf\]]{.link-target}, Sutton et al, 2000. **Contributions:** Established policy gradient theorem and showed convergence of policy gradient algorithm for arbitrary policy classes.
  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[101\]   [An Analysis of Temporal-Difference Learning with Function Approximation](http://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf){.reference .external}[ \[http://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf\]]{.link-target}, Tsitsiklis and Van Roy, 1997. **Contributions:** Variety of convergence results and counter-examples for value-learning methods in RL.
  --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[102\]   [Reinforcement Learning of Motor Skills with Policy Gradients](http://www.kyb.mpg.de/fileadmin/user_upload/files/publications/attachments/Neural-Netw-2008-21-682_4867%5b0%5d.pdf){.reference .external}[ \[http://www.kyb.mpg.de/fileadmin/user_upload/files/publications/attachments/Neural-Netw-2008-21-682_4867%5b0%5d.pdf\]]{.link-target}, Peters and Schaal, 2008. **Contributions:** Thorough review of policy gradient methods at the time, many of which are still serviceable descriptions of deep RL methods.
  --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[103\]   [Approximately Optimal Approximate Reinforcement Learning](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf){.reference .external}[ \[https://people.eecs.berkeley.edu/\~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf\]]{.link-target}, Kakade and Langford, 2002. **Contributions:** Early roots for monotonic improvement theory, later leading to theoretical justification for TRPO and other algorithms.
  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[104\]   [A Natural Policy Gradient](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf){.reference .external}[ \[https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf\]]{.link-target}, Kakade, 2002. **Contributions:** Brought natural gradients into RL, later leading to TRPO, ACKTR, and several other methods in deep RL.
  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[105\]   [Algorithms for Reinforcement Learning](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf){.reference .external}[ \[https://sites.ualberta.ca/\~szepesva/papers/RLAlgsInMDPs.pdf\]]{.link-target}, Szepesvari, 2009. **Contributions:** Unbeatable reference on RL before deep RL, containing foundations and theoretical background.
  --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

[]{#exercises.xhtml}

::::::::::::::::::: {.body role="main"}
:::::::::::::::::: {#exercises.xhtml_exercises .section}
# [Exercises](#exercises.xhtml_id2){.toc-backref}

::: {#exercises.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Exercises](#exercises.xhtml_exercises){#exercises.xhtml_id2
  .reference .internal}
  - [Problem Set 1: Basics of
    Implementation](#exercises.xhtml_problem-set-1-basics-of-implementation){#exercises.xhtml_id3
    .reference .internal}
  - [Problem Set 2: Algorithm Failure
    Modes](#exercises.xhtml_problem-set-2-algorithm-failure-modes){#exercises.xhtml_id4
    .reference .internal}
  - [Challenges](#exercises.xhtml_challenges){#exercises.xhtml_id5
    .reference .internal}
:::

:::::: {#exercises.xhtml_problem-set-1-basics-of-implementation .section}
## [Problem Set 1: Basics of Implementation](#exercises.xhtml_id3){.toc-backref}

::: {.admonition-exercise-1-1-gaussian-log-likelihood .admonition}
Exercise 1.1: Gaussian Log-Likelihood

**Path to Exercise:**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_1/exercise1_1.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_1/exercise1_1.py`{.docutils
  .literal}]{.pre}

**Path to Solution:**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_1_solutions/exercise1_1_soln.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_1_solutions/exercise1_1_soln.py`{.docutils
  .literal}]{.pre}

**Instructions.** Write a function that takes in the means and log stds
of a batch of diagonal Gaussian distributions, along with
(previously-generated) samples from those distributions, and returns the
log likelihoods of those samples. (In the Tensorflow version, you will
write a function that creates computation graph operations to do this;
in the PyTorch version, you will directly operate on given Tensors.)

You may find it useful to review the formula given in [this section of
the RL introduction](rl_intro.html_stochastic-policies){.reference
.external}.

Implement your solution in [`exercise1_1.py`{.docutils .literal}]{.pre},
and run that file to automatically check your work.

**Evaluation Criteria.** Your solution will be checked by comparing
outputs against a known-good implementation, using a batch of random
inputs.
:::

::: {.admonition-exercise-1-2-policy-for-ppo .admonition}
Exercise 1.2: Policy for PPO

**Path to Exercise:**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_1/exercise1_2.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_1/exercise1_2.py`{.docutils
  .literal}]{.pre}

**Path to Solution:**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_1_solutions/exercise1_2_soln.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_1_solutions/exercise1_2_soln.py`{.docutils
  .literal}]{.pre}

**Instructions.** Implement an MLP diagonal Gaussian policy for PPO.

Implement your solution in [`exercise1_2.py`{.docutils .literal}]{.pre},
and run that file to automatically check your work.

**Evaluation Criteria.** Your solution will be evaluated by running for
20 epochs in the InvertedPendulum-v2 Gym environment, and this should
take in the ballpark of 3-5 minutes (depending on your machine, and
other processes you are running in the background). The bar for success
is reaching an average score of over 500 in the last 5 epochs, or
getting to a score of 1000 (the maximum possible score) in the last 5
epochs.
:::

::: {.admonition-exercise-1-3-computation-graph-for-td3 .admonition}
Exercise 1.3: Computation Graph for TD3

**Path to Exercise.**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_1/exercise1_3.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_1/exercise1_3.py`{.docutils
  .literal}]{.pre}

**Path to Solution.**

- PyTorch version: [`spinup/algos/pytorch/td3/td3.py`{.docutils
  .literal}]{.pre}
- Tensorflow version: [`spinup/algos/tf1/td3/td3.py`{.docutils
  .literal}]{.pre}

**Instructions.** Implement the main mathematical logic for the TD3
algorithm.

As starter code, you are given the entirety of the TD3 algorithm except
for the main mathematical logic (essentially, the loss functions and
intermediate calculations needed for them). Find "YOUR CODE HERE" to
begin.

You may find it useful to review the pseudocode in our [page on
TD3](../algorithms/td3.html){.reference .external}.

Implement your solution in [`exercise1_3.py`{.docutils .literal}]{.pre},
and run that file to see the results of your work. There is no automatic
checking for this exercise.

**Evaluation Criteria.** Evaluate your code by running
[`exercise1_3.py`{.docutils .literal}]{.pre} with HalfCheetah-v2,
InvertedPendulum-v2, and one other Gym MuJoCo environment of your
choosing (set via the [`--env`{.docutils .literal}]{.pre} flag). It is
set up to use smaller neural networks (hidden sizes \[128,128\]) than
typical for TD3, with a maximum episode length of 150, and to run for
only 10 epochs. The goal is to see significant learning progress
relatively quickly (in terms of wall clock time). Experiments will
likely take on the order of \~10 minutes.

Use the [`--use_soln`{.docutils .literal}]{.pre} flag to run Spinning
Up's TD3 instead of your implementation. Anecdotally, within 10 epochs,
the score in HalfCheetah should go over 300, and the score in
InvertedPendulum should max out at 150.
:::
::::::

::::::::: {#exercises.xhtml_problem-set-2-algorithm-failure-modes .section}
## [Problem Set 2: Algorithm Failure Modes](#exercises.xhtml_id4){.toc-backref}

::::: {.admonition-exercise-2-1-value-function-fitting-in-trpo .admonition}
Exercise 2.1: Value Function Fitting in TRPO

**Path to Exercise.** (Not applicable, there is no code for this one.)

**Path to Solution.** [Solution available
here.](../spinningup/exercise2_1_soln.html){.reference .external}

Many factors can impact the performance of policy gradient algorithms,
but few more drastically than the quality of the learned value function
used for advantage estimation.

In this exercise, you will compare results between runs of TRPO where
you put lots of effort into fitting the value function
([`train_v_iters=80`{.docutils .literal}]{.pre}), versus where you put
very little effort into fitting the value function
([`train_v_iters=0`{.docutils .literal}]{.pre}).

**Instructions.** Run the following command:

:::: highlight-default
::: highlight
    python -m spinup.run trpo --env Hopper-v2 --train_v_iters[v] 0 80 --exp_name ex2-1 --epochs 250 --steps_per_epoch 4000 --seed 0 10 20 --dt
:::
::::

and plot the results. (These experiments might take \~10 minutes each,
and this command runs six of them.) What do you find?
:::::

::::: {.admonition-exercise-2-2-silent-bug-in-ddpg .admonition}
Exercise 2.2: Silent Bug in DDPG

**Path to Exercise.**

- PyTorch version:
  [`spinup/exercises/pytorch/problem_set_2/exercise2_2.py`{.docutils
  .literal}]{.pre}
- Tensorflow version:
  [`spinup/exercises/tf1/problem_set_2/exercise2_2.py`{.docutils
  .literal}]{.pre}

**Path to Solution.** [Solution available
here.](../spinningup/exercise2_2_soln.html){.reference .external}

The hardest part of writing RL code is dealing with bugs, because
failures are frequently silent. The code will appear to run correctly,
but the agent's performance will degrade relative to a bug-free
implementation---sometimes to the extent that it never learns anything.

In this exercise, you will observe a bug in vivo and compare results
against correct code. The bug is the same (conceptually, if not in exact
implementation) for both the PyTorch and Tensorflow versions of this
exercise.

**Instructions.** Run [`exercise2_2.py`{.docutils .literal}]{.pre},
which will launch DDPG experiments with and without a bug. The
non-bugged version runs the default Spinning Up implementation of DDPG,
using a default method for creating the actor and critic networks. The
bugged version runs the same DDPG code, except uses a bugged method for
creating the networks.

There will be six experiments in all (three random seeds for each case),
and each should take in the ballpark of 10 minutes. When they're
finished, plot the results. What is the difference in performance with
and without the bug?

Without referencing the correct actor-critic code (which is to
say---don't look in DDPG's [`core.py`{.docutils .literal}]{.pre} file),
try to figure out what the bug is and explain how it breaks things.

**Hint.** To figure out what's going wrong, think about how the DDPG
code implements the DDPG computation graph. For the Tensorflow version,
look at this excerpt:

:::: highlight-python
::: highlight
    # Bellman backup for Q function
    backup = tf.stop_gradient(r_ph + gamma*(1-d_ph)*q_pi_targ)

    # DDPG losses
    pi_loss = -tf.reduce_mean(q_pi)
    q_loss = tf.reduce_mean((q-backup)**2)
:::
::::

How could a bug in the actor-critic code have an impact here?

**Bonus.** Are there any choices of hyperparameters which would have
hidden the effects of the bug?
:::::
:::::::::

::::: {#exercises.xhtml_challenges .section}
## [Challenges](#exercises.xhtml_id5){.toc-backref}

::: {.admonition-write-code-from-scratch .admonition}
Write Code from Scratch

As we suggest in [the essay](spinningup.html_learn-by-doing){.reference
.external}, try reimplementing various deep RL algorithms from scratch.
:::

::: {.admonition-requests-for-research .admonition}
Requests for Research

If you feel comfortable with writing deep learning and deep RL code,
consider trying to make progress on any of OpenAI's standing requests
for research:

- [Requests for Research
  1](https://openai.com/requests-for-research/){.reference .external}[
  \[https://openai.com/requests-for-research/\]]{.link-target}
- [Requests for Research
  2](https://blog.openai.com/requests-for-research-2/){.reference
  .external}[
  \[https://blog.openai.com/requests-for-research-2/\]]{.link-target}
:::
:::::
::::::::::::::::::
:::::::::::::::::::

[]{#bench.xhtml}

::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::: {#bench.xhtml_benchmarks-for-spinning-up-implementations .section}
# [Benchmarks for Spinning Up Implementations](#bench.xhtml_id11){.toc-backref}

::: {#bench.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Benchmarks for Spinning Up
  Implementations](#bench.xhtml_benchmarks-for-spinning-up-implementations){#bench.xhtml_id11
  .reference .internal}
  - [Performance in Each
    Environment](#bench.xhtml_performance-in-each-environment){#bench.xhtml_id12
    .reference .internal}
    - [HalfCheetah: PyTorch
      Versions](#bench.xhtml_halfcheetah-pytorch-versions){#bench.xhtml_id13
      .reference .internal}
    - [HalfCheetah: Tensorflow
      Versions](#bench.xhtml_halfcheetah-tensorflow-versions){#bench.xhtml_id14
      .reference .internal}
    - [Hopper: PyTorch
      Versions](#bench.xhtml_hopper-pytorch-versions){#bench.xhtml_id15
      .reference .internal}
    - [Hopper: Tensorflow
      Versions](#bench.xhtml_hopper-tensorflow-versions){#bench.xhtml_id16
      .reference .internal}
    - [Walker2d: PyTorch
      Versions](#bench.xhtml_walker2d-pytorch-versions){#bench.xhtml_id17
      .reference .internal}
    - [Walker2d: Tensorflow
      Versions](#bench.xhtml_walker2d-tensorflow-versions){#bench.xhtml_id18
      .reference .internal}
    - [Swimmer: PyTorch
      Versions](#bench.xhtml_swimmer-pytorch-versions){#bench.xhtml_id19
      .reference .internal}
    - [Swimmer: Tensorflow
      Versions](#bench.xhtml_swimmer-tensorflow-versions){#bench.xhtml_id20
      .reference .internal}
    - [Ant: PyTorch
      Versions](#bench.xhtml_ant-pytorch-versions){#bench.xhtml_id21
      .reference .internal}
    - [Ant: Tensorflow
      Versions](#bench.xhtml_ant-tensorflow-versions){#bench.xhtml_id22
      .reference .internal}
  - [Experiment
    Details](#bench.xhtml_experiment-details){#bench.xhtml_id23
    .reference .internal}
  - [PyTorch vs
    Tensorflow](#bench.xhtml_pytorch-vs-tensorflow){#bench.xhtml_id24
    .reference .internal}
:::

We benchmarked the Spinning Up algorithm implementations in five
environments from the
[MuJoCo](https://gym.openai.com/envs/#mujoco){.reference .external}[
\[https://gym.openai.com/envs/#mujoco\]]{.link-target} Gym task suite:
HalfCheetah, Hopper, Walker2d, Swimmer, and Ant.

::::::::::::::::::::::: {#bench.xhtml_performance-in-each-environment .section}
## [Performance in Each Environment](#bench.xhtml_id12){.toc-backref}

:::: {#bench.xhtml_halfcheetah-pytorch-versions .section}
### [HalfCheetah: PyTorch Versions](#bench.xhtml_id13){.toc-backref}

::: {#bench.xhtml_id1 .figure .align-center}
![../\_images/pytorch_halfcheetah_performance.svg](_images/pytorch_halfcheetah_performance.svg)

[3M timestep benchmark for HalfCheetah-v3 using **PyTorch**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_halfcheetah-tensorflow-versions .section}
### [HalfCheetah: Tensorflow Versions](#bench.xhtml_id14){.toc-backref}

::: {#bench.xhtml_id2 .figure .align-center}
![../\_images/tensorflow_halfcheetah_performance.svg](_images/tensorflow_halfcheetah_performance.svg)

[3M timestep benchmark for HalfCheetah-v3 using **Tensorflow**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_hopper-pytorch-versions .section}
### [Hopper: PyTorch Versions](#bench.xhtml_id15){.toc-backref}

::: {#bench.xhtml_id3 .figure .align-center}
![../\_images/pytorch_hopper_performance.svg](_images/pytorch_hopper_performance.svg)

[3M timestep benchmark for Hopper-v3 using **PyTorch**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_hopper-tensorflow-versions .section}
### [Hopper: Tensorflow Versions](#bench.xhtml_id16){.toc-backref}

::: {#bench.xhtml_id4 .figure .align-center}
![../\_images/tensorflow_hopper_performance.svg](_images/tensorflow_hopper_performance.svg)

[3M timestep benchmark for Hopper-v3 using **Tensorflow**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_walker2d-pytorch-versions .section}
### [Walker2d: PyTorch Versions](#bench.xhtml_id17){.toc-backref}

::: {#bench.xhtml_id5 .figure .align-center}
![../\_images/pytorch_walker2d_performance.svg](_images/pytorch_walker2d_performance.svg)

[3M timestep benchmark for Walker2d-v3 using **PyTorch**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_walker2d-tensorflow-versions .section}
### [Walker2d: Tensorflow Versions](#bench.xhtml_id18){.toc-backref}

::: {#bench.xhtml_id6 .figure .align-center}
![../\_images/tensorflow_walker2d_performance.svg](_images/tensorflow_walker2d_performance.svg)

[3M timestep benchmark for Walker2d-v3 using **Tensorflow**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_swimmer-pytorch-versions .section}
### [Swimmer: PyTorch Versions](#bench.xhtml_id19){.toc-backref}

::: {#bench.xhtml_id7 .figure .align-center}
![../\_images/pytorch_swimmer_performance.svg](_images/pytorch_swimmer_performance.svg)

[3M timestep benchmark for Swimmer-v3 using **PyTorch**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_swimmer-tensorflow-versions .section}
### [Swimmer: Tensorflow Versions](#bench.xhtml_id20){.toc-backref}

::: {#bench.xhtml_id8 .figure .align-center}
![../\_images/tensorflow_swimmer_performance.svg](_images/tensorflow_swimmer_performance.svg)

[3M timestep benchmark for Swimmer-v3 using **Tensorflow**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_ant-pytorch-versions .section}
### [Ant: PyTorch Versions](#bench.xhtml_id21){.toc-backref}

::: {#bench.xhtml_id9 .figure .align-center}
![../\_images/pytorch_ant_performance.svg](_images/pytorch_ant_performance.svg)

[3M timestep benchmark for Ant-v3 using **PyTorch**
implementations.]{.caption-text}
:::
::::

:::: {#bench.xhtml_ant-tensorflow-versions .section}
### [Ant: Tensorflow Versions](#bench.xhtml_id22){.toc-backref}

::: {#bench.xhtml_id10 .figure .align-center}
![../\_images/tensorflow_ant_performance.svg](_images/tensorflow_ant_performance.svg)

[3M timestep benchmark for Ant-v3 using **Tensorflow**
implementations.]{.caption-text}
:::
::::
:::::::::::::::::::::::

:::: {#bench.xhtml_experiment-details .section}
## [Experiment Details](#bench.xhtml_id23){.toc-backref}

**Random seeds.** All experiments were run for 10 random seeds each.
Graphs show the average (solid line) and std dev (shaded) of performance
over random seed over the course of training.

**Performance metric.** Performance for the on-policy algorithms is
measured as the average trajectory return across the batch collected at
each epoch. Performance for the off-policy algorithms is measured once
every 10,000 steps by running the deterministic policy (or, in the case
of SAC, the mean policy) without action noise for ten trajectories, and
reporting the average return over those test trajectories.

**Network architectures.** The on-policy algorithms use networks of size
(64, 32) with tanh units for both the policy and the value function. The
off-policy algorithms use networks of size (256, 256) with relu units.

**Batch size.** The on-policy algorithms collected 4000 steps of
agent-environment interaction per batch update. The off-policy
algorithms used minibatches of size 100 at each gradient descent step.

All other hyperparameters are left at default settings for the Spinning
Up implementations. See algorithm pages for details.

Learning curves are smoothed by averaging over a window of 11 epochs.

::: {.admonition-you-should-know .admonition}
You Should Know

By comparison to the literature, the Spinning Up implementations of
DDPG, TD3, and SAC are roughly at-parity with the best reported results
for these algorithms. As a result, you can use the Spinning Up
implementations of these algorithms for research purposes.

The Spinning Up implementations of VPG, TRPO, and PPO are overall a bit
weaker than the best reported results for these algorithms. This is due
to the absence of some standard tricks (such as observation
normalization and normalized value regression targets) from our
implementations. For research comparisons, you should use the
implementations of TRPO or PPO from [OpenAI
Baselines](https://github.com/openai/baselines){.reference .external}[
\[https://github.com/openai/baselines\]]{.link-target}.
:::
::::

::: {#bench.xhtml_pytorch-vs-tensorflow .section}
## [PyTorch vs Tensorflow](#bench.xhtml_id24){.toc-backref}

We provide graphs for head-to-head comparisons between the PyTorch and
Tensorflow implementations of each algorithm at the following pages:

- [VPG Head-to-Head](../spinningup/bench_vpg.html){.reference .external}
- [PPO Head-to-Head](../spinningup/bench_ppo.html){.reference .external}
- [DDPG Head-to-Head](../spinningup/bench_ddpg.html){.reference
  .external}
- [TD3 Head-to-Head](../spinningup/bench_td3.html){.reference .external}
- [SAC Head-to-Head](../spinningup/bench_sac.html){.reference .external}
:::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

[]{#vpg.xhtml}

::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::: {#vpg.xhtml_vanilla-policy-gradient .section}
# [Vanilla Policy Gradient](#vpg.xhtml_id1){.toc-backref}

::: {#vpg.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Vanilla Policy
  Gradient](#vpg.xhtml_vanilla-policy-gradient){#vpg.xhtml_id1
  .reference .internal}
  - [Background](#vpg.xhtml_background){#vpg.xhtml_id2 .reference
    .internal}
    - [Quick Facts](#vpg.xhtml_quick-facts){#vpg.xhtml_id3 .reference
      .internal}
    - [Key Equations](#vpg.xhtml_key-equations){#vpg.xhtml_id4
      .reference .internal}
    - [Exploration vs.
      Exploitation](#vpg.xhtml_exploration-vs-exploitation){#vpg.xhtml_id5
      .reference .internal}
    - [Pseudocode](#vpg.xhtml_pseudocode){#vpg.xhtml_id6 .reference
      .internal}
  - [Documentation](#vpg.xhtml_documentation){#vpg.xhtml_id7 .reference
    .internal}
    - [Documentation: PyTorch
      Version](#vpg.xhtml_documentation-pytorch-version){#vpg.xhtml_id8
      .reference .internal}
    - [Saved Model Contents: PyTorch
      Version](#vpg.xhtml_saved-model-contents-pytorch-version){#vpg.xhtml_id9
      .reference .internal}
    - [Documentation: Tensorflow
      Version](#vpg.xhtml_documentation-tensorflow-version){#vpg.xhtml_id10
      .reference .internal}
    - [Saved Model Contents: Tensorflow
      Version](#vpg.xhtml_saved-model-contents-tensorflow-version){#vpg.xhtml_id11
      .reference .internal}
  - [References](#vpg.xhtml_references){#vpg.xhtml_id12 .reference
    .internal}
    - [Relevant Papers](#vpg.xhtml_relevant-papers){#vpg.xhtml_id13
      .reference .internal}
    - [Why These Papers?](#vpg.xhtml_why-these-papers){#vpg.xhtml_id14
      .reference .internal}
    - [Other Public
      Implementations](#vpg.xhtml_other-public-implementations){#vpg.xhtml_id15
      .reference .internal}
:::

:::::::::: {#vpg.xhtml_background .section}
## [Background](#vpg.xhtml_id2){.toc-backref}

(Previously: [Introduction to RL, Part
3](../spinningup/rl_intro3.html){.reference .external})

The key idea underlying policy gradients is to push up the probabilities
of actions that lead to higher return, and push down the probabilities
of actions that lead to lower return, until you arrive at the optimal
policy.

::: {#vpg.xhtml_quick-facts .section}
### [Quick Facts](#vpg.xhtml_id3){.toc-backref}

- VPG is an on-policy algorithm.
- VPG can be used for environments with either discrete or continuous
  action spaces.
- The Spinning Up implementation of VPG supports parallelization with
  MPI.
:::

::::: {#vpg.xhtml_key-equations .section}
### [Key Equations](#vpg.xhtml_id4){.toc-backref}

Let
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}
denote a policy with parameters
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math},
and
![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math}
denote the expected finite-horizon undiscounted return of the policy.
The gradient of
![J(\\pi\_{\\theta})](_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg){.math}
is

::: math
![\\nabla\_{\\theta} J(\\pi\_{\\theta}) = \\underE{\\tau \\sim
\\pi\_{\\theta}}{ \\sum\_{t=0}\^{T} \\nabla\_{\\theta} \\log
\\pi\_{\\theta}(a_t\|s_t) A\^{\\pi\_{\\theta}}(s_t,a_t)
},](_images/math/ada1266646d71c941e77e3fd41bba9d92d06b7c2.svg)
:::

where
![\\tau](_images/math/67a5412645decf6424bdd97aed3e9e7601bd784f.svg){.math}
is a trajectory and
![A\^{\\pi\_{\\theta}}](_images/math/5441ceb0039c72b114bb209edcd3bbbbe486c02c.svg){.math}
is the advantage function for the current policy.

The policy gradient algorithm works by updating policy parameters via
stochastic gradient ascent on policy performance:

::: math
![\\theta\_{k+1} = \\theta_k + \\alpha \\nabla\_{\\theta}
J(\\pi\_{\\theta_k})](_images/math/f5198e001f2c6053222b709af633865deb249cdf.svg)
:::

Policy gradient implementations typically compute advantage function
estimates based on the infinite-horizon discounted return, despite
otherwise using the finite-horizon undiscounted policy gradient formula.
:::::

::: {#vpg.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#vpg.xhtml_id5){.toc-backref}

VPG trains a stochastic policy in an on-policy way. This means that it
explores by sampling actions according to the latest version of its
stochastic policy. The amount of randomness in action selection depends
on both initial conditions and the training procedure. Over the course
of training, the policy typically becomes progressively less random, as
the update rule encourages it to exploit rewards that it has already
found. This may cause the policy to get trapped in local optima.
:::

:::: {#vpg.xhtml_pseudocode .section}
### [Pseudocode](#vpg.xhtml_id6){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{Vanilla Policy Gradient Algorithm}
\\label{alg1} \\begin{algorithmic}\[1\] \\STATE Input: initial policy
parameters \$\\theta_0\$, initial value function parameters \$\\phi_0\$
\\FOR{\$k = 0,1,2,\...\$} \\STATE Collect set of trajectories
\${\\mathcal D}\_k = \\{\\tau_i\\}\$ by running policy \$\\pi_k =
\\pi(\\theta_k)\$ in the environment. \\STATE Compute rewards-to-go
\$\\hat{R}\_t\$. \\STATE Compute advantage estimates, \$\\hat{A}\_t\$
(using any method of advantage estimation) based on the current value
function \$V\_{\\phi_k}\$. \\STATE Estimate policy gradient as
\\begin{equation\*} \\hat{g}\_k = \\frac{1}{\|{\\mathcal D}\_k\|}
\\sum\_{\\tau \\in {\\mathcal D}\_k} \\sum\_{t=0}\^T \\left.
\\nabla\_{\\theta} \\log\\pi\_{\\theta}(a_t\|s_t)\\right\|\_{\\theta_k}
\\hat{A}\_t. \\end{equation\*} \\STATE Compute policy update, either
using standard gradient ascent, \\begin{equation\*} \\theta\_{k+1} =
\\theta_k + \\alpha_k \\hat{g}\_k, \\end{equation\*} or via another
gradient ascent algorithm like Adam. \\STATE Fit value function by
regression on mean-squared error: \\begin{equation\*} \\phi\_{k+1} =
\\arg \\min\_{\\phi} \\frac{1}{\|{\\mathcal D}\_k\| T} \\sum\_{\\tau
\\in {\\mathcal D}\_k} \\sum\_{t=0}\^T\\left( V\_{\\phi} (s_t) -
\\hat{R}\_t \\right)\^2, \\end{equation\*} typically via some gradient
descent algorithm. \\ENDFOR \\end{algorithmic}
\\end{algorithm}](_images/math/262538f3077a7be8ce89066abbab523575132996.svg)
:::
::::
::::::::::

:::::::::: {#vpg.xhtml_documentation .section}
## [Documentation](#vpg.xhtml_id7){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow
implementations of VPG in Spinning Up. They have nearly identical
function calls and docstrings, except for details relating to model
construction. However, we include both full docstrings for completeness.
:::

::: {#vpg.xhtml_documentation-pytorch-version .section}
### [Documentation: PyTorch Version](#vpg.xhtml_id8){.toc-backref}

`spinup.`{.descclassname}`vpg_pytorch`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<MagicMock spec=\'str\' id=\'140679788252016\'\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=50*, *gamma=0.99*, *pi_lr=0.0003*, *vf_lr=0.001*, *train_v_iters=80*, *lam=0.97*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=10*[)]{.sig-paren}

:   Vanilla Policy Gradient

    (with GAE-Lambda for advantage estimation)

    +-------------+--------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment  |
    |             |   must satisfy the OpenAI Gym API.                                                   |
    |             |                                                                                      |
    |             | - **actor_critic** --                                                                |
    |             |                                                                                      |
    |             |   The constructor method for a PyTorch Module with a [`step`{.docutils               |
    |             |   .literal}]{.pre} method, an [`act`{.docutils .literal}]{.pre} method, a            |
    |             |   [`pi`{.docutils .literal}]{.pre} module, and a [`v`{.docutils .literal}]{.pre}     |
    |             |   module. The [`step`{.docutils .literal}]{.pre} method should accept a batch of     |
    |             |   observations and return:                                                           |
    |             |                                                                                      |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | Symbol              | Shape           | Description                            | |
    |             |   +=====================+=================+========================================+ |
    |             |   | [`a`{.docutils      | (batch,         | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    | act_dim)        | ::: line                               | |
    |             |   |                     |                 | Numpy array of actions for each        | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | observation.                           | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | [`v`{.docutils      | (batch,)        | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    |                 | ::: line                               | |
    |             |   |                     |                 | Numpy array of value estimates         | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | for the provided observations.         | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | [`logp_a`{.docutils | (batch,)        | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    |                 | ::: line                               | |
    |             |   |                     |                 | Numpy array of log probs for the       | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | actions in [`a`{.docutils              | |
    |             |   |                     |                 | .literal}]{.pre}.                      | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |                                                                                      |
    |             |   The [`act`{.docutils .literal}]{.pre} method behaves the same as [`step`{.docutils |
    |             |   .literal}]{.pre} but only returns [`a`{.docutils .literal}]{.pre}.                 |
    |             |                                                                                      |
    |             |   The [`pi`{.docutils .literal}]{.pre} module's forward call should accept a batch   |
    |             |   of observations and optionally a batch of actions, and return:                     |
    |             |                                                                                      |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |   | Symbol              | Shape         | Description                              | |
    |             |   +=====================+===============+==========================================+ |
    |             |   | [`pi`{.docutils     | N/A           | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}    |               | ::: line                                 | |
    |             |   |                     |               | Torch Distribution object, containing    | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | a batch of distributions describing      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the policy for the provided              | |
    |             |   |                     |               | observations.                            | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               | ::::::                                   | |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |   | [`logp_a`{.docutils | (batch,)      | ::::::::: {.first .last .line-block}     | |
    |             |   | .literal}]{.pre}    |               | ::: line                                 | |
    |             |   |                     |               | Optional (only returned if batch of      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | actions is given). Tensor containing     | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the log probability, according to        | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the policy, of the provided actions.     | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | If actions not given, will contain       | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | [`None`{.docutils .literal}]{.pre}.      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               | :::::::::                                | |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |                                                                                      |
    |             |   The [`v`{.docutils .literal}]{.pre} module's forward call should accept a batch of |
    |             |   observations and return:                                                           |
    |             |                                                                                      |
    |             |   +------------------+---------------+------------------------------------------+    |
    |             |   | Symbol           | Shape         | Description                              |    |
    |             |   +==================+===============+==========================================+    |
    |             |   | [`v`{.docutils   | (batch,)      | :::::: {.first .last .line-block}        |    |
    |             |   | .literal}]{.pre} |               | ::: line                                 |    |
    |             |   |                  |               | Tensor containing the value estimates    |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               |                                          |    |
    |             |   |                  |               | ::: line                                 |    |
    |             |   |                  |               | for the provided observations.           |    |
    |             |   |                  |               | (Critical:                               |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               |                                          |    |
    |             |   |                  |               | ::: line                                 |    |
    |             |   |                  |               | make sure to flatten this!)              |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               | ::::::                                   |    |
    |             |   +------------------+---------------+------------------------------------------+    |
    |             |                                                                                      |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the ActorCritic object you    |
    |             |   provided to VPG.                                                                   |
    |             |                                                                                      |
    |             | - **seed** (*int*) -- Seed for random number generators.                             |
    |             |                                                                                      |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs) |
    |             |   for the agent and the environment in each epoch.                                   |
    |             |                                                                                      |
    |             | - **epochs** (*int*) -- Number of epochs of interaction (equivalent to number of     |
    |             |   policy updates) to perform.                                                        |
    |             |                                                                                      |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                  |
    |             |                                                                                      |
    |             | - **pi_lr** (*float*) -- Learning rate for policy optimizer.                         |
    |             |                                                                                      |
    |             | - **vf_lr** (*float*) -- Learning rate for value function optimizer.                 |
    |             |                                                                                      |
    |             | - **train_v_iters** (*int*) -- Number of gradient descent steps to take on value     |
    |             |   function per epoch.                                                                |
    |             |                                                                                      |
    |             | - **lam** (*float*) -- Lambda for GAE-Lambda. (Always between 0 and 1, close to 1.)  |
    |             |                                                                                      |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.        |
    |             |                                                                                      |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                        |
    |             |                                                                                      |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the    |
    |             |   current policy and value function.                                                 |
    +-------------+--------------------------------------------------------------------------------------+
:::

::::: {#vpg.xhtml_saved-model-contents-pytorch-version .section}
### [Saved Model Contents: PyTorch Version](#vpg.xhtml_id9){.toc-backref}

The PyTorch saved model can be loaded with [`ac`{.docutils
.literal}]{.pre}` `{.docutils .literal}[`=`{.docutils
.literal}]{.pre}` `{.docutils
.literal}[`torch.load('path/to/model.pt')`{.docutils .literal}]{.pre},
yielding an actor-critic object ([`ac`{.docutils .literal}]{.pre}) that
has the properties described in the docstring for
[`vpg_pytorch`{.docutils .literal}]{.pre}.

You can get actions from this model with

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::

::: {#vpg.xhtml_documentation-tensorflow-version .section}
### [Documentation: Tensorflow Version](#vpg.xhtml_id10){.toc-backref}

`spinup.`{.descclassname}`vpg_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=50*, *gamma=0.99*, *pi_lr=0.0003*, *vf_lr=0.001*, *train_v_iters=80*, *lam=0.97*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=10*[)]{.sig-paren}

:   Vanilla Policy Gradient

    (with GAE-Lambda for advantage estimation)

    +-------------+----------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment    |
    |             |   must satisfy the OpenAI Gym API.                                                     |
    |             |                                                                                        |
    |             | - **actor_critic** --                                                                  |
    |             |                                                                                        |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils           |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns the    |
    |             |   main outputs from the agent's Tensorflow computation graph:                          |
    |             |                                                                                        |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | Symbol               | Shape          | Description                              | |
    |             |   +======================+================+==========================================+ |
    |             |   | [`pi`{.docutils      | (batch,        | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre}     | act_dim)       | ::: line                                 | |
    |             |   |                      |                | Samples actions from policy given        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | states.                                  | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | :::::                                    | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`logp`{.docutils    | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives log probability, according to      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | the policy, of taking actions            | |
    |             |   |                      |                | [`a_ph`{.docutils .literal}]{.pre}       | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | in states [`x_ph`{.docutils              | |
    |             |   |                      |                | .literal}]{.pre}.                        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`logp_pi`{.docutils | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives log probability, according to      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | the policy, of the action sampled by     | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | [`pi`{.docutils .literal}]{.pre}.        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`v`{.docutils       | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives the value estimate for states      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | in [`x_ph`{.docutils .literal}]{.pre}.   | |
    |             |   |                      |                | (Critical: make sure                     | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | to flatten this!)                        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |                                                                                        |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function you   |
    |             |   provided to VPG.                                                                     |
    |             |                                                                                        |
    |             | - **seed** (*int*) -- Seed for random number generators.                               |
    |             |                                                                                        |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs)   |
    |             |   for the agent and the environment in each epoch.                                     |
    |             |                                                                                        |
    |             | - **epochs** (*int*) -- Number of epochs of interaction (equivalent to number of       |
    |             |   policy updates) to perform.                                                          |
    |             |                                                                                        |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                    |
    |             |                                                                                        |
    |             | - **pi_lr** (*float*) -- Learning rate for policy optimizer.                           |
    |             |                                                                                        |
    |             | - **vf_lr** (*float*) -- Learning rate for value function optimizer.                   |
    |             |                                                                                        |
    |             | - **train_v_iters** (*int*) -- Number of gradient descent steps to take on value       |
    |             |   function per epoch.                                                                  |
    |             |                                                                                        |
    |             | - **lam** (*float*) -- Lambda for GAE-Lambda. (Always between 0 and 1, close to 1.)    |
    |             |                                                                                        |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.          |
    |             |                                                                                        |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                          |
    |             |                                                                                        |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the      |
    |             |   current policy and value function.                                                   |
    +-------------+----------------------------------------------------------------------------------------+
:::

::: {#vpg.xhtml_saved-model-contents-tensorflow-version .section}
### [Saved Model Contents: Tensorflow Version](#vpg.xhtml_id11){.toc-backref}

The computation graph saved by the logger includes:

  ----------------------------------------------------------------------------------
  Key                Value
  ------------------ ---------------------------------------------------------------
  [`x`{.docutils     Tensorflow placeholder for state input.
  .literal}]{.pre}   

  [`pi`{.docutils    Samples an action from the agent, conditioned on states in
  .literal}]{.pre}   [`x`{.docutils .literal}]{.pre}.

  [`v`{.docutils     Gives value estimate for states in [`x`{.docutils
  .literal}]{.pre}   .literal}]{.pre}.
  ----------------------------------------------------------------------------------

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.
:::
::::::::::

:::::: {#vpg.xhtml_references .section}
## [References](#vpg.xhtml_id12){.toc-backref}

::: {#vpg.xhtml_relevant-papers .section}
### [Relevant Papers](#vpg.xhtml_id13){.toc-backref}

- [Policy Gradient Methods for Reinforcement Learning with Function
  Approximation](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf){.reference
  .external}[
  \[https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf\]]{.link-target},
  Sutton et al. 2000
- [Optimizing Expectations: From Deep Reinforcement Learning to
  Stochastic Computation
  Graphs](http://joschu.net/docs/thesis.pdf){.reference .external}[
  \[http://joschu.net/docs/thesis.pdf\]]{.link-target}, Schulman 2016(a)
- [Benchmarking Deep Reinforcement Learning for Continuous
  Control](https://arxiv.org/abs/1604.06778){.reference .external}[
  \[https://arxiv.org/abs/1604.06778\]]{.link-target}, Duan et al. 2016
- [High Dimensional Continuous Control Using Generalized Advantage
  Estimation](https://arxiv.org/abs/1506.02438){.reference .external}[
  \[https://arxiv.org/abs/1506.02438\]]{.link-target}, Schulman et al.
  2016(b)
:::

::: {#vpg.xhtml_why-these-papers .section}
### [Why These Papers?](#vpg.xhtml_id14){.toc-backref}

Sutton 2000 is included because it is a timeless classic of
reinforcement learning theory, and contains references to the earlier
work which led to modern policy gradients. Schulman 2016(a) is included
because Chapter 2 contains a lucid introduction to the theory of policy
gradient algorithms, including pseudocode. Duan 2016 is a clear, recent
benchmark paper that shows how vanilla policy gradient in the deep RL
setting (eg with neural network policies and Adam as the optimizer)
compares with other deep RL algorithms. Schulman 2016(b) is included
because our implementation of VPG makes use of Generalized Advantage
Estimation for computing the policy gradient.
:::

::: {#vpg.xhtml_other-public-implementations .section}
### [Other Public Implementations](#vpg.xhtml_id15){.toc-backref}

- [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/vpg.py){.reference
  .external}[
  \[https://github.com/rll/rllab/blob/master/rllab/algos/vpg.py\]]{.link-target}
- [rllib
  (Ray)](https://github.com/ray-project/ray/blob/master/python/ray/rllib/agents/pg){.reference
  .external}[
  \[https://github.com/ray-project/ray/blob/master/python/ray/rllib/agents/pg\]]{.link-target}
:::
::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

[]{#trpo.xhtml}

:::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::: {#trpo.xhtml_trust-region-policy-optimization .section}
# [Trust Region Policy Optimization](#trpo.xhtml_id4){.toc-backref}

::: {#trpo.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Trust Region Policy
  Optimization](#trpo.xhtml_trust-region-policy-optimization){#trpo.xhtml_id4
  .reference .internal}
  - [Background](#trpo.xhtml_background){#trpo.xhtml_id5 .reference
    .internal}
    - [Quick Facts](#trpo.xhtml_quick-facts){#trpo.xhtml_id6 .reference
      .internal}
    - [Key Equations](#trpo.xhtml_key-equations){#trpo.xhtml_id7
      .reference .internal}
    - [Exploration vs.
      Exploitation](#trpo.xhtml_exploration-vs-exploitation){#trpo.xhtml_id8
      .reference .internal}
    - [Pseudocode](#trpo.xhtml_pseudocode){#trpo.xhtml_id9 .reference
      .internal}
  - [Documentation](#trpo.xhtml_documentation){#trpo.xhtml_id10
    .reference .internal}
    - [Saved Model
      Contents](#trpo.xhtml_saved-model-contents){#trpo.xhtml_id11
      .reference .internal}
  - [References](#trpo.xhtml_references){#trpo.xhtml_id12 .reference
    .internal}
    - [Relevant Papers](#trpo.xhtml_relevant-papers){#trpo.xhtml_id13
      .reference .internal}
    - [Why These Papers?](#trpo.xhtml_why-these-papers){#trpo.xhtml_id14
      .reference .internal}
    - [Other Public
      Implementations](#trpo.xhtml_other-public-implementations){#trpo.xhtml_id15
      .reference .internal}
:::

:::::::::::::::::: {#trpo.xhtml_background .section}
## [Background](#trpo.xhtml_id5){.toc-backref}

(Previously: [Background for VPG](vpg.html_background){.reference
.external})

TRPO updates policies by taking the largest step possible to improve
performance, while satisfying a special constraint on how close the new
and old policies are allowed to be. The constraint is expressed in terms
of
[KL-Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence){.reference
.external}[
\[https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence\]]{.link-target},
a measure of (something like, but not exactly) distance between
probability distributions.

This is different from normal policy gradient, which keeps new and old
policies close in parameter space. But even seemingly small differences
in parameter space can have very large differences in performance---so a
single bad step can collapse the policy performance. This makes it
dangerous to use large step sizes with vanilla policy gradients, thus
hurting its sample efficiency. TRPO nicely avoids this kind of collapse,
and tends to quickly and monotonically improve performance.

::: {#trpo.xhtml_quick-facts .section}
### [Quick Facts](#trpo.xhtml_id6){.toc-backref}

- TRPO is an on-policy algorithm.
- TRPO can be used for environments with either discrete or continuous
  action spaces.
- The Spinning Up implementation of TRPO supports parallelization with
  MPI.
:::

::::::::::::: {#trpo.xhtml_key-equations .section}
### [Key Equations](#trpo.xhtml_id7){.toc-backref}

Let
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}
denote a policy with parameters
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math}.
The theoretical TRPO update is:

::: math
![\\theta\_{k+1} = \\arg \\max\_{\\theta} \\; & {\\mathcal L}(\\theta_k,
\\theta) \\\\ \\text{s.t.} \\; & \\bar{D}\_{KL}(\\theta \|\| \\theta_k)
\\leq
\\delta](_images/math/23edf1f72f63a4729c40371c1481a36549a0b713.svg)
:::

where ![{\\mathcal L}(\\theta_k,
\\theta)](_images/math/0837b005b194415b2b922e42be1df8601b552857.svg){.math}
is the *surrogate advantage*, a measure of how policy
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}
performs relative to the old policy
![\\pi\_{\\theta_k}](_images/math/d8bb9f337fa712549e0428223df820773aa1169d.svg){.math}
using data from the old policy:

::: math
![{\\mathcal L}(\\theta_k, \\theta) = \\underE{s,a \\sim
\\pi\_{\\theta_k}}{
\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)}
A\^{\\pi\_{\\theta_k}}(s,a)
},](_images/math/ae8edab1e9c727bed15e54d4dda492382538b5fe.svg)
:::

and ![\\bar{D}\_{KL}(\\theta \|\|
\\theta_k)](_images/math/88396050a58384b85dfaa6fce02cf39d98c78c4b.svg){.math}
is an average KL-divergence between policies across states visited by
the old policy:

::: math
![\\bar{D}\_{KL}(\\theta \|\| \\theta_k) = \\underE{s \\sim
\\pi\_{\\theta_k}}{ D\_{KL}\\left(\\pi\_{\\theta}(\\cdot\|s) \|\|
\\pi\_{\\theta_k} (\\cdot\|s) \\right)
}.](_images/math/78a651e0ce4979bd3e17198594ad952ac20b9b45.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

The objective and constraint are both zero when ![\\theta =
\\theta_k](_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg){.math}.
Furthermore, the gradient of the constraint with respect to
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math}
is zero when ![\\theta =
\\theta_k](_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg){.math}.
Proving these facts requires some subtle command of the relevant
math---it's an exercise worth doing, whenever you feel ready!
:::

The theoretical TRPO update isn't the easiest to work with, so TRPO
makes some approximations to get an answer quickly. We Taylor expand the
objective and constraint to leading order around
![\\theta_k](_images/math/a485f77ef16acbb27539cdfe8286cd6029ccfd26.svg){.math}:

::: math
![{\\mathcal L}(\\theta_k, \\theta) &\\approx g\^T (\\theta - \\theta_k)
\\\\ \\bar{D}\_{KL}(\\theta \|\| \\theta_k) & \\approx \\frac{1}{2}
(\\theta - \\theta_k)\^T H (\\theta -
\\theta_k)](_images/math/7cdaa039734ec1d09adcc3e4dc351085823085cf.svg)
:::

resulting in an approximate optimization problem,

::: math
![\\theta\_{k+1} = \\arg \\max\_{\\theta} \\; & g\^T (\\theta -
\\theta_k) \\\\ \\text{s.t.} \\; & \\frac{1}{2} (\\theta - \\theta_k)\^T
H (\\theta - \\theta_k) \\leq
\\delta.](_images/math/69c9dcbe2fe1c669a1b2cb3a312a479cdfcb27a1.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

By happy coincidence, the gradient
![g](_images/math/7c8bf3a1920993c53ae254d3f08d697f368af350.svg){.math}
of the surrogate advantage function with respect to
![\\theta](_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg){.math},
evaluated at ![\\theta =
\\theta_k](_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg){.math},
is exactly equal to the policy gradient, ![\\nabla\_{\\theta}
J(\\pi\_{\\theta})](_images/math/fdc185c68404ece5c4deef076c9713af689421a2.svg){.math}!
Try proving this, if you feel comfortable diving into the math.
:::

This approximate problem can be analytically solved by the methods of
Lagrangian duality [\[1\]](#trpo.xhtml_id2){#trpo.xhtml_id1
.footnote-reference}, yielding the solution:

::: math
![\\theta\_{k+1} = \\theta_k + \\sqrt{\\frac{2 \\delta}{g\^T H\^{-1} g}}
H\^{-1} g.](_images/math/e990f7ff0230a8fa93cf1242ea0d49fdf63d05d7.svg)
:::

If we were to stop here, and just use this final result, the algorithm
would be exactly calculating the [Natural Policy
Gradient](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf){.reference
.external}[
\[https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf\]]{.link-target}.
A problem is that, due to the approximation errors introduced by the
Taylor expansion, this may not satisfy the KL constraint, or actually
improve the surrogate advantage. TRPO adds a modification to this update
rule: a backtracking line search,

::: math
![\\theta\_{k+1} = \\theta_k + \\alpha\^j \\sqrt{\\frac{2 \\delta}{g\^T
H\^{-1} g}} H\^{-1}
g,](_images/math/03cabd66ab79d8c17e36fc4247bb46fe0c6dcbfc.svg)
:::

where ![\\alpha \\in
(0,1)](_images/math/85e2502878c575c6e250a9224be42065ac9844d2.svg){.math}
is the backtracking coefficient, and
![j](_images/math/b42a5fa0aad66603180aff0fc5e346e98a2364ca.svg){.math}
is the smallest nonnegative integer such that
![\\pi\_{\\theta\_{k+1}}](_images/math/3944f0149054734c7f8537d8f9316cd77cbbb143.svg){.math}
satisfies the KL constraint and produces a positive surrogate advantage.

Lastly: computing and storing the matrix inverse,
![H\^{-1}](_images/math/c61d52a1bdbbfa95c007324ae431066f95be2296.svg){.math},
is painfully expensive when dealing with neural network policies with
thousands or millions of parameters. TRPO sidesteps the issue by using
the [conjugate
gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method){.reference
.external}[
\[https://en.wikipedia.org/wiki/Conjugate_gradient_method\]]{.link-target}
algorithm to solve ![Hx =
g](_images/math/1e5b7619f5aff65751670c7d6b3527e5721a9033.svg){.math} for
![x = H\^{-1}
g](_images/math/a0181d85fab06c9716a1bb2561dbf0f8534ef172.svg){.math},
requiring only a function which can compute the matrix-vector product
![Hx](_images/math/7c097b2fe748e8a45446bdc5d27721c82b75e969.svg){.math}
instead of computing and storing the whole matrix
![H](_images/math/bf6bcb1745aeab36cdc185e9f75bbfd3998352ce.svg){.math}
directly. This is not too hard to do: we set up a symbolic operation to
calculate

::: math
![Hx = \\nabla\_{\\theta} \\left( \\left(\\nabla\_{\\theta}
\\bar{D}\_{KL}(\\theta \|\| \\theta_k)\\right)\^T x
\\right),](_images/math/2b50eb41a25af9e480d1c6facfafe1218624fc35.svg)
:::

which gives us the correct output without computing the whole matrix.

  --------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#trpo.xhtml_id1){.fn-backref}   See [Convex Optimization](http://stanford.edu/~boyd/cvxbook/){.reference .external}[ \[http://stanford.edu/\~boyd/cvxbook/\]]{.link-target} by Boyd and Vandenberghe, especially chapters 2 through 5.
  --------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::::::::::::

::: {#trpo.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#trpo.xhtml_id8){.toc-backref}

TRPO trains a stochastic policy in an on-policy way. This means that it
explores by sampling actions according to the latest version of its
stochastic policy. The amount of randomness in action selection depends
on both initial conditions and the training procedure. Over the course
of training, the policy typically becomes progressively less random, as
the update rule encourages it to exploit rewards that it has already
found. This may cause the policy to get trapped in local optima.
:::

:::: {#trpo.xhtml_pseudocode .section}
### [Pseudocode](#trpo.xhtml_id9){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{Trust Region Policy Optimization}
\\label{alg1} \\begin{algorithmic}\[1\] \\STATE Input: initial policy
parameters \$\\theta_0\$, initial value function parameters \$\\phi_0\$
\\STATE Hyperparameters: KL-divergence limit \$\\delta\$, backtracking
coefficient \$\\alpha\$, maximum number of backtracking steps \$K\$
\\FOR{\$k = 0,1,2,\...\$} \\STATE Collect set of trajectories
\${\\mathcal D}\_k = \\{\\tau_i\\}\$ by running policy \$\\pi_k =
\\pi(\\theta_k)\$ in the environment. \\STATE Compute rewards-to-go
\$\\hat{R}\_t\$. \\STATE Compute advantage estimates, \$\\hat{A}\_t\$
(using any method of advantage estimation) based on the current value
function \$V\_{\\phi_k}\$. \\STATE Estimate policy gradient as
\\begin{equation\*} \\hat{g}\_k = \\frac{1}{\|{\\mathcal D}\_k\|}
\\sum\_{\\tau \\in {\\mathcal D}\_k} \\sum\_{t=0}\^T \\left.
\\nabla\_{\\theta} \\log\\pi\_{\\theta}(a_t\|s_t)\\right\|\_{\\theta_k}
\\hat{A}\_t. \\end{equation\*} \\STATE Use the conjugate gradient
algorithm to compute \\begin{equation\*} \\hat{x}\_k \\approx
\\hat{H}\_k\^{-1} \\hat{g}\_k, \\end{equation\*} where \$\\hat{H}\_k\$
is the Hessian of the sample average KL-divergence. \\STATE Update the
policy by backtracking line search with \\begin{equation\*}
\\theta\_{k+1} = \\theta_k + \\alpha\^j \\sqrt{
\\frac{2\\delta}{\\hat{x}\_k\^T \\hat{H}\_k \\hat{x}\_k}} \\hat{x}\_k,
\\end{equation\*} where \$j \\in \\{0, 1, 2, \... K\\}\$ is the smallest
value which improves the sample loss and satisfies the sample
KL-divergence constraint. \\STATE Fit value function by regression on
mean-squared error: \\begin{equation\*} \\phi\_{k+1} = \\arg
\\min\_{\\phi} \\frac{1}{\|{\\mathcal D}\_k\| T} \\sum\_{\\tau \\in
{\\mathcal D}\_k} \\sum\_{t=0}\^T\\left( V\_{\\phi} (s_t) - \\hat{R}\_t
\\right)\^2, \\end{equation\*} typically via some gradient descent
algorithm. \\ENDFOR \\end{algorithmic}
\\end{algorithm}](_images/math/5808864ea60ebc3702704717d9f4c3773c90540d.svg)
:::
::::
::::::::::::::::::

::::: {#trpo.xhtml_documentation .section}
## [Documentation](#trpo.xhtml_id10){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

Spinning Up currently only has a Tensorflow implementation of TRPO.
:::

`spinup.`{.descclassname}`trpo_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=50*, *gamma=0.99*, *delta=0.01*, *vf_lr=0.001*, *train_v_iters=80*, *damping_coeff=0.1*, *cg_iters=10*, *backtrack_iters=10*, *backtrack_coeff=0.8*, *lam=0.97*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=10*, *algo=\'trpo\'*[)]{.sig-paren}

:   Trust Region Policy Optimization

    (with support for Natural Policy Gradient)

    +-------------+----------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment    |
    |             |   must satisfy the OpenAI Gym API.                                                     |
    |             |                                                                                        |
    |             | - **actor_critic** --                                                                  |
    |             |                                                                                        |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils           |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns the    |
    |             |   main outputs from the agent's Tensorflow computation graph:                          |
    |             |                                                                                        |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | Symbol                | Shape          | Description                             | |
    |             |   +=======================+================+=========================================+ |
    |             |   | [`pi`{.docutils       | (batch,        | ::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}      | act_dim)       | ::: line                                | |
    |             |   |                       |                | Samples actions from policy given       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | states.                                 | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | :::::                                   | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`logp`{.docutils     | (batch,)       | :::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | Gives log probability, according to     | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | the policy, of taking actions           | |
    |             |   |                       |                | [`a_ph`{.docutils .literal}]{.pre}      | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | in states [`x_ph`{.docutils             | |
    |             |   |                       |                | .literal}]{.pre}.                       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | ::::::                                  | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`logp_pi`{.docutils  | (batch,)       | :::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | Gives log probability, according to     | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | the policy, of the action sampled by    | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | [`pi`{.docutils .literal}]{.pre}.       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | ::::::                                  | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`info`{.docutils     | N/A            | ::::::::: {.first .last .line-block}    | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | A dict of any intermediate quantities   | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | (from calculating the policy or log     | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | probabilities) which are needed for     | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | analytically computing KL divergence.   | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | (eg sufficient statistics of the        | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | distributions)                          | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | :::::::::                               | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`info_phs`{.docutils | N/A            | ::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | A dict of placeholders for old values   | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | of the entries in [`info`{.docutils     | |
    |             |   |                       |                | .literal}]{.pre}.                       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | :::::                                   | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`d_kl`{.docutils     | ()             | ::::::::: {.first .last .line-block}    | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | A symbol for computing the mean KL      | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | divergence between the current policy   | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | ([`pi`{.docutils .literal}]{.pre}) and  | |
    |             |   |                       |                | the old policy (as                      | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | specified by the inputs to              | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | [`info_phs`{.docutils .literal}]{.pre}) | |
    |             |   |                       |                | over the batch of                       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | states given in [`x_ph`{.docutils       | |
    |             |   |                       |                | .literal}]{.pre}.                       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | :::::::::                               | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |   | [`v`{.docutils        | (batch,)       | :::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}      |                | ::: line                                | |
    |             |   |                       |                | Gives the value estimate for states     | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | in [`x_ph`{.docutils .literal}]{.pre}.  | |
    |             |   |                       |                | (Critical: make sure                    | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                |                                         | |
    |             |   |                       |                | ::: line                                | |
    |             |   |                       |                | to flatten this!)                       | |
    |             |   |                       |                | :::                                     | |
    |             |   |                       |                | ::::::                                  | |
    |             |   +-----------------------+----------------+-----------------------------------------+ |
    |             |                                                                                        |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function you   |
    |             |   provided to TRPO.                                                                    |
    |             |                                                                                        |
    |             | - **seed** (*int*) -- Seed for random number generators.                               |
    |             |                                                                                        |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs)   |
    |             |   for the agent and the environment in each epoch.                                     |
    |             |                                                                                        |
    |             | - **epochs** (*int*) -- Number of epochs of interaction (equivalent to number of       |
    |             |   policy updates) to perform.                                                          |
    |             |                                                                                        |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                    |
    |             |                                                                                        |
    |             | - **delta** (*float*) -- KL-divergence limit for TRPO / NPG update. (Should be small   |
    |             |   for stability. Values like 0.01, 0.05.)                                              |
    |             |                                                                                        |
    |             | - **vf_lr** (*float*) -- Learning rate for value function optimizer.                   |
    |             |                                                                                        |
    |             | - **train_v_iters** (*int*) -- Number of gradient descent steps to take on value       |
    |             |   function per epoch.                                                                  |
    |             |                                                                                        |
    |             | - **damping_coeff** (*float*) --                                                       |
    |             |                                                                                        |
    |             |   Artifact for numerical stability, should be smallish. Adjusts Hessian-vector product |
    |             |   calculation:                                                                         |
    |             |                                                                                        |
    |             |   ::: math                                                                             |
    |             |   ![Hv \\rightarrow (\\alpha I +                                                       |
    |             |   H)v](_images/math/404dea4d6af56dc327dd856bc640e2699e8135d8.svg)                      |
    |             |   :::                                                                                  |
    |             |                                                                                        |
    |             |   where ![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math}   |
    |             |   is the damping coefficient. Probably don't play with this hyperparameter.            |
    |             |                                                                                        |
    |             | - **cg_iters** (*int*) --                                                              |
    |             |                                                                                        |
    |             |   Number of iterations of conjugate gradient to perform. Increasing this will lead to  |
    |             |   a more accurate approximation to ![H\^{-1}                                           |
    |             |   g](_images/math/e8f8599a36583b493f5c5aaf05228d443ddf1f00.svg){.math}, and possibly   |
    |             |   slightly-improved performance, but at the cost of slowing things down.               |
    |             |                                                                                        |
    |             |   Also probably don't play with this hyperparameter.                                   |
    |             |                                                                                        |
    |             | - **backtrack_iters** (*int*) -- Maximum number of steps allowed in the backtracking   |
    |             |   line search. Since the line search usually doesn't backtrack, and usually only steps |
    |             |   back once when it does, this hyperparameter doesn't often matter.                    |
    |             |                                                                                        |
    |             | - **backtrack_coeff** (*float*) -- How far back to step during backtracking line       |
    |             |   search. (Always between 0 and 1, usually above 0.5.)                                 |
    |             |                                                                                        |
    |             | - **lam** (*float*) -- Lambda for GAE-Lambda. (Always between 0 and 1, close to 1.)    |
    |             |                                                                                        |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.          |
    |             |                                                                                        |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                          |
    |             |                                                                                        |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the      |
    |             |   current policy and value function.                                                   |
    |             |                                                                                        |
    |             | - **algo** -- Either 'trpo' or 'npg': this code supports both, since they are almost   |
    |             |   the same.                                                                            |
    +-------------+----------------------------------------------------------------------------------------+

::: {#trpo.xhtml_saved-model-contents .section}
### [Saved Model Contents](#trpo.xhtml_id11){.toc-backref}

The computation graph saved by the logger includes:

  ----------------------------------------------------------------------------------
  Key                Value
  ------------------ ---------------------------------------------------------------
  [`x`{.docutils     Tensorflow placeholder for state input.
  .literal}]{.pre}   

  [`pi`{.docutils    Samples an action from the agent, conditioned on states in
  .literal}]{.pre}   [`x`{.docutils .literal}]{.pre}.

  [`v`{.docutils     Gives value estimate for states in [`x`{.docutils
  .literal}]{.pre}   .literal}]{.pre}.
  ----------------------------------------------------------------------------------

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.
:::
:::::

:::::: {#trpo.xhtml_references .section}
## [References](#trpo.xhtml_id12){.toc-backref}

::: {#trpo.xhtml_relevant-papers .section}
### [Relevant Papers](#trpo.xhtml_id13){.toc-backref}

- [Trust Region Policy
  Optimization](https://arxiv.org/abs/1502.05477){.reference .external}[
  \[https://arxiv.org/abs/1502.05477\]]{.link-target}, Schulman et al.
  2015
- [High Dimensional Continuous Control Using Generalized Advantage
  Estimation](https://arxiv.org/abs/1506.02438){.reference .external}[
  \[https://arxiv.org/abs/1506.02438\]]{.link-target}, Schulman et al.
  2016
- [Approximately Optimal Approximate Reinforcement
  Learning](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf){.reference
  .external}[
  \[https://people.eecs.berkeley.edu/\~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf\]]{.link-target},
  Kakade and Langford 2002
:::

::: {#trpo.xhtml_why-these-papers .section}
### [Why These Papers?](#trpo.xhtml_id14){.toc-backref}

Schulman 2015 is included because it is the original paper describing
TRPO. Schulman 2016 is included because our implementation of TRPO makes
use of Generalized Advantage Estimation for computing the policy
gradient. Kakade and Langford 2002 is included because it contains
theoretical results which motivate and deeply connect to the theoretical
foundations of TRPO.
:::

::: {#trpo.xhtml_other-public-implementations .section}
### [Other Public Implementations](#trpo.xhtml_id15){.toc-backref}

- [Baselines](https://github.com/openai/baselines/tree/master/baselines/trpo_mpi){.reference
  .external}[
  \[https://github.com/openai/baselines/tree/master/baselines/trpo_mpi\]]{.link-target}
- [ModularRL](https://github.com/joschu/modular_rl/blob/master/modular_rl/trpo.py){.reference
  .external}[
  \[https://github.com/joschu/modular_rl/blob/master/modular_rl/trpo.py\]]{.link-target}
- [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/trpo.py){.reference
  .external}[
  \[https://github.com/rll/rllab/blob/master/rllab/algos/trpo.py\]]{.link-target}
:::
::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

[]{#ppo.xhtml}

:::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::: {#ppo.xhtml_proximal-policy-optimization .section}
# [Proximal Policy Optimization](#ppo.xhtml_id3){.toc-backref}

::: {#ppo.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Proximal Policy
  Optimization](#ppo.xhtml_proximal-policy-optimization){#ppo.xhtml_id3
  .reference .internal}
  - [Background](#ppo.xhtml_background){#ppo.xhtml_id4 .reference
    .internal}
    - [Quick Facts](#ppo.xhtml_quick-facts){#ppo.xhtml_id5 .reference
      .internal}
    - [Key Equations](#ppo.xhtml_key-equations){#ppo.xhtml_id6
      .reference .internal}
    - [Exploration vs.
      Exploitation](#ppo.xhtml_exploration-vs-exploitation){#ppo.xhtml_id7
      .reference .internal}
    - [Pseudocode](#ppo.xhtml_pseudocode){#ppo.xhtml_id8 .reference
      .internal}
  - [Documentation](#ppo.xhtml_documentation){#ppo.xhtml_id9 .reference
    .internal}
    - [Documentation: PyTorch
      Version](#ppo.xhtml_documentation-pytorch-version){#ppo.xhtml_id10
      .reference .internal}
    - [Saved Model Contents: PyTorch
      Version](#ppo.xhtml_saved-model-contents-pytorch-version){#ppo.xhtml_id11
      .reference .internal}
    - [Documentation: Tensorflow
      Version](#ppo.xhtml_documentation-tensorflow-version){#ppo.xhtml_id12
      .reference .internal}
    - [Saved Model Contents: Tensorflow
      Version](#ppo.xhtml_saved-model-contents-tensorflow-version){#ppo.xhtml_id13
      .reference .internal}
  - [References](#ppo.xhtml_references){#ppo.xhtml_id14 .reference
    .internal}
    - [Relevant Papers](#ppo.xhtml_relevant-papers){#ppo.xhtml_id15
      .reference .internal}
    - [Why These Papers?](#ppo.xhtml_why-these-papers){#ppo.xhtml_id16
      .reference .internal}
    - [Other Public
      Implementations](#ppo.xhtml_other-public-implementations){#ppo.xhtml_id17
      .reference .internal}
:::

::::::::::::::: {#ppo.xhtml_background .section}
## [Background](#ppo.xhtml_id4){.toc-backref}

(Previously: [Background for TRPO](trpo.html_background){.reference
.external})

PPO is motivated by the same question as TRPO: how can we take the
biggest possible improvement step on a policy using the data we
currently have, without stepping so far that we accidentally cause
performance collapse? Where TRPO tries to solve this problem with a
complex second-order method, PPO is a family of first-order methods that
use a few other tricks to keep new policies close to old. PPO methods
are significantly simpler to implement, and empirically seem to perform
at least as well as TRPO.

There are two primary variants of PPO: PPO-Penalty and PPO-Clip.

**PPO-Penalty** approximately solves a KL-constrained update like TRPO,
but penalizes the KL-divergence in the objective function instead of
making it a hard constraint, and automatically adjusts the penalty
coefficient over the course of training so that it's scaled
appropriately.

**PPO-Clip** doesn't have a KL-divergence term in the objective and
doesn't have a constraint at all. Instead relies on specialized clipping
in the objective function to remove incentives for the new policy to get
far from the old policy.

Here, we'll focus only on PPO-Clip (the primary variant used at OpenAI).

::: {#ppo.xhtml_quick-facts .section}
### [Quick Facts](#ppo.xhtml_id5){.toc-backref}

- PPO is an on-policy algorithm.
- PPO can be used for environments with either discrete or continuous
  action spaces.
- The Spinning Up implementation of PPO supports parallelization with
  MPI.
:::

:::::::::: {#ppo.xhtml_key-equations .section}
### [Key Equations](#ppo.xhtml_id6){.toc-backref}

PPO-clip updates policies via

::: math
![\\theta\_{k+1} = \\arg \\max\_{\\theta} \\underset{s,a \\sim
\\pi\_{\\theta_k}}{{\\mathrm E}}\\left\[ L(s,a,\\theta_k,
\\theta)\\right\],](_images/math/96a52e61318720522e040e433c938ee829d54506.svg)
:::

typically taking multiple steps of (usually minibatch) SGD to maximize
the objective. Here
![L](_images/math/3ffe1da701d78dd473975ebd2f875807611f7713.svg){.math}
is given by

::: math
![L(s,a,\\theta_k,\\theta) = \\min\\left(
\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)}
A\^{\\pi\_{\\theta_k}}(s,a), \\;\\;
\\text{clip}\\left(\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)},
1 - \\epsilon, 1+\\epsilon \\right) A\^{\\pi\_{\\theta_k}}(s,a)
\\right),](_images/math/99621d5bcaccd056d6ca3aeb48a27bf8cc0e640c.svg)
:::

in which
![\\epsilon](_images/math/c589a82739d7aa277bcf45e632d930d1c119b7ef.svg){.math}
is a (small) hyperparameter which roughly says how far away the new
policy is allowed to go from the old.

This is a pretty complex expression, and it's hard to tell at first
glance what it's doing, or how it helps keep the new policy close to the
old policy. As it turns out, there's a considerably simplified version
[\[1\]](#ppo.xhtml_id2){#ppo.xhtml_id1 .footnote-reference} of this
objective which is a bit easier to grapple with (and is also the version
we implement in our code):

::: math
![L(s,a,\\theta_k,\\theta) = \\min\\left(
\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)}
A\^{\\pi\_{\\theta_k}}(s,a), \\;\\; g(\\epsilon,
A\^{\\pi\_{\\theta_k}}(s,a))
\\right),](_images/math/dd41a29292af3bc58c0c76bc7dba82a7355bf929.svg)
:::

where

::: math
![g(\\epsilon, A) = \\left\\{ \\begin{array}{ll} (1 + \\epsilon) A & A
\\geq 0 \\\\ (1 - \\epsilon) A & A \< 0. \\end{array}
\\right.](_images/math/39f524858866b80e627840ba77a54360e3bac55e.svg)
:::

To figure out what intuition to take away from this, let's look at a
single state-action pair
![(s,a)](_images/math/4a1b4e2fc586f984a8edafbcae068c3f3c992402.svg){.math},
and think of cases.

**Advantage is positive**: Suppose the advantage for that state-action
pair is positive, in which case its contribution to the objective
reduces to

::: math
![L(s,a,\\theta_k,\\theta) = \\min\\left(
\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)}, (1 + \\epsilon)
\\right)
A\^{\\pi\_{\\theta_k}}(s,a).](_images/math/b4e46e01172264315e9e5d6c8bd2ced884d6602c.svg)
:::

Because the advantage is positive, the objective will increase if the
action becomes more likely---that is, if
![\\pi\_{\\theta}(a\|s)](_images/math/400068784a9d13ffe96c61f29b4ab26ad5557376.svg){.math}
increases. But the min in this term puts a limit to how *much* the
objective can increase. Once ![\\pi\_{\\theta}(a\|s) \> (1+\\epsilon)
\\pi\_{\\theta_k}(a\|s)](_images/math/cee08da41b29ab9355f2e4dac94de335c6eff03f.svg){.math},
the min kicks in and this term hits a ceiling of ![(1+\\epsilon)
A\^{\\pi\_{\\theta_k}}(s,a)](_images/math/08d4d3bab53ce2aef0a6fd4d8e0e9f5cd0e4f7ca.svg){.math}.
Thus: *the new policy does not benefit by going far away from the old
policy*.

**Advantage is negative**: Suppose the advantage for that state-action
pair is negative, in which case its contribution to the objective
reduces to

::: math
![L(s,a,\\theta_k,\\theta) = \\max\\left(
\\frac{\\pi\_{\\theta}(a\|s)}{\\pi\_{\\theta_k}(a\|s)}, (1 - \\epsilon)
\\right)
A\^{\\pi\_{\\theta_k}}(s,a).](_images/math/b8b23f5e4578125c2d8fbfc66442629ff7a85fb5.svg)
:::

Because the advantage is negative, the objective will increase if the
action becomes less likely---that is, if
![\\pi\_{\\theta}(a\|s)](_images/math/400068784a9d13ffe96c61f29b4ab26ad5557376.svg){.math}
decreases. But the max in this term puts a limit to how *much* the
objective can increase. Once ![\\pi\_{\\theta}(a\|s) \< (1-\\epsilon)
\\pi\_{\\theta_k}(a\|s)](_images/math/82d6b288e893443689bf88b41b1f0f532c54f2f3.svg){.math},
the max kicks in and this term hits a ceiling of ![(1-\\epsilon)
A\^{\\pi\_{\\theta_k}}(s,a)](_images/math/0aea7de5d8df7541d515b563b9c7bb0191e28b32.svg){.math}.
Thus, again: *the new policy does not benefit by going far away from the
old policy*.

What we have seen so far is that clipping serves as a regularizer by
removing incentives for the policy to change dramatically, and the
hyperparameter
![\\epsilon](_images/math/c589a82739d7aa277bcf45e632d930d1c119b7ef.svg){.math}
corresponds to how far away the new policy can go from the old while
still profiting the objective.

::: {.admonition-you-should-know .admonition}
You Should Know

While this kind of clipping goes a long way towards ensuring reasonable
policy updates, it is still possible to end up with a new policy which
is too far from the old policy, and there are a bunch of tricks used by
different PPO implementations to stave this off. In our implementation
here, we use a particularly simple method: early stopping. If the mean
KL-divergence of the new policy from the old grows beyond a threshold,
we stop taking gradient steps.

When you feel comfortable with the basic math and implementation
details, it's worth checking out other implementations to see how they
handle this issue!
:::

  -------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#ppo.xhtml_id1){.fn-backref}   See [this note](https://drive.google.com/file/d/1PDzn9RPvaXjJFZkGeapMHbHGiWWW20Ey/view?usp=sharing){.reference .external}[ \[https://drive.google.com/file/d/1PDzn9RPvaXjJFZkGeapMHbHGiWWW20Ey/view?usp=sharing\]]{.link-target} for a derivation of the simplified form of the PPO-Clip objective.
  -------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
::::::::::

::: {#ppo.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#ppo.xhtml_id7){.toc-backref}

PPO trains a stochastic policy in an on-policy way. This means that it
explores by sampling actions according to the latest version of its
stochastic policy. The amount of randomness in action selection depends
on both initial conditions and the training procedure. Over the course
of training, the policy typically becomes progressively less random, as
the update rule encourages it to exploit rewards that it has already
found. This may cause the policy to get trapped in local optima.
:::

:::: {#ppo.xhtml_pseudocode .section}
### [Pseudocode](#ppo.xhtml_id8){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{PPO-Clip} \\label{alg1}
\\begin{algorithmic}\[1\] \\STATE Input: initial policy parameters
\$\\theta_0\$, initial value function parameters \$\\phi_0\$ \\FOR{\$k =
0,1,2,\...\$} \\STATE Collect set of trajectories \${\\mathcal D}\_k =
\\{\\tau_i\\}\$ by running policy \$\\pi_k = \\pi(\\theta_k)\$ in the
environment. \\STATE Compute rewards-to-go \$\\hat{R}\_t\$. \\STATE
Compute advantage estimates, \$\\hat{A}\_t\$ (using any method of
advantage estimation) based on the current value function
\$V\_{\\phi_k}\$. \\STATE Update the policy by maximizing the PPO-Clip
objective: \\begin{equation\*} \\theta\_{k+1} = \\arg \\max\_{\\theta}
\\frac{1}{\|{\\mathcal D}\_k\| T} \\sum\_{\\tau \\in {\\mathcal D}\_k}
\\sum\_{t=0}\^T \\min\\left(
\\frac{\\pi\_{\\theta}(a_t\|s_t)}{\\pi\_{\\theta_k}(a_t\|s_t)}
A\^{\\pi\_{\\theta_k}}(s_t,a_t), \\;\\; g(\\epsilon,
A\^{\\pi\_{\\theta_k}}(s_t,a_t)) \\right), \\end{equation\*} typically
via stochastic gradient ascent with Adam. \\STATE Fit value function by
regression on mean-squared error: \\begin{equation\*} \\phi\_{k+1} =
\\arg \\min\_{\\phi} \\frac{1}{\|{\\mathcal D}\_k\| T} \\sum\_{\\tau
\\in {\\mathcal D}\_k} \\sum\_{t=0}\^T\\left( V\_{\\phi} (s_t) -
\\hat{R}\_t \\right)\^2, \\end{equation\*} typically via some gradient
descent algorithm. \\ENDFOR \\end{algorithmic}
\\end{algorithm}](_images/math/e62a8971472597f4b014c2da064f636ffe365ba3.svg)
:::
::::
:::::::::::::::

:::::::::: {#ppo.xhtml_documentation .section}
## [Documentation](#ppo.xhtml_id9){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow
implementations of PPO in Spinning Up. They have nearly identical
function calls and docstrings, except for details relating to model
construction. However, we include both full docstrings for completeness.
:::

::: {#ppo.xhtml_documentation-pytorch-version .section}
### [Documentation: PyTorch Version](#ppo.xhtml_id10){.toc-backref}

`spinup.`{.descclassname}`ppo_pytorch`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<MagicMock spec=\'str\' id=\'140679791090264\'\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=50*, *gamma=0.99*, *clip_ratio=0.2*, *pi_lr=0.0003*, *vf_lr=0.001*, *train_pi_iters=80*, *train_v_iters=80*, *lam=0.97*, *max_ep_len=1000*, *target_kl=0.01*, *logger_kwargs={}*, *save_freq=10*[)]{.sig-paren}

:   Proximal Policy Optimization (by clipping),

    with early stopping based on approximate KL

    +-------------+--------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment  |
    |             |   must satisfy the OpenAI Gym API.                                                   |
    |             |                                                                                      |
    |             | - **actor_critic** --                                                                |
    |             |                                                                                      |
    |             |   The constructor method for a PyTorch Module with a [`step`{.docutils               |
    |             |   .literal}]{.pre} method, an [`act`{.docutils .literal}]{.pre} method, a            |
    |             |   [`pi`{.docutils .literal}]{.pre} module, and a [`v`{.docutils .literal}]{.pre}     |
    |             |   module. The [`step`{.docutils .literal}]{.pre} method should accept a batch of     |
    |             |   observations and return:                                                           |
    |             |                                                                                      |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | Symbol              | Shape           | Description                            | |
    |             |   +=====================+=================+========================================+ |
    |             |   | [`a`{.docutils      | (batch,         | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    | act_dim)        | ::: line                               | |
    |             |   |                     |                 | Numpy array of actions for each        | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | observation.                           | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | [`v`{.docutils      | (batch,)        | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    |                 | ::: line                               | |
    |             |   |                     |                 | Numpy array of value estimates         | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | for the provided observations.         | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |   | [`logp_a`{.docutils | (batch,)        | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}    |                 | ::: line                               | |
    |             |   |                     |                 | Numpy array of log probs for the       | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 |                                        | |
    |             |   |                     |                 | ::: line                               | |
    |             |   |                     |                 | actions in [`a`{.docutils              | |
    |             |   |                     |                 | .literal}]{.pre}.                      | |
    |             |   |                     |                 | :::                                    | |
    |             |   |                     |                 | :::::                                  | |
    |             |   +---------------------+-----------------+----------------------------------------+ |
    |             |                                                                                      |
    |             |   The [`act`{.docutils .literal}]{.pre} method behaves the same as [`step`{.docutils |
    |             |   .literal}]{.pre} but only returns [`a`{.docutils .literal}]{.pre}.                 |
    |             |                                                                                      |
    |             |   The [`pi`{.docutils .literal}]{.pre} module's forward call should accept a batch   |
    |             |   of observations and optionally a batch of actions, and return:                     |
    |             |                                                                                      |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |   | Symbol              | Shape         | Description                              | |
    |             |   +=====================+===============+==========================================+ |
    |             |   | [`pi`{.docutils     | N/A           | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}    |               | ::: line                                 | |
    |             |   |                     |               | Torch Distribution object, containing    | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | a batch of distributions describing      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the policy for the provided              | |
    |             |   |                     |               | observations.                            | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               | ::::::                                   | |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |   | [`logp_a`{.docutils | (batch,)      | ::::::::: {.first .last .line-block}     | |
    |             |   | .literal}]{.pre}    |               | ::: line                                 | |
    |             |   |                     |               | Optional (only returned if batch of      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | actions is given). Tensor containing     | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the log probability, according to        | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | the policy, of the provided actions.     | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | If actions not given, will contain       | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               |                                          | |
    |             |   |                     |               | ::: line                                 | |
    |             |   |                     |               | [`None`{.docutils .literal}]{.pre}.      | |
    |             |   |                     |               | :::                                      | |
    |             |   |                     |               | :::::::::                                | |
    |             |   +---------------------+---------------+------------------------------------------+ |
    |             |                                                                                      |
    |             |   The [`v`{.docutils .literal}]{.pre} module's forward call should accept a batch of |
    |             |   observations and return:                                                           |
    |             |                                                                                      |
    |             |   +------------------+---------------+------------------------------------------+    |
    |             |   | Symbol           | Shape         | Description                              |    |
    |             |   +==================+===============+==========================================+    |
    |             |   | [`v`{.docutils   | (batch,)      | :::::: {.first .last .line-block}        |    |
    |             |   | .literal}]{.pre} |               | ::: line                                 |    |
    |             |   |                  |               | Tensor containing the value estimates    |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               |                                          |    |
    |             |   |                  |               | ::: line                                 |    |
    |             |   |                  |               | for the provided observations.           |    |
    |             |   |                  |               | (Critical:                               |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               |                                          |    |
    |             |   |                  |               | ::: line                                 |    |
    |             |   |                  |               | make sure to flatten this!)              |    |
    |             |   |                  |               | :::                                      |    |
    |             |   |                  |               | ::::::                                   |    |
    |             |   +------------------+---------------+------------------------------------------+    |
    |             |                                                                                      |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the ActorCritic object you    |
    |             |   provided to PPO.                                                                   |
    |             |                                                                                      |
    |             | - **seed** (*int*) -- Seed for random number generators.                             |
    |             |                                                                                      |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs) |
    |             |   for the agent and the environment in each epoch.                                   |
    |             |                                                                                      |
    |             | - **epochs** (*int*) -- Number of epochs of interaction (equivalent to number of     |
    |             |   policy updates) to perform.                                                        |
    |             |                                                                                      |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                  |
    |             |                                                                                      |
    |             | - **clip_ratio** (*float*) -- Hyperparameter for clipping in the policy objective.   |
    |             |   Roughly: how far can the new policy go from the old policy while still profiting   |
    |             |   (improving the objective function)? The new policy can still go farther than the   |
    |             |   clip_ratio says, but it doesn't help on the objective anymore. (Usually small, 0.1 |
    |             |   to 0.3.) Typically denoted by                                                      |
    |             |   ![\\epsilon](_images/math/c589a82739d7aa277bcf45e632d930d1c119b7ef.svg){.math}.    |
    |             |                                                                                      |
    |             | - **pi_lr** (*float*) -- Learning rate for policy optimizer.                         |
    |             |                                                                                      |
    |             | - **vf_lr** (*float*) -- Learning rate for value function optimizer.                 |
    |             |                                                                                      |
    |             | - **train_pi_iters** (*int*) -- Maximum number of gradient descent steps to take on  |
    |             |   policy loss per epoch. (Early stopping may cause optimizer to take fewer than      |
    |             |   this.)                                                                             |
    |             |                                                                                      |
    |             | - **train_v_iters** (*int*) -- Number of gradient descent steps to take on value     |
    |             |   function per epoch.                                                                |
    |             |                                                                                      |
    |             | - **lam** (*float*) -- Lambda for GAE-Lambda. (Always between 0 and 1, close to 1.)  |
    |             |                                                                                      |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.        |
    |             |                                                                                      |
    |             | - **target_kl** (*float*) -- Roughly what KL divergence we think is appropriate      |
    |             |   between new and old policies after an update. This will get used for early         |
    |             |   stopping. (Usually small, 0.01 or 0.05.)                                           |
    |             |                                                                                      |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                        |
    |             |                                                                                      |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the    |
    |             |   current policy and value function.                                                 |
    +-------------+--------------------------------------------------------------------------------------+
:::

::::: {#ppo.xhtml_saved-model-contents-pytorch-version .section}
### [Saved Model Contents: PyTorch Version](#ppo.xhtml_id11){.toc-backref}

The PyTorch saved model can be loaded with [`ac`{.docutils
.literal}]{.pre}` `{.docutils .literal}[`=`{.docutils
.literal}]{.pre}` `{.docutils
.literal}[`torch.load('path/to/model.pt')`{.docutils .literal}]{.pre},
yielding an actor-critic object ([`ac`{.docutils .literal}]{.pre}) that
has the properties described in the docstring for
[`ppo_pytorch`{.docutils .literal}]{.pre}.

You can get actions from this model with

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::

::: {#ppo.xhtml_documentation-tensorflow-version .section}
### [Documentation: Tensorflow Version](#ppo.xhtml_id12){.toc-backref}

`spinup.`{.descclassname}`ppo_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=50*, *gamma=0.99*, *clip_ratio=0.2*, *pi_lr=0.0003*, *vf_lr=0.001*, *train_pi_iters=80*, *train_v_iters=80*, *lam=0.97*, *max_ep_len=1000*, *target_kl=0.01*, *logger_kwargs={}*, *save_freq=10*[)]{.sig-paren}

:   Proximal Policy Optimization (by clipping),

    with early stopping based on approximate KL

    +-------------+----------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment    |
    |             |   must satisfy the OpenAI Gym API.                                                     |
    |             |                                                                                        |
    |             | - **actor_critic** --                                                                  |
    |             |                                                                                        |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils           |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns the    |
    |             |   main outputs from the agent's Tensorflow computation graph:                          |
    |             |                                                                                        |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | Symbol               | Shape          | Description                              | |
    |             |   +======================+================+==========================================+ |
    |             |   | [`pi`{.docutils      | (batch,        | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre}     | act_dim)       | ::: line                                 | |
    |             |   |                      |                | Samples actions from policy given        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | states.                                  | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | :::::                                    | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`logp`{.docutils    | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives log probability, according to      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | the policy, of taking actions            | |
    |             |   |                      |                | [`a_ph`{.docutils .literal}]{.pre}       | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | in states [`x_ph`{.docutils              | |
    |             |   |                      |                | .literal}]{.pre}.                        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`logp_pi`{.docutils | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives log probability, according to      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | the policy, of the action sampled by     | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | [`pi`{.docutils .literal}]{.pre}.        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |   | [`v`{.docutils       | (batch,)       | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |                | ::: line                                 | |
    |             |   |                      |                | Gives the value estimate for states      | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | in [`x_ph`{.docutils .literal}]{.pre}.   | |
    |             |   |                      |                | (Critical: make sure                     | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                |                                          | |
    |             |   |                      |                | ::: line                                 | |
    |             |   |                      |                | to flatten this!)                        | |
    |             |   |                      |                | :::                                      | |
    |             |   |                      |                | ::::::                                   | |
    |             |   +----------------------+----------------+------------------------------------------+ |
    |             |                                                                                        |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function you   |
    |             |   provided to PPO.                                                                     |
    |             |                                                                                        |
    |             | - **seed** (*int*) -- Seed for random number generators.                               |
    |             |                                                                                        |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs)   |
    |             |   for the agent and the environment in each epoch.                                     |
    |             |                                                                                        |
    |             | - **epochs** (*int*) -- Number of epochs of interaction (equivalent to number of       |
    |             |   policy updates) to perform.                                                          |
    |             |                                                                                        |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                    |
    |             |                                                                                        |
    |             | - **clip_ratio** (*float*) -- Hyperparameter for clipping in the policy objective.     |
    |             |   Roughly: how far can the new policy go from the old policy while still profiting     |
    |             |   (improving the objective function)? The new policy can still go farther than the     |
    |             |   clip_ratio says, but it doesn't help on the objective anymore. (Usually small, 0.1   |
    |             |   to 0.3.) Typically denoted by                                                        |
    |             |   ![\\epsilon](_images/math/c589a82739d7aa277bcf45e632d930d1c119b7ef.svg){.math}.      |
    |             |                                                                                        |
    |             | - **pi_lr** (*float*) -- Learning rate for policy optimizer.                           |
    |             |                                                                                        |
    |             | - **vf_lr** (*float*) -- Learning rate for value function optimizer.                   |
    |             |                                                                                        |
    |             | - **train_pi_iters** (*int*) -- Maximum number of gradient descent steps to take on    |
    |             |   policy loss per epoch. (Early stopping may cause optimizer to take fewer than this.) |
    |             |                                                                                        |
    |             | - **train_v_iters** (*int*) -- Number of gradient descent steps to take on value       |
    |             |   function per epoch.                                                                  |
    |             |                                                                                        |
    |             | - **lam** (*float*) -- Lambda for GAE-Lambda. (Always between 0 and 1, close to 1.)    |
    |             |                                                                                        |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.          |
    |             |                                                                                        |
    |             | - **target_kl** (*float*) -- Roughly what KL divergence we think is appropriate        |
    |             |   between new and old policies after an update. This will get used for early stopping. |
    |             |   (Usually small, 0.01 or 0.05.)                                                       |
    |             |                                                                                        |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                          |
    |             |                                                                                        |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the      |
    |             |   current policy and value function.                                                   |
    +-------------+----------------------------------------------------------------------------------------+
:::

::: {#ppo.xhtml_saved-model-contents-tensorflow-version .section}
### [Saved Model Contents: Tensorflow Version](#ppo.xhtml_id13){.toc-backref}

The computation graph saved by the logger includes:

  ----------------------------------------------------------------------------------
  Key                Value
  ------------------ ---------------------------------------------------------------
  [`x`{.docutils     Tensorflow placeholder for state input.
  .literal}]{.pre}   

  [`pi`{.docutils    Samples an action from the agent, conditioned on states in
  .literal}]{.pre}   [`x`{.docutils .literal}]{.pre}.

  [`v`{.docutils     Gives value estimate for states in [`x`{.docutils
  .literal}]{.pre}   .literal}]{.pre}.
  ----------------------------------------------------------------------------------

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.
:::
::::::::::

:::::: {#ppo.xhtml_references .section}
## [References](#ppo.xhtml_id14){.toc-backref}

::: {#ppo.xhtml_relevant-papers .section}
### [Relevant Papers](#ppo.xhtml_id15){.toc-backref}

- [Proximal Policy Optimization
  Algorithms](https://arxiv.org/abs/1707.06347){.reference .external}[
  \[https://arxiv.org/abs/1707.06347\]]{.link-target}, Schulman et al.
  2017
- [High Dimensional Continuous Control Using Generalized Advantage
  Estimation](https://arxiv.org/abs/1506.02438){.reference .external}[
  \[https://arxiv.org/abs/1506.02438\]]{.link-target}, Schulman et al.
  2016
- [Emergence of Locomotion Behaviours in Rich
  Environments](https://arxiv.org/abs/1707.02286){.reference .external}[
  \[https://arxiv.org/abs/1707.02286\]]{.link-target}, Heess et al. 2017
:::

::: {#ppo.xhtml_why-these-papers .section}
### [Why These Papers?](#ppo.xhtml_id16){.toc-backref}

Schulman 2017 is included because it is the original paper describing
PPO. Schulman 2016 is included because our implementation of PPO makes
use of Generalized Advantage Estimation for computing the policy
gradient. Heess 2017 is included because it presents a large-scale
empirical analysis of behaviors learned by PPO agents in complex
environments (although it uses PPO-penalty instead of PPO-clip).
:::

::: {#ppo.xhtml_other-public-implementations .section}
### [Other Public Implementations](#ppo.xhtml_id17){.toc-backref}

- [Baselines](https://github.com/openai/baselines/tree/master/baselines/ppo2){.reference
  .external}[
  \[https://github.com/openai/baselines/tree/master/baselines/ppo2\]]{.link-target}
- [ModularRL](https://github.com/joschu/modular_rl/blob/master/modular_rl/ppo.py){.reference
  .external}[
  \[https://github.com/joschu/modular_rl/blob/master/modular_rl/ppo.py\]]{.link-target}
  (Caution: this implements PPO-penalty instead of PPO-clip.)
- [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/ppo.py){.reference
  .external}[
  \[https://github.com/rll/rllab/blob/master/rllab/algos/ppo.py\]]{.link-target}
  (Caution: this implements PPO-penalty instead of PPO-clip.)
- [rllib
  (Ray)](https://github.com/ray-project/ray/tree/master/python/ray/rllib/agents/ppo){.reference
  .external}[
  \[https://github.com/ray-project/ray/tree/master/python/ray/rllib/agents/ppo\]]{.link-target}
:::
::::::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

[]{#ddpg.xhtml}

:::::::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::::::::: {#ddpg.xhtml_deep-deterministic-policy-gradient .section}
# [Deep Deterministic Policy Gradient](#ddpg.xhtml_id1){.toc-backref}

::: {#ddpg.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Deep Deterministic Policy
  Gradient](#ddpg.xhtml_deep-deterministic-policy-gradient){#ddpg.xhtml_id1
  .reference .internal}
  - [Background](#ddpg.xhtml_background){#ddpg.xhtml_id2 .reference
    .internal}
    - [Quick Facts](#ddpg.xhtml_quick-facts){#ddpg.xhtml_id3 .reference
      .internal}
    - [Key Equations](#ddpg.xhtml_key-equations){#ddpg.xhtml_id4
      .reference .internal}
      - [The Q-Learning Side of
        DDPG](#ddpg.xhtml_the-q-learning-side-of-ddpg){#ddpg.xhtml_id5
        .reference .internal}
      - [The Policy Learning Side of
        DDPG](#ddpg.xhtml_the-policy-learning-side-of-ddpg){#ddpg.xhtml_id6
        .reference .internal}
    - [Exploration vs.
      Exploitation](#ddpg.xhtml_exploration-vs-exploitation){#ddpg.xhtml_id7
      .reference .internal}
    - [Pseudocode](#ddpg.xhtml_pseudocode){#ddpg.xhtml_id8 .reference
      .internal}
  - [Documentation](#ddpg.xhtml_documentation){#ddpg.xhtml_id9
    .reference .internal}
    - [Documentation: PyTorch
      Version](#ddpg.xhtml_documentation-pytorch-version){#ddpg.xhtml_id10
      .reference .internal}
    - [Saved Model Contents: PyTorch
      Version](#ddpg.xhtml_saved-model-contents-pytorch-version){#ddpg.xhtml_id11
      .reference .internal}
    - [Documentation: Tensorflow
      Version](#ddpg.xhtml_documentation-tensorflow-version){#ddpg.xhtml_id12
      .reference .internal}
    - [Saved Model Contents: Tensorflow
      Version](#ddpg.xhtml_saved-model-contents-tensorflow-version){#ddpg.xhtml_id13
      .reference .internal}
  - [References](#ddpg.xhtml_references){#ddpg.xhtml_id14 .reference
    .internal}
    - [Relevant Papers](#ddpg.xhtml_relevant-papers){#ddpg.xhtml_id15
      .reference .internal}
    - [Why These Papers?](#ddpg.xhtml_why-these-papers){#ddpg.xhtml_id16
      .reference .internal}
    - [Other Public
      Implementations](#ddpg.xhtml_other-public-implementations){#ddpg.xhtml_id17
      .reference .internal}
:::

::::::::::::::::::: {#ddpg.xhtml_background .section}
## [Background](#ddpg.xhtml_id2){.toc-backref}

(Previously: [Introduction to RL Part 1: The Optimal Q-Function and the
Optimal
Action](rl_intro.html_the-optimal-q-function-and-the-optimal-action){.reference
.external})

Deep Deterministic Policy Gradient (DDPG) is an algorithm which
concurrently learns a Q-function and a policy. It uses off-policy data
and the Bellman equation to learn the Q-function, and uses the
Q-function to learn the policy.

This approach is closely connected to Q-learning, and is motivated the
same way: if you know the optimal action-value function
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math},
then in any given state, the optimal action
![a\^\*(s)](_images/math/baf715aa6a295b7b7d85e1e1123552c5ae705756.svg){.math}
can be found by solving

::: math
![a\^\*(s) = \\arg \\max_a
Q\^\*(s,a).](_images/math/82f049ec26e21eb2bfc6af21e3465707814f4838.svg)
:::

DDPG interleaves learning an approximator to
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}
with learning an approximator to
![a\^\*(s)](_images/math/baf715aa6a295b7b7d85e1e1123552c5ae705756.svg){.math},
and it does so in a way which is specifically adapted for environments
with continuous action spaces. But what does it mean that DDPG is
adapted *specifically* for environments with continuous action spaces?
It relates to how we compute the max over actions in ![\\max_a
Q\^\*(s,a)](_images/math/1f3098d0653722949f8ceeefc8b5c951d99c8274.svg){.math}.

When there are a finite number of discrete actions, the max poses no
problem, because we can just compute the Q-values for each action
separately and directly compare them. (This also immediately gives us
the action which maximizes the Q-value.) But when the action space is
continuous, we can't exhaustively evaluate the space, and solving the
optimization problem is highly non-trivial. Using a normal optimization
algorithm would make calculating ![\\max_a
Q\^\*(s,a)](_images/math/1f3098d0653722949f8ceeefc8b5c951d99c8274.svg){.math}
a painfully expensive subroutine. And since it would need to be run
every time the agent wants to take an action in the environment, this is
unacceptable.

Because the action space is continuous, the function
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}
is presumed to be differentiable with respect to the action argument.
This allows us to set up an efficient, gradient-based learning rule for
a policy
![\\mu(s)](_images/math/3c89236fa57c3dbe71f7c249a07267f83d9c638b.svg){.math}
which exploits that fact. Then, instead of running an expensive
optimization subroutine each time we wish to compute ![\\max_a
Q(s,a)](_images/math/03f01f77446d623f1c933e335f9f81c9a3558c4f.svg){.math},
we can approximate it with ![\\max_a Q(s,a) \\approx
Q(s,\\mu(s))](_images/math/8070b852fa94029e80d5811417fd76818a31ec4c.svg){.math}.
See the Key Equations section details.

::: {#ddpg.xhtml_quick-facts .section}
### [Quick Facts](#ddpg.xhtml_id3){.toc-backref}

- DDPG is an off-policy algorithm.
- DDPG can only be used for environments with continuous action spaces.
- DDPG can be thought of as being deep Q-learning for continuous action
  spaces.
- The Spinning Up implementation of DDPG does not support
  parallelization.
:::

:::::::::::: {#ddpg.xhtml_key-equations .section}
### [Key Equations](#ddpg.xhtml_id4){.toc-backref}

Here, we'll explain the math behind the two parts of DDPG: learning a Q
function, and learning a policy.

::::::::: {#ddpg.xhtml_the-q-learning-side-of-ddpg .section}
#### [The Q-Learning Side of DDPG](#ddpg.xhtml_id5){.toc-backref}

First, let's recap the Bellman equation describing the optimal
action-value function,
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}.
It's given by

::: math
![Q\^\*(s,a) = \\underset{s\' \\sim P}{{\\mathrm E}}\\left\[r(s,a) +
\\gamma \\max\_{a\'} Q\^\*(s\',
a\')\\right\]](_images/math/3a8b6ce0d6c0b68744b5724403f5d70ed5cda5db.svg)
:::

where ![s\' \\sim
P](_images/math/411171ab57c4bec0d86c9f4b495106ba5d73decc.svg){.math} is
shorthand for saying that the next state,
![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math},
is sampled by the environment from a distribution ![P(\\cdot\|
s,a)](_images/math/400976c62fa52ed70c85d7389f039b5e41473654.svg){.math}.

This Bellman equation is the starting point for learning an approximator
to
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}.
Suppose the approximator is a neural network
![Q\_{\\phi}(s,a)](_images/math/521198ffdba43bf32186f95801549cd1502b76c7.svg){.math},
with parameters
![\\phi](_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg){.math},
and that we have collected a set ![{\\mathcal
D}](_images/math/452456a08130b84d0c030fdc6e9b05973c5bc8b2.svg){.math} of
transitions
![(s,a,r,s\',d)](_images/math/4d273c4abe9c8d2805d78e826ee4368ed92841d7.svg){.math}
(where
![d](_images/math/9d61e89bfc1aa6993172a3ac47ab5be75f8e9e81.svg){.math}
indicates whether state
![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math}
is terminal). We can set up a **mean-squared Bellman error (MSBE)**
function, which tells us roughly how closely
![Q\_{\\phi}](_images/math/c25464faf1bf4928960905461cbbabe1d2441cb2.svg){.math}
comes to satisfying the Bellman equation:

::: math
![L(\\phi, {\\mathcal D}) = \\underset{(s,a,r,s\',d) \\sim {\\mathcal
D}}{{\\mathrm E}}\\left\[ \\Bigg( Q\_{\\phi}(s,a) - \\left(r + \\gamma
(1 - d) \\max\_{a\'} Q\_{\\phi}(s\',a\') \\right) \\Bigg)\^2
\\right\]](_images/math/31dda6ac0678255c4e192dd6fae4f7ed3c7cd91b.svg)
:::

Here, in evaluating
![(1-d)](_images/math/4591928b993b71d80f43193ffbbbef8e9f3aea10.svg){.math},
we've used a Python convention of evaluating [`True`{.docutils
.literal}]{.pre} to 1 and [`False`{.docutils .literal}]{.pre} to zero.
Thus, when [`d==True`{.docutils .literal}]{.pre}---which is to say, when
![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math}
is a terminal state---the Q-function should show that the agent gets no
additional rewards after the current state. (This choice of notation
corresponds to what we later implement in code.)

Q-learning algorithms for function approximators, such as DQN (and all
its variants) and DDPG, are largely based on minimizing this MSBE loss
function. There are two main tricks employed by all of them which are
worth describing, and then a specific detail for DDPG.

**Trick One: Replay Buffers.** All standard algorithms for training a
deep neural network to approximate
![Q\^\*(s,a)](_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg){.math}
make use of an experience replay buffer. This is the set ![{\\mathcal
D}](_images/math/452456a08130b84d0c030fdc6e9b05973c5bc8b2.svg){.math} of
previous experiences. In order for the algorithm to have stable
behavior, the replay buffer should be large enough to contain a wide
range of experiences, but it may not always be good to keep everything.
If you only use the very-most recent data, you will overfit to that and
things will break; if you use too much experience, you may slow down
your learning. This may take some tuning to get right.

::: {.admonition-you-should-know .admonition}
You Should Know

We've mentioned that DDPG is an off-policy algorithm: this is as good a
point as any to highlight why and how. Observe that the replay buffer
*should* contain old experiences, even though they might have been
obtained using an outdated policy. Why are we able to use these at all?
The reason is that the Bellman equation *doesn't care* which transition
tuples are used, or how the actions were selected, or what happens after
a given transition, because the optimal Q-function should satisfy the
Bellman equation for *all* possible transitions. So any transitions that
we've ever experienced are fair game when trying to fit a Q-function
approximator via MSBE minimization.
:::

**Trick Two: Target Networks.** Q-learning algorithms make use of
**target networks**. The term

::: math
![r + \\gamma (1 - d) \\max\_{a\'}
Q\_{\\phi}(s\',a\')](_images/math/fac308175faa67be9f5b27260abaf0ae6c4a58bb.svg)
:::

is called the **target**, because when we minimize the MSBE loss, we are
trying to make the Q-function be more like this target. Problematically,
the target depends on the same parameters we are trying to train:
![\\phi](_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg){.math}.
This makes MSBE minimization unstable. The solution is to use a set of
parameters which comes close to
![\\phi](_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg){.math},
but with a time delay---that is to say, a second network, called the
target network, which lags the first. The parameters of the target
network are denoted
![\\phi\_{\\text{targ}}](_images/math/3d9fb7e74f48ade89cbbcc0f3d1f3cb89a824864.svg){.math}.

In DQN-based algorithms, the target network is just copied over from the
main network every some-fixed-number of steps. In DDPG-style algorithms,
the target network is updated once per main network update by polyak
averaging:

::: math
![\\phi\_{\\text{targ}} \\leftarrow \\rho \\phi\_{\\text{targ}} + (1 -
\\rho)
\\phi,](_images/math/d417987803ca9f61ac60741880a748129bd66dde.svg)
:::

where
![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math}
is a hyperparameter between 0 and 1 (usually close to 1). (This
hyperparameter is called [`polyak`{.docutils .literal}]{.pre} in our
code).

**DDPG Detail: Calculating the Max Over Actions in the Target.** As
mentioned earlier: computing the maximum over actions in the target is a
challenge in continuous action spaces. DDPG deals with this by using a
**target policy network** to compute an action which approximately
maximizes
![Q\_{\\phi\_{\\text{targ}}}](_images/math/a50d5d2b71fa30f115adf18b0bb1354f967b064a.svg){.math}.
The target policy network is found the same way as the target
Q-function: by polyak averaging the policy parameters over the course of
training.

Putting it all together, Q-learning in DDPG is performed by minimizing
the following MSBE loss with stochastic gradient descent:

::: math
![L(\\phi, {\\mathcal D}) = \\underset{(s,a,r,s\',d) \\sim {\\mathcal
D}}{{\\mathrm E}}\\left\[ \\Bigg( Q\_{\\phi}(s,a) - \\left(r + \\gamma
(1 - d) Q\_{\\phi\_{\\text{targ}}}(s\',
\\mu\_{\\theta\_{\\text{targ}}}(s\')) \\right) \\Bigg)\^2
\\right\],](_images/math/4421120861d55302d76c7e2fd7cc5b2da7aea320.svg)
:::

where
![\\mu\_{\\theta\_{\\text{targ}}}](_images/math/a325c9e05fa2ccce85eb2384ca00b4888d1c7824.svg){.math}
is the target policy.
:::::::::

:::: {#ddpg.xhtml_the-policy-learning-side-of-ddpg .section}
#### [The Policy Learning Side of DDPG](#ddpg.xhtml_id6){.toc-backref}

Policy learning in DDPG is fairly simple. We want to learn a
deterministic policy
![\\mu\_{\\theta}(s)](_images/math/6923cb2043e84ea05d3eddbb7436c60659243cb9.svg){.math}
which gives the action that maximizes
![Q\_{\\phi}(s,a)](_images/math/521198ffdba43bf32186f95801549cd1502b76c7.svg){.math}.
Because the action space is continuous, and we assume the Q-function is
differentiable with respect to action, we can just perform gradient
ascent (with respect to policy parameters only) to solve

::: math
![\\max\_{\\theta} \\underset{s \\sim {\\mathcal D}}{{\\mathrm
E}}\\left\[ Q\_{\\phi}(s, \\mu\_{\\theta}(s))
\\right\].](_images/math/cc4e3565d839e63e871a1cf7e3ce5e95bb616b29.svg)
:::

Note that the Q-function parameters are treated as constants here.
::::
::::::::::::

:::: {#ddpg.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#ddpg.xhtml_id7){.toc-backref}

DDPG trains a deterministic policy in an off-policy way. Because the
policy is deterministic, if the agent were to explore on-policy, in the
beginning it would probably not try a wide enough variety of actions to
find useful learning signals. To make DDPG policies explore better, we
add noise to their actions at training time. The authors of the original
DDPG paper recommended time-correlated [OU
noise](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process){.reference
.external}[
\[https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process\]]{.link-target},
but more recent results suggest that uncorrelated, mean-zero Gaussian
noise works perfectly well. Since the latter is simpler, it is
preferred. To facilitate getting higher-quality training data, you may
reduce the scale of the noise over the course of training. (We do not do
this in our implementation, and keep noise scale fixed throughout.)

At test time, to see how well the policy exploits what it has learned,
we do not add noise to the actions.

::: {.admonition-you-should-know .admonition}
You Should Know

Our DDPG implementation uses a trick to improve exploration at the start
of training. For a fixed number of steps at the beginning (set with the
[`start_steps`{.docutils .literal}]{.pre} keyword argument), the agent
takes actions which are sampled from a uniform random distribution over
valid actions. After that, it returns to normal DDPG exploration.
:::
::::

:::: {#ddpg.xhtml_pseudocode .section}
### [Pseudocode](#ddpg.xhtml_id8){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{Deep Deterministic Policy Gradient}
\\label{alg1} \\begin{algorithmic}\[1\] \\STATE Input: initial policy
parameters \$\\theta\$, Q-function parameters \$\\phi\$, empty replay
buffer \$\\mathcal{D}\$ \\STATE Set target parameters equal to main
parameters \$\\theta\_{\\text{targ}} \\leftarrow \\theta\$,
\$\\phi\_{\\text{targ}} \\leftarrow \\phi\$ \\REPEAT \\STATE Observe
state \$s\$ and select action \$a = \\text{clip}(\\mu\_{\\theta}(s) +
\\epsilon, a\_{Low}, a\_{High})\$, where \$\\epsilon \\sim
\\mathcal{N}\$ \\STATE Execute \$a\$ in the environment \\STATE Observe
next state \$s\'\$, reward \$r\$, and done signal \$d\$ to indicate
whether \$s\'\$ is terminal \\STATE Store \$(s,a,r,s\',d)\$ in replay
buffer \$\\mathcal{D}\$ \\STATE If \$s\'\$ is terminal, reset
environment state. \\IF{it\'s time to update} \\FOR{however many
updates} \\STATE Randomly sample a batch of transitions, \$B = \\{
(s,a,r,s\',d) \\}\$ from \$\\mathcal{D}\$ \\STATE Compute targets
\\begin{equation\*} y(r,s\',d) = r + \\gamma (1-d)
Q\_{\\phi\_{\\text{targ}}}(s\', \\mu\_{\\theta\_{\\text{targ}}}(s\'))
\\end{equation\*} \\STATE Update Q-function by one step of gradient
descent using \\begin{equation\*} \\nabla\_{\\phi}
\\frac{1}{\|B\|}\\sum\_{(s,a,r,s\',d) \\in B} \\left( Q\_{\\phi}(s,a) -
y(r,s\',d) \\right)\^2 \\end{equation\*} \\STATE Update policy by one
step of gradient ascent using \\begin{equation\*} \\nabla\_{\\theta}
\\frac{1}{\|B\|}\\sum\_{s \\in B}Q\_{\\phi}(s, \\mu\_{\\theta}(s))
\\end{equation\*} \\STATE Update target networks with \\begin{align\*}
\\phi\_{\\text{targ}} &\\leftarrow \\rho \\phi\_{\\text{targ}} +
(1-\\rho) \\phi \\\\ \\theta\_{\\text{targ}} &\\leftarrow \\rho
\\theta\_{\\text{targ}} + (1-\\rho) \\theta \\end{align\*} \\ENDFOR
\\ENDIF \\UNTIL{convergence} \\end{algorithmic}
\\end{algorithm}](_images/math/5811066e89799e65be299ec407846103fcf1f746.svg)
:::
::::
:::::::::::::::::::

:::::::::: {#ddpg.xhtml_documentation .section}
## [Documentation](#ddpg.xhtml_id9){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow
implementations of DDPG in Spinning Up. They have nearly identical
function calls and docstrings, except for details relating to model
construction. However, we include both full docstrings for completeness.
:::

::: {#ddpg.xhtml_documentation-pytorch-version .section}
### [Documentation: PyTorch Version](#ddpg.xhtml_id10){.toc-backref}

`spinup.`{.descclassname}`ddpg_pytorch`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<MagicMock spec=\'str\' id=\'140679788656120\'\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi_lr=0.001*, *q_lr=0.001*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *act_noise=0.1*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Deep Deterministic Policy Gradient (DDPG)

    +-------------+------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The            |
    |             |   environment must satisfy the OpenAI Gym API.                                     |
    |             |                                                                                    |
    |             | - **actor_critic** --                                                              |
    |             |                                                                                    |
    |             |   The constructor method for a PyTorch Module with an [`act`{.docutils             |
    |             |   .literal}]{.pre} method, a [`pi`{.docutils .literal}]{.pre} module, and a        |
    |             |   [`q`{.docutils .literal}]{.pre} module. The [`act`{.docutils .literal}]{.pre}    |
    |             |   method and [`pi`{.docutils .literal}]{.pre} module should accept batches of      |
    |             |   observations as inputs, and [`q`{.docutils .literal}]{.pre} should accept a      |
    |             |   batch of observations and a batch of actions as inputs. When called, these       |
    |             |   should return:                                                                   |
    |             |                                                                                    |
    |             |   +------------------+----------------+------------------------------------------+ |
    |             |   | Call             | Output Shape   | Description                              | |
    |             |   +==================+================+==========================================+ |
    |             |   | [`act`{.docutils | (batch,        | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre} | act_dim)       | ::: line                                 | |
    |             |   |                  |                | Numpy array of actions for each          | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                |                                          | |
    |             |   |                  |                | ::: line                                 | |
    |             |   |                  |                | observation.                             | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                | :::::                                    | |
    |             |   +------------------+----------------+------------------------------------------+ |
    |             |   | [`pi`{.docutils  | (batch,        | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre} | act_dim)       | ::: line                                 | |
    |             |   |                  |                | Tensor containing actions from policy    | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                |                                          | |
    |             |   |                  |                | ::: line                                 | |
    |             |   |                  |                | given observations.                      | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                | :::::                                    | |
    |             |   +------------------+----------------+------------------------------------------+ |
    |             |   | [`q`{.docutils   | (batch,)       | ::::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre} |                | ::: line                                 | |
    |             |   |                  |                | Tensor containing the current estimate   | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                |                                          | |
    |             |   |                  |                | ::: line                                 | |
    |             |   |                  |                | of Q\* for the provided observations     | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                |                                          | |
    |             |   |                  |                | ::: line                                 | |
    |             |   |                  |                | and actions. (Critical: make sure to     | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                |                                          | |
    |             |   |                  |                | ::: line                                 | |
    |             |   |                  |                | flatten this!)                           | |
    |             |   |                  |                | :::                                      | |
    |             |   |                  |                | :::::::                                  | |
    |             |   +------------------+----------------+------------------------------------------+ |
    |             |                                                                                    |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the ActorCritic object you  |
    |             |   provided to DDPG.                                                                |
    |             |                                                                                    |
    |             | - **seed** (*int*) -- Seed for random number generators.                           |
    |             |                                                                                    |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action      |
    |             |   pairs) for the agent and the environment in each epoch.                          |
    |             |                                                                                    |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                   |
    |             |                                                                                    |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                      |
    |             |                                                                                    |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                |
    |             |                                                                                    |
    |             | - **polyak** (*float*) --                                                          |
    |             |                                                                                    |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks    |
    |             |   are updated towards main networks according to:                                  |
    |             |                                                                                    |
    |             |   ::: math                                                                         |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)  |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)              |
    |             |   :::                                                                              |
    |             |                                                                                    |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math} |
    |             |   is polyak. (Always between 0 and 1, usually close to 1.)                         |
    |             |                                                                                    |
    |             | - **pi_lr** (*float*) -- Learning rate for policy.                                 |
    |             |                                                                                    |
    |             | - **q_lr** (*float*) -- Learning rate for Q-networks.                              |
    |             |                                                                                    |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                |
    |             |                                                                                    |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,  |
    |             |   before running real policy. Helps exploration.                                   |
    |             |                                                                                    |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before         |
    |             |   starting to do gradient descent updates. Ensures replay buffer is full enough    |
    |             |   for useful updates.                                                              |
    |             |                                                                                    |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse        |
    |             |   between gradient descent updates. Note: Regardless of how long you wait between  |
    |             |   updates, the ratio of env steps to gradient steps is locked to 1.                |
    |             |                                                                                    |
    |             | - **act_noise** (*float*) -- Stddev for Gaussian exploration noise added to policy |
    |             |   at training time. (At test time, no noise is added.)                             |
    |             |                                                                                    |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic    |
    |             |   policy at the end of each epoch.                                                 |
    |             |                                                                                    |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.      |
    |             |                                                                                    |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                      |
    |             |                                                                                    |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the  |
    |             |   current policy and value function.                                               |
    +-------------+------------------------------------------------------------------------------------+
:::

::::: {#ddpg.xhtml_saved-model-contents-pytorch-version .section}
### [Saved Model Contents: PyTorch Version](#ddpg.xhtml_id11){.toc-backref}

The PyTorch saved model can be loaded with [`ac`{.docutils
.literal}]{.pre}` `{.docutils .literal}[`=`{.docutils
.literal}]{.pre}` `{.docutils
.literal}[`torch.load('path/to/model.pt')`{.docutils .literal}]{.pre},
yielding an actor-critic object ([`ac`{.docutils .literal}]{.pre}) that
has the properties described in the docstring for
[`ddpg_pytorch`{.docutils .literal}]{.pre}.

You can get actions from this model with

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::

::: {#ddpg.xhtml_documentation-tensorflow-version .section}
### [Documentation: Tensorflow Version](#ddpg.xhtml_id12){.toc-backref}

`spinup.`{.descclassname}`ddpg_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi_lr=0.001*, *q_lr=0.001*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *act_noise=0.1*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Deep Deterministic Policy Gradient (DDPG)

    +-------------+------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The            |
    |             |   environment must satisfy the OpenAI Gym API.                                     |
    |             |                                                                                    |
    |             | - **actor_critic** --                                                              |
    |             |                                                                                    |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils       |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns    |
    |             |   the main outputs from the agent's Tensorflow computation graph:                  |
    |             |                                                                                    |
    |             |   +-------------------+-----------------+----------------------------------------+ |
    |             |   | Symbol            | Shape           | Description                            | |
    |             |   +===================+=================+========================================+ |
    |             |   | [`pi`{.docutils   | (batch,         | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}  | act_dim)        | ::: line                               | |
    |             |   |                   |                 | Deterministically computes actions     | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 |                                        | |
    |             |   |                   |                 | ::: line                               | |
    |             |   |                   |                 | from policy given states.              | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 | :::::                                  | |
    |             |   +-------------------+-----------------+----------------------------------------+ |
    |             |   | [`q`{.docutils    | (batch,)        | :::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}  |                 | ::: line                               | |
    |             |   |                   |                 | Gives the current estimate of Q\* for  | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 |                                        | |
    |             |   |                   |                 | ::: line                               | |
    |             |   |                   |                 | states in [`x_ph`{.docutils            | |
    |             |   |                   |                 | .literal}]{.pre} and actions in        | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 |                                        | |
    |             |   |                   |                 | ::: line                               | |
    |             |   |                   |                 | [`a_ph`{.docutils .literal}]{.pre}.    | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 | ::::::                                 | |
    |             |   +-------------------+-----------------+----------------------------------------+ |
    |             |   | [`q_pi`{.docutils | (batch,)        | :::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}  |                 | ::: line                               | |
    |             |   |                   |                 | Gives the composition of               | |
    |             |   |                   |                 | [`q`{.docutils .literal}]{.pre} and    | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 |                                        | |
    |             |   |                   |                 | ::: line                               | |
    |             |   |                   |                 | [`pi`{.docutils .literal}]{.pre} for   | |
    |             |   |                   |                 | states in [`x_ph`{.docutils            | |
    |             |   |                   |                 | .literal}]{.pre}:                      | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 |                                        | |
    |             |   |                   |                 | ::: line                               | |
    |             |   |                   |                 | q(x, pi(x)).                           | |
    |             |   |                   |                 | :::                                    | |
    |             |   |                   |                 | ::::::                                 | |
    |             |   +-------------------+-----------------+----------------------------------------+ |
    |             |                                                                                    |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function   |
    |             |   you provided to DDPG.                                                            |
    |             |                                                                                    |
    |             | - **seed** (*int*) -- Seed for random number generators.                           |
    |             |                                                                                    |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action      |
    |             |   pairs) for the agent and the environment in each epoch.                          |
    |             |                                                                                    |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                   |
    |             |                                                                                    |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                      |
    |             |                                                                                    |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                |
    |             |                                                                                    |
    |             | - **polyak** (*float*) --                                                          |
    |             |                                                                                    |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks    |
    |             |   are updated towards main networks according to:                                  |
    |             |                                                                                    |
    |             |   ::: math                                                                         |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)  |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)              |
    |             |   :::                                                                              |
    |             |                                                                                    |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math} |
    |             |   is polyak. (Always between 0 and 1, usually close to 1.)                         |
    |             |                                                                                    |
    |             | - **pi_lr** (*float*) -- Learning rate for policy.                                 |
    |             |                                                                                    |
    |             | - **q_lr** (*float*) -- Learning rate for Q-networks.                              |
    |             |                                                                                    |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                |
    |             |                                                                                    |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,  |
    |             |   before running real policy. Helps exploration.                                   |
    |             |                                                                                    |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before         |
    |             |   starting to do gradient descent updates. Ensures replay buffer is full enough    |
    |             |   for useful updates.                                                              |
    |             |                                                                                    |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse        |
    |             |   between gradient descent updates. Note: Regardless of how long you wait between  |
    |             |   updates, the ratio of env steps to gradient steps is locked to 1.                |
    |             |                                                                                    |
    |             | - **act_noise** (*float*) -- Stddev for Gaussian exploration noise added to policy |
    |             |   at training time. (At test time, no noise is added.)                             |
    |             |                                                                                    |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic    |
    |             |   policy at the end of each epoch.                                                 |
    |             |                                                                                    |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.      |
    |             |                                                                                    |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                      |
    |             |                                                                                    |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the  |
    |             |   current policy and value function.                                               |
    +-------------+------------------------------------------------------------------------------------+
:::

::: {#ddpg.xhtml_saved-model-contents-tensorflow-version .section}
### [Saved Model Contents: Tensorflow Version](#ddpg.xhtml_id13){.toc-backref}

The computation graph saved by the logger includes:

+------------------+---------------------------------------------------------------+
| Key              | Value                                                         |
+==================+===============================================================+
| [`x`{.docutils   | Tensorflow placeholder for state input.                       |
| .literal}]{.pre} |                                                               |
+------------------+---------------------------------------------------------------+
| [`a`{.docutils   | Tensorflow placeholder for action input.                      |
| .literal}]{.pre} |                                                               |
+------------------+---------------------------------------------------------------+
| [`pi`{.docutils  | ::::: {.first .last .line-block}                              |
| .literal}]{.pre} | ::: line                                                      |
|                  | Deterministically computes an action from the agent,          |
|                  | conditioned                                                   |
|                  | :::                                                           |
|                  |                                                               |
|                  | ::: line                                                      |
|                  | on states in [`x`{.docutils .literal}]{.pre}.                 |
|                  | :::                                                           |
|                  | :::::                                                         |
+------------------+---------------------------------------------------------------+
| [`q`{.docutils   | Gives action-value estimate for states in [`x`{.docutils      |
| .literal}]{.pre} | .literal}]{.pre} and actions in [`a`{.docutils                |
|                  | .literal}]{.pre}.                                             |
+------------------+---------------------------------------------------------------+

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.
:::
::::::::::

:::::: {#ddpg.xhtml_references .section}
## [References](#ddpg.xhtml_id14){.toc-backref}

::: {#ddpg.xhtml_relevant-papers .section}
### [Relevant Papers](#ddpg.xhtml_id15){.toc-backref}

- [Deterministic Policy Gradient
  Algorithms](http://proceedings.mlr.press/v32/silver14.pdf){.reference
  .external}[
  \[http://proceedings.mlr.press/v32/silver14.pdf\]]{.link-target},
  Silver et al. 2014
- [Continuous Control With Deep Reinforcement
  Learning](https://arxiv.org/abs/1509.02971){.reference .external}[
  \[https://arxiv.org/abs/1509.02971\]]{.link-target}, Lillicrap et al.
  2016
:::

::: {#ddpg.xhtml_why-these-papers .section}
### [Why These Papers?](#ddpg.xhtml_id16){.toc-backref}

Silver 2014 is included because it establishes the theory underlying
deterministic policy gradients (DPG). Lillicrap 2016 is included because
it adapts the theoretically-grounded DPG algorithm to the deep RL
setting, giving DDPG.
:::

::: {#ddpg.xhtml_other-public-implementations .section}
### [Other Public Implementations](#ddpg.xhtml_id17){.toc-backref}

- [Baselines](https://github.com/openai/baselines/tree/master/baselines/ddpg){.reference
  .external}[
  \[https://github.com/openai/baselines/tree/master/baselines/ddpg\]]{.link-target}
- [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/ddpg.py){.reference
  .external}[
  \[https://github.com/rll/rllab/blob/master/rllab/algos/ddpg.py\]]{.link-target}
- [rllib
  (Ray)](https://github.com/ray-project/ray/tree/master/python/ray/rllib/agents/ddpg){.reference
  .external}[
  \[https://github.com/ray-project/ray/tree/master/python/ray/rllib/agents/ddpg\]]{.link-target}
- [TD3 release repo](https://github.com/sfujim/TD3){.reference
  .external}[ \[https://github.com/sfujim/TD3\]]{.link-target}
:::
::::::
:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::

[]{#td3.xhtml}

:::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::: {#td3.xhtml_twin-delayed-ddpg .section}
# [Twin Delayed DDPG](#td3.xhtml_id1){.toc-backref}

::: {#td3.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Twin Delayed DDPG](#td3.xhtml_twin-delayed-ddpg){#td3.xhtml_id1
  .reference .internal}
  - [Background](#td3.xhtml_background){#td3.xhtml_id2 .reference
    .internal}
    - [Quick Facts](#td3.xhtml_quick-facts){#td3.xhtml_id3 .reference
      .internal}
    - [Key Equations](#td3.xhtml_key-equations){#td3.xhtml_id4
      .reference .internal}
    - [Exploration vs.
      Exploitation](#td3.xhtml_exploration-vs-exploitation){#td3.xhtml_id5
      .reference .internal}
    - [Pseudocode](#td3.xhtml_pseudocode){#td3.xhtml_id6 .reference
      .internal}
  - [Documentation](#td3.xhtml_documentation){#td3.xhtml_id7 .reference
    .internal}
    - [Documentation: PyTorch
      Version](#td3.xhtml_documentation-pytorch-version){#td3.xhtml_id8
      .reference .internal}
    - [Saved Model Contents: PyTorch
      Version](#td3.xhtml_saved-model-contents-pytorch-version){#td3.xhtml_id9
      .reference .internal}
    - [Documentation: Tensorflow
      Version](#td3.xhtml_documentation-tensorflow-version){#td3.xhtml_id10
      .reference .internal}
    - [Saved Model Contents: Tensorflow
      Version](#td3.xhtml_saved-model-contents-tensorflow-version){#td3.xhtml_id11
      .reference .internal}
  - [References](#td3.xhtml_references){#td3.xhtml_id12 .reference
    .internal}
    - [Relevant Papers](#td3.xhtml_relevant-papers){#td3.xhtml_id13
      .reference .internal}
    - [Other Public
      Implementations](#td3.xhtml_other-public-implementations){#td3.xhtml_id14
      .reference .internal}
:::

:::::::::::::: {#td3.xhtml_background .section}
## [Background](#td3.xhtml_id2){.toc-backref}

(Previously: [Background for DDPG](ddpg.html_background){.reference
.external})

While DDPG can achieve great performance sometimes, it is frequently
brittle with respect to hyperparameters and other kinds of tuning. A
common failure mode for DDPG is that the learned Q-function begins to
dramatically overestimate Q-values, which then leads to the policy
breaking, because it exploits the errors in the Q-function. Twin Delayed
DDPG (TD3) is an algorithm that addresses this issue by introducing
three critical tricks:

**Trick One: Clipped Double-Q Learning.** TD3 learns *two* Q-functions
instead of one (hence "twin"), and uses the smaller of the two Q-values
to form the targets in the Bellman error loss functions.

**Trick Two: "Delayed" Policy Updates.** TD3 updates the policy (and
target networks) less frequently than the Q-function. The paper
recommends one policy update for every two Q-function updates.

**Trick Three: Target Policy Smoothing.** TD3 adds noise to the target
action, to make it harder for the policy to exploit Q-function errors by
smoothing out Q along changes in action.

Together, these three tricks result in substantially improved
performance over baseline DDPG.

::: {#td3.xhtml_quick-facts .section}
### [Quick Facts](#td3.xhtml_id3){.toc-backref}

- TD3 is an off-policy algorithm.
- TD3 can only be used for environments with continuous action spaces.
- The Spinning Up implementation of TD3 does not support
  parallelization.
:::

:::::::: {#td3.xhtml_key-equations .section}
### [Key Equations](#td3.xhtml_id4){.toc-backref}

TD3 concurrently learns two Q-functions,
![Q\_{\\phi_1}](_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg){.math}
and
![Q\_{\\phi_2}](_images/math/ac4e235414bfd47d449e3440ba29ae8470d3952e.svg){.math},
by mean square Bellman error minimization, in almost the same way that
DDPG learns its single Q-function. To show exactly how TD3 does this and
how it differs from normal DDPG, we'll work from the innermost part of
the loss function outwards.

First: **target policy smoothing**. Actions used to form the Q-learning
target are based on the target policy,
![\\mu\_{\\theta\_{\\text{targ}}}](_images/math/a325c9e05fa2ccce85eb2384ca00b4888d1c7824.svg){.math},
but with clipped noise added on each dimension of the action. After
adding the clipped noise, the target action is then clipped to lie in
the valid action range (all valid actions,
![a](_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg){.math},
satisfy ![a\_{Low} \\leq a \\leq
a\_{High}](_images/math/a5132668c0af8733656505c5fb6c1dff4a7907a1.svg){.math}).
The target actions are thus:

::: math
![a\'(s\') = \\text{clip}\\left(\\mu\_{\\theta\_{\\text{targ}}}(s\') +
\\text{clip}(\\epsilon,-c,c), a\_{Low}, a\_{High}\\right),
\\;\\;\\;\\;\\; \\epsilon \\sim \\mathcal{N}(0,
\\sigma)](_images/math/8efd61c40551db4eddb3f780d2804cac34c8ae52.svg)
:::

Target policy smoothing essentially serves as a regularizer for the
algorithm. It addresses a particular failure mode that can happen in
DDPG: if the Q-function approximator develops an incorrect sharp peak
for some actions, the policy will quickly exploit that peak and then
have brittle or incorrect behavior. This can be averted by smoothing out
the Q-function over similar actions, which target policy smoothing is
designed to do.

Next: **clipped double-Q learning**. Both Q-functions use a single
target, calculated using whichever of the two Q-functions gives a
smaller target value:

::: math
![y(r,s\',d) = r + \\gamma (1 - d) \\min\_{i=1,2} Q\_{\\phi\_{i,
\\text{targ}}}(s\',
a\'(s\')),](_images/math/70901eaea34c31e03bb878d7a710a33cb75d1143.svg)
:::

and then both are learned by regressing to this target:

::: math
![L(\\phi_1, {\\mathcal D}) = \\underE{(s,a,r,s\',d) \\sim {\\mathcal
D}}{ \\Bigg( Q\_{\\phi_1}(s,a) - y(r,s\',d) \\Bigg)\^2
},](_images/math/7d5c18f49a242cc3eec554f717fe4f3bfc119bab.svg)
:::

::: math
![L(\\phi_2, {\\mathcal D}) = \\underE{(s,a,r,s\',d) \\sim {\\mathcal
D}}{ \\Bigg( Q\_{\\phi_2}(s,a) - y(r,s\',d) \\Bigg)\^2
}.](_images/math/cd73726a8a3845ade467aed57714912f868f6b36.svg)
:::

Using the smaller Q-value for the target, and regressing towards that,
helps fend off overestimation in the Q-function.

Lastly: the policy is learned just by maximizing
![Q\_{\\phi_1}](_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg){.math}:

::: math
![\\max\_{\\theta} \\underset{s \\sim {\\mathcal D}}{{\\mathrm
E}}\\left\[ Q\_{\\phi_1}(s, \\mu\_{\\theta}(s))
\\right\],](_images/math/9ed1a541005a48d51b624c3b329897064ec2c065.svg)
:::

which is pretty much unchanged from DDPG. However, in TD3, the policy is
updated less frequently than the Q-functions are. This helps damp the
volatility that normally arises in DDPG because of how a policy update
changes the target.
::::::::

:::: {#td3.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#td3.xhtml_id5){.toc-backref}

TD3 trains a deterministic policy in an off-policy way. Because the
policy is deterministic, if the agent were to explore on-policy, in the
beginning it would probably not try a wide enough variety of actions to
find useful learning signals. To make TD3 policies explore better, we
add noise to their actions at training time, typically uncorrelated
mean-zero Gaussian noise. To facilitate getting higher-quality training
data, you may reduce the scale of the noise over the course of training.
(We do not do this in our implementation, and keep noise scale fixed
throughout.)

At test time, to see how well the policy exploits what it has learned,
we do not add noise to the actions.

::: {.admonition-you-should-know .admonition}
You Should Know

Our TD3 implementation uses a trick to improve exploration at the start
of training. For a fixed number of steps at the beginning (set with the
[`start_steps`{.docutils .literal}]{.pre} keyword argument), the agent
takes actions which are sampled from a uniform random distribution over
valid actions. After that, it returns to normal TD3 exploration.
:::
::::

:::: {#td3.xhtml_pseudocode .section}
### [Pseudocode](#td3.xhtml_id6){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{Twin Delayed DDPG} \\label{alg1}
\\begin{algorithmic}\[1\] \\STATE Input: initial policy parameters
\$\\theta\$, Q-function parameters \$\\phi_1\$, \$\\phi_2\$, empty
replay buffer \$\\mathcal{D}\$ \\STATE Set target parameters equal to
main parameters \$\\theta\_{\\text{targ}} \\leftarrow \\theta\$,
\$\\phi\_{\\text{targ},1} \\leftarrow \\phi_1\$,
\$\\phi\_{\\text{targ},2} \\leftarrow \\phi_2\$ \\REPEAT \\STATE Observe
state \$s\$ and select action \$a = \\text{clip}(\\mu\_{\\theta}(s) +
\\epsilon, a\_{Low}, a\_{High})\$, where \$\\epsilon \\sim
\\mathcal{N}\$ \\STATE Execute \$a\$ in the environment \\STATE Observe
next state \$s\'\$, reward \$r\$, and done signal \$d\$ to indicate
whether \$s\'\$ is terminal \\STATE Store \$(s,a,r,s\',d)\$ in replay
buffer \$\\mathcal{D}\$ \\STATE If \$s\'\$ is terminal, reset
environment state. \\IF{it\'s time to update} \\FOR{\$j\$ in
range(however many updates)} \\STATE Randomly sample a batch of
transitions, \$B = \\{ (s,a,r,s\',d) \\}\$ from \$\\mathcal{D}\$ \\STATE
Compute target actions \\begin{equation\*} a\'(s\') =
\\text{clip}\\left(\\mu\_{\\theta\_{\\text{targ}}}(s\') +
\\text{clip}(\\epsilon,-c,c), a\_{Low}, a\_{High}\\right),
\\;\\;\\;\\;\\; \\epsilon \\sim \\mathcal{N}(0, \\sigma)
\\end{equation\*} \\STATE Compute targets \\begin{equation\*} y(r,s\',d)
= r + \\gamma (1-d) \\min\_{i=1,2} Q\_{\\phi\_{\\text{targ},i}}(s\',
a\'(s\')) \\end{equation\*} \\STATE Update Q-functions by one step of
gradient descent using \\begin{align\*} & \\nabla\_{\\phi_i}
\\frac{1}{\|B\|}\\sum\_{(s,a,r,s\',d) \\in B} \\left(
Q\_{\\phi_i}(s,a) - y(r,s\',d) \\right)\^2 && \\text{for } i=1,2
\\end{align\*} \\IF{ \$j \\mod\$ \\texttt{policy\\\_delay} \$ = 0\$}
\\STATE Update policy by one step of gradient ascent using
\\begin{equation\*} \\nabla\_{\\theta} \\frac{1}{\|B\|}\\sum\_{s \\in
B}Q\_{\\phi_1}(s, \\mu\_{\\theta}(s)) \\end{equation\*} \\STATE Update
target networks with \\begin{align\*} \\phi\_{\\text{targ},i}
&\\leftarrow \\rho \\phi\_{\\text{targ}, i} + (1-\\rho) \\phi_i &&
\\text{for } i=1,2\\\\ \\theta\_{\\text{targ}} &\\leftarrow \\rho
\\theta\_{\\text{targ}} + (1-\\rho) \\theta \\end{align\*} \\ENDIF
\\ENDFOR \\ENDIF \\UNTIL{convergence} \\end{algorithmic}
\\end{algorithm}](_images/math/b7dfe8fa3a703b9657dcecb624c4457926e0ce8a.svg)
:::
::::
::::::::::::::

:::::::::: {#td3.xhtml_documentation .section}
## [Documentation](#td3.xhtml_id7){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow
implementations of TD3 in Spinning Up. They have nearly identical
function calls and docstrings, except for details relating to model
construction. However, we include both full docstrings for completeness.
:::

::: {#td3.xhtml_documentation-pytorch-version .section}
### [Documentation: PyTorch Version](#td3.xhtml_id8){.toc-backref}

`spinup.`{.descclassname}`td3_pytorch`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<MagicMock spec=\'str\' id=\'140679788131776\'\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi_lr=0.001*, *q_lr=0.001*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *act_noise=0.1*, *target_noise=0.2*, *noise_clip=0.5*, *policy_delay=2*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Twin Delayed Deep Deterministic Policy Gradient (TD3)

    +-------------+------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The            |
    |             |   environment must satisfy the OpenAI Gym API.                                     |
    |             |                                                                                    |
    |             | - **actor_critic** --                                                              |
    |             |                                                                                    |
    |             |   The constructor method for a PyTorch Module with an [`act`{.docutils             |
    |             |   .literal}]{.pre} method, a [`pi`{.docutils .literal}]{.pre} module, a            |
    |             |   [`q1`{.docutils .literal}]{.pre} module, and a [`q2`{.docutils .literal}]{.pre}  |
    |             |   module. The [`act`{.docutils .literal}]{.pre} method and [`pi`{.docutils         |
    |             |   .literal}]{.pre} module should accept batches of observations as inputs, and     |
    |             |   [`q1`{.docutils .literal}]{.pre} and [`q2`{.docutils .literal}]{.pre} should     |
    |             |   accept a batch of observations and a batch of actions as inputs. When called,    |
    |             |   these should return:                                                             |
    |             |                                                                                    |
    |             |   +------------------+--------------+--------------------------------------------+ |
    |             |   | Call             | Output Shape | Description                                | |
    |             |   +==================+==============+============================================+ |
    |             |   | [`act`{.docutils | (batch,      | ::::: {.first .last .line-block}           | |
    |             |   | .literal}]{.pre} | act_dim)     | ::: line                                   | |
    |             |   |                  |              | Numpy array of actions for each            | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | observation.                               | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              | :::::                                      | |
    |             |   +------------------+--------------+--------------------------------------------+ |
    |             |   | [`pi`{.docutils  | (batch,      | ::::: {.first .last .line-block}           | |
    |             |   | .literal}]{.pre} | act_dim)     | ::: line                                   | |
    |             |   |                  |              | Tensor containing actions from policy      | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | given observations.                        | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              | :::::                                      | |
    |             |   +------------------+--------------+--------------------------------------------+ |
    |             |   | [`q1`{.docutils  | (batch,)     | ::::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre} |              | ::: line                                   | |
    |             |   |                  |              | Tensor containing one current estimate     | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | of Q\* for the provided observations       | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | and actions. (Critical: make sure to       | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | flatten this!)                             | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              | :::::::                                    | |
    |             |   +------------------+--------------+--------------------------------------------+ |
    |             |   | [`q2`{.docutils  | (batch,)     | ::::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre} |              | ::: line                                   | |
    |             |   |                  |              | Tensor containing the other current        | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | estimate of Q\* for the provided           | |
    |             |   |                  |              | observations                               | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | and actions. (Critical: make sure to       | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              |                                            | |
    |             |   |                  |              | ::: line                                   | |
    |             |   |                  |              | flatten this!)                             | |
    |             |   |                  |              | :::                                        | |
    |             |   |                  |              | :::::::                                    | |
    |             |   +------------------+--------------+--------------------------------------------+ |
    |             |                                                                                    |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the ActorCritic object you  |
    |             |   provided to TD3.                                                                 |
    |             |                                                                                    |
    |             | - **seed** (*int*) -- Seed for random number generators.                           |
    |             |                                                                                    |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action      |
    |             |   pairs) for the agent and the environment in each epoch.                          |
    |             |                                                                                    |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                   |
    |             |                                                                                    |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                      |
    |             |                                                                                    |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                |
    |             |                                                                                    |
    |             | - **polyak** (*float*) --                                                          |
    |             |                                                                                    |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks    |
    |             |   are updated towards main networks according to:                                  |
    |             |                                                                                    |
    |             |   ::: math                                                                         |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)  |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)              |
    |             |   :::                                                                              |
    |             |                                                                                    |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math} |
    |             |   is polyak. (Always between 0 and 1, usually close to 1.)                         |
    |             |                                                                                    |
    |             | - **pi_lr** (*float*) -- Learning rate for policy.                                 |
    |             |                                                                                    |
    |             | - **q_lr** (*float*) -- Learning rate for Q-networks.                              |
    |             |                                                                                    |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                |
    |             |                                                                                    |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,  |
    |             |   before running real policy. Helps exploration.                                   |
    |             |                                                                                    |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before         |
    |             |   starting to do gradient descent updates. Ensures replay buffer is full enough    |
    |             |   for useful updates.                                                              |
    |             |                                                                                    |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse        |
    |             |   between gradient descent updates. Note: Regardless of how long you wait between  |
    |             |   updates, the ratio of env steps to gradient steps is locked to 1.                |
    |             |                                                                                    |
    |             | - **act_noise** (*float*) -- Stddev for Gaussian exploration noise added to policy |
    |             |   at training time. (At test time, no noise is added.)                             |
    |             |                                                                                    |
    |             | - **target_noise** (*float*) -- Stddev for smoothing noise added to target policy. |
    |             |                                                                                    |
    |             | - **noise_clip** (*float*) -- Limit for absolute value of target policy smoothing  |
    |             |   noise.                                                                           |
    |             |                                                                                    |
    |             | - **policy_delay** (*int*) -- Policy will only be updated once every policy_delay  |
    |             |   times for each update of the Q-networks.                                         |
    |             |                                                                                    |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic    |
    |             |   policy at the end of each epoch.                                                 |
    |             |                                                                                    |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.      |
    |             |                                                                                    |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                      |
    |             |                                                                                    |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the  |
    |             |   current policy and value function.                                               |
    +-------------+------------------------------------------------------------------------------------+
:::

::::: {#td3.xhtml_saved-model-contents-pytorch-version .section}
### [Saved Model Contents: PyTorch Version](#td3.xhtml_id9){.toc-backref}

The PyTorch saved model can be loaded with [`ac`{.docutils
.literal}]{.pre}` `{.docutils .literal}[`=`{.docutils
.literal}]{.pre}` `{.docutils
.literal}[`torch.load('path/to/model.pt')`{.docutils .literal}]{.pre},
yielding an actor-critic object ([`ac`{.docutils .literal}]{.pre}) that
has the properties described in the docstring for
[`td3_pytorch`{.docutils .literal}]{.pre}.

You can get actions from this model with

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::

::: {#td3.xhtml_documentation-tensorflow-version .section}
### [Documentation: Tensorflow Version](#td3.xhtml_id10){.toc-backref}

`spinup.`{.descclassname}`td3_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi_lr=0.001*, *q_lr=0.001*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *act_noise=0.1*, *target_noise=0.2*, *noise_clip=0.5*, *policy_delay=2*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Twin Delayed Deep Deterministic Policy Gradient (TD3)

    +-------------+-------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment |
    |             |   must satisfy the OpenAI Gym API.                                                  |
    |             |                                                                                     |
    |             | - **actor_critic** --                                                               |
    |             |                                                                                     |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils        |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns the |
    |             |   main outputs from the agent's Tensorflow computation graph:                       |
    |             |                                                                                     |
    |             |   +--------------------+-----------------+----------------------------------------+ |
    |             |   | Symbol             | Shape           | Description                            | |
    |             |   +====================+=================+========================================+ |
    |             |   | [`pi`{.docutils    | (batch,         | ::::: {.first .last .line-block}       | |
    |             |   | .literal}]{.pre}   | act_dim)        | ::: line                               | |
    |             |   |                    |                 | Deterministically computes actions     | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | from policy given states.              | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 | :::::                                  | |
    |             |   +--------------------+-----------------+----------------------------------------+ |
    |             |   | [`q1`{.docutils    | (batch,)        | :::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}   |                 | ::: line                               | |
    |             |   |                    |                 | Gives one estimate of Q\* for          | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | states in [`x_ph`{.docutils            | |
    |             |   |                    |                 | .literal}]{.pre} and actions in        | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | [`a_ph`{.docutils .literal}]{.pre}.    | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 | ::::::                                 | |
    |             |   +--------------------+-----------------+----------------------------------------+ |
    |             |   | [`q2`{.docutils    | (batch,)        | :::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}   |                 | ::: line                               | |
    |             |   |                    |                 | Gives another estimate of Q\* for      | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | states in [`x_ph`{.docutils            | |
    |             |   |                    |                 | .literal}]{.pre} and actions in        | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | [`a_ph`{.docutils .literal}]{.pre}.    | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 | ::::::                                 | |
    |             |   +--------------------+-----------------+----------------------------------------+ |
    |             |   | [`q1_pi`{.docutils | (batch,)        | :::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}   |                 | ::: line                               | |
    |             |   |                    |                 | Gives the composition of               | |
    |             |   |                    |                 | [`q1`{.docutils .literal}]{.pre} and   | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | [`pi`{.docutils .literal}]{.pre} for   | |
    |             |   |                    |                 | states in [`x_ph`{.docutils            | |
    |             |   |                    |                 | .literal}]{.pre}:                      | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 |                                        | |
    |             |   |                    |                 | ::: line                               | |
    |             |   |                    |                 | q1(x, pi(x)).                          | |
    |             |   |                    |                 | :::                                    | |
    |             |   |                    |                 | ::::::                                 | |
    |             |   +--------------------+-----------------+----------------------------------------+ |
    |             |                                                                                     |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function    |
    |             |   you provided to TD3.                                                              |
    |             |                                                                                     |
    |             | - **seed** (*int*) -- Seed for random number generators.                            |
    |             |                                                                                     |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action       |
    |             |   pairs) for the agent and the environment in each epoch.                           |
    |             |                                                                                     |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                    |
    |             |                                                                                     |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                       |
    |             |                                                                                     |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                 |
    |             |                                                                                     |
    |             | - **polyak** (*float*) --                                                           |
    |             |                                                                                     |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks are |
    |             |   updated towards main networks according to:                                       |
    |             |                                                                                     |
    |             |   ::: math                                                                          |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)   |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)               |
    |             |   :::                                                                               |
    |             |                                                                                     |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math}  |
    |             |   is polyak. (Always between 0 and 1, usually close to 1.)                          |
    |             |                                                                                     |
    |             | - **pi_lr** (*float*) -- Learning rate for policy.                                  |
    |             |                                                                                     |
    |             | - **q_lr** (*float*) -- Learning rate for Q-networks.                               |
    |             |                                                                                     |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                 |
    |             |                                                                                     |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,   |
    |             |   before running real policy. Helps exploration.                                    |
    |             |                                                                                     |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before starting |
    |             |   to do gradient descent updates. Ensures replay buffer is full enough for useful   |
    |             |   updates.                                                                          |
    |             |                                                                                     |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse between |
    |             |   gradient descent updates. Note: Regardless of how long you wait between updates,  |
    |             |   the ratio of env steps to gradient steps is locked to 1.                          |
    |             |                                                                                     |
    |             | - **act_noise** (*float*) -- Stddev for Gaussian exploration noise added to policy  |
    |             |   at training time. (At test time, no noise is added.)                              |
    |             |                                                                                     |
    |             | - **target_noise** (*float*) -- Stddev for smoothing noise added to target policy.  |
    |             |                                                                                     |
    |             | - **noise_clip** (*float*) -- Limit for absolute value of target policy smoothing   |
    |             |   noise.                                                                            |
    |             |                                                                                     |
    |             | - **policy_delay** (*int*) -- Policy will only be updated once every policy_delay   |
    |             |   times for each update of the Q-networks.                                          |
    |             |                                                                                     |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic     |
    |             |   policy at the end of each epoch.                                                  |
    |             |                                                                                     |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.       |
    |             |                                                                                     |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                       |
    |             |                                                                                     |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the   |
    |             |   current policy and value function.                                                |
    +-------------+-------------------------------------------------------------------------------------+
:::

::: {#td3.xhtml_saved-model-contents-tensorflow-version .section}
### [Saved Model Contents: Tensorflow Version](#td3.xhtml_id11){.toc-backref}

The computation graph saved by the logger includes:

+------------------+----------------------------------------------------------------+
| Key              | Value                                                          |
+==================+================================================================+
| [`x`{.docutils   | Tensorflow placeholder for state input.                        |
| .literal}]{.pre} |                                                                |
+------------------+----------------------------------------------------------------+
| [`a`{.docutils   | Tensorflow placeholder for action input.                       |
| .literal}]{.pre} |                                                                |
+------------------+----------------------------------------------------------------+
| [`pi`{.docutils  | ::::: {.first .last .line-block}                               |
| .literal}]{.pre} | ::: line                                                       |
|                  | Deterministically computes an action from the agent,           |
|                  | conditioned                                                    |
|                  | :::                                                            |
|                  |                                                                |
|                  | ::: line                                                       |
|                  | on states in [`x`{.docutils .literal}]{.pre}.                  |
|                  | :::                                                            |
|                  | :::::                                                          |
+------------------+----------------------------------------------------------------+
| [`q1`{.docutils  | Gives one action-value estimate for states in [`x`{.docutils   |
| .literal}]{.pre} | .literal}]{.pre} and actions in [`a`{.docutils                 |
|                  | .literal}]{.pre}.                                              |
+------------------+----------------------------------------------------------------+
| [`q2`{.docutils  | Gives the other action-value estimate for states in            |
| .literal}]{.pre} | [`x`{.docutils .literal}]{.pre} and actions in [`a`{.docutils  |
|                  | .literal}]{.pre}.                                              |
+------------------+----------------------------------------------------------------+

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.
:::
::::::::::

::::: {#td3.xhtml_references .section}
## [References](#td3.xhtml_id12){.toc-backref}

::: {#td3.xhtml_relevant-papers .section}
### [Relevant Papers](#td3.xhtml_id13){.toc-backref}

- [Addressing Function Approximation Error in Actor-Critic
  Methods](https://arxiv.org/abs/1802.09477){.reference .external}[
  \[https://arxiv.org/abs/1802.09477\]]{.link-target}, Fujimoto et al,
  2018
:::

::: {#td3.xhtml_other-public-implementations .section}
### [Other Public Implementations](#td3.xhtml_id14){.toc-backref}

- [TD3 release repo](https://github.com/sfujim/TD3){.reference
  .external}[ \[https://github.com/sfujim/TD3\]]{.link-target}
:::
:::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

[]{#sac.xhtml}

::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::: {#sac.xhtml_soft-actor-critic .section}
# [Soft Actor-Critic](#sac.xhtml_id2){.toc-backref}

::: {#sac.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Soft Actor-Critic](#sac.xhtml_soft-actor-critic){#sac.xhtml_id2
  .reference .internal}
  - [Background](#sac.xhtml_background){#sac.xhtml_id3 .reference
    .internal}
    - [Quick Facts](#sac.xhtml_quick-facts){#sac.xhtml_id4 .reference
      .internal}
    - [Key Equations](#sac.xhtml_key-equations){#sac.xhtml_id5
      .reference .internal}
      - [Entropy-Regularized Reinforcement
        Learning](#sac.xhtml_entropy-regularized-reinforcement-learning){#sac.xhtml_id6
        .reference .internal}
      - [Soft Actor-Critic](#sac.xhtml_id1){#sac.xhtml_id7 .reference
        .internal}
    - [Exploration vs.
      Exploitation](#sac.xhtml_exploration-vs-exploitation){#sac.xhtml_id8
      .reference .internal}
    - [Pseudocode](#sac.xhtml_pseudocode){#sac.xhtml_id9 .reference
      .internal}
  - [Documentation](#sac.xhtml_documentation){#sac.xhtml_id10 .reference
    .internal}
    - [Documentation: PyTorch
      Version](#sac.xhtml_documentation-pytorch-version){#sac.xhtml_id11
      .reference .internal}
    - [Saved Model Contents: PyTorch
      Version](#sac.xhtml_saved-model-contents-pytorch-version){#sac.xhtml_id12
      .reference .internal}
    - [Documentation: Tensorflow
      Version](#sac.xhtml_documentation-tensorflow-version){#sac.xhtml_id13
      .reference .internal}
    - [Saved Model Contents: Tensorflow
      Version](#sac.xhtml_saved-model-contents-tensorflow-version){#sac.xhtml_id14
      .reference .internal}
  - [References](#sac.xhtml_references){#sac.xhtml_id15 .reference
    .internal}
    - [Relevant Papers](#sac.xhtml_relevant-papers){#sac.xhtml_id16
      .reference .internal}
    - [Other Public
      Implementations](#sac.xhtml_other-public-implementations){#sac.xhtml_id17
      .reference .internal}
:::

::::::::::::::::::::::::::::: {#sac.xhtml_background .section}
## [Background](#sac.xhtml_id3){.toc-backref}

(Previously: [Background for TD3](td3.html_background){.reference
.external})

Soft Actor Critic (SAC) is an algorithm that optimizes a stochastic
policy in an off-policy way, forming a bridge between stochastic policy
optimization and DDPG-style approaches. It isn't a direct successor to
TD3 (having been published roughly concurrently), but it incorporates
the clipped double-Q trick, and due to the inherent stochasticity of the
policy in SAC, it also winds up benefiting from something like target
policy smoothing.

A central feature of SAC is **entropy regularization.** The policy is
trained to maximize a trade-off between expected return and
[entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)){.reference
.external}[
\[https://en.wikipedia.org/wiki/Entropy\_(information_theory)\]]{.link-target},
a measure of randomness in the policy. This has a close connection to
the exploration-exploitation trade-off: increasing entropy results in
more exploration, which can accelerate learning later on. It can also
prevent the policy from prematurely converging to a bad local optimum.

::: {#sac.xhtml_quick-facts .section}
### [Quick Facts](#sac.xhtml_id4){.toc-backref}

- SAC is an off-policy algorithm.
- The version of SAC implemented here can only be used for environments
  with continuous action spaces.
- An alternate version of SAC, which slightly changes the policy update
  rule, can be implemented to handle discrete action spaces.
- The Spinning Up implementation of SAC does not support
  parallelization.
:::

::::::::::::::::::::::: {#sac.xhtml_key-equations .section}
### [Key Equations](#sac.xhtml_id5){.toc-backref}

To explain Soft Actor Critic, we first have to introduce the
entropy-regularized reinforcement learning setting. In
entropy-regularized RL, there are slightly-different equations for value
functions.

:::::::::: {#sac.xhtml_entropy-regularized-reinforcement-learning .section}
#### [Entropy-Regularized Reinforcement Learning](#sac.xhtml_id6){.toc-backref}

Entropy is a quantity which, roughly speaking, says how random a random
variable is. If a coin is weighted so that it almost always comes up
heads, it has low entropy; if it's evenly weighted and has a half chance
of either outcome, it has high entropy.

Let
![x](_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg){.math}
be a random variable with probability mass or density function
![P](_images/math/4204ba416334e663d7bd7c6457d737ba3cbbfe46.svg){.math}.
The entropy
![H](_images/math/bf6bcb1745aeab36cdc185e9f75bbfd3998352ce.svg){.math}
of
![x](_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg){.math}
is computed from its distribution
![P](_images/math/4204ba416334e663d7bd7c6457d737ba3cbbfe46.svg){.math}
according to

::: math
![H(P) = \\underE{x \\sim P}{-\\log
P(x)}.](_images/math/1bf89d5228652e14d82657fe9f1499b136f54094.svg)
:::

In entropy-regularized reinforcement learning, the agent gets a bonus
reward at each time step proportional to the entropy of the policy at
that timestep. This changes [the RL
problem](rl_intro.html_the-rl-problem){.reference .external} to:

::: math
![\\pi\^\* = \\arg \\max\_{\\pi} \\underE{\\tau \\sim \\pi}{
\\sum\_{t=0}\^{\\infty} \\gamma\^t \\bigg( R(s_t, a_t, s\_{t+1}) +
\\alpha H\\left(\\pi(\\cdot\|s_t)\\right)
\\bigg)},](_images/math/b86bf499707114c8789946df649871c5b9185b9d.svg)
:::

where ![\\alpha \>
0](_images/math/900375490edee0019a5c54a311bf91de801a1642.svg){.math} is
the trade-off coefficient. (Note: we're assuming an infinite-horizon
discounted setting here, and we'll do the same for the rest of this
page.) We can now define the slightly-different value functions in this
setting.
![V\^{\\pi}](_images/math/fbed8ae629f7512710c5352ca50e8f629d7f34e4.svg){.math}
is changed to include the entropy bonuses from every timestep:

::: math
![V\^{\\pi}(s) = \\underE{\\tau \\sim \\pi}{ \\left.
\\sum\_{t=0}\^{\\infty} \\gamma\^t \\bigg( R(s_t, a_t, s\_{t+1}) +
\\alpha H\\left(\\pi(\\cdot\|s_t)\\right) \\bigg) \\right\| s_0 =
s}](_images/math/dda9cebd308c7fe5313f6bf4cbce8d15af046279.svg)
:::

![Q\^{\\pi}](_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg){.math}
is changed to include the entropy bonuses from every timestep *except
the first*:

::: math
![Q\^{\\pi}(s,a) = \\underE{\\tau \\sim \\pi}{ \\left.
\\sum\_{t=0}\^{\\infty} \\gamma\^t R(s_t, a_t, s\_{t+1}) + \\alpha
\\sum\_{t=1}\^{\\infty} \\gamma\^t
H\\left(\\pi(\\cdot\|s_t)\\right)\\right\| s_0 = s, a_0 =
a}](_images/math/3c1b1d100a914b01d2f537fd11bdd1159921cad2.svg)
:::

With these definitions,
![V\^{\\pi}](_images/math/fbed8ae629f7512710c5352ca50e8f629d7f34e4.svg){.math}
and
![Q\^{\\pi}](_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg){.math}
are connected by:

::: math
![V\^{\\pi}(s) = \\underE{a \\sim \\pi}{Q\^{\\pi}(s,a)} + \\alpha
H\\left(\\pi(\\cdot\|s)\\right)](_images/math/46d0852616c131f3d5aa2d1798328141904a764d.svg)
:::

and the Bellman equation for
![Q\^{\\pi}](_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg){.math}
is

::: math
![Q\^{\\pi}(s,a) &= \\underE{s\' \\sim P \\\\ a\' \\sim
\\pi}{R(s,a,s\') + \\gamma\\left(Q\^{\\pi}(s\',a\') + \\alpha
H\\left(\\pi(\\cdot\|s\')\\right) \\right)} \\\\ &= \\underE{s\' \\sim
P}{R(s,a,s\') + \\gamma
V\^{\\pi}(s\')}.](_images/math/8010672f1e8269ce985f901728e7224faa07731e.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

The way we've set up the value functions in the entropy-regularized
setting is a little bit arbitrary, and actually we could have done it
differently (eg make
![Q\^{\\pi}](_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg){.math}
include the entropy bonus at the first timestep). The choice of
definition may vary slightly across papers on the subject.
:::
::::::::::

:::::::::::::: {#sac.xhtml_id1 .section}
#### [Soft Actor-Critic](#sac.xhtml_id7){.toc-backref}

SAC concurrently learns a policy
![\\pi\_{\\theta}](_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg){.math}
and two Q-functions ![Q\_{\\phi_1},
Q\_{\\phi_2}](_images/math/a4f90f64839041d3c84ac2dde832e76f9d6db7b6.svg){.math}.
There are two variants of SAC that are currently standard: one that uses
a fixed entropy regularization coefficient
![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math},
and another that enforces an entropy constraint by varying
![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math}
over the course of training. For simplicity, Spinning Up makes use of
the version with a fixed entropy regularization coefficient, but the
entropy-constrained variant is generally preferred by practitioners.

::: {.admonition-you-should-know .admonition}
You Should Know

The SAC algorithm has changed a little bit over time. An older version
of SAC also learns a value function
![V\_{\\psi}](_images/math/f8b8aa6de09a776f6aa37138d773730ba9e623c7.svg){.math}
in addition to the Q-functions; this page will focus on the modern
version that omits the extra value function.
:::

**Learning Q.** The Q-functions are learned in a similar way to TD3, but
with a few key differences.

First, what's similar?

1.  Like in TD3, both Q-functions are learned with MSBE minimization, by
    regressing to a single shared target.
2.  Like in TD3, the shared target is computed using target Q-networks,
    and the target Q-networks are obtained by polyak averaging the
    Q-network parameters over the course of training.
3.  Like in TD3, the shared target makes use of the **clipped double-Q**
    trick.

What's different?

1.  Unlike in TD3, the target also includes a term that comes from SAC's
    use of entropy regularization.
2.  Unlike in TD3, the next-state actions used in the target come from
    the **current policy** instead of a target policy.
3.  Unlike in TD3, there is no explicit target policy smoothing. TD3
    trains a deterministic policy, and so it accomplishes smoothing by
    adding random noise to the next-state actions. SAC trains a
    stochastic policy, and so the noise from that stochasticity is
    sufficient to get a similar effect.

Before we give the final form of the Q-loss, let's take a moment to
discuss how the contribution from entropy regularization comes in. We'll
start by taking our recursive Bellman equation for the
entropy-regularized
![Q\^{\\pi}](_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg){.math}
from earlier, and rewriting it a little bit by using the definition of
entropy:

::: math
![Q\^{\\pi}(s,a) &= \\underE{s\' \\sim P \\\\ a\' \\sim
\\pi}{R(s,a,s\') + \\gamma\\left(Q\^{\\pi}(s\',a\') + \\alpha
H\\left(\\pi(\\cdot\|s\')\\right) \\right)} \\\\ &= \\underE{s\' \\sim P
\\\\ a\' \\sim \\pi}{R(s,a,s\') + \\gamma\\left(Q\^{\\pi}(s\',a\') -
\\alpha \\log \\pi(a\'\|s\')
\\right)}](_images/math/1557c0c7205cbb2928eb3305b2df207e79bc70fe.svg)
:::

The RHS is an expectation over next states (which come from the replay
buffer) and next actions (which come from the current policy, and
**not** the replay buffer). Since it's an expectation, we can
approximate it with samples:

::: math
![Q\^{\\pi}(s,a) &\\approx r +
\\gamma\\left(Q\^{\\pi}(s\',\\tilde{a}\') - \\alpha \\log
\\pi(\\tilde{a}\'\|s\') \\right), \\;\\;\\;\\;\\; \\tilde{a}\' \\sim
\\pi(\\cdot\|s\').](_images/math/aa74b233b0820048f096edb81f0b3321730d71a8.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

We switch next action notation to
![\\tilde{a}\'](_images/math/f1523bc2b6ea2ca935e184990079e62313c3321f.svg){.math},
instead of
![a\'](_images/math/3200e4a6949b896a76b0e83a40edb16602433fd0.svg){.math},
to highlight that the next actions have to be sampled fresh from the
policy (whereas by contrast,
![r](_images/math/5a3ac7a81362ac174d142bab198b4bd5a9e2dcee.svg){.math}
and
![s\'](_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg){.math}
should come from the replay buffer).
:::

SAC sets up the MSBE loss for each Q-function using this kind of sample
approximation for the target. The only thing still undetermined here is
which Q-function gets used to compute the sample backup: like TD3, SAC
uses the clipped double-Q trick, and takes the minimum Q-value between
the two Q approximators.

Putting it all together, the loss functions for the Q-networks in SAC
are:

::: math
![L(\\phi_i, {\\mathcal D}) = \\underset{(s,a,r,s\',d) \\sim {\\mathcal
D}}{{\\mathrm E}}\\left\[ \\Bigg( Q\_{\\phi_i}(s,a) - y(r,s\',d)
\\Bigg)\^2
\\right\],](_images/math/0bd81fc5d1cb03a33d6477f5ff10ed879ea393ec.svg)
:::

where the target is given by

::: math
![y(r, s\', d) = r + \\gamma (1 - d) \\left( \\min\_{j=1,2}
Q\_{\\phi\_{\\text{targ},j}}(s\', \\tilde{a}\') - \\alpha \\log
\\pi\_{\\theta}(\\tilde{a}\'\|s\') \\right), \\;\\;\\;\\;\\;
\\tilde{a}\' \\sim
\\pi\_{\\theta}(\\cdot\|s\').](_images/math/fc03ff9e9f818fb31b7724907e2b43d5101d2ab8.svg)
:::

**Learning the Policy.** The policy should, in each state, act to
maximize the expected future return plus expected future entropy. That
is, it should maximize
![V\^{\\pi}(s)](_images/math/a81303323c25fc13cd0652ca46d7596276e5cb7e.svg){.math},
which we expand out into

::: math
![V\^{\\pi}(s) &= \\underE{a \\sim \\pi}{Q\^{\\pi}(s,a)} + \\alpha
H\\left(\\pi(\\cdot\|s)\\right) \\\\ &= \\underE{a \\sim
\\pi}{Q\^{\\pi}(s,a) - \\alpha \\log
\\pi(a\|s)}.](_images/math/5ff58df73caef07f6309a1460fe57b1c34e3b374.svg)
:::

The way we optimize the policy makes use of the **reparameterization
trick**, in which a sample from
![\\pi\_{\\theta}(\\cdot\|s)](_images/math/e57f13375048b8f7343f9066b6553bc282afa326.svg){.math}
is drawn by computing a deterministic function of state, policy
parameters, and independent noise. To illustrate: following the authors
of the SAC paper, we use a squashed Gaussian policy, which means that
samples are obtained according to

::: math
![\\tilde{a}\_{\\theta}(s, \\xi) = \\tanh\\left( \\mu\_{\\theta}(s) +
\\sigma\_{\\theta}(s) \\odot \\xi \\right), \\;\\;\\;\\;\\; \\xi \\sim
\\mathcal{N}(0,
I).](_images/math/dac3ddc2ea35e8233b8bc0a905273712793ab1cb.svg)
:::

::: {.admonition-you-should-know .admonition}
You Should Know

This policy has two key differences from the policies we use in the
other policy optimization algorithms:

**1. The squashing function.** The
![\\tanh](_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg){.math}
in the SAC policy ensures that actions are bounded to a finite range.
This is absent in the VPG, TRPO, and PPO policies. It also changes the
distribution: before the
![\\tanh](_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg){.math}
the SAC policy is a factored Gaussian like the other algorithms'
policies, but after the
![\\tanh](_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg){.math}
it is not. (You can still compute the log-probabilities of actions in
closed form, though: see the paper appendix for details.)

**2. The way standard deviations are parameterized.** In VPG, TRPO, and
PPO, we represent the log std devs with state-independent parameter
vectors. In SAC, we represent the log std devs as outputs from the
neural network, meaning that they depend on state in a complex way. SAC
with state-independent log std devs, in our experience, did not work.
(Can you think of why? Or better yet: run an experiment to verify?)
:::

The reparameterization trick allows us to rewrite the expectation over
actions (which contains a pain point: the distribution depends on the
policy parameters) into an expectation over noise (which removes the
pain point: the distribution now has no dependence on parameters):

::: math
![\\underE{a \\sim \\pi\_{\\theta}}{Q\^{\\pi\_{\\theta}}(s,a) - \\alpha
\\log \\pi\_{\\theta}(a\|s)} = \\underE{\\xi \\sim
\\mathcal{N}}{Q\^{\\pi\_{\\theta}}(s,\\tilde{a}\_{\\theta}(s,\\xi)) -
\\alpha \\log
\\pi\_{\\theta}(\\tilde{a}\_{\\theta}(s,\\xi)\|s)}](_images/math/5713f9f99ea3532e3cbde89eac91328eb8549409.svg)
:::

To get the policy loss, the final step is that we need to substitute
![Q\^{\\pi\_{\\theta}}](_images/math/9c39112fd52e66e3062f93c502ade0eb9381d957.svg){.math}
with one of our function approximators. Unlike in TD3, which uses
![Q\_{\\phi_1}](_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg){.math}
(just the first Q approximator), SAC uses ![\\min\_{j=1,2}
Q\_{\\phi_j}](_images/math/e5d14ed1b7128d64d43af73b7d0b189c6afda8ec.svg){.math}
(the minimum of the two Q approximators). The policy is thus optimized
according to

::: math
![\\max\_{\\theta} \\underE{s \\sim \\mathcal{D} \\\\ \\xi \\sim
\\mathcal{N}}{\\min\_{j=1,2}
Q\_{\\phi_j}(s,\\tilde{a}\_{\\theta}(s,\\xi)) - \\alpha \\log
\\pi\_{\\theta}(\\tilde{a}\_{\\theta}(s,\\xi)\|s)},](_images/math/bdbe4cabbba4687b310d99e8fa67ed314339bd31.svg)
:::

which is almost the same as the DDPG and TD3 policy optimization, except
for the min-double-Q trick, the stochasticity, and the entropy term.
::::::::::::::
:::::::::::::::::::::::

:::: {#sac.xhtml_exploration-vs-exploitation .section}
### [Exploration vs. Exploitation](#sac.xhtml_id8){.toc-backref}

SAC trains a stochastic policy with entropy regularization, and explores
in an on-policy way. The entropy regularization coefficient
![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math}
explicitly controls the explore-exploit tradeoff, with higher
![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math}
corresponding to more exploration, and lower
![\\alpha](_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg){.math}
corresponding to more exploitation. The right coefficient (the one which
leads to the stablest / highest-reward learning) may vary from
environment to environment, and could require careful tuning.

At test time, to see how well the policy exploits what it has learned,
we remove stochasticity and use the mean action instead of a sample from
the distribution. This tends to improve performance over the original
stochastic policy.

::: {.admonition-you-should-know .admonition}
You Should Know

Our SAC implementation uses a trick to improve exploration at the start
of training. For a fixed number of steps at the beginning (set with the
[`start_steps`{.docutils .literal}]{.pre} keyword argument), the agent
takes actions which are sampled from a uniform random distribution over
valid actions. After that, it returns to normal SAC exploration.
:::
::::

:::: {#sac.xhtml_pseudocode .section}
### [Pseudocode](#sac.xhtml_id9){.toc-backref}

::: math
![\\begin{algorithm}\[H\] \\caption{Soft Actor-Critic} \\label{alg1}
\\begin{algorithmic}\[1\] \\STATE Input: initial policy parameters
\$\\theta\$, Q-function parameters \$\\phi_1\$, \$\\phi_2\$, empty
replay buffer \$\\mathcal{D}\$ \\STATE Set target parameters equal to
main parameters \$\\phi\_{\\text{targ},1} \\leftarrow \\phi_1\$,
\$\\phi\_{\\text{targ},2} \\leftarrow \\phi_2\$ \\REPEAT \\STATE Observe
state \$s\$ and select action \$a \\sim \\pi\_{\\theta}(\\cdot\|s)\$
\\STATE Execute \$a\$ in the environment \\STATE Observe next state
\$s\'\$, reward \$r\$, and done signal \$d\$ to indicate whether \$s\'\$
is terminal \\STATE Store \$(s,a,r,s\',d)\$ in replay buffer
\$\\mathcal{D}\$ \\STATE If \$s\'\$ is terminal, reset environment
state. \\IF{it\'s time to update} \\FOR{\$j\$ in range(however many
updates)} \\STATE Randomly sample a batch of transitions, \$B = \\{
(s,a,r,s\',d) \\}\$ from \$\\mathcal{D}\$ \\STATE Compute targets for
the Q functions: \\begin{align\*} y (r,s\',d) &= r + \\gamma (1-d)
\\left(\\min\_{i=1,2} Q\_{\\phi\_{\\text{targ}, i}} (s\',
\\tilde{a}\') - \\alpha \\log
\\pi\_{\\theta}(\\tilde{a}\'\|s\')\\right), && \\tilde{a}\' \\sim
\\pi\_{\\theta}(\\cdot\|s\') \\end{align\*} \\STATE Update Q-functions
by one step of gradient descent using \\begin{align\*} &
\\nabla\_{\\phi_i} \\frac{1}{\|B\|}\\sum\_{(s,a,r,s\',d) \\in B} \\left(
Q\_{\\phi_i}(s,a) - y(r,s\',d) \\right)\^2 && \\text{for } i=1,2
\\end{align\*} \\STATE Update policy by one step of gradient ascent
using \\begin{equation\*} \\nabla\_{\\theta} \\frac{1}{\|B\|}\\sum\_{s
\\in B} \\Big(\\min\_{i=1,2} Q\_{\\phi_i}(s, \\tilde{a}\_{\\theta}(s)) -
\\alpha \\log \\pi\_{\\theta} \\left(\\left. \\tilde{a}\_{\\theta}(s)
\\right\| s\\right) \\Big), \\end{equation\*} where
\$\\tilde{a}\_{\\theta}(s)\$ is a sample from
\$\\pi\_{\\theta}(\\cdot\|s)\$ which is differentiable wrt \$\\theta\$
via the reparametrization trick. \\STATE Update target networks with
\\begin{align\*} \\phi\_{\\text{targ},i} &\\leftarrow \\rho
\\phi\_{\\text{targ}, i} + (1-\\rho) \\phi_i && \\text{for } i=1,2
\\end{align\*} \\ENDFOR \\ENDIF \\UNTIL{convergence} \\end{algorithmic}
\\end{algorithm}](_images/math/c01f4994ae4aacf299a6b3ceceedfe0a14d4b874.svg)
:::
::::
:::::::::::::::::::::::::::::

:::::::::: {#sac.xhtml_documentation .section}
## [Documentation](#sac.xhtml_id10){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow
implementations of SAC in Spinning Up. They have nearly identical
function calls and docstrings, except for details relating to model
construction. However, we include both full docstrings for completeness.
:::

::: {#sac.xhtml_documentation-pytorch-version .section}
### [Documentation: PyTorch Version](#sac.xhtml_id11){.toc-backref}

`spinup.`{.descclassname}`sac_pytorch`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<MagicMock spec=\'str\' id=\'140679788317944\'\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *lr=0.001*, *alpha=0.2*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Soft Actor-Critic (SAC)

    +-------------+---------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment   |
    |             |   must satisfy the OpenAI Gym API.                                                    |
    |             |                                                                                       |
    |             | - **actor_critic** --                                                                 |
    |             |                                                                                       |
    |             |   The constructor method for a PyTorch Module with an [`act`{.docutils                |
    |             |   .literal}]{.pre} method, a [`pi`{.docutils .literal}]{.pre} module, a               |
    |             |   [`q1`{.docutils .literal}]{.pre} module, and a [`q2`{.docutils .literal}]{.pre}     |
    |             |   module. The [`act`{.docutils .literal}]{.pre} method and [`pi`{.docutils            |
    |             |   .literal}]{.pre} module should accept batches of observations as inputs, and        |
    |             |   [`q1`{.docutils .literal}]{.pre} and [`q2`{.docutils .literal}]{.pre} should accept |
    |             |   a batch of observations and a batch of actions as inputs. When called,              |
    |             |   [`act`{.docutils .literal}]{.pre}, [`q1`{.docutils .literal}]{.pre}, and            |
    |             |   [`q2`{.docutils .literal}]{.pre} should return:                                     |
    |             |                                                                                       |
    |             |   +------------------+--------------+--------------------------------------------+    |
    |             |   | Call             | Output Shape | Description                                |    |
    |             |   +==================+==============+============================================+    |
    |             |   | [`act`{.docutils | (batch,      | ::::: {.first .last .line-block}           |    |
    |             |   | .literal}]{.pre} | act_dim)     | ::: line                                   |    |
    |             |   |                  |              | Numpy array of actions for each            |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | observation.                               |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              | :::::                                      |    |
    |             |   +------------------+--------------+--------------------------------------------+    |
    |             |   | [`q1`{.docutils  | (batch,)     | ::::::: {.first .last .line-block}         |    |
    |             |   | .literal}]{.pre} |              | ::: line                                   |    |
    |             |   |                  |              | Tensor containing one current estimate     |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | of Q\* for the provided observations       |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | and actions. (Critical: make sure to       |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | flatten this!)                             |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              | :::::::                                    |    |
    |             |   +------------------+--------------+--------------------------------------------+    |
    |             |   | [`q2`{.docutils  | (batch,)     | ::::::: {.first .last .line-block}         |    |
    |             |   | .literal}]{.pre} |              | ::: line                                   |    |
    |             |   |                  |              | Tensor containing the other current        |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | estimate of Q\* for the provided           |    |
    |             |   |                  |              | observations                               |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | and actions. (Critical: make sure to       |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              |                                            |    |
    |             |   |                  |              | ::: line                                   |    |
    |             |   |                  |              | flatten this!)                             |    |
    |             |   |                  |              | :::                                        |    |
    |             |   |                  |              | :::::::                                    |    |
    |             |   +------------------+--------------+--------------------------------------------+    |
    |             |                                                                                       |
    |             |   Calling [`pi`{.docutils .literal}]{.pre} should return:                             |
    |             |                                                                                       |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | Symbol               | Shape         | Description                              | |
    |             |   +======================+===============+==========================================+ |
    |             |   | [`a`{.docutils       | (batch,       | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre}     | act_dim)      | ::: line                                 | |
    |             |   |                      |               | Tensor containing actions from policy    | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | given observations.                      | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | :::::                                    | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | [`logp_pi`{.docutils | (batch,)      | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |               | ::: line                                 | |
    |             |   |                      |               | Tensor containing log probabilities of   | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | actions in [`a`{.docutils                | |
    |             |   |                      |               | .literal}]{.pre}. Importantly: gradients | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | should be able to flow back into         | |
    |             |   |                      |               | [`a`{.docutils .literal}]{.pre}.         | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | ::::::                                   | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |                                                                                       |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the ActorCritic object you     |
    |             |   provided to SAC.                                                                    |
    |             |                                                                                       |
    |             | - **seed** (*int*) -- Seed for random number generators.                              |
    |             |                                                                                       |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs)  |
    |             |   for the agent and the environment in each epoch.                                    |
    |             |                                                                                       |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                      |
    |             |                                                                                       |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                         |
    |             |                                                                                       |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                   |
    |             |                                                                                       |
    |             | - **polyak** (*float*) --                                                             |
    |             |                                                                                       |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks are   |
    |             |   updated towards main networks according to:                                         |
    |             |                                                                                       |
    |             |   ::: math                                                                            |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)     |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)                 |
    |             |   :::                                                                                 |
    |             |                                                                                       |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math} is |
    |             |   polyak. (Always between 0 and 1, usually close to 1.)                               |
    |             |                                                                                       |
    |             | - **lr** (*float*) -- Learning rate (used for both policy and value learning).        |
    |             |                                                                                       |
    |             | - **alpha** (*float*) -- Entropy regularization coefficient. (Equivalent to inverse   |
    |             |   of reward scale in the original SAC paper.)                                         |
    |             |                                                                                       |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                   |
    |             |                                                                                       |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,     |
    |             |   before running real policy. Helps exploration.                                      |
    |             |                                                                                       |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before starting   |
    |             |   to do gradient descent updates. Ensures replay buffer is full enough for useful     |
    |             |   updates.                                                                            |
    |             |                                                                                       |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse between   |
    |             |   gradient descent updates. Note: Regardless of how long you wait between updates,    |
    |             |   the ratio of env steps to gradient steps is locked to 1.                            |
    |             |                                                                                       |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic       |
    |             |   policy at the end of each epoch.                                                    |
    |             |                                                                                       |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.         |
    |             |                                                                                       |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                         |
    |             |                                                                                       |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the     |
    |             |   current policy and value function.                                                  |
    +-------------+---------------------------------------------------------------------------------------+
:::

::::: {#sac.xhtml_saved-model-contents-pytorch-version .section}
### [Saved Model Contents: PyTorch Version](#sac.xhtml_id12){.toc-backref}

The PyTorch saved model can be loaded with [`ac`{.docutils
.literal}]{.pre}` `{.docutils .literal}[`=`{.docutils
.literal}]{.pre}` `{.docutils
.literal}[`torch.load('path/to/model.pt')`{.docutils .literal}]{.pre},
yielding an actor-critic object ([`ac`{.docutils .literal}]{.pre}) that
has the properties described in the docstring for
[`sac_pytorch`{.docutils .literal}]{.pre}.

You can get actions from this model with

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::

::: {#sac.xhtml_documentation-tensorflow-version .section}
### [Documentation: Tensorflow Version](#sac.xhtml_id13){.toc-backref}

`spinup.`{.descclassname}`sac_tf1`{.descname}[(]{.sig-paren}*env_fn*, *actor_critic=\<function mlp_actor_critic\>*, *ac_kwargs={}*, *seed=0*, *steps_per_epoch=4000*, *epochs=100*, *replay_size=1000000*, *gamma=0.99*, *polyak=0.995*, *lr=0.001*, *alpha=0.2*, *batch_size=100*, *start_steps=10000*, *update_after=1000*, *update_every=50*, *num_test_episodes=10*, *max_ep_len=1000*, *logger_kwargs={}*, *save_freq=1*[)]{.sig-paren}

:   Soft Actor-Critic (SAC)

    +-------------+---------------------------------------------------------------------------------------+
    | Parameters: | - **env_fn** -- A function which creates a copy of the environment. The environment   |
    |             |   must satisfy the OpenAI Gym API.                                                    |
    |             |                                                                                       |
    |             | - **actor_critic** --                                                                 |
    |             |                                                                                       |
    |             |   A function which takes in placeholder symbols for state, [`x_ph`{.docutils          |
    |             |   .literal}]{.pre}, and action, [`a_ph`{.docutils .literal}]{.pre}, and returns the   |
    |             |   main outputs from the agent's Tensorflow computation graph:                         |
    |             |                                                                                       |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | Symbol               | Shape         | Description                              | |
    |             |   +======================+===============+==========================================+ |
    |             |   | [`mu`{.docutils      | (batch,       | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre}     | act_dim)      | ::: line                                 | |
    |             |   |                      |               | Computes mean actions from policy        | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | given states.                            | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | :::::                                    | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | [`pi`{.docutils      | (batch,       | ::::: {.first .last .line-block}         | |
    |             |   | .literal}]{.pre}     | act_dim)      | ::: line                                 | |
    |             |   |                      |               | Samples actions from policy given        | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | states.                                  | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | :::::                                    | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | [`logp_pi`{.docutils | (batch,)      | :::::::: {.first .last .line-block}      | |
    |             |   | .literal}]{.pre}     |               | ::: line                                 | |
    |             |   |                      |               | Gives log probability, according to      | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | the policy, of the action sampled by     | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | [`pi`{.docutils .literal}]{.pre}.        | |
    |             |   |                      |               | Critical: must be differentiable         | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | with respect to policy parameters all    | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | the way through action sampling.         | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | ::::::::                                 | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | [`q1`{.docutils      | (batch,)      | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |               | ::: line                                 | |
    |             |   |                      |               | Gives one estimate of Q\* for            | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | states in [`x_ph`{.docutils              | |
    |             |   |                      |               | .literal}]{.pre} and actions in          | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | [`a_ph`{.docutils .literal}]{.pre}.      | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | ::::::                                   | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |   | [`q2`{.docutils      | (batch,)      | :::::: {.first .last .line-block}        | |
    |             |   | .literal}]{.pre}     |               | ::: line                                 | |
    |             |   |                      |               | Gives another estimate of Q\* for        | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | states in [`x_ph`{.docutils              | |
    |             |   |                      |               | .literal}]{.pre} and actions in          | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               |                                          | |
    |             |   |                      |               | ::: line                                 | |
    |             |   |                      |               | [`a_ph`{.docutils .literal}]{.pre}.      | |
    |             |   |                      |               | :::                                      | |
    |             |   |                      |               | ::::::                                   | |
    |             |   +----------------------+---------------+------------------------------------------+ |
    |             |                                                                                       |
    |             | - **ac_kwargs** (*dict*) -- Any kwargs appropriate for the actor_critic function you  |
    |             |   provided to SAC.                                                                    |
    |             |                                                                                       |
    |             | - **seed** (*int*) -- Seed for random number generators.                              |
    |             |                                                                                       |
    |             | - **steps_per_epoch** (*int*) -- Number of steps of interaction (state-action pairs)  |
    |             |   for the agent and the environment in each epoch.                                    |
    |             |                                                                                       |
    |             | - **epochs** (*int*) -- Number of epochs to run and train agent.                      |
    |             |                                                                                       |
    |             | - **replay_size** (*int*) -- Maximum length of replay buffer.                         |
    |             |                                                                                       |
    |             | - **gamma** (*float*) -- Discount factor. (Always between 0 and 1.)                   |
    |             |                                                                                       |
    |             | - **polyak** (*float*) --                                                             |
    |             |                                                                                       |
    |             |   Interpolation factor in polyak averaging for target networks. Target networks are   |
    |             |   updated towards main networks according to:                                         |
    |             |                                                                                       |
    |             |   ::: math                                                                            |
    |             |   ![\\theta\_{\\text{targ}} \\leftarrow \\rho \\theta\_{\\text{targ}} + (1-\\rho)     |
    |             |   \\theta](_images/math/ea6c5fdb8bb78fe30797537bbb28553b9a7706ef.svg)                 |
    |             |   :::                                                                                 |
    |             |                                                                                       |
    |             |   where ![\\rho](_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg){.math} is |
    |             |   polyak. (Always between 0 and 1, usually close to 1.)                               |
    |             |                                                                                       |
    |             | - **lr** (*float*) -- Learning rate (used for both policy and value learning).        |
    |             |                                                                                       |
    |             | - **alpha** (*float*) -- Entropy regularization coefficient. (Equivalent to inverse   |
    |             |   of reward scale in the original SAC paper.)                                         |
    |             |                                                                                       |
    |             | - **batch_size** (*int*) -- Minibatch size for SGD.                                   |
    |             |                                                                                       |
    |             | - **start_steps** (*int*) -- Number of steps for uniform-random action selection,     |
    |             |   before running real policy. Helps exploration.                                      |
    |             |                                                                                       |
    |             | - **update_after** (*int*) -- Number of env interactions to collect before starting   |
    |             |   to do gradient descent updates. Ensures replay buffer is full enough for useful     |
    |             |   updates.                                                                            |
    |             |                                                                                       |
    |             | - **update_every** (*int*) -- Number of env interactions that should elapse between   |
    |             |   gradient descent updates. Note: Regardless of how long you wait between updates,    |
    |             |   the ratio of env steps to gradient steps is locked to 1.                            |
    |             |                                                                                       |
    |             | - **num_test_episodes** (*int*) -- Number of episodes to test the deterministic       |
    |             |   policy at the end of each epoch.                                                    |
    |             |                                                                                       |
    |             | - **max_ep_len** (*int*) -- Maximum length of trajectory / episode / rollout.         |
    |             |                                                                                       |
    |             | - **logger_kwargs** (*dict*) -- Keyword args for EpochLogger.                         |
    |             |                                                                                       |
    |             | - **save_freq** (*int*) -- How often (in terms of gap between epochs) to save the     |
    |             |   current policy and value function.                                                  |
    +-------------+---------------------------------------------------------------------------------------+
:::

::: {#sac.xhtml_saved-model-contents-tensorflow-version .section}
### [Saved Model Contents: Tensorflow Version](#sac.xhtml_id14){.toc-backref}

The computation graph saved by the logger includes:

  -----------------------------------------------------------------------------------
  Key                Value
  ------------------ ----------------------------------------------------------------
  [`x`{.docutils     Tensorflow placeholder for state input.
  .literal}]{.pre}   

  [`a`{.docutils     Tensorflow placeholder for action input.
  .literal}]{.pre}   

  [`mu`{.docutils    Deterministically computes mean action from the agent, given
  .literal}]{.pre}   states in [`x`{.docutils .literal}]{.pre}.

  [`pi`{.docutils    Samples an action from the agent, conditioned on states in
  .literal}]{.pre}   [`x`{.docutils .literal}]{.pre}.

  [`q1`{.docutils    Gives one action-value estimate for states in [`x`{.docutils
  .literal}]{.pre}   .literal}]{.pre} and actions in [`a`{.docutils .literal}]{.pre}.

  [`q2`{.docutils    Gives the other action-value estimate for states in
  .literal}]{.pre}   [`x`{.docutils .literal}]{.pre} and actions in [`a`{.docutils
                     .literal}]{.pre}.

  [`v`{.docutils     Gives the value estimate for states in [`x`{.docutils
  .literal}]{.pre}   .literal}]{.pre}.
  -----------------------------------------------------------------------------------

This saved model can be accessed either by

- running the trained policy with the
  [test_policy.py](saving_and_loading.html_loading-and-running-trained-policies){.reference
  .external} tool,
- or loading the whole saved graph into a program with
  [restore_tf_graph](logger.html_spinup.utils.logx.restore_tf_graph){.reference
  .external}.

Note: for SAC, the correct evaluation policy is given by [`mu`{.docutils
.literal}]{.pre} and not by [`pi`{.docutils .literal}]{.pre}. The policy
[`pi`{.docutils .literal}]{.pre} may be thought of as the exploration
policy, while [`mu`{.docutils .literal}]{.pre} is the exploitation
policy.
:::
::::::::::

::::: {#sac.xhtml_references .section}
## [References](#sac.xhtml_id15){.toc-backref}

::: {#sac.xhtml_relevant-papers .section}
### [Relevant Papers](#sac.xhtml_id16){.toc-backref}

- [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement
  Learning with a Stochastic
  Actor](https://arxiv.org/abs/1801.01290){.reference .external}[
  \[https://arxiv.org/abs/1801.01290\]]{.link-target}, Haarnoja et al,
  2018
- [Soft Actor-Critic Algorithms and
  Applications](https://arxiv.org/abs/1812.05905){.reference .external}[
  \[https://arxiv.org/abs/1812.05905\]]{.link-target}, Haarnoja et al,
  2018
- [Learning to Walk via Deep Reinforcement
  Learning](https://arxiv.org/abs/1812.11103){.reference .external}[
  \[https://arxiv.org/abs/1812.11103\]]{.link-target}, Haarnoja et al,
  2018
:::

::: {#sac.xhtml_other-public-implementations .section}
### [Other Public Implementations](#sac.xhtml_id17){.toc-backref}

- [SAC release repo](https://github.com/haarnoja/sac){.reference
  .external}[ \[https://github.com/haarnoja/sac\]]{.link-target}
  (original "official" codebase)
- [Softlearning
  repo](https://github.com/rail-berkeley/softlearning){.reference
  .external}[
  \[https://github.com/rail-berkeley/softlearning\]]{.link-target}
  (current "official" codebase)
- [Yarats and Kostrikov
  repo](https://github.com/denisyarats/pytorch_sac){.reference
  .external}[
  \[https://github.com/denisyarats/pytorch_sac\]]{.link-target}
:::
:::::
::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

[]{#logger.xhtml}

::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::: {#logger.xhtml_logger .section}
# [Logger](#logger.xhtml_id2){.toc-backref}

::: {#logger.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Logger](#logger.xhtml_logger){#logger.xhtml_id2 .reference .internal}
  - [Using a Logger](#logger.xhtml_using-a-logger){#logger.xhtml_id3
    .reference .internal}
    - [Examples](#logger.xhtml_examples){#logger.xhtml_id4 .reference
      .internal}
    - [Logging and
      PyTorch](#logger.xhtml_logging-and-pytorch){#logger.xhtml_id5
      .reference .internal}
    - [Logging and MPI](#logger.xhtml_logging-and-mpi){#logger.xhtml_id6
      .reference .internal}
  - [Logger Classes](#logger.xhtml_logger-classes){#logger.xhtml_id7
    .reference .internal}
  - [Loading Saved Models (PyTorch
    Only)](#logger.xhtml_loading-saved-models-pytorch-only){#logger.xhtml_id8
    .reference .internal}
  - [Loading Saved Graphs (Tensorflow
    Only)](#logger.xhtml_loading-saved-graphs-tensorflow-only){#logger.xhtml_id9
    .reference .internal}
:::

::::::::::: {#logger.xhtml_using-a-logger .section}
## [Using a Logger](#logger.xhtml_id3){.toc-backref}

Spinning Up ships with basic logging tools, implemented in the classes
[Logger](logger.html_spinup.utils.logx.Logger){.reference .external} and
[EpochLogger](logger.html_spinup.utils.logx.EpochLogger){.reference
.external}. The Logger class contains most of the basic functionality
for saving diagnostics, hyperparameter configurations, the state of a
training run, and the trained model. The EpochLogger class adds a thin
layer on top of that to make it easy to track the average, standard
deviation, min, and max value of a diagnostic over each epoch and across
MPI workers.

::: {.admonition-you-should-know .admonition}
You Should Know

All Spinning Up algorithm implementations use an EpochLogger.
:::

:::::: {#logger.xhtml_examples .section}
### [Examples](#logger.xhtml_id4){.toc-backref}

First, let's look at a simple example of how an EpochLogger keeps track
of a diagnostic value:

:::: highlight-default
::: highlight
    >>> from spinup.utils.logx import EpochLogger
    >>> epoch_logger = EpochLogger()
    >>> for i in range(10):
            epoch_logger.store(Test=i)
    >>> epoch_logger.log_tabular('Test', with_min_and_max=True)
    >>> epoch_logger.dump_tabular()
    -------------------------------------
    |     AverageTest |             4.5 |
    |         StdTest |            2.87 |
    |         MaxTest |               9 |
    |         MinTest |               0 |
    -------------------------------------
:::
::::

The [`store`{.docutils .literal}]{.pre} method is used to save all
values of [`Test`{.docutils .literal}]{.pre} to the
[`epoch_logger`{.docutils .literal}]{.pre}'s internal state. Then, when
[`log_tabular`{.docutils .literal}]{.pre} is called, it computes the
average, standard deviation, min, and max of [`Test`{.docutils
.literal}]{.pre} over all of the values in the internal state. The
internal state is wiped clean after the call to [`log_tabular`{.docutils
.literal}]{.pre} (to prevent leakage into the statistics at the next
epoch). Finally, [`dump_tabular`{.docutils .literal}]{.pre} is called to
write the diagnostics to file and to stdout.

Next, let's look at a full training procedure with the logger embedded,
to highlight configuration and model saving as well as diagnostic
logging:

::: highlight-python
+-----------------------------------+----------------------------------------------------------------------------------------------+
| ::: linenodiv                     | ::: highlight                                                                                |
|      1                            |      import numpy as np                                                                      |
|      2                            |      import tensorflow as tf                                                                 |
|      3                            |      import time                                                                             |
|      4                            |      from spinup.utils.logx import EpochLogger                                               |
|      5                            |                                                                                              |
|      6                            |                                                                                              |
|      7                            |      def mlp(x, hidden_sizes=(32,), activation=tf.tanh, output_activation=None):             |
|      8                            |          for h in hidden_sizes[:-1]:                                                         |
|      9                            |              x = tf.layers.dense(x, units=h, activation=activation)                          |
|     10                            |          return tf.layers.dense(x, units=hidden_sizes[-1], activation=output_activation)     |
|     11                            |                                                                                              |
|     12                            |                                                                                              |
|     13                            |      # Simple script for training an MLP on MNIST.                                           |
|     14                            |      def train_mnist(steps_per_epoch=100, epochs=5,                                          |
|     15                            |                      lr=1e-3, layers=2, hidden_size=64,                                      |
|     16                            |                      logger_kwargs=dict(), save_freq=1):                                     |
|     17                            |                                                                                              |
|     18                            |          logger = EpochLogger(**logger_kwargs)                                               |
|     19                            |          logger.save_config(locals())                                                        |
|     20                            |                                                                                              |
|     21                            |          # Load and preprocess MNIST data                                                    |
|     22                            |          (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()                         |
|     23                            |          x_train = x_train.reshape(-1, 28*28) / 255.0                                        |
|     24                            |                                                                                              |
|     25                            |          # Define inputs & main outputs from computation graph                               |
|     26                            |          x_ph = tf.placeholder(tf.float32, shape=(None, 28*28))                              |
|     27                            |          y_ph = tf.placeholder(tf.int32, shape=(None,))                                      |
|     28                            |          logits = mlp(x_ph, hidden_sizes=[hidden_size]*layers + [10], activation=tf.nn.relu) |
|     29                            |          predict = tf.argmax(logits, axis=1, output_type=tf.int32)                           |
|     30                            |                                                                                              |
|     31                            |          # Define loss function, accuracy, and training op                                   |
|     32                            |          y = tf.one_hot(y_ph, 10)                                                            |
|     33                            |          loss = tf.losses.softmax_cross_entropy(y, logits)                                   |
|     34                            |          acc = tf.reduce_mean(tf.cast(tf.equal(y_ph, predict), tf.float32))                  |
|     35                            |          train_op = tf.train.AdamOptimizer().minimize(loss)                                  |
|     36                            |                                                                                              |
|     37                            |          # Prepare session                                                                   |
|     38                            |          sess = tf.Session()                                                                 |
|     39                            |          sess.run(tf.global_variables_initializer())                                         |
|     40                            |                                                                                              |
|     41                            |          # Setup model saving                                                                |
|     42                            |          logger.setup_tf_saver(sess, inputs={'x': x_ph},                                     |
|     43                            |                                      outputs={'logits': logits, 'predict': predict})         |
|     44                            |                                                                                              |
|     45                            |          start_time = time.time()                                                            |
|     46                            |                                                                                              |
|     47                            |          # Run main training loop                                                            |
|     48                            |          for epoch in range(epochs):                                                         |
|     49                            |              for t in range(steps_per_epoch):                                                |
|     50                            |                  idxs = np.random.randint(0, len(x_train), 32)                               |
|     51                            |                  feed_dict = {x_ph: x_train[idxs],                                           |
|     52                            |                               y_ph: y_train[idxs]}                                           |
|     53                            |                  outs = sess.run([loss, acc, train_op], feed_dict=feed_dict)                 |
|     54                            |                  logger.store(Loss=outs[0], Acc=outs[1])                                     |
|     55                            |                                                                                              |
|     56                            |              # Save model                                                                    |
|     57                            |              if (epoch % save_freq == 0) or (epoch == epochs-1):                             |
|     58                            |                  logger.save_state(state_dict=dict(), itr=None)                              |
|     59                            |                                                                                              |
|     60                            |              # Log info about epoch                                                          |
|     61                            |              logger.log_tabular('Epoch', epoch)                                              |
|     62                            |              logger.log_tabular('Acc', with_min_and_max=True)                                |
|     63                            |              logger.log_tabular('Loss', average_only=True)                                   |
|     64                            |              logger.log_tabular('TotalGradientSteps', (epoch+1)*steps_per_epoch)             |
|     65                            |              logger.log_tabular('Time', time.time()-start_time)                              |
|     66                            |              logger.dump_tabular()                                                           |
|     67                            |                                                                                              |
|     68                            |      if __name__ == '__main__':                                                              |
|     69                            |          train_mnist()                                                                       |
| :::                               | :::                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------+
:::

In this example, observe that

- On line 19,
  [logger.save_config](logger.html_spinup.utils.logx.Logger.save_config){.reference
  .external} is used to save the hyperparameter configuration to a JSON
  file.
- On lines 42 and 43,
  [logger.setup_tf_saver](logger.html_spinup.utils.logx.Logger.setup_tf_saver){.reference
  .external} is used to prepare the logger to save the key elements of
  the computation graph.
- On line 54, diagnostics are saved to the logger's internal state via
  [logger.store](logger.html_spinup.utils.logx.EpochLogger.store){.reference
  .external}.
- On line 58, the computation graph is saved once per epoch via
  [logger.save_state](logger.html_spinup.utils.logx.Logger.save_state){.reference
  .external}.
- On lines 61-66,
  [logger.log_tabular](logger.html_spinup.utils.logx.EpochLogger.log_tabular){.reference
  .external} and
  [logger.dump_tabular](logger.html_spinup.utils.logx.Logger.dump_tabular){.reference
  .external} are used to write the epoch diagnostics to file. Note that
  the keys passed into
  [logger.log_tabular](logger.html_spinup.utils.logx.EpochLogger.log_tabular){.reference
  .external} are the same as the keys passed into
  [logger.store](logger.html_spinup.utils.logx.EpochLogger.store){.reference
  .external}.
::::::

::: {#logger.xhtml_logging-and-pytorch .section}
### [Logging and PyTorch](#logger.xhtml_id5){.toc-backref}

The preceding example was given in Tensorflow. For PyTorch, everything
is the same except for L42-43: instead of
[`logger.setup_tf_saver`{.docutils .literal}]{.pre}, you would use
[`logger.setup_pytorch_saver`{.docutils .literal}]{.pre}, and you would
pass it [a PyTorch
module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module){.reference
.external}[
\[https://pytorch.org/docs/stable/nn.html#torch.nn.Module\]]{.link-target}
(the network you are training) as an argument.

The behavior of [`logger.save_state`{.docutils .literal}]{.pre} is the
same as in the Tensorflow case: each time it is called, it'll save the
latest version of the PyTorch module.
:::

:::: {#logger.xhtml_logging-and-mpi .section}
### [Logging and MPI](#logger.xhtml_id6){.toc-backref}

::: {.admonition-you-should-know .admonition}
You Should Know

Several algorithms in RL are easily parallelized by using MPI to average
gradients and/or other key quantities. The Spinning Up loggers are
designed to be well-behaved when using MPI: things will only get written
to stdout and to file from the process with rank 0. But information from
other processes isn't lost if you use the EpochLogger: everything which
is passed into EpochLogger via [`store`{.docutils .literal}]{.pre},
regardless of which process it's stored in, gets used to compute
average/std/min/max values for a diagnostic.
:::
::::
:::::::::::

::: {#logger.xhtml_logger-classes .section}
## [Logger Classes](#logger.xhtml_id7){.toc-backref}

*class* `spinup.utils.logx.`{.descclassname}`Logger`{.descname}[(]{.sig-paren}*output_dir=None*, *output_fname=\'progress.txt\'*, *exp_name=None*[)]{.sig-paren}

:   A general-purpose logger.

    Makes it easy to save diagnostics, hyperparameter configurations,
    the state of a training run, and the trained model.

    `__init__`{.descname}[(]{.sig-paren}*output_dir=None*, *output_fname=\'progress.txt\'*, *exp_name=None*[)]{.sig-paren}

    :   Initialize a Logger.

        +-------------+--------------------------------------------------------+
        | Parameters: | - **output_dir** (*string*) -- A directory for saving  |
        |             |   results to. If [`None`{.docutils .literal}]{.pre},   |
        |             |   defaults to a temp directory of the form             |
        |             |   [`/tmp/experiments/somerandomnumber`{.docutils       |
        |             |   .literal}]{.pre}.                                    |
        |             | - **output_fname** (*string*) -- Name for the          |
        |             |   tab-separated-value file containing metrics logged   |
        |             |   throughout a training run. Defaults to               |
        |             |   [`progress.txt`{.docutils .literal}]{.pre}.          |
        |             | - **exp_name** (*string*) -- Experiment name. If you   |
        |             |   run multiple training runs and give them all the     |
        |             |   same [`exp_name`{.docutils .literal}]{.pre}, the     |
        |             |   plotter will know to group them. (Use case: if you   |
        |             |   run the same hyperparameter configuration with       |
        |             |   multiple random seeds, you should give them all the  |
        |             |   same [`exp_name`{.docutils .literal}]{.pre}.)        |
        +-------------+--------------------------------------------------------+

    `dump_tabular`{.descname}[(]{.sig-paren}[)]{.sig-paren}

    :   Write all of the diagnostics from the current iteration.

        Writes both to stdout, and to the output file.

    `log`{.descname}[(]{.sig-paren}*msg*, *color=\'green\'*[)]{.sig-paren}

    :   Print a colorized message to stdout.

    `log_tabular`{.descname}[(]{.sig-paren}*key*, *val*[)]{.sig-paren}

    :   Log a value of some diagnostic.

        Call this only once for each diagnostic quantity, each
        iteration. After using [`log_tabular`{.docutils .literal}]{.pre}
        to store values for each diagnostic, make sure to call
        [`dump_tabular`{.docutils .literal}]{.pre} to write them out to
        file and stdout (otherwise they will not get saved anywhere).

    `save_config`{.descname}[(]{.sig-paren}*config*[)]{.sig-paren}

    :   Log an experiment configuration.

        Call this once at the top of your experiment, passing in all
        important config vars as a dict. This will serialize the config
        to JSON, while handling anything which can't be serialized in a
        graceful way (writing as informative a string as possible).

        Example use:

        :::: highlight-python
        ::: highlight
            logger = EpochLogger(**logger_kwargs)
            logger.save_config(locals())
        :::
        ::::

    `save_state`{.descname}[(]{.sig-paren}*state_dict*, *itr=None*[)]{.sig-paren}

    :   Saves the state of an experiment.

        To be clear: this is about saving *state*, not logging
        diagnostics. All diagnostic logging is separate from this
        function. This function will save whatever is in
        [`state_dict`{.docutils .literal}]{.pre}---usually just a copy
        of the environment---and the most recent parameters for the
        model you previously set up saving for with
        [`setup_tf_saver`{.docutils .literal}]{.pre}.

        Call with any frequency you prefer. If you only want to maintain
        a single state and overwrite it at each call with the most
        recent version, leave [`itr=None`{.docutils .literal}]{.pre}. If
        you want to keep all of the states you save, provide unique
        (increasing) values for 'itr'.

        +-------------+--------------------------------------------------------+
        | Parameters: | - **state_dict** (*dict*) -- Dictionary containing     |
        |             |   essential elements to describe the current state of  |
        |             |   training.                                            |
        |             | - **itr** -- An int, or None. Current iteration of     |
        |             |   training.                                            |
        +-------------+--------------------------------------------------------+

    `setup_pytorch_saver`{.descname}[(]{.sig-paren}*what_to_save*[)]{.sig-paren}

    :   Set up easy model saving for a single PyTorch model.

        Because PyTorch saving and loading is especially painless, this
        is very minimal; we just need references to whatever we would
        like to pickle. This is integrated into the logger because the
        logger knows where the user would like to save information about
        this training run.

          ------------- -----------------------------------------------------------------------------------------
          Parameters:   **what_to_save** -- Any PyTorch model or serializable object containing PyTorch models.
          ------------- -----------------------------------------------------------------------------------------

    `setup_tf_saver`{.descname}[(]{.sig-paren}*sess*, *inputs*, *outputs*[)]{.sig-paren}

    :   Set up easy model saving for tensorflow.

        Call once, after defining your computation graph but before
        training.

        +-------------+--------------------------------------------------------+
        | Parameters: | - **sess** -- The Tensorflow session in which you      |
        |             |   train your computation graph.                        |
        |             | - **inputs** (*dict*) -- A dictionary that maps from   |
        |             |   keys of your choice to the tensorflow placeholders   |
        |             |   that serve as inputs to the computation graph. Make  |
        |             |   sure that *all* of the placeholders needed for your  |
        |             |   outputs are included!                                |
        |             | - **outputs** (*dict*) -- A dictionary that maps from  |
        |             |   keys of your choice to the outputs from your         |
        |             |   computation graph.                                   |
        +-------------+--------------------------------------------------------+

<!-- -->

*class* `spinup.utils.logx.`{.descclassname}`EpochLogger`{.descname}[(]{.sig-paren}*\*args*, *\*\*kwargs*[)]{.sig-paren}

:   Bases: [[`spinup.utils.logx.Logger`{.xref .py .py-class .docutils
    .literal}]{.pre}](#logger.xhtml_spinup.utils.logx.Logger "spinup.utils.logx.Logger"){.reference
    .internal}

    A variant of Logger tailored for tracking average values over
    epochs.

    Typical use case: there is some quantity which is calculated many
    times throughout an epoch, and at the end of the epoch, you would
    like to report the average / std / min / max value of that quantity.

    With an EpochLogger, each time the quantity is calculated, you would
    use

    :::: highlight-python
    ::: highlight
        epoch_logger.store(NameOfQuantity=quantity_value)
    :::
    ::::

    to load it into the EpochLogger's state. Then at the end of the
    epoch, you would use

    :::: highlight-python
    ::: highlight
        epoch_logger.log_tabular(NameOfQuantity, **options)
    :::
    ::::

    to record the desired values.

    `get_stats`{.descname}[(]{.sig-paren}*key*[)]{.sig-paren}

    :   Lets an algorithm ask the logger for mean/std/min/max of a
        diagnostic.

    `log_tabular`{.descname}[(]{.sig-paren}*key*, *val=None*, *with_min_and_max=False*, *average_only=False*[)]{.sig-paren}

    :   Log a value or possibly the mean/std/min/max values of a
        diagnostic.

        +-------------+--------------------------------------------------------+
        | Parameters: | - **key** (*string*) -- The name of the diagnostic. If |
        |             |   you are logging a diagnostic whose state has         |
        |             |   previously been saved with [`store`{.docutils        |
        |             |   .literal}]{.pre}, the key here has to match the key  |
        |             |   you used there.                                      |
        |             | - **val** -- A value for the diagnostic. If you have   |
        |             |   previously saved values for this key via             |
        |             |   [`store`{.docutils .literal}]{.pre}, do *not*        |
        |             |   provide a [`val`{.docutils .literal}]{.pre} here.    |
        |             | - **with_min_and_max** (*bool*) -- If true, log min    |
        |             |   and max values of the diagnostic over the epoch.     |
        |             | - **average_only** (*bool*) -- If true, do not log the |
        |             |   standard deviation of the diagnostic over the epoch. |
        +-------------+--------------------------------------------------------+

    `store`{.descname}[(]{.sig-paren}*\*\*kwargs*[)]{.sig-paren}

    :   Save something into the epoch_logger's current state.

        Provide an arbitrary number of keyword arguments with numerical
        values.
:::

::::::: {#logger.xhtml_loading-saved-models-pytorch-only .section}
## [Loading Saved Models (PyTorch Only)](#logger.xhtml_id8){.toc-backref}

To load an actor-critic model saved by a PyTorch Spinning Up
implementation, run:

:::: highlight-python
::: highlight
    ac = torch.load('path/to/model.pt')
:::
::::

When you use this method to load an actor-critic model, you can
minimally expect it to have an [`act`{.docutils .literal}]{.pre} method
that allows you to sample actions from the policy, given observations:

:::: highlight-python
::: highlight
    actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
:::
::::
:::::::

::: {#logger.xhtml_loading-saved-graphs-tensorflow-only .section}
## [Loading Saved Graphs (Tensorflow Only)](#logger.xhtml_id9){.toc-backref}

`spinup.utils.logx.`{.descclassname}`restore_tf_graph`{.descname}[(]{.sig-paren}*sess*, *fpath*[)]{.sig-paren}

:   Loads graphs saved by Logger.

    Will output a dictionary whose keys and values are from the 'inputs'
    and 'outputs' dict you specified with logger.setup_tf_saver().

    +-------------+--------------------------------------------------------+
    | Parameters: | - **sess** -- A Tensorflow session.                    |
    |             | - **fpath** -- Filepath to save directory.             |
    +-------------+--------------------------------------------------------+
    | Returns:    | A dictionary mapping from keys to tensors in the       |
    |             | computation graph loaded from [`fpath`{.docutils       |
    |             | .literal}]{.pre}.                                      |
    +-------------+--------------------------------------------------------+

When you use this method to restore a graph saved by a Tensorflow
Spinning Up implementation, you can minimally expect it to include the
following:

+------------------+---------------------------------------------------------------+
| Key              | Value                                                         |
+==================+===============================================================+
| [`x`{.docutils   | Tensorflow placeholder for state input.                       |
| .literal}]{.pre} |                                                               |
+------------------+---------------------------------------------------------------+
| [`pi`{.docutils  | ::::: {.first .last .line-block}                              |
| .literal}]{.pre} | ::: line                                                      |
|                  | Samples an action from the agent, conditioned                 |
|                  | :::                                                           |
|                  |                                                               |
|                  | ::: line                                                      |
|                  | on states in [`x`{.docutils .literal}]{.pre}.                 |
|                  | :::                                                           |
|                  | :::::                                                         |
+------------------+---------------------------------------------------------------+

The relevant value functions for an algorithm are also typically stored.
For details of what else gets saved by a given algorithm, see its
documentation page.
:::
::::::::::::::::::::
:::::::::::::::::::::

[]{#plotter.xhtml}

:::: {.body role="main"}
::: {#plotter.xhtml_plotter .section}
# Plotter

See the page on [plotting results](../user/plotting.html){.reference
.external} for documentation of the plotter.
:::
::::

[]{#mpi.xhtml}

:::::::::: {.body role="main"}
::::::::: {#mpi.xhtml_mpi-tools .section}
# [MPI Tools](#mpi.xhtml_id1){.toc-backref}

::: {#mpi.xhtml_table-of-contents .contents .topic}
Table of Contents

- [MPI Tools](#mpi.xhtml_mpi-tools){#mpi.xhtml_id1 .reference .internal}
  - [Core MPI
    Utilities](#mpi.xhtml_module-spinup.utils.mpi_tools){#mpi.xhtml_id2
    .reference .internal}
  - [MPI + PyTorch
    Utilities](#mpi.xhtml_mpi-pytorch-utilities){#mpi.xhtml_id3
    .reference .internal}
  - [MPI + Tensorflow
    Utilities](#mpi.xhtml_mpi-tensorflow-utilities){#mpi.xhtml_id4
    .reference .internal}
:::

::: {#mpi.xhtml_module-spinup.utils.mpi_tools .section}
[]{#mpi.xhtml_core-mpi-utilities}

## [Core MPI Utilities](#mpi.xhtml_id2){.toc-backref}

`spinup.utils.mpi_tools.`{.descclassname}`mpi_avg`{.descname}[(]{.sig-paren}*x*[)]{.sig-paren}

:   Average a scalar or vector over MPI processes.

<!-- -->

`spinup.utils.mpi_tools.`{.descclassname}`mpi_fork`{.descname}[(]{.sig-paren}*n*, *bind_to_core=False*[)]{.sig-paren}

:   Re-launches the current script with workers linked by MPI.

    Also, terminates the original process that launched it.

    Taken almost without modification from the Baselines function of the
    [same
    name](https://github.com/openai/baselines/blob/master/baselines/common/mpi_fork.py){.reference
    .external}[
    \[https://github.com/openai/baselines/blob/master/baselines/common/mpi_fork.py\]]{.link-target}.

    +-------------+--------------------------------------------------------+
    | Parameters: | - **n** (*int*) -- Number of process to split into.    |
    |             | - **bind_to_core** (*bool*) -- Bind each MPI process   |
    |             |   to a core.                                           |
    +-------------+--------------------------------------------------------+

<!-- -->

`spinup.utils.mpi_tools.`{.descclassname}`mpi_statistics_scalar`{.descname}[(]{.sig-paren}*x*, *with_min_and_max=False*[)]{.sig-paren}

:   Get mean/std and optional min/max of scalar x across MPI processes.

    +-------------+--------------------------------------------------------+
    | Parameters: | - **x** -- An array containing samples of the scalar   |
    |             |   to produce statistics for.                           |
    |             | - **with_min_and_max** (*bool*) -- If true, return min |
    |             |   and max of x in addition to mean and std.            |
    +-------------+--------------------------------------------------------+

<!-- -->

`spinup.utils.mpi_tools.`{.descclassname}`num_procs`{.descname}[(]{.sig-paren}[)]{.sig-paren}

:   Count active MPI processes.

<!-- -->

`spinup.utils.mpi_tools.`{.descclassname}`proc_id`{.descname}[(]{.sig-paren}[)]{.sig-paren}

:   Get rank of calling process.
:::

::::: {#mpi.xhtml_mpi-pytorch-utilities .section}
## [MPI + PyTorch Utilities](#mpi.xhtml_id3){.toc-backref}

[`spinup.utils.mpi_pytorch`{.docutils .literal}]{.pre} contains a few
tools to make it easy to do data-parallel PyTorch optimization across
MPI processes. The two main ingredients are syncing parameters and
averaging gradients before they are used by the adaptive optimizer. Also
there's a hacky fix for a problem where the PyTorch instance in each
separate process tries to get too many threads, and they start to
clobber each other.

The pattern for using these tools looks something like this:

1.  At the beginning of the training script, call
    [`setup_pytorch_for_mpi()`{.docutils .literal}]{.pre}. (Avoids
    clobbering problem.)
2.  After you've constructed a PyTorch module, call
    [`sync_params(module)`{.docutils .literal}]{.pre}.
3.  Then, during gradient descent, call [`mpi_avg_grads`{.docutils
    .literal}]{.pre} after the backward pass, like so:

:::: highlight-python
::: highlight
    optimizer.zero_grad()
    loss = compute_loss(module)
    loss.backward()
    mpi_avg_grads(module)   # averages gradient buffers across MPI processes!
    optimizer.step()
:::
::::

[]{#mpi.xhtml_module-spinup.utils.mpi_pytorch .target}

`spinup.utils.mpi_pytorch.`{.descclassname}`mpi_avg_grads`{.descname}[(]{.sig-paren}*module*[)]{.sig-paren}

:   Average contents of gradient buffers across MPI processes.

<!-- -->

`spinup.utils.mpi_pytorch.`{.descclassname}`setup_pytorch_for_mpi`{.descname}[(]{.sig-paren}[)]{.sig-paren}

:   Avoid slowdowns caused by each separate process's PyTorch using more
    than its fair share of CPU resources.

<!-- -->

`spinup.utils.mpi_pytorch.`{.descclassname}`sync_params`{.descname}[(]{.sig-paren}*module*[)]{.sig-paren}

:   Sync all parameters of module across all MPI processes.
:::::

::: {#mpi.xhtml_mpi-tensorflow-utilities .section}
## [MPI + Tensorflow Utilities](#mpi.xhtml_id4){.toc-backref}

The [`spinup.utils.mpi_tf`{.docutils .literal}]{.pre} contains a a few
tools to make it easy to use the AdamOptimizer across many MPI
processes. This is a bit hacky---if you're looking for something more
sophisticated and general-purpose, consider
[horovod](https://github.com/uber/horovod){.reference .external}[
\[https://github.com/uber/horovod\]]{.link-target}.

[]{#mpi.xhtml_module-spinup.utils.mpi_tf .target}

*class* `spinup.utils.mpi_tf.`{.descclassname}`MpiAdamOptimizer`{.descname}[(]{.sig-paren}*\*\*kwargs*[)]{.sig-paren}

:   Adam optimizer that averages gradients across MPI processes.

    The compute_gradients method is taken from Baselines
    [MpiAdamOptimizer](https://github.com/openai/baselines/blob/master/baselines/common/mpi_adam_optimizer.py){.reference
    .external}[
    \[https://github.com/openai/baselines/blob/master/baselines/common/mpi_adam_optimizer.py\]]{.link-target}.
    For documentation on method arguments, see the Tensorflow docs page
    for the base
    [AdamOptimizer](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer){.reference
    .external}[
    \[https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer\]]{.link-target}.

    `apply_gradients`{.descname}[(]{.sig-paren}*grads_and_vars*, *global_step=None*, *name=None*[)]{.sig-paren}

    :   Same as normal apply_gradients, except sync params after update.

    `compute_gradients`{.descname}[(]{.sig-paren}*loss*, *var_list*, *\*\*kwargs*[)]{.sig-paren}

    :   Same as normal compute_gradients, except average grads over
        processes.

<!-- -->

`spinup.utils.mpi_tf.`{.descclassname}`sync_all_params`{.descname}[(]{.sig-paren}[)]{.sig-paren}

:   Sync all tf variables across MPI processes.
:::
:::::::::
::::::::::

[]{#run_utils.xhtml}

::::::: {.body role="main"}
:::::: {#run_utils.xhtml_run-utils .section}
# [Run Utils](#run_utils.xhtml_id1){.toc-backref}

::: {#run_utils.xhtml_table-of-contents .contents .topic}
Table of Contents

- [Run Utils](#run_utils.xhtml_run-utils){#run_utils.xhtml_id1
  .reference .internal}
  - [ExperimentGrid](#run_utils.xhtml_experimentgrid){#run_utils.xhtml_id2
    .reference .internal}
  - [Calling
    Experiments](#run_utils.xhtml_calling-experiments){#run_utils.xhtml_id3
    .reference .internal}
:::

::: {#run_utils.xhtml_experimentgrid .section}
## [ExperimentGrid](#run_utils.xhtml_id2){.toc-backref}

Spinning Up ships with a tool called ExperimentGrid for making
hyperparameter ablations easier. This is based on (but simpler than)
[the rllab
tool](https://github.com/rll/rllab/blob/master/rllab/misc/instrument.py#L173){.reference
.external}[
\[https://github.com/rll/rllab/blob/master/rllab/misc/instrument.py#L173\]]{.link-target}
called VariantGenerator.

*class* `spinup.utils.run_utils.`{.descclassname}`ExperimentGrid`{.descname}[(]{.sig-paren}*name=\'\'*[)]{.sig-paren}

:   Tool for running many experiments given hyperparameter ranges.

    `add`{.descname}[(]{.sig-paren}*key*, *vals*, *shorthand=None*, *in_name=False*[)]{.sig-paren}

    :   Add a parameter (key) to the grid config, with potential values
        (vals).

        By default, if a shorthand isn't given, one is automatically
        generated from the key using the first three letters of each
        colon-separated term. To disable this behavior, change
        [`DEFAULT_SHORTHAND`{.docutils .literal}]{.pre} in the
        [`spinup/user_config.py`{.docutils .literal}]{.pre} file to
        [`False`{.docutils .literal}]{.pre}.

        +-------------+--------------------------------------------------------+
        | Parameters: | - **key** (*string*) -- Name of parameter.             |
        |             | - **vals** (*value* *or* *list of values*) -- Allowed  |
        |             |   values of parameter.                                 |
        |             | - **shorthand** (*string*) -- Optional, shortened name |
        |             |   of parameter. For example, maybe the parameter       |
        |             |   [`steps_per_epoch`{.docutils .literal}]{.pre} is     |
        |             |   shortened to [`steps`{.docutils .literal}]{.pre}.    |
        |             | - **in_name** (*bool*) -- When constructing variant    |
        |             |   names, force the inclusion of this parameter into    |
        |             |   the name.                                            |
        +-------------+--------------------------------------------------------+

    `print`{.descname}[(]{.sig-paren}[)]{.sig-paren}

    :   Print a helpful report about the experiment grid.

    `run`{.descname}[(]{.sig-paren}*thunk*, *num_cpu=1*, *data_dir=None*, *datestamp=False*[)]{.sig-paren}

    :   Run each variant in the grid with function 'thunk'.

        Note: 'thunk' must be either a callable function, or a string.
        If it is a string, it must be the name of a parameter whose
        values are all callable functions.

        Uses [`call_experiment`{.docutils .literal}]{.pre} to actually
        launch each experiment, and gives each variant a name using
        [`self.variant_name()`{.docutils .literal}]{.pre}.

        Maintenance note: the args for ExperimentGrid.run should track
        closely to the args for call_experiment. However,
        [`seed`{.docutils .literal}]{.pre} is omitted because we presume
        the user may add it as a parameter in the grid.

    `variant_name`{.descname}[(]{.sig-paren}*variant*[)]{.sig-paren}

    :   Given a variant (dict of valid param/value pairs), make an
        exp_name.

        A variant's name is constructed as the grid name (if you've
        given it one), plus param names (or shorthands if available) and
        values separated by underscores.

        Note: if [`seed`{.docutils .literal}]{.pre} is a parameter, it
        is not included in the name.

    `variants`{.descname}[(]{.sig-paren}[)]{.sig-paren}

    :   Makes a list of dicts, where each dict is a valid config in the
        grid.

        There is special handling for variant parameters whose names
        take the form

        > ::: {}
        > [`'full:param:name'`{.docutils .literal}]{.pre}.
        > :::

        The colons are taken to indicate that these parameters should
        have a nested dict structure. eg, if there are two params,

        > ::: {}
        >   -----------------------------------------------------------------------
        >   Key                                                           Val
        >   ------------------------------------------------------------- ---------
        >   [`'base:param:a'`{.docutils .literal}]{.pre}                  1
        >
        >   [`'base:param:b'`{.docutils .literal}]{.pre}                  2
        >   -----------------------------------------------------------------------
        > :::

        the variant dict will have the structure

        :::: highlight-default
        ::: highlight
            variant = {
                base: {
                    param : {
                        a : 1,
                        b : 2
                        }
                    }
                }
        :::
        ::::
:::

::: {#run_utils.xhtml_calling-experiments .section}
## [Calling Experiments](#run_utils.xhtml_id3){.toc-backref}

`spinup.utils.run_utils.`{.descclassname}`call_experiment`{.descname}[(]{.sig-paren}*exp_name*, *thunk*, *seed=0*, *num_cpu=1*, *data_dir=None*, *datestamp=False*, *\*\*kwargs*[)]{.sig-paren}

:   Run a function (thunk) with hyperparameters (kwargs), plus
    configuration.

    This wraps a few pieces of functionality which are useful when you
    want to run many experiments in sequence, including logger
    configuration and splitting into multiple processes for MPI.

    There's also a SpinningUp-specific convenience added into executing
    the thunk: if [`env_name`{.docutils .literal}]{.pre} is one of the
    kwargs passed to call_experiment, it's assumed that the thunk
    accepts an argument called [`env_fn`{.docutils .literal}]{.pre}, and
    that the [`env_fn`{.docutils .literal}]{.pre} should make a gym
    environment with the given [`env_name`{.docutils .literal}]{.pre}.

    The way the experiment is actually executed is slightly complicated:
    the function is serialized to a string, and then
    [`run_entrypoint.py`{.docutils .literal}]{.pre} is executed in a
    subprocess call with the serialized string as an argument.
    [`run_entrypoint.py`{.docutils .literal}]{.pre} unserializes the
    function call and executes it. We choose to do it this way---instead
    of just calling the function directly here---to avoid leaking state
    between successive experiments.

    +-------------+--------------------------------------------------------+
    | Parameters: | - **exp_name** (*string*) -- Name for experiment.      |
    |             | - **thunk** (*callable*) -- A python function.         |
    |             | - **seed** (*int*) -- Seed for random number           |
    |             |   generators.                                          |
    |             | - **num_cpu** (*int*) -- Number of MPI processes to    |
    |             |   split into. Also accepts 'auto', which will set up   |
    |             |   as many procs as there are cpus on the machine.      |
    |             | - **data_dir** (*string*) -- Used in configuring the   |
    |             |   logger, to decide where to store experiment results. |
    |             |   Note: if left as None, data_dir will default to      |
    |             |   [`DEFAULT_DATA_DIR`{.docutils .literal}]{.pre} from  |
    |             |   [`spinup/user_config.py`{.docutils .literal}]{.pre}. |
    |             | - **\*\*kwargs** -- All kwargs to pass to thunk.       |
    +-------------+--------------------------------------------------------+

<!-- -->

`spinup.utils.run_utils.`{.descclassname}`setup_logger_kwargs`{.descname}[(]{.sig-paren}*exp_name*, *seed=None*, *data_dir=None*, *datestamp=False*[)]{.sig-paren}

:   Sets up the output_dir for a logger and returns a dict for logger
    kwargs.

    If no seed is given and datestamp is false,

    :::: highlight-default
    ::: highlight
        output_dir = data_dir/exp_name
    :::
    ::::

    If a seed is given and datestamp is false,

    :::: highlight-default
    ::: highlight
        output_dir = data_dir/exp_name/exp_name_s[seed]
    :::
    ::::

    If datestamp is true, amend to

    :::: highlight-default
    ::: highlight
        output_dir = data_dir/YY-MM-DD_exp_name/YY-MM-DD_HH-MM-SS_exp_name_s[seed]
    :::
    ::::

    You can force datestamp=True by setting
    [`FORCE_DATESTAMP=True`{.docutils .literal}]{.pre} in
    [`spinup/user_config.py`{.docutils .literal}]{.pre}.

    +-------------+--------------------------------------------------------+
    | Parameters: | - **exp_name** (*string*) -- Name for experiment.      |
    |             | - **seed** (*int*) -- Seed for random number           |
    |             |   generators used by experiment.                       |
    |             | - **data_dir** (*string*) -- Path to folder where      |
    |             |   results should be saved. Default is the              |
    |             |   [`DEFAULT_DATA_DIR`{.docutils .literal}]{.pre} in    |
    |             |   [`spinup/user_config.py`{.docutils .literal}]{.pre}. |
    |             | - **datestamp** (*bool*) -- Whether to include a date  |
    |             |   and timestamp in the name of the save directory.     |
    +-------------+--------------------------------------------------------+
    | Returns:    | logger_kwargs, a dict containing output_dir and        |
    |             | exp_name.                                              |
    +-------------+--------------------------------------------------------+
:::
::::::
:::::::

[]{#acknowledgements.xhtml}

:::: {.body role="main"}
::: {#acknowledgements.xhtml_acknowledgements .section}
# Acknowledgements

We gratefully acknowledge the contributions of the many people who
helped get this project off of the ground, including people who beta
tested the software, gave feedback on the material, improved
dependencies of Spinning Up code in service of this release, or
otherwise supported the project. Given the number of people who were
involved at various points, this list of names may not be exhaustive.
(If you think you should have been listed here, please do not hesitate
to reach out.)

In no particular order, thank you Alex Ray, Amanda Askell, Ben
Garfinkel, Christy Dennison, Coline Devin, Daniel Zeigler, Dylan
Hadfield-Menell, Ge Yang, Greg Khan, Jack Clark, Jonas Rothfuss, Larissa
Schiavo, Leandro Castelao, Lilian Weng, Maddie Hall, Matthias Plappert,
Miles Brundage, Peter Zokhov, and Pieter Abbeel.

We are also grateful to Pieter Abbeel's group at Berkeley, and the
Center for Human-Compatible AI, for giving feedback on presentations
about Spinning Up.
:::
::::

[]{#author.xhtml}

:::: {.body role="main"}
::: {#author.xhtml_about-the-author .section}
# About the Author

Spinning Up in Deep RL was primarily developed by Josh Achiam, a
research scientist on the OpenAI Safety Team and PhD student at UC
Berkeley advised by Pieter Abbeel. Josh studies topics related to safety
in deep reinforcement learning, and has previously published work on
[safe exploration](https://arxiv.org/abs/1705.10528){.reference
.external}[ \[https://arxiv.org/abs/1705.10528\]]{.link-target}.
:::
::::

[]{#py-modindex.xhtml}

:::: {.body role="main"}
# Python Module Index

::: modindex-jumpbox
[**s**](#py-modindex.xhtml_cap-s)
:::

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------- --
                                                                                                                                                            
                                                                      **s**                                                                                 
  ![-](_static/minus.png){#toggle-1 .toggler style="display: none"}   `spinup`{.xref}                                                                       
                                                                          [`spinup.utils.mpi_pytorch`{.xref}](#mpi.xhtml_module-spinup.utils.mpi_pytorch)   
                                                                          [`spinup.utils.mpi_tf`{.xref}](#mpi.xhtml_module-spinup.utils.mpi_tf)             
                                                                          [`spinup.utils.mpi_tools`{.xref}](#mpi.xhtml_module-spinup.utils.mpi_tools)       
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------- --
::::

[]{#genindex.xhtml}

:::: {.body role="main"}
# Index {#genindex.xhtml_index}

::: genindex-jumpbox
[**Symbols**](#genindex.xhtml_Symbols) \| [**\_**](#genindex.xhtml__) \|
[**A**](#genindex.xhtml_A) \| [**C**](#genindex.xhtml_C) \|
[**D**](#genindex.xhtml_D) \| [**E**](#genindex.xhtml_E) \|
[**G**](#genindex.xhtml_G) \| [**L**](#genindex.xhtml_L) \|
[**M**](#genindex.xhtml_M) \| [**N**](#genindex.xhtml_N) \|
[**P**](#genindex.xhtml_P) \| [**R**](#genindex.xhtml_R) \|
[**S**](#genindex.xhtml_S) \| [**T**](#genindex.xhtml_T) \|
[**V**](#genindex.xhtml_V)
:::

## Symbols {#genindex.xhtml_Symbols}

+-------------------------------------------------+-----------------------------------------------------+
| - \--act, \--ac_kwargs:activation               | - -d, \--deterministic                              |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-act)       |     option](#saving_and_loading.xhtml_cmdoption-d)  |
| - \--count                                      | - -i I, \--itr=I, default=-1                        |
|   - [command line                               |   - [command line                                   |
|     option](#plotting.xhtml_cmdoption-count)    |     option](#saving_and_loading.xhtml_cmdoption-i)  |
| - \--cpu, \--num_cpu                            | - -l L, \--len=L, default=0                         |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-cpu)       |     option](#saving_and_loading.xhtml_cmdoption-l)  |
| - \--data_dir                                   | - -l, \--legend=\[LEGEND \...\]                     |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-data-dir)  |     option](#plotting.xhtml_cmdoption-l)            |
| - \--datestamp                                  | - -n N, \--episodes=N, default=100                  |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-datestamp) |     option](#saving_and_loading.xhtml_cmdoption-n)  |
| - \--env, \--env_name                           | - -nr, \--norender                                  |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-env)       |     option](#saving_and_loading.xhtml_cmdoption-nr) |
| - \--exclude=\[EXC \...\]                       | - -s, \--smooth=S, default=1                        |
|   - [command line                               |   - [command line                                   |
|     option](#plotting.xhtml_cmdoption-exclude)  |     option](#plotting.xhtml_cmdoption-s)            |
| - \--exp_name                                   | - -x, \--xaxis=XAXIS, default=\'TotalEnvInteracts\' |
|   - [command line                               |   - [command line                                   |
|     option](#running.xhtml_cmdoption-exp-name)  |     option](#plotting.xhtml_cmdoption-x)            |
| - \--hid, \--ac_kwargs:hidden_sizes             | - -y, \--value=\[VALUE \...\],                      |
|   - [command line                               |   default=\'Performance\'                           |
|     option](#running.xhtml_cmdoption-hid)       |   - [command line                                   |
| - \--select=\[SEL \...\]                        |     option](#plotting.xhtml_cmdoption-y)            |
|   - [command line                               |                                                     |
|     option](#plotting.xhtml_cmdoption-select)   |                                                     |
+-------------------------------------------------+-----------------------------------------------------+

## \_ {#genindex.xhtml__}

+-----------------------------------------------------------------------+
| - [\_\_init\_\_() (spinup.utils.logx.Logger                           |
|   method)](#logger.xhtml_spinup.utils.logx.Logger.__init__)           |
+-----------------------------------------------------------------------+

## A {#genindex.xhtml_A}

+------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - [add() (spinup.utils.run_utils.ExperimentGrid                        | - [apply_gradients() (spinup.utils.mpi_tf.MpiAdamOptimizer                  |
|   method)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid.add) |   method)](#mpi.xhtml_spinup.utils.mpi_tf.MpiAdamOptimizer.apply_gradients) |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------+

## C {#genindex.xhtml_C}

+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - [call_experiment() (in module                                                     | - [compute_gradients() (spinup.utils.mpi_tf.MpiAdamOptimizer                  |
|   spinup.utils.run_utils)](#run_utils.xhtml_spinup.utils.run_utils.call_experiment) |   method)](#mpi.xhtml_spinup.utils.mpi_tf.MpiAdamOptimizer.compute_gradients) |
| - command line option                                                               |                                                                               |
|   - [\--act, \--ac_kwargs:activation](#running.xhtml_cmdoption-act)                 |                                                                               |
|   - [\--count](#plotting.xhtml_cmdoption-count)                                     |                                                                               |
|   - [\--cpu, \--num_cpu](#running.xhtml_cmdoption-cpu)                              |                                                                               |
|   - [\--data_dir](#running.xhtml_cmdoption-data-dir)                                |                                                                               |
|   - [\--datestamp](#running.xhtml_cmdoption-datestamp)                              |                                                                               |
|   - [\--env, \--env_name](#running.xhtml_cmdoption-env)                             |                                                                               |
|   - [\--exclude=\[EXC \...\]](#plotting.xhtml_cmdoption-exclude)                    |                                                                               |
|   - [\--exp_name](#running.xhtml_cmdoption-exp-name)                                |                                                                               |
|   - [\--hid, \--ac_kwargs:hidden_sizes](#running.xhtml_cmdoption-hid)               |                                                                               |
|   - [\--select=\[SEL \...\]](#plotting.xhtml_cmdoption-select)                      |                                                                               |
|   - [-d, \--deterministic](#saving_and_loading.xhtml_cmdoption-d)                   |                                                                               |
|   - [-i I, \--itr=I, default=-1](#saving_and_loading.xhtml_cmdoption-i)             |                                                                               |
|   - [-l L, \--len=L, default=0](#saving_and_loading.xhtml_cmdoption-l)              |                                                                               |
|   - [-l, \--legend=\[LEGEND \...\]](#plotting.xhtml_cmdoption-l)                    |                                                                               |
|   - [-n N, \--episodes=N, default=100](#saving_and_loading.xhtml_cmdoption-n)       |                                                                               |
|   - [-nr, \--norender](#saving_and_loading.xhtml_cmdoption-nr)                      |                                                                               |
|   - [-s, \--smooth=S, default=1](#plotting.xhtml_cmdoption-s)                       |                                                                               |
|   - [-x, \--xaxis=XAXIS,                                                            |                                                                               |
|     default=\'TotalEnvInteracts\'](#plotting.xhtml_cmdoption-x)                     |                                                                               |
|   - [-y, \--value=\[VALUE \...\],                                                   |                                                                               |
|     default=\'Performance\'](#plotting.xhtml_cmdoption-y)                           |                                                                               |
|   - [logdir](#plotting.xhtml_cmdoption-arg-logdir)                                  |                                                                               |
+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## D {#genindex.xhtml_D}

+---------------------------------------------+-----------------------------------------------------------------+
| - [ddpg_pytorch() (in module                | - [ddpg_tf1() (in module spinup)](#ddpg.xhtml_spinup.ddpg_tf1)  |
|   spinup)](#ddpg.xhtml_spinup.ddpg_pytorch) | - [dump_tabular() (spinup.utils.logx.Logger                     |
|                                             |   method)](#logger.xhtml_spinup.utils.logx.Logger.dump_tabular) |
+---------------------------------------------+-----------------------------------------------------------------+

## E {#genindex.xhtml_E}

+--------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - [EpochLogger (class in                                           | - [ExperimentGrid (class in                                                        |
|   spinup.utils.logx)](#logger.xhtml_spinup.utils.logx.EpochLogger) |   spinup.utils.run_utils)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid) |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------+

## G {#genindex.xhtml_G}

+-----------------------------------------------------------------------+
| - [get_stats() (spinup.utils.logx.EpochLogger                         |
|   method)](#logger.xhtml_spinup.utils.logx.EpochLogger.get_stats)     |
+-----------------------------------------------------------------------+

## L {#genindex.xhtml_L}

+---------------------------------------------------------------------+---------------------------------------------------------------+
| - [log() (spinup.utils.logx.Logger                                  | - logdir                                                      |
|   method)](#logger.xhtml_spinup.utils.logx.Logger.log)              |   - [command line                                             |
| - [log_tabular() (spinup.utils.logx.EpochLogger                     |     option](#plotting.xhtml_cmdoption-arg-logdir)             |
|   method)](#logger.xhtml_spinup.utils.logx.EpochLogger.log_tabular) | - [Logger (class in                                           |
|   - [(spinup.utils.logx.Logger                                      |   spinup.utils.logx)](#logger.xhtml_spinup.utils.logx.Logger) |
|     method)](#logger.xhtml_spinup.utils.logx.Logger.log_tabular)    |                                                               |
+---------------------------------------------------------------------+---------------------------------------------------------------+

## M {#genindex.xhtml_M}

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - [mpi_avg() (in module                                                         | - [mpi_fork() (in module                                                            |
|   spinup.utils.mpi_tools)](#mpi.xhtml_spinup.utils.mpi_tools.mpi_avg)           |   spinup.utils.mpi_tools)](#mpi.xhtml_spinup.utils.mpi_tools.mpi_fork)              |
| - [mpi_avg_grads() (in module                                                   | - [mpi_statistics_scalar() (in module                                               |
|   spinup.utils.mpi_pytorch)](#mpi.xhtml_spinup.utils.mpi_pytorch.mpi_avg_grads) |   spinup.utils.mpi_tools)](#mpi.xhtml_spinup.utils.mpi_tools.mpi_statistics_scalar) |
|                                                                                 | - [MpiAdamOptimizer (class in                                                       |
|                                                                                 |   spinup.utils.mpi_tf)](#mpi.xhtml_spinup.utils.mpi_tf.MpiAdamOptimizer)            |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

## N {#genindex.xhtml_N}

+-------------------------------------------------------------------------+
| - [num_procs() (in module                                               |
|   spinup.utils.mpi_tools)](#mpi.xhtml_spinup.utils.mpi_tools.num_procs) |
+-------------------------------------------------------------------------+

## P {#genindex.xhtml_P}

+-------------------------------------------+--------------------------------------------------------------------------+
| - [ppo_pytorch() (in module               | - [print() (spinup.utils.run_utils.ExperimentGrid                        |
|   spinup)](#ppo.xhtml_spinup.ppo_pytorch) |   method)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid.print) |
| - [ppo_tf1() (in module                   | - [proc_id() (in module                                                  |
|   spinup)](#ppo.xhtml_spinup.ppo_tf1)     |   spinup.utils.mpi_tools)](#mpi.xhtml_spinup.utils.mpi_tools.proc_id)    |
+-------------------------------------------+--------------------------------------------------------------------------+

## R {#genindex.xhtml_R}

+-------------------------------------------------------------------------+------------------------------------------------------------------------+
| - [restore_tf_graph() (in module                                        | - [run() (spinup.utils.run_utils.ExperimentGrid                        |
|   spinup.utils.logx)](#logger.xhtml_spinup.utils.logx.restore_tf_graph) |   method)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid.run) |
+-------------------------------------------------------------------------+------------------------------------------------------------------------+

## S {#genindex.xhtml_S}

+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - [sac_pytorch() (in module spinup)](#sac.xhtml_spinup.sac_pytorch)                     | - [setup_tf_saver() (spinup.utils.logx.Logger                                 |
| - [sac_tf1() (in module spinup)](#sac.xhtml_spinup.sac_tf1)                             |   method)](#logger.xhtml_spinup.utils.logx.Logger.setup_tf_saver)             |
| - [save_config() (spinup.utils.logx.Logger                                              | - [spinup.utils.mpi_pytorch                                                   |
|   method)](#logger.xhtml_spinup.utils.logx.Logger.save_config)                          |   (module)](#mpi.xhtml_module-spinup.utils.mpi_pytorch)                       |
| - [save_state() (spinup.utils.logx.Logger                                               | - [spinup.utils.mpi_tf (module)](#mpi.xhtml_module-spinup.utils.mpi_tf)       |
|   method)](#logger.xhtml_spinup.utils.logx.Logger.save_state)                           | - [spinup.utils.mpi_tools (module)](#mpi.xhtml_module-spinup.utils.mpi_tools) |
| - [setup_logger_kwargs() (in module                                                     | - [store() (spinup.utils.logx.EpochLogger                                     |
|   spinup.utils.run_utils)](#run_utils.xhtml_spinup.utils.run_utils.setup_logger_kwargs) |   method)](#logger.xhtml_spinup.utils.logx.EpochLogger.store)                 |
| - [setup_pytorch_for_mpi() (in module                                                   | - [sync_all_params() (in module                                               |
|   spinup.utils.mpi_pytorch)](#mpi.xhtml_spinup.utils.mpi_pytorch.setup_pytorch_for_mpi) |   spinup.utils.mpi_tf)](#mpi.xhtml_spinup.utils.mpi_tf.sync_all_params)       |
| - [setup_pytorch_saver() (spinup.utils.logx.Logger                                      | - [sync_params() (in module                                                   |
|   method)](#logger.xhtml_spinup.utils.logx.Logger.setup_pytorch_saver)                  |   spinup.utils.mpi_pytorch)](#mpi.xhtml_spinup.utils.mpi_pytorch.sync_params) |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## T {#genindex.xhtml_T}

+-------------------------------------------+-----------------------------------------+
| - [td3_pytorch() (in module               | - [td3_tf1() (in module                 |
|   spinup)](#td3.xhtml_spinup.td3_pytorch) |   spinup)](#td3.xhtml_spinup.td3_tf1)   |
|                                           | - [trpo_tf1() (in module                |
|                                           |   spinup)](#trpo.xhtml_spinup.trpo_tf1) |
+-------------------------------------------+-----------------------------------------+

## V {#genindex.xhtml_V}

+---------------------------------------------------------------------------------+-------------------------------------------+
| - [variant_name() (spinup.utils.run_utils.ExperimentGrid                        | - [vpg_pytorch() (in module               |
|   method)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid.variant_name) |   spinup)](#vpg.xhtml_spinup.vpg_pytorch) |
| - [variants() (spinup.utils.run_utils.ExperimentGrid                            | - [vpg_tf1() (in module                   |
|   method)](#run_utils.xhtml_spinup.utils.run_utils.ExperimentGrid.variants)     |   spinup)](#vpg.xhtml_spinup.vpg_tf1)     |
+---------------------------------------------------------------------------------+-------------------------------------------+
::::
