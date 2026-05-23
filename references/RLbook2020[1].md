# Contents

| Preface<br>to<br>the<br>Second<br>Edition<br>xiii |         |                                                     |      |  |
|---------------------------------------------------|---------|-----------------------------------------------------|------|--|
|                                                   | Preface | to<br>the<br>First<br>Edition                       | xvii |  |
|                                                   | Summary | of<br>Notation                                      | xix  |  |
| 1                                                 |         | Introduction                                        | 1    |  |
|                                                   | 1.1     | Reinforcement<br>Learning                           | 1    |  |
|                                                   | 1.2     | Examples                                            | 4    |  |
|                                                   | 1.3     | Elements<br>of<br>Reinforcement<br>Learning         | 6    |  |
|                                                   | 1.4     | Limitations<br>and<br>Scope                         | 7    |  |
|                                                   | 1.5     | An<br>Extended<br>Example:<br>Tic-Tac-Toe           | 8    |  |
|                                                   | 1.6     | Summary                                             | 13   |  |
|                                                   | 1.7     | Early<br>History<br>of<br>Reinforcement<br>Learning | 13   |  |
| I                                                 |         | Tabular<br>Solution<br>Methods                      | 23   |  |
| 2                                                 |         | Multi-armed<br>Bandits                              | 25   |  |
|                                                   | 2.1     | A<br>k-armed<br>Bandit<br>Problem                   | 25   |  |
|                                                   | 2.2     | Action-value<br>Methods                             | 27   |  |
|                                                   | 2.3     | The<br>10-armed<br>Testbed                          | 28   |  |
|                                                   | 2.4     | Incremental<br>Implementation                       | 30   |  |
|                                                   | 2.5     | Tracking<br>a<br>Nonstationary<br>Problem           | 32   |  |
|                                                   | 2.6     | Optimistic<br>Initial<br>Values                     | 34   |  |
|                                                   | 2.7     | Upper-Confidence-Bound<br>Action<br>Selection       | 35   |  |
|                                                   | 2.8     | Gradient<br>Bandit<br>Algorithms                    | 37   |  |
|                                                   | 2.9     | Associative<br>Search<br>(Contextual<br>Bandits)    | 41   |  |
|                                                   | 2.10    | Summary                                             | 42   |  |

*viii Contents*

| 3 | Finite | Markov<br>Decision<br>Processes                                      | 47  |
|---|--------|----------------------------------------------------------------------|-----|
|   | 3.1    | The<br>Agent–Environment<br>Interface                                | 47  |
|   | 3.2    | Goals<br>and<br>Rewards                                              | 53  |
|   | 3.3    | Returns<br>and<br>Episodes                                           | 54  |
|   | 3.4    | Unified<br>Notation<br>for<br>Episodic<br>and<br>Continuing<br>Tasks | 57  |
|   | 3.5    | Policies<br>and<br>Value<br>Functions                                | 58  |
|   | 3.6    | Optimal<br>Policies<br>and<br>Optimal<br>Value<br>Functions          | 62  |
|   | 3.7    | Optimality<br>and<br>Approximation                                   | 67  |
|   | 3.8    | Summary                                                              | 68  |
| 4 |        | Dynamic<br>Programming                                               | 73  |
|   | 4.1    | Policy<br>Evaluation<br>(Prediction)                                 | 74  |
|   | 4.2    | Policy<br>Improvement                                                | 76  |
|   | 4.3    | Policy<br>Iteration                                                  | 80  |
|   | 4.4    | Value<br>Iteration                                                   | 82  |
|   | 4.5    | Asynchronous<br>Dynamic<br>Programming                               | 85  |
|   | 4.6    | Generalized<br>Policy<br>Iteration                                   | 86  |
|   | 4.7    | Eciency<br>of<br>Dynamic<br>Programming                              | 87  |
|   | 4.8    | Summary                                                              | 88  |
| 5 | Monte  | Carlo<br>Methods                                                     | 91  |
|   | 5.1    | Monte<br>Carlo<br>Prediction                                         | 92  |
|   | 5.2    | Monte<br>Carlo<br>Estimation<br>of<br>Action<br>Values               | 96  |
|   | 5.3    | Monte<br>Carlo<br>Control                                            | 97  |
|   | 5.4    | Monte<br>Carlo<br>Control<br>without<br>Exploring<br>Starts          | 100 |
|   | 5.5    | O↵-policy<br>Prediction<br>via<br>Importance<br>Sampling             | 103 |
|   | 5.6    | Incremental<br>Implementation                                        | 109 |
|   | 5.7    | O↵-policy<br>Monte<br>Carlo<br>Control                               | 110 |
|   | 5.8    | *Discounting-aware<br>Importance<br>Sampling                         | 112 |
|   | 5.9    | *Per-decision<br>Importance<br>Sampling                              | 114 |
|   | 5.10   | Summary                                                              | 115 |
| 6 |        | Temporal-Di↵erence<br>Learning                                       | 119 |
|   | 6.1    | TD<br>Prediction                                                     | 119 |
|   | 6.2    | Advantages<br>of<br>TD<br>Prediction<br>Methods                      | 124 |
|   | 6.3    | Optimality<br>of<br>TD(0)                                            | 126 |
|   | 6.4    | Sarsa:<br>On-policy<br>TD<br>Control                                 | 129 |
|   | 6.5    | Q-learning:<br>O↵-policy<br>TD<br>Control                            | 131 |
|   | 6.6    | Expected<br>Sarsa                                                    | 133 |
|   | 6.7    | Maximization<br>Bias<br>and<br>Double<br>Learning                    | 134 |
|   | 6.8    | Games,<br>Afterstates,<br>and<br>Other<br>Special<br>Cases           | 136 |
|   | 6.9    | Summary                                                              | 138 |

*Contents ix*

| 7  | n-step | Bootstrapping                                                               | 141 |
|----|--------|-----------------------------------------------------------------------------|-----|
|    | 7.1    | n-step<br>TD<br>Prediction                                                  | 142 |
|    | 7.2    | n-step<br>Sarsa                                                             | 145 |
|    | 7.3    | n-step<br>O↵-policy<br>Learning                                             | 148 |
|    | 7.4    | *Per-decision<br>Methods<br>with<br>Control<br>Variates                     | 150 |
|    | 7.5    | O↵-policy<br>Learning<br>Without<br>Importance<br>Sampling:                 |     |
|    |        | The<br>n-step<br>Tree<br>Backup<br>Algorithm                                | 152 |
|    | 7.6    | *A<br>Unifying<br>Algorithm:<br>n-step<br>Q()<br>                           | 154 |
|    | 7.7    | Summary                                                                     | 157 |
| 8  |        | Planning<br>and<br>Learning<br>with<br>Tabular<br>Methods                   | 159 |
|    | 8.1    | Models<br>and<br>Planning                                                   | 159 |
|    | 8.2    | Dyna:<br>Integrated<br>Planning,<br>Acting,<br>and<br>Learning              | 161 |
|    | 8.3    | When<br>the<br>Model<br>Is<br>Wrong                                         | 166 |
|    | 8.4    | Prioritized<br>Sweeping                                                     | 168 |
|    | 8.5    | Expected<br>vs.<br>Sample<br>Updates                                        | 172 |
|    | 8.6    | Trajectory<br>Sampling                                                      | 174 |
|    | 8.7    | Real-time<br>Dynamic<br>Programming                                         | 177 |
|    | 8.8    | Planning<br>at<br>Decision<br>Time                                          | 180 |
|    | 8.9    | Heuristic<br>Search                                                         | 181 |
|    | 8.10   | Rollout<br>Algorithms                                                       | 183 |
|    | 8.11   | Monte<br>Carlo<br>Tree<br>Search                                            | 185 |
|    | 8.12   | Summary<br>of<br>the<br>Chapter                                             | 188 |
|    | 8.13   | Summary<br>of<br>Part<br>I:<br>Dimensions                                   | 189 |
|    |        |                                                                             |     |
| II |        | Approximate<br>Solution<br>Methods                                          | 195 |
| 9  |        | On-policy<br>Prediction<br>with<br>Approximation                            | 197 |
|    | 9.1    | Value-function<br>Approximation                                             | 198 |
|    | 9.2    | The<br>Prediction<br>Objective<br>(VE)                                      | 199 |
|    | 9.3    | Stochastic-gradient<br>and<br>Semi-gradient<br>Methods                      | 200 |
|    | 9.4    | Linear<br>Methods                                                           | 204 |
|    | 9.5    | Feature<br>Construction<br>for<br>Linear<br>Methods                         | 210 |
|    |        | 9.5.1<br>Polynomials                                                        | 210 |
|    |        | 9.5.2<br>Fourier<br>Basis                                                   | 211 |
|    |        | 9.5.3<br>Coarse<br>Coding                                                   | 215 |
|    |        | 9.5.4<br>Tile<br>Coding                                                     | 217 |
|    |        | 9.5.5<br>Radial<br>Basis<br>Functions                                       | 221 |
|    | 9.6    | Selecting<br>Step-Size<br>Parameters<br>Manually                            | 222 |
|    | 9.7    | Nonlinear<br>Function<br>Approximation:<br>Artificial<br>Neural<br>Networks | 223 |
|    | 9.8    | Least-Squares<br>TD                                                         | 228 |

*x Contents*

|    | 9.9   | Memory-based<br>Function<br>Approximation                                          | 230 |
|----|-------|------------------------------------------------------------------------------------|-----|
|    | 9.10  | Kernel-based<br>Function<br>Approximation                                          | 232 |
|    | 9.11  | Looking<br>Deeper<br>at<br>On-policy<br>Learning:<br>Interest<br>and<br>Emphasis   | 234 |
|    | 9.12  | Summary                                                                            | 236 |
| 10 |       | On-policy<br>Control<br>with<br>Approximation                                      | 243 |
|    | 10.1  | Episodic<br>Semi-gradient<br>Control                                               | 243 |
|    | 10.2  | Semi-gradient<br>n-step<br>Sarsa                                                   | 247 |
|    | 10.3  | Average<br>Reward:<br>A<br>New<br>Problem<br>Setting<br>for<br>Continuing<br>Tasks | 249 |
|    | 10.4  | Deprecating<br>the<br>Discounted<br>Setting                                        | 253 |
|    | 10.5  | Di↵erential<br>Semi-gradient<br>n-step<br>Sarsa                                    | 255 |
|    | 10.6  | Summary                                                                            | 256 |
| 11 |       | *O↵-policy<br>Methods<br>with<br>Approximation                                     | 257 |
|    | 11.1  | Semi-gradient<br>Methods                                                           | 258 |
|    | 11.2  | Examples<br>of<br>O↵-policy<br>Divergence                                          | 260 |
|    | 11.3  | The<br>Deadly<br>Triad                                                             | 264 |
|    | 11.4  | Linear<br>Value-function<br>Geometry                                               | 266 |
|    | 11.5  | Gradient<br>Descent<br>in<br>the<br>Bellman<br>Error                               | 269 |
|    | 11.6  | The<br>Bellman<br>Error<br>is<br>Not<br>Learnable                                  | 274 |
|    | 11.7  | Gradient-TD<br>Methods                                                             | 278 |
|    | 11.8  | Emphatic-TD<br>Methods                                                             | 281 |
|    | 11.9  | Reducing<br>Variance                                                               | 283 |
|    | 11.10 | Summary                                                                            | 284 |
| 12 |       | Eligibility<br>Traces                                                              | 287 |
|    | 12.1  | The<br>-return                                                                     | 288 |
|    | 12.2  | TD()<br>                                                                           | 292 |
|    | 12.3  | n-step<br>Truncated<br>-return<br>Methods                                          | 295 |
|    | 12.4  | Redoing<br>Updates:<br>Online<br>-return<br>Algorithm                              | 297 |
|    | 12.5  | True<br>Online<br>TD()                                                             | 299 |
|    | 12.6  | *Dutch<br>Traces<br>in<br>Monte<br>Carlo<br>Learning                               | 301 |
|    | 12.7  | Sarsa()<br>                                                                        | 303 |
|    | 12.8  | Variable<br><br>and<br><br>                                                        | 307 |
|    | 12.9  | O↵-policy<br>Traces<br>with<br>Control<br>Variates                                 | 309 |
|    | 12.10 | Watkins's<br>Q()<br>to<br>Tree-Backup()                                            | 312 |
|    | 12.11 | Stable<br>O↵-policy<br>Methods<br>with<br>Traces                                   | 314 |
|    | 12.12 | Implementation<br>Issues                                                           | 316 |
|    | 12.13 | Conclusions                                                                        | 317 |

*Contents xi*

| 13  | Policy | Gradient<br>Methods                                                                       | 321 |
|-----|--------|-------------------------------------------------------------------------------------------|-----|
|     | 13.1   | Policy<br>Approximation<br>and<br>its<br>Advantages                                       | 322 |
|     | 13.2   | The<br>Policy<br>Gradient<br>Theorem                                                      | 324 |
|     | 13.3   | REINFORCE:<br>Monte<br>Carlo<br>Policy<br>Gradient                                        | 326 |
|     | 13.4   | REINFORCE<br>with<br>Baseline                                                             | 329 |
|     | 13.5   | Actor–Critic<br>Methods                                                                   | 331 |
|     | 13.6   | Policy<br>Gradient<br>for<br>Continuing<br>Problems                                       | 333 |
|     | 13.7   | Policy<br>Parameterization<br>for<br>Continuous<br>Actions                                | 335 |
|     | 13.8   | Summary                                                                                   | 337 |
| III |        | Looking<br>Deeper                                                                         | 339 |
| 14  |        | Psychology                                                                                | 341 |
|     | 14.1   | Prediction<br>and<br>Control                                                              | 342 |
|     | 14.2   | Classical<br>Conditioning                                                                 | 343 |
|     |        | 14.2.1<br>Blocking<br>and<br>Higher-order<br>Conditioning                                 | 345 |
|     |        | 14.2.2<br>The<br>Rescorla–Wagner<br>Model                                                 | 346 |
|     |        | 14.2.3<br>The<br>TD<br>Model                                                              | 349 |
|     |        | 14.2.4<br>TD<br>Model<br>Simulations                                                      | 350 |
|     | 14.3   | Instrumental<br>Conditioning                                                              | 357 |
|     | 14.4   | Delayed<br>Reinforcement                                                                  | 361 |
|     | 14.5   | Cognitive<br>Maps                                                                         | 363 |
|     | 14.6   | Habitual<br>and<br>Goal-directed<br>Behavior                                              | 364 |
|     | 14.7   | Summary                                                                                   | 368 |
| 15  |        | Neuroscience                                                                              | 377 |
|     | 15.1   | Neuroscience<br>Basics                                                                    | 378 |
|     | 15.2   | Reward<br>Signals,<br>Reinforcement<br>Signals,<br>Values,<br>and<br>Prediction<br>Errors | 380 |
|     | 15.3   | The<br>Reward<br>Prediction<br>Error<br>Hypothesis                                        | 381 |
|     | 15.4   | Dopamine                                                                                  | 383 |
|     | 15.5   | Experimental<br>Support<br>for<br>the<br>Reward<br>Prediction<br>Error<br>Hypothesis      | 387 |
|     | 15.6   | TD<br>Error/Dopamine<br>Correspondence                                                    | 390 |
|     | 15.7   | Neural<br>Actor–Critic                                                                    | 395 |
|     | 15.8   | Actor<br>and<br>Critic<br>Learning<br>Rules                                               | 398 |
|     | 15.9   | Hedonistic<br>Neurons                                                                     | 402 |
|     | 15.10  | Collective<br>Reinforcement<br>Learning                                                   | 404 |
|     | 15.11  | Model-based<br>Methods<br>in<br>the<br>Brain                                              | 407 |
|     | 15.12  | Addiction                                                                                 | 409 |
|     | 15.13  | Summary                                                                                   | 410 |

*xii Contents*

| 16<br>Applications<br>and<br>Case<br>Studies                                                  | 421 |
|-----------------------------------------------------------------------------------------------|-----|
| 16.1<br>TD-Gammon                                                                             | 421 |
| 16.2<br>Samuel's<br>Checkers<br>Player                                                        | 426 |
| 16.3<br>Watson's<br>Daily-Double<br>Wagering                                                  | 429 |
| 16.4<br>Optimizing<br>Memory<br>Control                                                       | 432 |
| 16.5<br>Human-level<br>Video<br>Game<br>Play                                                  | 436 |
| 16.6<br>Mastering<br>the<br>Game<br>of<br>Go                                                  | 441 |
| 16.6.1<br>AlphaGo                                                                             | 444 |
| 16.6.2<br>AlphaGo<br>Zero                                                                     | 447 |
| 16.7<br>Personalized<br>Web<br>Services                                                       | 450 |
| 16.8<br>Thermal<br>Soaring                                                                    | 453 |
| 17<br>Frontiers                                                                               | 459 |
| 17.1<br>General<br>Value<br>Functions<br>and<br>Auxiliary<br>Tasks                            | 459 |
| 17.2<br>Temporal<br>Abstraction<br>via<br>Options                                             | 461 |
| 17.3<br>Observations<br>and<br>State                                                          | 464 |
| 17.4<br>Designing<br>Reward<br>Signals                                                        | 469 |
| 17.5<br>Remaining<br>Issues                                                                   | 472 |
| 17.6<br>Reinforcement<br>Learning<br>and<br>the<br>Future<br>of<br>Artificial<br>Intelligence | 475 |
| References                                                                                    | 481 |
| Index                                                                                         | 519 |

# <span id="page-6-0"></span>Summary of Notation

*.*

Capital letters are used for random variables, whereas lower case letters are used for the values of random variables and for scalar functions. Quantities that are required to be real-valued vectors are written in bold and in lower case (even if random variables). Matrices are bold capitals.

```
= equality relationship that is true by definition
⇡ approximately equal
/ proportional to
Pr{X =x} probability that a random variable X takes on the value x
X ⇠ p random variable X selected from distribution p(x) .
                                                        = Pr{X =x}
E[X] expectation of a random variable X, i.e., E[X] .
                                                    = P
                                                        x p(x)x
argmaxa f(a) a value of a at which f(a) takes its maximal value
ln x natural logarithm of x
ex, exp(x) the base of the natural logarithm, e ⇡ 2.71828, carried to power x; eln x = x
R set of real numbers
f : X ! Y function f from elements of set X to elements of set Y
 assignment
(a, b] the real interval between a and b including b but not including a
" probability of taking a random action in an "-greedy policy
↵,  step-size parameters
 discount-rate parameter
 decay-rate parameter for eligibility traces
 predicate indicator function ( predicate
                                     .
                                     = 1 if the predicate is true, else 0)
In a multi-arm bandit problem:
k number of actions (arms)
t discrete time step or play number
q⇤(a) true value (expected reward) of action a
Qt(a) estimate at time t of q⇤(a)
Nt(a) number of times action a has been selected up prior to time t
Ht(a) learned preference for selecting action a at time t
⇡t(a) probability of selecting action a at time t
R¯t estimate at time t of the expected reward given ⇡t
```

```
In a Markov Decision Process:
s, s0 states
a an action
r a reward
S set of all nonterminal states
S+ set of all states, including the terminal state
A(s) set of all actions available in state s
R set of all possible rewards, a finite subset of R
⇢ subset of (e.g., R ⇢ R)
2 is an element of; e.g. (s 2 S, r 2 R)
|S| number of elements in set S
t discrete time step
T,T(t) final time step of an episode, or of the episode including time step t
At action at time t
St state at time t, typically due, stochastically, to St1 and At1
Rt reward at time t, typically due, stochastically, to St1 and At1
⇡ policy (decision-making rule)
⇡(s) action taken in state s under deterministic policy ⇡
⇡(a|s) probability of taking action a in state s under stochastic policy ⇡
Gt return following time t
h horizon, the time step one looks up to in a forward view
Gt:t+n, Gt:h n-step return from t + 1 to t + n, or to h (discounted and corrected)
G¯t:h flat return (undiscounted and uncorrected) from t + 1 to h (Section 5.8)
G
 t -return (Section 12.1)
G
 t:h truncated, corrected -return (Section 12.3)
Gs
 t , Ga
     t -return, corrected by estimated state, or action, values (Section 12.8)
p(s0
   , r|s, a) probability of transition to state s0 with reward r, from state s and action a
p(s0 |s, a) probability of transition to state s0
                                           , from state s taking action a
r(s, a) expected immediate reward from state s after action a
r(s, a, s0
       ) expected immediate reward on transition from s to s0 under action a
v⇡(s) value of state s under policy ⇡ (expected return)
v⇤(s) value of state s under the optimal policy
q⇡(s, a) value of taking action a in state s under policy ⇡
q⇤(s, a) value of taking action a in state s under the optimal policy
V,Vt array estimates of state-value function v⇡ or v⇤
Q, Qt array estimates of action-value function q⇡ or q⇤
V¯t(s) expected approximate action value; for example, V¯t(s) .
                                                            = P
                                                                a ⇡(a|s)Qt(s, a)
Ut target for estimate at time t
```

```
t temporal-di↵erence (TD) error at t (a random variable) (Section 6.1)
s
t , a
   t state- and action-specific forms of the TD error (Section 12.9)
n in n-step methods, n is the number of steps of bootstrapping
d dimensionality—the number of components of w
d0 alternate dimensionality—the number of components of ✓
w, wt d-vector of weights underlying an approximate value function
wi, wt,i ith component of learnable weight vector
vˆ(s,w) approximate value of state s given weight vector w
vw(s) alternate notation for ˆv(s,w)
qˆ(s, a, w) approximate value of state–action pair s, a given weight vector w
rvˆ(s,w) column vector of partial derivatives of ˆv(s,w) with respect to w
rqˆ(s, a, w) column vector of partial derivatives of ˆq(s, a, w) with respect to w
x(s) vector of features visible when in state s
x(s, a) vector of features visible when in state s taking action a
xi(s), xi(s, a) ith component of vector x(s) or x(s, a)
xt shorthand for x(St) or x(St, At)
w>x inner product of vectors, w>x .
                                        = P
                                            i wixi; for example, ˆv(s,w) .
                                                                     = w>x(s)
v, vt secondary d-vector of weights, used to learn w (Chapter 11)
zt d-vector of eligibility traces at time t (Chapter 12)
✓, ✓t parameter vector of target policy (Chapter 13)
⇡(a|s, ✓) probability of taking action a in state s given parameter vector ✓
⇡✓ policy corresponding to parameter ✓
r⇡(a|s, ✓) column vector of partial derivatives of ⇡(a|s, ✓) with respect to ✓
J(✓) performance measure for the policy ⇡✓
rJ(✓) column vector of partial derivatives of J(✓) with respect to ✓
h(s, a, ✓) preference for selecting action a in state s based on ✓
b(a|s) behavior policy used to select actions while learning about target policy ⇡
b(s) a baseline function b : S 7! R for policy-gradient methods
b branching factor for an MDP or search tree
⇢t:h importance sampling ratio for time t through time h (Section 5.5)
⇢t importance sampling ratio for time t alone, ⇢t
                                                      .
                                                      = ⇢t:t
r(⇡) average reward (reward rate) for policy ⇡ (Section 10.3)
R¯t estimate of r(⇡) at time t
µ(s) on-policy distribution over states (Section 9.2)
µ |S|-vector of the µ(s) for all s 2 S
kvk
   2
   µ µ-weighted squared norm of value function v, i.e., kvk
                                                            2
                                                            µ
                                                               .
                                                              = P
                                                                  s2S µ(s)v(s)2
⌘(s) expected number of visits to state s per episode (page 199)
⇧ projection operator for value functions (page 268)
B⇡ Bellman operator for value functions (Section 11.4)
```

```
A d ⇥ d matrix A .
                           = E
                               h
                               xt

                                  xt  xt+1>i
b d-dimensional vector b .
                                  = E[Rt+1xt]
wTD TD fixed point wTD
                               = A1b (a d-vector, Section 9.4)
I identity matrix
P |S| ⇥ |S| matrix of state-transition probabilities under ⇡
D |S| ⇥ |S| diagonal matrix with µ on its diagonal
X |S| ⇥ d matrix with the x(s) as its rows
¯w(s) Bellman error (expected TD error) for vw at state s (Section 11.4) ¯w, BE Bellman error vector, with components ¯w(s)
VE(w) mean square value error VE(w) .
                                          = kvw  v⇡k
                                                     2
                                                     µ (Section 9.2)
BE(w) mean square Bellman error BE(w) .
                                            = 
                                               ¯w

                                                   2
                                                   µ
PBE(w) mean square projected Bellman error PBE(w) .
                                                       = 
                                                         ⇧¯w

                                                               2
                                                               µ
TDE(w) mean square temporal-di↵erence error TDE(w) .
                                                        = Eb
                                                            ⇥
                                                             ⇢t2
                                                                t
                                                                 ⇤
                                                                  (Section 11.5)
```

