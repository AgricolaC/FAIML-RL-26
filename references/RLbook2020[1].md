_ii_


## **Contents**

**Preface** **to** **the** **Second** **Edition** **xiii**


**Preface** **to** **the** **First** **Edition** **xvii**


**Summary** **of** **Notation** **xix**


**1** **Introduction** **1**
1.1 Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Elements of Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . 6
1.4 Limitations and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.5 An Extended Example: Tic-Tac-Toe . . . . . . . . . . . . . . . . . . . . . 8
1.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.7 Early History of Reinforcement Learning . . . . . . . . . . . . . . . . . . . 13


**I** **Tabular** **Solution** **Methods** **23**


**2** **Multi-armed** **Bandits** **25**
2.1 A _k_ -armed Bandit Problem . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.2 Action-value Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.3 The 10-armed Testbed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.4 Incremental Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.5 Tracking a Nonstationary Problem . . . . . . . . . . . . . . . . . . . . . . 32
2.6 Optimistic Initial Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.7 Upper-Confidence-Bound Action Selection . . . . . . . . . . . . . . . . . . 35
2.8 Gradient Bandit Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.9 Associative Search (Contextual Bandits) . . . . . . . . . . . . . . . . . . . 41
2.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


_viii_ _Contents_


**3** **Finite** **Markov** **Decision** **Processes** **47**
3.1 The Agent–Environment Interface . . . . . . . . . . . . . . . . . . . . . . 47
3.2 Goals and Rewards . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.3 Returns and Episodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3.4 Unified Notation for Episodic and Continuing Tasks . . . . . . . . . . . . 57
3.5 Policies and Value Functions . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.6 Optimal Policies and Optimal Value Functions . . . . . . . . . . . . . . . 62
3.7 Optimality and Approximation . . . . . . . . . . . . . . . . . . . . . . . . 67
3.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68


**4** **Dynamic** **Programming** **73**
4.1 Policy Evaluation (Prediction) . . . . . . . . . . . . . . . . . . . . . . . . 74
4.2 Policy Improvement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.3 Policy Iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.4 Value Iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.5 Asynchronous Dynamic Programming . . . . . . . . . . . . . . . . . . . . 85
4.6 Generalized Policy Iteration . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.7 Efficiency of Dynamic Programming . . . . . . . . . . . . . . . . . . . . . 87
4.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88


**5** **Monte** **Carlo** **Methods** **91**
5.1 Monte Carlo Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
5.2 Monte Carlo Estimation of Action Values . . . . . . . . . . . . . . . . . . 96
5.3 Monte Carlo Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
5.4 Monte Carlo Control without Exploring Starts . . . . . . . . . . . . . . . 100
5.5 O↵-policy Prediction via Importance Sampling . . . . . . . . . . . . . . . 103
5.6 Incremental Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . 109
5.7 O↵-policy Monte Carlo Control . . . . . . . . . . . . . . . . . . . . . . . . 110
5.8 *Discounting-aware Importance Sampling . . . . . . . . . . . . . . . . . . 112
5.9 *Per-decision Importance Sampling . . . . . . . . . . . . . . . . . . . . . . 114
5.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115


**6** **Temporal-Di↵erence** **Learning** **119**
6.1 TD Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
6.2 Advantages of TD Prediction Methods . . . . . . . . . . . . . . . . . . . . 124
6.3 Optimality of TD(0) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6.4 Sarsa: On-policy TD Control . . . . . . . . . . . . . . . . . . . . . . . . . 129
6.5 Q-learning: O↵-policy TD Control . . . . . . . . . . . . . . . . . . . . . . 131
6.6 Expected Sarsa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.7 Maximization Bias and Double Learning . . . . . . . . . . . . . . . . . . . 134
6.8 Games, Afterstates, and Other Special Cases . . . . . . . . . . . . . . . . 136
6.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138


## **Summary of Notation**

Capital letters are used for random variables, whereas lower case letters are used for
the values of random variables and for scalar functions. Quantities that are required to
be real-valued vectors are written in bold and in lower case (even if random variables).
Matrices are bold capitals.


_._
= equality relationship that is true by definition
_⇡_ approximately equal
_/_ proportional to
Pr _{X_ = _x}_ probability that a random variable _X_ takes on the value _x_
_X_ _⇠_ _p_ random variable _X_ selected from distribution _p_ ( _x_ ) = Pr _[.]_ _{X_ = _x}_
E[ _X_ ] expectation of a random variable _X_, i.e., E[ _X_ ] = _[.]_ [P] _x_ _[p]_ [(] _[x]_ [)] _[x]_

argmax _a f_ ( _a_ ) a value of _a_ at which _f_ ( _a_ ) takes its maximal value
ln _x_ natural logarithm of _x_
_e_ _[x]_, exp( _x_ ) the base of the natural logarithm, _e ⇡_ 2 _._ 71828, carried to power _x_ ; _e_ [ln] _[ x]_ = _x_
R set of real numbers
_f_ : X _!_ Y function _f_ from elements of set X to elements of set Y
assignment
( _a, b_ ] the real interval between _a_ and _b_ including _b_ but not including _a_


_"_ probability of taking a random action in an _"_ -greedy policy
_↵, β_ step-size parameters
_γ_ discount-rate parameter
_λ_ decay-rate parameter for eligibility traces

_predicate_ indicator function ( _predicate_ [= 1] _[.]_ [if] [the] _[predicate]_ [is] [true,] [else] [0)]


In a multi-arm bandit problem:
_k_ number of actions (arms)
_t_ discrete time step or play number
_q_ ( _a_ ) true value (expected reward) of action _a_
_⇤_
_Qt_ ( _a_ ) estimate at time _t_ of _q⇤_ ( _a_ )
_Nt_ ( _a_ ) number of times action _a_ has been selected up prior to time _t_
_Ht_ ( _a_ ) learned preference for selecting action _a_ at time _t_
_⇡t_ ( _a_ ) probability of selecting action _a_ at time _t_
_R_ ¯ _t_ estimate at time _t_ of the expected reward given _⇡t_


_xx_ _Summary_ _of_ _Notation_


In a Markov Decision Process:
_s, s_ _[0]_ states
_a_ an action
_r_ a reward
S set of all nonterminal states
S [+] set of all states, including the terminal state
A( _s_ ) set of all actions available in state _s_
R set of all possible rewards, a finite subset of R
_⇢_ subset of (e.g., R _⇢_ R)
_2_ is an element of; e.g. ( _s 2_ S, _r_ _2_ R)
_|_ S _|_ number of elements in set S


_t_ discrete time step
_T, T_ ( _t_ ) final time step of an episode, or of the episode including time step _t_
_At_ action at time _t_
_St_ state at time _t_, typically due, stochastically, to _St−_ 1 and _At−_ 1
_Rt_ reward at time _t_, typically due, stochastically, to _St−_ 1 and _At−_ 1
_⇡_ policy (decision-making rule)
_⇡_ ( _s_ ) action taken in state _s_ under _deterministic_ policy _⇡_
_⇡_ ( _a|s_ ) probability of taking action _a_ in state _s_ under _stochastic_ policy _⇡_



_Gt_ return following time _t_
_h_ horizon, the time step one looks up to in a forward view
_Gt_ : _t_ + _n, Gt_ : _h_ _n_ -step return from _t_ + 1 to _t_ + _n_, or to _h_ (discounted and corrected)
_G_ ¯ _t_ : _h_ flat return (undiscounted and uncorrected) from _t_ + 1 to _h_ (Section 5.8)
_G_ _[λ]_ _λ_ -return (Section 12.1)



_G_ _[λ]_ _t_ _λ_ -return (Section 12.1)

_G_ _[λ]_ truncated, corrected _λ_



_G_ _[λ]_ _t_ : _h_ truncated, corrected _λ_ -return (Section 12.3)

_G_ _[λs][, G][λa]_ _λ_ -return, corrected by estimated state, or




_[λs]_ _t_ _[, G]_ _t_ _[λa]_




_[λa]_ _t_ _λ_ -return, corrected by estimated state, or action, values (Section 12.8)



_p_ ( _s_ _[0]_ _, r_ _|s, a_ ) probability of transition to state _s_ _[0]_ with reward _r_, from state _s_ and action _a_
_p_ ( _s_ _[0]_ _|s, a_ ) probability of transition to state _s_ _[0]_, from state _s_ taking action _a_
_r_ ( _s, a_ ) expected immediate reward from state _s_ after action _a_
_r_ ( _s, a, s_ _[0]_ ) expected immediate reward on transition from _s_ to _s_ _[0]_ under action _a_


_v⇡_ ( _s_ ) value of state _s_ under policy _⇡_ (expected return)
_v_ ( _s_ ) value of state _s_ under the optimal policy
_⇤_
_q⇡_ ( _s, a_ ) value of taking action _a_ in state _s_ under policy _⇡_
_q_ ( _s, a_ ) value of taking action _a_ in state _s_ under the optimal policy
_⇤_


_V, Vt_ array estimates of state-value function _v⇡_ or _v⇤_
_Q, Qt_ array estimates of action-value function _q⇡_ or _q⇤_
_V_ ¯ _t_ ( _s_ ) expected approximate action value; for example, _V_ [¯] _t_ ( _s_ ) = _[.]_ [P] _a_ _[⇡]_ [(] _[a][|][s]_ [)] _[Q][t]_ [(] _[s, a]_ [)]

_Ut_ target for estimate at time _t_


_Summary_ _of_ _Notation_ _xxi_



_δt_ temporal-di↵erence (TD) error at _t_ (a random variable) (Section 6.1)
_δ_ _[s][, δ][a]_ state- and action-specific forms of the TD error (Section 12.9)



_t_ _[s][, δ]_ _t_ _[a]_



_δt_ _[s][, δ]_ _t_ _[a]_ state- and action-specific forms of the TD error (Section 12.9)

_n_ in _n_ -step methods, _n_ is the number of steps of bootstrapping



_d_ dimensionality—the number of components of **w**
_d_ _[0]_ alternate dimensionality—the number of components of _**✓**_
**w** _,_ **w** _t_ _d_ -vector of weights underlying an approximate value function
_wi, wt,i_ _i_ th component of learnable weight vector
_v_ ˆ( _s,_ **w** ) approximate value of state _s_ given weight vector **w**
_v_ **w** ( _s_ ) alternate notation for _v_ ˆ( _s,_ **w** )
_q_ ˆ( _s, a,_ **w** ) approximate value of state–action pair _s, a_ given weight vector **w**
_rv_ ˆ( _s,_ **w** ) column vector of partial derivatives of _v_ ˆ( _s,_ **w** ) with respect to **w**
_rq_ ˆ( _s, a,_ **w** ) column vector of partial derivatives of _q_ ˆ( _s, a,_ **w** ) with respect to **w**


**x** ( _s_ ) vector of features visible when in state _s_
**x** ( _s, a_ ) vector of features visible when in state _s_ taking action _a_
_xi_ ( _s_ ) _, xi_ ( _s, a_ ) _i_ th component of vector **x** ( _s_ ) or **x** ( _s, a_ )
**xw** _t_ _[>]_ **x** shorthandinner productfor **x** of( _S_ vectors, _t_ ) or **x** ( **w** _St_ _[>]_ _, A_ **x** _t_ =) _[.]_ [P] _i_ _[w][i][x][i]_ [;] [for] [example,] _[v]_ [ˆ][(] _[s,]_ **[w]** [)] [=] _[.]_ **[ w]** _[>]_ **[x]** [(] _[s]_ [)]

**v** _,_ **v** _t_ secondary _d_ -vector of weights, used to learn **w** (Chapter 11)
**z** _t_ _d_ -vector of eligibility traces at time _t_ (Chapter 12)


_**✓**_ _,_ _**✓**_ _t_ parameter vector of target policy (Chapter 13)
_⇡_ ( _a|s,_ _**✓**_ ) probability of taking action _a_ in state _s_ given parameter vector _**✓**_
_⇡_ _**✓**_ policy corresponding to parameter _**✓**_
_r⇡_ ( _a|s,_ _**✓**_ ) column vector of partial derivatives of _⇡_ ( _a|s,_ _**✓**_ ) with respect to _**✓**_
_J_ ( _**✓**_ ) performance measure for the policy _⇡_ _**✓**_
_rJ_ ( _**✓**_ ) column vector of partial derivatives of _J_ ( _**✓**_ ) with respect to _**✓**_
_h_ ( _s, a,_ _**✓**_ ) preference for selecting action _a_ in state _s_ based on _**✓**_


_b_ ( _a|s_ ) behavior policy used to select actions while learning about target policy _⇡_
_b_ ( _s_ ) a baseline function _b_ : S _7!_ R for policy-gradient methods
_b_ branching factor for an MDP or search tree
_⇢t_ : _h_ importance sampling ratio for time _t_ through time _h_ (Section 5.5)
_⇢t_ importance sampling ratio for time _t_ alone, _⇢t_ = _[.]_ _⇢t_ : _t_
_r_ ( _⇡_ ) average reward (reward rate) for policy _⇡_ (Section 10.3)
_R_ ¯ _t_ estimate of _r_ ( _⇡_ ) at time _t_



_µ_ ( _s_ ) on-policy distribution over states (Section 9.2)
_**µ**_ _|_ S _|_ -vector of the _µ_ ( _s_ ) for all _s 2_ S
_v_ _µ_ _µ_ -weighted squared norm of value function _v_,
_k_ _k_ [2]



_s_ S _[µ]_ [(] _[s]_ [)] _[v]_ [(] _[s]_ [)][2]
_2_



_µ_ _µ_ -weighted squared norm of value function _v_, i.e., _v_ _µ_

[2] _k_ _k_ [2]



_µ_



= _._ [P]



_⌘_ ( _s_ ) expected number of visits to state _s_ per episode (page 199)
⇧ projection operator for value functions (page 268)
_B⇡_ Bellman operator for value functions (Section 11.4)


_xxii_ _Summary_ _of_ _Notation_





_>_ [i]



**A** _d ⇥_ _d_ matrix **A** = _[.]_ E



h



**x** _t_




**x** _t_ _γ_ **x** _t_ +1
_−_

_[.]_



**b** _d_ -dimensional vector **b** = _[.]_ E[ _Rt_ +1 **x** _t_ ]
**w** TD TD fixed point **w** TD = _[.]_ **A** _[−]_ [1] **b** (a _d_ -vector, Section 9.4)
**I** identity matrix
**P** _|_ S _| ⇥|_ S _|_ matrix of state-transition probabilities under _⇡_
**D** _|_ S _| ⇥|_ S _|_ diagonal matrix with _**µ**_ on its diagonal
**X** _|_ S _| ⇥_ _d_ matrix with the **x** ( _s_ ) as its rows



