_Robotics_ **2013**, _2_, 122-148; doi:10.3390/robotics2030122


_Article_



**OPEN ACCESS**
# **_robotics_**

**ISSN 2218-6581**
www.mdpi.com/journal/robotics


## **Reinforcement Learning in Robotics: Applications and** Real-World Challenges [†]

**Petar Kormushev** _[⋆]_ **, Sylvain Calinon and Darwin G. Caldwell**


Department of Advanced Robotics, Istituto Italiano di Tecnologia, via Morego 30, 16163 Genova, Italy;

E-Mails: sylvain.calinon@iit.it (S.C.); darwin.caldwell@iit.it (D.G.C.)


_**†**_ Based on “Kormushev, P.; Calinon, S.; Caldwell, D.G.; Ugurlu, B. Challenges for the Policy

Representation When Applying Reinforcement Learning in Robotics. In Proceedings of WCCI 2012

IEEE World Congress on Computational Intelligence, Brisbane, Australia, 10–15 June 2012”.


_**⋆**_ Author to whom correspondence should be addressed; E-Mail: petar.kormushev@iit.it.


_Received:_ _4 June 2013; in revised form:_ _24 June 2013 / Accepted:_ _28 June 2013 /_

_Published:_ _5 July 2013_


**Abstract:** In robotics, the ultimate goal of reinforcement learning is to endow robots

with the ability to learn, improve, adapt and reproduce tasks with dynamically changing

constraints based on exploration and autonomous learning. We give a summary of

the state-of-the-art of reinforcement learning in the context of robotics, in terms of

both algorithms and policy representations. Numerous challenges faced by the policy

representation in robotics are identified. Three recent examples for the application

of reinforcement learning to real-world robots are described: a pancake flipping task,

a bipedal walking energy minimization task and an archery-based aiming task. In all

examples, a state-of-the-art expectation-maximization-based reinforcement learning is used,

and different policy representations are proposed and evaluated for each task. The proposed

policy representations offer viable solutions to six rarely-addressed challenges in policy

representations: correlations, adaptability, multi-resolution, globality, multi-dimensionality

and convergence. Both the successes and the practical difficulties encountered in these

examples are discussed. Based on insights from these particular cases, conclusions are drawn

about the state-of-the-art and the future perspective directions for reinforcement learning

in robotics.


**Keywords:** reinforcement learning; robotics; learning and adaptive systems


_Robotics_ **2013**, _2_ **123**


**1. Introduction**


Endowing robots with human-like abilities to perform motor skills in a smooth and natural way is one

of the important goals of robotics. A promising way to achieve this is by creating robots that can learn

new skills by themselves, similarly to humans. However, acquiring new motor skills is not simple and

involves various forms of learning.

Over the years, the approaches for teaching new skill to robots have evolved significantly, and

currently, there are three well-established types of approaches: _direct programming_, _imitation learning_

and _reinforcement_ _learning_ . All of these approaches are still being actively used, and each one has

its own advantages and disadvantages and is preferred for certain settings, as summarized in Table 1.

The bottom row in Table 1 indicates our prediction about a hypothetical future approach, predicted

based on extrapolation from the existing approaches, as explained in Section 10.

The ultimate goal of these approaches is to give robots the ability to learn, improve, adapt and

reproduce tasks with dynamically changing constraints. However, these approaches differ significantly

from one another:


_•_ **Direct** **programming** : This is the lowest-level approach, but it is still being actively used in

industrial settings, where the environment is well-structured and complete control over the precise

movement of the robot is crucial. We add it for completeness, although it is not really a _teaching_

method; hence, we classify it as _programming_ . Industrial robots are usually equipped with the

so-called _teach pendant_ —a device that is used to manually set the desired robot positions.


_•_ **Imitation** **learning** : This approach is called _learning_ instead of _programming_, in order to

emphasize the active part that the agent (the robot) has in the process. This approach is also

known as _programming by demonstration_ [1] or _learning from demonstration_ [2]. There are three

main methods used to perform demonstrations for imitation learning:


**–** **Kinesthetic** **teaching** : This is the process of manually moving the robot’s body and

recording its motion [3]. This approach usually works only for smaller, lightweight robots