RE(w) mean square return error (Section 11.6)

## <span id="page-10-0"></span>Chapter 1

# Introduction

The idea that we learn by interacting with our environment is probably the first to occur to us when we think about the nature of learning. When an infant plays, waves its arms, or looks about, it has no explicit teacher, but it does have a direct sensorimotor connection to its environment. Exercising this connection produces a wealth of information about cause and e↵ect, about the consequences of actions, and about what to do in order to achieve goals. Throughout our lives, such interactions are undoubtedly a major source of knowledge about our environment and ourselves. Whether we are learning to drive a car or to hold a conversation, we are acutely aware of how our environment responds to what we do, and we seek to influence what happens through our behavior. Learning from interaction is a foundational idea underlying nearly all theories of learning and intelligence.

In this book we explore a *computational* approach to learning from interaction. Rather than directly theorizing about how people or animals learn, we primarily explore idealized learning situations and evaluate the e↵ectiveness of various learning methods. That is, we adopt the perspective of an artificial intelligence researcher or engineer. We explore designs for machines that are e↵ective in solving learning problems of scientific or economic interest, evaluating the designs through mathematical analysis or computational experiments. The approach we explore, called *reinforcement learning*, is much more focused on goal-directed learning from interaction than are other approaches to machine learning.

#### <span id="page-10-1"></span>1.1 Reinforcement Learning

Reinforcement learning is learning what to do—how to map situations to actions—so as to maximize a numerical reward signal. The learner is not told which actions to take, but instead must discover which actions yield the most reward by trying them. In the most interesting and challenging cases, actions may a↵ect not only the immediate reward but also the next situation and, through that, all subsequent rewards. These two characteristics—trial-and-error search and delayed reward—are the two most important distinguishing features of reinforcement learning.

Reinforcement learning, like many topics whose names end with "ing," such as machine learning and mountaineering, is simultaneously a problem, a class of solution methods that work well on the problem, and the field that studies this problem and its solution methods. It is convenient to use a single name for all three things, but at the same time essential to keep the three conceptually separate. In particular, the distinction between problems and solution methods is very important in reinforcement learning; failing to make this distinction is the source of many confusions.

We formalize the problem of reinforcement learning using ideas from dynamical systems theory, specifically, as the optimal control of incompletely-known Markov decision processes. The details of this formalization must wait until [Chapter 3,](#page-33-0) but the basic idea is simply to capture the most important aspects of the real problem facing a learning agent interacting over time with its environment to achieve a goal. A learning agent must be able to sense the state of its environment to some extent and must be able to take actions that a↵ect the state. The agent also must have a goal or goals relating to the state of the environment. Markov decision processes are intended to include just these three aspects—sensation, action, and goal—in their simplest possible forms without trivializing any of them. Any method that is well suited to solving such problems we consider to be a reinforcement learning method.

Reinforcement learning is di↵erent from *supervised learning*, the kind of learning studied in most current research in the field of machine learning. Supervised learning is learning from a training set of labeled examples provided by a knowledgable external supervisor. Each example is a description of a situation together with a specification—the label—of the correct action the system should take in that situation, which is often to identify a category to which the situation belongs. The object of this kind of learning is for the system to extrapolate, or generalize, its responses so that it acts correctly in situations not present in the training set. This is an important kind of learning, but alone it is not adequate for learning from interaction. In interactive problems it is often impractical to obtain examples of desired behavior that are both correct and representative of all the situations in which the agent has to act. In uncharted territory—where one would expect learning to be most beneficial—an agent must be able to learn from its own experience.

Reinforcement learning is also di↵erent from what machine learning researchers call *unsupervised learning*, which is typically about finding structure hidden in collections of unlabeled data. The terms supervised learning and unsupervised learning would seem to exhaustively classify machine learning paradigms, but they do not. Although one might be tempted to think of reinforcement learning as a kind of unsupervised learning because it does not rely on examples of correct behavior, reinforcement learning is trying to maximize a reward signal instead of trying to find hidden structure. Uncovering structure in an agent's experience can certainly be useful in reinforcement learning, but by itself does not address the reinforcement learning problem of maximizing a reward signal. We therefore consider reinforcement learning to be a third machine learning paradigm, alongside supervised learning and unsupervised learning and perhaps other paradigms.

One of the challenges that arise in reinforcement learning, and not in other kinds of learning, is the trade-o↵ between exploration and exploitation. To obtain a lot of reward, a reinforcement learning agent must prefer actions that it has tried in the past and found to be e↵ective in producing reward. But to discover such actions, it has to try actions that it has not selected before. The agent has to *exploit* what it has already experienced in order to obtain reward, but it also has to *explore* in order to make better action selections in the future. The dilemma is that neither exploration nor exploitation can be pursued exclusively without failing at the task. The agent must try a variety of actions *and* progressively favor those that appear to be best. On a stochastic task, each action must be tried many times to gain a reliable estimate of its expected reward. The exploration–exploitation dilemma has been intensively studied by mathematicians for many decades, yet remains unresolved. For now, we simply note that the entire issue of balancing exploration and exploitation does not even arise in supervised and unsupervised learning, at least in the purest forms of these paradigms.

Another key feature of reinforcement learning is that it explicitly considers the *whole* problem of a goal-directed agent interacting with an uncertain environment. This is in contrast to many approaches that consider subproblems without addressing how they might fit into a larger picture. For example, we have mentioned that many machine learning researchers have studied supervised learning without specifying how such an ability would ultimately be useful. Other researchers have developed theories of planning with general goals, but without considering planning's role in real-time decision making, or the question of where the predictive models necessary for planning would come from. Although these approaches have yielded many useful results, their focus on isolated subproblems is a significant limitation.

Reinforcement learning takes the opposite tack, starting with a complete, interactive, goal-seeking agent. All reinforcement learning agents have explicit goals, can sense aspects of their environments, and can choose actions to influence their environments. Moreover, it is usually assumed from the beginning that the agent has to operate despite significant uncertainty about the environment it faces. When reinforcement learning involves planning, it has to address the interplay between planning and real-time action selection, as well as the question of how environment models are acquired and improved. When reinforcement learning involves supervised learning, it does so for specific reasons that determine which capabilities are critical and which are not. For learning research to make progress, important subproblems have to be isolated and studied, but they should be subproblems that play clear roles in complete, interactive, goal-seeking agents, even if all the details of the complete agent cannot yet be filled in.

By a complete, interactive, goal-seeking agent we do not always mean something like a complete organism or robot. These are clearly examples, but a complete, interactive, goal-seeking agent can also be a component of a larger behaving system. In this case, the agent directly interacts with the rest of the larger system and indirectly interacts with the larger system's environment. A simple example is an agent that monitors the charge level of robot's battery and sends commands to the robot's control architecture. This agent's environment is the rest of the robot together with the robot's environment. It is

important to look beyond the most obvious examples of agents and their environments to appreciate the generality of the reinforcement learning framework.

One of the most exciting aspects of modern reinforcement learning is its substantive and fruitful interactions with other engineering and scientific disciplines. Reinforcement learning is part of a decades-long trend within artificial intelligence and machine learning toward greater integration with statistics, optimization, and other mathematical subjects. For example, the ability of some reinforcement learning methods to learn with parameterized approximators addresses the classical "curse of dimensionality" in operations research and control theory. More distinctively, reinforcement learning has also interacted strongly with psychology and neuroscience, with substantial benefits going both ways. Of all the forms of machine learning, reinforcement learning is the closest to the kind of learning that humans and other animals do, and many of the core algorithms of reinforcement learning were originally inspired by biological learning systems. Reinforcement learning has also given back, both through a psychological model of animal learning that better matches some of the empirical data, and through an influential model of parts of the brain's reward system. The body of this book develops the ideas of reinforcement learning that pertain to engineering and artificial intelligence, with connections to psychology and neuroscience summarized in Chapters 14 and 15.

Finally, reinforcement learning is also part of a larger trend in artificial intelligence back toward simple general principles. Since the late 1960s, many artificial intelligence researchers presumed that there are no general principles to be discovered, that intelligence is instead due to the possession of a vast number of special purpose tricks, procedures, and heuristics. It was sometimes said that if we could just get enough relevant facts into a machine, say one million, or one billion, then it would become intelligent. Methods based on general principles, such as search or learning, were characterized as "weak methods," whereas those based on specific knowledge were called "strong methods." This view is uncommon today. From our point of view, it was premature: too little e↵ort had been put into the search for general principles to conclude that there were none. Modern artificial intelligence now includes much research looking for general principles of learning, search, and decision making. It is not clear how far back the pendulum will swing, but reinforcement learning research is certainly part of the swing back toward simpler and fewer general principles of artificial intelligence.

#### <span id="page-13-0"></span>1.2 Examples

A good way to understand reinforcement learning is to consider some of the examples and possible applications that have guided its development.

- A master chess player makes a move. The choice is informed both by planning anticipating possible replies and counterreplies—and by immediate, intuitive judgments of the desirability of particular positions and moves.
- An adaptive controller adjusts parameters of a petroleum refinery's operation in real time. The controller optimizes the yield/cost/quality trade-o↵ on the basis

*1.2. Examples 5*

of specified marginal costs without sticking strictly to the set points originally suggested by engineers.

- A gazelle calf struggles to its feet minutes after being born. Half an hour later it is running at 20 miles per hour.
- A mobile robot decides whether it should enter a new room in search of more trash to collect or start trying to find its way back to its battery recharging station. It makes its decision based on the current charge level of its battery and how quickly and easily it has been able to find the recharger in the past.
- Phil prepares his breakfast. Closely examined, even this apparently mundane activity reveals a complex web of conditional behavior and interlocking goal–subgoal relationships: walking to the cupboard, opening it, selecting a cereal box, then reaching for, grasping, and retrieving the box. Other complex, tuned, interactive sequences of behavior are required to obtain a bowl, spoon, and milk carton. Each step involves a series of eye movements to obtain information and to guide reaching and locomotion. Rapid judgments are continually made about how to carry the objects or whether it is better to ferry some of them to the dining table before obtaining others. Each step is guided by goals, such as grasping a spoon or getting to the refrigerator, and is in service of other goals, such as having the spoon to eat with once the cereal is prepared and ultimately obtaining nourishment. Whether he is aware of it or not, Phil is accessing information about the state of his body that determines his nutritional needs, level of hunger, and food preferences.

These examples share features that are so basic that they are easy to overlook. All involve *interaction* between an active decision-making agent and its environment, within which the agent seeks to achieve a *goal* despite *uncertainty* about its environment. The agent's actions are permitted to a↵ect the future state of the environment (e.g., the next chess position, the level of reservoirs of the refinery, the robot's next location and the future charge level of its battery), thereby a↵ecting the actions and opportunities available to the agent at later times. Correct choice requires taking into account indirect, delayed consequences of actions, and thus may require foresight or planning.

At the same time, in all of these examples the e↵ects of actions cannot be fully predicted; thus the agent must monitor its environment frequently and react appropriately. For example, Phil must watch the milk he pours into his cereal bowl to keep it from overflowing. All these examples involve goals that are explicit in the sense that the agent can judge progress toward its goal based on what it can sense directly. The chess player knows whether or not he wins, the refinery controller knows how much petroleum is being produced, the gazelle calf knows when it falls, the mobile robot knows when its batteries run down, and Phil knows whether or not he is enjoying his breakfast.

In all of these examples the agent can use its experience to improve its performance over time. The chess player refines the intuition he uses to evaluate positions, thereby improving his play; the gazelle calf improves the eciency with which it can run; Phil learns to streamline making his breakfast. The knowledge the agent brings to the task at the start—either from previous experience with related tasks or built into it by design or

evolution—influences what is useful or easy to learn, but interaction with the environment is essential for adjusting behavior to exploit specific features of the task.

#### <span id="page-15-0"></span>1.3 Elements of Reinforcement Learning

Beyond the agent and the environment, one can identify four main subelements of a reinforcement learning system: a *policy*, a *reward signal*, a *value function*, and, optionally, a *model* of the environment.

A *policy* defines the learning agent's way of behaving at a given time. Roughly speaking, a policy is a mapping from perceived states of the environment to actions to be taken when in those states. It corresponds to what in psychology would be called a set of stimulus–response rules or associations. In some cases the policy may be a simple function or lookup table, whereas in others it may involve extensive computation such as a search process. The policy is the core of a reinforcement learning agent in the sense that it alone is sucient to determine behavior. In general, policies may be stochastic, specifying probabilities for each action.

A *reward signal* defines the goal of a reinforcement learning problem. On each time step, the environment sends to the reinforcement learning agent a single number called the *reward*. The agent's sole objective is to maximize the total reward it receives over the long run. The reward signal thus defines what are the good and bad events for the agent. In a biological system, we might think of rewards as analogous to the experiences of pleasure or pain. They are the immediate and defining features of the problem faced by the agent. The reward signal is the primary basis for altering the policy; if an action selected by the policy is followed by low reward, then the policy may be changed to select some other action in that situation in the future. In general, reward signals may be stochastic functions of the state of the environment and the actions taken.

Whereas the reward signal indicates what is good in an immediate sense, a *value function* specifies what is good in the long run. Roughly speaking, the *value* of a state is the total amount of reward an agent can expect to accumulate over the future, starting from that state. Whereas rewards determine the immediate, intrinsic desirability of environmental states, values indicate the *long-term* desirability of states after taking into account the states that are likely to follow and the rewards available in those states. For example, a state might always yield a low immediate reward but still have a high value because it is regularly followed by other states that yield high rewards. Or the reverse could be true. To make a human analogy, rewards are somewhat like pleasure (if high) and pain (if low), whereas values correspond to a more refined and farsighted judgment of how pleased or displeased we are that our environment is in a particular state.

Rewards are in a sense primary, whereas values, as predictions of rewards, are secondary. Without rewards there could be no values, and the only purpose of estimating values is to achieve more reward. Nevertheless, it is values with which we are most concerned when making and evaluating decisions. Action choices are made based on value judgments. We seek actions that bring about states of highest value, not highest reward, because these actions obtain the greatest amount of reward for us over the long run. Unfortunately, it is much harder to determine values than it is to determine rewards. Rewards are basically given directly by the environment, but values must be estimated and re-estimated from

the sequences of observations an agent makes over its entire lifetime. In fact, the most important component of almost all reinforcement learning algorithms we consider is a method for eciently estimating values. The central role of value estimation is arguably the most important thing that has been learned about reinforcement learning over the last six decades.

The fourth and final element of some reinforcement learning systems is a *model* of the environment. This is something that mimics the behavior of the environment, or more generally, that allows inferences to be made about how the environment will behave. For example, given a state and action, the model might predict the resultant next state and next reward. Models are used for *planning*, by which we mean any way of deciding on a course of action by considering possible future situations before they are actually experienced. Methods for solving reinforcement learning problems that use models and planning are called *model-based* methods, as opposed to simpler *model-free* methods that are explicitly trial-and-error learners—viewed as almost the *opposite* of planning. In Chapter 8 we explore reinforcement learning systems that simultaneously learn by trial and error, learn a model of the environment, and use the model for planning. Modern reinforcement learning spans the spectrum from low-level, trial-and-error learning to high-level, deliberative planning.

### <span id="page-16-0"></span>1.4 Limitations and Scope