_δ_ ¯ **w** ( _s_ ) Bellman error (expected TD error) for _v_ **w** at state _s_ (Section 11.4)
_δ_ ¯ **w**, BE Bellman error vector, with components _δ_ [¯] **w** ( _s_ )
VE( **w** ) mean square value error VE( **w** ) = _[.]_ _kv_ **w** _−_ _v⇡_ 2 _kµ_ [2] [(Section] [9.2)]

_[.]_



VE( **w** ) mean square value error VE( **w** ) = _kv_ **w** _−_ _v⇡_ 2 _kµ_ [(Section] [9.2)]

BE( **w** ) mean square Bellman error BE( **w** ) = _[.]_ �� _δ_ ¯ **w** ��



_µ_

2

BE( **w** ) mean square Bellman error BE( **w** ) = _[.]_ �� _δ_ ¯ **w** �� _µ_

PBE( **w** ) mean square projected Bellman error PBE( **w** ) = _[.]_



⇥



_µ_

2

PBE( **w** ) mean square projected Bellman error PBE( **w** ) = _[.]_ ��⇧¯ _δ_ ⇥ **w** �� _µ_

TDE( **w** ) mean square temporal-di↵erence error TDE( **w** ) = _[.]_ E _b_ _⇢tδt_ [2]



_⇢tδt_ [2]



⇤



TDE( **w** ) mean square temporal-di↵erence error TDE( **w** ) = E _b_ _⇢tδt_ [2] (Section 11.5)

RE( **w** ) mean square return error (Section 11.6)



_t_


### **Chapter 1**

## **Introduction**

The idea that we learn by interacting with our environment is probably the first to occur
to us when we think about the nature of learning. When an infant plays, waves its arms,
or looks about, it has no explicit teacher, but it does have a direct sensorimotor connection
to its environment. Exercising this connection produces a wealth of information about
cause and e↵ect, about the consequences of actions, and about what to do in order to
achieve goals. Throughout our lives, such interactions are undoubtedly a major source
of knowledge about our environment and ourselves. Whether we are learning to drive
a car or to hold a conversation, we are acutely aware of how our environment responds
to what we do, and we seek to influence what happens through our behavior. Learning
from interaction is a foundational idea underlying nearly all theories of learning and
intelligence.

In this book we explore a _computational_ approach to learning from interaction. Rather
than directly theorizing about how people or animals learn, we primarily explore idealized
learning situations and evaluate the e↵ectiveness of various learning methods. That
is, we adopt the perspective of an artificial intelligence researcher or engineer. We
explore designs for machines that are e↵ective in solving learning problems of scientific or
economic interest, evaluating the designs through mathematical analysis or computational
experiments. The approach we explore, called _reinforcement_ _learning_, is much more
focused on goal-directed learning from interaction than are other approaches to machine
learning.

###### **1.1 Reinforcement Learning**


Reinforcement learning is learning what to do—how to map situations to actions—so
as to maximize a numerical reward signal. The learner is not told which actions to
take, but instead must discover which actions yield the most reward by trying them. In
the most interesting and challenging cases, actions may a↵ect not only the immediate
reward but also the next situation and, through that, all subsequent rewards. These two
characteristics—trial-and-error search and delayed reward—are the two most important
distinguishing features of reinforcement learning.


_2_ _Chapter_ _1:_ _Introduction_


Reinforcement learning, like many topics whose names end with “ing,” such as machine
learning and mountaineering, is simultaneously a problem, a class of solution methods
that work well on the problem, and the field that studies this problem and its solution
methods. It is convenient to use a single name for all three things, but at the same time
essential to keep the three conceptually separate. In particular, the distinction between
problems and solution methods is very important in reinforcement learning; failing to
make this distinction is the source of many confusions.

We formalize the problem of reinforcement learning using ideas from dynamical systems theory, specifically, as the optimal control of incompletely-known Markov decision
processes. The details of this formalization must wait until Chapter 3, but the basic idea
is simply to capture the most important aspects of the real problem facing a learning
agent interacting over time with its environment to achieve a goal. A learning agent
must be able to sense the state of its environment to some extent and must be able to
take actions that a↵ect the state. The agent also must have a goal or goals relating to
the state of the environment. Markov decision processes are intended to include just
these three aspects—sensation, action, and goal—in their simplest possible forms without
trivializing any of them. Any method that is well suited to solving such problems we
consider to be a reinforcement learning method.

Reinforcement learning is di↵erent from _supervised learning_, the kind of learning studied
in most current research in the field of machine learning. Supervised learning is learning
from a training set of labeled examples provided by a knowledgable external supervisor.
Each example is a description of a situation together with a specification—the label—of
the correct action the system should take in that situation, which is often to identify a
category to which the situation belongs. The object of this kind of learning is for the
system to extrapolate, or generalize, its responses so that it acts correctly in situations
not present in the training set. This is an important kind of learning, but alone it is not
adequate for learning from interaction. In interactive problems it is often impractical to
obtain examples of desired behavior that are both correct and representative of all the
situations in which the agent has to act. In uncharted territory—where one would expect
learning to be most beneficial—an agent must be able to learn from its own experience.

Reinforcement learning is also di↵erent from what machine learning researchers call
_unsupervised_ _learning_, which is typically about finding structure hidden in collections of

unlabeled data. The terms supervised learning and unsupervised learning would seem
to exhaustively classify machine learning paradigms, but they do not. Although one
might be tempted to think of reinforcement learning as a kind of unsupervised learning
because it does not rely on examples of correct behavior, reinforcement learning is trying
to maximize a reward signal instead of trying to find hidden structure. Uncovering
structure in an agent’s experience can certainly be useful in reinforcement learning, but by
itself does not address the reinforcement learning problem of maximizing a reward signal.
We therefore consider reinforcement learning to be a third machine learning paradigm,

alongside supervised learning and unsupervised learning and perhaps other paradigms.


_1.1._ _Reinforcement_ _Learning_ _3_


One of the challenges that arise in reinforcement learning, and not in other kinds
of learning, is the trade-o↵between exploration and exploitation. To obtain a lot of
reward, a reinforcement learning agent must prefer actions that it has tried in the past
and found to be e↵ective in producing reward. But to discover such actions, it has to
try actions that it has not selected before. The agent has to _exploit_ what it has already
experienced in order to obtain reward, but it also has to _explore_ in order to make better
action selections in the future. The dilemma is that neither exploration nor exploitation
can be pursued exclusively without failing at the task. The agent must try a variety of
actions _and_ progressively favor those that appear to be best. On a stochastic task, each
action must be tried many times to gain a reliable estimate of its expected reward. The
exploration–exploitation dilemma has been intensively studied by mathematicians for
many decades, yet remains unresolved. For now, we simply note that the entire issue of
balancing exploration and exploitation does not even arise in supervised and unsupervised
learning, at least in the purest forms of these paradigms.

Another key feature of reinforcement learning is that it explicitly considers the _whole_
problem of a goal-directed agent interacting with an uncertain environment. This is in
contrast to many approaches that consider subproblems without addressing how they
might fit into a larger picture. For example, we have mentioned that many machine
learning researchers have studied supervised learning without specifying how such an
ability would ultimately be useful. Other researchers have developed theories of planning
with general goals, but without considering planning’s role in real-time decision making,
or the question of where the predictive models necessary for planning would come from.
Although these approaches have yielded many useful results, their focus on isolated
subproblems is a significant limitation.

Reinforcement learning takes the opposite tack, starting with a complete, interactive,
goal-seeking agent. All reinforcement learning agents have explicit goals, can sense
aspects of their environments, and can choose actions to influence their environments.
Moreover, it is usually assumed from the beginning that the agent has to operate despite
significant uncertainty about the environment it faces. When reinforcement learning
involves planning, it has to address the interplay between planning and real-time action
selection, as well as the question of how environment models are acquired and improved.
When reinforcement learning involves supervised learning, it does so for specific reasons

that determine which capabilities are critical and which are not. For learning research to
make progress, important subproblems have to be isolated and studied, but they should
be subproblems that play clear roles in complete, interactive, goal-seeking agents, even if
all the details of the complete agent cannot yet be filled in.

By a complete, interactive, goal-seeking agent we do not always mean something like
a complete organism or robot. These are clearly examples, but a complete, interactive,
goal-seeking agent can also be a component of a larger behaving system. In this case, the
agent directly interacts with the rest of the larger system and indirectly interacts with
the larger system’s environment. A simple example is an agent that monitors the charge
level of robot’s battery and sends commands to the robot’s control architecture. This
agent’s environment is the rest of the robot together with the robot’s environment. It is


_4_ _Chapter_ _1:_ _Introduction_


important to look beyond the most obvious examples of agents and their environments
to appreciate the generality of the reinforcement learning framework.

One of the most exciting aspects of modern reinforcement learning is its substantive
and fruitful interactions with other engineering and scientific disciplines. Reinforcement
learning is part of a decades-long trend within artificial intelligence and machine learning
toward greater integration with statistics, optimization, and other mathematical subjects.
For example, the ability of some reinforcement learning methods to learn with parameterized approximators addresses the classical “curse of dimensionality” in operations research
and control theory. More distinctively, reinforcement learning has also interacted strongly
with psychology and neuroscience, with substantial benefits going both ways. Of all the
forms of machine learning, reinforcement learning is the closest to the kind of learning
that humans and other animals do, and many of the core algorithms of reinforcement
learning were originally inspired by biological learning systems. Reinforcement learning
has also given back, both through a psychological model of animal learning that better
matches some of the empirical data, and through an influential model of parts of the
brain’s reward system. The body of this book develops the ideas of reinforcement learning
that pertain to engineering and artificial intelligence, with connections to psychology and
neuroscience summarized in Chapters 14 and 15.

Finally, reinforcement learning is also part of a larger trend in artificial intelligence
back toward simple general principles. Since the late 1960s, many artificial intelligence researchers presumed that there are no general principles to be discovered, that intelligence is
instead due to the possession of a vast number of special purpose tricks, procedures, and
heuristics. It was sometimes said that if we could just get enough relevant facts into a
machine, say one million, or one billion, then it would become intelligent. Methods based
on general principles, such as search or learning, were characterized as “weak methods,”
whereas those based on specific knowledge were called “strong methods.” This view is
uncommon today. From our point of view, it was premature: too little e↵ort had been
put into the search for general principles to conclude that there were none. Modern
artificial intelligence now includes much research looking for general principles of learning,
search, and decision making. It is not clear how far back the pendulum will swing, but
reinforcement learning research is certainly part of the swing back toward simpler and
fewer general principles of artificial intelligence.

###### **1.2 Examples**


A good way to understand reinforcement learning is to consider some of the examples
and possible applications that have guided its development.


  - A master chess player makes a move. The choice is informed both by planning—
anticipating possible replies and counterreplies—and by immediate, intuitive judgments of the desirability of particular positions and moves.


  - An adaptive controller adjusts parameters of a petroleum refinery’s operation in
real time. The controller optimizes the yield/cost/quality trade-o↵on the basis


_1.2._ _Examples_ _5_


of specified marginal costs without sticking strictly to the set points originally
suggested by engineers.


  - A gazelle calf struggles to its feet minutes after being born. Half an hour later it is
running at 20 miles per hour.


  - A mobile robot decides whether it should enter a new room in search of more trash
to collect or start trying to find its way back to its battery recharging station. It
makes its decision based on the current charge level of its battery and how quickly
and easily it has been able to find the recharger in the past.


  - Phil prepares his breakfast. Closely examined, even this apparently mundane
activity reveals a complex web of conditional behavior and interlocking goal–subgoal
relationships: walking to the cupboard, opening it, selecting a cereal box, then
reaching for, grasping, and retrieving the box. Other complex, tuned, interactive
sequences of behavior are required to obtain a bowl, spoon, and milk carton. Each
step involves a series of eye movements to obtain information and to guide reaching
and locomotion. Rapid judgments are continually made about how to carry the
objects or whether it is better to ferry some of them to the dining table before
obtaining others. Each step is guided by goals, such as grasping a spoon or getting
to the refrigerator, and is in service of other goals, such as having the spoon to eat
with once the cereal is prepared and ultimately obtaining nourishment. Whether
he is aware of it or not, Phil is accessing information about the state of his body
that determines his nutritional needs, level of hunger, and food preferences.


These examples share features that are so basic that they are easy to overlook. All
involve _interaction_ between an active decision-making agent and its environment, within
which the agent seeks to achieve a _goal_ despite _uncertainty_ about its environment. The
agent’s actions are permitted to a↵ect the future state of the environment (e.g., the
next chess position, the level of reservoirs of the refinery, the robot’s next location and
the future charge level of its battery), thereby a↵ecting the actions and opportunities
available to the agent at later times. Correct choice requires taking into account indirect,
delayed consequences of actions, and thus may require foresight or planning.

At the same time, in all of these examples the e↵ects of actions cannot be fully predicted;
thus the agent must monitor its environment frequently and react appropriately. For
example, Phil must watch the milk he pours into his cereal bowl to keep it from overflowing.
All these examples involve goals that are explicit in the sense that the agent can judge
progress toward its goal based on what it can sense directly. The chess player knows
whether or not he wins, the refinery controller knows how much petroleum is being
produced, the gazelle calf knows when it falls, the mobile robot knows when its batteries
run down, and Phil knows whether or not he is enjoying his breakfast.

In all of these examples the agent can use its experience to improve its performance
over time. The chess player refines the intuition he uses to evaluate positions, thereby
improving his play; the gazelle calf improves the efficiency with which it can run; Phil
learns to streamline making his breakfast. The knowledge the agent brings to the task at
the start—either from previous experience with related tasks or built into it by design or


_6_ _Chapter_ _1:_ _Introduction_


evolution—influences what is useful or easy to learn, but interaction with the environment
is essential for adjusting behavior to exploit specific features of the task.

###### **1.3 Elements of Reinforcement Learning**


Beyond the agent and the environment, one can identify four main subelements of a
reinforcement learning system: a _policy_, a _reward_ _signal_, a _value_ _function_, and, optionally,
a _model_ of the environment.

A _policy_ defines the learning agent’s way of behaving at a given time. Roughly speaking,
a policy is a mapping from perceived states of the environment to actions to be taken
when in those states. It corresponds to what in psychology would be called a set of
stimulus–response rules or associations. In some cases the policy may be a simple function
or lookup table, whereas in others it may involve extensive computation such as a search
process. The policy is the core of a reinforcement learning agent in the sense that it alone
is sufficient to determine behavior. In general, policies may be stochastic, specifying
probabilities for each action.

