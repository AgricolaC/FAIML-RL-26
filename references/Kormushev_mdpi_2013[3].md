[]{#title_page.xhtml}

[]{#ch001.xhtml}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#ch001.xhtml_robotics-02-00122 .section .level1 .unnumbered}
# Reinforcement Learning in Robotics: Applications and Real-World Challenges

<article>

::::::::::::::::::::::: html-front
::: html-art-header
*Robotics* **2013**, *2*(3), 122-148;
doi:[10.3390/robotics2030122](http://dx.doi.org/10.3390/robotics2030122)
:::

::: html-art-type
Article
:::

::: {#ch001.xhtml_html-article-title}
Reinforcement Learning in Robotics: Applications and Real-World
Challenges [†](#ch001.xhtml_fn1-robotics-02-00122){.html-fn}
:::

::: html-author-group
Petar Kormushev [\*]{rid="c1-robotics-02-00122"}, Sylvain Calinon and
Darwin G. Caldwell
:::

::::: html-aff-group
:::: {#ch001.xhtml_af1-robotics-02-00122 .html-aff}
::: html-content
Department of Advanced Robotics, Istituto Italiano di Tecnologia, via
Morego 30, 16163 Genova, Italy
:::
::::
:::::

::::::::: html-notes
::::: {#ch001.xhtml_fn1-robotics-02-00122 .html-note}
::: html-label
^†^
:::

::: html-content
Based on "Kormushev, P.; Calinon, S.; Caldwell, D.G.; Ugurlu, B.
Challenges for the Policy Representation When Applying Reinforcement
Learning in Robotics. In Proceedings of WCCI 2012 IEEE World Congress on
Computational Intelligence, Brisbane, Australia, 10--15 June 2012".
:::
:::::

::::: {#ch001.xhtml_c1-robotics-02-00122 .html-note}
::: html-label
\*
:::

::: html-content
Author to whom correspondence should be addressed.
:::
:::::
:::::::::

::: html-history
Received: 4 June 2013; in revised form: 24 June 2013 / Accepted: 28 June
2013 / Published: 5 July 2013
:::

:::: {#ch001.xhtml_html-abstract .section .html-abstract}
## Abstract: {#ch001.xhtml_html-abstract-title}

::: html-p
In robotics, the ultimate goal of reinforcement learning is to endow
robots with the ability to learn, improve, adapt and reproduce tasks
with dynamically changing constraints based on exploration and
autonomous learning. We give a summary of the state-of-the-art of
reinforcement learning in the context of robotics, in terms of both
algorithms and policy representations. Numerous challenges faced by the
policy representation in robotics are identified. Three recent examples
for the application of reinforcement learning to real-world robots are
described: a pancake flipping task, a bipedal walking energy
minimization task and an archery-based aiming task. In all examples, a
state-of-the-art expectation-maximization-based reinforcement learning
is used, and different policy representations are proposed and evaluated
for each task. The proposed policy representations offer viable
solutions to six rarely-addressed challenges in policy representations:
correlations, adaptability, multi-resolution, globality,
multi-dimensionality and convergence. Both the successes and the
practical difficulties encountered in these examples are discussed.
Based on insights from these particular cases, conclusions are drawn
about the state-of-the-art and the future perspective directions for
reinforcement learning in robotics.
:::
::::

::::: {#ch001.xhtml_html-keywords}
:::: html-gwd-group
::: {#ch001.xhtml_html-keywords-title}
Keywords:
:::

reinforcement learning; robotics; learning and adaptive systems
::::
:::::
:::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: html-body
::::::::::: {#ch001.xhtml_sec1-robotics-02-00122 .section type="intro"}
## 1. Introduction {#ch001.xhtml_introduction nested="1"}

::: html-p
Endowing robots with human-like abilities to perform motor skills in a
smooth and natural way is one of the important goals of robotics. A
promising way to achieve this is by creating robots that can learn new
skills by themselves, similarly to humans. However, acquiring new motor
skills is not simple and involves various forms of learning.
:::

:::: html-p
Over the years, the approaches for teaching new skill to robots have
evolved significantly, and currently, there are three well-established
types of approaches: [direct programming]{.html-italic}, [imitation
learning]{.html-italic} and [reinforcement learning]{.html-italic}. All
of these approaches are still being actively used, and each one has its
own advantages and disadvantages and is preferred for certain settings,
as summarized in [Table
1](#ch001.xhtml_robotics-02-00122-t001){.html-table}. The bottom row in
[Table 1](#ch001.xhtml_robotics-02-00122-t001){.html-table} indicates
our prediction about a hypothetical future approach, predicted based on
extrapolation from the existing approaches, as explained in [Section
10](#ch001.xhtml_sec10-robotics-02-00122){.html-sec}.

::: {#ch001.xhtml_robotics-02-00122-t001 .html-table_show .mfp-hide}
+------------------------------------------------+---------------+--------------+---------------------+
| Approach/method for teaching the robot         | Computational | Advantages   | Disadvantages       |
|                                                | complexity    |              |                     |
|                                                +---------------+              |                     |
|                                                | Difficult for |              |                     |
|                                                | the teacher   |              |                     |
+:============:+:============+:=================:+==============:+:=============+:====================+
| Existing     | **Direct programming** Manually | Lowest        | Complete     | Time-consuming,     |
| approaches   | specifying (programming) the    |               | control of   | error-prone, not    |
|              | robot how to move each joint    |               | the movement | scalable, not       |
|              |                                 |               | of the robot | reusable            |
|              |                                 |               | to the       |                     |
|              |                                 |               | lowest level |                     |
|              |                                 +---------------+              |                     |
|              |                                 | High          |              |                     |
|              +-------------+-------------------+---------------+--------------+---------------------+
|              | **Imitation | **Kinesthetic     | Low           | No need to   | Cannot perform fast |
|              | learning**  | teaching** and    |               | manually     | movements; can move |
|              |             | **Teleoperation** |               | program, can | usually only one    |
|              |             | Directly move the |               | just record  | limb at a time; the |
|              |             | robot's limbs or  |               | and replay   | robot has to be     |
|              |             | teleoperate to    |               | movements    | lightweight         |
|              |             | record the        |               |              |                     |
|              |             | movement          |               |              |                     |
|              |             |                   +---------------+              |                     |
|              |             |                   | Medium        |              |                     |
|              |             +-------------------+---------------+--------------+---------------------+
|              |             | **Observational   | Medium        | Easy and     | Correspondence      |
|              |             | learning**        |               | natural to   | problem caused by   |
|              |             | Demonstrate the   |               | demonstrate; | the different       |
|              |             | movement using    |               | also works   | embodiment; the     |
|              |             | the teacher's own |               | for bimanual | teacher must be     |
|              |             | body; perceive    |               | tasks or     | able to do the      |
|              |             | the movement      |               | even         | task; often         |
|              |             | using motion      |               | whole-body   | requires multiple   |
|              |             | capture systems   |               | motion       | demonstrations that |
|              |             | or video cameras  |               |              | need to be          |
|              |             |                   |               |              | segmented and       |
|              |             |                   |               |              | time-aligned        |
|              |             |                   +---------------+              |                     |
|              |             |                   | Low           |              |                     |
|              +-------------+-------------------+---------------+--------------+---------------------+
|              | **Reinforcement learning**      | Higher        | Robot can    | No control over the |
|              | Specify a scalar reward         |               | learn tasks  | actions of the      |
|              | function evaluating the robot's |               | that even    | robot; robot has    |
|              | performance that needs to be    |               | the human    | only indirect       |
|              | maximized; no need to           |               | cannot       | information about   |
|              | demonstrate how to perform the  |               | demonstrate; | the goal; need to   |
|              | task; the robot discovers this  |               | novel ways   | specify reward      |
|              | on its own                      |               | to reach a   | function, policy    |
|              |                                 |               | goal can be  | parameterization,   |
|              |                                 |               | discovered   | exploration         |
|              |                                 |               |              | magnitude/strategy, |
|              |                                 |               |              | initial policy      |
|              |                                 +---------------+              |                     |
|              |                                 | Lower         |              |                     |
+--------------+---------------------------------+---------------+--------------+---------------------+
| Hypothetical | **"Goal-directed learning"**    | Highest       | The easiest  | No control of the   |
|              | (predicted via extrapolation)   |               | way to       | movement of the     |
|              | Only specifying the goal that   |               | specify      | robot; must know    |
|              | the robot must achieve, without |               | (e.g., using | what the goal is    |
|              | evaluating the intermediate     |               | NLP); robot  | and how to formally |
|              | progress                        |               | has direct   | define it           |
|              |                                 |               | knowledge of |                     |
|              |                                 |               | the goal     |                     |
|              |                                 +---------------+              |                     |
|              |                                 | Lowest        |              |                     |
+--------------+---------------------------------+---------------+--------------+---------------------+

: **Table 1.** Comparison of the main robot teaching approaches.\
{style="width: 100% !important; border: none;" cellspacing="0"
align="left"}
:::
::::

::: html-p
The ultimate goal of these approaches is to give robots the ability to
learn, improve, adapt and reproduce tasks with dynamically changing
constraints. However, these approaches differ significantly from one
another:

- ::: html-p
  **Direct programming**: This is the lowest-level approach, but it is
  still being actively used in industrial settings, where the
  environment is well-structured and complete control over the precise
  movement of the robot is crucial. We add it for completeness, although
  it is not really a [teaching]{.html-italic} method; hence, we classify
  it as [programming]{.html-italic}. Industrial robots are usually
  equipped with the so-called [teach pendant]{.html-italic}---a device
  that is used to manually set the desired robot positions.
  :::

- ::: html-p
  **Imitation learning**: This approach is called
  [learning]{.html-italic} instead of [programming]{.html-italic}, in
  order to emphasize the active part that the agent (the robot) has in
  the process. This approach is also known as [programming by
  demonstration]{.html-italic}
  \[[1](#ch001.xhtml_B1-robotics-02-00122){.html-bibr}\] or [learning
  from demonstration]{.html-italic}
  \[[2](#ch001.xhtml_B2-robotics-02-00122){.html-bibr}\]. There are
  three main methods used to perform demonstrations for imitation
  learning:

  \-

  :   ::: html-p
      **Kinesthetic teaching**: This is the process of manually moving
      the robot's body and recording its motion
      \[[3](#ch001.xhtml_B3-robotics-02-00122){.html-bibr}\]. This
      approach usually works only for smaller, lightweight robots and in
      combination with a gravity-compensation controller, in order to
      minimize the apparent weight of the robot. However, nevertheless,
      since the robot's inertia cannot be effectively reduced, it is not
      practical for bigger robots. Kinesthetic teaching could be
      performed in a continuous way, recording whole trajectories, or
      alternatively, it could be performed by recording discrete
      snapshots of the robot's state at separate time instances, such as
      in keyframe-based teaching of sequences of key poses
      \[[4](#ch001.xhtml_B4-robotics-02-00122){.html-bibr}\].
      :::

  \-

  :   ::: html-p
      **Teleoperation**: This is the process of remotely controlling the
      robot's body using another input device, such as a joystick or a
      haptic device. This approach shares many similarities with
      kinesthetic teaching in terms of advantages and disadvantages. One
      big difference is that with teleoperation, the teacher can be
      located in a geographically distant location. However, time delays
      become an issue as the distance increases (e.g., teleoperating a
      Mars rover would be difficult). Similarly to kinesthetic teaching,
      only a limited number of degrees of freedom (DoFs) can be
      controlled at the same time. Furthermore, with teleoperation, it
      is more difficult to feel the limitations and capabilities of the
      robot than by using kinesthetic teaching. As an advantage,
      sometimes the setup could be simpler, and additional information
      can be displayed at the interface (e.g., forces rendered by the
      haptic device).
      :::

  \-

  :   ::: html-p
      **Observational learning**: In this method, the movement is
      demonstrated using the teacher's own body and is perceived using
      motion capture systems or video cameras or other sensors. It is
      usually needed to solve the correspondence problem
      \[[5](#ch001.xhtml_B5-robotics-02-00122){.html-bibr}\],
      [i.e.]{.html-italic}, to map the robot's kinematics to that of the
      teacher.
      :::
  :::

  ::: html-p
  The simplest way to use the demonstrations is to do a simple
  record-and-replay, which can only execute a particular instance of a
  task. However, using smart representation of the recorded movement in
  appropriate frame of reference (e.g., using the target object as the
  origin), it is possible to have somewhat adaptable skill to different
  initial configurations, for simple (mostly one-object) tasks. Based on
  multiple demonstrations that include variations of a task, the robot
  can calculate correlations and variance and figure out which part of a
  task is important to be repeated verbatim and which part is acceptable
  to be changed (and to what extent). Imitation learning has been
  successfully applied many times for learning tasks on robots, for
  which the human teacher can demonstrate a successful execution
  \[[3](#ch001.xhtml_B3-robotics-02-00122){.html-bibr},[6](#ch001.xhtml_B6-robotics-02-00122){.html-bibr}\].
  :::

- ::: html-p
  **Reinforcement learning (RL)**: This is the process of learning from
  trial-and-error
  \[[7](#ch001.xhtml_B7-robotics-02-00122){.html-bibr}\], by exploring
  the environment and the robot's own body. The goal in RL is specified
  by the [reward function]{.html-italic}, which acts as positive
  reinforcement or negative punishment depending on the performance of
  the robot with respect to the desired goal. RL has created a
  well-defined niche for its application in robotics
  \[[8](#ch001.xhtml_B8-robotics-02-00122){.html-bibr},[9](#ch001.xhtml_B9-robotics-02-00122){.html-bibr},[10](#ch001.xhtml_B10-robotics-02-00122){.html-bibr},[11](#ch001.xhtml_B11-robotics-02-00122){.html-bibr},[12](#ch001.xhtml_B12-robotics-02-00122){.html-bibr},[13](#ch001.xhtml_B13-robotics-02-00122){.html-bibr},[14](#ch001.xhtml_B14-robotics-02-00122){.html-bibr}\].
  The main motivation for using reinforcement learning to teach robots
  new skills is that it offers three previously missing abilities:
  :::

  \-

  :   ::: html-p
      to learn new tasks, which even the human teacher cannot physically
      demonstrate or cannot directly program (e.g., jump three meters
      high, lift heavy weights, move very fast, [etc.]{.html-italic});
      :::

  \-

  :   ::: html-p
      to learn to achieve optimization goals of difficult problems that
      have no analytic formulation or no known closed form solution,
      when even the human teacher does not know what the optimum is, by
      using only a known cost function (e.g., minimize the used energy
      for performing a task or find the fastest gait,
      [etc.]{.html-italic});
      :::

  \-

  :   ::: html-p
      to learn to adapt a skill to a new, previously unseen version of a
      task (e.g., learning to walk from flat ground to a slope, learning
      to generalize a task to new previously unseen parameter values,
      [etc.]{.html-italic}). Some imitation learning approaches can also
      do this, but in a much more restricted way (e.g., by adjusting
      parameters of a learned model, without being able to change the
      model itself).
      :::
:::

::: html-p
Reinforcement learning also offers some additional advantages. For
example, it is possible to start from a "good enough" demonstration and
gradually refine it. Another example would be the ability to dynamically
adapt to changes in the agent itself, such as a robot adapting to
hardware changes---heating up, mechanical wear, growing body parts,
[etc]{.html-italic}.
:::

::: html-p
This paper provides a summary of some of the main components for
applying reinforcement learning in robotics. We present some of the most
important classes of learning algorithms and classes of policies. We
give a comprehensive list of challenges for effective policy
representations for the application of policy-search RL to robotics and
provide three examples of tasks demonstrating how the policy
representation may address some of these challenges. The paper is a
significantly improved and extended version of our previous work in
\[[15](#ch001.xhtml_B15-robotics-02-00122){.html-bibr}\]. The novelties
include: new experimental section based on robotic archery task; new
section with insights about the future of RL in robotics; new comparison
of existing robot learning approaches and their respective advantages
and disadvantages; an expanded list of challenges for the policy
representation and more detailed description of use cases.
:::

::: html-p
The paper does not propose new algorithmic strategies. Rather, it
summarizes what our team has learned from a fairly extensive base of
empirical evidence over the last 4--5 years, aiming to serve as a
reference for the field of robot learning. While we may still dream of a
general purpose algorithm that would allow robots to learn optimal
policies without human guidance, it is likely that these are far off.
The paper describes several classes of policies that have proved to work
very well for a wide range of robot motor control tasks. The main
contribution of this work is a better understanding that the design of
appropriate policy representations is essential for RL methods to be
successfully applied to real-world robots.
:::

::: html-p
The paper is structured as follows. In [Section
2](#ch001.xhtml_sec2-robotics-02-00122){.html-sec}, we present an
overview of the most important recent RL algorithms that are being
successfully applied in robotics. Then, in [Section
3](#ch001.xhtml_sec3-robotics-02-00122){.html-sec}, we identify numerous
challenges posed by robotics on the RL policy representation, and in
[Section 4](#ch001.xhtml_sec4-robotics-02-00122){.html-sec}, we describe
the state-of-the-art policy representations. To illustrate some of these
challenges, and to propose adequate solutions to them, the three
consecutive [Section 5](#ch001.xhtml_sec5-robotics-02-00122){.html-sec},
[Section 6](#ch001.xhtml_sec6-robotics-02-00122){.html-sec} and [Section
7](#ch001.xhtml_sec7-robotics-02-00122){.html-sec}, give three
representative examples for real-world application of RL in robotics.
The examples are all based on the same RL algorithm, but each faces
different policy representation problems and, therefore, requires
different solutions. In [Section
8](#ch001.xhtml_sec8-robotics-02-00122){.html-sec}, we give a summary of
the three tasks and compare them to three other robot skill learning
tasks. Then, in [Section
9](#ch001.xhtml_sec9-robotics-02-00122){.html-sec}, we give insights
about the future perspective directions for RL based on these examples
and having in mind robotics, in particular, as the application. Finally,
in [Section 10](#ch001.xhtml_sec10-robotics-02-00122){.html-sec}, we
discuss potential future alternative methods for teaching robots new
tasks that might appear. We conclude with a brief peek into the future
of robotics, revealing, in particular, the potential wider need for RL.
:::
:::::::::::

::::::::: {#ch001.xhtml_sec2-robotics-02-00122 .section type=""}
## 2. State-of-the-Art Reinforcement Learning Algorithms in Robotics {#ch001.xhtml_state-of-the-art-reinforcement-learning-algorithms-in-robotics nested="1"}

::: html-p
Robot systems are naturally of high-dimensionality, having many degrees
of freedom (DoF), continuous states and actions and high noise. Because
of this, traditional RL approaches based on MDP/POMDP/discretized state
and action spaces have problems scaling up to work in robotics, because
they suffer severely from the curse of dimensionality. The first partial
successes in applying RL to robotics came with the function
approximation techniques, but the real "renaissance" came with the
policy-search RL methods.
:::

::: html-p
In policy-search RL, instead of working in the huge state/action spaces,
a smaller policy space is used, which contains all possible policies
representable with a certain choice of policy parameterization. Thus,
the dimensionality is drastically reduced and the convergence speed is
increased.
:::

::: html-p
Until recently, [policy-gradient algorithms]{.html-italic} (such as
Episodic Natural Actor-Critic eNAC
\[[16](#ch001.xhtml_B16-robotics-02-00122){.html-bibr}\] and Episodic
REINFORCE \[[17](#ch001.xhtml_B17-robotics-02-00122){.html-bibr}\]) have
been a well-established approach for implementing policy-search RL
\[[10](#ch001.xhtml_B10-robotics-02-00122){.html-bibr}\]. Unfortunately,
policy-gradient algorithms have certain shortcomings, such as high
sensitivity to the learning rate and exploratory variance.
:::

::: html-p
An alternative approach that has gained popularity recently derives from
the Expectation-Maximization (EM) algorithm. For example, Kober [et
al]{.html-italic}. proposed in
\[[18](#ch001.xhtml_B18-robotics-02-00122){.html-bibr}\] an episodic RL
algorithm, called PoWER ([policy learning by weighting exploration with
the returns]{.html-italic}). It is based on the EM algorithm and, thus,
has a major advantage over policy-gradient-based approaches: it does not
require a learning rate parameter. This is desirable, because tuning a
learning rate is usually difficult to do for control problems, but
critical for achieving good performance of policy-gradient algorithms.
PoWER also demonstrates superior performance in tasks learned directly
on a real robot, by applying an importance sampling technique to reuse
previous experience efficiently.
:::

::: html-p
Another state-of-the-art policy-search RL algorithm, called
[PI\^2]{.html-italic} ([policy improvement with path
integrals]{.html-italic}), was proposed by Theodorou [et
al]{.html-italic}. in
\[[19](#ch001.xhtml_B19-robotics-02-00122){.html-bibr}\], for learning
parameterized control policies based on the framework of stochastic
optimal control with path integrals. They derived update equations for
learning to avoid numerical instabilities, because neither matrix
inversions nor gradient learning rates are required. The approach
demonstrates significant performance improvements over gradient-based
policy learning and scalability to high-dimensional control problems,
such as control of a quadruped robot dog.
:::

::: html-p
Several search algorithms from the field of stochastic optimization have
recently found successful use for iterative policy improvement. Examples
of such approaches are the cross-entropy method (CEM)
\[[20](#ch001.xhtml_B20-robotics-02-00122){.html-bibr}\] and the
covariance matrix adaptation evolution strategy (CMA-ES)
\[[21](#ch001.xhtml_B21-robotics-02-00122){.html-bibr}\]. Although these
algorithms come from a different domain and are not well-established in
RL research, they seem to be a viable alternative for direct policy
search RL, as some recent findings suggest
\[[22](#ch001.xhtml_B22-robotics-02-00122){.html-bibr}\].
:::
:::::::::

:::::: {#ch001.xhtml_sec3-robotics-02-00122 .section type=""}
## 3. Challenges for the Policy Representation in Robotics {#ch001.xhtml_challenges-for-the-policy-representation-in-robotics nested="1"}

::: html-p
Only having a good policy-search RL algorithm is not enough for solving
real-world problems in robotics. Before any given RL algorithm can be
applied to learn a task on a robot, an appropriate [policy
representation]{.html-italic} (also called [policy
encoding]{.html-italic}) needs to be devised. This is important, because
the choice of policy representation determines what in principle can be
learned by the RL algorithm ([i.e.]{.html-italic}, the policy search
space), analogous to the way a hypothesis model determines what kind of
data a regression method can fit well. In addition, the policy
representation can have significant influence on the RL algorithm
itself, e.g., it can help or impede the convergence or influence the
variance of the generated policies.
:::

::: html-p
However, creating a good policy representation is not a trivial problem,
due to a number of serious [challenges]{.html-italic} posed by the high
requirements from a robotic system, such as:

- ::: html-p
  [smoothness]{.html-italic}---the policy representation needs to encode
  smooth, continuous trajectories, without sudden accelerations or
  jerks, in order to be safe for the robot itself and also to reduce its
  energy consumption. In some rare cases, though, such as in bang-bang
  control, sudden changes might be desirable;
  :::

- ::: html-p
  [safety]{.html-italic}---the policy should be safe, not only for the
  robot (in terms of joint limits, torque limits, work space
  restrictions, obstacles, [etc.]{.html-italic}), but also for the
  people around it;
  :::

- ::: html-p
  [gradual exploration]{.html-italic}---the representation should allow
  gradual, incremental exploration, so that the policy does not suddenly
  change by a lot; e.g., in state-action-based policies, changing the
  policy action at only a single state could cause a sudden dramatic
  change in the overall behavior of the system when following this new
  branch of the policy, which is not desirable neither for the robot,
  nor for the people around it. In some cases, though, a considerable
  step change might be necessary, e.g., a navigation task where a robot
  needs to decide whether to go left or right to avoid an obstacle;
  :::

- ::: html-p
  [scalability]{.html-italic}---to be able to scale up to high
  dimensions and for more complex tasks; e.g., a typical humanoid robot
  nowadays has well above 50 DoF;
  :::

- ::: html-p
  [compactness]{.html-italic}---despite the high DoF of robots, the
  policy should use very compact encoding, e.g., it is impossible to
  directly use all points on a trajectory as policy parameters;
  :::

- ::: html-p
  [adaptability]{.html-italic}---the policy parameterization should be
  adaptable to the complexity and fidelity of the task, e.g., lifting
  weights [vs]{.html-italic}. micro-surgery;
  :::

- ::: html-p
  [multi-resolution]{.html-italic}---different parts of the policy
  parameterization should allow different resolution/precision;
  :::

- ::: html-p
  [unbiasedness]{.html-italic}---the policy parameterization should work
  without prior knowledge about the solution being sought and without
  restricting unnecessarily the search scope for possible solutions;
  :::

- ::: html-p
  [prior/bias]{.html-italic}---whenever feasible, it should be possible
  to add prior information (also called [bias]{.html-italic}) in order
  to jump-start policy search approaches, as illustrated in some of the
  use cases in this paper;
  :::

- ::: html-p
  [regularization]{.html-italic}---the policy should allow one to
  incorporate regularization to guide the exploration towards desired
  types of policies;
  :::

- ::: html-p
  [time-independence]{.html-italic}---this is the property of a policy
  not to depend on precise time or position, in order to cope with
  unforeseen perturbations;
  :::

- ::: html-p
  [embodiment-agnostic]{.html-italic}---the representation should not
  depend on any particular embodiment of the robot, e.g.,
  joint-trajectory based policies cannot be transferred to another robot
  easily;
  :::

- ::: html-p
  [invariance]{.html-italic}---the policy should be an invariant
  representation of the task (e.g., rotation-invariant, scale-invariant,
  position-invariant, [etc.]{.html-italic});
  :::

- ::: html-p
  [correlations]{.html-italic}---the policy should encapsulate
  correlations between the control variables (e.g., actuator control
  signals), similar to the motor synergies found in animals;
  :::

- ::: html-p
  [globality]{.html-italic}---the representation should help the RL
  algorithm to avoid local minima;
  :::

- ::: html-p
  [periodicity]{.html-italic}---to be able to represent easily
  periodic/cyclic movements, which occur often in robotics (e.g., for
  locomotion---different walking gaits, for manipulation---wiping
  movements, [etc.]{.html-italic});
  :::

- ::: html-p
  [analyzability]{.html-italic}---facility to visualize and analyze the
  policy (e.g., proving its stability by poles analysis,
  [etc.]{.html-italic});
  :::

- ::: html-p
  [multi-dimensionality]{.html-italic}---to be able to use efficiently
  high-dimensional feedback without the need to convert it into a scalar
  value by using a weighted sum of components;
  :::

- ::: html-p
  [convergence]{.html-italic}---to help the RL algorithm to converge
  faster to the (possibly local) optima.
  :::
:::

::: html-p
A good policy representation should provide solutions to all of these
challenges. However, it is not easy to come up with such a policy
representation that satisfies all of them. In fact, the existing
state-of-the-art policy representations in robotics cover only subsets
of these requirements, as highlighted in the next section.
:::
::::::

:::::: {#ch001.xhtml_sec4-robotics-02-00122 .section type=""}
## 4. State-of-the-Art Policy Representations in Robotics {#ch001.xhtml_state-of-the-art-policy-representations-in-robotics nested="1"}

::: html-p
Traditionally, explicit time-dependent approaches, such as cubic splines
or higher-order polynomials, were used as policy representations. These,
however, are not autonomous, in the sense that they cannot cope easily
with perturbations (unexpected changes in the environment). Currently,
there are a number of efficient state-of-the-art representations
available to address this and many of the other challenges mentioned
earlier. We give three examples of such policy representations below:

- ::: html-p
  Guenter [et al]{.html-italic}. explored in
  \[[23](#ch001.xhtml_B23-robotics-02-00122){.html-bibr}\] the use of
  the [Gaussian Mixture Model]{.html-italic} (GMM) and [Gaussian Mixture
  Regression]{.html-italic} (GMR) to respectively compactly encode a
  skill and reproduce a generalized version of it. The model was
  initially learned by demonstration through
  [expectation-maximization]{.html-italic} techniques. RL was then used
  to move the Gaussian centers in order to alter the reproduced
  trajectory by regression. It was successfully applied to the imitation
  of constrained reaching movements, where the learned movement was
  refined in simulation to avoid an obstacle that was not present during
  the demonstration attempts.
  :::

- ::: html-p
  Kober and Peters explored in
  \[[24](#ch001.xhtml_B24-robotics-02-00122){.html-bibr}\] the use of
  [Dynamic Movement Primitives]{.html-italic} (DMP)
  \[[25](#ch001.xhtml_B25-robotics-02-00122){.html-bibr}\] as a compact
  representation of a movement. The DMP framework was originally
  proposed by Ijspeert [et al]{.html-italic}.
  \[[26](#ch001.xhtml_B26-robotics-02-00122){.html-bibr}\] and further
  extended in
  \[[25](#ch001.xhtml_B25-robotics-02-00122){.html-bibr},[27](#ch001.xhtml_B27-robotics-02-00122){.html-bibr}\].
  In DMP, a set of attractors is used to reach a target, whose influence
  is smoothly switched along the movement. The set of attractors is
  first learned by imitation, and a proportional-derivative controller
  is used to move sequentially towards the sequence of targets. RL is
  then used to explore the effect of changing the position of these
  attractors. The proposed approach was demonstrated with pendulum
  swing-up and ball-in-a-cup tasks
  \[[28](#ch001.xhtml_B28-robotics-02-00122){.html-bibr}\]. One of the
  first uses of motion primitives was in the work of Peters [et
  al]{.html-italic}. for a ball-batting experiment using the eNAC
  algorithm \[[29](#ch001.xhtml_B29-robotics-02-00122){.html-bibr}\].
  :::

- ::: html-p
  Pardo [et al]{.html-italic}. proposed in
  \[[30](#ch001.xhtml_B30-robotics-02-00122){.html-bibr}\] a framework
  to learn coordination for simple rest-to-rest movements, by taking
  inspiration of the motor coordination, joint synergies and the
  importance of coupling in motor control
  \[[31](#ch001.xhtml_B31-robotics-02-00122){.html-bibr},[32](#ch001.xhtml_B32-robotics-02-00122){.html-bibr},[33](#ch001.xhtml_B33-robotics-02-00122){.html-bibr}\].
  The authors suggested to start from a basic representation of the
  movement by considering point-to-point movements driven by a
  proportional-derivative controller, where each variable encoding the
  task is decoupled. They then extended the possibilities of movement by
  encapsulating coordination information in the representation. RL was
  then used to learn how to efficiently coordinate the set of variables,
  which were originally decoupled.
  :::
:::

::: html-p
Although these policy representations work reasonably well for specific
tasks, neither one of them manages to address all of the challenges
listed in the previous section, but only a different subset. In
particular, the challenges of [correlations]{.html-italic},
[adaptability]{.html-italic}, [multi-resolution]{.html-italic},
[globality]{.html-italic}, [multi-dimensionality]{.html-italic} and
[convergence]{.html-italic} are rarely addressed by the existing policy
representations.
:::

::: html-p
In the following three sections. we give three concrete examples of
tasks that pose such rarely-addressed challenges for the policy
representation, and we propose some possible solutions to them. The
three examples are: pancake flipping task, bipedal walking energy
minimization task and archery-based aiming task. In all examples, the
same EM-based RL algorithm is used (PoWER), but different policy
representations are devised to address the specific challenges of the
task at hand. Videos of the three presented robot experiments are
available online at: <http://kormushev.com/research/videos/>.
:::
::::::

::::::::::::::::::::::::::::::::::::::::: {#ch001.xhtml_sec5-robotics-02-00122 .section type=""}
## 5. Example A: Pancake Flipping Task {#ch001.xhtml_example-a-pancake-flipping-task nested="1"}

::: html-p
This example addresses mainly the [correlations]{.html-italic},
[compactness]{.html-italic} and [smoothness]{.html-italic} challenges
described in [Section
3](#ch001.xhtml_sec3-robotics-02-00122){.html-sec}. We present an
approach allowing a robot to acquire new motor skills by learning the
couplings across motor control variables. The demonstrated skill is
first encoded in a compact form through a modified version of DMP, which
encapsulates correlation information. RL is then used to modulate the
mixture of dynamical systems initialized from the user's demonstration
via weighted least-squares regression. The approach is evaluated on a
torque-controlled seven-DoF Barrett WAMrobotic arm. More implementation
details can be found in
\[[13](#ch001.xhtml_B13-robotics-02-00122){.html-bibr}\].
:::

::::::::: {#ch001.xhtml_sec5dot1-robotics-02-00122 .section type=""}
#### 5.1. Task Description {#ch001.xhtml_task-description .html-italic nested="2"}

:::::: html-p
The goal of the pancake flipping task is to first toss a pancake in the
air, so that it rotates 180°, and then to catch it with the frying pan.
Due to the complex dynamics of the task, it is unfeasible to try
learning it directly with [tabula rasa]{.html-italic} RL. Instead, a
person presents a demonstration of the task first via kinesthetic
teaching, which is then used to initialize the RL policy. The
experimental setup is shown in [Figure
1](#ch001.xhtml_robotics-02-00122-f001){.html-fig}.

::::: {#ch001.xhtml_robotics-02-00122-f001 .html-fig_show .mfp-hide}
::: html-caption
**Figure 1.** Experimental setup for the pancake flipping task. A
torque-controlled seven-DoF Barrett WAM robot learns to flip pancakes in
the air and catch them with a real frying pan attached to its
end-effector. Artificial pancakes with passive reflective markers are
used to evaluate the performance of the learned policy.
:::

::: html-img
![Robotics 02 00122 g001](media/file2.png)
:::
:::::
::::::

::: html-p
The pancake flipping task is difficult to learn from multiple
demonstrations, because of the high variability of the task execution,
even when the same person is providing the demonstrations. Extracting
the task constraints by observing multiple demonstrations is not
appropriate in this case for two reasons:

- ::: html-p
  when considering such skillful movements, extracting the regularities
  and correlations from multiple observations would be difficult, as
  consistency in the skill execution would appear only after the user
  has mastered the skill;
  :::

- ::: html-p
  the generalization process may smooth important acceleration peaks and
  sharp turns in the motion. Therefore, in such highly dynamic skillful
  tasks, early trials have shown that it was more appropriate to select
  a single successful demonstration (among a small series of trials) to
  initialize the learning process.
  :::
:::

::: html-p
A common missing part of most existing policy representations is the
lack of any coupling between the different variables. To address this
problem, we propose an approach that builds upon the works above by
taking into consideration the efficiency of DMP to encode a skill with a
reduced number of states and by extending the approach to take into
consideration local coupling information across the different variables.
:::
:::::::::

::::::::::::::: {#ch001.xhtml_sec5dot2-robotics-02-00122 .section type=""}
#### 5.2. Proposed Compact Encoding with Coupling {#ch001.xhtml_proposed-compact-encoding-with-coupling .html-italic nested="2"}

::: html-p
The proposed approach represents a movement as a superposition of basis
force fields, where the model is initialized from weighted least-squares
regression of demonstrated trajectories. RL is then used to adapt and
improve the encoded skill by learning optimal values for the policy
parameters. The proposed policy parameterization allows the RL algorithm
to learn the coupling across the different motor control variables.
:::

:::::: html-p
A demonstration consisting of [T]{.html-italic} positions,
[x]{.html-italic} in 3D, velocities, ![there is no
content](150104000359780d838fe18.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:1.33ex;max-width: 1.33ex;max-height:1.884ex"},
and accelerations, ![there is no
content](150104000359780d83ed9fa.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:1.33ex;max-width: 1.33ex;max-height:1.884ex"},
is shown to the robot. By considering flexibility and compactness
issues, we propose to use a controller based on a mixture of
[K]{.html-italic} proportional-derivative systems:

::::: {#ch001.xhtml_FD1-robotics-02-00122 .html-disp-formula-info}
::: f
`<mrow>`{=html}`<mover accent="true">`{=html}![there is no
content](150104000359780d83ed9fa.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:1.33ex;max-width: 1.33ex;max-height:1.884ex"}`<mo>`{=html}\^`</mo>`{=html}`</mover>`{=html}`<mo>`{=html}=`</mo>`{=html}`<munderover>`{=html}`<mo>`{=html}∑`</mo>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mi>`{=html}K`</mi>`{=html}`</munderover>`{=html}`<msub>`{=html}`<mi>`{=html}h`</mi>`{=html}`<mi>`{=html}i`</mi>`{=html}`</msub>`{=html}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}`<mi>`{=html}t`</mi>`{=html}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`<mfenced open="[" close="]">`{=html}![there
is no
content](150104000559780d85ad062.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.524ex;max-width: 3.524ex;max-height:2.759ex"}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}![there
is no
content](150104001859780d9273769.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:2.948ex;max-width: 2.948ex;max-height:2.759ex"}`<mo>`{=html}−`</mo>`{=html}`<mi>`{=html}x`</mi>`{=html}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`<mo>`{=html}−`</mo>`{=html}`<msup>`{=html}`<mi>`{=html}κ`</mi>`{=html}`<mstyle scriptlevel="2" displaystyle="false">`{=html}`<mi mathvariant="script">`{=html}V`</mi>`{=html}`</mstyle>`{=html}`</msup>`{=html}![there
is no
content](150104000359780d838fe18.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:1.33ex;max-width: 1.33ex;max-height:1.884ex"}`</mfenced>`{=html}`</mrow>`{=html}
:::

::: l
`<label>`{=html}(1)`</label>`{=html}
:::
:::::
::::::

::: html-p
The above formulation shares similarities with the DMP framework. The
difference is that the non-linear force of DMP is considered as
resulting from a set of virtual springs, adding local corrective terms
to swiftly react to perturbations
\[[34](#ch001.xhtml_B34-robotics-02-00122){.html-bibr}\]. Here, we
extend the use of DMP by considering synergy across the different motion
variables through the association of a full matrix, ![there is no
content](150104000559780d85ad062.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.524ex;max-width: 3.524ex;max-height:2.759ex"},
with each of the [K]{.html-italic} primitives (or states) instead of a
fixed ![there is no
content](150104000659780d860fad2.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:2.769ex;max-width: 2.769ex;max-height:2.134ex"}
gain.
:::

::: html-p
The superposition of basis force fields is determined in Equation
([1](#ch001.xhtml_FD1-robotics-02-00122){.html-disp-formula}) by an
implicit time dependency, but other forms of activation weights can also
be used. For example, we showed in
\[[35](#ch001.xhtml_B35-robotics-02-00122){.html-bibr}\] that the
representation in Equation
([1](#ch001.xhtml_FD1-robotics-02-00122){.html-disp-formula}) could also
be used with activation weights based on spatial inputs instead of
temporal inputs, used to encode reaching behaviors modulated by the
position of objects.
:::

:::::: html-p
Similarly to DMP, a decay term defined by a canonical system, ![there is
no
content](150104000659780d86653d7.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:8.776ex;max-width: 8.776ex;max-height:2.134ex"},
is used to create an implicit time dependency, ![there is no
content](150104000659780d86bc0b0.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.759ex;width:10.109ex;max-width: 10.109ex;max-height:3.759ex"},
where [s]{.html-italic} is initialized with ![there is no
content](150104000759780d871cb88.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.009ex;width:5.351ex;max-width: 5.351ex;max-height:2.009ex"}
and converges to zero. We define a set of Gaussians, ![there is no
content](150104000759780d87728a0.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.134ex;width:11.829ex;max-width: 11.829ex;max-height:3.134ex"},
in time space, ![there is no
content](150104000759780d87c7d92.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.634ex;width:1.637ex;max-width: 1.637ex;max-height:1.634ex"},
with centers, ![there is no
content](150104000859780d882d7e0.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:2.791ex;max-width: 2.791ex;max-height:2.759ex"},
equally distributed in time, and variance parameters, ![there is no
content](150104000859780d8881607.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.068ex;max-width: 3.068ex;max-height:2.759ex"},
set to a constant value inversely proportional to the number of
Gaussians. This set is used as a set of Gaussian basis functions. The
scalar, [α]{.html-italic}, is fixed depending on the duration of the
demonstrations. The weights are defined by:

::::: {#ch001.xhtml_FD2-robotics-02-00122 .html-disp-formula-info}
::: f
`<mrow>`{=html}`<msub>`{=html}`<mi>`{=html}h`</mi>`{=html}`<mi>`{=html}i`</mi>`{=html}`</msub>`{=html}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}`<mi>`{=html}t`</mi>`{=html}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mfrac>`{=html}`<mrow>`{=html}`<mi mathvariant="script">`{=html}N`</mi>`{=html}`<mo>`{=html}(`</mo>`{=html}`<mi>`{=html}t`</mi>`{=html}`<mo>`{=html};`</mo>`{=html}`<mspace width="0.277778em">`{=html}`</mspace>`{=html}![there
is no
content](150104000859780d882d7e0.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:2.791ex;max-width: 2.791ex;max-height:2.759ex"}`<mo>`{=html},`</mo>`{=html}![there
is no
content](150104000859780d8881607.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.068ex;max-width: 3.068ex;max-height:2.759ex"}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<msubsup>`{=html}`<mo>`{=html}∑`</mo>`{=html}`<mrow>`{=html}`<mi>`{=html}k`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mi>`{=html}K`</mi>`{=html}`</msubsup>`{=html}`<mi mathvariant="script">`{=html}N`</mi>`{=html}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}`<mi>`{=html}t`</mi>`{=html}`<mo>`{=html};`</mo>`{=html}`<mspace width="0.277778em">`{=html}`</mspace>`{=html}`<msubsup>`{=html}`<mi>`{=html}μ`</mi>`{=html}`<mi>`{=html}k`</mi>`{=html}`<mstyle scriptlevel="2" displaystyle="false">`{=html}`<mi mathvariant="script">`{=html}T`</mi>`{=html}`</mstyle>`{=html}`</msubsup>`{=html}`<mo>`{=html},`</mo>`{=html}`<msubsup>`{=html}`<mo>`{=html}Σ`</mo>`{=html}`<mi>`{=html}k`</mi>`{=html}`<mstyle scriptlevel="2" displaystyle="false">`{=html}`<mi mathvariant="script">`{=html}T`</mi>`{=html}`</mstyle>`{=html}`</msubsup>`{=html}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`</mrow>`{=html}`</mfrac>`{=html}`</mrow>`{=html}
:::

::: l
`<label>`{=html}(2)`</label>`{=html}
:::
:::::
::::::

::: html-p
In Equation
([1](#ch001.xhtml_FD1-robotics-02-00122){.html-disp-formula}),
`<msubsup>`{=html}`<mrow>`{=html}`<mo>`{=html}{`</mo>`{=html}![there is
no
content](150104000559780d85ad062.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.524ex;max-width: 3.524ex;max-height:2.759ex"}`<mo>`{=html}}`</mo>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mi>`{=html}K`</mi>`{=html}`</msubsup>`{=html}
is a set of full stiffness matrices, which we refer to as [coordination
matrices]{.html-italic}. Using the full coordination matrices (not only
their diagonal elements) allows us to consider different types of
synergies across the variables, where each state/primitive encodes local
correlation information. Both attractor vectors, ![there is no
content](150104001059780d8a91439.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.759ex;width:8.559ex;max-width: 8.559ex;max-height:3.759ex"},
and coordination matrices,
`<msubsup>`{=html}`<mrow>`{=html}`<mo>`{=html}{`</mo>`{=html}![there is
no
content](150104000559780d85ad062.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.524ex;max-width: 3.524ex;max-height:2.759ex"}`<mo>`{=html}}`</mo>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mi>`{=html}K`</mi>`{=html}`</msubsup>`{=html},
in Equation
([1](#ch001.xhtml_FD1-robotics-02-00122){.html-disp-formula}) are
initialized from the observed data through weighted least-squares
regression (see \[[13](#ch001.xhtml_B13-robotics-02-00122){.html-bibr}\]
for details).
:::
:::::::::::::::

::::::::: {#ch001.xhtml_sec5dot3-robotics-02-00122 .section type=""}
#### 5.3. Experiment {#ch001.xhtml_experiment .html-italic nested="2"}

::: html-p
Custom-made artificial pancakes are used, whose position and orientation
are tracked in real-time by a reflective marker-based [NaturalPoint
OptiTrack]{.html-italic} motion capture system.
:::

:::::: html-p
The return of a [rollout]{.html-italic}, [τ]{.html-italic} (also called
trial), is calculated from the time-step reward, ![there is no
content](150104001159780d8b5062c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:3.698ex;max-width: 3.698ex;max-height:2.634ex"}.
It is defined as a weighted sum of two criteria (orientational reward
and positional reward), which encourage successful flipping and
successful catching of the pancake:

::::: {#ch001.xhtml_FD3-robotics-02-00122 .html-disp-formula-info}
::: f
![there is no
content](150104001259780d8cafee2.png){style="border: none;vertical-align: middle; height:7.384ex;width:54.554ex;max-width: 54.554ex;max-height:7.384ex"}
:::

::: l
`<label>`{=html}(3)`</label>`{=html}
:::
:::::

where ![there is no
content](150104001359780d8d1161b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.464ex;max-width: 2.464ex;max-height:1.759ex"}
are weights, ![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"}
is the moment when the pancake passes, with a downward direction, the
horizontal level at a fixed height, ![there is no
content](150104001359780d8dbc20b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:3.115ex;max-width: 3.115ex;max-height:2.384ex"},
above the frying pan's current vertical position, ![there is no
content](150104001459780d8e256ce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:2.182ex;max-width: 2.182ex;max-height:1.884ex"}
is the initial orientation of the pancake (represented by a unit vector
perpendicular to the pancake),
`<msub>`{=html}`<mi>`{=html}v`</mi>`{=html}![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"}`</msub>`{=html}
is the orientation of the pancake at time, ![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"},
![there is no
content](150104001559780d8f3ab62.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:2.796ex;max-width: 2.796ex;max-height:2.384ex"}
is the position of the pancake center at time, ![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"},
![there is no
content](150104001559780d8fea9d1.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:2.793ex;max-width: 2.793ex;max-height:2.384ex"}
is the position of the frying pan center at time, ![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"},
and ![there is no
content](150104001659780d909f185.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.009ex;width:3.289ex;max-width: 3.289ex;max-height:3.009ex"}
is the maximum reached altitude of the pancake. The first term is
maximized when the pancake's orientation (represented as a normal
vector) at time, ![there is no
content](150104001359780d8d66bce.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.509ex;width:1.976ex;max-width: 1.976ex;max-height:2.509ex"},
points in the opposite direction of the initial orientation, which
happens in a successful flip. The second term is maximized when the
pancake lands close to the center of the frying pan.
::::::

::: html-p
To learn new values for the coordination matrices, the RL algorithm
PoWER is used. The policy parameters, ![there is no
content](150104001759780d9161644.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:2.309ex;max-width: 2.309ex;max-height:2.384ex"},
for the RL algorithm are composed of two sets of variables: the first
set contains the full
`<mrow>`{=html}`<mn>`{=html}3`</mn>`{=html}`<mspace width="0.166667em">`{=html}`</mspace>`{=html}`<mo>`{=html}×`</mo>`{=html}`<mspace width="0.166667em">`{=html}`</mspace>`{=html}`<mn>`{=html}3`</mn>`{=html}`</mrow>`{=html}
coordination matrices, ![there is no
content](150104000559780d85ad062.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.524ex;max-width: 3.524ex;max-height:2.759ex"},
with the positional error gains in the main diagonal and the
coordination gains in the off-diagonal elements; the second set contains
the vectors, ![there is no
content](150104001859780d9273769.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:2.948ex;max-width: 2.948ex;max-height:2.759ex"},
with the attractor positions for the primitives.
:::
:::::::::

:::::::::::: {#ch001.xhtml_sec5dot4-robotics-02-00122 .section type=""}
#### 5.4. Experimental Results {#ch001.xhtml_experimental-results .html-italic nested="2"}

::::::::: html-p
In practice, around 60 rollouts were necessary to find a good policy
that can reproducibly flip the pancake without dropping it. [Figure
2](#ch001.xhtml_robotics-02-00122-f002){.html-fig} shows a recorded
sample rollout from the RL exploration, during which the pancake rotated
fully 180° and was caught successfully with the frying pan. The video
frame sequence from a successful 180° flipping rollout is shown in
[Figure 3](#ch001.xhtml_robotics-02-00122-f003){.html-fig}.

::::: {#ch001.xhtml_robotics-02-00122-f002 .html-fig_show .mfp-hide}
::: html-caption
**Figure 2.** Visualization of a real-world pancake flipping rollout
(trial) performed by the robot. The pancake (in yellow) was successfully
tossed and caught with the frying pan, and it rotated 180° (for better
visibility of the pancake's trajectory, the frying pan is not displayed
here). The trajectory of the end-effector is displayed with black dots
and its orientation (represented by the normal vector) with blue arrows.
The normal vectors perpendicular to the pancake are shown with black
arrows.
:::

::: html-img
![Robotics 02 00122 g002](media/file4.png)
:::
:::::

::::: {#ch001.xhtml_robotics-02-00122-f003 .html-fig_show .mfp-hide}
::: html-caption
**Figure 3.** Sequence of video frames showing a successful pancake
flipping, performed on the WAM robot.
:::

::: html-img
![Robotics 02 00122 g003](media/file6.png)
:::
:::::
:::::::::

::: html-p
It is interesting to notice the up-down bouncing of the frying pan
towards the end of the learned skill, when the pancake has just fallen
inside of it. The bouncing behavior is due to the increased compliance
of the robot during this part of the movement. This was produced by the
RL algorithm in an attempt to catch the fallen pancake inside the frying
pan. Without it, if a controller is too stiff, it would cause the
pancake to bounce off from the surface of the frying pan and fall out of
it. Such unintentional discoveries made by the RL algorithm highlight
its important role for achieving adaptable and flexible robots.
:::

::: html-p
In summary, the proposed policy parameterization based on superposition
of basis force fields demonstrates three major advantages:

- ::: html-p
  it provides a mechanism for learning the couplings across multiple
  motor control variables, thus addressing the
  [correlations]{.html-italic} challenge;
  :::

- ::: html-p
  it highlights the advantages of using correlations in RL for reducing
  the size of the representation, thus addressing the
  [compactness]{.html-italic} challenge;
  :::

- ::: html-p
  it demonstrates that even fast, dynamic tasks can still be represented
  and executed in a safe-for-the-robot manner, addressing the
  [smoothness]{.html-italic} challenge.
  :::
:::
::::::::::::
:::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::: {#ch001.xhtml_sec6-robotics-02-00122 .section type=""}
## 6. Example B: Bipedal Walking Energy Minimization Task {#ch001.xhtml_example-b-bipedal-walking-energy-minimization-task nested="1"}

::: html-p
In this example, we address mainly the [adaptability]{.html-italic},
[multi-resolution]{.html-italic} and [globality]{.html-italic}
challenges described in [Section
3](#ch001.xhtml_sec3-robotics-02-00122){.html-sec}. Adaptive resolution
methods [in state space]{.html-italic} have been studied in RL before
(see e.g., \[[36](#ch001.xhtml_B36-robotics-02-00122){.html-bibr}\]).
They address the pitfalls of discretization during reinforcement
learning and show that in high dimensions, it is better if the learning
is not planned uniformly over the state space. For example, in
\[[37](#ch001.xhtml_B37-robotics-02-00122){.html-bibr}\], Moore [et
al]{.html-italic}. employed a decision-tree partitioning of state-space
and applied techniques from game-theory and computational geometry to
efficiently and adaptively concentrate high resolution on critical
areas.
:::

::: html-p
However, in the context of RL, adaptive resolution [in policy
parameterization]{.html-italic} remains largely unexplored, so far. To
address this challenge, we present a policy parameterization that can
evolve dynamically, while the RL algorithm is running without losing
information about past experience. We show that the gradually increasing
representational power of the policy parameterization helps to find
better policies faster than a fixed parameterization. The particular
problem at hand is an energy minimization problem for a bipedal walking
task. More implementation details can be found in
\[[38](#ch001.xhtml_B38-robotics-02-00122){.html-bibr}\].
:::

:::::::::: {#ch001.xhtml_sec6dot1-robotics-02-00122 .section type=""}
#### 6.1. Energy Minimization Problem {#ch001.xhtml_energy-minimization-problem .html-italic nested="2"}

:::::: html-p
Recent advances in robotics and mechatronics have allowed for the
creation of a new generation of passively-compliant robots, such as the
humanoid robot, COMAN(derived from the cCubbipedal robot
\[[39](#ch001.xhtml_B39-robotics-02-00122){.html-bibr}\]), shown in
[Figure 4](#ch001.xhtml_robotics-02-00122-f004){.html-fig}.

::::: {#ch001.xhtml_robotics-02-00122-f004 .html-fig_show .mfp-hide}
::: html-caption
**Figure 4.** The experimental setup for the bipedal walking energy
minimization task, showing a snapshot of the lower body of the compliant
humanoid robot, COMAN, during one walking rollout.
:::

::: html-img
![Robotics 02 00122 g004](media/file8.png)
:::
:::::
::::::

::: html-p
Such robots have springs that can store and release energy and are
essential for reducing the energy consumption and for achieving
mechanical power peaks. However, it is difficult to manually engineer an
optimal way to use the passive compliance for dynamic and variable
tasks, such as walking. For instance, the walking energy minimization
problem is very challenging, because it is nearly impossible to be
solved analytically, due to the difficulty in modeling accurately the
properties of the springs, the dynamics of the whole robot and various
nonlinearities of its parts. In this section, we apply RL to learn to
minimize the energy consumption required for walking of this
passively-compliant bipedal robot.
:::

::: html-p
The vertical center of mass (CoM) movement is a crucial factor in
reducing the energy consumption. Therefore, the proposed RL method is
used to learn an optimal vertical trajectory for the center of mass
(CoM) of the robot to be used during walking, in order to minimize the
energy consumption. In order to apply RL in robotics to optimize the
movement of the robot, first, the trajectory needs to be represented
(encoded) in some way. This particular experiment is based on cubic
splines. Similar approaches have been investigated before in robotics
under the name [via-points]{.html-italic}
\[[40](#ch001.xhtml_B40-robotics-02-00122){.html-bibr},[41](#ch001.xhtml_B41-robotics-02-00122){.html-bibr},[42](#ch001.xhtml_B42-robotics-02-00122){.html-bibr}\].
:::

::: html-p
However, there is a problem with applying a fixed policy
parameterization RL to such a complex optimization problem.
:::
::::::::::

::::: {#ch001.xhtml_sec6dot2-robotics-02-00122 .section type=""}
#### 6.2. Problems with Fixed Policy Parameterization {#ch001.xhtml_problems-with-fixed-policy-parameterization .html-italic nested="2"}

::: html-p
In policy-search RL, in order to find a good solution, the policy
parameterization has to be powerful enough to represent a large enough
policy space, so that a good candidate solution is present in it. If the
policy parameterization is too simple, with only a few parameters, then
the convergence is quick, but often a sub-optimal solution is reached.
If the policy parameterization is overly complex, the convergence is
slow, and there is a higher possibility that the learning algorithm will
converge to some local optimum, possibly much worse than the global
optimum. The level of sophistication of the policy parameterization
should be just the right amount, in order to provide both fast
convergence and a good enough solution.
:::

::: html-p
Deciding what policy parameterization to use and how simple/complex it
should be is a very difficult task, often performed via trial-and-error
manually by the researchers. This additional overhead is usually not
even mentioned in reinforcement learning papers and falls into the
category of "empirically tuned" parameters, together with the reward
function, decay factor, exploration noise, weights, [etc.]{.html-italic}
Since changing the policy parameterization requires restarting the
learning from scratch, throwing away all accumulated data, this process
is slow and inefficient. As a consequence, the search for new solutions
often cannot be done directly on a real-world robot system and requires,
instead, the use of simulations, which are not accurate enough.
:::
:::::

::::::: {#ch001.xhtml_sec6dot3-robotics-02-00122 .section type=""}
#### 6.3. Evolving Policy Parameterization {#ch001.xhtml_evolving-policy-parameterization .html-italic nested="2"}

::: html-p
To solve this problem, we propose an approach that allows us to change
the complexity of the policy representation dynamically, while the
reinforcement learning is running, without losing any of the collected
data and without having to restart the learning. We propose a mechanism
that can incrementally "evolve" the policy parameterization as
necessary, starting from a very simple parameterization and gradually
increasing its complexity and, thus, its representational power. The
goal is to create an adaptive policy parameterization, which can
automatically "grow" to accommodate increasingly more complex policies
and get closer to the global optimum.
:::

::: html-p
A very desirable side effect of this is that the tendency of converging
to a sub-optimal solution will be reduced, because in the
lower-dimensional representations, this effect is less exhibited, and
gradual increasing the complexity of the parameterization helps us not
to get caught in a poor local optimum. A drawback of such an approach is
that an informed initialization would be harder, depending on the
expressive power of the initial parameterization.
:::

::: html-p
The main difficulty to be solved is providing backward compatibility,
[i.e.]{.html-italic}, how to design the subsequent policy
representations in such a way that they are backward-compatible with the
previously collected data, such as past rollouts and their corresponding
policies and rewards. One of the simplest representations that have the
property of backward compatibility are the geometric splines. For
example, if we have a cubic spline with [K]{.html-italic} knots, and
then we increase the number of knots, we can still preserve the shape of
the generated curve (trajectory) by the spline. In fact, if we put one
additional knot between every two consecutive knots of the original
spline, we end up with ![there is no
content](150104001859780d92c4724.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:7.231ex;max-width: 7.231ex;max-height:2.134ex"}
knots and a spline that coincides with the original spline. Based on
this, the idea we propose is to use the spline knots as a policy
parameterization and use the spline backward compatibility property for
evolving the policy parameterization without losing the previously
collected data.
:::

::: html-p
The proposed technique for evolving the policy parameterization can be
used with any policy-search RL algorithm. For this particular
implementation, we use PoWER, due to its low number of parameters that
need tuning. Different techniques can be used to trigger the increase in
the number of knots of the spline representation. For this example, we
used a fixed, pre-determined trigger, activating at regular time
intervals.
:::
:::::::

::::::::::::::: {#ch001.xhtml_sec6dot4-robotics-02-00122 .section type=""}
#### 6.4. Evaluation of Evolving Policy Parameterization {#ch001.xhtml_evaluation-of-evolving-policy-parameterization .html-italic nested="2"}

::: html-p
In order to evaluate the proposed evolving policy parameterization, we
conduct a function approximation experiment. The goal is to compare the
proposed method with a conventional fixed policy parameterization method
that uses the same reinforcement learning algorithm as a baseline.
:::

:::::: html-p
For this experiment, the reward function is defined as follows:

::::: {#ch001.xhtml_FD4-robotics-02-00122 .html-disp-formula-info}
::: f
![there is no
content](150104001959780d932fc5d.png){style="border: none;vertical-align: middle; height:3.509ex;width:23.42ex;max-width: 23.42ex;max-height:3.509ex"}
:::

::: l
`<label>`{=html}(4)`</label>`{=html}
:::
:::::

where ![there is no
content](150104001959780d9386368.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:4.775ex;max-width: 4.775ex;max-height:2.634ex"}
is the return of a rollout (the policy-generated trajectory),
[τ]{.html-italic}, and ![there is no
content](150104001959780d93e0eba.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:1.368ex;max-width: 1.368ex;max-height:1.884ex"}
is the (unknown to the learning algorithm) function that the algorithm
is trying to approximate.
::::::

::::::::: html-p
[Figure 5](#ch001.xhtml_robotics-02-00122-f005){.html-fig} shows a
comparison of the generated policy output produced by the proposed
evolving policy parameterization method, compared with the output from
the conventional fixed policy parameterization method. [Figure
6](#ch001.xhtml_robotics-02-00122-f006){.html-fig} shows that the
convergence properties of the proposed method are significantly better
than the conventional approach.

::::: {#ch001.xhtml_robotics-02-00122-f005 .html-fig_show .mfp-hide}
::: html-caption
**Figure 5.** Comparison of the policy output from RL with fixed policy
parameterization (30-knot spline) [versus]{.html-italic} evolving policy
parameterization (from four- to 30-knot spline). In black, the unknown
to the algorithm global optimum, which it is trying to approximate. In
green, all the rollouts performed during the learning process. In red,
the current locally-optimal discovered policy by each reinforcement
learning (RL) algorithm. Due to the lower policy-space dimensionality at
the beginning, the evolving policy parameterization approaches the shape
of the globally-optimal trajectory much faster. The fixed policy
parameterization suffers from inefficient exploration, due to the high
dimensionality, as well as from overfitting problems, as seen by the
high-frequency oscillations of the discovered policies. (**a**) Fixed
policy parameterization; (**b**) Evolving policy parameterization.
:::

::: html-img
![Robotics 02 00122 g005](media/file10.png)
:::
:::::

::::: {#ch001.xhtml_robotics-02-00122-f006 .html-fig_show .mfp-hide}
::: html-caption
**Figure 6.** Comparison of the convergence of the RL algorithm with
fixed policy parameterization (30-knot spline) [versus]{.html-italic}
evolving policy parameterization (from four- to 30-knot spline). The
results are averaged over 20 runs of each of the two algorithms. The
standard deviation is indicated with error bars. In addition to faster
convergence and higher achieved rewards, the evolving policy
parameterization also achieves lower variance compared to the fixed
policy parameterization.
:::

::: html-img
![Robotics 02 00122 g006](media/file12.png)
:::
:::::
:::::::::
:::::::::::::::

:::::::::::: {#ch001.xhtml_sec6dot5-robotics-02-00122 .section type=""}
#### 6.5. Bipedal Walking Experiment {#ch001.xhtml_bipedal-walking-experiment .html-italic nested="2"}

::: html-p
For the real-world bipedal walking experiment, we use the lower body of
the passively-compliant humanoid robot, COMAN, which has 17 DoF. The
experimental setup is shown in [Figure
4](#ch001.xhtml_robotics-02-00122-f004){.html-fig}.
:::

::: html-p
To generate trajectories for the robot joints, we use a custom
variable-height bipedal walking generator. Given the z-axis CoM
trajectory provided by the RL, we use the ZMP (Zero Moment Point)
concept for deriving the x- and y-axis CoM trajectories.
:::

:::::: html-p
To calculate the reward, we measure the actual electrical energy used by
the motors of the robot. The return of a rollout, [τ]{.html-italic},
depends on the average electric energy consumed per walking cycle and is
defined as:

::::: {#ch001.xhtml_FD5-robotics-02-00122 .html-disp-formula-info}
::: f
![there is no
content](150104002059780d94488b6.png){style="border: none;vertical-align: middle; height:3.509ex;width:24.064ex;max-width: 24.064ex;max-height:3.509ex"}
:::

::: l
`<label>`{=html}(5)`</label>`{=html}
:::
:::::

where [J]{.html-italic} is the set of joints whose energy consumption we
try to minimize, ![there is no
content](150104002059780d949fc56.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:9.643ex;max-width: 9.643ex;max-height:2.759ex"}
is the accumulated consumed electric energy for the motor of the
[j]{.html-italic}-th individual joint of COMAN and [k]{.html-italic} is
a scaling constant. To reduce the effect of noise on the measurement,
for each rollout, the robot walks for 16 s (from time ![there is no
content](150104002159780d9506baa.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:1.894ex;max-width: 1.894ex;max-height:2.134ex"}
to ![there is no
content](150104002159780d95625da.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:1.894ex;max-width: 1.894ex;max-height:2.134ex"}),
which corresponds to eight steps (![there is no
content](150104002159780d95b7711.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.009ex;width:5.268ex;max-width: 5.268ex;max-height:2.009ex"}
walking cycles).
::::::

::: html-p
The learning converged after 150 rollouts. The total cumulative distance
traveled by the robot during our experiments was 0.5 km. The discovered
optimal policy by the RL algorithm, for which the lowest energy
consumption was achieved, consumes 18% less energy than a conventional
fixed-height walking, which is a significant improvement.
:::

::: html-p
In summary, the proposed evolving policy parameterization demonstrates
three major advantages:

- ::: html-p
  it achieves faster convergence and higher rewards than the fixed
  policy parameterization, using varying resolution for the policy
  parameterization, thus addressing the [adaptability]{.html-italic} and
  [multi-resolution]{.html-italic} challenges;
  :::

- ::: html-p
  it exhibits much lower variance of the generated policies, addressing
  the [gradual exploration]{.html-italic} challenge;
  :::

- ::: html-p
  it helps to avoid local minima, thus addressing the
  [globality]{.html-italic} challenge.
  :::
:::

::: html-p
The described approach has been successfully applied also to other robot
locomotion tasks, such as learning to optimize the walking speed of a
quadruped robot
\[[43](#ch001.xhtml_B43-robotics-02-00122){.html-bibr}\].
:::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::: {#ch001.xhtml_sec7-robotics-02-00122 .section type=""}
## 7. Example C: Archery-Based Aiming Task {#ch001.xhtml_example-c-archery-based-aiming-task nested="1"}

::: html-p
This example addresses mainly the [multi-dimensionality]{.html-italic}
and [convergence speed]{.html-italic} challenges described in [Section
3](#ch001.xhtml_sec3-robotics-02-00122){.html-sec}. We show that RL in
combination with regression yields an extremely fast-converging
algorithm, and we demonstrate it in practice using the iCubhumanoid
robot to quickly learn the skill of archery.
:::

::: html-p
The goal of this example is to develop an integrated approach allowing
the humanoid robot, iCub, to learn the skill of archery. After being
instructed how to hold the bow and release the arrow, the robot learns
by itself to shoot the arrow in such a way that it hits the center of
the target. Two learning algorithms are introduced and compared to learn
the bi-manual skill: one with Expectation-Maximization-based
reinforcement Learning and one with chained vector regression, called
the Augmented Reward Chained Regression (ARCHER) algorithm. Both
algorithms are used to modulate and coordinate the motion of the two
hands, while an inverse kinematics controller is used for the motion of
the arms. The approach is evaluated on the humanoid robot, iCub, where
only the upper body is used for the experiment (38 DoF). The image
processing part recognizes where the arrow hits the target and is based
on Gaussian Mixture Models for color-based detection of the target and
the arrow's tip. More implementation details can be found in
\[[14](#ch001.xhtml_B14-robotics-02-00122){.html-bibr}\].
:::

:::::: {#ch001.xhtml_sec7dot1-robotics-02-00122 .section type=""}
#### 7.1. Description of the Archery Task {#ch001.xhtml_description-of-the-archery-task .html-italic nested="2"}

::: html-p
The archery task is challenging because: (1) it involves bi-manual
coordination; (2) it can be performed with slow movements of the arms
and using small torques and forces; (3) it requires using tools (bow and
arrow) to affect an external object (target); (4) it is an appropriate
task for testing different learning algorithms and aspects of learning,
because the reward is inherently defined by the high-level description
of the task goal; (5) it involves integration of image processing, motor
control and learning parts in one coherent task.
:::

::: html-p
The focus of this task is on learning the bi-manual coordination
necessary to control the shooting direction and velocity in order to hit
the target. Two learning algorithms are introduced and compared: one
with Expectation-Maximization-based reinforcement Learning and one with
chained vector regression. Both algorithms are used to modulate and
coordinate the motion of the two hands, while an inverse kinematics
controller is used for the motion of the arms. We propose solutions to
the learning part, the image processing part used to detect the arrow's
tip on the target and the motor control part of the archery training.
:::

::: html-p
In the following two subsections, we introduce two different learning
algorithms for the archery training. The focus of the proposed approach
falls on learning the bi-manual coordination for shooting the arrow with
a desired direction and velocity.
:::
::::::

::::::::: {#ch001.xhtml_sec7dot2-robotics-02-00122 .section type=""}
#### 7.2. Learning Algorithm 1: PoWER {#ch001.xhtml_learning-algorithm-1-power .html-italic nested="2"}

::: html-p
As a first approach for learning the bi-manual coordination needed in
archery, we use the state-of-the-art EM-based RL algorithm, PoWER, by
Kober [et al]{.html-italic}.
\[[18](#ch001.xhtml_B18-robotics-02-00122){.html-bibr}\]. We selected
the PoWER algorithm, because it does not need a learning rate (unlike
policy-gradient methods) and also because it can be combined with
importance sampling to make better use of the previous experience of the
agent in the estimation of new exploratory parameters.
:::

::: html-p
PoWER uses a parameterized policy and tries to find values for the
parameters that maximize the expected return of rollouts (also called
trials) under the corresponding policy. For the archery task, the policy
parameters are represented by the elements of a 3D vector corresponding
to the relative position of the two hands performing the task.
:::

:::::: html-p
We define the return of an arrow shooting rollout, [τ]{.html-italic}, to
be:

::::: {#ch001.xhtml_FD6-robotics-02-00122 .html-disp-formula-info}
::: f
![there is no
content](150104002259780d961a410.png){style="border: none;vertical-align: middle; height:3.134ex;width:17.884ex;max-width: 17.884ex;max-height:3.134ex"}
:::

::: l
`<label>`{=html}(6)`</label>`{=html}
:::
:::::

where ![there is no
content](150104002259780d967220c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.259ex;width:2.681ex;max-width: 2.681ex;max-height:2.259ex"}
is the estimated 2D position of the center of the target on the target's
plane, ![there is no
content](150104002259780d96c711c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:2.756ex;max-width: 2.756ex;max-height:2.384ex"}
is the estimated 2D position of the arrow's tip and ![there is no
content](150104002359780d972540c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:4.266ex;max-width: 4.266ex;max-height:2.634ex"}
is Euclidean distance.
::::::
:::::::::

::::::::::::::: {#ch001.xhtml_sec7dot3-robotics-02-00122 .section type=""}
#### 7.3. Learning Algorithm 2: ARCHER {#ch001.xhtml_learning-algorithm-2-archer .html-italic nested="2"}

::: html-p
For a second learning approach, we propose a custom algorithm developed
and optimized specifically for problems like the archery training, which
has a smooth solution space and prior knowledge about the goal to be
achieved. We will refer to it as the ARCHER algorithm (Augmented Reward
Chained Regression). The motivation for ARCHER is to make use of richer
feedback information about the result of a rollout. Such information is
ignored by the PoWER RL algorithm, because it uses scalar feedback,
which only depends on the distance to the target's center. ARCHER, on
the other hand, is designed to use the prior knowledge we have on the
optimum reward possible. In this case, we know that hitting the center
corresponds to the maximum reward we can get. Using this prior
information about the task, we can view the position of the arrow's tip
as an augmented reward. In this case, it consists of a two-dimensional
vector giving the horizontal and vertical displacement of the arrow's
tip with respect to the target's center. This information is obtained by
the image processing algorithm in [Section
7.4](#ch001.xhtml_sec7dot4-robotics-02-00122){.html-sec} during the
real-world experiment. Then, ARCHER uses a chained local regression
process that iteratively estimates new policy parameters, which have a
greater probability of leading to the achievement of the goal of the
task, based on experience, so far.
:::

::: html-p
Each rollout, ![there is no
content](150104002359780d977e48c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:1.816ex;max-width: 1.816ex;max-height:1.759ex"},
where ![there is no
content](150104002359780d97d9cf5.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:13.985ex;max-width: 13.985ex;max-height:2.634ex"},
is initiated by input parameters, ![there is no
content](150104002459780d98436b5.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:7.463ex;max-width: 7.463ex;max-height:2.634ex"},
which is the vector describing the relative position of the hands and is
produced by the learning algorithms. Each rollout has an associated
observed result (considered as a two-dimensional reward), ![there is no
content](150104002459780d989df2c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.884ex;width:15.885ex;max-width: 15.885ex;max-height:2.884ex"},
which is the relative position of the arrow's tip with respect to the
target's center, ![there is no
content](150104002559780d9902082.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.134ex;width:12.094ex;max-width: 12.094ex;max-height:3.134ex"}.
The unknown function, [f]{.html-italic}, is considered to be non-linear
due to air friction, wind flow, friction between the bow and the arrow,
[etc.]{.html-italic}
:::

:::::: html-p
Without loss of generality, we assume that the rollouts are sorted in
descending order by their scalar return calculated by Equation
([6](#ch001.xhtml_FD6-robotics-02-00122){.html-disp-formula}),
[i.e.]{.html-italic},
`<mrow>`{=html}`<mi>`{=html}R`</mi>`{=html}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}![there
is no
content](150104002359780d977e48c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:1.816ex;max-width: 1.816ex;max-height:1.759ex"}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`<mo>`{=html}≥`</mo>`{=html}`<mi>`{=html}R`</mi>`{=html}`<mrow>`{=html}`<mo>`{=html}(`</mo>`{=html}`<msub>`{=html}`<mi>`{=html}τ`</mi>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}+`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`</msub>`{=html}`<mo>`{=html})`</mo>`{=html}`</mrow>`{=html}`</mrow>`{=html},
[i.e.]{.html-italic}, that ![there is no
content](150104002559780d99b01b6.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.103ex;max-width: 2.103ex;max-height:1.759ex"}
is the closest to ![there is no
content](150104002659780d9a0f426.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.438ex;max-width: 2.438ex;max-height:1.759ex"}.
For convenience, we define vectors, ![there is no
content](150104002659780d9a6ba90.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:12.729ex;max-width: 12.729ex;max-height:2.384ex"}
and ![there is no
content](150104002659780d9ac5342.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:12.854ex;max-width: 12.854ex;max-height:2.759ex"}.
Then, we represent the vector, ![there is no
content](150104002759780d9b26b02.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:3.717ex;max-width: 3.717ex;max-height:2.134ex"},
as a linear combination of vectors using the [N]{.html-italic} best
results:

::::: {#ch001.xhtml_FD7-robotics-02-00122 .html-disp-formula-info}
::: f
`<mrow>`{=html}![there is no
content](150104002759780d9b26b02.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:3.717ex;max-width: 3.717ex;max-height:2.134ex"}`<mo>`{=html}=`</mo>`{=html}`<munderover>`{=html}`<mo>`{=html}∑`</mo>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<mi>`{=html}N`</mi>`{=html}`<mo>`{=html}−`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`</munderover>`{=html}![there
is no
content](150104001359780d8d1161b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.464ex;max-width: 2.464ex;max-height:1.759ex"}`<msub>`{=html}`<mi>`{=html}r`</mi>`{=html}`<mrow>`{=html}`<mn>`{=html}1`</mn>`{=html}`<mo>`{=html},`</mo>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}+`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`</msub>`{=html}`</mrow>`{=html}
:::

::: l
`<label>`{=html}(7)`</label>`{=html}
:::
:::::
::::::

:::::: html-p
Under the assumption that the original parameter space can be linearly
approximated in a small neighborhood, the calculated weights, ![there is
no
content](150104001359780d8d1161b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.464ex;max-width: 2.464ex;max-height:1.759ex"},
are transferred back to the original parameter space. Then, the unknown
vector to the goal parameter value, ![there is no
content](150104002859780d9c37b2c.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.759ex;width:3.759ex;max-width: 3.759ex;max-height:2.759ex"},
is approximated with ![there is no
content](150104002859780d9c8afb2.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.259ex;width:4.025ex;max-width: 4.025ex;max-height:3.259ex"}
as a linear combination of the corresponding parameter vectors using the
same weights:

::::: {#ch001.xhtml_FD8-robotics-02-00122 .html-disp-formula-info}
::: f
`<mrow>`{=html}![there is no
content](150104002859780d9c8afb2.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.259ex;width:4.025ex;max-width: 4.025ex;max-height:3.259ex"}`<mo>`{=html}=`</mo>`{=html}`<munderover>`{=html}`<mo>`{=html}∑`</mo>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<mi>`{=html}N`</mi>`{=html}`<mo>`{=html}−`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`</munderover>`{=html}![there
is no
content](150104001359780d8d1161b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.464ex;max-width: 2.464ex;max-height:1.759ex"}`<msub>`{=html}`<mi>`{=html}θ`</mi>`{=html}`<mrow>`{=html}`<mn>`{=html}1`</mn>`{=html}`<mo>`{=html},`</mo>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}+`</mo>`{=html}`<mn>`{=html}1`</mn>`{=html}`</mrow>`{=html}`</msub>`{=html}`</mrow>`{=html}
:::

::: l
`<label>`{=html}(8)`</label>`{=html}
:::
:::::
::::::

::: html-p
In a matrix form, we have `<mrow>`{=html}![there is no
content](150104002759780d9b26b02.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:3.717ex;max-width: 3.717ex;max-height:2.134ex"}`<mo>`{=html}=`</mo>`{=html}`<mi>`{=html}W`</mi>`{=html}`<mi>`{=html}U`</mi>`{=html}`</mrow>`{=html},
where [W]{.html-italic} contains the weights,
`<msubsup>`{=html}`<mrow>`{=html}`<mo>`{=html}{`</mo>`{=html}![there is
no
content](150104001359780d8d1161b.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.464ex;max-width: 2.464ex;max-height:1.759ex"}`<mo>`{=html}}`</mo>`{=html}`</mrow>`{=html}`<mrow>`{=html}`<mi>`{=html}i`</mi>`{=html}`<mo>`{=html}=`</mo>`{=html}`<mn>`{=html}2`</mn>`{=html}`</mrow>`{=html}`<mi>`{=html}N`</mi>`{=html}`</msubsup>`{=html},
and [U]{.html-italic} contains the collected vectors, ![there is no
content](150104003059780d9e0b766.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:3.384ex;width:8.353ex;max-width: 8.353ex;max-height:3.384ex"},
from the observed rewards of [N]{.html-italic} rollouts. The least-norm
approximation of the weights is given by
`<mrow>`{=html}`<mover accent="true">`{=html}`<mi>`{=html}W`</mi>`{=html}`<mo>`{=html}\^`</mo>`{=html}`</mover>`{=html}`<mo>`{=html}=`</mo>`{=html}![there
is no
content](150104002759780d9b26b02.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:3.717ex;max-width: 3.717ex;max-height:2.134ex"}`<msup>`{=html}`<mi>`{=html}U`</mi>`{=html}`<mrow>`{=html}`<mspace width="-0.166667em">`{=html}`</mspace>`{=html}`<mo>`{=html}†`</mo>`{=html}`</mrow>`{=html}`</msup>`{=html}`</mrow>`{=html},
where
`<msup>`{=html}`<mi>`{=html}U`</mi>`{=html}`<mrow>`{=html}`<mspace width="-0.166667em">`{=html}`</mspace>`{=html}`<mo>`{=html}†`</mo>`{=html}`</mrow>`{=html}`</msup>`{=html}
is the pseudoinverse of [U]{.html-italic}. By repeating this regression
process when adding a new couple, ![there is no
content](150104003159780d9f1bf91.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.634ex;width:7.097ex;max-width: 7.097ex;max-height:2.634ex"},
to the dataset at each iteration, the algorithm refines the solution by
selecting at each iteration the [N]{.html-italic} closest points to
![there is no
content](150104002659780d9a0f426.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:2.438ex;max-width: 2.438ex;max-height:1.759ex"}.
ARCHER can thus be viewed as a linear vector regression with a shrinking
support region.
:::

::: html-p
The ARCHER algorithm can also be used for other tasks, provided that:
(1) [a priori]{.html-italic} knowledge about the desired target reward
is known; (2) the reward can be decomposed into separate dimensions; and
(3) the task has a smooth solution space.
:::
:::::::::::::::

:::: {#ch001.xhtml_sec7dot4-robotics-02-00122 .section type=""}
#### 7.4. Image Processing Algorithm {#ch001.xhtml_image-processing-algorithm .html-italic nested="2"}

::: html-p
The problem of detecting where the target is and what is the relative
position of the arrow with respect to the center of the target is solved
by image processing. We use color-based detection of the target and the
tip of the arrow based on the Gaussian Mixture Model (GMM). Two separate
GMM models are fitted to represent the target's and arrow's color
characteristics in YUVcolor space. After each shot, the reward vector,
![there is no
content](150104003159780d9fcb5da.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.384ex;width:6.708ex;max-width: 6.708ex;max-height:2.384ex"},
is calculated as ![there is no
content](150104003259780da033570.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:2.134ex;width:13.922ex;max-width: 13.922ex;max-height:2.134ex"},
where ![there is no
content](150104003259780da08763d.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.884ex;width:3.505ex;max-width: 3.505ex;max-height:1.884ex"}
is the estimated center of the arrow and ![there is no
content](150104003259780da0e0956.png){style="display:inline-block; padding-left: 4px; padding-right: 4px; border: none;vertical-align: middle; height:1.759ex;width:3.43ex;max-width: 3.43ex;max-height:1.759ex"}
is the estimated center of the target.
:::
::::

::::::::::: {#ch001.xhtml_sec7dot5-robotics-02-00122 .section type=""}
#### 7.5. PoWER [vs.]{.html-italic} ARCHER (RL [vs.]{.html-italic} Regression) {#ch001.xhtml_power-vs.-archer-rl-vs.-regression .html-italic nested="2"}

::::::::: html-p
The two proposed learning algorithms (PoWER and ARCHER) are first
evaluated in a simulation experiment. The trajectory of the arrow is
modeled as a simple ballistic trajectory, ignoring air friction, wind
velocity, [etc.]{.html-italic} A typical experimental result for each
algorithm is shown in [Figure
7](#ch001.xhtml_robotics-02-00122-f007){.html-fig}. A comparison of the
convergence of the two algorithms is shown in [Figure
8](#ch001.xhtml_robotics-02-00122-f008){.html-fig}. The ARCHER algorithm
clearly outperforms the PoWER algorithm for the archery task. This is
due to the use of 2D feedback information, which allows ARCHER to make
better estimations/predictions of good parameter values, and to the
prior knowledge concerning the maximum reward that can be achieved.
PoWER, on the other hand, achieves reasonable performance despite using
only 1D feedback information.

::::: {#ch001.xhtml_robotics-02-00122-f007 .html-fig_show .mfp-hide}
::: html-caption
**Figure 7.** Simulation of archery. Learning is performed under the
same starting conditions with two different algorithms. The red
trajectory is the final rollout. (**a**) The PoWER algorithm needs 19
rollouts to reach the center; (**b**) The ARCHER algorithm needs five
rollouts to do the same.
:::

::: html-img
![Robotics 02 00122 g007](media/file14.png)
:::
:::::

::::: {#ch001.xhtml_robotics-02-00122-f008 .html-fig_show .mfp-hide}
::: html-caption
**Figure 8.** Comparison of the speed of convergence for the PoWER and
ARCHER algorithms. Statistics are collected from 40 learning sessions
with 60 rollouts in each session. The first three rollouts of ARCHER are
done with large random exploratory noise, which explains the big
variance at the beginning.
:::

::: html-img
![Robotics 02 00122 g008](media/file16.png)
:::
:::::
:::::::::

::: html-p
Based on the results from the simulated experiment, the ARCHER algorithm
was chosen to conduct the following real-world experiment:
:::
:::::::::::

::::::::::: {#ch001.xhtml_sec7dot6-robotics-02-00122 .section type=""}
#### 7.6. Experimental Results on the iCub Robot {#ch001.xhtml_experimental-results-on-the-icub-robot .html-italic nested="2"}

:::::: html-p
The real-world robot experimental setup is shown in [Figure
9](#ch001.xhtml_robotics-02-00122-f009){.html-fig}. The experiment was
conducted with iCub
\[[44](#ch001.xhtml_B44-robotics-02-00122){.html-bibr}\]. The iCub is an
open-source robotic platform with dimensions comparable to a three and a
half year-old child (about 104cm tall), with 53° of freedom (DOF)
distributed on the head, torso, arms, hands and legs.

::::: {#ch001.xhtml_robotics-02-00122-f009 .html-fig_show .mfp-hide}
::: html-caption
**Figure 9.** Experimental setup for the archery task. A
position-controlled 53-DOF humanoid robot, iCub, learns to shoot arrows
using a bow and learns to hit the center of the target using the RL
algorithm and visual feedback from a camera. Real-world experiment using
the iCub. The distance between the target and the robot is 2.2 m. The
diameter of the target is 50 cm.
:::

::: html-img
![Robotics 02 00122 g009](media/file18.png)
:::
:::::
::::::

::: html-p
In the experiment, we used the torso (three DoF), arms (seven DoF each)
and hands (nine DoF each). The thick blue arrow shows the relative
position of the two hands, which is controlled by the learning algorithm
during the learning sessions.
:::

::: html-p
To robot's arms are controlled using inverse kinematics solved as an
optimization under an inequality constraints problem. The posture of the
iCub's arms and the grasping configuration for the bow and the arrow are
shown in [Figure 9](#ch001.xhtml_robotics-02-00122-f009){.html-fig}.
During the experiment, while the robot is learning, between every trial
shot, it is adjusting the relative position and orientation of the two
hands, which, in turn, controls the direction and speed of the arrow.
The desired relative position between the two hands is given by the
learning algorithm before each trial. The orientation of the two hands
is calculated in such a way that the bow is kept vertical.
:::

::: html-p
The real-world experiment was conducted using the proposed ARCHER
algorithm and the proposed image processing method. During the real
experiments, the ARCHER algorithm needed less than 10 rollouts to
converge to the center.
:::

::: html-p
For the archery task, we can conclude that a local regression algorithm,
like ARCHER, performs better than a state-of-the-art RL algorithm. The
experiments show significant improvement in terms of speed of
convergence, which is due to the use of a multi-dimensional reward and
prior knowledge about the optimum reward that one can reach.
:::
:::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::

::::: {#ch001.xhtml_sec8-robotics-02-00122 .section type=""}
## 8. Summary and Comparison of the Robot Learning Tasks {#ch001.xhtml_summary-and-comparison-of-the-robot-learning-tasks nested="1"}

:::: html-p
[Table 2](#ch001.xhtml_robotics-02-00122-t002){.html-table} summarizes
the high-level properties of the three presented RL problems (rows
1--3). In addition, a comparison is made with three other robot skill
learning problems (rows 4--6) in which, also, the goal is to learn motor
skills. Based on the empirical results about the best-performing
approach in each of these particular situations, the following
conclusions can be drawn:

- ::: html-p
  Reinforcement learning is well suited for highly-dynamic tasks, where
  there is a clear measure about the success of the task;
  :::

- ::: html-p
  Imitation learning works well for slow tasks, which are easy to
  demonstrate and which do not have a clear optimal way of execution;
  :::

- ::: html-p
  Regression-based learning performs well in cases when the goal is
  known in advance, and it is possible to exploit a multi-dimensional
  feedback in the learning algorithm.
  :::

::: {#ch001.xhtml_robotics-02-00122-t002 .html-table_show .mfp-hide}
+-----------+----------------------------------------------------------+----------------+-----------+-------------+------------+
| No.       | Task                                                     | Dimensionality | Task      | Noise and   | Best       |
|           |                                                          |                | dynamics  | uncertainty | performing |
|           |                                                          |                |           |             | approach   |
+:=========:+:=========================================================+:===============+:==========+:============+:===========+
| 1         | **Pancake flipping**                                     | High           | Very high | High        | RL + DMP   |
|           |                                                          | (positions and |           |             |            |
|           |                                                          | stiffness for  |           |             |            |
|           |                                                          | each           |           |             |            |
|           |                                                          | attractor)     |           |             |            |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+------------+
| 2         | **Walking optimization**                                 | Medium         | High      | High        | RL +       |
|           |                                                          | (continuous    |           |             | evolving   |
|           |                                                          | trajectory of  |           |             | policy     |
|           |                                                          | CoM)           |           |             |            |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+------------+
| 3         | **Archery**                                              | Low (relative  | Low       | Medium      | Regression |
|           |                                                          | pose of hands) | (static   |             |            |
|           |                                                          |                | shooting  |             |            |
|           |                                                          |                | pose)     |             |            |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+------------+
| 4         | **Ironing                                                | Medium (pose   | Low\      | Low         | Imitation  |
|           | \[[3](#ch001.xhtml_B3-robotics-02-00122){.html-bibr}\]** | of             | (slow     |             | learning + |
|           |                                                          | end-effector)  | movement) |             | DMP        |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+            |
| 5         | **Whiteboard cleaning                                    | Medium (pose   | Low\      | Medium      |            |
|           | \[[6](#ch001.xhtml_B6-robotics-02-00122){.html-bibr}\]** | and force at   | (slow     |             |            |
|           |                                                          | end-effector)  | movement, |             |            |
|           |                                                          |                | medium    |             |            |
|           |                                                          |                | forces)   |             |            |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+            |
| 6         | **Door opening                                           | Medium (pose   | Low\      | Medium      |            |
|           | \[[3](#ch001.xhtml_B3-robotics-02-00122){.html-bibr}\]** | and force at   | (slow     |             |            |
|           |                                                          | end-effector)  | movement, |             |            |
|           |                                                          |                | high      |             |            |
|           |                                                          |                | forces)   |             |            |
+-----------+----------------------------------------------------------+----------------+-----------+-------------+------------+

: **Table 2.** Comparison of the three presented RL problems (rows 1--3)
with three other robot skill learning problems (rows 4--6). DMP, Dynamic
Movement Primitives; CoM, center of mass.\
{style="width: 100% !important; border: none;" cellspacing="0"
align="left"}
:::
::::
:::::

::::: {#ch001.xhtml_sec9-robotics-02-00122 .section type=""}
## 9. The Future of Reinforcement Learning in Robotics {#ch001.xhtml_the-future-of-reinforcement-learning-in-robotics nested="1"}

::: html-p
What does the future hold for RL in robotics? This seems difficult to
predict [for RL]{.html-italic}, but it is relatively easier to predict
the near-future trend [for robotics]{.html-italic}. Robotics is moving
towards higher and higher DoF robots, having more nonlinear elements,
variable passive compliance, variable damping, flexible joints,
reconfigurability, fault tolerance, independence, power autonomy,
[etc.]{.html-italic} Robots will be progressively going out of the robot
labs and into everyday life.
:::

::: html-p
As the robot hardware complexity increases to higher levels, the
conventional engineering approaches and analytical methods for robot
control will start to fail. Therefore, machine learning (and RL, in
particular) will inevitably become a more and more important tool to
cope with the ever-increasing complexity of the physical robotic
systems. Furthermore, the future RL candidates will have to address an
ever-growing number of challenges accordingly.
:::
:::::

::::::: {#ch001.xhtml_sec10-robotics-02-00122 .section type=""}
## 10. Beyond Reinforcement Learning {#ch001.xhtml_beyond-reinforcement-learning nested="1"}

::: html-p
Turning back to [Table
1](#ch001.xhtml_robotics-02-00122-t001){.html-table}, in the bottom row,
we have made a prediction, based on extrapolation of the trend in the
existing approaches for teaching robots. The result of this
extrapolation has lead us to a hypothetical approach that we call
[goal-directed learning]{.html-italic}. For example, a goal could be
"throw the basketball through the hoop", and it could actually be
specified as human-readable text and require natural language processing
to understand it. Note that this is different from unsupervised
learning, where there is not any goal specified by a teacher, but the
system is performing self-organization.
:::

::: html-p
The hypothetical goal-directed learning could be "emulated" using the
existing RL methods, but it would be extremely inefficient. For
instance, it would be similar to learning how to play chess based on
only terminal reward (win, lose or draw) without the possibility to
assess any intermediate chessboard configurations. This means that in
goal-directed learning, novel mechanisms should be invented to
autonomously guide the exploration towards the goal, without any help
from a human teacher, and extensively using a bias from the previous
experience of the agent.
:::

::: html-p
Another promising direction is to move towards semantics, where the
robot will have direct knowledge about the goal and the meaning of
achieving it. This is contrary to the current approaches, where the
robot never has any direct information about the goal of the task, and
it blindly executes trajectories without realizing their outcome and
meaning in the real world.
:::

::: html-p
Ideally, the robot should be aware of what it is doing, what the goal is
and should be able to evaluate its own partial incremental progress by
itself, using a self-developed internal performance metric. This is a
far more natural mechanism for self-improvement than the currently
employed method of providing an externally-imposed reward function.
:::
:::::::

:::: {#ch001.xhtml_sec11-robotics-02-00122 .section type="conclusions"}
## 11. Conclusions {#ch001.xhtml_conclusions nested="1"}

::: html-p
We summarized the state-of-the-art for RL in robotics, in terms of both
algorithms and policy representations. We identified a significant
number of the existing challenges for policy representations in
robotics. Three examples for extensions of the capabilities of policy
representations on three real-world tasks were presented: pancake
flipping, bipedal walking and archery aiming. In these examples, we
proposed solutions to six rarely-addressed challenges in policy
representations: [correlations]{.html-italic},
[adaptability]{.html-italic}, [multi-resolution]{.html-italic},
[globality]{.html-italic}, [multi-dimensionality]{.html-italic} and
[convergence]{.html-italic}. Finally, we attempted to have a peek into
the future of RL and its significance to robotics.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::: html-back
:::: {#ch001.xhtml_html-ack .section .html-ack}
## Acknowledgments {#ch001.xhtml_acknowledgments}

::: html-p
This work was partially supported by the AMARSi European project under
contract FP7-ICT-248311, and by the PANDORA European project under
contract FP7-ICT-288273.
:::
::::

:::: {#ch001.xhtml_html-notes .section .html-notes}
## Conflict of Interest {#ch001.xhtml_conflict-of-interest}

::: html-p
The authors declare no conflict of interest.
:::
::::

::: {#ch001.xhtml_html-references_list .section}
## References {#ch001.xhtml_references}

1.  [1. ]{#ch001.xhtml_B1-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Billard, A.;
    Calinon, S.; Dillmann, R.; Schaal, S. Robot programming by
    demonstration. In [Handbook of Robotics]{.html-italic}; Siciliano,
    B., Khatib, O., Eds.; Springer: Secaucus, NJ, USA, 2008; pp.
    1371--1394. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Robot%20programming%20by%20demonstration&author=Billard,+A.&author=Calinon,+S.&author=Dillmann,+R.&author=Schaal,+S.&publication_year=2008&pages=1371%E2%80%931394){.google-scholar}\]
2.  [2. ]{#ch001.xhtml_B2-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Argall, B.D.;
    Chernova, S.; Veloso, M.; Browning, B. A survey of robot learning
    from demonstration. [Robot. Auton. Syst.]{.html-italic} **2009**,
    [57]{.html-italic}, 469--483. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=A%20survey%20of%20robot%20learning%20from%20demonstration&author=Argall,+B.D.&author=Chernova,+S.&author=Veloso,+M.&author=Browning,+B.&publication_year=2009&journal=Robot.+Auton.+Syst.&volume=57&pages=469%E2%80%93483&doi=10.1016/j.robot.2008.10.024){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1016/j.robot.2008.10.024){.cross-ref}\]
3.  [3. ]{#ch001.xhtml_B3-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Calinon, S.; Caldwell, D.G. Imitation learning of positional and
    force skills demonstrated via kinesthetic teaching and haptic input.
    [Adv. Robot.]{.html-italic} **2011**, [25]{.html-italic}, 581--603.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Imitation%20learning%20of%20positional%20and%20force%20skills%20demonstrated%20via%20kinesthetic%20teaching%20and%20haptic%20input&author=Kormushev,+P.&author=Calinon,+S.&author=Caldwell,+D.G.&publication_year=2011&journal=Adv.+Robot.&volume=25&pages=581%E2%80%93603&doi=10.1163/016918611X558261){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1163/016918611X558261){.cross-ref}\]
4.  [4. ]{#ch001.xhtml_B4-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Akgun, B.; Cakmak,
    M.; Jiang, K.; Thomaz, A. Keyframe-based learning from
    demonstration. [Int. J. Soc. Robot.]{.html-italic} **2012**,
    [4]{.html-italic}, 343--355. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Keyframe-based%20learning%20from%20demonstration&author=Akgun,+B.&author=Cakmak,+M.&author=Jiang,+K.&author=Thomaz,+A.&publication_year=2012&journal=Int.+J.+Soc.+Robot.&volume=4&pages=343%E2%80%93355&doi=10.1007/s12369-012-0160-0){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1007/s12369-012-0160-0){.cross-ref}\]
5.  [5. ]{#ch001.xhtml_B5-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Nehaniv, C.L.;
    Dautenhahn, K. [Imitation and Social Learning in Robots, Humans and
    Animals: Behavioural, Social and Communicative
    Dimensions]{.html-italic}; Cambridge University Press: Cambridge,
    UK, 2007. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Imitation+and+Social+Learning+in+Robots,+Humans+and+Animals:+Behavioural,+Social+and+Communicative+Dimensions&author=Nehaniv,+C.L.&author=Dautenhahn,+K.&publication_year=2007){.google-scholar}\]
6.  [6. ]{#ch001.xhtml_B6-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Nenchev, D.N.; Calinon, S.; Caldwell, D.G. Upper-Body Kinesthetic
    Teaching of a Free-Standing Humanoid Robot. In Proceedings of the
    IEEE International Conference on Robotics and Automation (ICRA),
    Shanghai, China, 9--13 May 2011; pp. 3970--3975.
7.  [7. ]{#ch001.xhtml_B7-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Sutton, R.S.;
    Barto, A.G. [Reinforcement Learning: An Introduction]{.html-italic};
    MIT Press: Cambridge, MA, USA, 1998. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Reinforcement+Learning:+An+Introduction&author=Sutton,+R.S.&author=Barto,+A.G.&publication_year=1998){.google-scholar}\]
8.  [8. ]{#ch001.xhtml_B8-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Pastor, P.;
    Kalakrishnan, M.; Chitta, S.; Theodorou, E.; Schaal, S. Skill
    Learning and Task Outcome Prediction for Manipulation. In
    Proceedings of the International Conference on Robotics and
    Automation (ICRA), Shanghai, China, 9--13 May 2011; pp. 3828--3834.
9.  [9. ]{#ch001.xhtml_B9-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Stulp, F.; Buchli,
    J.; Theodorou, E.; Schaal, S. Reinforcement Learning of Full-Body
    Humanoid Motor Skills. In Proceedings of the IEEE International
    Conference on Humanoid Robots (Humanoids), Nashville, TN, USA, 6--8
    December 2010; pp. 405--410.
10. [10. ]{#ch001.xhtml_B10-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Peters, J.;
    Schaal, S. Policy Gradient Methods for Robotics. In Proceedings of
    the IEEE/RSJ International Conference on Intelligent Robots and
    Systems (IROS), Beijing, China, October 2006; pp. 2219--2225.
11. [11. ]{#ch001.xhtml_B11-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Coates, A.; Abbeel,
    P.; Ng, A.Y. Apprenticeship learning for helicopter control.
    [Commun. ACM]{.html-italic} **2009**, [52]{.html-italic}, 97--105.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Apprenticeship%20learning%20for%20helicopter%20control&author=Coates,+A.&author=Abbeel,+P.&author=Ng,+A.Y.&publication_year=2009&journal=Commun.+ACM&volume=52&pages=97%E2%80%93105&doi=10.1145/1538788.1538812){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1145/1538788.1538812){.cross-ref}\]
12. [12. ]{#ch001.xhtml_B12-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Rosenstein, M.T.;
    Barto, A.G.; van Emmerik, R.E.A. Learning at the level of synergies
    for a robot weightlifter. [Robot. Auton. Syst.]{.html-italic}
    **2006**, [54]{.html-italic}, 706--717. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Learning%20at%20the%20level%20of%20synergies%20for%20a%20robot%20weightlifter&author=Rosenstein,+M.T.&author=Barto,+A.G.&author=van+Emmerik,+R.E.A.&publication_year=2006&journal=Robot.+Auton.+Syst.&volume=54&pages=706%E2%80%93717&doi=10.1016/j.robot.2006.03.002){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1016/j.robot.2006.03.002){.cross-ref}\]
13. [13. ]{#ch001.xhtml_B13-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Calinon, S.; Caldwell, D.G. Robot Motor Skill Coordination with
    EM-Based Reinforcement Learning. In Proceedings of the IEEE/RSJ
    International Conference on Intelligent Robots and Systems (IROS),
    Taipei, Taiwan, 18--22 October 2010; pp. 3232--3237.
14. [14. ]{#ch001.xhtml_B14-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Calinon, S.; Saegusa, R.; Metta, G. Learning the Skill of Archery by
    a Humanoid Robot iCub. In Proceedings of the IEEE International
    Conference on Humanoid Robots (Humanoids), Nashville, TN, USA, 6--8
    December 2010; pp. 417--423.
15. [15. ]{#ch001.xhtml_B15-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Calinon, S.; Ugurlu, B.; Caldwell, D.G. Challenges for the Policy
    Representation When Applying Reinforcement Learning in Robotics. In
    Proceedings of the International Joint Conference on Neural Networks
    (IJCNN), Brisbane, Australia, 10--15 June 2012; pp. 2819--2826.
16. [16. ]{#ch001.xhtml_B16-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Peters, J.;
    Schaal, S. Natural actor-critic. [Neurocomputing]{.html-italic}
    **2008**, [71]{.html-italic}, 1180--1190. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Natural%20actor-critic&author=Peters,+J.&author=Schaal,+S.&publication_year=2008&journal=Neurocomputing&volume=71&pages=1180%E2%80%931190&doi=10.1016/j.neucom.2007.11.026){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1016/j.neucom.2007.11.026){.cross-ref}\]
17. [17. ]{#ch001.xhtml_B17-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Williams, R.J.
    Simple statistical gradient-following algorithms for connectionist
    reinforcement learning. [Mach. Learn.]{.html-italic} **1992**,
    [8]{.html-italic}, 229--256. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Simple%20statistical%20gradient-following%20algorithms%20for%20connectionist%20reinforcement%20learning&author=Williams,+R.J.&publication_year=1992&journal=Mach.+Learn.&volume=8&pages=229%E2%80%93256&doi=10.1007/BF00992696){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1007/BF00992696){.cross-ref}\]
18. [18. ]{#ch001.xhtml_B18-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kober, J.;
    Peters, J. Learning Motor Primitives for Robotics. In Proceedings of
    the IEEE International Conference on Robotics and Automation (ICRA),
    Kobe, Japan, 12--17 May 2009; pp. 2112--2118.
19. [19. ]{#ch001.xhtml_B19-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Theodorou, E.;
    Buchli, J.; Schaal, S. A generalized path integral control approach
    to reinforcement learning. [J. Mach. Learn. Res.]{.html-italic}
    **2010**, [11]{.html-italic}, 3137--3181. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=A%20generalized%20path%20integral%20control%20approach%20to%20reinforcement%20learning&author=Theodorou,+E.&author=Buchli,+J.&author=Schaal,+S.&publication_year=2010&journal=J.+Mach.+Learn.+Res.&volume=11&pages=3137%E2%80%933181){.google-scholar}\]
20. [20. ]{#ch001.xhtml_B20-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Rubinstein, R.;
    Kroese, D. [The Cross-Entropy Method: A Unified Approach to
    Combinatorial Optimization, Monte-Carlo Simulation and Machine
    Learning]{.html-italic}; Springer-Verlag: New York, NY, USA, 2004.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=The+Cross-Entropy+Method:+A+Unified+Approach+to+Combinatorial+Optimization,+Monte-Carlo+Simulation+and+Machine+Learning&author=Rubinstein,+R.&author=Kroese,+D.&publication_year=2004){.google-scholar}\]
21. [21. ]{#ch001.xhtml_B21-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Hansen, N. The CMA
    evolution strategy: A comparing review. In [Towards a New
    Evolutionary Computation]{.html-italic}; Lozano, J., Larranaga, P.,
    Inza, I., Bengoetxea, E., Eds.; Springer: Berlin, Germany, 2006;
    Volume 192, pp. 75--102. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=The%20CMA%20evolution%20strategy:%20A%20comparing%20review&author=Hansen,+N.&publication_year=2006&pages=75%E2%80%93102){.google-scholar}\]
22. [22. ]{#ch001.xhtml_B22-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Stulp, F.;
    Sigaud, O. Path Integral Policy Improvement with Covariance Matrix
    Adaptation. In Proceedings of the International Conference on
    Machine Learning (ICML), Edinburgh, UK, 26 June--1 July 2012.
23. [23. ]{#ch001.xhtml_B23-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Guenter, F.;
    Hersch, M.; Calinon, S.; Billard, A. Reinforcement learning for
    imitating constrained reaching movements. [Adv.
    Robot.]{.html-italic} **2007**, [21]{.html-italic}, 1521--1544.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Reinforcement%20learning%20for%20imitating%20constrained%20reaching%20movements&author=Guenter,+F.&author=Hersch,+M.&author=Calinon,+S.&author=Billard,+A.&publication_year=2007&journal=Adv.+Robot.&volume=21&pages=1521%E2%80%931544){.google-scholar}\]
24. [24. ]{#ch001.xhtml_B24-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kober, J.;
    Peters, J. Policy search for motor primitives in robotics. In
    [Advances in Neural Information Processing Systems]{.html-italic};
    MIT Press: Cambridge, MA, USA, 2009; Volume 21, pp. 849--856.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Policy%20search%20for%20motor%20primitives%20in%20robotics&author=Kober,+J.&author=Peters,+J.&publication_year=2009&pages=849%E2%80%93856){.google-scholar}\]
25. [25. ]{#ch001.xhtml_B25-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Schaal, S.;
    Mohajerian, P.; Ijspeert, A.J. Dynamics systems [vs]{.html-italic}.
    optimal control a unifying view. [Progr. Brain Res.]{.html-italic}
    **2007**, [165]{.html-italic}, 425--445. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Dynamics%20systems%20vs.%20optimal%20control%20a%20unifying%20view&author=Schaal,+S.&author=Mohajerian,+P.&author=Ijspeert,+A.J.&publication_year=2007&journal=Progr.+Brain+Res.&volume=165&pages=425%E2%80%93445){.google-scholar}\]
26. [26. ]{#ch001.xhtml_B26-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Ijspeert, A.J.;
    Nakanishi, J.; Schaal, S. Trajectory Formation for Imitation with
    Nonlinear Dynamical Systems. In Proceedings of the IEEE
    International Conference on Intelligent Robots and Systems (IROS),
    Maui, HI, USA, 29 October--3 November 2001; pp. 752--757.
27. [27. ]{#ch001.xhtml_B27-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Hoffmann, H.;
    Pastor, P.; Park, D.H.; Schaal, S. Biologically-Inspired Dynamical
    Systems for Movement Generation: Automatic Real-Time Goal Adaptation
    and Obstacle Avoidance. In Proceedings of the IEEE International
    Conference on Robotics and Automation (ICRA), Kobe, Japan, 12--17
    May 2009; pp. 2587--2592.
28. [28. ]{#ch001.xhtml_B28-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kober, J.
    Reinforcement Learning for Motor Primitives. Master's Thesis,
    University of Stuttgart, Stuttgart, Germany, 2008. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Reinforcement%20Learning%20for%20Motor%20Primitives&author=Kober,+J.&publication_year=2008){.google-scholar}\]
29. [29. ]{#ch001.xhtml_B29-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Peters, J.;
    Schaal, S. Applying the Episodic Natural Actor-Critic Architecture
    to Motor Primitive Learning. In Proceedings of the 15th European
    Symposium on Artificial Neural Networks (ESANN 2007), Bruges,
    Belgium, 25--27 April 2007; pp. 1--6.
30. [30. ]{#ch001.xhtml_B30-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Pardo, D. Learning
    Rest-to-Rest Motor Coordination in Articulated Mobile Robots. Ph.D.
    Thesis, Technical University of Catalonia (UPC), Catalonia,
    Spain, 2009. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Learning%20Rest-to-Rest%20Motor%20Coordination%20in%20Articulated%20Mobile%20Robots&author=Pardo,+D.&publication_year=2009){.google-scholar}\]
31. [31. ]{#ch001.xhtml_B31-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Todorov, E.;
    Jordan, M.I. Optimal feedback control as a theory of motor
    coordination. [Nat. Neurosci.]{.html-italic} **2002**,
    [5]{.html-italic}, 1226--1235. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Optimal%20feedback%20control%20as%20a%20theory%20of%20motor%20coordination&author=Todorov,+E.&author=Jordan,+M.I.&publication_year=2002&journal=Nat.+Neurosci.&volume=5&pages=1226%E2%80%931235&doi=10.1038/nn963&pmid=12404008){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1038/nn963){.cross-ref}\]
    \[[PubMed](http://www.ncbi.nlm.nih.gov/pubmed/12404008){.cross-ref}\]
32. [32. ]{#ch001.xhtml_B32-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Huys, R.;
    Daffertshofer, A.; Beek, P.J. The evolution of coordination during
    skill acquisition: The dynamical systems approach. In [Skill
    Acquisition in Sport: Research, Theory and Practice]{.html-italic};
    Williams, A.M., Hodges, N.J., Eds.; Routledge: London, UK, 2004; pp.
    351--373. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=The%20evolution%20of%20coordination%20during%20skill%20acquisition:%20The%20dynamical%20systems%20approach&author=Huys,+R.&author=Daffertshofer,+A.&author=Beek,+P.J.&publication_year=2004&pages=351%E2%80%93373){.google-scholar}\]
33. [33. ]{#ch001.xhtml_B33-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Bernikera, M.;
    Jarcb, A.; Bizzic, E.; Trescha, M.C. Simplified and effective motor
    control based on muscle synergies to exploit musculoskeletal
    dynamics. [Proc. Natl. Acad. Sci. USA]{.html-italic} **2009**,
    [106]{.html-italic}, 7601--7606. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Simplified%20and%20effective%20motor%20control%20based%20on%20muscle%20synergies%20to%20exploit%20musculoskeletal%20dynamics&author=Bernikera,+M.&author=Jarcb,+A.&author=Bizzic,+E.&author=Trescha,+M.C.&publication_year=2009&journal=Proc.+Natl.+Acad.+Sci.+USA&volume=106&pages=7601%E2%80%937606&doi=10.1073/pnas.0901512106&pmid=19380738){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1073/pnas.0901512106){.cross-ref}\]
    \[[PubMed](http://www.ncbi.nlm.nih.gov/pubmed/19380738){.cross-ref}\]
34. [34. ]{#ch001.xhtml_B34-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Calinon, S.;
    Sardellitti, I.; Caldwell, D.G. Learning-Based Control Strategy for
    Safe Human-Robot Interaction Exploiting Task and Robot Redundancies.
    In Proceedings of the IEEE/RSJ International Conference on
    Intelligent Robots and Systems (IROS), Taipei, Taiwan, 18--22
    October 2010; pp. 249--254.
35. [35. ]{#ch001.xhtml_B35-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Calinon, S.; Li,
    Z.; Alizadeh, T.; Tsagarakis, N.G.; Caldwell, D.G. Statistical
    Dynamical Systems for Skills Acquisition in Humanoids. In
    Proceedings of the IEEE International Conference on Humanoid Robots
    (Humanoids), Osaka, Japan, 29 November--1 December 2012; pp.
    323--329.
36. [36. ]{#ch001.xhtml_B36-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Bernstein, A.;
    Shimkin, N. Adaptive-resolution reinforcement learning with
    polynomial exploration in deterministic domains. [Mach.
    Learn.]{.html-italic} **2010**, [81]{.html-italic}, 359--397.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Adaptive-resolution%20reinforcement%20learning%20with%20polynomial%20exploration%20in%20deterministic%20domains&author=Bernstein,+A.&author=Shimkin,+N.&publication_year=2010&journal=Mach.+Learn.&volume=81&pages=359%E2%80%93397&doi=10.1007/s10994-010-5186-7){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1007/s10994-010-5186-7){.cross-ref}\]
37. [37. ]{#ch001.xhtml_B37-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Moore, A.W.;
    Atkeson, C.G. The parti-game algorithm for variable resolution
    reinforcement learning in multidimensional state-spaces. [Mach.
    Learn.]{.html-italic} **1995**, [21]{.html-italic}, 199--233.
    \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=The%20parti-game%20algorithm%20for%20variable%20resolution%20reinforcement%20learning%20in%20multidimensional%20state-spaces&author=Moore,+A.W.&author=Atkeson,+C.G.&publication_year=1995&journal=Mach.+Learn.&volume=21&pages=199%E2%80%93233&doi=10.1007/BF00993591){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1007/BF00993591){.cross-ref}\]
38. [38. ]{#ch001.xhtml_B38-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Kormushev, P.;
    Ugurlu, B.; Calinon, S.; Tsagarakis, N.; Caldwell, D.G. Bipedal
    Walking Energy Minimization by Reinforcement Learning with Evolving
    Policy Parameterization. In Proceedings of the IEEE/RSJ
    International Conference on Intelligent Robots and Systems (IROS),
    San Francisco, CA, USA, 25--30 September 2011; pp. 318--324.
39. [39. ]{#ch001.xhtml_B39-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Ugurlu, B.;
    Tsagarakis, N.G.; Spyrakos-Papastravridis, E.; Caldwell, D.G.
    Compiant Joint Modification and Real-Time Dynamic Walking
    Implementation on Bipedal Robot cCub. In Proceedings of the IEEE
    International Conference on Mechatronics, Istanbul, Turkey, 13--15
    April 2011; pp. 833--838.
40. [40. ]{#ch001.xhtml_B40-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Miyamoto, H.;
    Morimoto, J.; Doya, K.; Kawato, M. Reinforcement learning with
    via-point representation. [Neural Netw.]{.html-italic} **2004**,
    [17]{.html-italic}, 299--305. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Reinforcement%20learning%20with%20via-point%20representation&author=Miyamoto,+H.&author=Morimoto,+J.&author=Doya,+K.&author=Kawato,+M.&publication_year=2004&journal=Neural+Netw.&volume=17&pages=299%E2%80%93305&doi=10.1016/j.neunet.2003.11.004&pmid=15037348){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1016/j.neunet.2003.11.004){.cross-ref}\]
    \[[PubMed](http://www.ncbi.nlm.nih.gov/pubmed/15037348){.cross-ref}\]
41. [41. ]{#ch001.xhtml_B41-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Morimoto, J.;
    Atkeson, C.G. Learning biped locomotion: Application of
    poincare-map-based reinforcement learning. [IEEE Robot. Autom.
    Mag.]{.html-italic} **2007**, [14]{.html-italic}, 41--51. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Learning%20biped%20locomotion:%20Application%20of%20poincare-map-based%20reinforcement%20learning&author=Morimoto,+J.&author=Atkeson,+C.G.&publication_year=2007&journal=IEEE+Robot.+Autom.+Mag.&volume=14&pages=41%E2%80%9351&doi=10.1109/MRA.2007.380654){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1109/MRA.2007.380654){.cross-ref}\]
42. [42. ]{#ch001.xhtml_B42-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Wada, Y.;
    Sumita, K. A Reinforcement Learning Scheme for Acquisition of
    Via-Point Representation of Human Motion. In Proceedings of the IEEE
    International Conference on Neural Networks, Budapest, Hungary,
    25--29 July 2004; Volume 2, pp. 1109--1114.
43. [43. ]{#ch001.xhtml_B43-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Shen, H.; Yosinski,
    J.; Kormushev, P.; Caldwell, D.G.; Lipson, H. Learning fast
    quadruped robot gaits with the RL power spline parameterization.
    [Cybern. Inf. Technol.]{.html-italic} **2012**, [12]{.html-italic},
    66--75. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=Learning%20fast%20quadruped%20robot%20gaits%20with%20the%20RL%20power%20spline%20parameterization&author=Shen,+H.&author=Yosinski,+J.&author=Kormushev,+P.&author=Caldwell,+D.G.&author=Lipson,+H.&publication_year=2012&journal=Cybern.+Inf.+Technol.&volume=12&pages=66%E2%80%9375&doi=10.2478/cait-2012-0022){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.2478/cait-2012-0022){.cross-ref}\]
44. [44. ]{#ch001.xhtml_B44-robotics-02-00122
    style="display:inline-block;font-weight: bold;"} Tsagarakis, N.G.;
    Metta, G.; Sandini, G.; Vernon, D.; Beira, R.; Becchi, F.; Righetti,
    L.; Santos-Victor, J.; Ijspeert, A.J.; Carrozza, M.C.; Caldwell,
    D.G. iCub: The design and realization of an open humanoid platform
    for cognitive and neuroscience research. [Adv. Robot.]{.html-italic}
    **2007**, [21]{.html-italic}, 1151--1175. \[[Google
    Scholar](http://scholar.google.com/scholar_lookup?title=iCub:%20The%20design%20and%20realization%20of%20an%20open%20humanoid%20platform%20for%20cognitive%20and%20neuroscience%20research&author=Tsagarakis,+N.G.&author=Metta,+G.&author=Sandini,+G.&author=Vernon,+D.&author=Beira,+R.&author=Becchi,+F.&author=Righetti,+L.&author=Santos-Victor,+J.&author=Ijspeert,+A.J.&author=Carrozza,+M.C.&publication_year=2007&journal=Adv.+Robot.&volume=21&pages=1151%E2%80%931175&doi=10.1163/156855307781389419){.google-scholar}\]
    \[[CrossRef](http://dx.doi.org/10.1163/156855307781389419){.cross-ref}\]
:::

::: section
© 2013 by the authors; licensee MDPI, Basel, Switzerland. This article
is an open access article distributed under the terms and conditions of
the Creative Commons Attribution license (
<http://creativecommons.org/licenses/by/3.0/>).
:::
:::::::::

</article>
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