and in combination with a gravity-compensation controller, in order to minimize the apparent

weight of the robot. However, nevertheless, since the robot’s inertia cannot be effectively

reduced, it is not practical for bigger robots. Kinesthetic teaching could be performed

in a continuous way, recording whole trajectories, or alternatively, it could be performed

by recording discrete snapshots of the robot’s state at separate time instances, such as in

keyframe-based teaching of sequences of key poses [4].


**–** **Teleoperation** : This is the process of remotely controlling the robot’s body using another

input device, such as a joystick or a haptic device. This approach shares many similarities

with kinesthetic teaching in terms of advantages and disadvantages. One big difference

is that with teleoperation, the teacher can be located in a geographically distant location.

However, time delays become an issue as the distance increases (e.g., teleoperating a Mars

rover would be difficult). Similarly to kinesthetic teaching, only a limited number of degrees

of freedom (DoFs) can be controlled at the same time. Furthermore, with teleoperation, it is

more difficult to feel the limitations and capabilities of the robot than by using kinesthetic


_Robotics_ **2013**, _2_ **124**


teaching. As an advantage, sometimes the setup could be simpler, and additional information

can be displayed at the interface (e.g., forces rendered by the haptic device).


**–** **Observational learning** : In this method, the movement is demonstrated using the teacher’s

own body and is perceived using motion capture systems or video cameras or other sensors.

It is usually needed to solve the correspondence problem [5], _i.e._, to map the robot’s

kinematics to that of the teacher.


The simplest way to use the demonstrations is to do a simple record-and-replay, which can only

execute a particular instance of a task. However, using smart representation of the recorded

movement in appropriate frame of reference (e.g., using the target object as the origin), it is

possible to have somewhat adaptable skill to different initial configurations, for simple (mostly

one-object) tasks. Based on multiple demonstrations that include variations of a task, the robot can

calculate correlations and variance and figure out which part of a task is important to be repeated

verbatim and which part is acceptable to be changed (and to what extent). Imitation learning has

been successfully applied many times for learning tasks on robots, for which the human teacher

can demonstrate a successful execution [3,6].


_•_ **Reinforcement** **learning** **(RL)** : This is the process of learning from trial-and-error [7],

by exploring the environment and the robot’s own body. The goal in RL is specified by the

_reward_ _function_, which acts as positive reinforcement or negative punishment depending on the

performance of the robot with respect to the desired goal. RL has created a well-defined niche for

its application in robotics [8–14]. The main motivation for using reinforcement learning to teach

robots new skills is that it offers three previously missing abilities:


**–** to learn new tasks, which even the human teacher cannot physically demonstrate or cannot

directly program (e.g., jump three meters high, lift heavy weights, move very fast, _etc._ );

**–** to learn to achieve optimization goals of difficult problems that have no analytic formulation

or no known closed form solution, when even the human teacher does not know what

the optimum is, by using only a known cost function (e.g., minimize the used energy for

performing a task or find the fastest gait, _etc._ );

**–** to learn to adapt a skill to a new, previously unseen version of a task (e.g., learning to

walk from flat ground to a slope, learning to generalize a task to new previously unseen

parameter values, _etc._ ). Some imitation learning approaches can also do this, but in a much

more restricted way (e.g., by adjusting parameters of a learned model, without being able to

change the model itself).


Reinforcement learning also offers some additional advantages. For example, it is possible to start

from a “good enough” demonstration and gradually refine it. Another example would be the ability to

dynamically adapt to changes in the agent itself, such as a robot adapting to hardware changes—heating

up, mechanical wear, growing body parts, _etc_ .


_Robotics_ **2013**, _2_ **125**


**Table 1.** Comparison of the main robot teaching approaches.
