A _reward_ _signal_ defines the goal of a reinforcement learning problem. On each time
step, the environment sends to the reinforcement learning agent a single number called
the _reward_ . The agent’s sole objective is to maximize the total reward it receives over
the long run. The reward signal thus defines what are the good and bad events for the
agent. In a biological system, we might think of rewards as analogous to the experiences
of pleasure or pain. They are the immediate and defining features of the problem faced
by the agent. The reward signal is the primary basis for altering the policy; if an action
selected by the policy is followed by low reward, then the policy may be changed to
select some other action in that situation in the future. In general, reward signals may
be stochastic functions of the state of the environment and the actions taken.

Whereas the reward signal indicates what is good in an immediate sense, a _value_
_function_ specifies what is good in the long run. Roughly speaking, the _value_ of a state is
the total amount of reward an agent can expect to accumulate over the future, starting
from that state. Whereas rewards determine the immediate, intrinsic desirability of
environmental states, values indicate the _long-term_ desirability of states after taking into
account the states that are likely to follow and the rewards available in those states. For
example, a state might always yield a low immediate reward but still have a high value
because it is regularly followed by other states that yield high rewards. Or the reverse
could be true. To make a human analogy, rewards are somewhat like pleasure (if high)
and pain (if low), whereas values correspond to a more refined and farsighted judgment
of how pleased or displeased we are that our environment is in a particular state.

Rewards are in a sense primary, whereas values, as predictions of rewards, are secondary.
Without rewards there could be no values, and the only purpose of estimating values is to

achieve more reward. Nevertheless, it is values with which we are most concerned when
making and evaluating decisions. Action choices are made based on value judgments. We
seek actions that bring about states of highest value, not highest reward, because these
actions obtain the greatest amount of reward for us over the long run. Unfortunately, it
is much harder to determine values than it is to determine rewards. Rewards are basically
given directly by the environment, but values must be estimated and re-estimated from


_1.4._ _Limitations_ _and_ _Scope_ _7_


the sequences of observations an agent makes over its entire lifetime. In fact, the most
important component of almost all reinforcement learning algorithms we consider is a
method for efficiently estimating values. The central role of value estimation is arguably
the most important thing that has been learned about reinforcement learning over the
last six decades.

The fourth and final element of some reinforcement learning systems is a _model_ of
the environment. This is something that mimics the behavior of the environment, or
more generally, that allows inferences to be made about how the environment will behave.
For example, given a state and action, the model might predict the resultant next state
and next reward. Models are used for _planning_, by which we mean any way of deciding
on a course of action by considering possible future situations before they are actually
experienced. Methods for solving reinforcement learning problems that use models and
planning are called _model-based_ methods, as opposed to simpler _model-free_ methods that
are explicitly trial-and-error learners—viewed as almost the _opposite_ of planning. In
Chapter 8 we explore reinforcement learning systems that simultaneously learn by trial
and error, learn a model of the environment, and use the model for planning. Modern
reinforcement learning spans the spectrum from low-level, trial-and-error learning to
high-level, deliberative planning.

###### **1.4 Limitations and Scope**


Reinforcement learning relies heavily on the concept of state—as input to the policy and
value function, and as both input to and output from the model. Informally, we can
think of the state as a signal conveying to the agent some sense of “how the environment
is” at a particular time. The formal definition of state as we use it here is given by
the framework of Markov decision processes presented in Chapter 3. More generally,
however, we encourage the reader to follow the informal meaning and think of the state
as whatever information is available to the agent about its environment. In e↵ect, we
assume that the state signal is produced by some preprocessing system that is nominally
part of the agent’s environment. We do not address the issues of constructing, changing,
or learning the state signal in this book (other than briefly in Section 17.3). We take this
approach not because we consider state representation to be unimportant, but in order
to focus fully on the decision-making issues. In other words, our concern in this book is
not with designing the state signal, but with deciding what action to take as a function
of whatever state signal is available.

Most of the reinforcement learning methods we consider in this book are structured
around estimating value functions, but it is not strictly necessary to do this to solve
reinforcement learning problems. For example, solution methods such as genetic algorithms, genetic programming, simulated annealing, and other optimization methods never
estimate value functions. These methods apply multiple static policies each interacting
over an extended period of time with a separate instance of the environment. The policies
that obtain the most reward, and random variations of them, are carried over to the
next generation of policies, and the process repeats. We call these _evolutionary_ methods
because their operation is analogous to the way biological evolution produces organisms


_8_ _Chapter_ _1:_ _Introduction_


with skilled behavior even if they do not learn during their individual lifetimes. If the
space of policies is sufficiently small, or can be structured so that good policies are
common or easy to find—or if a lot of time is available for the search—then evolutionary
methods can be e↵ective. In addition, evolutionary methods have advantages on problems
in which the learning agent cannot sense the complete state of its environment.

Our focus is on reinforcement learning methods that learn while interacting with the
environment, which evolutionary methods do not do. Methods able to take advantage
of the details of individual behavioral interactions can be much more efficient than
evolutionary methods in many cases. Evolutionary methods ignore much of the useful
structure of the reinforcement learning problem: they do not use the fact that the policy
they are searching for is a function from states to actions; they do not notice which states
an individual passes through during its lifetime, or which actions it selects. In some cases
such information can be misleading (e.g., when states are misperceived), but more often it
should enable more efficient search. Although evolution and learning share many features
and naturally work together, we do not consider evolutionary methods by themselves to
be especially well suited to reinforcement learning problems and, accordingly, we do not
cover them in this book.

###### **1.5 An Extended Example: Tic-Tac-Toe**


To illustrate the general idea of reinforcement learning and contrast it with other approaches, we next consider a single example in more detail.

Consider the familiar child’s game of tic-tac-toe. Two players
take turns playing on a three-by-three board. One player plays
Xs and the other Os until one player wins by placing three marks
in a row, horizontally, vertically, or diagonally, as the X player

neither player getting three in a row, then the game is a draw.

that we are playing against an imperfect player, one whose play
is sometimes incorrect and allows us to win. For the moment, in
fact, let us consider draws and losses to be equally bad for us. How might we construct a
player that will find the imperfections in its opponent’s play and learn to maximize its
chances of winning?

Although this is a simple problem, it cannot readily be solved in a satisfactory way
through classical techniques. For example, the classical “minimax” solution from game
theory is not correct here because it assumes a particular way of playing by the opponent.
For example, a minimax player would never reach a game state from which it could
lose, even if in fact it always won from that state because of incorrect play by the
opponent. Classical optimization methods for sequential decision problems, such as
dynamic programming, can _compute_ an optimal solution for any opponent, but require
as input a complete specification of that opponent, including the probabilities with which
the opponent makes each move in each board state. Let us assume that this information
is not available a priori for this problem, as it is not for the vast majority of problems of










_1.5._ _An_ _Extended_ _Example:_ _Tic-Tac-Toe_ _9_


practical interest. On the other hand, such information can be estimated from experience,
in this case by playing many games against the opponent. About the best one can do
on this problem is first to learn a model of the opponent’s behavior, up to some level of
confidence, and then apply dynamic programming to compute an optimal solution given
the approximate opponent model. In the end, this is not that di↵erent from some of the
reinforcement learning methods we examine later in this book.

An evolutionary method applied to this problem would directly search the space
of possible policies for one with a high probability of winning against the opponent.
Here, a policy is a rule that tells the player what move to make for every state of the
game—every possible configuration of Xs and Os on the three-by-three board. For each
policy considered, an estimate of its winning probability would be obtained by playing
some number of games against the opponent. This evaluation would then direct which
policy or policies were considered next. A typical evolutionary method would hill-climb
in policy space, successively generating and evaluating policies in an attempt to obtain
incremental improvements. Or, perhaps, a genetic-style algorithm could be used that
would maintain and evaluate a population of policies. Literally hundreds of di↵erent
optimization methods could be applied.

Here is how the tic-tac-toe problem would be approached with a method making use
of a value function. First we would set up a table of numbers, one for each possible state
of the game. Each number will be the latest estimate of the probability of our winning
from that state. We treat this estimate as the state’s _value_, and the whole table is the
learned value function. State A has higher value than state B, or is considered “better”
than state B, if the current estimate of the probability of our winning from A is higher
than it is from B. Assuming we always play Xs, then for all states with three Xs in a row
the probability of winning is 1, because we have already won. Similarly, for all states
with three Os in a row, or that are filled up, the correct probability is 0, as we cannot
win from them. We set the initial values of all the other states to 0.5, representing a
guess that we have a 50% chance of winning.

We then play many games against the opponent. To select our moves we examine the
states that would result from each of our possible moves (one for each blank space on the
board) and look up their current values in the table. Most of the time we move _greedily_,
selecting the move that leads to the state with greatest value, that is, with the highest
estimated probability of winning. Occasionally, however, we select randomly from among
the other moves instead. These are called _exploratory_ moves because they cause us to
experience states that we might otherwise never see. A sequence of moves made and
considered during a game can be diagrammed as in Figure 1.1.

While we are playing, we change the values of the states in which we find ourselves
during the game. We attempt to make them more accurate estimates of the probabilities
of winning. To do this, we “back up” the value of the state after each greedy move to
the state before the move, as suggested by the arrows in Figure 1.1. More precisely, the
current value of the earlier state is updated to be closer to the value of the later state.
This can be done by moving the earlier state’s value a fraction of the way toward the
value of the later state. If we let _St_ denote the state before the greedy move, and _St_ +1
the state after that move, then the update to the estimated value of _St_, denoted _V_ ( _St_ ),


_10_ _Chapter_ _1:_ _Introduction_



starting position



starting position





opponent's move
# {


our move
# {


opponent's move
# {


our move
# {


opponent's move
# {


our move
# {









































**Figure** **1.1:** A sequence of tic-tac-toe moves. The solid black lines represent the moves taken
during a game; the dashed lines represent moves that we (our reinforcement learning player)
considered but did not make. The - indicates the move currently estimated to be the best. Our
second move was an exploratory move, meaning that it was taken even though another sibling
move, the one leading to e _[⇤]_, was ranked higher. Exploratory moves do not result in any learning,
but each of our other moves does, causing updates as suggested by the red arrows in which
estimated values are moved up the tree from later nodes to earlier nodes as detailed in the text.


can be written as



h



_V_ ( _St_ ) _V_ ( _St_ ) + _↵_



_V_ ( _St_ +1) _V_ ( _St_ )
_−_



i

_,_



where _↵_ is a small positive fraction called the _step-size_ _parameter_, which influences
the rate of learning. This update rule is an example of a _temporal-di↵erence_ learning
method, so called because its changes are based on a di↵erence, _V_ ( _St_ +1) _V_ ( _St_ ), between

_−_
estimates at two successive times.

The method described above performs quite well on this task. For example, if the
step-size parameter is reduced properly over time, then this method converges, for any
fixed opponent, to the true probabilities of winning from each state given optimal play
by our player. Furthermore, the moves then taken (except on exploratory moves) are in
fact the optimal moves against this (imperfect) opponent. In other words, the method
converges to an optimal policy for playing the game against this opponent. If the step-size
parameter is not reduced all the way to zero over time, then this player also plays well
against opponents that slowly change their way of playing.


_1.5._ _An_ _Extended_ _Example:_ _Tic-Tac-Toe_ _11_


This example illustrates the di↵erences between evolutionary methods and methods
that learn value functions. To evaluate a policy, an evolutionary method holds the policy
fixed and plays many games against the opponent or simulates many games using a model
of the opponent. The frequency of wins gives an unbiased estimate of the probability
of winning with that policy, and can be used to direct the next policy selection. But
each policy change is made only after many games, and only the final outcome of each
game is used: what happens _during_ the games is ignored. For example, if the player wins,
then _all_ of its behavior in the game is given credit, independently of how specific moves
might have been critical to the win. Credit is even given to moves that never occurred!
Value function methods, in contrast, allow individual states to be evaluated. In the end,
evolutionary and value function methods both search the space of policies, but learning a
value function takes advantage of information available during the course of play.

This simple example illustrates some of the key features of reinforcement learning
methods. First, there is the emphasis on learning while interacting with an environment,
in this case with an opponent player. Second, there is a clear goal, and correct behavior
requires planning or foresight that takes into account delayed e↵ects of one’s choices. For
example, the simple reinforcement learning player would learn to set up multi-move traps
for a shortsighted opponent. It is a striking feature of the reinforcement learning solution
that it can achieve the e↵ects of planning and lookahead without using a model of the
opponent and without conducting an explicit search over possible sequences of future
states and actions.

While this example illustrates some of the key features of reinforcement learning, it is
so simple that it might give the impression that reinforcement learning is more limited
than it really is. Although tic-tac-toe is a two-person game, reinforcement learning
also applies in the case in which there is no external adversary, that is, in the case of
a “game against nature.” Reinforcement learning also is not restricted to problems in
which behavior breaks down into separate episodes, like the separate games of tic-tac-toe,
with reward only at the end of each episode. It is just as applicable when behavior
continues indefinitely and when rewards of various magnitudes can be received at any
time. Reinforcement learning is also applicable to problems that do not even break down
into discrete time steps like the plays of tic-tac-toe. The general principles apply to
continuous-time problems as well, although the theory gets more complicated and we
omit it from this introductory treatment.

Tic-tac-toe has a relatively small, finite state set, whereas reinforcement learning can
be used when the state set is very large, or even infinite. For example, Gerry Tesauro
(1992, 1995) combined the algorithm described above with an artificial neural network to

learn to play backgammon, which has approximately 10 [20] states. With this many states
it is impossible ever to experience more than a small fraction of them. Tesauro’s program
learned to play far better than any previous program and eventually better than the
world’s best human players (see Section 16.1). The artificial neural network provides the
program with the ability to generalize from its experience, so that in new states it selects
moves based on information saved from similar states faced in the past, as determined
by the network. How well a reinforcement learning system can work in problems with
such large state sets is intimately tied to how appropriately it can generalize from past


_12_ _Chapter_ _1:_ _Introduction_


experience. It is in this role that we have the greatest need for supervised learning
methods within reinforcement learning. Artificial neural networks and deep learning
(Section 9.7) are not the only, or necessarily the best, way to do this.