Reinforcement learning relies heavily on the concept of state—as input to the policy and value function, and as both input to and output from the model. Informally, we can think of the state as a signal conveying to the agent some sense of "how the environment is" at a particular time. The formal definition of state as we use it here is given by the framework of Markov decision processes presented in [Chapter 3.](#page-33-0) More generally, however, we encourage the reader to follow the informal meaning and think of the state as whatever information is available to the agent about its environment. In e↵ect, we assume that the state signal is produced by some preprocessing system that is nominally part of the agent's environment. We do not address the issues of constructing, changing, or learning the state signal in this book (other than briefly in Section 17.3). We take this approach not because we consider state representation to be unimportant, but in order to focus fully on the decision-making issues. In other words, our concern in this book is not with designing the state signal, but with deciding what action to take as a function of whatever state signal is available.

Most of the reinforcement learning methods we consider in this book are structured around estimating value functions, but it is not strictly necessary to do this to solve reinforcement learning problems. For example, solution methods such as genetic algorithms, genetic programming, simulated annealing, and other optimization methods never estimate value functions. These methods apply multiple static policies each interacting over an extended period of time with a separate instance of the environment. The policies that obtain the most reward, and random variations of them, are carried over to the next generation of policies, and the process repeats. We call these *evolutionary* methods because their operation is analogous to the way biological evolution produces organisms

with skilled behavior even if they do not learn during their individual lifetimes. If the space of policies is suciently small, or can be structured so that good policies are common or easy to find—or if a lot of time is available for the search—then evolutionary methods can be e↵ective. In addition, evolutionary methods have advantages on problems in which the learning agent cannot sense the complete state of its environment.

Our focus is on reinforcement learning methods that learn while interacting with the environment, which evolutionary methods do not do. Methods able to take advantage of the details of individual behavioral interactions can be much more ecient than evolutionary methods in many cases. Evolutionary methods ignore much of the useful structure of the reinforcement learning problem: they do not use the fact that the policy they are searching for is a function from states to actions; they do not notice which states an individual passes through during its lifetime, or which actions it selects. In some cases such information can be misleading (e.g., when states are misperceived), but more often it should enable more ecient search. Although evolution and learning share many features and naturally work together, we do not consider evolutionary methods by themselves to be especially well suited to reinforcement learning problems and, accordingly, we do not cover them in this book.

### <span id="page-17-0"></span>1.5 An Extended Example: Tic-Tac-Toe

To illustrate the general idea of reinforcement learning and contrast it with other approaches, we next consider a single example in more detail.

Consider the familiar child's game of tic-tac-toe. Two players take turns playing on a three-by-three board. One player plays Xs and the other Os until one player wins by placing three marks in a row, horizontally, vertically, or diagonally, as the X player has in the game shown to the right. If the board fills up with neither player getting three in a row, then the game is a draw. Because a skilled player can play so as never to lose, let us assume that we are playing against an imperfect player, one whose play is sometimes incorrect and allows us to win. For the moment, in

| X | O | O |
|---|---|---|
| O | X | X |
|   |   | X |

fact, let us consider draws and losses to be equally bad for us. How might we construct a player that will find the imperfections in its opponent's play and learn to maximize its chances of winning?

Although this is a simple problem, it cannot readily be solved in a satisfactory way through classical techniques. For example, the classical "minimax" solution from game theory is not correct here because it assumes a particular way of playing by the opponent. For example, a minimax player would never reach a game state from which it could lose, even if in fact it always won from that state because of incorrect play by the opponent. Classical optimization methods for sequential decision problems, such as dynamic programming, can *compute* an optimal solution for any opponent, but require as input a complete specification of that opponent, including the probabilities with which the opponent makes each move in each board state. Let us assume that this information is not available a priori for this problem, as it is not for the vast majority of problems of

practical interest. On the other hand, such information can be estimated from experience, in this case by playing many games against the opponent. About the best one can do on this problem is first to learn a model of the opponent's behavior, up to some level of confidence, and then apply dynamic programming to compute an optimal solution given the approximate opponent model. In the end, this is not that di↵erent from some of the reinforcement learning methods we examine later in this book.

An evolutionary method applied to this problem would directly search the space of possible policies for one with a high probability of winning against the opponent. Here, a policy is a rule that tells the player what move to make for every state of the game—every possible configuration of Xs and Os on the three-by-three board. For each policy considered, an estimate of its winning probability would be obtained by playing some number of games against the opponent. This evaluation would then direct which policy or policies were considered next. A typical evolutionary method would hill-climb in policy space, successively generating and evaluating policies in an attempt to obtain incremental improvements. Or, perhaps, a genetic-style algorithm could be used that would maintain and evaluate a population of policies. Literally hundreds of di↵erent optimization methods could be applied.

Here is how the tic-tac-toe problem would be approached with a method making use of a value function. First we would set up a table of numbers, one for each possible state of the game. Each number will be the latest estimate of the probability of our winning from that state. We treat this estimate as the state's *value*, and the whole table is the learned value function. State A has higher value than state B, or is considered "better" than state B, if the current estimate of the probability of our winning from A is higher than it is from B. Assuming we always play Xs, then for all states with three Xs in a row the probability of winning is 1, because we have already won. Similarly, for all states with three Os in a row, or that are filled up, the correct probability is 0, as we cannot win from them. We set the initial values of all the other states to 0.5, representing a guess that we have a 50% chance of winning.

We then play many games against the opponent. To select our moves we examine the states that would result from each of our possible moves (one for each blank space on the board) and look up their current values in the table. Most of the time we move *greedily*, selecting the move that leads to the state with greatest value, that is, with the highest estimated probability of winning. Occasionally, however, we select randomly from among the other moves instead. These are called *exploratory* moves because they cause us to experience states that we might otherwise never see. A sequence of moves made and considered during a game can be diagrammed as in [Figure 1.1.](#page-19-0)

While we are playing, we change the values of the states in which we find ourselves during the game. We attempt to make them more accurate estimates of the probabilities of winning. To do this, we "back up" the value of the state after each greedy move to the state before the move, as suggested by the arrows in [Figure 1.1.](#page-19-0) More precisely, the current value of the earlier state is updated to be closer to the value of the later state. This can be done by moving the earlier state's value a fraction of the way toward the value of the later state. If we let *S<sup>t</sup>* denote the state before the greedy move, and *St*+1 the state after that move, then the update to the estimated value of *St*, denoted *V* (*St*),

<span id="page-19-0"></span>![](_page_19_Figure_2.jpeg)

Figure 1.1: A sequence of tic-tac-toe moves. The solid black lines represent the moves taken during a game; the dashed lines represent moves that we (our reinforcement learning player) considered but did not make. The \* indicates the move currently estimated to be the best. Our second move was an exploratory move, meaning that it was taken even though another sibling move, the one leading to e⇤, was ranked higher. Exploratory moves do not result in any learning, but each of our other moves does, causing updates as suggested by the red arrows in which estimated values are moved up the tree from later nodes to earlier nodes as detailed in the text.

can be written as

$$V(S_t) \leftarrow V(S_t) + \alpha \Big[ V(S_{t+1}) - V(S_t) \Big],$$

where ↵ is a small positive fraction called the *step-size parameter*, which influences the rate of learning. This update rule is an example of a *temporal-di*↵*erence* learning method, so called because its changes are based on a di↵erence, *V* (*St*+1)*V* (*St*), between estimates at two successive times.

The method described above performs quite well on this task. For example, if the step-size parameter is reduced properly over time, then this method converges, for any fixed opponent, to the true probabilities of winning from each state given optimal play by our player. Furthermore, the moves then taken (except on exploratory moves) are in fact the optimal moves against this (imperfect) opponent. In other words, the method converges to an optimal policy for playing the game against this opponent. If the step-size parameter is not reduced all the way to zero over time, then this player also plays well against opponents that slowly change their way of playing.

This example illustrates the di↵erences between evolutionary methods and methods that learn value functions. To evaluate a policy, an evolutionary method holds the policy fixed and plays many games against the opponent or simulates many games using a model of the opponent. The frequency of wins gives an unbiased estimate of the probability of winning with that policy, and can be used to direct the next policy selection. But each policy change is made only after many games, and only the final outcome of each game is used: what happens *during* the games is ignored. For example, if the player wins, then *all* of its behavior in the game is given credit, independently of how specific moves might have been critical to the win. Credit is even given to moves that never occurred! Value function methods, in contrast, allow individual states to be evaluated. In the end, evolutionary and value function methods both search the space of policies, but learning a value function takes advantage of information available during the course of play.

This simple example illustrates some of the key features of reinforcement learning methods. First, there is the emphasis on learning while interacting with an environment, in this case with an opponent player. Second, there is a clear goal, and correct behavior requires planning or foresight that takes into account delayed e↵ects of one's choices. For example, the simple reinforcement learning player would learn to set up multi-move traps for a shortsighted opponent. It is a striking feature of the reinforcement learning solution that it can achieve the e↵ects of planning and lookahead without using a model of the opponent and without conducting an explicit search over possible sequences of future states and actions.

While this example illustrates some of the key features of reinforcement learning, it is so simple that it might give the impression that reinforcement learning is more limited than it really is. Although tic-tac-toe is a two-person game, reinforcement learning also applies in the case in which there is no external adversary, that is, in the case of a "game against nature." Reinforcement learning also is not restricted to problems in which behavior breaks down into separate episodes, like the separate games of tic-tac-toe, with reward only at the end of each episode. It is just as applicable when behavior continues indefinitely and when rewards of various magnitudes can be received at any time. Reinforcement learning is also applicable to problems that do not even break down into discrete time steps like the plays of tic-tac-toe. The general principles apply to continuous-time problems as well, although the theory gets more complicated and we omit it from this introductory treatment.

Tic-tac-toe has a relatively small, finite state set, whereas reinforcement learning can be used when the state set is very large, or even infinite. For example, Gerry Tesauro (1992, 1995) combined the algorithm described above with an artificial neural network to learn to play backgammon, which has approximately 10<sup>20</sup> states. With this many states it is impossible ever to experience more than a small fraction of them. Tesauro's program learned to play far better than any previous program and eventually better than the world's best human players (see Section 16.1). The artificial neural network provides the program with the ability to generalize from its experience, so that in new states it selects moves based on information saved from similar states faced in the past, as determined by the network. How well a reinforcement learning system can work in problems with such large state sets is intimately tied to how appropriately it can generalize from past

experience. It is in this role that we have the greatest need for supervised learning methods within reinforcement learning. Artificial neural networks and deep learning (Section 9.7) are not the only, or necessarily the best, way to do this.

In this tic-tac-toe example, learning started with no prior knowledge beyond the rules of the game, but reinforcement learning by no means entails a tabula rasa view of learning and intelligence. On the contrary, prior information can be incorporated into reinforcement learning in a variety of ways that can be critical for ecient learning (e.g., see Sections 9.5, 17.4, and [13.1\)](#page-60-0). We also have access to the true state in the tic-tac-toe example, whereas reinforcement learning can also be applied when part of the state is hidden, or when di↵erent states appear to the learner to be the same.

Finally, the tic-tac-toe player was able to look ahead and know the states that would result from each of its possible moves. To do this, it had to have a model of the game that allowed it to foresee how its environment would change in response to moves that it might never make. Many problems are like this, but in others even a short-term model of the e↵ects of actions is lacking. Reinforcement learning can be applied in either case. A model is not required, but models can easily be used if they are available or can be learned (Chapter 8).

On the other hand, there are reinforcement learning methods that do not need any kind of environment model at all. Model-free systems cannot even think about how their environments will change in response to a single action. The tic-tac-toe player is model-free in this sense with respect to its opponent: it has no model of its opponent of any kind. Because models have to be reasonably accurate to be useful, model-free methods can have advantages over more complex methods when the real bottleneck in solving a problem is the diculty of constructing a suciently accurate environment model. Model-free methods are also important building blocks for model-based methods. In this book we devote several chapters to model-free methods before we discuss how they can be used as components of more complex model-based methods.

Reinforcement learning can be used at both high and low levels in a system. Although the tic-tac-toe player learned only about the basic moves of the game, nothing prevents reinforcement learning from working at higher levels where each of the "actions" may itself be the application of a possibly elaborate problem-solving method. In hierarchical learning systems, reinforcement learning can work simultaneously on several levels.

*Exercise 1.1: Self-Play* Suppose, instead of playing against a random opponent, the reinforcement learning algorithm described above played against itself, with both sides learning. What do you think would happen in this case? Would it learn a di↵erent policy for selecting moves? ⇤

*Exercise 1.2: Symmetries* Many tic-tac-toe positions appear di↵erent but are really the same because of symmetries. How might we amend the learning process described above to take advantage of this? In what ways would this change improve the learning process? Now think again. Suppose the opponent did not take advantage of symmetries. In that case, should we? Is it true, then, that symmetrically equivalent positions should necessarily have the same value? ⇤

*Exercise 1.3: Greedy Play* Suppose the reinforcement learning player was *greedy*, that is, it always played the move that brought it to the position that it rated the best. Might it

![](_page_22_Figure_2.jpeg)

#### <span id="page-22-0"></span>1.6 Summary

Reinforcement learning is a computational approach to understanding and automating goal-directed learning and decision making. It is distinguished from other computational approaches by its emphasis on learning by an agent from direct interaction with its environment, without requiring exemplary supervision or complete models of the environment. In our opinion, reinforcement learning is the first field to seriously address the computational issues that arise when learning from interaction with an environment in order to achieve long-term goals.

Reinforcement learning uses the formal framework of Markov decision processes to define the interaction between a learning agent and its environment in terms of states, actions, and rewards. This framework is intended to be a simple way of representing essential features of the artificial intelligence problem. These features include a sense of cause and e↵ect, a sense of uncertainty and nondeterminism, and the existence of explicit goals.

The concepts of value and value function are key to most of the reinforcement learning methods that we consider in this book. We take the position that value functions are important for ecient search in the space of policies. The use of value functions distinguishes reinforcement learning methods from evolutionary methods that search directly in policy space guided by evaluations of entire policies.

#### <span id="page-22-1"></span>1.7 Early History of Reinforcement Learning

The early history of reinforcement learning has two main threads, both long and rich, that were pursued independently before intertwining in modern reinforcement learning. One thread concerns learning by trial and error, and originated in the psychology of animal learning. This thread runs through some of the earliest work in artificial intelligence and led to the revival of reinforcement learning in the early 1980s. The second thread concerns the problem of optimal control and its solution using value functions and dynamic programming. For the most part, this thread did not involve learning. The two threads were mostly independent, but became interrelated to some extent around a

third, less distinct thread concerning temporal-di↵erence methods such as that used in the tic-tac-toe example in this chapter. All three threads came together in the late 1980s to produce the modern field of reinforcement learning as we present it in this book.

The thread focusing on trial-and-error learning is the one with which we are most familiar and about which we have the most to say in this brief history. Before doing that, however, we briefly discuss the optimal control thread.

The term "optimal control" came into use in the late 1950s to describe the problem of designing a controller to minimize or maximize a measure of a dynamical system's behavior over time. One of the approaches to this problem was developed in the mid-1950s by Richard Bellman and others through extending a nineteenth century theory of Hamilton and Jacobi. This approach uses the concepts of a dynamical system's state and of a value function, or "optimal return function," to define a functional equation, now often called the Bellman equation. The class of methods for solving optimal control problems by solving this equation came to be known as dynamic programming (Bellman, 1957a). Bellman (1957b) also introduced the discrete stochastic version of the optimal control problem known as Markov decision processes (MDPs). Ronald Howard (1960) devised the policy iteration method for MDPs. All of these are essential elements underlying the theory and algorithms of modern reinforcement learning.

Dynamic programming is widely considered the only feasible way of solving general stochastic optimal control problems. It su↵ers from what Bellman called "the curse of dimensionality," meaning that its computational requirements grow exponentially with the number of state variables, but it is still far more ecient and more widely applicable than any other general method. Dynamic programming has been extensively developed since the late 1950s, including extensions to partially observable MDPs (surveyed by Lovejoy, 1991), many applications (surveyed by White, 1985, 1988, 1993), approximation methods (surveyed by Rust, 1996), and asynchronous methods (Bertsekas, 1982, 1983). Many excellent modern treatments of dynamic programming are available (e.g., Bertsekas, 2005, 2012; Puterman, 1994; Ross, 1983; Whittle, 1982, 1983). Bryson (1996) provides an authoritative history of optimal control.

Connections between optimal control and dynamic programming, on the one hand, and learning, on the other, were slow to be recognized. We cannot be sure about what accounted for this separation, but its main cause was likely the separation between the disciplines involved and their di↵erent goals. Also contributing may have been the prevalent view of dynamic programming as an o↵-line computation depending essentially on accurate system models and analytic solutions to the Bellman equation. Further, the simplest form of dynamic programming is a computation that proceeds backwards in time, making it dicult to see how it could be involved in a learning process that must proceed in a forward direction. Some of the earliest work in dynamic programming, such as that by Bellman and Dreyfus (1959), might now be classified as following a learning approach. Witten's (1977) work (discussed below) certainly qualifies as a combination of learning and dynamic-programming ideas. Werbos (1987) argued explicitly for greater interrelation of dynamic programming and learning methods and for dynamic programming's relevance to understanding neural and cognitive mechanisms. For us the full integration of dynamic programming methods with online learning did not occur

until the work of Chris Watkins in 1989, whose treatment of reinforcement learning using the MDP formalism has been widely adopted. Since then these relationships have been extensively developed by many researchers, most particularly by Dimitri Bertsekas and John Tsitsiklis (1996), who coined the term "neurodynamic programming" to refer to the combination of dynamic programming and artificial neural networks. Another term currently in use is "approximate dynamic programming." These various approaches emphasize di↵erent aspects of the subject, but they all share with reinforcement learning an interest in circumventing the classical shortcomings of dynamic programming.

We consider all of the work in optimal control also to be, in a sense, work in reinforcement learning. We define a reinforcement learning method as any e↵ective way of solving reinforcement learning problems, and it is now clear that these problems are closely related to optimal control problems, particularly stochastic optimal control problems such as those formulated as MDPs. Accordingly, we must consider the solution methods of optimal control, such as dynamic programming, also to be reinforcement learning methods. Because almost all of the conventional methods require complete knowledge of the system to be controlled, it feels a little unnatural to say that they are part of reinforcement *learning*. On the other hand, many dynamic programming algorithms are incremental and iterative. Like learning methods, they gradually reach the correct answer through successive approximations. As we show in the rest of this book, these similarities are far more than superficial. The theories and solution methods for the cases of complete and incomplete knowledge are so closely related that we feel they must be considered together as part of the same subject matter.

Let us return now to the other major thread leading to the modern field of reinforcement learning, the thread centered on the idea of trial-and-error learning. We only touch on the major points of contact here, taking up this topic in more detail in Section 14.3. According to American psychologist R. S. Woodworth (1938) the idea of trial-and-error learning goes as far back as the 1850s to Alexander Bain's discussion of learning by "groping and experiment" and more explicitly to the British ethologist and psychologist Conway Lloyd Morgan's 1894 use of the term to describe his observations of animal behavior. Perhaps the first to succinctly express the essence of trial-and-error learning as a principle of learning was Edward Thorndike:

Of several responses made to the same situation, those which are accompanied or closely followed by satisfaction to the animal will, other things being equal, be more firmly connected with the situation, so that, when it recurs, they will be more likely to recur; those which are accompanied or closely followed by discomfort to the animal will, other things being equal, have their connections with that situation weakened, so that, when it recurs, they will be less likely to occur. The greater the satisfaction or discomfort, the greater the strengthening or weakening of the bond. (Thorndike, 1911, p. 244)

Thorndike called this the "Law of E↵ect" because it describes the e↵ect of reinforcing events on the tendency to select actions. Thorndike later modified the law to better account for subsequent data on animal learning (such as di↵erences between the e↵ects of reward and punishment), and the law in its various forms has generated considerable controversy among learning theorists (e.g., see Gallistel, 2005; Herrnstein, 1970; Kimble, 1961, 1967; Mazur, 1994). Despite this, the Law of E↵ect—in one form or another—is widely regarded as a basic principle underlying much behavior (e.g., Hilgard and Bower, 1975; Dennett, 1978; Campbell, 1960; Cziko, 1995). It is the basis of the influential learning theories of Clark Hull (1943, 1952) and the influential experimental methods of B. F. Skinner (1938).

The term "reinforcement" in the context of animal learning came into use well after Thorndike's expression of the Law of E↵ect, first appearing in this context (to the best of our knowledge) in the 1927 English translation of Pavlov's monograph on conditioned reflexes. Pavlov described reinforcement as the strengthening of a pattern of behavior due to an animal receiving a stimulus—a reinforcer—in an appropriate temporal relationship with another stimulus or with a response. Some psychologists extended the idea of reinforcement to include weakening as well as strengthening of behavior, and extended the idea of a reinforcer to include possibly the omission or termination of stimulus. To be considered a reinforcer, the strengthening or weakening must persist after the reinforcer is withdrawn; a stimulus that merely attracts an animal's attention or that energizes its behavior without producing lasting changes would not be considered a reinforcer.

The idea of implementing trial-and-error learning in a computer appeared among the earliest thoughts about the possibility of artificial intelligence. In a 1948 report, Alan Turing described a design for a "pleasure-pain system" that worked along the lines of the Law of E↵ect:

When a configuration is reached for which the action is undetermined, a random choice for the missing data is made and the appropriate entry is made in the description, tentatively, and is applied. When a pain stimulus occurs all tentative entries are cancelled, and when a pleasure stimulus occurs they are all made permanent. (Turing, 1948)

Many ingenious electro-mechanical machines were constructed that demonstrated trialand-error learning. The earliest may have been a machine built by Thomas Ross (1933) that was able to find its way through a simple maze and remember the path through the settings of switches. In 1951 W. Grey Walter built a version of his "mechanical tortoise" (Walter, 1950) capable of a simple form of learning. In 1952 Claude Shannon demonstrated a maze-running mouse named Theseus that used trial and error to find its way through a maze, with the maze itself remembering the successful directions via magnets and relays under its floor (see also Shannon, 1951). J. A. Deutsch (1954) described a maze-solving machine based on his behavior theory (Deutsch, 1953) that has some properties in common with model-based reinforcement learning (Chapter 8). In his PhD dissertation, Marvin Minsky (1954) discussed computational models of reinforcement learning and described his construction of an analog machine composed of components he called SNARCs (Stochastic Neural-Analog Reinforcement Calculators) meant to resemble modifiable synaptic connections in the brain (Chapter 15). The web site cyberneticzoo.com contains a wealth of information on these and many other electro-mechanical learning machines.

Building electro-mechanical learning machines gave way to programming digital computers to perform various types of learning, some of which implemented trial-and-error learning. Farley and Clark (1954) described a digital simulation of a neural-network

learning machine that learned by trial and error. But their interests soon shifted from trial-and-error learning to generalization and pattern recognition, that is, from reinforcement learning to supervised learning (Clark and Farley, 1955). This began a pattern of confusion about the relationship between these types of learning. Many researchers seemed to believe that they were studying reinforcement learning when they were actually studying supervised learning. For example, artificial neural network pioneers such as Rosenblatt (1962) and Widrow and Ho↵ (1960) were clearly motivated by reinforcement learning—they used the language of rewards and punishments—but the systems they studied were supervised learning systems suitable for pattern recognition and perceptual learning. Even today, some researchers and textbooks minimize or blur the distinction between these types of learning. For example, some textbooks have used the term "trialand-error" to describe artificial neural networks that learn from training examples. This is an understandable confusion because these networks use error information to update connection weights, but this misses the essential character of trial-and-error learning as selecting actions on the basis of evaluative feedback that does not rely on knowledge of what the correct action should be.

Partly as a result of these confusions, research into genuine trial-and-error learning became rare in the 1960s and 1970s, although there were notable exceptions. In the 1960s the terms "reinforcement" and "reinforcement learning" were used in the engineering literature for the first time to describe engineering uses of trial-and-error learning (e.g., Waltz and Fu, 1965; Mendel, 1966; Fu, 1970; Mendel and McClaren, 1970). Particularly influential was Minsky's paper "Steps Toward Artificial Intelligence" (Minsky, 1961), which discussed several issues relevant to trial-and-error learning, including prediction, expectation, and what he called the *basic credit-assignment problem for complex reinforcement learning systems*: How do you distribute credit for success among the many decisions that may have been involved in producing it? All of the methods we discuss in this book are, in a sense, directed toward solving this problem. Minsky's paper is well worth reading today.

In the next few paragraphs we discuss some of the other exceptions and partial exceptions to the relative neglect of computational and theoretical study of genuine trial-and-error learning in the 1960s and 1970s.

One exception was the work of the New Zealand researcher John Andreae, who developed a system called STeLLA that learned by trial and error in interaction with its environment. This system included an internal model of the world and, later, an "internal monologue" to deal with problems of hidden state (Andreae, 1963, 1969; Andreae and Cashin, 1969). Andreae's later work (1977) placed more emphasis on learning from a teacher, but still included learning by trial and error, with the generation of novel events being one of the system's goals. A feature of this work was a "leakback process," elaborated more fully in Andreae (1998), that implemented a credit-assignment mechanism similar to the backing-up update operations that we describe. Unfortunately, his pioneering research was not well known and did not greatly impact subsequent reinforcement learning research. Recent summaries are available (Andreae, 2017a,b).

More influential was the work of Donald Michie. In 1961 and 1963 he described a simple trial-and-error learning system for learning how to play tic-tac-toe (or naughts

and crosses) called MENACE (for Matchbox Educable Naughts and Crosses Engine). It consisted of a matchbox for each possible game position, each matchbox containing a number of colored beads, a di↵erent color for each possible move from that position. By drawing a bead at random from the matchbox corresponding to the current game position, one could determine MENACE's move. When a game was over, beads were added to or removed from the boxes used during play to reward or punish MENACE's decisions. Michie and Chambers (1968) described another tic-tac-toe reinforcement learner called GLEE (Game Learning Expectimaxing Engine) and a reinforcement learning controller called BOXES. They applied BOXES to the task of learning to balance a pole hinged to a movable cart on the basis of a failure signal occurring only when the pole fell or the cart reached the end of a track. This task was adapted from the earlier work of Widrow and Smith (1964), who used supervised learning methods, assuming instruction from a teacher already able to balance the pole. Michie and Chambers's version of pole-balancing is one of the best early examples of a reinforcement learning task under conditions of incomplete knowledge. It influenced much later work in reinforcement learning, beginning with some of our own studies (Barto, Sutton, and Anderson, 1983; Sutton, 1984). Michie (1974) consistently emphasized trial and error and learning as essential aspects of artificial intelligence.

Widrow, Gupta, and Maitra (1973) modified the Least-Mean-Square (LMS) algorithm of Widrow and Ho↵ (1960) to produce a reinforcement learning rule that could learn from success and failure signals instead of from training examples. They called this form of learning "selective bootstrap adaptation" and described it as "learning with a critic" instead of "learning with a teacher." They analyzed this rule and showed how it could learn to play blackjack. This was an isolated foray into reinforcement learning by Widrow, whose contributions to supervised learning were much more influential. Our use of the term "critic" is derived from Widrow, Gupta, and Maitra's paper. Buchanan, Mitchell, Smith, and Johnson (1978) independently used the term critic in the context of machine learning (see also Dietterich and Buchanan, 1984), but for them a critic was an expert system able to do more than evaluate performance.

Research on *learning automata* had a more direct influence on the trial-and-error thread leading to modern reinforcement learning research. These are methods for solving a nonassociative, purely selectional learning problem known as the *k-armed bandit* by analogy to a slot machine, or "one-armed bandit," except with *k* levers (see Chapter 2). Learning automata are simple, low-memory machines for improving the probability of reward in these problems. Learning automata originated with work in the 1960s of the Russian mathematician and physicist M. L. Tsetlin and colleagues (published posthumously in Tsetlin, 1973) and has been extensively developed since then within engineering (see Narendra and Thathachar, 1974, 1989). These developments included the study of *stochastic learning automata*, which are methods for updating action probabilities on the basis of reward signals. Although not developed in the tradition of stochastic learning automata, Harth and Tzanakou's (1974) Alopex algorithm (for *Al*gorithm *o*f *p*attern *ex*traction) is a stochastic method for detecting correlations between actions and reinforcement that influenced some of our early research (Barto, Sutton, and Brouwer, 1981). Stochastic learning automata were foreshadowed by earlier work in psychology, beginning with William Estes' (1950) e↵ort toward a statistical theory of learning and further developed by others (e.g., Bush and Mosteller, 1955; Sternberg, 1963).

The statistical learning theories developed in psychology were adopted by researchers in economics, leading to a thread of research in that field devoted to reinforcement learning. This work began in 1973 with the application of Bush and Mosteller's learning theory to a collection of classical economic models (Cross, 1973). One goal of this research was to study artificial agents that act more like real people than do traditional idealized economic agents (Arthur, 1991). This approach expanded to the study of reinforcement learning in the context of game theory. Reinforcement learning in economics developed largely independently of the early work in reinforcement learning in artificial intelligence, though game theory remains a topic of interest in both fields (beyond the scope of this book). Camerer (2011) discusses the reinforcement learning tradition in economics, and Now´e, Vrancx, and De Hauwere (2012) provide an overview of the subject from the point of view of multi-agent extensions to the approach that we introduce in this book. Reinforcement learning in the context of game theory is a much di↵erent subject than reinforcement learning used in programs to play tic-tac-toe, checkers, and other recreational games. See, for example, Szita (2012) for an overview of this aspect of reinforcement learning and games.

John Holland (1975) outlined a general theory of adaptive systems based on selectional principles. His early work concerned trial and error primarily in its nonassociative form, as in evolutionary methods and the *k*-armed bandit. In 1976 and more fully in 1986, he introduced *classifier systems*, true reinforcement learning systems including association and value functions. A key component of Holland's classifier systems was the "bucket-brigade algorithm" for credit assignment, which is closely related to the temporal di↵erence algorithm used in our tic-tac-toe example and discussed in Chapter 6. Another key component was a *genetic algorithm*, an evolutionary method whose role was to evolve useful representations. Classifier systems have been extensively developed by many researchers to form a major branch of reinforcement learning research (reviewed by Urbanowicz and Moore, 2009), but genetic algorithms—which we do not consider to be reinforcement learning systems by themselves—have received much more attention, as have other approaches to evolutionary computation (e.g., Fogel, Owens and Walsh, 1966; Koza, 1992).

The individual most responsible for reviving the trial-and-error thread of reinforcement learning within artificial intelligence was Harry Klopf (1972, 1975, 1982). Klopf recognized that essential aspects of adaptive behavior were being lost as learning researchers came to focus almost exclusively on supervised learning. What was missing, according to Klopf, were the hedonic aspects of behavior: the drive to achieve some result from the environment, to control the environment toward desired ends and away from undesired ends (see Section 15.9). This is the essential idea of trial-and-error learning. Klopf's ideas were especially influential on the authors because our assessment of them (Barto and Sutton, 1981a) led to our appreciation of the distinction between supervised and reinforcement learning, and to our eventual focus on reinforcement learning. Much of the early work that we and colleagues accomplished was directed toward showing that reinforcement learning and supervised learning were indeed di↵erent (Barto, Sutton, and Brouwer, 1981; Barto and Sutton, 1981b; Barto and Anandan, 1985). Other studies showed how reinforcement learning could address important problems in artificial neural

network learning, in particular, how it could produce learning algorithms for multilayer networks (Barto, Anderson, and Sutton, 1982; Barto and Anderson, 1985; Barto, 1985, 1986; Barto and Jordan, 1987; see Section 15.10).

We turn now to the third thread to the history of reinforcement learning, that concerning temporal-di↵erence learning. Temporal-di↵erence learning methods are distinctive in being driven by the di↵erence between temporally successive estimates of the same quantity—for example, of the probability of winning in the tic-tac-toe example. This thread is smaller and less distinct than the other two, but it has played a particularly important role in the field, in part because temporal-di↵erence methods seem to be new and unique to reinforcement learning.

The origins of temporal-di↵erence learning are in part in animal learning psychology, in particular, in the notion of *secondary reinforcers*. A secondary reinforcer is a stimulus that has been paired with a primary reinforcer such as food or pain and, as a result, has come to take on similar reinforcing properties. Minsky (1954) may have been the first to realize that this psychological principle could be important for artificial learning systems. Arthur Samuel (1959) was the first to propose and implement a learning method that included temporal-di↵erence ideas, as part of his celebrated checkers-playing program (Section 16.2).

Samuel made no reference to Minsky's work or to possible connections to animal learning. His inspiration apparently came from Claude Shannon's (1950) suggestion that a computer could be programmed to use an evaluation function to play chess, and that it might be able to improve its play by modifying this function online. (It is possible that these ideas of Shannon's also influenced Bellman, but we know of no evidence for this.) Minsky (1961) extensively discussed Samuel's work in his "Steps" paper, suggesting the connection to secondary reinforcement theories, both natural and artificial.

As we have discussed, in the decade following the work of Minsky and Samuel, little computational work was done on trial-and-error learning, and apparently no computational work at all was done on temporal-di↵erence learning. In 1972, Klopf brought trial-anderror learning together with an important component of temporal-di↵erence learning. Klopf was interested in principles that would scale to learning in large systems, and thus was intrigued by notions of local reinforcement, whereby subcomponents of an overall learning system could reinforce one another. He developed the idea of "generalized reinforcement," whereby every component (nominally, every neuron) views all of its inputs in reinforcement terms: excitatory inputs as rewards and inhibitory inputs as punishments. This is not the same idea as what we now know as temporal-di↵erence learning, and in retrospect it is farther from it than was Samuel's work. On the other hand, Klopf linked the idea with trial-and-error learning and related it to the massive empirical database of animal learning psychology.

Sutton (1978a,b,c) developed Klopf's ideas further, particularly the links to animal learning theories, describing learning rules driven by changes in temporally successive predictions. He and Barto refined these ideas and developed a psychological model of classical conditioning based on temporal-di↵erence learning (Sutton and Barto, 1981a; Barto and Sutton, 1982). There followed several other influential psychological models of classical conditioning based on temporal-di↵erence learning (e.g., Klopf, 1988; Moore et al., 1986; Sutton and Barto, 1987, 1990). Some neuroscience models developed at this time are well interpreted in terms of temporal-di↵erence learning (Hawkins and Kandel, 1984; Byrne, Gingrich, and Baxter, 1990; Gelperin, Hopfield, and Tank, 1985; Tesauro, 1986; Friston et al., 1994), although in most cases there was no historical connection.

Our early work on temporal-di↵erence learning was strongly influenced by animal learning theories and by Klopf's work. Relationships to Minsky's "Steps" paper and to Samuel's checkers players were recognized only afterward. By 1981, however, we were fully aware of all the prior work mentioned above as part of the temporal-di↵erence and trial-and-error threads. At this time we developed a method for using temporal-di↵erence learning combined with trial-and-error learning, known as the *actor–critic architecture*, and applied this method to Michie and Chambers's pole-balancing problem (Barto, Sutton, and Anderson, 1983). This method was extensively studied in Sutton's (1984) PhD dissertation and extended to use backpropagation neural networks in Anderson's (1986) PhD dissertation. Around this time, Holland (1986) incorporated temporaldi↵erence ideas explicitly into his classifier systems in the form of his bucket-brigade algorithm. A key step was taken by Sutton (1988) by separating temporal-di↵erence learning from control, treating it as a general prediction method. That paper also introduced the TD() algorithm and proved some of its convergence properties.

As we were finalizing our work on the actor–critic architecture in 1981, we discovered a paper by Ian Witten (1977, 1976a) which appears to be the earliest publication of a temporal-di↵erence learning rule. He proposed the method that we now call tabular TD(0) for use as part of an adaptive controller for solving MDPs. This work was first submitted for journal publication in 1974 and also appeared in Witten's 1976 PhD dissertation. Witten's work was a descendant of Andreae's early experiments with STeLLA and other trial-and-error learning systems. Thus, Witten's 1977 paper spanned both major threads of reinforcement learning research—trial-and-error learning and optimal control—while making a distinct early contribution to temporal-di↵erence learning.

The temporal-di↵erence and optimal control threads were fully brought together in 1989 with Chris Watkins's development of Q-learning. This work extended and integrated prior work in all three threads of reinforcement learning research. Paul Werbos (1987) contributed to this integration by arguing for the convergence of trial-and-error learning and dynamic programming since 1977. By the time of Watkins's work there had been tremendous growth in reinforcement learning research, primarily in the machine learning subfield of artificial intelligence, but also in artificial neural networks and artificial intelligence more broadly. In 1992, the remarkable success of Gerry Tesauro's backgammon playing program, TD-Gammon, brought additional attention to the field.

In the time since publication of the first edition of this book, a flourishing subfield of neuroscience developed that focuses on the relationship between reinforcement learning algorithms and reinforcement learning in the nervous system. Most responsible for this is an uncanny similarity between the behavior of temporal-di↵erence algorithms and the activity of dopamine producing neurons in the brain, as pointed out by a number of researchers (Friston et al., 1994; Barto, 1995a; Houk, Adams, and Barto, 1995; Montague, Dayan, and Sejnowski, 1996; and Schultz, Dayan, and Montague, 1997). Chapter 15 provides an introduction to this exciting aspect of reinforcement learning. Other important

contributions made in the recent history of reinforcement learning are too numerous to mention in this brief account; we cite many of these at the end of the individual chapters in which they arise.

#### Bibliographical Remarks

For additional general coverage of reinforcement learning, we refer the reader to the books by Szepesv´ari (2010), Bertsekas and Tsitsiklis (1996), Kaelbling (1993a), and Sugiyama, Hachiya, and Morimura (2013). Books that take a control or operations research perspective include those of Si, Barto, Powell, and Wunsch (2004), Powell (2011), Lewis and Liu (2012), and Bertsekas (2012). Cao's (2009) review places reinforcement learning in the context of other approaches to learning and optimization of stochastic dynamic systems. Three special issues of the journal *Machine Learning* focus on reinforcement learning: Sutton (1992a), Kaelbling (1996), and Singh (2002). Useful surveys are provided by Barto (1995b); Kaelbling, Littman, and Moore (1996); and Keerthi and Ravindran (1997). The volume edited by Weiring and van Otterlo (2012) provides an excellent overview of recent developments.

- 1.2 The example of Phil's breakfast in this chapter was inspired by Agre (1988).
- 1.5 The temporal-di↵erence method used in the tic-tac-toe example is developed in Chapter 6.

## <span id="page-32-0"></span>*Part I: Tabular Solution Methods*

In this part of the book we describe almost all the core ideas of reinforcement learning algorithms in their simplest forms: that in which the state and action spaces are small enough for the approximate value functions to be represented as arrays, or *tables*. In this case, the methods can often find exact solutions, that is, they can often find exactly the optimal value function and the optimal policy. This contrasts with the approximate methods described in the next part of the book, which only find approximate solutions, but which in return can be applied e↵ectively to much larger problems.

The first chapter of this part of the book describes solution methods for the special case of the reinforcement learning problem in which there is only a single state, called bandit problems. The second chapter describes the general problem formulation that we treat throughout the rest of the book—finite Markov decision processes—and its main ideas including Bellman equations and value functions.

The next three chapters describe three fundamental classes of methods for solving finite Markov decision problems: dynamic programming, Monte Carlo methods, and temporaldi↵erence learning. Each class of methods has its strengths and weaknesses. Dynamic programming methods are well developed mathematically, but require a complete and accurate model of the environment. Monte Carlo methods don't require a model and are conceptually simple, but are not well suited for step-by-step incremental computation. Finally, temporal-di↵erence methods require no model and are fully incremental, but are more complex to analyze. The methods also di↵er in several ways with respect to their eciency and speed of convergence.

The remaining two chapters describe how these three classes of methods can be combined to obtain the best features of each of them. In one chapter we describe how the strengths of Monte Carlo methods can be combined with the strengths of temporaldi↵erence methods via multi-step bootstrapping methods. In the final chapter of this part of the book we show how temporal-di↵erence learning methods can be combined with model learning and planning methods (such as dynamic programming) for a complete and unified solution to the tabular reinforcement learning problem.

## <span id="page-33-0"></span>Chapter 3

# Finite Markov Decision Processes

In this chapter we introduce the formal problem of finite Markov decision processes, or finite MDPs, which we try to solve in the rest of the book. This problem involves evaluative feedback, as in bandits, but also an associative aspect—choosing di↵erent actions in di↵erent situations. MDPs are a classical formalization of sequential decision making, where actions influence not just immediate rewards, but also subsequent situations, or states, and through those future rewards. Thus MDPs involve delayed reward and the need to trade o↵ immediate and delayed reward. Whereas in bandit problems we estimated the value *q*⇤(*a*) of each action *a*, in MDPs we estimate the value *q*⇤(*s, a*) of each action *a* in each state *s*, or we estimate the value *v*⇤(*s*) of each state given optimal action selections. These state-dependent quantities are essential to accurately assigning credit for long-term consequences to individual action selections.

MDPs are a mathematically idealized form of the reinforcement learning problem for which precise theoretical statements can be made. We introduce key elements of the problem's mathematical structure, such as returns, value functions, and Bellman equations. We try to convey the wide range of applications that can be formulated as finite MDPs. As in all of artificial intelligence, there is a tension between breadth of applicability and mathematical tractability. In this chapter we introduce this tension and discuss some of the trade-o↵s and challenges that it implies. Some ways in which reinforcement learning can be taken beyond MDPs are treated in Chapter 17.

#### <span id="page-33-1"></span>3.1 The Agent–Environment Interface

MDPs are meant to be a straightforward framing of the problem of learning from interaction to achieve a goal. The learner and decision maker is called the *agent*. The thing it interacts with, comprising everything outside the agent, is called the *environment*. These interact continually, the agent selecting actions and the environment responding to

these actions and presenting new situations to the agent.[1](#page-34-0) The environment also gives rise to rewards, special numerical values that the agent seeks to maximize over time through its choice of actions.

![](_page_34_Figure_3.jpeg)

Figure 3.1: The agent–environment interaction in a Markov decision process.

More specifically, the agent and environment interact at each of a sequence of discrete time steps, *t* = 0*,* 1*,* 2*,* 3*,...*. [2](#page-34-1) At each time step *t*, the agent receives some representation of the environment's *state*, *<sup>S</sup><sup>t</sup>* <sup>2</sup> <sup>S</sup>, and on that basis selects an *action*, *<sup>A</sup><sup>t</sup>* <sup>2</sup> <sup>A</sup>(*s*).[3](#page-34-2) One time step later, in part as a consequence of its action, the agent receives a numerical *reward*, *Rt*+1 2 R ⇢ R, and finds itself in a new state, *St*+1. [4](#page-34-3) The MDP and agent together thereby give rise to a sequence or *trajectory* that begins like this:

$$S_0, A_0, R_1, S_1, A_1, R_2, S_2, A_2, R_3, \dots$$
 (3.1)

In a *finite* MDP, the sets of states, actions, and rewards (S, A, and R) all have a finite number of elements. In this case, the random variables *R<sup>t</sup>* and *S<sup>t</sup>* have well defined discrete probability distributions dependent only on the preceding state and action. That is, for particular values of these random variables, *s*<sup>0</sup> 2 S and *r* 2 R, there is a probability of those values occurring at time *t*, given particular values of the preceding state and action:

<span id="page-34-4"></span>
$$p(s', r | s, a) \doteq \Pr\{S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a\},$$
 (3.2)

for all *s*<sup>0</sup> *, s* 2 S, *r* 2 R, and *a* 2 A(*s*). The function *p* defines the *dynamics* of the MDP. The dot over the equals sign in the equation reminds us that it is a definition (in this case of the function *p*) rather than a fact that follows from previous definitions. The dynamics function *p* : S ⇥ R ⇥ S ⇥ A ! [0*,* 1] is an ordinary deterministic function of four arguments. The '*|*' in the middle of it comes from the notation for conditional probability,

<span id="page-34-0"></span><sup>1</sup>We use the terms *agent*, *environment*, and *action* instead of the engineers' terms *controller*, *controlled system* (or *plant*), and *control signal* because they are meaningful to a wider audience.

<span id="page-34-1"></span><sup>2</sup>We restrict attention to discrete time to keep things as simple as possible, even though many of the ideas can be extended to the continuous-time case (e.g., see Bertsekas and Tsitsiklis, 1996; Doya, 1996).

<span id="page-34-2"></span><sup>3</sup>To simplify notation, we sometimes assume the special case in which the action set is the same in all states and write it simply as A.

<span id="page-34-3"></span><sup>4</sup>We use *Rt*+1 instead of *R<sup>t</sup>* to denote the reward due to *A<sup>t</sup>* because it emphasizes that the next reward and next state, *Rt*+1 and *St*+1, are jointly determined. Unfortunately, both conventions are widely used in the literature.

but here it just reminds us that *p* specifies a probability distribution for each choice of *s* and *a*, that is, that

<span id="page-35-0"></span>
$$\sum_{s' \in \mathbb{S}} \sum_{r \in \mathbb{R}} p(s', r | s, a) = 1, \text{ for all } s \in \mathbb{S}, a \in \mathcal{A}(s).$$
(3.3)

In a *Markov* decision process, the probabilities given by *p* completely characterize the environment's dynamics. That is, the probability of each possible value for *S<sup>t</sup>* and *R<sup>t</sup>* depends on the immediately preceding state and action, *S<sup>t</sup>*<sup>1</sup> and *A<sup>t</sup>*1, and, given them, not at all on earlier states and actions. This is best viewed as a restriction not on the decision process, but on the *state*. The state must include information about all aspects of the past agent–environment interaction that make a di↵erence for the future. If it does, then the state is said to have the *Markov property*. We will assume the Markov property throughout this book, though starting in Part II we will consider approximation methods that do not rely on it, and in Chapter 17 we consider how a Markov state can be eciently learned and constructed from non-Markov observations.

<span id="page-35-1"></span>From the four-argument dynamics function, *p*, one can compute anything else one might want to know about the environment, such as the *state-transition probabilities* (which we denote, with a slight abuse of notation, as a three-argument function *p* : S⇥S⇥A ! [0*,* 1]),

$$p(s'|s,a) \doteq \Pr\{S_t = s' \mid S_{t-1} = s, A_{t-1} = a\} = \sum_{r \in \mathcal{R}} p(s',r|s,a).$$
 (3.4)

We can also compute the expected rewards for state–action pairs as a two-argument function *r* : S ⇥ A ! R:

<span id="page-35-2"></span>
$$r(s,a) \doteq \mathbb{E}[R_t \mid S_{t-1} = s, A_{t-1} = a] = \sum_{r \in \mathcal{R}} r \sum_{s' \in \mathcal{S}} p(s', r \mid s, a),$$
 (3.5)

and the expected rewards for state–action–next-state triples as a three-argument function *r* : S ⇥ A ⇥ S ! R,

$$r(s, a, s') \doteq \mathbb{E}[R_t \mid S_{t-1} = s, A_{t-1} = a, S_t = s'] = \sum_{r \in \mathcal{R}} r \frac{p(s', r \mid s, a)}{p(s' \mid s, a)}.$$
 (3.6)

In this book, we usually use the four-argument *p* function [\(3.2\)](#page-34-4), but each of these other notations are also occasionally convenient.

The MDP framework is abstract and flexible and can be applied to many di↵erent problems in many di↵erent ways. For example, the time steps need not refer to fixed intervals of real time; they can refer to arbitrary successive stages of decision making and acting. The actions can be low-level controls, such as the voltages applied to the motors of a robot arm, or high-level decisions, such as whether or not to have lunch or to go to graduate school. Similarly, the states can take a wide variety of forms. They can be completely determined by low-level sensations, such as direct sensor readings, or they can be more high-level and abstract, such as symbolic descriptions of objects in a room. Some of what makes up a state could be based on memory of past sensations or

even be entirely mental or subjective. For example, an agent could be in the state of not being sure where an object is, or of having just been surprised in some clearly defined sense. Similarly, some actions might be totally mental or computational. For example, some actions might control what an agent chooses to think about, or where it focuses its attention. In general, actions can be any decisions we want to learn how to make, and states can be anything we can know that might be useful in making them.

In particular, the boundary between agent and environment is typically not the same as the physical boundary of a robot's or an animal's body. Usually, the boundary is drawn closer to the agent than that. For example, the motors and mechanical linkages of a robot and its sensing hardware should usually be considered parts of the environment rather than parts of the agent. Similarly, if we apply the MDP framework to a person or animal, the muscles, skeleton, and sensory organs should be considered part of the environment. Rewards, too, presumably are computed inside the physical bodies of natural and artificial learning systems, but are considered external to the agent.

The general rule we follow is that anything that cannot be changed arbitrarily by the agent is considered to be outside of it and thus part of its environment. We do not assume that everything in the environment is unknown to the agent. For example, the agent often knows quite a bit about how its rewards are computed as a function of its actions and the states in which they are taken. But we always consider the reward computation to be external to the agent because it defines the task facing the agent and thus must be beyond its ability to change arbitrarily. In fact, in some cases the agent may know *everything* about how its environment works and still face a dicult reinforcement learning task, just as we may know exactly how a puzzle like Rubik's cube works, but still be unable to solve it. The agent–environment boundary represents the limit of the agent's *absolute control*, not of its knowledge.

The agent–environment boundary can be located at di↵erent places for di↵erent purposes. In a complicated robot, many di↵erent agents may be operating at once, each with its own boundary. For example, one agent may make high-level decisions which form part of the states faced by a lower-level agent that implements the high-level decisions. In practice, the agent–environment boundary is determined once one has selected particular states, actions, and rewards, and thus has identified a specific decision-making task of interest.

The MDP framework is a considerable abstraction of the problem of goal-directed learning from interaction. It proposes that whatever the details of the sensory, memory, and control apparatus, and whatever objective one is trying to achieve, any problem of learning goal-directed behavior can be reduced to three signals passing back and forth between an agent and its environment: one signal to represent the choices made by the agent (the actions), one signal to represent the basis on which the choices are made (the states), and one signal to define the agent's goal (the rewards). This framework may not be sucient to represent all decision-learning problems usefully, but it has proved to be widely useful and applicable.

Of course, the particular states and actions vary greatly from task to task, and how they are represented can strongly a↵ect performance. In reinforcement learning, as in other kinds of learning, such representational choices are at present more art than science. In this book we o↵er some advice and examples regarding good ways of representing states and actions, but our primary focus is on general principles for learning how to behave once the representations have been selected.

Example 3.1: Bioreactor Suppose reinforcement learning is being applied to determine moment-by-moment temperatures and stirring rates for a bioreactor (a large vat of nutrients and bacteria used to produce useful chemicals). The actions in such an application might be target temperatures and target stirring rates that are passed to lower-level control systems that, in turn, directly activate heating elements and motors to attain the targets. The states are likely to be thermocouple and other sensory readings, perhaps filtered and delayed, plus symbolic inputs representing the ingredients in the vat and the target chemical. The rewards might be moment-by-moment measures of the rate at which the useful chemical is produced by the bioreactor. Notice that here each state is a list, or vector, of sensor readings and symbolic inputs, and each action is a vector consisting of a target temperature and a stirring rate. It is typical of reinforcement learning tasks to have states and actions with such structured representations. Rewards, on the other hand, are always single numbers.

Example 3.2: Pick-and-Place Robot Consider using reinforcement learning to control the motion of a robot arm in a repetitive pick-and-place task. If we want to learn movements that are fast and smooth, the learning agent will have to control the motors directly and have low-latency information about the current positions and velocities of the mechanical linkages. The actions in this case might be the voltages applied to each motor at each joint, and the states might be the latest readings of joint angles and velocities. The reward might be +1 for each object successfully picked up and placed. To encourage smooth movements, on each time step a small, negative reward could be given as a function of the moment-to-moment jerkiness of the motion.

*Exercise 3.1* Devise three example tasks of your own that fit into the MDP framework, identifying for each its states, actions, and rewards. Make the three examples as *di*↵*erent* from each other as possible. The framework is abstract and flexible and can be applied in many di↵erent ways. Stretch its limits in some way in at least one of your examples. ⇤

*Exercise 3.2* Is the MDP framework adequate to usefully represent *all* goal-directed learning tasks? Can you think of any clear exceptions? ⇤

*Exercise 3.3* Consider the problem of driving. You could define the actions in terms of the accelerator, steering wheel, and brake, that is, where your body meets the machine. Or you could define them farther out—say, where the rubber meets the road, considering your actions to be tire torques. Or you could define them farther in—say, where your brain meets your body, the actions being muscle twitches to control your limbs. Or you could go to a really high level and say that your actions are your choices of *where* to drive. What is the right level, the right place to draw the line between agent and environment? On what basis is one location of the line to be preferred over another? Is there any fundamental reason for preferring one location over another, or is it a free choice? ⇤

#### Example 3.3 Recycling Robot

<span id="page-38-0"></span>A mobile robot has the job of collecting empty soda cans in an oce environment. It has sensors for detecting cans, and an arm and gripper that can pick them up and place them in an onboard bin; it runs on a rechargeable battery. The robot's control system has components for interpreting sensory information, for navigating, and for controlling the arm and gripper. High-level decisions about how to search for cans are made by a reinforcement learning agent based on the current charge level of the battery. To make a simple example, we assume that only two charge levels can be distinguished, comprising a small state set S = *{*high*,* low*}*. In each state, the agent can decide whether to (1) actively search for a can for a certain period of time, (2) remain stationary and wait for someone to bring it a can, or (3) head back to its home base to recharge its battery. When the energy level is high, recharging would always be foolish, so we do not include it in the action set for this state. The action sets are then A(high) = *{*search*,* wait*}* and A(low) = *{*search*,* wait*,* recharge*}*.

The rewards are zero most of the time, but become positive when the robot secures an empty can, or large and negative if the battery runs all the way down. The best way to find cans is to actively search for them, but this runs down the robot's battery, whereas waiting does not. Whenever the robot is searching, the possibility exists that its battery will become depleted. In this case the robot must shut down and wait to be rescued (producing a low reward). If the energy level is high, then a period of active search can always be completed without risk of depleting the battery. A period of searching that begins with a high energy level leaves the energy level high with probability ↵ and reduces it to low with probability 1 ↵. On the other hand, a period of searching undertaken when the energy level is low leaves it low with probability and depletes the battery with probability 1 . In the latter case, the robot must be rescued, and the battery is then recharged back to high. Each can collected by the robot counts as a unit reward, whereas a reward of 3 results whenever the robot has to be rescued. Let *r*search and *r*wait, with *r*search *> r*wait, denote the expected number of cans the robot will collect (and hence the expected reward) while searching and while waiting respectively. Finally, suppose that no cans can be collected during a run home for recharging, and that no cans can be collected on a step in which the battery is depleted. This system is then a finite MDP, and we can write down the transition probabilities and the expected rewards, with dynamics as indicated in the table on the left:

![](_page_38_Figure_5.jpeg)

![](_page_38_Figure_6.jpeg)

Note that there is a row in the table for each possible combination of current state, *s*, action, *a* 2 A(*s*), and next state, *s*<sup>0</sup> . Some transitions have zero probability of occurring, so no expected reward is specified for them. Shown on the right is another useful way of

summarizing the dynamics of a finite MDP, as a *transition graph*. There are two kinds of nodes: *state nodes* and *action nodes*. There is a state node for each possible state (a large open circle labeled by the name of the state), and an action node for each state–action pair (a small solid circle labeled by the name of the action and connected by a line to the state node). Starting in state *s* and taking action *a* moves you along the line from state node *s* to action node (*s, a*). Then the environment responds with a transition to the next state's node via one of the arrows leaving action node (*s, a*). Each arrow corresponds to a triple (*s, s*<sup>0</sup> *, a*), where *s*<sup>0</sup> is the next state, and we label the arrow with the transition probability, *p*(*s*<sup>0</sup> *|s, a*), and the expected reward for that transition, *r*(*s, a, s*<sup>0</sup> ). Note that the transition probabilities labeling the arrows leaving an action node always sum to 1.

*Exercise 3.4* Give a table analogous to that in [Example 3.3,](#page-38-0) but for *p*(*s*<sup>0</sup> *, r|s, a*). It should have columns for *s*, *a*, *s*<sup>0</sup> , *r*, and *p*(*s*<sup>0</sup> *, r|s, a*), and a row for every 4-tuple for which *p*(*s*<sup>0</sup> *, r|s, a*) *>* 0. ⇤

#### <span id="page-39-0"></span>3.2 Goals and Rewards

In reinforcement learning, the purpose or goal of the agent is formalized in terms of a special signal, called the *reward*, passing from the environment to the agent. At each time step, the reward is a simple number, *R<sup>t</sup>* 2 R. Informally, the agent's goal is to maximize the total amount of reward it receives. This means maximizing not immediate reward, but cumulative reward in the long run. We can clearly state this informal idea as the *reward hypothesis*:

That all of what we mean by goals and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal (called reward).

The use of a reward signal to formalize the idea of a goal is one of the most distinctive features of reinforcement learning.

Although formulating goals in terms of reward signals might at first appear limiting, in practice it has proved to be flexible and widely applicable. The best way to see this is to consider examples of how it has been, or could be, used. For example, to make a robot learn to walk, researchers have provided reward on each time step proportional to the robot's forward motion. In making a robot learn how to escape from a maze, the reward is often 1 for every time step that passes prior to escape; this encourages the agent to escape as quickly as possible. To make a robot learn to find and collect empty soda cans for recycling, one might give it a reward of zero most of the time, and then a reward of +1 for each can collected. One might also want to give the robot negative rewards when it bumps into things or when somebody yells at it. For an agent to learn to play checkers or chess, the natural rewards are +1 for winning, 1 for losing, and 0 for drawing and for all nonterminal positions.

You can see what is happening in all of these examples. The agent always learns to maximize its reward. If we want it to do something for us, we must provide rewards to it in such a way that in maximizing them the agent will also achieve our goals. It is thus critical that the rewards we set up truly indicate what we want accomplished. In particular, the reward signal is not the place to impart to the agent prior knowledge about *how* to achieve what we want it to do.[5](#page-40-1) For example, a chess-playing agent should be rewarded only for actually winning, not for achieving subgoals such as taking its opponent's pieces or aining control of the center of the board. If achieving these sorts of subgoals were rewarded, then the agent might find a way to achieve them without achieving the real goal. For example, it might find a way to take the opponent's pieces even at the cost of losing the game. The reward signal is your way of communicating to the agent *what* you want achieved, not *how* you want it achieved.[6](#page-40-2)

#### <span id="page-40-0"></span>3.3 Returns and Episodes

So far we have discussed informally the objective of learning. We have said that the agent's goal is to maximize the cumulative reward it receives in the long run. How might this be defined formally? If the sequence of rewards received after time step *t* is denoted *Rt*+1*, Rt*+2*, Rt*+3*,...*, then what precise aspect of this sequence do we wish to maximize? In general, we seek to maximize the *expected return*, where the return, denoted *Gt*, is defined as some specific function of the reward sequence. In the simplest case the return is the sum of the rewards:

<span id="page-40-4"></span>
$$G_t \doteq R_{t+1} + R_{t+2} + R_{t+3} + \dots + R_T,$$
 (3.7)

where *T* is a final time step. This approach makes sense in applications in which there is a natural notion of final time step, that is, when the agent–environment interaction breaks naturally into subsequences, which we call *episodes*, [7](#page-40-3) such as plays of a game, trips through a maze, or any sort of repeated interaction. Each episode ends in a special state called the *terminal state*, followed by a reset to a standard starting state or to a sample from a standard distribution of starting states. Even if you think of episodes as ending in di↵erent ways, such as winning and losing a game, the next episode begins independently of how the previous one ended. Thus the episodes can all be considered to end in the same terminal state, with di↵erent rewards for the di↵erent outcomes. Tasks with episodes of this kind are called *episodic tasks*. In episodic tasks we sometimes need to distinguish the set of all nonterminal states, denoted S, from the set of all states plus the terminal state, denoted S<sup>+</sup>. The time of termination, *T*, is a random variable that normally varies from episode to episode.

On the other hand, in many cases the agent–environment interaction does not break naturally into identifiable episodes, but goes on continually without limit. For example, this would be the natural way to formulate an on-going process-control task, or an application to a robot with a long life span. We call these *continuing tasks*. The return formulation [\(3.7\)](#page-40-4) is problematic for continuing tasks because the final time step would be *T* = 1, and the return, which is what we are trying to maximize, could easily be infinite.

<span id="page-40-1"></span><sup>5</sup>Better places for imparting this kind of prior knowledge are the initial policy or initial value function.

<span id="page-40-2"></span><sup>6</sup>Section 17.4 delves further into the issue of designing e↵ective reward signals.

<span id="page-40-3"></span><sup>7</sup>Episodes are sometimes called "trials" in the literature.

(For example, suppose the agent receives a reward of +1 at each time step.) Thus, in this book we usually use a definition of return that is slightly more complex conceptually but much simpler mathematically.

The additional concept that we need is that of *discounting*. According to this approach, the agent tries to select actions so that the sum of the discounted rewards it receives over the future is maximized. In particular, it chooses *A<sup>t</sup>* to maximize the expected *discounted return*:

<span id="page-41-0"></span>
$$G_t \doteq R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1},$$
 (3.8)

where is a parameter, 0 1, called the *discount rate*.

The discount rate determines the present value of future rewards: a reward received *k* time steps in the future is worth only *<sup>k</sup>*<sup>1</sup> times what it would be worth if it were received immediately. If *<* 1, the infinite sum in [\(3.8\)](#page-41-0) has a finite value as long as the reward sequence *{Rk}* is bounded. If = 0, the agent is "myopic" in being concerned only with maximizing immediate rewards: its objective in this case is to learn how to choose *A<sup>t</sup>* so as to maximize only *Rt*+1. If each of the agent's actions happened to influence only the immediate reward, not future rewards as well, then a myopic agent could maximize [\(3.8\)](#page-41-0) by separately maximizing each immediate reward. But in general, acting to maximize immediate reward can reduce access to future rewards so that the return is reduced. As approaches 1, the return objective takes future rewards into account more strongly; the agent becomes more farsighted.

Returns at successive time steps are related to each other in a way that is important for the theory and algorithms of reinforcement learning:

<span id="page-41-2"></span>
$$G_{t} \doteq R_{t+1} + \gamma R_{t+2} + \gamma^{2} R_{t+3} + \gamma^{3} R_{t+4} + \cdots$$

$$= R_{t+1} + \gamma \left( R_{t+2} + \gamma R_{t+3} + \gamma^{2} R_{t+4} + \cdots \right)$$

$$= R_{t+1} + \gamma G_{t+1}$$
(3.9)

Note that this works for all time steps *t<T*, even if termination occurs at *t* + 1, provided we define *G<sup>T</sup>* = 0. This often makes it easy to compute returns from reward sequences.

Note that although the return [\(3.8\)](#page-41-0) is a sum of an infinite number of terms, it is still finite if the reward is nonzero and constant—if *<* 1. For example, if the reward is a constant +1, then the return is

<span id="page-41-1"></span>
$$G_t = \sum_{k=0}^{\infty} \gamma^k = \frac{1}{1 - \gamma}.$$
 (3.10)

*Exercise 3.5* The equations in [Section 3.1](#page-33-1) are for the continuing case and need to be modified (very slightly) to apply to episodic tasks. Show that you know the modifications needed by giving the modified version of [\(3.3\)](#page-35-0). ⇤

#### Example 3.4: Pole-Balancing

The objective in this task is to apply forces to a cart moving along a track so as to keep a pole hinged to the cart from falling over: A failure is said to occur if the pole falls past a given angle from vertical or if the cart runs o↵ the track. The pole is reset to vertical after each failure. This task could be treated as episodic, where the natural

![](_page_42_Picture_4.jpeg)

episodes are the repeated attempts to balance the pole. The reward in this case could be +1 for every time step on which failure did not occur, so that the return at each time would be the number of steps until failure. In this case, successful balancing forever would mean a return of infinity. Alternatively, we could treat pole-balancing as a continuing task, using discounting. In this case the reward would be 1 on each failure and zero at all other times. The return at each time would then be related to *<sup>K</sup>*<sup>1</sup>, where *<sup>K</sup>* is the number of time steps before failure (as well as to the times of later failures). In either case, the return is maximized by keeping the pole balanced for as long as possible.

*Exercise 3.6* Suppose you treated pole-balancing as an episodic task but also used discounting, with all rewards zero except for 1 upon failure. What then would the return be at each time? How does this return di↵er from that in the discounted, continuing formulation of this task? ⇤

*Exercise 3.7* Imagine that you are designing a robot to run a maze. You decide to give it a reward of +1 for escaping from the maze and a reward of zero at all other times. The task seems to break down naturally into episodes—the successive runs through the maze—so you decide to treat it as an episodic task, where the goal is to maximize expected total reward [\(3.7\)](#page-40-4). After running the learning agent for a while, you find that it is showing no improvement in escaping from the maze. What is going wrong? Have you e↵ectively communicated to the agent what you want it to achieve? ⇤

*Exercise 3.8* Suppose = 0*.*5 and the following sequence of rewards is received *R*<sup>1</sup> = 1, *R*<sup>2</sup> = 2, *R*<sup>3</sup> = 6, *R*<sup>4</sup> = 3, and *R*<sup>5</sup> = 2, with *T* = 5. What are *G*0, *G*1, *...*, *G*5? Hint: Work backwards. ⇤

*Exercise 3.9* Suppose = 0*.*9 and the reward sequence is *R*<sup>1</sup> = 2 followed by an infinite sequence of 7s. What are *G*<sup>1</sup> and *G*0? ⇤

*Exercise 3.10* Prove the second equality in [\(3.10\)](#page-41-1). ⇤

### <span id="page-43-0"></span>3.4 Unified Notation for Episodic and Continuing Tasks

In the preceding section we described two kinds of reinforcement learning tasks, one in which the agent–environment interaction naturally breaks down into a sequence of separate episodes (episodic tasks), and one in which it does not (continuing tasks). The former case is mathematically easier because each action a↵ects only the finite number of rewards subsequently received during the episode. In this book we consider sometimes one kind of problem and sometimes the other, but often both. It is therefore useful to establish one notation that enables us to talk precisely about both cases simultaneously.

To be precise about episodic tasks requires some additional notation. Rather than one long sequence of time steps, we need to consider a series of episodes, each of which consists of a finite sequence of time steps. We number the time steps of each episode starting anew from zero. Therefore, we have to refer not just to *St*, the state representation at time *t*, but to *St,i*, the state representation at time *t* of episode *i* (and similarly for *At,i*, *Rt,i*, ⇡*t,i*, *Ti*, etc.). However, it turns out that when we discuss episodic tasks we almost never have to distinguish between di↵erent episodes. We are almost always considering a particular episode, or stating something that is true for all episodes. Accordingly, in practice we almost always abuse notation slightly by dropping the explicit reference to episode number. That is, we write *S<sup>t</sup>* to refer to *St,i*, and so on.

We need one other convention to obtain a single notation that covers both episodic and continuing tasks. We have defined the return as a sum over a finite number of terms in one case [\(3.7\)](#page-40-4) and as a sum over an infinite number of terms in the other [\(3.8\)](#page-41-0). These two can be unified by considering episode termination to be the entering of a special *absorbing state* that transitions only to itself and that generates only rewards of zero. For example, consider the state transition diagram:

![](_page_43_Figure_6.jpeg)

Here the solid square represents the special absorbing state corresponding to the end of an episode. Starting from *S*0, we get the reward sequence +1*,* +1*,* +1*,* 0*,* 0*,* 0*,...*. Summing these, we get the same return whether we sum over the first *T* rewards (here *T* = 3) or over the full infinite sequence. This remains true even if we introduce discounting. Thus, we can define the return, in general, according to [\(3.8\)](#page-41-0), using the convention of omitting episode numbers when they are not needed, and including the possibility that = 1 if the sum remains defined (e.g., because all episodes terminate). Alternatively, we can write

$$G_t \doteq \sum_{k=t+1}^{T} \gamma^{k-t-1} R_k, \tag{3.11}$$

including the possibility that *T* = 1 or = 1 (but not both). We use these conventions throughout the rest of the book to simplify notation and to express the close parallels between episodic and continuing tasks. (Later, in Chapter 10, we will introduce a formulation that is both continuing and undiscounted.)

### <span id="page-44-0"></span>3.5 Policies and Value Functions

Almost all reinforcement learning algorithms involve estimating *value functions*—functions of states (or of state–action pairs) that estimate *how good* it is for the agent to be in a given state (or how good it is to perform a given action in a given state). The notion of "how good" here is defined in terms of future rewards that can be expected, or, to be precise, in terms of expected return. Of course the rewards the agent can expect to receive in the future depend on what actions it will take. Accordingly, value functions are defined with respect to particular ways of acting, called policies.

Formally, a *policy* is a mapping from states to probabilities of selecting each possible action. If the agent is following policy ⇡ at time *t*, then ⇡(*a|s*) is the probability that *A<sup>t</sup>* = *a* if *S<sup>t</sup>* = *s*. Like *p*, ⇡ is an ordinary function; the "*|*" in the middle of ⇡(*a|s*) merely reminds us that it defines a probability distribution over *a* 2 A(*s*) for each *s* 2 S. Reinforcement learning methods specify how the agent's policy is changed as a result of its experience.

*Exercise 3.11* If the current state is *St*, and actions are selected according to a stochastic policy ⇡, then what is the expectation of *Rt*+1 in terms of ⇡ and the four-argument function *p* [\(3.2\)](#page-34-4)? ⇤

The *value function* of a state *s* under a policy ⇡, denoted *v*⇡(*s*), is the expected return when starting in *s* and following ⇡ thereafter. For MDPs, we can define *v*⇡ formally by

$$v_{\pi}(s) \doteq \mathbb{E}_{\pi}[G_t \mid S_t = s] = \mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s\right], \text{ for all } s \in \mathcal{S},$$
 (3.12)

where E⇡[*·*] denotes the expected value of a random variable given that the agent follows policy ⇡, and *t* is any time step. Note that the value of the terminal state, if any, is always zero. We call the function *v*⇡ the *state-value function for policy* ⇡.

Similarly, we define the value of taking action *a* in state *s* under a policy ⇡, denoted *q*⇡(*s, a*), as the expected return starting from *s*, taking the action *a*, and thereafter following policy ⇡:

$$q_{\pi}(s,a) \doteq \mathbb{E}_{\pi}[G_t \mid S_t = s, A_t = a] = \mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s, A_t = a\right].$$
 (3.13)

We call *q*⇡ the *action-value function for policy* ⇡.

*Exercise 3.12* Give an equation for *v*⇡ in terms of *q*⇡ and ⇡. ⇤

*Exercise 3.13* Give an equation for *q*⇡ in terms of *v*⇡ and the four-argument *p*. ⇤

The value functions *v*⇡ and *q*⇡ can be estimated from experience. For example, if an agent follows policy ⇡ and maintains an average, for each state encountered, of the actual returns that have followed that state, then the average will converge to the state's value, *v*⇡(*s*), as the number of times that state is encountered approaches infinity. If separate

averages are kept for each action taken in each state, then these averages will similarly converge to the action values, *q*⇡(*s, a*). We call estimation methods of this kind *Monte Carlo methods* because they involve averaging over many random samples of actual returns. These kinds of methods are presented in Chapter 5. Of course, if there are very many states, then it may not be practical to keep separate averages for each state individually. Instead, the agent would have to maintain *v*⇡ and *q*⇡ as parameterized functions (with fewer parameters than states) and adjust the parameters to better match the observed returns. This can also produce accurate estimates, although much depends on the nature of the parameterized function approximator. These possibilities are discussed in Part II of the book.

A fundamental property of value functions used throughout reinforcement learning and dynamic programming is that they satisfy recursive relationships similar to that which we have already established for the return [\(3.9\)](#page-41-2). For any policy ⇡ and any state *s*, the following consistency condition holds between the value of *s* and the value of its possible successor states:

$$v_{\pi}(s) \doteq \mathbb{E}_{\pi}[G_{t} \mid S_{t} = s]$$

$$= \mathbb{E}_{\pi}[R_{t+1} + \gamma G_{t+1} \mid S_{t} = s]$$

$$= \sum_{a} \pi(a|s) \sum_{s'} \sum_{r} p(s', r|s, a) \Big[ r + \gamma \mathbb{E}_{\pi}[G_{t+1}|S_{t+1} = s'] \Big]$$

$$= \sum_{a} \pi(a|s) \sum_{s', r} p(s', r|s, a) \Big[ r + \gamma v_{\pi}(s') \Big], \text{ for all } s \in \mathcal{S},$$
(3.14)

where it is implicit that the actions, *a*, are taken from the set A(*s*), that the next states, *s*0 , are taken from the set S (or from S<sup>+</sup> in the case of an episodic problem), and that the rewards, *r*, are taken from the set R. Note also how in the last equation we have merged the two sums, one over all the values of *s*<sup>0</sup> and the other over all the values of *r*, into one sum over all the possible values of both. We use this kind of merged sum often to simplify formulas. Note how the final expression can be read easily as an expected value. It is really a sum over all values of the three variables, *a*, *s*<sup>0</sup> , and *r*. For each triple, we compute its probability, ⇡(*a|s*)*p*(*s*<sup>0</sup> *, r|s, a*), weight the quantity in brackets by that probability, then sum over all possibilities to get an expected value.

Equation [\(3.14\)](#page-45-0) is the *Bellman equation for v*⇡. It expresses a relationship between the value of a state and the values of its successor states. Think of looking ahead from a state to its possible successor states, as suggested by the diagram to the right. Each open circle represents a state and each solid circle represents a state–action pair. Starting from state *s*, the root node at the top, the agent could take any of some set of actions three are shown in the diagram—based on its policy ⇡. From

<span id="page-45-0"></span>![](_page_45_Picture_7.jpeg)

Backup diagram for *v*⇡

each of these, the environment could respond with one of several next states, *s*<sup>0</sup> (two are shown in the figure), along with a reward, *r*, depending on its dynamics given by the function *p*. The Bellman equation [\(3.14\)](#page-45-0) averages over all the possibilities, weighting each by its probability of occurring. It states that the value of the start state must equal the (discounted) value of the expected next state, plus the reward expected along the way.

The value function *v*⇡ is the unique solution to its Bellman equation. We show in subsequent chapters how this Bellman equation forms the basis of a number of ways to compute, approximate, and learn *v*⇡. We call diagrams like that above *backup diagrams* because they diagram relationships that form the basis of the update or *backup* operations that are at the heart of reinforcement learning methods. These operations transfer value information *back* to a state (or a state–action pair) from its successor states (or state–action pairs). We use backup diagrams throughout the book to provide graphical summaries of the algorithms we discuss. (Note that, unlike transition graphs, the state nodes of backup diagrams do not necessarily represent distinct states; for example, a state might be its own successor.) of the special states A and B. From state A, all four actions yield a reward of +10 and take the agent to A . From state B, all actions yield a reward of +5 and take the agent to B . Suppose the agent selects all four actions with equal probability in all states. Figure 3.5b shows the value function, *v*⇡, for this policy, for the discounted reward case with = 0*.*9. This value function was computed by solving the system of equations (3.10). Notice the negative values near the lower edge; these are the result of the high probability of hitting the edge of the grid

<span id="page-46-1"></span>Example 3.5: Gridworld [Figure 3.2](#page-46-0) (left) shows a rectangular gridworld representation of a simple finite MDP. The cells of the grid correspond to the states of the environment. At each cell, four actions are possible: north, south, east, and west, which deterministically cause the agent to move one cell in the respective direction on the grid. Actions that would take the agent o↵ the grid leave its location unchanged, but also result in a reward of 1. Other actions result in a reward of 0, except those that move the agent out of the special states A and B. From state A, all four actions yield a reward of +10 and take the agent to A<sup>0</sup> . From state B, all actions yield a reward of +5 and take the agent to B<sup>0</sup> . there under the random policy. State A is the best state to be in under this policy, but its expected return is less than 10, its immediate reward, because from A the agent is taken to A , from which it is likely to run into the edge of the grid. State B, on the other hand, is valued more than 5, its immediate reward, because from B the agent is taken to B , which has a positive value. From B the expected penalty (negative reward) for possibly running into an edge is more

<span id="page-46-0"></span>![](_page_46_Figure_4.jpeg)

(a) (b) Figure 3.2: Gridworld example: exceptional reward dynamics (left) and state-value function for the equiprobable random policy (right).

Figure 3.5: Grid example: (a) exceptional reward dynamics; (b) state-value

function for the equiprobable random policy. Suppose the agent selects all four actions with equal probability in all states. [Figure 3.2](#page-46-0) (right) shows the value function, *v*⇡, for this policy, for the discounted reward case with = 0*.*9. This value function was computed by solving the system of linear equations [\(3.14\)](#page-45-0). Notice the negative values near the lower edge; these are the result of the high probability of hitting the edge of the grid there under the random policy. State A is the best state to be in under this policy. Note that A's expected return is *less* than its immediate reward of 10, because from A the agent is taken to state A<sup>0</sup> from which it is likely to run into the edge of the grid. State B, on the other hand, is valued *more* than its immediate reward of 5, because from B the agent is taken to B0 which has a positive value. From B0 the expected penalty (negative reward) for possibly running into an edge is more than compensated for by the expected gain for possibly stumbling onto A or B.

*Exercise 3.14* The Bellman equation [\(3.14\)](#page-45-0) must hold for each state for the value function *v*⇡ shown in [Figure 3.2](#page-46-0) (right) of [Example 3.5.](#page-46-1) Show numerically that this equation holds for the center state, valued at +0*.*7, with respect to its four neighboring states, valued at +2*.*3, +0*.*4, 0*.*4, and +0*.*7. (These numbers are accurate only to one decimal place.) ⇤

*Exercise 3.15* In the gridworld example, rewards are positive for goals, negative for running into the edge of the world, and zero the rest of the time. Are the signs of these rewards important, or only the intervals between them? Prove, using [\(3.8\)](#page-41-0), that adding a constant *c* to all the rewards adds a constant, *vc*, to the values of all states, and thus does not a↵ect the relative values of any states under any policies. What is *v<sup>c</sup>* in terms of *c* and ? ⇤

*Exercise 3.16* Now consider adding a constant *c* to all the rewards in an episodic task, such as maze running. Would this have any e↵ect, or would it leave the task unchanged as in the continuing task above? Why or why not? Give an example. ⇤

Example 3.6: Golf To formulate playing a hole of golf as a reinforcement learning task, we count a penalty (negative reward) of 1 for each stroke until we hit the ball into the hole. The state is the location of the ball. The value of a state is the negative of the number of strokes to the hole from that location. Our actions are how we aim and swing at the ball, of course, and which club we select. Let us take the former as given and consider just the choice of club, which we assume is either a putter or a driver. The upper part of [Figure 3.3](#page-47-0) shows a possible state-value function, *v*putt(*s*), for the policy that

always uses the putter. The terminal state *in-the-hole* has a value of 0. From anywhere on the green we assume we can make a putt; these states have value 1. O↵ the green we cannot reach the hole by putting, and the value is lower. If we can reach the green from a state by putting, then that state must have value one less than the green's value, that is, 2. For simplicity, let us assume we can putt very precisely and deterministically, but with a limited range. This gives us the sharp contour line labeled 2 in the figure; all locations between that line and the green require exactly two strokes to complete the hole. Similarly, any location within putting range of the 2 contour line must have a value of 3, and so on to get all the contour lines shown in the figure. Putting doesn't get us out of sand traps, so they have a value of 1. Overall, it takes us six strokes to get from the tee to the hole by putting.

<span id="page-47-0"></span>![](_page_47_Picture_6.jpeg)

Figure 3.3: A golf example: the state-value function for putting (upper) and the optimal actionvalue function for using the driver (lower).

*Exercise 3.17* What is the Bellman equation for action values, that is, for *q*⇡? It must give the action value *q*⇡(*s, a*) in terms of the action values, *q*⇡(*s*<sup>0</sup> *, a*<sup>0</sup> ), of possible successors to the state–action pair (*s, a*). Hint: The backup diagram to the right corresponds to this equation. Show the sequence of equations analogous to [\(3.14\)](#page-45-0), but for action values. ⇤

![](_page_47_Picture_9.jpeg)

<span id="page-48-1"></span>*Exercise 3.18* The value of a state depends on the values of the actions possible in that state and on how likely each action is to be taken under the current policy. We can think of this in terms of a small backup diagram rooted at the state and considering each possible action:

![](_page_48_Figure_3.jpeg)

Give the equation corresponding to this intuition and diagram for the value at the root node, *v*⇡(*s*), in terms of the value at the expected leaf node, *q*⇡(*s, a*), given *S<sup>t</sup>* = *s*. This equation should include an expectation conditioned on following the policy, ⇡. Then give a second equation in which the expected value is written out explicitly in terms of ⇡(*a|s*) such that no expected value notation appears in the equation. ⇤

<span id="page-48-2"></span>*Exercise 3.19* The value of an action, *q*⇡(*s, a*), depends on the expected next reward and the expected sum of the remaining rewards. Again we can think of this in terms of a small backup diagram, this one rooted at an action (state–action pair) and branching to the possible next states:

![](_page_48_Figure_6.jpeg)

Give the equation corresponding to this intuition and diagram for the action value, *q*⇡(*s, a*), in terms of the expected next reward, *Rt*+1, and the expected next state value, *v*⇡(*St*+1), given that *S<sup>t</sup>* =*s* and *A<sup>t</sup>* =*a*. This equation should include an expectation but *not* one conditioned on following the policy. Then give a second equation, writing out the expected value explicitly in terms of *p*(*s*<sup>0</sup> *, r|s, a*) defined by [\(3.2\)](#page-34-4), such that no expected value notation appears in the equation. ⇤

### <span id="page-48-0"></span>3.6 Optimal Policies and Optimal Value Functions

Solving a reinforcement learning task means, roughly, finding a policy that achieves a lot of reward over the long run. For finite MDPs, we can precisely define an optimal policy in the following way. Value functions define a partial ordering over policies. A policy ⇡ is defined to be better than or equal to a policy ⇡<sup>0</sup> if its expected return is greater than or equal to that of ⇡<sup>0</sup> for all states. In other words, ⇡ ⇡<sup>0</sup> if and only if *v*⇡(*s*) *v*⇡<sup>0</sup> (*s*) for all *s* 2 S. There is always at least one policy that is better than or equal to all other policies. This is an *optimal policy*. Although there may be more than one, we denote all the optimal policies by ⇡⇤. They share the same state-value function, called the *optimal state-value function*, denoted *v*⇤, and defined as

$$v_*(s) \doteq \max_{\pi} v_{\pi}(s), \tag{3.15}$$

for all *s* 2 S.

Optimal policies also share the same *optimal action-value function*, denoted *q*⇤, and defined as

$$q_*(s,a) \doteq \max_{\pi} q_{\pi}(s,a), \tag{3.16}$$

for all *s* 2 S and *a* 2 A(*s*). For the state–action pair (*s, a*), this function gives the expected return for taking action *a* in state *s* and thereafter following an optimal policy. Thus, we can write *q*⇤ in terms of *v*⇤ as follows:

$$q_*(s,a) = \mathbb{E}[R_{t+1} + \gamma v_*(S_{t+1}) \mid S_t = s, A_t = a]. \tag{3.17}$$

Example 3.7: Optimal Value Functions for Golf The lower part of [Figure 3.3](#page-47-0) shows the contours of a possible optimal action-value function *q*⇤(*s,* driver). These are the values of each state if we first play a stroke with the driver and afterward select either the driver or the putter, whichever is better. The driver enables us to hit the ball farther, but with less accuracy. We can reach the hole in one shot using the driver only if we are already very close; thus the 1 contour for *q*⇤(*s,* driver) covers only a small portion of the green. If we have two strokes, however, then we can reach the hole from much farther away, as shown by the 2 contour. In this case we don't have to drive all the way to within the small 1 contour, but only to anywhere on the green; from there we can use the putter. The optimal action-value function gives the values after committing to a particular *first* action, in this case, to the driver, but afterward using whichever actions are best. The 3 contour is still farther out and includes the starting tee. From the tee, the best sequence of actions is two drives and one putt, sinking the ball in three strokes.

Because *v*⇤ is the value function for a policy, it must satisfy the self-consistency condition given by the Bellman equation for state values [\(3.14\)](#page-45-0). Because it is the optimal value function, however, *v*⇤'s consistency condition can be written in a special form without reference to any specific policy. This is the Bellman equation for *v*⇤, or the *Bellman optimality equation*. Intuitively, the Bellman optimality equation expresses the fact that the value of a state under an optimal policy must equal the expected return for the best action from that state:

$$v_{*}(s) = \max_{a \in \mathcal{A}(s)} q_{\pi_{*}}(s, a)$$

$$= \max_{a} \mathbb{E}_{\pi_{*}}[G_{t} \mid S_{t} = s, A_{t} = a]$$

$$= \max_{a} \mathbb{E}_{\pi_{*}}[R_{t+1} + \gamma G_{t+1} \mid S_{t} = s, A_{t} = a]$$

$$= \max_{a} \mathbb{E}[R_{t+1} + \gamma v_{*}(S_{t+1}) \mid S_{t} = s, A_{t} = a]$$
(by (3.9))
$$= \max_{a} \mathbb{E}[R_{t+1} + \gamma v_{*}(S_{t+1}) \mid S_{t} = s, A_{t} = a]$$
(3.18)

<span id="page-49-0"></span>
$$= \max_{a} \sum_{s',r} p(s',r|s,a) [r + \gamma v_*(s')].$$
 (3.19)

The last two equations are two forms of the Bellman optimality equation for *v*⇤. The Bellman optimality equation for *q*⇤ is

<span id="page-50-0"></span>
$$q_{*}(s,a) = \mathbb{E}\left[R_{t+1} + \gamma \max_{a'} q_{*}(S_{t+1}, a') \mid S_{t} = s, A_{t} = a\right]$$

$$= \sum_{s',r} p(s', r \mid s, a) \left[r + \gamma \max_{a'} q_{*}(s', a')\right]. \tag{3.20}$$

The backup diagrams in the figure below show graphically the spans of future states and actions considered in the Bellman optimality equations for *v*⇤ and *q*⇤. These are the same as the backup diagrams for *v*⇡ and *q*⇡ presented earlier except that arcs have been added at the agent's choice points to represent that the maximum over that choice is taken rather than the expected value given some policy. The backup diagram on the left graphically represents the Bellman optimality equation [\(3.19\)](#page-49-0) and the backup diagram on the right graphically represents [\(3.20\)](#page-50-0).

![](_page_50_Figure_5.jpeg)

Figure 3.4: Backup diagrams for *v*⇤ and *q*⇤

For finite MDPs, the Bellman optimality equation for *v*⇤ [\(3.19\)](#page-49-0) has a unique solution. The Bellman optimality equation is actually a system of equations, one for each state, so if there are *n* states, then there are *n* equations in *n* unknowns. If the dynamics *p* of the environment are known, then in principle one can solve this system of equations for *v*⇤ using any one of a variety of methods for solving systems of nonlinear equations. One can solve a related set of equations for *q*⇤.

Once one has *v*⇤, it is relatively easy to determine an optimal policy. For each state *s*, there will be one or more actions at which the maximum is obtained in the Bellman optimality equation. Any policy that assigns nonzero probability only to these actions is an optimal policy. You can think of this as a one-step search. If you have the optimal value function, *v*⇤, then the actions that appear best after a one-step search will be optimal actions. Another way of saying this is that any policy that is *greedy* with respect to the optimal evaluation function *v*⇤ is an optimal policy. The term greedy is used in computer science to describe any search or decision procedure that selects alternatives based only on local or immediate considerations, without considering the possibility that such a selection may prevent future access to even better alternatives. Consequently, it describes policies that select actions based only on their short-term consequences. The beauty of *v*⇤ is that if one uses it to evaluate the short-term consequences of actions—specifically, the one-step consequences—then a greedy policy is actually optimal in the long-term sense in which we are interested because *v*⇤ already takes into account the reward consequences of all possible future behavior. By means of *v*⇤, the optimal expected long-term return is

turned into a quantity that is locally and immediately available for each state. Hence, a one-step-ahead search yields the long-term optimal actions.

Having *q*⇤ makes choosing optimal actions even easier. With *q*⇤, the agent does not even have to do a one-step-ahead search: for any state *s*, it can simply find any action that maximizes *q*⇤(*s, a*). The action-value function e↵ectively caches the results of all one-step-ahead searches. It provides the optimal expected long-term return as a value that is locally and immediately available for each state–action pair. Hence, at the cost of representing a function of state–action pairs, instead of just of states, the optimal actionvalue function allows optimal actions to be selected without having to know anything about possible successor states and their values, that is, without having to know anything about the environment's dynamics.

Example 3.8: Solving the Gridworld Suppose we solve the Bellman equation for *v*⇤ for the simple grid task introduced in [Example 3.5](#page-46-1) and shown again in [Figure 3.5](#page-51-0) (left). Recall that state A is followed by a reward of +10 and transition to state A0 , while state B is followed by a reward of +5 and transition to state B0 . [Figure 3.5](#page-51-0) (middle) shows the optimal value function, and [Figure 3.5](#page-51-0) (right) shows the corresponding optimal policies. Where there are multiple arrows in a cell, all of the corresponding actions are optimal.

<span id="page-51-0"></span>![](_page_51_Figure_5.jpeg)

Figure 3.5: Optimal solutions to the gridworld example.

Example 3.9: Bellman Optimality Equations for the Recycling Robot Using [\(3.19\)](#page-49-0), we can explicitly give the Bellman optimality equation for the recycling robot example. To make things more compact, we abbreviate the states high and low, and the actions search, wait, and recharge respectively by h, l, s, w, and re. Because there are only two states, the Bellman optimality equation consists of two equations. The equation for *v*⇤(h) can be written as follows:

$$\begin{array}{lll} v_*(\mathbf{h}) & = & \max \left\{ \begin{array}{l} p(\mathbf{h} | \mathbf{h}, \mathbf{s})[r(\mathbf{h}, \mathbf{s}, \mathbf{h}) + \gamma v_*(\mathbf{h})] + p(\mathbf{1} | \mathbf{h}, \mathbf{s})[r(\mathbf{h}, \mathbf{s}, \mathbf{1}) + \gamma v_*(\mathbf{1})], \\ p(\mathbf{h} | \mathbf{h}, \mathbf{w})[r(\mathbf{h}, \mathbf{w}, \mathbf{h}) + \gamma v_*(\mathbf{h})] + p(\mathbf{1} | \mathbf{h}, \mathbf{w})[r(\mathbf{h}, \mathbf{w}, \mathbf{1}) + \gamma v_*(\mathbf{1})], \\ \end{array} \right\} \\ & = & \max \left\{ \begin{array}{l} \alpha[r_{\mathbf{s}} + \gamma v_*(\mathbf{h})] + (1 - \alpha)[r_{\mathbf{s}} + \gamma v_*(\mathbf{1})], \\ 1[r_{\mathbf{w}} + \gamma v_*(\mathbf{h})] + 0[r_{\mathbf{w}} + \gamma v_*(\mathbf{1})], \\ \end{array} \right\} \\ & = & \max \left\{ \begin{array}{l} r_{\mathbf{s}} + \gamma[\alpha v_*(\mathbf{h}) + (1 - \alpha)v_*(\mathbf{1})], \\ r_{\mathbf{w}} + \gamma v_*(\mathbf{h}) \end{array} \right\}. \end{array}$$

Following the same procedure for *v*⇤(l) yields the equation

$$v_*(\mathbf{1}) = \max \left\{ \begin{array}{l} \beta r_{\mathrm{s}} - 3(1-\beta) + \gamma[(1-\beta)v_*(\mathbf{h}) + \beta v_*(\mathbf{1})], \\ r_{\mathrm{w}} + \gamma v_*(\mathbf{1}), \\ \gamma v_*(\mathbf{h}) \end{array} \right\}.$$

For any choice of *r*s, *r*w, ↵, , and , with 0 *<* 1, 0 ↵*,* 1, there is exactly one pair of numbers, *v*⇤(h) and *v*⇤(l), that simultaneously satisfy these two nonlinear equations.

Explicitly solving the Bellman optimality equation provides one route to finding an optimal policy, and thus to solving the reinforcement learning problem. However, this solution is rarely directly useful. It is akin to an exhaustive search, looking ahead at all possibilities, computing their probabilities of occurrence and their desirabilities in terms of expected rewards. This solution relies on at least three assumptions that are rarely true in practice: (1) the dynamics of the environment are accurately known; (2) computational resources are sucient to complete the calculation; and (3) the states have the Markov property. For the kinds of tasks in which we are interested, one is generally not able to implement this solution exactly because various combinations of these assumptions are violated. For example, although the first and third assumptions present no problems for the game of backgammon, the second is a major impediment. Because the game has about 10<sup>20</sup> states, it would take thousands of years on today's fastest computers to solve the Bellman equation for *v*⇤, and the same is true for finding *q*⇤. In reinforcement learning one typically has to settle for approximate solutions.

Many di↵erent decision-making methods can be viewed as ways of approximately solving the Bellman optimality equation. For example, heuristic search methods can be viewed as expanding the right-hand side of [\(3.19\)](#page-49-0) several times, up to some depth, forming a "tree" of possibilities, and then using a heuristic evaluation function to approximate *v*⇤ at the "leaf" nodes. (Heuristic search methods such as A⇤ are almost always based on the episodic case.) The methods of dynamic programming can be related even more closely to the Bellman optimality equation. Many reinforcement learning methods can be clearly understood as approximately solving the Bellman optimality equation, using actual experienced transitions in place of knowledge of the expected transitions. We consider a variety of such methods in the following chapters.

*Exercise 3.20* Draw or describe the optimal state-value function for the golf example. ⇤

*Exercise 3.21* Draw or describe the contours of the optimal action-value function for putting, *q*⇤(*s,* putter), for the golf example. ⇤

*Exercise 3.22* Consider the continuing MDP shown to the right. The only decision to be made is that in the top state, where two actions are available, left and right. The numbers show the rewards that are received deterministically after each action. There are exactly two deterministic policies, ⇡left and ⇡right. What policy is optimal if = 0? If = 0*.*9? If = 0*.*5? ⇤

![](_page_52_Picture_10.jpeg)

![](_page_53_Figure_2.jpeg)

#### <span id="page-53-0"></span>3.7 Optimality and Approximation

We have defined optimal value functions and optimal policies. Clearly, an agent that learns an optimal policy has done very well, but in practice this rarely happens. For the kinds of tasks in which we are interested, optimal policies can be generated only with extreme computational cost. A well-defined notion of optimality organizes the approach to learning we describe in this book and provides a way to understand the theoretical properties of various learning algorithms, but it is an ideal that agents can only approximate. As we discussed above, even if we have a complete and accurate model of the environment's dynamics, it is usually not possible to simply compute an optimal policy by solving the Bellman optimality equation. For example, board games such as chess are a tiny fraction of human experience, yet large, custom-designed computers still cannot compute the optimal moves. A critical aspect of the problem facing the agent is always the computational power available to it, in particular, the amount of computation it can perform in a single time step.

The memory available is also an important constraint. A large amount of memory is often required to build up approximations of value functions, policies, and models. In tasks with small, finite state sets, it is possible to form these approximations using arrays or tables with one entry for each state (or state–action pair). This we call the *tabular* case, and the corresponding methods we call tabular methods. In many cases of practical interest, however, there are far more states than could possibly be entries in a table. In these cases the functions must be approximated, using some sort of more compact parameterized function representation.

Our framing of the reinforcement learning problem forces us to settle for approximations. However, it also presents us with some unique opportunities for achieving useful approximations. For example, in approximating optimal behavior, there may be many states that the agent faces with such a low probability that selecting suboptimal actions for them has little impact on the amount of reward the agent receives. Tesauro's backgammon player, for example, plays with exceptional skill even though it might make

very bad decisions on board configurations that never occur in games against experts. In fact, it is possible that TD-Gammon makes bad decisions for a large fraction of the game's state set. The online nature of reinforcement learning makes it possible to approximate optimal policies in ways that put more e↵ort into learning to make good decisions for frequently encountered states, at the expense of less e↵ort for infrequently encountered states. This is one key property that distinguishes reinforcement learning from other approaches to approximately solving MDPs.

#### <span id="page-54-0"></span>3.8 Summary

Let us summarize the elements of the reinforcement learning problem that we have presented in this chapter. Reinforcement learning is about learning from interaction how to behave in order to achieve a goal. The reinforcement learning *agent* and its *environment* interact over a sequence of discrete time steps. The specification of their interface defines a particular task: the *actions* are the choices made by the agent; the *states* are the basis for making the choices; and the *rewards* are the basis for evaluating the choices. Everything inside the agent is known and controllable. Its environment, on the other hand, is incompletely controllable and may or may not be completely known. A *policy* is a stochastic rule by which the agent selects actions as a function of states. The agent's objective is to maximize the amount of reward it receives over time.

When the reinforcement learning setup described above is formulated with well defined transition probabilities it constitutes a *Markov decision process* (MDP). A *finite MDP* is an MDP with finite state, action, and (as we formulate it here) reward sets. Much of the current theory of reinforcement learning is restricted to finite MDPs, but the methods and ideas apply more generally.

The *return* is the function of future rewards that the agent seeks to maximize (in expected value). It has several di↵erent definitions depending upon the nature of the task and whether one wishes to *discount* delayed reward. The undiscounted formulation is appropriate for *episodic tasks*, in which the agent–environment interaction breaks naturally into *episodes*; the discounted formulation is appropriate for tabular *continuing tasks*, in which the interaction does not naturally break into episodes but continues without limit (but see Sections 10.3–4). We try to define the returns for the two kinds of tasks such that one set of equations can apply to both the episodic and continuing cases.

A policy's *value functions* (*v*⇡ and *q*⇡) assign to each state, or state–action pair, the expected return from that state, or state–action pair, given that the agent uses the policy. The *optimal value functions* (*v*⇤ and *q*⇤) assign to each state, or state–action pair, the largest expected return achievable by any policy. A policy whose value functions are optimal is an *optimal policy*. Whereas the optimal value functions for states and state–action pairs are unique for a given MDP, there can be many optimal policies. Any policy that is *greedy* with respect to the optimal value functions must be an optimal policy. The *Bellman optimality equations* are special consistency conditions that the optimal value functions must satisfy and that can, in principle, be solved for the optimal value functions, from which an optimal policy can be determined with relative ease.

*3.8. Summary 69*

A reinforcement learning problem can be posed in a variety of di↵erent ways depending on assumptions about the level of knowledge initially available to the agent. In problems of *complete knowledge*, the agent has a complete and accurate model of the environment's dynamics. If the environment is an MDP, then such a model consists of the complete fourargument dynamics function *p* [\(3.2\)](#page-34-4). In problems of *incomplete knowledge*, a complete and perfect model of the environment is not available.

Even if the agent had a complete and accurate environment model, the agent would typically be unable to fully use it because of limitations on its memory and computation per time step. In particular, extensive memory may be required to build up accurate approximations of value functions, policies, and models. In most cases of practical interest there are far more states than could possibly be entries in a table, and approximations must be made.

A well-defined notion of optimality organizes the approach to learning we describe in this book and provides a way to understand the theoretical properties of various learning algorithms, but it is an ideal that reinforcement learning agents can only approximate to varying degrees. In reinforcement learning we are very much concerned with cases in which optimal solutions cannot be found but must be approximated in some way.

### Bibliographical and Historical Remarks

The reinforcement learning problem is deeply indebted to the idea of Markov decision processes (MDPs) from the field of optimal control. These historical influences and other major influences from psychology are described in the brief history given in [Chapter 1.](#page-10-0) Reinforcement learning adds to MDPs a focus on approximation and incomplete information for realistically large problems. MDPs and the reinforcement learning problem are only weakly linked to traditional learning and decision-making problems in artificial intelligence. However, artificial intelligence is now vigorously exploring MDP formulations for planning and decision making from a variety of perspectives. MDPs are more general than previous formulations used in artificial intelligence in that they permit more general kinds of goals and uncertainty.

The theory of MDPs is treated by, for example, Bertsekas (2005), White (1969), Whittle (1982, 1983), and Puterman (1994). A particularly compact treatment of the finite case is given by Ross (1983). MDPs are also studied under the heading of stochastic optimal control, where *adaptive* optimal control methods are most closely related to reinforcement learning (e.g., Kumar, 1985; Kumar and Varaiya, 1986).

The theory of MDPs evolved from e↵orts to understand the problem of making sequences of decisions under uncertainty, where each decision can depend on the previous decisions and their outcomes. It is sometimes called the theory of multistage decision processes, or sequential decision processes, and has roots in the statistical literature on sequential sampling beginning with the papers by Thompson (1933, 1934) and Robbins (1952) that we cited in Chapter 2 in connection with bandit problems (which are prototypical MDPs if formulated as multiple-situation problems).

The earliest instance (that we are aware of) in which reinforcement learning was discussed using the MDP formalism is Andreae's (1969) description of a unified view of learning machines. Witten and Corbin (1973) experimented with a reinforcement learning system later analyzed by Witten (1977, 1976a) using the MDP formalism. Although he did not explicitly mention MDPs, Werbos (1977) suggested approximate solution methods for stochastic optimal control problems that are related to modern reinforcement learning methods (see also Werbos, 1982, 1987, 1988, 1989, 1992). Although Werbos's ideas were not widely recognized at the time, they were prescient in emphasizing the importance of approximately solving optimal control problems in a variety of domains, including artificial intelligence. The most influential integration of reinforcement learning and MDPs is due to Watkins (1989).

3.1 Our characterization of the dynamics of an MDP in terms of *p*(*s*<sup>0</sup> *, r|s, a*) is slightly unusual. It is more common in the MDP literature to describe the dynamics in terms of the state transition probabilities *p*(*s*<sup>0</sup> *|s, a*) and expected next rewards *r*(*s, a*). In reinforcement learning, however, we more often have to refer to individual actual or sample rewards (rather than just their expected values). Our notation also makes it plainer that *S<sup>t</sup>* and *R<sup>t</sup>* are in general jointly determined, and thus must have the same time index. In teaching reinforcement learning, we have found our notation to be more straightforward conceptually and easier to understand.

For a good intuitive discussion of the system-theoretic concept of state, see Minsky (1967).

The bioreactor example is based on the work of Ungar (1990) and Miller and Williams (1992). The recycling robot example was inspired by the can-collecting robot built by Jonathan Connell (1989). Kober and Peters (2012) present a collection of robotics applications of reinforcement learning.

- 3.2 An explicit statement of the reward hypothesis was suggested by Michael Littman (personal communication).
- 3.3–4 The terminology of *episodic* and *continuing* tasks is di↵erent from that usually used in the MDP literature. In that literature it is common to distinguish three types of tasks: (1) finite-horizon tasks, in which interaction terminates after a particular *fixed* number of time steps; (2) indefinite-horizon tasks, in which interaction can last arbitrarily long but must eventually terminate; and (3) infinite-horizon tasks, in which interaction does not terminate. Our episodic and continuing tasks are similar to indefinite-horizon and infinite-horizon tasks, respectively, but we prefer to emphasize the di↵erence in the nature of the interaction. This di↵erence seems more fundamental than the di↵erence in the objective functions emphasized by the usual terms. Often episodic tasks use an indefinite-horizon objective function and continuing tasks an infinite-horizon objective function, but we see this as a common coincidence rather than a fundamental di↵erence.

The pole-balancing example is from Michie and Chambers (1968) and Barto, Sutton, and Anderson (1983).

*3.8. Summary 71*

3.5–6 Assigning value on the basis of what is good or bad in the long run has ancient roots. In control theory, mapping states to numerical values representing the long-term consequences of control decisions is a key part of optimal control theory, which was developed in the 1950s by extending nineteenth century state-function theories of classical mechanics (see, for example, Schultz and Melsa, 1967). In describing how a computer could be programmed to play chess, Shannon (1950) suggested using an evaluation function that took into account the long-term advantages and disadvantages of chess positions.

Watkins's (1989) Q-learning algorithm for estimating *q*⇤ (Chapter 6) made actionvalue functions an important part of reinforcement learning, and consequently these functions are often called "Q-functions." But the idea of an action-value function is much older than this. Shannon (1950) suggested that a function *h*(*P,M*) could be used by a chess-playing program to decide whether a move *M* in position *P* is worth exploring. Michie's (1961, 1963) MENACE system and Michie and Chambers's (1968) BOXES system can be understood as estimating action-value functions. In classical physics, Hamilton's principal function is an action-value function; Newtonian dynamics are greedy with respect to this function (e.g., Goldstein, 1957). Action-value functions also played a central role in Denardo's (1967) theoretical treatment of dynamic programming in terms of contraction mappings.

The Bellman optimality equation (for *v*⇤) was popularized by Richard Bellman (1957a), who called it the "basic functional equation." The counterpart of the Bellman optimality equation for continuous time and state problems is known as the Hamilton–Jacobi–Bellman equation (or often just the Hamilton–Jacobi equation), indicating its roots in classical physics (e.g., Schultz and Melsa, 1967).

The golf example was suggested by Chris Watkins.

## <span id="page-59-0"></span>Chapter 13

# Policy Gradient Methods

In this chapter we consider something new. So far in this book almost all the methods have been *action-value methods*; they learned the values of actions and then selected actions based on their estimated action values[1](#page-59-1); their policies would not even exist without the action-value estimates. In this chapter we consider methods that instead learn a *parameterized policy* that can select actions without consulting a value function. A value function may still be used to *learn* the policy parameter, but is not required for action selection. We use the notation ✓ <sup>2</sup> <sup>R</sup>*<sup>d</sup>*<sup>0</sup> for the policy's parameter vector. Thus we write ⇡(*a|s,* ✓) = Pr*{A<sup>t</sup>* =*a | S<sup>t</sup>* =*s,* ✓*<sup>t</sup>* =✓*}* for the probability that action *a* is taken at time *t* given that the environment is in state *s* at time *t* with parameter ✓. If a method uses a learned value function as well, then the value function's weight vector is denoted <sup>w</sup> <sup>2</sup> <sup>R</sup>*<sup>d</sup>* as usual, as in ˆ*v*(*s,*w).

In this chapter we consider methods for learning the policy parameter based on the gradient of some scalar performance measure *J*(✓) with respect to the policy parameter. These methods seek to *maximize* performance, so their updates approximate gradient *ascent* in *J*:

<span id="page-59-2"></span>
$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \alpha \widehat{\nabla J(\boldsymbol{\theta}_t)}, \tag{13.1}$$

where <sup>r</sup>\*J*(✓*t*) <sup>2</sup> <sup>R</sup>*<sup>d</sup>*<sup>0</sup> is a stochastic estimate whose expectation approximates the gradient of the performance measure with respect to its argument ✓*t*. All methods that follow this general schema we call *policy gradient methods*, whether or not they also learn an approximate value function. Methods that learn approximations to both policy and value functions are often called *actor–critic methods*, where 'actor' is a reference to the learned policy, and 'critic' refers to the learned value function, usually a state-value function. First we treat the episodic case, in which performance is defined as the value of the start state under the parameterized policy, before going on to consider the continuing case, in

<span id="page-59-1"></span><sup>1</sup>The lone exception is the gradient bandit algorithms of Section 2.8. In fact, that section goes through many of the same steps, in the single-state bandit case, as we go through here for full MDPs. Reviewing that section would be good preparation for fully understanding this chapter.

which performance is defined as the average reward rate, as in Section 10.3. In the end, we are able to express the algorithms for both cases in very similar terms.

#### <span id="page-60-0"></span>13.1 Policy Approximation and its Advantages

In policy gradient methods, the policy can be parameterized in any way, as long as ⇡(*a|s,* ✓) is di↵erentiable with respect to its parameters, that is, as long as r⇡(*a|s,* ✓) (the column vector of partial derivatives of ⇡(*a|s,* ✓) with respect to the components of ✓) exists and is finite for all *<sup>s</sup>* <sup>2</sup> <sup>S</sup>, *<sup>a</sup>* <sup>2</sup> <sup>A</sup>(*s*), and ✓ <sup>2</sup> <sup>R</sup>*<sup>d</sup>*<sup>0</sup> . In practice, to ensure exploration we generally require that the policy never becomes deterministic (i.e., that ⇡(*a|s,* ✓) 2 (0*,* 1), for all *s, a,* ✓). In this section we introduce the most common parameterization for discrete action spaces and point out the advantages it o↵ers over action-value methods. Policy-based methods also o↵er useful ways of dealing with continuous action spaces, as we describe later in [Section 13.7.](#page-73-0)

If the action space is discrete and not too large, then a natural and common kind of parameterization is to form parameterized numerical preferences *h*(*s, a,* ✓) 2 R for each state–action pair. The actions with the highest preferences in each state are given the highest probabilities of being selected, for example, according to an exponential soft-max distribution:

<span id="page-60-2"></span>
$$\pi(a|s,\boldsymbol{\theta}) \doteq \frac{e^{h(s,a,\boldsymbol{\theta})}}{\sum_{b} e^{h(s,b,\boldsymbol{\theta})}},\tag{13.2}$$

where *e* ⇡ 2*.*71828 is the base of the natural logarithm. Note that the denominator here is just what is required so that the action probabilities in each state sum to one. We call this kind of policy parameterization *soft-max in action preferences*.

The action preferences themselves can be parameterized arbitrarily. For example, they might be computed by a deep artificial neural network (ANN), where ✓ is the vector of all the connection weights of the network (as in the AlphaGo system described in Section 16.6). Or the preferences could simply be linear in features,

<span id="page-60-1"></span>
$$h(s, a, \boldsymbol{\theta}) = \boldsymbol{\theta}^{\top} \mathbf{x}(s, a), \tag{13.3}$$

using feature vectors <sup>x</sup>(*s, a*) <sup>2</sup> <sup>R</sup>*<sup>d</sup>*<sup>0</sup> constructed by any of the methods described in Section 9.5.

One advantage of parameterizing policies according to the soft-max in action preferences is that the approximate policy can approach a deterministic policy, whereas with "-greedy action selection over action values there is always an " probability of selecting a random action. Of course, one could select according to a soft-max distribution based on action values, but this alone would not allow the policy to approach a deterministic policy. Instead, the action-value estimates would converge to their corresponding true values, which would di↵er by a finite amount, translating to specific probabilities other than 0 and 1. If the soft-max distribution included a temperature parameter, then the temperature could be reduced over time to approach determinism, but in practice it would be dicult to choose the reduction schedule, or even the initial temperature, without more prior knowledge of the true action values than we would like to assume. Action preferences

are di↵erent because they do not approach specific values; instead they are driven to produce the optimal stochastic policy. If the optimal policy is deterministic, then the preferences of the optimal actions will be driven infinitely higher than all suboptimal actions (if permitted by the parameterization).

A second advantage of parameterizing policies according to the soft-max in action preferences is that it enables the selection of actions with arbitrary probabilities. In problems with significant function approximation, the best approximate policy may be stochastic. For example, in card games with imperfect information the optimal play is often to do two di↵erent things with specific probabilities, such as when blung in Poker. Action-value methods have no natural way of finding stochastic optimal policies, whereas policy approximating methods can, as shown in [Example 13.1.](#page-60-1)

#### Example 13.1 Short corridor with switched actions

Consider the small corridor gridworld shown inset in the graph below. The reward is 1 per step, as usual. In each of the three nonterminal states there are only two actions, right and left. These actions have their usual consequences in the first and third states (left causes no movement in the first state), but in the second state they are reversed, so that right moves to the left and left moves to the right. The problem is dicult because all the states appear identical under the function approximation. In particular, we define x(*s,*right) = [1*,* 0]<sup>&</sup>gt; and x(*s,* left) = [0*,* 1]>, for all *s*. An action-value method with "-greedy action selection is forced to choose between just two policies: choosing right with high probability 1 "*/*2 on all steps or choosing left with the same high probability on all time steps. If " = 0*.*1, then these two policies achieve a value (at the start state) of less than 44 and 82, respectively, as shown in the graph. A method can do significantly better if it can learn a specific probability with which to select right. The best probability is about 0.59, which achieves a value of about 11*.*6.

![](_page_61_Figure_6.jpeg)

Perhaps the simplest advantage that policy parameterization may have over actionvalue parameterization is that the policy may be a simpler function to approximate. Problems vary in the complexity of their policies and action-value functions. For some, the action-value function is simpler and thus easier to approximate. For others, the policy is simpler. In the latter case a policy-based method will typically learn faster and yield a superior asymptotic policy (as in Tetris; see S¸im¸sek, Alg´orta, and Kothiyal, 2016).

Finally, we note that the choice of policy parameterization is sometimes a good way of injecting prior knowledge about the desired form of the policy into the reinforcement learning system. This is often the most important reason for using a policy-based learning method.

*Exercise 13.1* Use your knowledge of the gridworld and its dynamics to determine an *exact* symbolic expression for the optimal probability of selecting the right action in [Example 13.1.](#page-60-1) ⇤

#### <span id="page-62-0"></span>13.2 The Policy Gradient Theorem

In addition to the practical advantages of policy parameterization over "-greedy action selection, there is also an important theoretical advantage. With continuous policy parameterization the action probabilities change smoothly as a function of the learned parameter, whereas in "-greedy selection the action probabilities may change dramatically for an arbitrarily small change in the estimated action values, if that change results in a di↵erent action having the maximal value. Largely because of this, stronger convergence guarantees are available for policy-gradient methods than for action-value methods. In particular, it is the continuity of the policy dependence on the parameters that enables policy-gradient methods to approximate gradient ascent [\(13.1\)](#page-59-2).

The episodic and continuing cases define the performance measure, *J*(✓), di↵erently and thus have to be treated separately to some extent. Nevertheless, we will try to present both cases uniformly, and we develop a notation so that the major theoretical results can be described with a single set of equations.

In this section we treat the episodic case, for which we define the performance measure as the value of the start state of the episode. We can simplify the notation without losing any meaningful generality by assuming that every episode starts in some particular (non-random) state *s*0. Then, in the episodic case we define performance as

$$J(\boldsymbol{\theta}) \doteq v_{\pi_{\boldsymbol{\theta}}}(s_0), \tag{13.4}$$

where *v*⇡✓ is the true value function for ⇡✓, the policy determined by ✓. From here on in our discussion we will assume no discounting ( = 1) for the episodic case, although for completeness we do include the possibility of discounting in the boxed algorithms.

With function approximation it may seem challenging to change the policy parameter in a way that ensures improvement. The problem is that performance depends on both the action selections and the distribution of states in which those selections are made, and that both of these are a↵ected by the policy parameter. Given a state, the e↵ect of the policy parameter on the actions, and thus on reward, can be computed in a relatively straightforward way from knowledge of the parameterization. But the e↵ect of the policy

#### Proof of the Policy Gradient Theorem (episodic case)

<span id="page-63-0"></span>With just elementary calculus and re-arranging of terms, we can prove the policy gradient theorem from first principles. To keep the notation simple, we leave it implicit in all cases that ⇡ is a function of ✓, and all gradients are also implicitly with respect to ✓. First note that the gradient of the state-value function can be written in terms of the action-value function as

$$\nabla v_{\pi}(s) = \nabla \left[ \sum_{a} \pi(a|s) q_{\pi}(s, a) \right], \quad \text{for all } s \in \mathbb{S}$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \nabla q_{\pi}(s, a) \right] \quad \text{(product rule of calculus)}$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \nabla \sum_{s', r} p(s', r|s, a) (r + v_{\pi}(s')) \right]$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \sum_{s', r} p(s'|s, a) \nabla v_{\pi}(s') \right]$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \sum_{s'} p(s'|s, a) \nabla v_{\pi}(s') \right]$$

$$= \sum_{a'} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \sum_{s'} p(s'|s, a) \right]$$

$$= \sum_{a'} \left[ \nabla \pi(a'|s') q_{\pi}(s', a') + \pi(a'|s') \sum_{s''} p(s''|s', a') \nabla v_{\pi}(s'') \right]$$

$$= \sum_{x \in \mathbb{S}} \sum_{k=0}^{\infty} \Pr(s \to x, k, \pi) \sum_{a} \nabla \pi(a|x) q_{\pi}(x, a),$$

after repeated unrolling, where Pr(*s*!*x, k,* ⇡) is the probability of transitioning from state *s* to state *x* in *k* steps under policy ⇡. It is then immediate that

$$\nabla J(\boldsymbol{\theta}) = \nabla v_{\pi}(s_{0})$$

$$= \sum_{s} \left(\sum_{k=0}^{\infty} \Pr(s_{0} \to s, k, \pi)\right) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a)$$

$$= \sum_{s} \eta(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a) \qquad \text{(box page 199)}$$

$$= \sum_{s'} \eta(s') \sum_{s} \frac{\eta(s)}{\sum_{s'} \eta(s')} \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a)$$

$$= \sum_{s'} \eta(s') \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a) \qquad \text{(Eq. 9.3)}$$

$$\propto \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a) \qquad \text{(Q.E.D.)}$$

on the state distribution is a function of the environment and is typically unknown. How can we estimate the performance gradient with respect to the policy parameter when the gradient depends on the unknown e↵ect of policy changes on the state distribution?

Fortunately, there is an excellent theoretical answer to this challenge in the form of the *policy gradient theorem*, which provides an analytic expression for the gradient of performance with respect to the policy parameter (which is what we need to approximate for gradient ascent [\(13.1\)](#page-59-2)) that does *not* involve the derivative of the state distribution. The policy gradient theorem for the episodic case establishes that

<span id="page-64-2"></span>
$$\nabla J(\boldsymbol{\theta}) \propto \sum_{s} \mu(s) \sum_{a} q_{\pi}(s, a) \nabla \pi(a|s, \boldsymbol{\theta}),$$
 (13.5)

where the gradients are column vectors of partial derivatives with respect to the components of ✓, and ⇡ denotes the policy corresponding to parameter vector ✓. The symbol / here means "proportional to". In the episodic case, the constant of proportionality is the average length of an episode, and in the continuing case it is 1, so that the relationship is actually an equality. The distribution *µ* here (as in Chapters 9 and 10) is the on-policy distribution under ⇡ (see page 199). The policy gradient theorem is proved for the episodic case in the box on the previous page.

### <span id="page-64-0"></span>13.3 REINFORCE: Monte Carlo Policy Gradient

We are now ready to derive our first policy-gradient learning algorithm. Recall our overall strategy of stochastic gradient ascent [\(13.1\)](#page-59-2), which requires a way to obtain samples such that the expectation of the sample gradient is proportional to the actual gradient of the performance measure as a function of the parameter. The sample gradients need only be proportional to the gradient because any constant of proportionality can be absorbed into the step size ↵, which is otherwise arbitrary. The policy gradient theorem gives an exact expression proportional to the gradient; all that is needed is some way of sampling whose expectation equals or approximates this expression. Notice that the right-hand side of the policy gradient theorem is a sum over states weighted by how often the states occur under the target policy ⇡; if ⇡ is followed, then states will be encountered in these proportions. Thus

<span id="page-64-1"></span>
$$\nabla J(\boldsymbol{\theta}) \propto \sum_{s} \mu(s) \sum_{a} q_{\pi}(s, a) \nabla \pi(a|s, \boldsymbol{\theta})$$

$$= \mathbb{E}_{\pi} \left[ \sum_{a} q_{\pi}(S_{t}, a) \nabla \pi(a|S_{t}, \boldsymbol{\theta}) \right]. \tag{13.6}$$

We could stop here and instantiate our stochastic gradient-ascent algorithm [\(13.1\)](#page-59-2) as

$$\boldsymbol{\theta}_{t+1} \doteq \boldsymbol{\theta}_t + \alpha \sum_{a} \hat{q}(S_t, a, \mathbf{w}) \nabla \pi(a|S_t, \boldsymbol{\theta}),$$
 (13.7)

where *q*ˆ is some learned approximation to *q*⇡. This algorithm, which has been called an *all-actions* method because its update involves all of the actions, is promising and

deserving of further study, but our current interest is the classical REINFORCE algorithm (Willams, 1992) whose update at time *t* involves just *At*, the one action actually taken at time *t*.

We continue our derivation of REINFORCE by introducing *A<sup>t</sup>* in the same way as we introduced *S<sup>t</sup>* in [\(13.6\)](#page-64-1)—by replacing a sum over the random variable's possible values by an expectation under ⇡, and then sampling the expectation. Equation [\(13.6\)](#page-64-1) involves an appropriate sum over actions, but each term is not weighted by ⇡(*a|St,* ✓) as is needed for an expectation under ⇡. So we introduce such a weighting, without changing the equality, by multiplying and then dividing the summed terms by ⇡(*a|St,* ✓). Continuing from [\(13.6\)](#page-64-1), we have

$$\nabla J(\boldsymbol{\theta}) \propto \mathbb{E}_{\pi} \left[ \sum_{a} \pi(a|S_{t}, \boldsymbol{\theta}) q_{\pi}(S_{t}, a) \frac{\nabla \pi(a|S_{t}, \boldsymbol{\theta})}{\pi(a|S_{t}, \boldsymbol{\theta})} \right]$$

$$= \mathbb{E}_{\pi} \left[ q_{\pi}(S_{t}, A_{t}) \frac{\nabla \pi(A_{t}|S_{t}, \boldsymbol{\theta})}{\pi(A_{t}|S_{t}, \boldsymbol{\theta})} \right] \qquad \text{(replacing } a \text{ by the sample } A_{t} \sim \pi)$$

$$= \mathbb{E}_{\pi} \left[ G_{t} \frac{\nabla \pi(A_{t}|S_{t}, \boldsymbol{\theta})}{\pi(A_{t}|S_{t}, \boldsymbol{\theta})} \right], \qquad \text{(because } \mathbb{E}_{\pi}[G_{t}|S_{t}, A_{t}] = q_{\pi}(S_{t}, A_{t}))$$

where *G<sup>t</sup>* is the return as usual. The final expression in brackets is exactly what is needed, a quantity that can be sampled on each time step whose expectation is proportional to the gradient. Using this sample to instantiate our generic stochastic gradient ascent algorithm [\(13.1\)](#page-59-2) yields the REINFORCE update:

<span id="page-65-0"></span>
$$\boldsymbol{\theta}_{t+1} \doteq \boldsymbol{\theta}_t + \alpha G_t \frac{\nabla \pi(A_t | S_t, \boldsymbol{\theta}_t)}{\pi(A_t | S_t, \boldsymbol{\theta}_t)}.$$
(13.8)

This update has an intuitive appeal. Each increment is proportional to the product of a return *G<sup>t</sup>* and a vector, the gradient of the probability of taking the action actually taken divided by the probability of taking that action. The vector is the direction in parameter space that most increases the probability of repeating the action *A<sup>t</sup>* on future visits to state *St*. The update increases the parameter vector in this direction proportional to the return, and inversely proportional to the action probability. The former makes sense because it causes the parameter to move most in the directions that favor actions that yield the highest return. The latter makes sense because otherwise actions that are selected frequently are at an advantage (the updates will be more often in their direction) and might win out even if they do not yield the highest return.

Note that REINFORCE uses the complete return from time *t*, which includes all future rewards up until the end of the episode. In this sense REINFORCE is a Monte Carlo algorithm and is well defined only for the episodic case with all updates made in retrospect after the episode is completed (like the Monte Carlo algorithms in Chapter 5). This is shown explicitly in the boxed algorithm on the next page.

Notice that the update in the last line of pseudocode appears rather di↵erent from the REINFORCE update rule [\(13.8\)](#page-65-0). One di↵erence is that the pseudocode uses the compact expression <sup>r</sup> ln ⇡(*At|St,* ✓*t*) for the fractional vector <sup>r</sup>⇡(*At|St,*✓*t*) ⇡(*At|St,*✓*t*) in [\(13.8\)](#page-65-0). That these two expressions for the vector are equivalent follows from the identity <sup>r</sup> ln *<sup>x</sup>* <sup>=</sup> <sup>r</sup>*<sup>x</sup> x* . This vector has been given several names and notations in the literature; we will refer to it simply as the *eligibility vector*. Note that it is the only place that the policy parameterization appears in the algorithm.

```
REINFORCE: Monte-Carlo Policy-Gradient Control (episodic) for ⇡⇤
Input: a di↵erentiable policy parameterization ⇡(a|s, ✓)
Algorithm parameter: step size ↵ > 0
Initialize policy parameter ✓ 2 Rd0
                              (e.g., to 0)
Loop forever (for each episode):
  Generate an episode S0, A0, R1,...,ST 1, AT 1, RT , following ⇡(·|·, ✓)
  Loop for each step of the episode t = 0, 1,...,T  1:
     G PT
           k=t+1 kt1Rk (Gt)
     ✓ ✓ + ↵tGr ln ⇡(At|St, ✓)
```

The second di↵erence between the pseudocode update and the REINFORCE update equation [\(13.8\)](#page-65-0) is that the former includes a factor of *<sup>t</sup>* . This is because, as mentioned earlier, in the text we are treating the non-discounted case ( = 1) while in the boxed algorithms we are giving the algorithms for the general discounted case. All of the ideas go through in the discounted case with appropriate adjustments (including to the box on page 199) but involve additional complexity that distracts from the main ideas.

⇤ *Exercise 13.2* Generalize the box on page 199, the policy gradient theorem [\(13.5\)](#page-64-2), the proof of the policy gradient theorem (page [325\)](#page-63-0), and the steps leading to the REINFORCE update equation [\(13.8\)](#page-65-0), so that [\(13.8\)](#page-65-0) ends up with a factor of *<sup>t</sup>* and thus aligns with the general algorithm given in the pseudocode. ⇤

[Figure 13.1](#page-66-0) shows the performance of REINFORCE on the short-corridor gridworld from [Example 13.1.](#page-60-1)

<span id="page-66-0"></span>![](_page_66_Figure_7.jpeg)

Figure 13.1: REINFORCE on the short-corridor gridworld [\(Example 13.1\)](#page-60-1). With a good step size, the total reward per episode approaches the optimal value of the start state.

As a stochastic gradient method, REINFORCE has good theoretical convergence properties. By construction, the expected update over an episode is in the same direction as the performance gradient. This assures an improvement in expected performance for suciently small ↵, and convergence to a local optimum under standard stochastic approximation conditions for decreasing ↵. However, as a Monte Carlo method REINFORCE may be of high variance and thus produce slow learning.

*Exercise 13.3* In [Section 13.1](#page-60-0) we considered policy parameterizations using the soft-max in action preferences [\(13.2\)](#page-60-2) with linear action preferences [\(13.3\)](#page-60-1). For this parameterization, prove that the eligibility vector is

$$\nabla \ln \pi(a|s, \boldsymbol{\theta}) = \mathbf{x}(s, a) - \sum_{b} \pi(b|s, \boldsymbol{\theta}) \mathbf{x}(s, b), \tag{13.9}$$

using the definitions and elementary calculus. ⇤

#### <span id="page-67-0"></span>13.4 REINFORCE with Baseline

The policy gradient theorem [\(13.5\)](#page-64-2) can be generalized to include a comparison of the action value to an arbitrary *baseline b*(*s*):

<span id="page-67-1"></span>
$$\nabla J(\boldsymbol{\theta}) \propto \sum_{s} \mu(s) \sum_{a} \left( q_{\pi}(s, a) - b(s) \right) \nabla \pi(a|s, \boldsymbol{\theta}). \tag{13.10}$$

The baseline can be any function, even a random variable, as long as it does not vary with *a*; the equation remains valid because the subtracted quantity is zero:

$$\sum_a b(s) \nabla \pi(a|s, \boldsymbol{\theta}) \ = \ b(s) \nabla \sum_a \pi(a|s, \boldsymbol{\theta}) \ = \ b(s) \nabla 1 \ = \ 0.$$

The policy gradient theorem with baseline [\(13.10\)](#page-67-1) can be used to derive an update rule using similar steps as in the previous section. The update rule that we end up with is a new version of REINFORCE that includes a general baseline:

<span id="page-67-2"></span>
$$\boldsymbol{\theta}_{t+1} \doteq \boldsymbol{\theta}_t + \alpha \Big( G_t - b(S_t) \Big) \frac{\nabla \pi(A_t | S_t, \boldsymbol{\theta}_t)}{\pi(A_t | S_t, \boldsymbol{\theta}_t)}.$$
(13.11)

Because the baseline could be uniformly zero, this update is a strict generalization of REINFORCE. In general, the baseline leaves the expected value of the update unchanged, but it can have a large e↵ect on its variance. For example, we saw in Section 2.8 that an analogous baseline can significantly reduce the variance (and thus speed the learning) of gradient bandit algorithms. In the bandit algorithms the baseline was just a number (the average of the rewards seen so far), but for MDPs the baseline should vary with state. In some states all actions have high values and we need a high baseline to di↵erentiate the higher valued actions from the less highly valued ones; in other states all actions will have low values and a low baseline is appropriate.

One natural choice for the baseline is an estimate of the state value, *v*ˆ(*St,*w), where <sup>w</sup> <sup>2</sup> <sup>R</sup>*<sup>d</sup>* is a weight vector learned by one of the methods presented in previous chapters.

Because REINFORCE is a Monte Carlo method for learning the policy parameter, ✓, it seems natural to also use a Monte Carlo method to learn the state-value weights, w. A complete pseudocode algorithm for REINFORCE with baseline using such a learned state-value function as the baseline is given in the box below.

```
REINFORCE with Baseline (episodic), for estimating ⇡✓ ⇡ ⇡⇤
Input: a di↵erentiable policy parameterization ⇡(a|s, ✓)
Input: a di↵erentiable state-value function parameterization ˆv(s,w)
Algorithm parameters: step sizes ↵✓ > 0, ↵w > 0
Initialize policy parameter ✓ 2 Rd0
                               and state-value weights w 2 Rd (e.g., to 0)
Loop forever (for each episode):
  Generate an episode S0, A0, R1,...,ST 1, AT 1, RT , following ⇡(·|·, ✓)
  Loop for each step of the episode t = 0, 1,...,T  1:
     G PT
            k=t+1 kt1Rk (Gt)
      G  vˆ(St,w)
     w w + ↵w rvˆ(St,w)
     ✓ ✓ + ↵✓ t r ln ⇡(At|St, ✓)
```

This algorithm has two step sizes, denoted ↵✓ and ↵<sup>w</sup> (where ↵✓ is the ↵ in [\(13.11\)](#page-67-2)). Choosing the step size for values (here ↵<sup>w</sup>) is relatively easy; in the linear case we have rules of thumb for setting it, such as ↵<sup>w</sup> = 0*.*1*/*E ⇥ kr*v*ˆ(*St,*w)k 2 *µ* ⇤ (see Section 9.6). It is much less clear how to set the step size for the policy parameters, ↵✓, whose best value depends on the range of variation of the rewards and on the policy parameterization.

<span id="page-68-0"></span>![](_page_68_Figure_5.jpeg)

Figure 13.2: Adding a baseline to REINFORCE can make it learn much faster, as illustrated here on the short-corridor gridworld [\(Example 13.1\)](#page-60-1). The step size used here for plain REINFORCE is that at which it performs best (to the nearest power of two; see [Figure 13.1\)](#page-66-0).

[Figure 13.2](#page-68-0) compares the behavior of REINFORCE with and without a baseline on the short-corridor gridword [\(Example 13.1\)](#page-60-1). Here the approximate state-value function used in the baseline is ˆ*v*(*s,*w) = *w*. That is, w is a single component, *w*.

#### <span id="page-69-0"></span>13.5 Actor–Critic Methods

In REINFORCE with baseline, the learned state-value function estimates the value of the *first* state of each state transition. This estimate sets a baseline for the subsequent return, but is made prior to the transition's action and thus cannot be used to assess that action. In actor–critic methods, on the other hand, the state-value function is applied also to the *second* state of the transition. The estimated value of the second state, when discounted and added to the reward, constitutes the one-step return, *Gt*:*t*+1, which is a useful estimate of the actual return and thus *is* a way of assessing the action. As we have seen in the TD learning of value functions throughout this book, the one-step return is often superior to the actual return in terms of its variance and computational congeniality, even though it introduces bias. We also know how we can flexibly modulate the extent of the bias with *n*-step returns and eligibility traces (Chapters 7 and 12). When the state-value function is used to assess actions in this way it is called a *critic*, and the overall policy-gradient method is termed an *actor–critic* method. Note that the bias in the gradient estimate is not due to bootstrapping as such; the actor would be biased even if the critic was learned by a Monte Carlo method.

First consider one-step actor–critic methods, the analog of the TD methods introduced in Chapter 6 such as TD(0), Sarsa(0), and Q-learning. The main appeal of one-step methods is that they are fully online and incremental, yet avoid the complexities of eligibility traces. They are a special case of the eligibility trace methods, but easier to understand. One-step actor–critic methods replace the full return of REINFORCE [\(13.11\)](#page-67-2) with the one-step return (and use a learned state-value function as the baseline) as follows:

$$\boldsymbol{\theta}_{t+1} \doteq \boldsymbol{\theta}_t + \alpha \Big( G_{t:t+1} - \hat{v}(S_t, \mathbf{w}) \Big) \frac{\nabla \pi(A_t | S_t, \boldsymbol{\theta}_t)}{\pi(A_t | S_t, \boldsymbol{\theta}_t)}$$
(13.12)

<span id="page-69-1"></span>
$$= \boldsymbol{\theta}_t + \alpha \left( R_{t+1} + \gamma \hat{v}(S_{t+1}, \mathbf{w}) - \hat{v}(S_t, \mathbf{w}) \right) \frac{\nabla \pi(A_t | S_t, \boldsymbol{\theta}_t)}{\pi(A_t | S_t, \boldsymbol{\theta}_t)}$$
(13.13)

$$= \boldsymbol{\theta}_t + \alpha \delta_t \frac{\nabla \pi(A_t | S_t, \boldsymbol{\theta}_t)}{\pi(A_t | S_t, \boldsymbol{\theta}_t)}.$$
 (13.14)

The natural state-value-function learning method to pair with this is semi-gradient TD(0). Pseudocode for the complete algorithm is given in the box at the top of the next page. Note that it is now a fully online, incremental algorithm, with states, actions, and rewards processed as they occur and then never revisited.

```
One-step Actor–Critic (episodic), for estimating ⇡✓ ⇡ ⇡⇤
Input: a di↵erentiable policy parameterization ⇡(a|s, ✓)
Input: a di↵erentiable state-value function parameterization ˆv(s,w)
Parameters: step sizes ↵✓ > 0, ↵w > 0
Initialize policy parameter ✓ 2 Rd0
                                  and state-value weights w 2 Rd (e.g., to 0)
Loop forever (for each episode):
  Initialize S (first state of episode)
  I 1
  Loop while S is not terminal (for each time step):
     A ⇠ ⇡(·|S, ✓)
     Take action A, observe S0
                              , R
      R +  vˆ(S0
                    ,w)  vˆ(S,w) (if S0 is terminal, then ˆv(S0
                                                                  ,w) .
                                                                      = 0)
     w w + ↵w rvˆ(S,w)
     ✓ ✓ + ↵✓ I r ln ⇡(A|S, ✓)
     I I
     S S0
```

The generalizations to the forward view of *n*-step methods and then to a -return algorithm are straightforward. The one-step return in [\(13.12\)](#page-69-1) is merely replaced by *Gt*:*t*+*<sup>n</sup>* or *G <sup>t</sup>* respectively. The backward view of the -return algorithm is also straightforward, using separate eligibility traces for the actor and critic, each after the patterns in Chapter 12. Pseudocode for the complete algorithm is given in the box below.

```
Actor–Critic with Eligibility Traces (episodic), for estimating ⇡✓ ⇡ ⇡⇤
Input: a di↵erentiable policy parameterization ⇡(a|s, ✓)
Input: a di↵erentiable state-value function parameterization ˆv(s,w)
Parameters: trace-decay rates ✓ 2 [0, 1], w 2 [0, 1]; step sizes ↵✓ > 0, ↵w > 0
Initialize policy parameter ✓ 2 Rd0
                                  and state-value weights w 2 Rd (e.g., to 0)
Loop forever (for each episode):
  Initialize S (first state of episode)
  z✓ 0 (d0
             -component eligibility trace vector)
  zw 0 (d-component eligibility trace vector)
  I 1
  Loop while S is not terminal (for each time step):
     A ⇠ ⇡(·|S, ✓)
     Take action A, observe S0
                              , R
      R +  vˆ(S0
                    ,w)  vˆ(S,w) (if S0 is terminal, then ˆv(S0
                                                                  ,w) .
                                                                      = 0)
     zw wzw + rvˆ(S,w)
     z✓ ✓z✓ + I r ln ⇡(A|S, ✓)
     w w + ↵w zw
     ✓ ✓ + ↵✓ z✓
     I I
     S S0
```

#### <span id="page-71-0"></span>13.6 Policy Gradient for Continuing Problems

As discussed in Section 10.3, for continuing problems without episode boundaries we need to define performance in terms of the average rate of reward per time step:

<span id="page-71-1"></span>
$$J(\boldsymbol{\theta}) \doteq r(\pi) \doteq \lim_{h \to \infty} \frac{1}{h} \sum_{t=1}^{h} \mathbb{E}[R_t \mid S_0, A_{0:t-1} \sim \pi]$$

$$= \lim_{t \to \infty} \mathbb{E}[R_t \mid S_0, A_{0:t-1} \sim \pi]$$

$$= \sum_{s} \mu(s) \sum_{a} \pi(a|s) \sum_{s',r} p(s', r|s, a)r,$$
(13.15)

where *<sup>µ</sup>* is the steady-state distribution under ⇡, *<sup>µ</sup>*(*s*) *.* = lim*<sup>t</sup>*!1 Pr*{S<sup>t</sup>* =*s|A*0:*<sup>t</sup>* ⇠⇡*}*, which is assumed to exist and to be independent of *S*<sup>0</sup> (an ergodicity assumption). Remember that this is the special distribution under which, if you select actions according to ⇡, you remain in the same distribution:

<span id="page-71-2"></span>
$$\sum_{s} \mu(s) \sum_{a} \pi(a|s, \boldsymbol{\theta}) p(s'|s, a) = \mu(s'), \text{ for all } s' \in \mathcal{S}.$$
(13.16)

Complete pseudocode for the actor–critic algorithm in the continuing case (backward view) is given in the box below.

#### Actor–Critic with Eligibility Traces (continuing), for estimating ⇡✓ ⇡ ⇡⇤ Input: a di↵erentiable policy parameterization ⇡(*a|s,* ✓) Input: a di↵erentiable state-value function parameterization ˆ*v*(*s,*w) Algorithm parameters: <sup>w</sup> <sup>2</sup> [0*,* 1], ✓ <sup>2</sup> [0*,* 1], ↵<sup>w</sup> *<sup>&</sup>gt;* 0, ↵✓ *<sup>&</sup>gt;* 0, ↵*<sup>R</sup>*¯ *<sup>&</sup>gt;* <sup>0</sup> Initialize *<sup>R</sup>*¯ <sup>2</sup> <sup>R</sup> (e.g., to 0) Initialize state-value weights <sup>w</sup> <sup>2</sup> <sup>R</sup>*<sup>d</sup>* and policy parameter ✓ <sup>2</sup> <sup>R</sup>*<sup>d</sup>*<sup>0</sup> (e.g., to 0) Initialize *S* 2 S (e.g., to *s*0) <sup>z</sup><sup>w</sup> <sup>0</sup> (*d*-component eligibility trace vector) <sup>z</sup>✓ <sup>0</sup> (*d*<sup>0</sup> -component eligibility trace vector) Loop forever (for each time step): *A* ⇠ ⇡(*·|S,* ✓) Take action *A*, observe *S*<sup>0</sup> *, R <sup>R</sup> <sup>R</sup>*¯ + ˆ*v*(*S*<sup>0</sup> *,*w) *v*ˆ(*S,*w) *<sup>R</sup>*¯ *<sup>R</sup>*¯ <sup>+</sup> ↵*<sup>R</sup>*¯ <sup>z</sup><sup>w</sup> <sup>w</sup>z<sup>w</sup> <sup>+</sup> <sup>r</sup>*v*ˆ(*S,*w) <sup>z</sup>✓ ✓z✓ <sup>+</sup> <sup>r</sup> ln ⇡(*A|S,* ✓) <sup>w</sup> <sup>w</sup> <sup>+</sup> ↵<sup>w</sup> z<sup>w</sup> ✓ ✓ <sup>+</sup> ↵✓ z✓ *S S*<sup>0</sup>

Naturally, in the continuing case, we define values, *<sup>v</sup>*⇡(*s*) *.* <sup>=</sup> <sup>E</sup>⇡[*Gt|S<sup>t</sup>* <sup>=</sup>*s*] and *<sup>q</sup>*⇡(*s, a*) *.* = E⇡[*Gt|S<sup>t</sup>* =*s, A<sup>t</sup>* =*a*], with respect to the di↵erential return:

<span id="page-72-0"></span>
$$G_t \doteq R_{t+1} - r(\pi) + R_{t+2} - r(\pi) + R_{t+3} - r(\pi) + \cdots$$
 (13.17)

With these alternate definitions, the policy gradient theorem as given for the episodic case [\(13.5\)](#page-64-2) remains true for the continuing case. A proof is given in the box on the next page. The forward and backward view equations also remain the same.

Proof of the Policy Gradient Theorem (continuing case)

<span id="page-72-1"></span>The proof of the policy gradient theorem for the continuing case begins similarly to the episodic case. Again we leave it implicit in all cases that ⇡ is a function of ✓ and that the gradients are with respect to ✓. Recall that in the continuing case *J*(✓) = *r*(⇡) [\(13.15\)](#page-71-1) and that *v*⇡ and *q*⇡ denote values with respect to the di↵erential return [\(13.17\)](#page-72-0). The gradient of the state-value function can be written, for any *s* 2 S, as

$$\nabla v_{\pi}(s) = \nabla \left[ \sum_{a} \pi(a|s) q_{\pi}(s, a) \right], \quad \text{for all } s \in \mathbb{S}$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \nabla q_{\pi}(s, a) \right]$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \nabla \sum_{s', r} p(s', r|s, a) (r - r(\boldsymbol{\theta}) + v_{\pi}(s')) \right]$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \nabla \sum_{s', r} p(s', r|s, a) (r - r(\boldsymbol{\theta}) + v_{\pi}(s')) \right]$$

$$= \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s, a) + \pi(a|s) \left[ -\nabla r(\boldsymbol{\theta}) + \sum_{s'} p(s'|s, a) \nabla v_{\pi}(s') \right] \right].$$

After re-arranging terms, we obtain

$$\nabla r(\boldsymbol{\theta}) = \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s,a) + \pi(a|s) \sum_{s'} p(s'|s,a) \nabla v_{\pi}(s') \right] - \nabla v_{\pi}(s).$$

Notice that the left-hand side can be written r*J*(✓), and that it does not depend on *s*. Thus the right-hand side does not depend on *s* either, and we can safely sum it over all *<sup>s</sup>* <sup>2</sup> <sup>S</sup>, weighted by *<sup>µ</sup>*(*s*), without changing it (because <sup>P</sup> *<sup>s</sup> µ*(*s*) = 1):

$$\begin{split} \nabla J(\boldsymbol{\theta}) &= \sum_{s} \mu(s) \left( \sum_{a} \left[ \nabla \pi(a|s) q_{\pi}(s,a) + \pi(a|s) \sum_{s'} p(s'|s,a) \nabla v_{\pi}(s') \right] - \nabla v_{\pi}(s) \right) \\ &= \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s,a) \\ &+ \sum_{s} \mu(s) \sum_{a} \pi(a|s) \sum_{s'} p(s'|s,a) \nabla v_{\pi}(s') - \sum_{s} \mu(s) \nabla v_{\pi}(s) \end{split}$$

$$= \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a)$$

$$+ \sum_{s'} \underbrace{\sum_{s} \mu(s) \sum_{a} \pi(a|s) p(s'|s, a)}_{\mu(s') \text{ (13.16)}} \nabla v_{\pi}(s') - \sum_{s} \mu(s) \nabla v_{\pi}(s)$$

$$= \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a) + \sum_{s'} \mu(s') \nabla v_{\pi}(s') - \sum_{s} \mu(s) \nabla v_{\pi}(s)$$

$$= \sum_{s} \mu(s) \sum_{a} \nabla \pi(a|s) q_{\pi}(s, a). \qquad Q.E.D.$$

#### <span id="page-73-0"></span>13.7 Policy Parameterization for Continuous Actions

Policy-based methods o↵er practical ways of dealing with large action spaces, even continuous spaces with an infinite number of actions. Instead of computing learned probabilities for each of the many actions, we instead learn statistics of the probability distribution. For example, the action set might be the real numbers, with actions chosen from a normal (Gaussian) distribution.

The probability density function for the normal distribution is conventionally written

$$p(x) \doteq \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),\tag{13.18}$$

*<sup>p</sup>*(*x*) *.* <sup>=</sup> <sup>1</sup> *<sup>p</sup>*(*x*) *.* <sup>=</sup> <sup>1</sup> <sup>p</sup>2⇡ exp ✓ (*<sup>x</sup> <sup>µ</sup>*)<sup>2</sup> 2<sup>2</sup> where *µ* and here are the mean and standard deviation of the normal distribution, and of course ⇡ here is just the number ⇡ ⇡ 3*.*14159. The probability density functions for several di↵erent means and standard deviations are shown to the right. The value *p*(*x*) is the *density* of the probability at *x*, not the probability. It can be greater than 1; it is the total area under *p*(*x*) that must sum to 1. In general, one can take the integral under *p*(*x*) for any range of *x* values to get the probability of *x* falling within that range.

<span id="page-73-2"></span><span id="page-73-1"></span>![](_page_73_Figure_8.jpeg)

To produce a policy parameterization, the policy can be defined as the normal probability density over a real-valued scalar action, with mean and standard deviation given by parametric function approximators that depend on the state. That is,

$$\pi(a|s,\boldsymbol{\theta}) \doteq \frac{1}{\sigma(s,\boldsymbol{\theta})\sqrt{2\pi}} \exp\left(-\frac{(a-\mu(s,\boldsymbol{\theta}))^2}{2\sigma(s,\boldsymbol{\theta})^2}\right),\tag{13.19}$$

where *<sup>µ</sup>* : <sup>S</sup>⇥R*<sup>d</sup>*<sup>0</sup> ! <sup>R</sup> and : <sup>S</sup>⇥R*<sup>d</sup>*<sup>0</sup> ! <sup>R</sup><sup>+</sup> are two parameterized function approximators. To complete the example we need only give a form for these approximators. For this we divide the policy's parameter vector into two parts, ✓ = [✓*µ,* ✓] <sup>&</sup>gt;, one part to be used for the approximation of the mean and one part for the approximation of the standard deviation. The mean can be approximated as a linear function. The standard deviation must always be positive and is better approximated as the exponential of a linear function. Thus

<span id="page-74-0"></span>
$$\mu(s, \boldsymbol{\theta}) \doteq \boldsymbol{\theta}_{\mu}^{\top} \mathbf{x}_{\mu}(s) \quad \text{and} \quad \sigma(s, \boldsymbol{\theta}) \doteq \exp(\boldsymbol{\theta}_{\sigma}^{\top} \mathbf{x}_{\sigma}(s)),$$
 (13.20)

where x*µ*(*s*) and x(*s*) are state feature vectors perhaps constructed by one of the methods described in Section 9.5. With these definitions, all the algorithms described in the rest of this chapter can be applied to learn to select real-valued actions.

*Exercise 13.4* Show that for the Gaussian policy parameterization (Equations [13.19](#page-73-1) and [13.20\)](#page-74-0) the eligibility vector has the following two parts:

$$\nabla \ln \pi(a|s, \boldsymbol{\theta}_{\mu}) = \frac{\nabla \pi(a|s, \boldsymbol{\theta}_{\mu})}{\pi(a|s, \boldsymbol{\theta})} = \frac{1}{\sigma(s, \boldsymbol{\theta})^2} (a - \mu(s, \boldsymbol{\theta})) \mathbf{x}_{\mu}(s), \text{ and}$$

$$\nabla \ln \pi(a|s, \boldsymbol{\theta}_{\sigma}) = \frac{\nabla \pi(a|s, \boldsymbol{\theta}_{\sigma})}{\pi(a|s, \boldsymbol{\theta})} = \left(\frac{\left(a - \mu(s, \boldsymbol{\theta})\right)^{2}}{\sigma(s, \boldsymbol{\theta})^{2}} - 1\right) \mathbf{x}_{\sigma}(s).$$

*Exercise 13.5* A *Bernoulli-logistic unit* is a stochastic neuron-like unit used in some ANNs (Section 9.7). Its input at time *t* is a feature vector x(*St*); its output, *At*, is a random variable having two values, 0 and 1, with Pr*{A<sup>t</sup>* = 1*}* = *P<sup>t</sup>* and Pr*{A<sup>t</sup>* = 0*}* = 1 *P<sup>t</sup>* (the Bernoulli distribution). Let *h*(*s,* 0*,* ✓) and *h*(*s,* 1*,* ✓) be the preferences in state *s* for the unit's two actions given policy parameter ✓. Assume that the di↵erence between the action preferences is given by a weighted sum of the unit's input vector, that is, assume that *h*(*s,* 1*,* ✓) *h*(*s,* 0*,* ✓) = ✓>x(*s*), where ✓ is the unit's weight vector.

- (a) Show that if the exponential soft-max distribution [\(13.2\)](#page-60-2) is used to convert action preferences to policies, then *P<sup>t</sup>* = ⇡(1*|St,* ✓*t*)=1*/*(1 + exp(✓<sup>&</sup>gt; *<sup>t</sup>* x(*St*))) (the logistic function).
- (b) What is the Monte-Carlo REINFORCE update of ✓*<sup>t</sup>* to ✓*t*+1 upon receipt of return *Gt*?
- (c) Express the eligibility r ln ⇡(*a|s,* ✓) for a Bernoulli-logistic unit, in terms of *a*, x(*s*), and ⇡(*a|s,* ✓) by calculating the gradient.

Hint for part (c): Define *P* = ⇡(1*|s,* ✓) and compute the derivative of the logarithm, for each action, using the chain rule on *P*. Combine the two results into one expression that depends on *a* and *P*, and then use the chain rule again, this time on ✓>x(*s*), noting that the derivative of the logistic function *<sup>f</sup>*(*x*)=1*/*(1 + *<sup>e</sup><sup>x</sup>*) is *<sup>f</sup>*(*x*)(1 *<sup>f</sup>*(*x*)). ⇤

*13.8. Summary 337*

#### <span id="page-75-0"></span>13.8 Summary

Prior to this chapter, this book focused on *action-value methods*—meaning methods that learn action values and then use them to determine action selections. In this chapter, on the other hand, we considered methods that learn a parameterized policy that enables actions to be taken without consulting action-value estimates. In particular, we have considered *policy-gradient methods*—meaning methods that update the policy parameter on each step in the direction of an estimate of the gradient of performance with respect to the policy parameter.

Methods that learn and store a policy parameter have many advantages. They can learn specific probabilities for taking the actions. They can learn appropriate levels of exploration and approach deterministic policies asymptotically. They can naturally handle continuous action spaces. All these things are easy for policy-based methods but awkward or impossible for "-greedy methods and for action-value methods in general. In addition, on some problems the policy is just simpler to represent parametrically than the value function; these problems are more suited to parameterized policy methods.

Parameterized policy methods also have an important theoretical advantage over action-value methods in the form of the *policy gradient theorem*, which gives an exact formula for how performance is a↵ected by the policy parameter that does not involve derivatives of the state distribution. This theorem provides a theoretical foundation for all policy gradient methods.

The REINFORCE method follows directly from the policy gradient theorem. Adding a state-value function as a *baseline* reduces REINFORCE's variance without introducing bias. If the state-value function is also used to assess—or criticize—the policy's action selections, then the value function is called a *critic* and the policy is called an *actor* ; the overall method is called an *actor–critic* method. The critic introduces bias into the actor's gradient estimates, but is often desirable for the same reason that bootstrapping TD methods are often superior to Monte Carlo methods (substantially reduced variance).

Overall, policy-gradient methods provide a significantly di↵erent set of strengths and weaknesses than action-value methods. Today they are less well understood in some respects, but a subject of excitement and ongoing research.

#### Bibliographical and Historical Remarks

Methods that we now see as related to policy gradients were actually some of the earliest to be studied in reinforcement learning (Witten, 1977; Barto, Sutton, and Anderson, 1983; Sutton, 1984; Williams, 1987, 1992) and in predecessor fields (see Phansalkar and Thathachar, 1995). They were largely supplanted in the 1990s by the action-value methods that are the focus of the other chapters of this book. In recent years, however, attention has returned to actor–critic methods and to policy-gradient methods in general. Among the further developments beyond what we cover here are natural-gradient methods (Amari, 1998; Kakade, 2002, Peters, Vijayakumar and Schaal, 2005; Peters and Schaal, 2008; Park, Kim and Kang, 2005; Bhatnagar, Sutton, Ghavamzadeh and Lee, 2009; see Grondman, Busoniu, Lopes and Babuska, 2012), deterministic policy-gradient methods

(Silver et al., 2014), o↵-policy policy-gradient methods (Degris, White, and Sutton, 2012; Maei, 2018), and entropy regularization (see Schulman, Chen, and Abbeel, 2017). Major applications include acrobatic helicopter autopilots and AlphaGo (Section 16.6).

Our presentation in this chapter is based primarily on that by Sutton, McAllester, Singh, and Mansour (2000), who introduced the term "policy gradient methods." A useful overview is provided by Bhatnagar et al. (2009). One of the earliest related works is by Aleksandrov, Sysoyev, and Shemeneva (1968). Thomas (2014) first realized that the factor of *<sup>t</sup>* , as specified in the boxed algorithms of this chapter, was needed in the case of discounted episodic problems.

- [13.1](#page-60-0) [Example 13.1](#page-60-1) and the results with it in this chapter were developed with Eric Graves.
- [13.2](#page-62-0) The policy gradient theorem here and on [page 334](#page-72-1) was first obtained by Marbach and Tsitsiklis (1998, 2001) and then independently by Sutton et al. (2000). A similar expression was obtained by Cao and Chen (1997). Other early results are due to Konda and Tsitsiklis (2000, 2003), Baxter and Bartlett (2001), and Baxter, Bartlett, and Weaver (2001). Some additional results are developed by Sutton, Singh, and McAllester (2000).
- [13.3](#page-64-0) REINFORCE is due to Williams (1987, 1992). Phansalkar and Thathachar (1995) proved both local and global convergence theorems for modified versions of REINFORCE algorithms.
  - The all-actions algorithm was first presented in an unpublished but widely circulated incomplete paper (Sutton, Singh, and McAllester, 2000) and then developed further by Ciosek and Whiteson (2017, 2018), who termed it "expected policy gradients," and by Asadi, Allen, Roderick, Mohamed, Konidaris, and Littman (2017), who called it "mean actor critic."
- [13.4](#page-67-0) The baseline was introduced in Williams's (1987, 1992) original work. Greensmith, Bartlett, and Baxter (2004) analyzed an arguably better baseline (see Dick, 2015). Thomas and Brunskill (2017) argue that an action-dependent baseline can be used without incurring bias.
- [13.5–](#page-69-0)6 Actor–critic methods were among the earliest to be investigated in reinforcement learning (Witten, 1977; Barto, Sutton, and Anderson, 1983; Sutton, 1984). The algorithms presented here are based on the work of Degris, White, and Sutton (2012). Actor–critic methods are sometimes referred to as advantage actor–critic ("A2C") methods in the literature.
- [13.7](#page-73-0) The first to show how continuous actions could be handled this way appears to have been Williams (1987, 1992). The figure on [page 335](#page-73-2) is adapted from Wikipedia.