|Approach/method for teaching the robot|Col2|Col3|Computational<br>H<br>H complexity<br>H<br>DifficulHty<br>H<br>for the teacheHr<br>H<br>H|Advantages|Disadvantages|
|---|---|---|---|---|---|
|Existing approaches|**Direct**<br>**programming**<br>Manually<br>specifying<br>(programming) the robot<br>how to move each joint|**Direct**<br>**programming**<br>Manually<br>specifying<br>(programming) the robot<br>how to move each joint|HHHHHH<br>High<br>Lowest|Complete control<br>of the movement<br>of the robot to the<br>lowest level|Time-consuming,<br>error-prone,<br>not<br>scalable,<br>not reusable|
|Existing approaches|**Imitation learning**|**Kinesthetic teaching**<br>and** Teleoperation**<br>Directly move the robot’s<br>limbs<br>or<br>teleoperate<br>to<br>record the movement|HHHHHH<br>Medium<br>Low|No<br>need<br>to<br>manually<br>program,<br>can<br>just<br>record<br>and<br>replay movements|Cannot<br>perform<br>fast<br>movements;<br>can<br>move<br>usually only one limb at a<br>time; the robot has to be<br>lightweight|
|Existing approaches|**Imitation learning**|**Observational learning**<br>Demonstrate the movement<br>using<br>the<br>teacher’s<br>own<br>body;<br>perceive<br>the<br>movement<br>using<br>motion<br>capture systems or video<br>cameras|HHHHHH<br>Low<br>Medium|Easy and natural<br>to<br>demonstrate;<br>also<br>works<br>for<br>bimanual tasks or<br>even whole-body<br>motion|Correspondence<br>problem<br>caused<br>by<br>the<br>different<br>embodiment;<br>the<br>teacher<br>must be able to do the<br>task; often requires multiple<br>demonstrations<br>that<br>need<br>to<br>be<br>segmented<br>and<br>time-aligned|
|Existing approaches|**Reinforcement**<br>**learning**<br>Specify<br>a<br>scalar<br>reward<br>function evaluating the robot’s<br>performance<br>that<br>needs<br>to<br>be<br>maximized;<br>no<br>need<br>to<br>demonstrate how to perform the<br>task; the robot discovers this on<br>its own|**Reinforcement**<br>**learning**<br>Specify<br>a<br>scalar<br>reward<br>function evaluating the robot’s<br>performance<br>that<br>needs<br>to<br>be<br>maximized;<br>no<br>need<br>to<br>demonstrate how to perform the<br>task; the robot discovers this on<br>its own|HHHHHH<br>Lower<br>Higher|Robot can learn<br>tasks<br>that<br>even<br>the human cannot<br>demonstrate;<br>novel<br>ways<br>to<br>reach a goal can<br>be discovered|No control over the actions<br>of<br>the<br>robot;<br>robot<br>has<br>only<br>indirect<br>information<br>about the goal;<br>need to<br>specify<br>reward<br>function,<br>policy<br>parameterization,<br>exploration<br>magnitude/strategy,<br>initial<br>policy|
|Hypothetical|**“Goal-directed**<br>**learning”**<br>(predicted via extrapolation) Only<br>specifying the goal that the robot<br>must achieve, without evaluating<br>the intermediate progress|**“Goal-directed**<br>**learning”**<br>(predicted via extrapolation) Only<br>specifying the goal that the robot<br>must achieve, without evaluating<br>the intermediate progress|HHHHHH<br>Lowest<br>Highest|The easiest way<br>to<br>specify<br>(e.g.,<br>using<br>NLP);<br>robot<br>has<br>direct<br>knowledge of the<br>goal|No control of the movement<br>of the robot;<br>must know<br>what the goal is and how to<br>formally deﬁne it|



This paper provides a summary of some of the main components for applying reinforcement learning

in robotics. We present some of the most important classes of learning algorithms and classes of policies.

We give a comprehensive list of challenges for effective policy representations for the application

of policy-search RL to robotics and provide three examples of tasks demonstrating how the policy

representation may address some of these challenges. The paper is a significantly improved and extended

version of our previous work in [15]. The novelties include: new experimental section based on

robotic archery task; new section with insights about the future of RL in robotics; new comparison

of existing robot learning approaches and their respective advantages and disadvantages; an expanded

list of challenges for the policy representation and more detailed description of use cases.


_Robotics_ **2013**, _2_ **126**


The paper does not propose new algorithmic strategies. Rather, it summarizes what our team has

learned from a fairly extensive base of empirical evidence over the last 4–5 years, aiming to serve as

a reference for the field of robot learning. While we may still dream of a general purpose algorithm

that would allow robots to learn optimal policies without human guidance, it is likely that these are