In this tic-tac-toe example, learning started with no prior knowledge beyond the
rules of the game, but reinforcement learning by no means entails a tabula rasa view of
learning and intelligence. On the contrary, prior information can be incorporated into
reinforcement learning in a variety of ways that can be critical for efficient learning (e.g.,
see Sections 9.5, 17.4, and 13.1). We also have access to the true state in the tic-tac-toe
example, whereas reinforcement learning can also be applied when part of the state is
hidden, or when di↵erent states appear to the learner to be the same.

Finally, the tic-tac-toe player was able to look ahead and know the states that would
result from each of its possible moves. To do this, it had to have a model of the game
that allowed it to foresee how its environment would change in response to moves that it
might never make. Many problems are like this, but in others even a short-term model
of the e↵ects of actions is lacking. Reinforcement learning can be applied in either case.
A model is not required, but models can easily be used if they are available or can be
learned (Chapter 8).

On the other hand, there are reinforcement learning methods that do not need any
kind of environment model at all. Model-free systems cannot even think about how
their environments will change in response to a single action. The tic-tac-toe player is
model-free in this sense with respect to its opponent: it has no model of its opponent
of any kind. Because models have to be reasonably accurate to be useful, model-free
methods can have advantages over more complex methods when the real bottleneck in
solving a problem is the difficulty of constructing a sufficiently accurate environment
model. Model-free methods are also important building blocks for model-based methods.
In this book we devote several chapters to model-free methods before we discuss how
they can be used as components of more complex model-based methods.

Reinforcement learning can be used at both high and low levels in a system. Although
the tic-tac-toe player learned only about the basic moves of the game, nothing prevents
reinforcement learning from working at higher levels where each of the “actions” may
itself be the application of a possibly elaborate problem-solving method. In hierarchical
learning systems, reinforcement learning can work simultaneously on several levels.


_Exercise_ _1.1:_ _Self-Play_ Suppose, instead of playing against a random opponent, the
reinforcement learning algorithm described above played against itself, with both sides
learning. What do you think would happen in this case? Would it learn a di↵erent policy
for selecting moves? ⇤

_Exercise_ _1.2:_ _Symmetries_ Many tic-tac-toe positions appear di↵erent but are really
the same because of symmetries. How might we amend the learning process described
above to take advantage of this? In what ways would this change improve the learning
process? Now think again. Suppose the opponent did not take advantage of symmetries.
In that case, should we? Is it true, then, that symmetrically equivalent positions should
necessarily have the same value? ⇤

_Exercise_ _1.3:_ _Greedy_ _Play_ Suppose the reinforcement learning player was _greedy_, that is,
it always played the move that brought it to the position that it rated the best. Might it


_1.7._ _Early_ _History_ _of_ _Reinforcement_ _Learning_ _13_


learn to play better, or worse, than a nongreedy player? What problems might occur? ⇤

_Exercise_ _1.4:_ _Learning_ _from_ _Exploration_ Suppose learning updates occurred after _all_
moves, including exploratory moves. If the step-size parameter is appropriately reduced
over time (but not the tendency to explore), then the state values would converge to
a di↵erent set of probabilities. What (conceptually) are the two sets of probabilities
computed when we do, and when we do not, learn from exploratory moves? Assuming
that we do continue to make exploratory moves, which set of probabilities might be better
to learn? Which would result in more wins? ⇤

_Exercise_ _1.5:_ _Other_ _Improvements_ Can you think of other ways to improve the reinforcement learning player? Can you think of any better way to solve the tic-tac-toe problem
as posed? ⇤

###### **1.6 Summary**


Reinforcement learning is a computational approach to understanding and automating
goal-directed learning and decision making. It is distinguished from other computational
approaches by its emphasis on learning by an agent from direct interaction with its
environment, without requiring exemplary supervision or complete models of the environment. In our opinion, reinforcement learning is the first field to seriously address the
computational issues that arise when learning from interaction with an environment in
order to achieve long-term goals.

Reinforcement learning uses the formal framework of Markov decision processes to
define the interaction between a learning agent and its environment in terms of states,
actions, and rewards. This framework is intended to be a simple way of representing
essential features of the artificial intelligence problem. These features include a sense of
cause and e↵ect, a sense of uncertainty and nondeterminism, and the existence of explicit
goals.

The concepts of value and value function are key to most of the reinforcement learning
methods that we consider in this book. We take the position that value functions
are important for efficient search in the space of policies. The use of value functions
distinguishes reinforcement learning methods from evolutionary methods that search
directly in policy space guided by evaluations of entire policies.

###### **1.7 Early History of Reinforcement Learning**


The early history of reinforcement learning has two main threads, both long and rich, that
were pursued independently before intertwining in modern reinforcement learning. One
thread concerns learning by trial and error, and originated in the psychology of animal
learning. This thread runs through some of the earliest work in artificial intelligence
and led to the revival of reinforcement learning in the early 1980s. The second thread
concerns the problem of optimal control and its solution using value functions and
dynamic programming. For the most part, this thread did not involve learning. The
two threads were mostly independent, but became interrelated to some extent around a


### **Chapter 3**

## **Finite Markov Decision** **Processes**

In this chapter we introduce the formal problem of finite Markov decision processes, or
finite MDPs, which we try to solve in the rest of the book. This problem involves evaluative
feedback, as in bandits, but also an associative aspect—choosing di↵erent actions in
di↵erent situations. MDPs are a classical formalization of sequential decision making,
where actions influence not just immediate rewards, but also subsequent situations,
or states, and through those future rewards. Thus MDPs involve delayed reward and
the need to trade o↵immediate and delayed reward. Whereas in bandit problems we
estimated the value _q_ ( _a_ ) of each action _a_, in MDPs we estimate the value _q_ ( _s, a_ ) of
_⇤_ _⇤_
each action _a_ in each state _s_, or we estimate the value _v_ ( _s_ ) of each state given optimal
_⇤_
action selections. These state-dependent quantities are essential to accurately assigning
credit for long-term consequences to individual action selections.

MDPs are a mathematically idealized form of the reinforcement learning problem
for which precise theoretical statements can be made. We introduce key elements of
the problem’s mathematical structure, such as returns, value functions, and Bellman
equations. We try to convey the wide range of applications that can be formulated as
finite MDPs. As in all of artificial intelligence, there is a tension between breadth of
applicability and mathematical tractability. In this chapter we introduce this tension
and discuss some of the trade-o↵s and challenges that it implies. Some ways in which
reinforcement learning can be taken beyond MDPs are treated in Chapter 17.

###### **3.1 The Agent–Environment Interface**


MDPs are meant to be a straightforward framing of the problem of learning from
interaction to achieve a goal. The learner and decision maker is called the _agent_ . The
thing it interacts with, comprising everything outside the agent, is called the _environment_ .
These interact continually, the agent selecting actions and the environment responding to


_48_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


these actions and presenting new situations to the agent. [1] The environment also gives
rise to rewards, special numerical values that the agent seeks to maximize over time
through its choice of actions.





state

_St_









action
_At_



**Figure** **3.1:** The agent–environment interaction in a Markov decision process.


More specifically, the agent and environment interact at each of a sequence of discrete
time steps, _t_ = 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ . [2] At each time step _t_, the agent receives some representation
of the environment’s _state_, _St_ S, and on that basis selects an _action_, _At_ A( _s_ ). [3] One
_2_ _2_
time step later, in part as a consequence of its action, the agent receives a numerical
_reward_, _Rt_ +1 _2_ R _⇢_ R, and finds itself in a new state, _St_ +1. [4] The MDP and agent

together thereby give rise to a sequence or _trajectory_ that begins like this:


_S_ 0 _, A_ 0 _, R_ 1 _, S_ 1 _, A_ 1 _, R_ 2 _, S_ 2 _, A_ 2 _, R_ 3 _, . . ._ (3.1)


In a _finite_ MDP, the sets of states, actions, and rewards (S, A, and R) all have a finite
number of elements. In this case, the random variables _Rt_ and _St_ have well defined
discrete probability distributions dependent only on the preceding state and action. That
is, for particular values of these random variables, _s_ _[0]_ _2_ S and _r_ _2_ R, there is a probability
of those values occurring at time _t_, given particular values of the preceding state and
action:


_._
_p_ ( _s_ _[0]_ _, r_ _s, a_ ) = Pr _St_ = _s0, Rt_ = _r_ _St_ 1 = _s, At_ 1 = _a_ _,_ (3.2)
_|_ _{_ _|_ _−_ _−_ _}_

for all _s_ _[0]_ _, s 2_ S, _r_ _2_ R, and _a 2_ A( _s_ ). The function _p_ defines the _dynamics_ of the MDP.
The dot over the equals sign in the equation reminds us that it is a definition (in this
case of the function _p_ ) rather than a fact that follows from previous definitions. The
dynamics function _p_ : S _⇥_ R _⇥_ S _⇥_ A _!_ [0 _,_ 1] is an ordinary deterministic function of four
arguments. The ‘ _|_ ’ in the middle of it comes from the notation for conditional probability,

1We use the terms _agent_, _environment_, and _action_ instead of the engineers’ terms _controller_, _controlled_
_system_ (or _plant_ ), and _control_ _signal_ because they are meaningful to a wider audience.

2We restrict attention to discrete time to keep things as simple as possible, even though many of the
ideas can be extended to the continuous-time case (e.g., see Bertsekas and Tsitsiklis, 1996; Doya, 1996).

3To simplify notation, we sometimes assume the special case in which the action set is the same in all
states and write it simply as A.

4We use _Rt_ +1 instead of _Rt_ to denote the reward due to _At_ because it emphasizes that the next
reward and next state, _Rt_ +1 and _St_ +1, are jointly determined. Unfortunately, both conventions are
widely used in the literature.


_3.1._ _The_ _Agent–Environment_ _Interface_ _49_


but here it just reminds us that _p_ specifies a probability distribution for each choice of _s_
and _a_, that is, that



X


_s_ _[0]_ _2_ S



X


_r2_ R



_p_ ( _s_ _[0]_ _, r_ _|s, a_ ) = 1 _,_ for all _s 2_ S _, a 2_ A( _s_ ) _._ (3.3)



In a _Markov_ decision process, the probabilities given by _p_ completely characterize the
environment’s dynamics. That is, the probability of each possible value for _St_ and _Rt_
depends on the immediately preceding state and action, _St−_ 1 and _At−_ 1, and, given them,
not at all on earlier states and actions. This is best viewed as a restriction not on the
decision process, but on the _state_ . The state must include information about all aspects
of the past agent–environment interaction that make a di↵erence for the future. If it
does, then the state is said to have the _Markov_ _property_ . We will assume the Markov
property throughout this book, though starting in Part II we will consider approximation
methods that do not rely on it, and in Chapter 17 we consider how a Markov state can
be efficiently learned and constructed from non-Markov observations.

From the four-argument dynamics function, _p_, one can compute anything else one might
want to know about the environment, such as the _state-transition_ _probabilities_ (which we
denote, with a slight abuse of notation, as a three-argument function _p_ : S _⇥_ S _⇥_ A _!_ [0 _,_ 1]),



_._
_p_ ( _s_ _[0]_ _s, a_ ) = Pr _St_ = _s0_ _St_ 1 = _s, At_ 1 = _a_ =
_|_ _{_ _|_ _−_ _−_ _}_



X


_r2_ R



_p_ ( _s_ _[0]_ _, r_ _|s, a_ ) _._ (3.4)



We can also compute the expected rewards for state–action pairs as a two-argument



function _r_ : S _⇥_ A _!_ R:

_._
_r_ ( _s, a_ ) = E[ _Rt_ _St_ 1 = _s, At_ 1 = _a_ ] =
_|_ _−_ _−_



X


_r2_ R



_r_



X


_s_ _[0]_ _2_ S



_p_ ( _s_ _[0]_ _, r_ _|s, a_ ) _,_ (3.5)



and the expected rewards for state–action–next-state triples as a three-argument function
_r_ : S _⇥_ A _⇥_ S _!_ R,



_._
_r_ ( _s, a, s_ _[0]_ ) = E[ _Rt_ _St_ 1 = _s, At_ 1 = _a, St_ = _s0_ ] =
_|_ _−_ _−_



X



_r2_ R



_r_ _[p]_ [(] _[s][0][, r]_ _[|][s, a]_ [)] (3.6)

_p_ ( _s_ _[0]_ _s, a_ ) _[.]_
_|_



In this book, we usually use the four-argument _p_ function (3.2), but each of these other
notations are also occasionally convenient.

The MDP framework is abstract and flexible and can be applied to many di↵erent
problems in many di↵erent ways. For example, the time steps need not refer to fixed
intervals of real time; they can refer to arbitrary successive stages of decision making
and acting. The actions can be low-level controls, such as the voltages applied to the
motors of a robot arm, or high-level decisions, such as whether or not to have lunch or
to go to graduate school. Similarly, the states can take a wide variety of forms. They
can be completely determined by low-level sensations, such as direct sensor readings, or
they can be more high-level and abstract, such as symbolic descriptions of objects in a
room. Some of what makes up a state could be based on memory of past sensations or


_50_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


even be entirely mental or subjective. For example, an agent could be in the state of not
being sure where an object is, or of having just been surprised in some clearly defined
sense. Similarly, some actions might be totally mental or computational. For example,
some actions might control what an agent chooses to think about, or where it focuses its
attention. In general, actions can be any decisions we want to learn how to make, and
states can be anything we can know that might be useful in making them.

In particular, the boundary between agent and environment is typically not the same
as the physical boundary of a robot’s or an animal’s body. Usually, the boundary is
drawn closer to the agent than that. For example, the motors and mechanical linkages of
a robot and its sensing hardware should usually be considered parts of the environment
rather than parts of the agent. Similarly, if we apply the MDP framework to a person
or animal, the muscles, skeleton, and sensory organs should be considered part of the
environment. Rewards, too, presumably are computed inside the physical bodies of
natural and artificial learning systems, but are considered external to the agent.

The general rule we follow is that anything that cannot be changed arbitrarily by
the agent is considered to be outside of it and thus part of its environment. We do
not assume that everything in the environment is unknown to the agent. For example,
the agent often knows quite a bit about how its rewards are computed as a function of
its actions and the states in which they are taken. But we always consider the reward
computation to be external to the agent because it defines the task facing the agent and
thus must be beyond its ability to change arbitrarily. In fact, in some cases the agent may
know _everything_ about how its environment works and still face a difficult reinforcement
learning task, just as we may know exactly how a puzzle like Rubik’s cube works, but
still be unable to solve it. The agent–environment boundary represents the limit of the
agent’s _absolute_ _control_, not of its knowledge.

The agent–environment boundary can be located at di↵erent places for di↵erent
purposes. In a complicated robot, many di↵erent agents may be operating at once, each
with its own boundary. For example, one agent may make high-level decisions which form
part of the states faced by a lower-level agent that implements the high-level decisions. In
practice, the agent–environment boundary is determined once one has selected particular
states, actions, and rewards, and thus has identified a specific decision-making task of
interest.

The MDP framework is a considerable abstraction of the problem of goal-directed
learning from interaction. It proposes that whatever the details of the sensory, memory,
and control apparatus, and whatever objective one is trying to achieve, any problem of
learning goal-directed behavior can be reduced to three signals passing back and forth
between an agent and its environment: one signal to represent the choices made by the
agent (the actions), one signal to represent the basis on which the choices are made (the
states), and one signal to define the agent’s goal (the rewards). This framework may not
be sufficient to represent all decision-learning problems usefully, but it has proved to be
widely useful and applicable.

Of course, the particular states and actions vary greatly from task to task, and how
they are represented can strongly a↵ect performance. In reinforcement learning, as in
other kinds of learning, such representational choices are at present more art than science.


_3.1._ _The_ _Agent–Environment_ _Interface_ _51_


In this book we o↵er some advice and examples regarding good ways of representing
states and actions, but our primary focus is on general principles for learning how to
behave once the representations have been selected.


**Example 3.1:** **Bioreactor** Suppose reinforcement learning is being applied to determine
moment-by-moment temperatures and stirring rates for a bioreactor (a large vat of
nutrients and bacteria used to produce useful chemicals). The actions in such an
application might be target temperatures and target stirring rates that are passed to
lower-level control systems that, in turn, directly activate heating elements and motors to
attain the targets. The states are likely to be thermocouple and other sensory readings,
perhaps filtered and delayed, plus symbolic inputs representing the ingredients in the
vat and the target chemical. The rewards might be moment-by-moment measures of the
rate at which the useful chemical is produced by the bioreactor. Notice that here each
state is a list, or vector, of sensor readings and symbolic inputs, and each action is a
vector consisting of a target temperature and a stirring rate. It is typical of reinforcement
learning tasks to have states and actions with such structured representations. Rewards,
on the other hand, are always single numbers.


**Example** **3.2:** **Pick-and-Place** **Robot** Consider using reinforcement learning to
control the motion of a robot arm in a repetitive pick-and-place task. If we want to learn
movements that are fast and smooth, the learning agent will have to control the motors
directly and have low-latency information about the current positions and velocities
of the mechanical linkages. The actions in this case might be the voltages applied to
each motor at each joint, and the states might be the latest readings of joint angles and
velocities. The reward might be +1 for each object successfully picked up and placed. To
encourage smooth movements, on each time step a small, negative reward could be given
as a function of the moment-to-moment jerkiness of the motion.


_Exercise_ _3.1_ Devise three example tasks of your own that fit into the MDP framework,

identifying for each its states, actions, and rewards. Make the three examples as _di↵erent_
from each other as possible. The framework is abstract and flexible and can be applied in
many di↵erent ways. Stretch its limits in some way in at least one of your examples. ⇤


_Exercise_ _3.2_ Is the MDP framework adequate to usefully represent _all_ goal-directed

learning tasks? Can you think of any clear exceptions? ⇤


_Exercise_ _3.3_ Consider the problem of driving. You could define the actions in terms of

the accelerator, steering wheel, and brake, that is, where your body meets the machine.
Or you could define them farther out—say, where the rubber meets the road, considering
your actions to be tire torques. Or you could define them farther in—say, where your
brain meets your body, the actions being muscle twitches to control your limbs. Or you
could go to a really high level and say that your actions are your choices of _where_ to drive.
What is the right level, the right place to draw the line between agent and environment?

On what basis is one location of the line to be preferred over another? Is there any
fundamental reason for preferring one location over another, or is it a free choice? ⇤


_52_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_






















_3.2._ _Goals_ _and_ _Rewards_ _53_





_Exercise_ _3.4_ Give a table analogous to that in Example 3.3, but for _p_ ( _s_ _[0]_ _, r_ _|s, a_ ). It
should have columns for _s_, _a_, _s_ _[0]_, _r_, and _p_ ( _s_ _[0]_ _, r_ _|s, a_ ), and a row for every 4-tuple for which
_p_ ( _s_ _[0]_ _, r_ _|s, a_ ) _>_ 0. ⇤

###### **3.2 Goals and Rewards**


In reinforcement learning, the purpose or goal of the agent is formalized in terms of a
special signal, called the _reward_, passing from the environment to the agent. At each time
step, the reward is a simple number, _Rt_ _2_ R. Informally, the agent’s goal is to maximize
the total amount of reward it receives. This means maximizing not immediate reward,
but cumulative reward in the long run. We can clearly state this informal idea as the
_reward_ _hypothesis_ :


That all of what we mean by goals and purposes can be well thought of as
the maximization of the expected value of the cumulative sum of a received
scalar signal (called reward).


The use of a reward signal to formalize the idea of a goal is one of the most distinctive
features of reinforcement learning.

Although formulating goals in terms of reward signals might at first appear limiting,
in practice it has proved to be flexible and widely applicable. The best way to see this is
to consider examples of how it has been, or could be, used. For example, to make a robot
learn to walk, researchers have provided reward on each time step proportional to the
robot’s forward motion. In making a robot learn how to escape from a maze, the reward
is often _−_ 1 for every time step that passes prior to escape; this encourages the agent to
escape as quickly as possible. To make a robot learn to find and collect empty soda cans
for recycling, one might give it a reward of zero most of the time, and then a reward of
+1 for each can collected. One might also want to give the robot negative rewards when

it bumps into things or when somebody yells at it. For an agent to learn to play checkers
or chess, the natural rewards are +1 for winning, _−_ 1 for losing, and 0 for drawing and
for all nonterminal positions.

You can see what is happening in all of these examples. The agent always learns to
maximize its reward. If we want it to do something for us, we must provide rewards
to it in such a way that in maximizing them the agent will also achieve our goals. It


_54_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


is thus critical that the rewards we set up truly indicate what we want accomplished.
In particular, the reward signal is not the place to impart to the agent prior knowledge
about _how_ to achieve what we want it to do. [5] For example, a chess-playing agent should
be rewarded only for actually winning, not for achieving subgoals such as taking its
opponent’s pieces or aining control of the center of the board. If achieving these sorts
of subgoals were rewarded, then the agent might find a way to achieve them without
achieving the real goal. For example, it might find a way to take the opponent’s pieces
even at the cost of losing the game. The reward signal is your way of communicating to
the agent _what_ you want achieved, not _how_ you want it achieved. [6]

###### **3.3 Returns and Episodes**


So far we have discussed informally the objective of learning. We have said that the
agent’s goal is to maximize the cumulative reward it receives in the long run. How might
this be defined formally? If the sequence of rewards received after time step _t_ is denoted
_Rt_ +1 _, Rt_ +2 _, Rt_ +3 _, . . ._, then what precise aspect of this sequence do we wish to maximize?
In general, we seek to maximize the _expected_ _return_, where the return, denoted _Gt_, is
defined as some specific function of the reward sequence. In the simplest case the return
is the sum of the rewards:

_Gt_ = _[.]_ _Rt_ +1 + _Rt_ +2 + _Rt_ +3 + _· · ·_ + _RT,_ (3.7)


where _T_ is a final time step. This approach makes sense in applications in which there
is a natural notion of final time step, that is, when the agent–environment interaction
breaks naturally into subsequences, which we call _episodes_, [7] such as plays of a game,
trips through a maze, or any sort of repeated interaction. Each episode ends in a special
state called the _terminal_ _state_, followed by a reset to a standard starting state or to a
sample from a standard distribution of starting states. Even if you think of episodes as
ending in di↵erent ways, such as winning and losing a game, the next episode begins
independently of how the previous one ended. Thus the episodes can all be considered to
end in the same terminal state, with di↵erent rewards for the di↵erent outcomes. Tasks
with episodes of this kind are called _episodic_ _tasks_ . In episodic tasks we sometimes need
to distinguish the set of all nonterminal states, denoted S, from the set of all states plus
the terminal state, denoted S [+] . The time of termination, _T_, is a random variable that
normally varies from episode to episode.

On the other hand, in many cases the agent–environment interaction does not break
naturally into identifiable episodes, but goes on continually without limit. For example,
this would be the natural way to formulate an on-going process-control task, or an
application to a robot with a long life span. We call these _continuing_ _tasks_ . The return
formulation (3.7) is problematic for continuing tasks because the final time step would be
_T_ = _1_, and the return, which is what we are trying to maximize, could easily be infinite.

5Better places for imparting this kind of prior knowledge are the initial policy or initial value function.
6Section 17.4 delves further into the issue of designing e↵ective reward signals.
7Episodes are sometimes called “trials” in the literature.


_3.3._ _Returns_ _and_ _Episodes_ _55_


(For example, suppose the agent receives a reward of +1 at each time step.) Thus, in this

book we usually use a definition of return that is slightly more complex conceptually but
much simpler mathematically.

The additional concept that we need is that of _discounting_ . According to this approach,
the agent tries to select actions so that the sum of the discounted rewards it receives over
the future is maximized. In particular, it chooses _At_ to maximize the expected _discounted_
_return_ :



_Gt_ = _._ _Rt_ +1 + _γRt_ +2 + _γ_ 2 _Rt_ +3 + _· · ·_ =



X _1_


_k_ =0



_γ_ _[k]_ _Rt_ + _k_ +1 _,_ (3.8)



where _γ_ is a parameter, 0 __ _γ_ __ 1, called the _discount_ _rate_ .

The discount rate determines the present value of future rewards: a reward received
_k_ time steps in the future is worth only _γ_ _[k][−]_ [1] times what it would be worth if it were
received immediately. If _γ_ _<_ 1, the infinite sum in (3.8) has a finite value as long as the
reward sequence _Rk_ is bounded. If _γ_ = 0, the agent is “myopic” in being concerned
_{_ _}_
only with maximizing immediate rewards: its objective in this case is to learn how to
choose _At_ so as to maximize only _Rt_ +1. If each of the agent’s actions happened to
influence only the immediate reward, not future rewards as well, then a myopic agent
could maximize (3.8) by separately maximizing each immediate reward. But in general,
acting to maximize immediate reward can reduce access to future rewards so that the
return is reduced. As _γ_ approaches 1, the return objective takes future rewards into
account more strongly; the agent becomes more farsighted.

Returns at successive time steps are related to each other in a way that is important
for the theory and algorithms of reinforcement learning:



_Gt_ = _[.]_ _Rt_ +1 + _γR_ - _t_ +2 + _γ_ [2] _Rt_ +3 + _γ_ [3] _Rt_ +4 + _· · ·_







= _Rt_ +1 + _γ_




_Rt_ +2 + _γRt_ +3 + _γ_ [2] _Rt_ +4 + _· · ·_



= _Rt_ +1 + _γGt_ +1 (3.9)



Note that this works for all time steps _t < T_, even if termination occurs at _t_ + 1, provided
we define _GT_ = 0. This often makes it easy to compute returns from reward sequences.

Note that although the return (3.8) is a sum of an infinite number of terms, it is still
finite if the reward is nonzero and constant—if _γ_ _<_ 1. For example, if the reward is a
constant +1, then the return is



1
_γ_ _[k]_ = (3.10)
1 _γ_ _[.]_
_−_



_Gt_ =



X _1_


_k_ =0



_Exercise_ _3.5_ The equations in Section 3.1 are for the continuing case and need to be

modified (very slightly) to apply to episodic tasks. Show that you know the modifications
needed by giving the modified version of (3.3). ⇤


_56_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


**Example** **3.4:** **Pole-Balancing**
The objective in this task is to apply
forces to a cart moving along a track
so as to keep a pole hinged to the cart
from falling over: A failure is said to
occur if the pole falls past a given angle
from vertical or if the cart runs o↵the
track. The pole is reset to vertical
after each failure. This task could be
treated as episodic, where the natural
episodes are the repeated attempts to balance the pole. The reward in this case could be
+1 for every time step on which failure did not occur, so that the return at each time

would be the number of steps until failure. In this case, successful balancing forever would
mean a return of infinity. Alternatively, we could treat pole-balancing as a continuing
task, using discounting. In this case the reward would be _−_ 1 on each failure and zero at
all other times. The return at each time would then be related to _−γ_ _[K][−]_ [1], where _K_ is
the number of time steps before failure (as well as to the times of later failures). In either
case, the return is maximized by keeping the pole balanced for as long as possible.


_Exercise_ _3.6_ Suppose you treated pole-balancing as an episodic task but also used
discounting, with all rewards zero except for _−_ 1 upon failure. What then would the
return be at each time? How does this return di↵er from that in the discounted, continuing
formulation of this task? ⇤

_Exercise_ _3.7_ Imagine that you are designing a robot to run a maze. You decide to give it a

reward of +1 for escaping from the maze and a reward of zero at all other times. The task
seems to break down naturally into episodes—the successive runs through the maze—so
you decide to treat it as an episodic task, where the goal is to maximize expected total
reward (3.7). After running the learning agent for a while, you find that it is showing
no improvement in escaping from the maze. What is going wrong? Have you e↵ectively
communicated to the agent what you want it to achieve? ⇤

_Exercise_ _3.8_ Suppose _γ_ = 0 _._ 5 and the following sequence of rewards is received _R_ 1 = 1,
_−_

_R_ 2 = 2, _R_ 3 = 6, _R_ 4 = 3, and _R_ 5 = 2, with _T_ = 5. What are _G_ 0, _G_ 1, _. . ._, _G_ 5? Hint:
Work backwards. ⇤

_Exercise_ _3.9_ Suppose _γ_ = 0 _._ 9 and the reward sequence is _R_ 1 = 2 followed by an infinite

sequence of 7s. What are _G_ 1 and _G_ 0? ⇤

_Exercise_ _3.10_ Prove the second equality in (3.10). ⇤


_3.4._ _Unifed_ _Notation_ _for_ _Episodic_ _and_ _Continuing_ _Tasks_ _57_

###### **3.4 Unified Notation for Episodic and Continuing Tasks**


In the preceding section we described two kinds of reinforcement learning tasks, one
in which the agent–environment interaction naturally breaks down into a sequence of
separate episodes (episodic tasks), and one in which it does not (continuing tasks). The
former case is mathematically easier because each action a↵ects only the finite number of
rewards subsequently received during the episode. In this book we consider sometimes
one kind of problem and sometimes the other, but often both. It is therefore useful to
establish one notation that enables us to talk precisely about both cases simultaneously.