far off. The paper describes several classes of policies that have proved to work very well for a wide

range of robot motor control tasks. The main contribution of this work is a better understanding that the

design of appropriate policy representations is essential for RL methods to be successfully applied to

real-world robots.

The paper is structured as follows. In Section 2, we present an overview of the most important

recent RL algorithms that are being successfully applied in robotics. Then, in Section 3, we identify

numerous challenges posed by robotics on the RL policy representation, and in Section 4, we describe

the state-of-the-art policy representations. To illustrate some of these challenges, and to propose adequate

solutions to them, the three consecutive Sections 5–7, give three representative examples for real-world

application of RL in robotics. The examples are all based on the same RL algorithm, but each faces

different policy representation problems and, therefore, requires different solutions. In Section 8,

we give a summary of the three tasks and compare them to three other robot skill learning tasks. Then,

in Section 9, we give insights about the future perspective directions for RL based on these examples

and having in mind robotics, in particular, as the application. Finally, in Section 10, we discuss potential

future alternative methods for teaching robots new tasks that might appear. We conclude with a brief

peek into the future of robotics, revealing, in particular, the potential wider need for RL.


**2. State-of-the-Art Reinforcement Learning Algorithms in Robotics**


Robot systems are naturally of high-dimensionality, having many degrees of freedom (DoF),

continuous states and actions and high noise. Because of this, traditional RL approaches based on

MDP/POMDP/discretized state and action spaces have problems scaling up to work in robotics, because

they suffer severely from the curse of dimensionality. The first partial successes in applying RL to

robotics came with the function approximation techniques, but the real “renaissance” came with the

policy-search RL methods.

In policy-search RL, instead of working in the huge state/action spaces, a smaller policy space is used,

which contains all possible policies representable with a certain choice of policy parameterization. Thus,

the dimensionality is drastically reduced and the convergence speed is increased.

Until recently, _policy-gradient_ _algorithms_ (such as Episodic Natural Actor-Critic eNAC [16] and

Episodic REINFORCE [17]) have been a well-established approach for implementing policy-search

RL [10]. Unfortunately, policy-gradient algorithms have certain shortcomings, such as high sensitivity

to the learning rate and exploratory variance.

An alternative approach that has gained popularity recently derives from the

Expectation-Maximization (EM) algorithm. For example, Kober _et al_ . proposed in [18] an episodic RL

algorithm, called PoWER ( _policy_ _learning_ _by_ _weighting_ _exploration_ _with_ _the_ _returns_ ). It is based on

the EM algorithm and, thus, has a major advantage over policy-gradient-based approaches: it does not

require a learning rate parameter. This is desirable, because tuning a learning rate is usually difficult


_Robotics_ **2013**, _2_ **127**


to do for control problems, but critical for achieving good performance of policy-gradient algorithms.

PoWER also demonstrates superior performance in tasks learned directly on a real robot, by applying

an importance sampling technique to reuse previous experience efficiently.

Another state-of-the-art policy-search RL algorithm, called _PIˆ2_ ( _policy_ _improvement_ _with_ _path_

_integrals_ ), was proposed by Theodorou _et al_ . in [19], for learning parameterized control policies based

on the framework of stochastic optimal control with path integrals. They derived update equations for

learning to avoid numerical instabilities, because neither matrix inversions nor gradient learning rates are

required. The approach demonstrates significant performance improvements over gradient-based policy

learning and scalability to high-dimensional control problems, such as control of a quadruped robot dog.

Several search algorithms from the field of stochastic optimization have recently found successful

use for iterative policy improvement. Examples of such approaches are the cross-entropy method

(CEM) [20] and the covariance matrix adaptation evolution strategy (CMA-ES) [21]. Although these

algorithms come from a different domain and are not well-established in RL research, they seem to be a

viable alternative for direct policy search RL, as some recent findings suggest [22].


**3. Challenges for the Policy Representation in Robotics**


Only having a good policy-search RL algorithm is not enough for solving real-world problems in

robotics. Before any given RL algorithm can be applied to learn a task on a robot, an appropriate _policy_

_representation_ (also called _policy encoding_ ) needs to be devised. This is important, because the choice

of policy representation determines what in principle can be learned by the RL algorithm ( _i.e._, the policy

search space), analogous to the way a hypothesis model determines what kind of data a regression method