To be precise about episodic tasks requires some additional notation. Rather than one
long sequence of time steps, we need to consider a series of episodes, each of which consists
of a finite sequence of time steps. We number the time steps of each episode starting
anew from zero. Therefore, we have to refer not just to _St_, the state representation at
time _t_, but to _St,i_, the state representation at time _t_ of episode _i_ (and similarly for _At,i_,
_Rt,i_, _⇡t,i_, _Ti_, etc.). However, it turns out that when we discuss episodic tasks we almost
never have to distinguish between di↵erent episodes. We are almost always considering
a particular episode, or stating something that is true for all episodes. Accordingly, in
practice we almost always abuse notation slightly by dropping the explicit reference to
episode number. That is, we write _St_ to refer to _St,i_, and so on.

We need one other convention to obtain a single notation that covers both episodic
and continuing tasks. We have defined the return as a sum over a finite number of terms
in one case (3.7) and as a sum over an infinite number of terms in the other (3.8). These
two can be unified by considering episode termination to be the entering of a special
_absorbing_ _state_ that transitions only to itself and that generates only rewards of zero. For

example, consider the state transition diagram:







_R_ 5 = 0



Here the solid square represents the special absorbing state corresponding to the end of an
episode. Starting from _S_ 0, we get the reward sequence +1 _,_ +1 _,_ +1 _,_ 0 _,_ 0 _,_ 0 _, . . ._ . Summing
these, we get the same return whether we sum over the first _T_ rewards (here _T_ = 3) or
over the full infinite sequence. This remains true even if we introduce discounting. Thus,
we can define the return, in general, according to (3.8), using the convention of omitting
episode numbers when they are not needed, and including the possibility that _γ_ = 1 if the
sum remains defined (e.g., because all episodes terminate). Alternatively, we can write



_Gt_ = _[.]_



X _T_


_k_ = _t_ +1



_γ_ _[k][−][t][−]_ [1] _Rk,_ (3.11)



including the possibility that _T_ = _1_ or _γ_ = 1 (but not both). We use these conventions
throughout the rest of the book to simplify notation and to express the close parallels


_58_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


between episodic and continuing tasks. (Later, in Chapter 10, we will introduce a
formulation that is both continuing and undiscounted.)

###### **3.5 Policies and Value Functions**


Almost all reinforcement learning algorithms involve estimating _value functions_ —functions
of states (or of state–action pairs) that estimate _how_ _good_ it is for the agent to be in a
given state (or how good it is to perform a given action in a given state). The notion
of “how good” here is defined in terms of future rewards that can be expected, or, to
be precise, in terms of expected return. Of course the rewards the agent can expect to
receive in the future depend on what actions it will take. Accordingly, value functions
are defined with respect to particular ways of acting, called policies.

Formally, a _policy_ is a mapping from states to probabilities of selecting each possible
action. If the agent is following policy _⇡_ at time _t_, then _⇡_ ( _a|s_ ) is the probability that
_At_ = _a_ if _St_ = _s_ . Like _p_, _⇡_ is an ordinary function; the “ ” in the middle of _⇡_ ( _a_ _s_ )
_|_ _|_
merely reminds us that it defines a probability distribution over _a 2_ A( _s_ ) for each _s 2_ S.
Reinforcement learning methods specify how the agent’s policy is changed as a result of
its experience.


_Exercise_ _3.11_ If the current state is _St_, and actions are selected according to a stochastic

policy _⇡_, then what is the expectation of _Rt_ +1 in terms of _⇡_ and the four-argument
function _p_ (3.2)? ⇤
The _value_ _function_ of a state _s_ under a policy _⇡_, denoted _v⇡_ ( _s_ ), is the expected return
when starting in _s_ and following _⇡_ thereafter. For MDPs, we can define _v⇡_ formally by



#

_,_ for all _s 2_ S _,_ (3.12)



"
X _1_



_γ_ _[k]_ _Rt_ + _k_ +1



_._
_v⇡_ ( _s_ ) = E _⇡_ [ _Gt_ _|_ _St_ = _s_ ] = E _⇡_



_k_ =0



_St_ = _s_
�����



where E _⇡_ [ _·_ ] denotes the expected value of a random variable given that the agent follows
policy _⇡_, and _t_ is any time step. Note that the value of the terminal state, if any, is
always zero. We call the function _v⇡_ the _state-value_ _function_ _for_ _policy_ _⇡_ .

Similarly, we define the value of taking action _a_ in state _s_ under a policy _⇡_, denoted
_q⇡_ ( _s, a_ ), as the expected return starting from _s_, taking the action _a_, and thereafter
following policy _⇡_ :



"
X _1_



_γ_ _[k]_ _Rt_ + _k_ +1



#



_._ (3.13)



_._
_q⇡_ ( _s, a_ ) = E _⇡_ [ _Gt_ _|_ _St_ = _s, At_ = _a_ ] = E _⇡_



_k_ =0



_St_ = _s, At_ = _a_
�����



We call _q⇡_ the _action-value_ _function_ _for_ _policy_ _⇡_ .

_Exercise_ _3.12_ Give an equation for _v⇡_ in terms of _q⇡_ and _⇡_ . ⇤

_Exercise_ _3.13_ Give an equation for _q⇡_ in terms of _v⇡_ and the four-argument _p_ . ⇤
The value functions _v⇡_ and _q⇡_ can be estimated from experience. For example, if an
agent follows policy _⇡_ and maintains an average, for each state encountered, of the actual
returns that have followed that state, then the average will converge to the state’s value,
_v⇡_ ( _s_ ), as the number of times that state is encountered approaches infinity. If separate


_3.5._ _Policies_ _and_ _Value_ _Functions_ _59_


averages are kept for each action taken in each state, then these averages will similarly
converge to the action values, _q⇡_ ( _s, a_ ). We call estimation methods of this kind _Monte_
_Carlo methods_ because they involve averaging over many random samples of actual returns.

These kinds of methods are presented in Chapter 5. Of course, if there are very many
states, then it may not be practical to keep separate averages for each state individually.
Instead, the agent would have to maintain _v⇡_ and _q⇡_ as parameterized functions (with
fewer parameters than states) and adjust the parameters to better match the observed
returns. This can also produce accurate estimates, although much depends on the nature
of the parameterized function approximator. These possibilities are discussed in Part II
of the book.

A fundamental property of value functions used throughout reinforcement learning and
dynamic programming is that they satisfy recursive relationships similar to that which
we have already established for the return (3.9). For any policy _⇡_ and any state _s_, the
following consistency condition holds between the value of _s_ and the value of its possible
successor states:



_v⇡_ ( _s_ ) = _[.]_ E _⇡_ [ _Gt_ _|_ _St_ = _s_ ]



= EX _⇡_ [ _Rt_ +1 +X _γG_ X _t_ +1 _|_ _St_ = _s_ ] h i (by (3.9))



_r_ + _γ_ E _⇡_ [ _Gt_ +1 _|St_ +1 = _s_ _[0]_ ]



X



_p_ ( _s_ _[0]_ _, r_ _|s, a_ )



h



i



X



_s_ _[0]_ _,r_



X



=


=



_a_

X


_a_



_⇡_ ( _a|s_ )


_⇡_ ( _a|s_ )



_s_ _[0]_

X



_s_ _[0]_



_r_



_r_ + _γv⇡_ ( _s_ _[0]_ )



h



i



_,_ for all _s 2_ S _,_ (3.14)



_p_ ( _s_ _[0]_ _, r_ _|s, a_ )



where it is implicit that the actions, _a_, are taken from the set A( _s_ ), that the next states,
_s_ _[0]_, are taken from the set S (or from S [+] in the case of an episodic problem), and that
the rewards, _r_, are taken from the set R. Note also how in the last equation we have
merged the two sums, one over all the values of _s_ _[0]_ and the other over all the values of _r_,
into one sum over all the possible values of both. We use this kind of merged sum often
to simplify formulas. Note how the final expression can be read easily as an expected
value. It is really a sum over all values of the three variables, _a_, _s_ _[0]_, and _r_ . For each triple,
we compute its probability, _⇡_ ( _a|s_ ) _p_ ( _s_ _[0]_ _, r_ _|s, a_ ), weight the quantity in brackets by that
probability, then sum over all possibilities to get an expected value.


a relationship between the value of a state and the values of

represents a state–action pair. Starting from state _s_, the root

_s_ _[0]_

node at the top, the agent could take any of some set of actions—
three are shown in the diagram—based on its policy _⇡_ . From Backup diagram for _v⇡_
each of these, the environment could respond with one of several next states, _s_ _[0]_ (two are
shown in the figure), along with a reward, _r_, depending on its dynamics given by the
function _p_ . The Bellman equation (3.14) averages over all the possibilities, weighting each
by its probability of occurring. It states that the value of the start state must equal the
(discounted) value of the expected next state, plus the reward expected along the way.













_s_ _[0]_



Backup diagram for _v⇡_


_60_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


The value function _v⇡_ is the unique solution to its Bellman equation. We show in
subsequent chapters how this Bellman equation forms the basis of a number of ways to
compute, approximate, and learn _v⇡_ . We call diagrams like that above _backup_ _diagrams_
because they diagram relationships that form the basis of the update or _backup_ operations
that are at the heart of reinforcement learning methods. These operations transfer
value information _back_ to a state (or a state–action pair) from its successor states (or
state–action pairs). We use backup diagrams throughout the book to provide graphical
summaries of the algorithms we discuss. (Note that, unlike transition graphs, the state
nodes of backup diagrams do not necessarily represent distinct states; for example, a
state might be its own successor.)


**Example 3.5:** **Gridworld** Figure 3.2 (left) shows a rectangular gridworld representation
of a simple finite MDP. The cells of the grid correspond to the states of the environment. At
each cell, four actions are possible: `north`, `south`, `east`, and `west`, which deterministically
cause the agent to move one cell in the respective direction on the grid. Actions that
would take the agent o↵the grid leave its location unchanged, but also result in a reward
of _−_ 1. Other actions result in a reward of 0, except those that move the agent out of the
special states A and B. From state A, all four actions yield a reward of +10 and take the
agent to A _[0]_ . From state B, all actions yield a reward of +5 and take the agent to B _[0]_ .





Actions




|Col1|Col2|A|Col4|B|Col6|
|---|---|---|---|---|---|
|||||+5||
||||+10|B'||
|||||||
|||A'||||


|3.3|8.8|4.4|5.3|1.5|
|---|---|---|---|---|
|1.5|3.0|2.3|1.9|0.5|
|0.1|0.7|0.7|0.4|-0.4|
|-1.0|-0.4|-0.4|-0.6|-1.2|
|-1.9|-1.3|-1.2|-1.4|-2.0|



**Figure** **3.2:** Gridworld example: exceptional reward dynamics (left) and state-value function
for the equiprobable random policy (right).


Suppose the agent selects all four actions with equal probability in all states. Figure 3.2
(right) shows the value function, _v⇡_, for this policy, for the discounted reward case with

_γ_ = 0 _._ 9. This value function was computed by solving the system of linear equations
(3.14). Notice the negative values near the lower edge; these are the result of the high

probability of hitting the edge of the grid there under the random policy. State A is
the best state to be in under this policy. Note that A’s expected return is _less_ than its
immediate reward of 10, because from A the agent is taken to state A _[0]_ from which it is
likely to run into the edge of the grid. State B, on the other hand, is valued _more_ than
its immediate reward of 5, because from B the agent is taken to B _[0]_ which has a positive
value. From B _[0]_ the expected penalty (negative reward) for possibly running into an edge
is more than compensated for by the expected gain for possibly stumbling onto A or B.


_Exercise_ _3.14_ The Bellman equation (3.14) must hold for each state for the value function

_v⇡_ shown in Figure 3.2 (right) of Example 3.5. Show numerically that this equation holds
for the center state, valued at +0 _._ 7, with respect to its four neighboring states, valued at
+2 _._ 3, +0 _._ 4, _−_ 0 _._ 4, and +0 _._ 7. (These numbers are accurate only to one decimal place.) ⇤


_3.5._ _Policies_ _and_ _Value_ _Functions_ _61_


_Exercise_ _3.15_ In the gridworld example, rewards are positive for goals, negative for
running into the edge of the world, and zero the rest of the time. Are the signs of these
rewards important, or only the intervals between them? Prove, using (3.8), that adding a
constant _c_ to all the rewards adds a constant, _vc_, to the values of all states, and thus
does not a↵ect the relative values of any states under any policies. What is _vc_ in terms
of _c_ and _γ_ ? ⇤

_Exercise_ _3.16_ Now consider adding a constant _c_ to all the rewards in an episodic task,

such as maze running. Would this have any e↵ect, or would it leave the task unchanged
as in the continuing task above? Why or why not? Give an example. ⇤

**Example** **3.6:** **Golf** To formulate playing a hole of golf as a reinforcement learning
task, we count a penalty (negative reward) of _−_ 1 for each stroke until we hit the ball
into the hole. The state is the location of the ball. The value of a state is the negative of
the number of strokes to the hole from that location. Our actions are how we aim and
swing at the ball, of course, and which club we select. Let us take the former as given
and consider just the choice of club, which we assume is either a putter or a driver. The
upper part of Figure 3.3 shows a possible state-value function, _v_ `putt` ( _s_ ), for the policy that



always uses the putter. The terminal
state _in-the-hole_ has a value of 0. From
anywhere on the green we assume we can
make a putt; these states have value _−_ 1.
O↵the green we cannot reach the hole by
putting, and the value is lower. If we can
reach the green from a state by putting,
then that state must have value one less
than the green’s value, that is, _−_ 2. For
simplicity, let us assume we can putt very
precisely and deterministically, but with
a limited range. This gives us the sharp
contour line labeled _−_ 2 in the figure; all
locations between that line and the green
require exactly two strokes to complete
the hole. Similarly, any location within
putting range of the _−_ 2 contour line must
have a value of _−_ 3, and so on to get all the
contour lines shown in the figure. Putting
doesn’t get us out of sand traps, so they
have a value of _−1_ . Overall, it takes us
six strokes to get from the tee to the hole
by putting.









_V_

































!2













**Figure** **3.3:** A golf example: the state-value function for putting (upper) and the optimal actionvalue function for using the driver (lower).



_Exercise_ _3.17_ What is the Bellman equation for action values, that
is, for _q⇡_ ? It must give the action value _q⇡_ ( _s, a_ ) in terms of the action
values, _q⇡_ ( _s_ _[0]_ _, a_ _[0]_ ), of possible successors to the state–action pair ( _s, a_ ).
Hint: The backup diagram to the right corresponds to this equation.
Show the sequence of equations analogous to (3.14), but for action
values. ⇤



_s, a_





_a_ _[0]_

_q⇡_ backup diagram


_62_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


_Exercise_ _3.18_ The value of a state depends on the values of the actions possible in that

state and on how likely each action is to be taken under the current policy. We can
think of this in terms of a small backup diagram rooted at the state and considering each
possible action:



taken with





_q⇡_ ( _s, a_ )

Give the equation corresponding to this intuition and diagram for the value at the root
node, _v⇡_ ( _s_ ), in terms of the value at the expected leaf node, _q⇡_ ( _s, a_ ), given _St_ = _s_ . This
equation should include an expectation conditioned on following the policy, _⇡_ . Then give
a second equation in which the expected value is written out explicitly in terms of _⇡_ ( _a|s_ )
such that no expected value notation appears in the equation. ⇤

_Exercise_ _3.19_ The value of an action, _q⇡_ ( _s, a_ ), depends on the expected next reward and

the expected sum of the remaining rewards. Again we can think of this in terms of a
small backup diagram, this one rooted at an action (state–action pair) and branching to
the possible next states:



expected

rewards



_v⇡_ ( _s_ _[0]_ )







1





Give the equation corresponding to this intuition and diagram for the action value,
_q⇡_ ( _s, a_ ), in terms of the expected next reward, _Rt_ +1, and the expected next state value,
_v⇡_ ( _St_ +1), given that _St_ = _s_ and _At_ = _a_ . This equation should include an expectation but
_not_ one conditioned on following the policy. Then give a second equation, writing out the

expected value explicitly in terms of _p_ ( _s_ _[0]_ _, r_ _|s, a_ ) defined by (3.2), such that no expected
value notation appears in the equation. ⇤

###### **3.6 Optimal Policies and Optimal Value Functions**



Solving a reinforcement learning task means, roughly, finding a policy that achieves a lot
of reward over the long run. For finite MDPs, we can precisely define an optimal policy
in the following way. Value functions define a partial ordering over policies. A policy _⇡_ is
defined to be better than or equal to a policy _⇡_ _[0]_ if its expected return is greater than
or equal to that of _⇡_ _[0]_ for all states. In other words, _⇡_ _⇡_ _[0]_ if and only if _v⇡_ ( _s_ ) _v⇡_ _[0]_ ( _s_ )
_≥_ _≥_
for all _s 2_ S. There is always at least one policy that is better than or equal to all other
policies. This is an _optimal_ _policy_ . Although there may be more than one, we denote all
the optimal policies by _⇡_ . They share the same state-value function, called the _optimal_
_⇤_
_state-value_ _function_, denoted _v_, and defined as
_⇤_



_v_ ( _s_ ) = max _[.]_
_⇤_ _⇡_



_v⇡_ ( _s_ ) _,_ (3.15)
_⇡_



for all _s 2_ S.


_3.6._ _Optimal_ _Policies_ _and_ _Optimal_ _Value_ _Functions_ _63_


Optimal policies also share the same _optimal_ _action-value_ _function_, denoted _q_, and
_⇤_
defined as

_q_ ( _s, a_ ) = max _[.]_ _q⇡_ ( _s, a_ ) _,_ (3.16)
_⇤_ _⇡_


for all _s_ _2_ S and _a_ _2_ A( _s_ ). For the state–action pair ( _s, a_ ), this function gives the
expected return for taking action _a_ in state _s_ and thereafter following an optimal policy.
Thus, we can write _q_ in terms of _v_ as follows:
_⇤_ _⇤_

_q_ ( _s, a_ ) = E[ _Rt_ +1 + _γv_ ( _St_ +1) _St_ = _s, At_ = _a_ ] _._ (3.17)
_⇤_ _⇤_ _|_


**Example** **3.7:** **Optimal** **Value** **Functions** **for** **Golf** The lower part of Figure 3.3
shows the contours of a possible optimal action-value function _q_ ( _s,_ `driver` ). These are
_⇤_
the values of each state if we first play a stroke with the driver and afterward select either
the driver or the putter, whichever is better. The driver enables us to hit the ball farther,
but with less accuracy. We can reach the hole in one shot using the driver only if we
are already very close; thus the 1 contour for _q_ ( _s,_ `driver` ) covers only a small portion

_−_ _⇤_
of the green. If we have two strokes, however, then we can reach the hole from much
farther away, as shown by the _−_ 2 contour. In this case we don’t have to drive all the way
to within the small _−_ 1 contour, but only to anywhere on the green; from there we can
use the putter. The optimal action-value function gives the values after committing to a
particular _first_ action, in this case, to the driver, but afterward using whichever actions
are best. The _−_ 3 contour is still farther out and includes the starting tee. From the tee,
the best sequence of actions is two drives and one putt, sinking the ball in three strokes.

Because _v_ is the value function for a policy, it must satisfy the self-consistency
_⇤_
condition given by the Bellman equation for state values (3.14). Because it is the optimal
value function, however, _v_ ’s consistency condition can be written in a special form
_⇤_
without reference to any specific policy. This is the Bellman equation for _v_, or the
_⇤_
_Bellman_ _optimality_ _equation_ . Intuitively, the Bellman optimality equation expresses the

fact that the value of a state under an optimal policy must equal the expected return for
the best action from that state:



_v_ ( _s_ ) = max
_⇤_ _a_ A(



max

_a_ A( _s_ ) _[q][⇡][⇤]_ [(] _[s, a]_ [)]
_2_



E _⇡_ [ _Gt_ _St_ = _s, At_ = _a_ ]
_a_ _⇤_ _|_



= max

_a_

= max

_a_

= max



E _⇡_ [ _Rt_ +1 + _γGt_ +1 _St_ = _s, At_ = _a_ ] (by (3.9))
_a_ _⇤_ _|_

E[ _Rt_ +1 + _γv_ ( _St_ +1) _St_ = _s, At_ = _a_ ] (3.18)
_a_ _⇤_ _|_



X



_r_ + _γv_ ( _s_ _[0]_ )
_⇤_



_._ (3.19)



⇥



⇤



= max

_a_



_s_ _[0]_ _,r_



_p_ ( _s_ _[0]_ _, r_ _|s, a_ )


_64_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_



The last two equations are two forms of the Bellman optimality equation for _v_ . The
_⇤_
Bellman optimality equation for _q_ is
_⇤_



_a_ _[0]_ _[q][⇤]_ [(] _[S][t]_ [+1] _[, a][0]_ [)]



��� _St_ = _s, At_ = _a_ i



i



_q_ ( _s, a_ ) = E
_⇤_



h



_Rt_ +1 + _γ_ max



_a_ _[0]_ _[q][⇤]_ [(] _[s][0][, a][0]_ [)]



_._ (3.20)



h



_r_ + _γ_ max _a_ _[0]_ _[q][⇤]_ [(] _[s][0][, a][0]_ [)]



=



X



_s_ _[0]_ _,r_



_p_ ( _s_ _[0]_ _, r_ _|s, a_ )



The backup diagrams in the figure below show graphically the spans of future states
and actions considered in the Bellman optimality equations for _v_ and _q_ . These are the
_⇤_ _⇤_
same as the backup diagrams for _v⇡_ and _q⇡_ presented earlier except that arcs have been
added at the agent’s choice points to represent that the maximum over that choice is
taken rather than the expected value given some policy. The backup diagram on the left
graphically represents the Bellman optimality equation (3.19) and the backup diagram
on the right graphically represents (3.20).







_s, a_













_s_ _[0]_


**Figure** **3.4:** Backup diagrams for _v_ and _q_
_⇤_ _⇤_



_a_ _[0]_



For finite MDPs, the Bellman optimality equation for _v_ (3.19) has a unique solution.
_⇤_
The Bellman optimality equation is actually a system of equations, one for each state, so
if there are _n_ states, then there are _n_ equations in _n_ unknowns. If the dynamics _p_ of the
environment are known, then in principle one can solve this system of equations for _v_
_⇤_
using any one of a variety of methods for solving systems of nonlinear equations. One
can solve a related set of equations for _q_ .
_⇤_

Once one has _v_, it is relatively easy to determine an optimal policy. For each state
_⇤_
_s_, there will be one or more actions at which the maximum is obtained in the Bellman
optimality equation. Any policy that assigns nonzero probability only to these actions is
an optimal policy. You can think of this as a one-step search. If you have the optimal
value function, _v_, then the actions that appear best after a one-step search will be optimal
_⇤_
actions. Another way of saying this is that any policy that is _greedy_ with respect to the
optimal evaluation function _v_ is an optimal policy. The term greedy is used in computer
_⇤_
science to describe any search or decision procedure that selects alternatives based only
on local or immediate considerations, without considering the possibility that such a
selection may prevent future access to even better alternatives. Consequently, it describes
policies that select actions based only on their short-term consequences. The beauty of _v_
_⇤_
is that if one uses it to evaluate the short-term consequences of actions—specifically, the
one-step consequences—then a greedy policy is actually optimal in the long-term sense in
which we are interested because _v_ already takes into account the reward consequences of
_⇤_
all possible future behavior. By means of _v_, the optimal expected long-term return is
_⇤_


_3.6._ _Optimal_ _Policies_ _and_ _Optimal_ _Value_ _Functions_ _65_


turned into a quantity that is locally and immediately available for each state. Hence, a
one-step-ahead search yields the long-term optimal actions.

Having _q_ makes choosing optimal actions even easier. With _q_, the agent does not
_⇤_ _⇤_
even have to do a one-step-ahead search: for any state _s_, it can simply find any action
that maximizes _q_ ( _s, a_ ). The action-value function e↵ectively caches the results of all
_⇤_
one-step-ahead searches. It provides the optimal expected long-term return as a value
that is locally and immediately available for each state–action pair. Hence, at the cost of
representing a function of state–action pairs, instead of just of states, the optimal actionvalue function allows optimal actions to be selected without having to know anything
about possible successor states and their values, that is, without having to know anything
about the environment’s dynamics.


**Example** **3.8:** **Solving** **the** **Gridworld** Suppose we solve the Bellman equation for _v_
_⇤_
for the simple grid task introduced in Example 3.5 and shown again in Figure 3.5 (left).
Recall that state A is followed by a reward of +10 and transition to state A _[0]_, while state
B is followed by a reward of +5 and transition to state B _[0]_ . Figure 3.5 (middle) shows the
optimal value function, and Figure 3.5 (right) shows the corresponding optimal policies.
Where there are multiple arrows in a cell, all of the corresponding actions are optimal.






|Col1|Col2|A|Col4|B|Col6|
|---|---|---|---|---|---|
|||||+5||
||||+10|B'||
|||||||
|||A'||||


|22.0|24.4|22.0|19.4|17.5|
|---|---|---|---|---|
|19.8|22.0|19.8|17.8|16.0|
|17.8|19.8|17.8|16.0|14.4|
|16.0|17.8|16.0|14.4|13.0|
|14.4|16.0|14.4|13.0|11.7|


##### a) gridworldGridworld b) vvV⇤ ** c) ⇡ ! π ⇤ **


###### a) gridworldGridworld b) vV * c) !*



**Figure** **3.5:** Optimal solutions to the gridworld example.



**Example** **3.9:** **Bellman** **Optimality** **Equations** **for** **the** **Recycling** **Robot** Using
(3.19), we can explicitly give the Bellman optimality equation for the recycling robot

example. To make things more compact, we abbreviate the states `high` and `low`, and the
actions `search`, `wait`, and `recharge` respectively by `h`, `l`, `s`, `w`, and `re` . Because there are
only two states, the Bellman optimality equation consists of two equations. The equation
for _v_ ( `h` ) can be written as follows:
_⇤_







_v_ ( `h` ) = max
_⇤_


= max


= max



⇢
_p_ ( `h` `h` _,_ `s` )[ _r_ ( `h` _,_ `s` _,_ `h` ) + _γv_ ( `h` )] + _p_ ( `l` `h` _,_ `s` )[ _r_ ( `h` _,_ `s` _,_ `l` ) + _γv_ ( `l` )] _,_
_|_ _⇤_ _|_ _⇤_



⇢
_r_ `s` + _γ_ [ _↵v_ ( `h` ) + (1 _↵_ ) _v_ ( `l` )] _,_
_⇤_ _−_ _⇤_



_r_ `w` + _γv_ ( `h` )
_⇤_



⇢



_p_ ( `h` `h` _,_ `w` )[ _r_ ( `h` _,_ `w` _,_ `h` ) + _γv_ ( `h` )] + _p_ ( `l` `h` _,_ `w` )[ _r_ ( `h` _,_ `w` _,_ `l` ) + _γv_ ( `l` )]
_|_ _⇤_ _|_   - _⇤_



_↵_ [ _r_ `s` + _γv_ ( `h` )] + (1 _↵_ )[ _r_ `s` + _γv_ ( `l` )] _,_
_⇤_ _−_ _⇤_
1[ _r_ `w` + _γv_ ( `h` )] + 0[ _r_ `w` + _γv_ ( `l` )]
_⇤_ _⇤_      







_._


_66_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_



Following the same procedure for _v_ ( `l` ) yields the equation
_⇤_



_βr_ `s` _−_ 3(1 _−_ _β_ ) + _γ_ [(1 _−_ _β_ ) _v⇤_ ( `h` ) + _βv⇤_ ( `l` )] _,_
_r_ `w` + _γv_ ( `l` ) _,_
_⇤_
_γv_ ( `h` )
_⇤_



9
=

; _[.]_



_v_ ( `l` ) = max
_⇤_



8
<


:



For any choice of _r_ `s`, _r_ `w`, _↵_, _β_, and _γ_, with 0 _γ_ _<_ 1, 0 _↵, β_ 1, there is exactly
__ __ __
one pair of numbers, _v_ ( `h` ) and _v_ ( `l` ), that simultaneously satisfy these two nonlinear
_⇤_ _⇤_
equations.

Explicitly solving the Bellman optimality equation provides one route to finding an
optimal policy, and thus to solving the reinforcement learning problem. However, this
solution is rarely directly useful. It is akin to an exhaustive search, looking ahead at
all possibilities, computing their probabilities of occurrence and their desirabilities in
terms of expected rewards. This solution relies on at least three assumptions that are
rarely true in practice: (1) the dynamics of the environment are accurately known; (2)
computational resources are sufficient to complete the calculation; and (3) the states
have the Markov property. For the kinds of tasks in which we are interested, one is
generally not able to implement this solution exactly because various combinations of
these assumptions are violated. For example, although the first and third assumptions
present no problems for the game of backgammon, the second is a major impediment.
Because the game has about 10 [20] states, it would take thousands of years on today’s
fastest computers to solve the Bellman equation for _v_, and the same is true for finding
_⇤_
_q_ . In reinforcement learning one typically has to settle for approximate solutions.
_⇤_

Many di↵erent decision-making methods can be viewed as ways of approximately
solving the Bellman optimality equation. For example, heuristic search methods can be
viewed as expanding the right-hand side of (3.19) several times, up to some depth, forming
a “tree” of possibilities, and then using a heuristic evaluation function to approximate
_v_ at the “leaf” nodes. (Heuristic search methods such as A _[⇤]_ are almost always based
_⇤_
on the episodic case.) The methods of dynamic programming can be related even more
closely to the Bellman optimality equation. Many reinforcement learning methods can
be clearly understood as approximately solving the Bellman optimality equation, using
actual experienced transitions in place of knowledge of the expected transitions. We
consider a variety of such methods in the following chapters.


_Exercise_ _3.20_ Draw or describe the optimal state-value function for the golf example. ⇤


_Exercise_ _3.21_ Draw or describe the contours of the optimal action-value function for

putting, _q_ ( _s,_ `putter` ), for the golf example. ⇤
_⇤_

_Exercise_ _3.22_ Consider the continuing MDP shown to the

where two actions are available, left and right. The numbers

each action. There are exactly two deterministic policies,
_⇡_ left and _⇡_ right. What policy is optimal if _γ_ = 0? If _γ_ = 0 _._ 9?
If _γ_ = 0 _._ 5? ⇤


_3.7._ _Optimality_ _and_ _Approximation_ _67_


_Exercise_ _3.23_ Give the Bellman equation for _q_ for the recycling robot. ⇤
_⇤_

_Exercise_ _3.24_ Figure 3.5 gives the optimal value of the best state of the gridworld as
24.4, to one decimal place. Use your knowledge of the optimal policy and (3.8) to express
this value symbolically, and then to compute it to three decimal places. ⇤

_Exercise_ _3.25_ Give an equation for _v_ in terms of _q_ . ⇤
_⇤_ _⇤_

_Exercise_ _3.26_ Give an equation for _q_ in terms of _v_ and the four-argument _p_ . ⇤
_⇤_ _⇤_

_Exercise_ _3.27_ Give an equation for _⇡_ in terms of _q_ . ⇤
_⇤_ _⇤_

_Exercise_ _3.28_ Give an equation for _⇡_ in terms of _v_ and the four-argument _p_ . ⇤
_⇤_ _⇤_

_Exercise_ _3.29_ Rewrite the four Bellman equations for the four value functions ( _v⇡_, _v⇤_, _q⇡_,

and _q_ ) in terms of the three argument function _p_ (3.4) and the two-argument function _r_
_⇤_
(3.5). ⇤

###### **3.7 Optimality and Approximation**


We have defined optimal value functions and optimal policies. Clearly, an agent that

learns an optimal policy has done very well, but in practice this rarely happens. For
the kinds of tasks in which we are interested, optimal policies can be generated only
with extreme computational cost. A well-defined notion of optimality organizes the
approach to learning we describe in this book and provides a way to understand the
theoretical properties of various learning algorithms, but it is an ideal that agents can
only approximate. As we discussed above, even if we have a complete and accurate model
of the environment’s dynamics, it is usually not possible to simply compute an optimal
policy by solving the Bellman optimality equation. For example, board games such as
chess are a tiny fraction of human experience, yet large, custom-designed computers still
cannot compute the optimal moves. A critical aspect of the problem facing the agent is
always the computational power available to it, in particular, the amount of computation
it can perform in a single time step.

The memory available is also an important constraint. A large amount of memory
is often required to build up approximations of value functions, policies, and models.
In tasks with small, finite state sets, it is possible to form these approximations using
arrays or tables with one entry for each state (or state–action pair). This we call the
_tabular_ case, and the corresponding methods we call tabular methods. In many cases

of practical interest, however, there are far more states than could possibly be entries
in a table. In these cases the functions must be approximated, using some sort of more
compact parameterized function representation.

Our framing of the reinforcement learning problem forces us to settle for approximations. However, it also presents us with some unique opportunities for achieving
useful approximations. For example, in approximating optimal behavior, there may be
many states that the agent faces with such a low probability that selecting suboptimal
actions for them has little impact on the amount of reward the agent receives. Tesauro’s
backgammon player, for example, plays with exceptional skill even though it might make


_68_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


very bad decisions on board configurations that never occur in games against experts. In
fact, it is possible that TD-Gammon makes bad decisions for a large fraction of the game’s
state set. The online nature of reinforcement learning makes it possible to approximate
optimal policies in ways that put more e↵ort into learning to make good decisions for
frequently encountered states, at the expense of less e↵ort for infrequently encountered
states. This is one key property that distinguishes reinforcement learning from other
approaches to approximately solving MDPs.

###### **3.8 Summary**


Let us summarize the elements of the reinforcement learning problem that we have
presented in this chapter. Reinforcement learning is about learning from interaction
how to behave in order to achieve a goal. The reinforcement learning _agent_ and its
_environment_ interact over a sequence of discrete time steps. The specification of their

interface defines a particular task: the _actions_ are the choices made by the agent; the
_states_ are the basis for making the choices; and the _rewards_ are the basis for evaluating

the choices. Everything inside the agent is known and controllable. Its environment, on
the other hand, is incompletely controllable and may or may not be completely known.
A _policy_ is a stochastic rule by which the agent selects actions as a function of states.
The agent’s objective is to maximize the amount of reward it receives over time.

When the reinforcement learning setup described above is formulated with well defined
transition probabilities it constitutes a _Markov_ _decision_ _process_ (MDP). A _finite_ _MDP_ is
an MDP with finite state, action, and (as we formulate it here) reward sets. Much of the
current theory of reinforcement learning is restricted to finite MDPs, but the methods
and ideas apply more generally.

The _return_ is the function of future rewards that the agent seeks to maximize (in
expected value). It has several di↵erent definitions depending upon the nature of the
task and whether one wishes to _discount_ delayed reward. The undiscounted formulation
is appropriate for _episodic_ _tasks_, in which the agent–environment interaction breaks
naturally into _episodes_ ; the discounted formulation is appropriate for tabular _continuing_
_tasks_, in which the interaction does not naturally break into episodes but continues
without limit (but see Sections 10.3–4). We try to define the returns for the two kinds of
tasks such that one set of equations can apply to both the episodic and continuing cases.

A policy’s _value_ _functions_ ( _v⇡_ and _q⇡_ ) assign to each state, or state–action pair, the
expected return from that state, or state–action pair, given that the agent uses the
policy. The _optimal_ _value_ _functions_ ( _v_ and _q_ ) assign to each state, or state–action pair,
_⇤_ _⇤_
the largest expected return achievable by any policy. A policy whose value functions
are optimal is an _optimal_ _policy_ . Whereas the optimal value functions for states and
state–action pairs are unique for a given MDP, there can be many optimal policies. Any
policy that is _greedy_ with respect to the optimal value functions must be an optimal
policy. The _Bellman_ _optimality_ _equations_ are special consistency conditions that the
optimal value functions must satisfy and that can, in principle, be solved for the optimal
value functions, from which an optimal policy can be determined with relative ease.


_3.8._ _Summary_ _69_


A reinforcement learning problem can be posed in a variety of di↵erent ways depending
on assumptions about the level of knowledge initially available to the agent. In problems
of _complete_ _knowledge_, the agent has a complete and accurate model of the environment’s
dynamics. If the environment is an MDP, then such a model consists of the complete fourargument dynamics function _p_ (3.2). In problems of _incomplete_ _knowledge_, a complete
and perfect model of the environment is not available.

Even if the agent had a complete and accurate environment model, the agent would
typically be unable to fully use it because of limitations on its memory and computation
per time step. In particular, extensive memory may be required to build up accurate
approximations of value functions, policies, and models. In most cases of practical interest
there are far more states than could possibly be entries in a table, and approximations
must be made.

A well-defined notion of optimality organizes the approach to learning we describe in
this book and provides a way to understand the theoretical properties of various learning
algorithms, but it is an ideal that reinforcement learning agents can only approximate
to varying degrees. In reinforcement learning we are very much concerned with cases in
which optimal solutions cannot be found but must be approximated in some way.

###### **Bibliographical and Historical Remarks**


The reinforcement learning problem is deeply indebted to the idea of Markov decision
processes (MDPs) from the field of optimal control. These historical influences and other
major influences from psychology are described in the brief history given in Chapter 1.
Reinforcement learning adds to MDPs a focus on approximation and incomplete information for realistically large problems. MDPs and the reinforcement learning problem
are only weakly linked to traditional learning and decision-making problems in artificial
intelligence. However, artificial intelligence is now vigorously exploring MDP formulations
for planning and decision making from a variety of perspectives. MDPs are more general
than previous formulations used in artificial intelligence in that they permit more general
kinds of goals and uncertainty.

The theory of MDPs is treated by, for example, Bertsekas (2005), White (1969), Whittle
(1982, 1983), and Puterman (1994). A particularly compact treatment of the finite case

is given by Ross (1983). MDPs are also studied under the heading of stochastic optimal
control, where _adaptive_ optimal control methods are most closely related to reinforcement
learning (e.g., Kumar, 1985; Kumar and Varaiya, 1986).

The theory of MDPs evolved from e↵orts to understand the problem of making sequences
of decisions under uncertainty, where each decision can depend on the previous decisions
and their outcomes. It is sometimes called the theory of multistage decision processes,
or sequential decision processes, and has roots in the statistical literature on sequential
sampling beginning with the papers by Thompson (1933, 1934) and Robbins (1952) that
we cited in Chapter 2 in connection with bandit problems (which are prototypical MDPs
if formulated as multiple-situation problems).

The earliest instance (that we are aware of) in which reinforcement learning was
discussed using the MDP formalism is Andreae’s (1969) description of a unified view of


_70_ _Chapter_ _3:_ _Finite_ _Markov_ _Decision_ _Processes_


learning machines. Witten and Corbin (1973) experimented with a reinforcement learning
system later analyzed by Witten (1977, 1976a) using the MDP formalism. Although
he did not explicitly mention MDPs, Werbos (1977) suggested approximate solution
methods for stochastic optimal control problems that are related to modern reinforcement
learning methods (see also Werbos, 1982, 1987, 1988, 1989, 1992). Although Werbos’s
ideas were not widely recognized at the time, they were prescient in emphasizing the
importance of approximately solving optimal control problems in a variety of domains,
including artificial intelligence. The most influential integration of reinforcement learning
and MDPs is due to Watkins (1989).


**3.1** Our characterization of the dynamics of an MDP in terms of _p_ ( _s_ _[0]_ _, r_ _|s, a_ ) is
slightly unusual. It is more common in the MDP literature to describe the
dynamics in terms of the state transition probabilities _p_ ( _s_ _[0]_ _|s, a_ ) and expected
next rewards _r_ ( _s, a_ ). In reinforcement learning, however, we more often have
to refer to individual actual or sample rewards (rather than just their expected
values). Our notation also makes it plainer that _St_ and _Rt_ are in general jointly
determined, and thus must have the same time index. In teaching reinforcement
learning, we have found our notation to be more straightforward conceptually
and easier to understand.


For a good intuitive discussion of the system-theoretic concept of state, see
Minsky (1967).


The bioreactor example is based on the work of Ungar (1990) and Miller and
Williams (1992). The recycling robot example was inspired by the can-collecting

robot built by Jonathan Connell (1989). Kober and Peters (2012) present a
collection of robotics applications of reinforcement learning.


**3.2** An explicit statement of the reward hypothesis was suggested by Michael Littman
(personal communication).


**3.3–4** The terminology of _episodic_ and _continuing_ tasks is di↵erent from that usually
used in the MDP literature. In that literature it is common to distinguish
three types of tasks: (1) finite-horizon tasks, in which interaction terminates
after a particular _fixed_ number of time steps; (2) indefinite-horizon tasks, in
which interaction can last arbitrarily long but must eventually terminate; and
(3) infinite-horizon tasks, in which interaction does not terminate. Our episodic

and continuing tasks are similar to indefinite-horizon and infinite-horizon tasks,
respectively, but we prefer to emphasize the di↵erence in the nature of the
interaction. This di↵erence seems more fundamental than the di↵erence in the
objective functions emphasized by the usual terms. Often episodic tasks use
an indefinite-horizon objective function and continuing tasks an infinite-horizon
objective function, but we see this as a common coincidence rather than a
fundamental di↵erence.


The pole-balancing example is from Michie and Chambers (1968) and Barto,
Sutton, and Anderson (1983).


_3.8._ _Summary_ _71_


**3.5–6** Assigning value on the basis of what is good or bad in the long run has ancient
roots. In control theory, mapping states to numerical values representing the
long-term consequences of control decisions is a key part of optimal control theory,
which was developed in the 1950s by extending nineteenth century state-function
theories of classical mechanics (see, for example, Schultz and Melsa, 1967). In
describing how a computer could be programmed to play chess, Shannon (1950)
suggested using an evaluation function that took into account the long-term
advantages and disadvantages of chess positions.


Watkins’s (1989) Q-learning algorithm for estimating _q_ (Chapter 6) made action_⇤_
value functions an important part of reinforcement learning, and consequently
these functions are often called “Q-functions.” But the idea of an action-value
function is much older than this. Shannon (1950) suggested that a function
_h_ ( _P, M_ ) could be used by a chess-playing program to decide whether a move _M_
in position _P_ is worth exploring. Michie’s (1961, 1963) MENACE system and
Michie and Chambers’s (1968) BOXES system can be understood as estimating
action-value functions. In classical physics, Hamilton’s principal function is
an action-value function; Newtonian dynamics are greedy with respect to this
function (e.g., Goldstein, 1957). Action-value functions also played a central role
in Denardo’s (1967) theoretical treatment of dynamic programming in terms of
contraction mappings.


The Bellman optimality equation (for _v_ ) was popularized by Richard Bellman
_⇤_
(1957a), who called it the “basic functional equation.” The counterpart of the

Bellman optimality equation for continuous time and state problems is known
as the Hamilton–Jacobi–Bellman equation (or often just the Hamilton–Jacobi
equation), indicating its roots in classical physics (e.g., Schultz and Melsa, 1967).


The golf example was suggested by Chris Watkins.