can fit well. In addition, the policy representation can have significant influence on the RL algorithm

itself, e.g., it can help or impede the convergence or influence the variance of the generated policies.

However, creating a good policy representation is not a trivial problem, due to a number of serious

_challenges_ posed by the high requirements from a robotic system, such as:


_•_ _smoothness_ —the policy representation needs to encode smooth, continuous trajectories, without

sudden accelerations or jerks, in order to be safe for the robot itself and also to reduce its energy

consumption. In some rare cases, though, such as in bang-bang control, sudden changes might

be desirable;

_•_ _safety_ —the policy should be safe, not only for the robot (in terms of joint limits, torque limits,

work space restrictions, obstacles, _etc._ ), but also for the people around it;

_•_ _gradual exploration_ —the representation should allow gradual, incremental exploration, so that the

policy does not suddenly change by a lot; e.g., in state-action-based policies, changing the policy

action at only a single state could cause a sudden dramatic change in the overall behavior of the

system when following this new branch of the policy, which is not desirable neither for the robot,

nor for the people around it. In some cases, though, a considerable step change might be necessary,

e.g., a navigation task where a robot needs to decide whether to go left or right to avoid an obstacle;

_•_ _scalability_ —to be able to scale up to high dimensions and for more complex tasks; e.g., a typical

humanoid robot nowadays has well above 50 DoF;


_Robotics_ **2013**, _2_ **128**


_•_ _compactness_ —despite the high DoF of robots, the policy should use very compact encoding, e.g.,

it is impossible to directly use all points on a trajectory as policy parameters;

_•_ _adaptability_ —the policy parameterization should be adaptable to the complexity and fidelity of the

task, e.g., lifting weights _vs_ . micro-surgery;

_•_ _multi-resolution_ —different parts of the policy parameterization should allow different

resolution/precision;

_•_ _unbiasedness_ —the policy parameterization should work without prior knowledge about the

solution being sought and without restricting unnecessarily the search scope for possible solutions;

_•_ _prior/bias_ —whenever feasible, it should be possible to add prior information (also called _bias_ ) in

order to jump-start policy search approaches, as illustrated in some of the use cases in this paper;

_•_ _regularization_ —the policy should allow one to incorporate regularization to guide the exploration

towards desired types of policies;

_•_ _time-independence_ —this is the property of a policy not to depend on precise time or position,

in order to cope with unforeseen perturbations;

_•_ _embodiment-agnostic_ —the representation should not depend on any particular embodiment of the

robot, e.g., joint-trajectory based policies cannot be transferred to another robot easily;

_•_ _invariance_ —the policy should be an invariant representation of the task (e.g., rotation-invariant,

scale-invariant, position-invariant, _etc._ );

_•_ _correlations_ —the policy should encapsulate correlations between the control variables (e.g.,

actuator control signals), similar to the motor synergies found in animals;

_•_ _globality_ —the representation should help the RL algorithm to avoid local minima;

_•_ _periodicity_ —to be able to represent easily periodic/cyclic movements, which occur

often in robotics (e.g., for locomotion—different walking gaits, for manipulation—wiping

movements, _etc._ );

_•_ _analyzability_ —facility to visualize and analyze the policy (e.g., proving its stability by poles

analysis, _etc._ );

_•_ _multi-dimensionality_ —to be able to use efficiently high-dimensional feedback without the need to

convert it into a scalar value by using a weighted sum of components;

_•_ _convergence_ —to help the RL algorithm to converge faster to the (possibly local) optima.


A good policy representation should provide solutions to all of these challenges. However, it is

not easy to come up with such a policy representation that satisfies all of them. In fact, the existing

state-of-the-art policy representations in robotics cover only subsets of these requirements, as highlighted

in the next section.


**4. State-of-the-Art Policy Representations in Robotics**


Traditionally, explicit time-dependent approaches, such as cubic splines or higher-order polynomials,

were used as policy representations. These, however, are not autonomous, in the sense that they cannot

cope easily with perturbations (unexpected changes in the environment). Currently, there are a number

of efficient state-of-the-art representations available to address this and many of the other challenges

mentioned earlier. We give three examples of such policy representations below:


