---
abstract: |
  Bridging the 'reality gap' that separates simulated robotics from
  experiments on hardware could accelerate robotic research through
  improved data availability. This paper explores *domain
  randomization*, a simple technique for training models on simulated
  images that transfer to real images by randomizing rendering in the
  simulator. With enough variability in the simulator, the real world
  may appear to the model as just another variation. We focus on the
  task of object localization, which is a stepping stone to general
  robotic manipulation skills. We find that it is possible to train a
  real-world object detector that is accurate to 1.5 cm and robust to
  distractors and partial occlusions using only data from a simulator
  with non-realistic random textures. To demonstrate the capabilities of
  our detectors, we show they can be used to perform grasping in a
  cluttered environment. To our knowledge, this is the first successful
  transfer of a deep neural network trained *only* on simulated RGB
  images (without pre-training on real images) to the real world for the
  purpose of robotic control.
author:
- Josh Tobin$^{1}$, Rachel Fong$^{2}$, Alex Ray$^{2}$, Jonas
  Schneider$^{2}$, Wojciech Zaremba$^{2}$, Pieter Abbeel$^{3}$ [^1] [^2]
  [^3]
title: " **Domain Randomization for Transferring Deep Neural Networks
  from Simulation to the Real World**"
---

# INTRODUCTION

Performing robotic learning in a physics simulator could accelerate the
impact of machine learning on robotics by allowing faster, more
scalable, and lower-cost data collection than is possible with physical
robots. Learning in simulation is especially promising for building on
recent results using deep reinforcement learning to achieve human-level
performance on tasks like Atari [@mnih2015human] and robotic control
[@levine2016end; @schulman2015trust]. Deep reinforcement learning
employs random exploration, which can be dangerous on physical hardware.
It often requires hundreds of thousands or millions of samples
[@mnih2015human], which could take thousands of hours to collect, making
it impractical for many applications. Ideally, we could learn policies
that encode complex behaviors entirely in simulation and successfully
run those policies on physical robots with minimal additional training.

Unfortunately, discrepancies between physics simulators and the real
world make transferring behaviors from simulation challenging. *System
identification*, the process of tuning the parameters of the simulation
to match the behavior of the physical system, is time-consuming and
error-prone. Even with strong system identification, the real world has
*unmodeled physical effects* like nonrigidity, gear backlash,
wear-and-tear, and fluid dynamics that are not captured by current
physics simulators. Furthermore, *low-fidelity simulated sensors* like
image renderers are often unable to reproduce the richness and noise
produced by their real-world counterparts. These differences, known
collectively as the *reality gap*, form the barrier to using simulated
data on real robots.

<figure id="fig:main_fig" data-latex-placement="t">
<embed src="main_figure_v5.pdf" style="width:100.0%" />
<figcaption>Illustration of our approach. An object detector is trained
on hundreds of thousands of low-fidelity rendered images with random
camera positions, lighting conditions, object positions, and
non-realistic textures. At test time, the same detector is used in the
real world with no additional training.</figcaption>
</figure>

This paper explores *domain randomization*, a simple but promising
method for addressing the reality gap. Instead of training a model on a
single simulated environment, we randomize the simulator to expose the
model to a wide range of environments at training time. The purpose of
this work is to test the following hypothesis: if the variability in
simulation is significant enough, models trained in simulation will
generalize to the real world with no additional training.

Though in principle domain randomization could be applied to any
component of the reality gap, we focus on the challenge of transferring
from low-fidelity simulated camera images. Robotic control from camera
pixels is attractive due to the low cost of cameras and the rich data
they provide, but challenging because it involves processing
high-dimensional input data. Recent work has shown that supervised
learning with deep neural networks is a powerful tool for learning
generalizable representations from high-dimensional inputs
[@lecun2015deep], but deep learning relies on a large amount of labeled
data. Labeled data is difficult to obtain in the real world for precise
robotic manipulation behaviors, but it is easy to generate in a physics
simulator.

We focus on the task of training a neural network to detect the location
of an object. Object localization from pixels is a well-studied problem
in robotics, and state-of-the-art methods employ complex,
hand-engineered image processing pipelines (e.g.,
[@collet2010efficient], [@collet2011moped], [@tang2012textured]). This
work is a first step toward the goal of using deep learning to improve
the accuracy of object detection pipelines. Moreover, we see sim-to-real
transfer for object localization as a stepping stone to transferring
general-purpose manipulation behaviors.

We find that for a range of geometric objects, we are able to train a
detector that is accurate to around 1.5 cm in the real world using only
simulated data rendered with simple, algorithmically generated textures.
Although previous work demonstrated the ability to perform robotic
control using a neural network pretrained on ImageNet and fine-tuned on
randomized rendered pixels [@sadeghi2016cad], this paper provides the
first demonstration that domain randomization can be useful for robotic
tasks requiring precision. We also provide an ablation study of the
impact of different choices of randomization and training method on the
success of transfer. We find that with a sufficient number of textures,
pre-training the object detector using real images is unnecessary. To
our knowledge, this is the first successful transfer of a deep neural
network trained *only* on simulated RGB images to the real world for the
purpose of robotic control.

# RELATED WORK

## Object detection and pose estimation for robotics

Object detection and pose estimation for robotics is a well-studied
problem in the literature (see, e.g., [@collet2009object],
[@collet2011moped], [@collet2010efficient], [@ekvall2005object],
[@tang2012textured], [@wunsch1997real], [@zickler2006detection]). Recent
approaches typically involve offline construction or learning of a 3D
model of objects in the scene (e.g., a full 3D mesh model
[@tang2012textured] or a 3D metric feature representation
[@collet2011moped]). At test time, features from the test data (e.g.,
Scale-Invariant Feature Transform \[SIFT\] features [@gordon2006and] or
color co-occurrence histograms [@ekvall2005object]) are matched with the
3D models (or features from the 3D models). For example, a black-box
nonlinear optimization algorithm can be used to minimize the
re-projection error of the SIFT points from the object model and the 2D
points in the test image [@collet2009object]. Most successful approaches
rely on using multiple camera frames [@collet2010efficient] or depth
information [@tang2012textured]. There has also been some success with
only monocular camera images [@collet2009object].

Compared to our method, traditional approaches require less extensive
training and take advantage of richer sensory data, allowing them to
detect the full 3D pose of objects (position and orientation) without
any assumptions about the location or size of the surface on which the
objects are placed. However, our approach avoids the challenging problem
of 3D reconstruction, and employs a simple, easy to implement deep
learning-based pipeline that may scale better to more challenging
problems.

## Domain adaptation

The computer vision community has devoted significant study to the
problem of adapting vision-based models trained in a source domain to a
previously unseen target domain (see, e.g., [@duan2012learning],
[@Hoffman_NIPS2014], [@hoffman2013efficient], [@kulis2011you],
[@long2015learning], [@mansour2009domain], [@yang2007cross]). A variety
of approaches have been proposed, including re-training the model in the
target domain (e.g., [@yosinski2014transferable]), adapting the weights
of the model based on the statistics of the source and target domains
(e.g., [@li2016revisiting]), learning invariant features between domains
(e.g., [@tzeng2014deep]), and learning a mapping from the target domain
to the source domain (e.g., [@taigman2016unsupervised]). Researchers in
the reinforcement learning community have also studied the problem of
domain adaptation by learning invariant feature representations
[@gupta2016feature], adapting pretrained networks
[@rusu2016progressive], and other methods. See [@gupta2016feature] for a
more complete treatment of domain adaptation in the reinforcement
learning literature.

In this paper we study the possibility of transfer from simulation to
the real world *without* performing domain adaptation.

## Bridging the reality gap

Previous work on leveraging simulated data for physical robotic
experiments explored several strategies for bridging the reality gap.

One approach is to make the simulator closely match the physical reality
by performing system identification and using high-quality rendering.
Though using realistic RGB rendering alone has had limited success for
transferring to real robotic tasks [@james20163d], incorporating
realistic simulation of depth information can allow models trained on
rendered images to transfer reasonably well to the real world
[@planche2017depthsynth]. Combining data from high-quality simulators
with other approaches like fine-tuning can also reduce the number of
labeled samples required in the real world [@richter2016playing].

Unlike these approaches, ours allows the use of low-quality renderers
optimized for speed and not carefully matched to real-world textures,
lighting, and scene configurations.

Other work explores using domain adaptation techniques to bridge the
reality gap. It is often faster to fine-tune a controller learned in
simulation than to learn from scratch in the real world
[@cutler2015efficient; @kolter2007learning]. In [@ghadirzadeh2017deep],
the authors use a variational autoencoder trained on simulated data to
encode trajectories of motor outputs corresponding to a desired behavior
type (e.g., reaching, grasping) as a low-dimensional latent code. A
policy is learned on real data mapping features to distributions over
latent codes. The learned policy overcomes the reality gap by choosing
latent codes that correspond to the desired physical behavior via
exploration.

Domain adaptation has also been applied to robotic vision. Rusu et al.
[@rusu2016sim] explore using the progressive network architecture to
adapt a model that is pre-trained on simulated pixels, and find it has
better sample efficiency than fine-tuning or training in the real-world
alone. In [@tzeng2016adapting], the authors explore learning a
correspondence between domains that allows the real images to be mapped
into a space understood by the model. While both of the preceding
approaches require reward functions or labeled data, which can be
difficult to obtain in the real world, Mitash and collaborators
[@mitash2017self] explore pretraining an object detector using realistic
rendered images with randomized lighting from 3D models to bootstrap an
automated learning learning process that does not require manually
labeling data and uses only around 500 real-world samples.

A related idea, *iterative learning control*, employs real-world data to
improve the dynamics model used to determine the optimal control
behavior, rather than using real-world data to improve the controller
directly. Iterative learning control starts with a dynamics model,
applies the corresponding control behavior on the real system, and then
closes the loop by using the resulting data to improve the dynamics
model. Iterative learning control has been applied to a variety of
robotic control problems, from model car control (e.g.,
[@abbeel2006using] and [@cutler2014reinforcement]) to surgical robotics
(e.g., [@van2010superhuman]).

Domain adaptation and iterative learning control are important tools for
addressing the reality gap, but in contrast to these approaches, ours
requires no additional training on real-world data. Our method can also
be combined easily with most domain adaptation techniques.

Several authors have previously explored the idea of using domain
randomization to bridge the reality gap.

In the context of physics adaptation, Mordatch and collaborators
[@mordatch2015ensemble] show that training a policy on an ensemble of
dynamics models can make the controller robust to modeling error and
improve transfer to a real robot. Similarly, in
[@antonova2017reinforcement], the authors train a policy to pivot a tool
held in the robot's gripper in a simulator with randomized friction and
action delays, and find that it works in the real world and is robust to
errors in estimation of the system parameters.

Rather than relying on controller robustness, Yu et al.
[@yu2017preparing] use a model trained on varied physics to perform
system identification using online trajectory data, but their approach
is not shown to succeed in the real world. Rajeswaran et al.
[@rajeswaran2016epopt] explore different training strategies for
learning from an ensemble of models, including adversarial training and
adapting the ensemble distribution using data from the target domain,
but also do not demonstrate successful real-world transfer.

Researchers in computer vision have used 3D models as a tool to improve
performance on real images since the earliest days of the field (e.g.,
[@nevatia1977description], [@lowe1987three]). More recently, 3D models
have been used to augment training data to aid transferring deep neural
networks between datasets and prevent over-fitting on small datasets for
tasks like viewpoint estimation [@su2015render] and object detection
[@sun2014virtual], [@movshovitz2016useful]. Recent work has explored
using only synthetic data for training 2D object detectors (i.e.,
predicting a bounding box for objects in the scene). In
[@peng2015learning], the authors find that by pretraining a network on
ImageNet and fine-tuning on synthetic data created from 3D models,
better detection performance on the PASCAL dataset can be achieved than
training with only a few labeled examples from the real dataset.

In contrast to our work, most object detection results in computer
vision use realistic textures, but do not create coherent 3D scenes.
Instead, objects are rendered against a solid background or a randomly
chosen photograph. As a result, our approach allows our models to
understand the 3D spatial information necessary for rich interactions
with the physical world.

Sadeghi and Levine's work [@sadeghi2016cad] is the most similar to our
own. The authors demonstrate that a policy mapping images to controls
learned in a simulator with varied 3D scenes and textures can be applied
successfully to real-world quadrotor flight. However, their experiments
-- collision avoidance in hallways and open spaces -- do not demonstrate
the ability to deal with high-precision tasks. Our approach also does
not rely on precise camera information or calibration, instead
randomizing the position, orientation, and field of view of the camera
in the simulator. Whereas their approach chooses textures from a dataset
of around $200$ pre-generated materials, most of which are realistic,
our approach is the first to use only non-realistic textures created by
a simple random generation process, which allows us to train on hundreds
of thousands (or more) of unique texturizations of the scene.

# METHOD

Given some objects of interest $\{s_i\}_i$, our goal is to train an
object detector $d(I_0)$ that maps a single monocular camera frame $I_0$
to the Cartesian coordinates $\{(x_i, y_i, z_i)\}_i$ of each object. In
addition to the objects of interest, our scenes sometimes contain
distractor objects that must be ignored by the network. Our approach is
to train a deep neural network in simulation using domain randomization.
The remainder of this section describes the specific domain
randomization and neural network training methodology we use.

## Domain randomization

The purpose of domain randomization is to provide enough simulated
variability at training time such that at test time the model is able to
generalize to real-world data. We randomize the following aspects of the
domain for each sample used during training:

- Number and shape of distractor objects on the table

- Position and texture of all objects on the table

- Textures of the table, floor, skybox, and robot

- Position, orientation, and field of view of the camera

- Number of lights in the scene

- Position, orientation, and specular characteristics of the lights

- Type and amount of random noise added to images

Since we use a single monocular camera image from an uncalibrated camera
to estimate object positions, we fix the height of the table in
simulation, effectively creating a 2D pose estimation task. Random
textures are chosen among the following:

1.  A random RGB value

2.  A gradient between two random RGB values

3.  A checker pattern between two random RGB values

The textures of all objects are chosen uniformly at random -- the
detector does not have access to the color of the object(s) of interest
at training time, only their size and shape. We render images using the
MuJoCo Physics Engine's [@todorov2012mujoco] built-in renderer. This
renderer is not intended to be photo-realistic, and physically plausible
choices of textures and lighting are not needed.

Between $0$ and $10$ distractor objects are added to the table in each
scene. Distractor objects on the floor or in the background are
unnecessary, despite some clutter (e.g., cables) on the floor in our
real images.

Our method avoids calibration and precise placement of the camera in the
real world by randomizing characteristics of the cameras used to render
images in training. We manually place a camera in the simulated scene
that approximately matches the viewpoint and field of view of the real
camera. Each training sample places the camera randomly within a
$(10 \times 5 \times 10)$ cm box around this initial point. The viewing
angle of the camera is calculated analytically to point at a fixed point
on the table, and then offset by up to $0.1$ radians in each direction.
The field of view is also scaled by up to 5 % from the starting point.

## Model architecture and training

<figure id="fig:model_architecture" data-latex-placement="h!">
<embed src="model_architecture.pdf" style="width:100.0%" />
<figcaption>The model architecture used in our experiments. Each
vertical bar corresponds to a layer of the model. ReLU nonlinearities
are used throughout, and max pooling occurs between each of the
groupings of convolutional layers. The input is an image from an
external webcam downsized to <span
class="math inline">(224 × 224)</span> and the output of the network
predicts the <span
class="math inline">(<em>x</em>, <em>y</em>, <em>z</em>)</span>
coordinates of object(s) of interest.</figcaption>
</figure>

We parametrize our object detector with a deep convolutional neural
network. In particular, we use a modified version the VGG-16
architecture [@simonyan2014very] shown in Figure
[2](#fig:model_architecture){reference-type="ref"
reference="fig:model_architecture"}. We chose this architecture because
it performs well on a variety of computer vision tasks, and because it
has a wide availability of pretrained weights. We use the standard VGG
convolutional layers, but use smaller fully connected layers of sizes
$256$ and $64$ and do not use dropout. For the majority of our
experiments, we use weights obtained by pretraining on ImageNet to
initialize the convolutional layers, which we hypothesized would be
essential to achieving transfer. In practice, we found that using random
weight initialization works as well in most cases.

We train the detector through stochastic gradient descent on the $L_2$
loss between the object positions estimated by the network and the true
object positions using the Adam optimizer [@kingma2014adam]. We found
that using a learning rate of around $1\mathrm{e}{-4}$ (as opposed to
the standard $1\mathrm{e}{-3}$ for Adam) improved convergence and helped
avoid a common local optimum, mapping all objects to the center of the
table.

# EXPERIMENTS

## Experimental Setup

<figure data-latex-placement="h!">
<img src="all_objs.jpeg" style="width:80.0%" />
<figcaption>The geometric objects used in our experiments.</figcaption>
</figure>

We evaluated our approach by training object detectors for each of eight
geometric objects. We constructed mesh representations for each object
to render in the simulator. Each training sample consists of (a) a
rendered image of the object and one or more distractors (also from
among the geometric object set) on a simulated tabletop and (b) a label
corresponding to the Cartesian coordinates of the center of mass of the
object in the world frame.

For each experiment, we performed a small hyperparameter search,
evaluating combinations of two learning rates ($1 \mathrm{e}{-4}$ and
$2\mathrm{e}{-4}$) and three batch sizes ($25$, $50$, and $100$). We
report the performance of the best network.

The goals of our experiments are:

1.  Evaluate the localization accuracy of our trained detectors in the
    real world, including in the presence of distractor objects and
    partial occlusions

2.  Assess which elements of our approach are most critical for
    achieving transfer from simulation to the real world

3.  Determine whether the learned detectors are accurate enough to
    perform robotic manipulation tasks

[]{#table:maintable label="table:maintable"}

::: {#table:maintable}
+-------------------------------------------------------------------------------------------------+
| **Detection error for various objects, cm**                                                     |
+:==============:+:========================:+:========================:+:========================:+
| Evaluation     | Object only              | Distractors              | Occlusions               |
| type           |                          |                          |                          |
+----------------+--------------------------+--------------------------+--------------------------+
| Cone           | $1.3 \pm 1.1$[^4]        | $1.5 \pm 1.0$            | $1.4 \pm 0.6$            |
+----------------+--------------------------+--------------------------+--------------------------+
| Cube           | $1.3 \pm 0.6$            | $1.8 \pm 1.2$            | $1.4 \pm 0.6^{\text{1}}$ |
+----------------+--------------------------+--------------------------+--------------------------+
| Cylinder       | $1.1 \pm 0.9^{\text{1}}$ | $1.9 \pm 2.8$            | $1.9 \pm 2.9$            |
+----------------+--------------------------+--------------------------+--------------------------+
| Hexagonal      | $0.7 \pm 0.5$            | $0.6 \pm 0.3^{\text{1}}$ | $1.0 \pm 1.0^{\text{1}}$ |
| Prism          |                          |                          |                          |
+----------------+--------------------------+--------------------------+--------------------------+
| Pyramid        | $0.9 \pm 0.3^{\text{1}}$ | $1.0 \pm 0.5^{\text{1}}$ | $1.1 \pm 0.7^{\text{1}}$ |
+----------------+--------------------------+--------------------------+--------------------------+
| Rectangular    | $1.3 \pm 0.7$            | $1.2 \pm 0.4^{\text{1}}$ | $0.9 \pm 0.6$            |
| Prism          |                          |                          |                          |
+----------------+--------------------------+--------------------------+--------------------------+
| Tetrahedron    | $0.8 \pm 0.4^{\text{1}}$ | $1.0 \pm 0.4^{\text{1}}$ | $3.2 \pm 5.8$            |
+----------------+--------------------------+--------------------------+--------------------------+
| Triangular     | $0.9 \pm 0.4^{\text{1}}$ | $0.9 \pm 0.4^{\text{1}}$ | $1.9 \pm 2.2$            |
| Prism          |                          |                          |                          |
+----------------+--------------------------+--------------------------+--------------------------+
:::

## Localization accuracy

To evaluate the accuracy of learned detectors in the real world, we
captured $480$ webcam images of one or more geometric objects on a table
at a distance of 70 cm--105 cm from the camera. The camera position
remains constant across all images. We did not control for lighting
conditions or the rest of the scene around the table (e.g., all images
contain part of the robot and tape and wires on the floor). We measured
ground truth positions for a single object per image by aligning the
object on a grid on the tabletop. Each of the eight geometric objects
has 60 labeled images in the dataset: $20$ with the object alone on the
table, $20$ in which one or more distractor objects are present on the
table, and $20$ in which the object is also partially occluded by
another object.

Table I summarizes the performance of our models on the test set. Our
object detectors are able to localize objects to within 1.5 cm (on
average) in the real world and perform well in the presence of clutter
and partial occlusions. Though the accuracy of our trained detectors is
promising, note that they are still over-fitting[^5] the simulated
training data, where error is 0.3 cm--0.5 cm. Even with over-fitting,
the accuracy is comparable at a similar distance to the translation
error in traditional techniques for pose estimation in clutter from a
single monocular camera frame [@collet2011moped] that use
higher-resolution images.

## Ablation study

To evaluate the importance of different factors of our training
methodology, we assessed the sensitivity of the algorithm to the
following:

- Number of training images

- Number of unique textures seen in training

- Use of random noise in pre-processing

- Presence of distractors in training

- Randomization of camera position in training

- Use of pre-trained weights in the detection model

We found that the method is at least somewhat sensitive to all of the
factors except the use of random noise.

<figure id="fig:amt_data" data-latex-placement="h!">
<img src="scaling_v3-19.png" style="width:100.0%" />
<figcaption>Sensitivity of test error on real images to the number of
simulated training examples used. Each training example corresponds to a
single labeled example of an object on the table with between 0 and 10
distractor objects. Lighting and all textures are randomized between
iterations. </figcaption>
</figure>

Figure [4](#fig:amt_data){reference-type="ref" reference="fig:amt_data"}
shows the sensitivity to the number of training samples used for
pre-trained models and models trained from scratch. Using a pre-trained
model, we are able to achieve relatively accurate real-world detection
performance with as few as $5,000$ training samples, but performance
improves up to around $50,000$ samples.

Figure [4](#fig:amt_data){reference-type="ref" reference="fig:amt_data"}
also compares to the performance of a model trained from scratch (i.e.,
without using pre-trained ImageNet weights). Our hypothesis that
pre-training would be essential to generalizing to the real world proved
to be false. With a large amount of training data, random weight
initialization can achieve nearly the same performance in transferring
to the real world as does pre-trained weight initialization. The best
detectors for a given object were often those initialized with random
weights. However, using a pre-trained model can significantly improve
performance when less training data is used.

Figure [5](#fig:amt_textures){reference-type="ref"
reference="fig:amt_textures"} shows the sensitivity to the number of
unique texturizations of the scene when trained on a fixed number
($10,000$) of training examples. We found that performance degrades
significantly when fewer than $1,000$ textures are used, indicating that
for our experiments, using a large number of random textures (in
addition to random distractors and object positions) is necessary to
achieving transfer. Note that when $1,000$ random textures are used in
training, the performance using $10,000$ images is comparable to that of
using only $1,000$ images, indicating that in the low data regime,
texture randomization is more important than randomization of object
positions.[^6]

<figure id="fig:amt_textures" data-latex-placement="h!">
<img src="texture_ablation.png" style="width:100.0%" />
<figcaption>Sensitivity to amount of texture randomization. In each
case, the detector was trained using <span
class="math inline">10, 000</span> random object positions and
combinations of distractors, but only the given number of unique
texturizations and lighting conditions were used.</figcaption>
</figure>

Table II examines the performance of the algorithm when random noise,
distractors, and camera randomization are removed in training.
Incorporating distractors during training appears to be critical to
resilience to distractors in the real world. Randomizing the position of
the camera also consistently provides a slight accuracy boost, but
reasonably high accuracy is achievable without it. Adding noise during
pretraining appears to have a negligible effect. In practice, we found
that adding a small amount of random noise to images at training time
improves convergence and makes training less susceptible to local
minima.

[]{#table:ablation label="table:ablation"}

::: {#table:ablation}
+-------------------------------------------------------------------------------+
| **Average detection error on geometric shapes by method, cm[^7]**             |
+:==============:+:==================:+:==================:+:==================:+
| Evaluation     | *Real images*                                                |
+----------------+--------------------+--------------------+--------------------+
| 2-4 type       | Object only        | Distractors        | Occlusions         |
+----------------+--------------------+--------------------+--------------------+
| Full method    | $\bf{1.3 \pm 0.6}$ | $\bf{1.8 \pm 1.7}$ | $\bf{2.4 \pm 3.0}$ |
+----------------+--------------------+--------------------+--------------------+
| No noise added | $1.4 \pm 0.7$      | $1.9 \pm 2.0$      | $\bf{2.4 \pm 2.8}$ |
+----------------+--------------------+--------------------+--------------------+
| No camera      | $2.0 \pm 2.1$      | $2.4 \pm 2.3$      | $2.9 \pm 3.5$      |
| randomization  |                    |                    |                    |
+----------------+--------------------+--------------------+--------------------+
| No distractors | $1.5 \pm 0.6$      | $7.2 \pm 4.5$      | $7.4 \pm 5.3$      |
| in training    |                    |                    |                    |
+----------------+--------------------+--------------------+--------------------+
:::

## Robotics experiments

To demonstrate the potential of this technique for transferring robotic
behaviors learned in simulation to the real world, we evaluated the use
of our object detection networks for localizing an object in clutter and
performing a prescribed grasp. For two of our most consistently accurate
detectors, we evaluated the ability to pick up the detected object in 20
increasingly cluttered scenes using the positions estimated by the
detector and off-the-shelf motion planning software [@moveit]. To test
the robustness of our method to discrepancies in object distributions
between training and test time, some of our test images contain
distractors placed at orientations not seen during training (e.g., a
hexagonal prism placed on its side).

We deployed the pipeline on a Fetch robot [@wise2016fetch], and found it
was able to successfully detect and pick up the target object in 38 out
of 40 trials, including in highly cluttered scenes with significant
occlusion of the target object. Note that the trained detectors have no
prior information about the color of the target object, only its shape
and size, and are able to detect objects placed closely to other objects
of the same color.

To test the performance of our object detectors on real-world objects
with non-uniform textures, we trained an object detector to localize a
can of Spam from the YCB Dataset [@calli2015ycb]. At training time, the
can was present on the table along with geometric object distractors. At
test time, instead of using geometric object distractors, we placed
other food items from the YCB set on the table. The detector was able to
ignore the previously unseen distractors and pick up the target in 9 of
10 trials.

Figure [6](#fig:grasping){reference-type="ref" reference="fig:grasping"}
shows examples of the robot grasping trials. For videos, please visit
the web page associated with this paper.[^8]

<figure id="fig:grasping" data-latex-placement="t!">
<img src="grasping_vF.png" style="width:100.0%" />
<figcaption>Two representative executions of grasping objects using
vision learned in simulation only. The object detector network estimates
the positions of the object of interest, and then a motion planner plans
a simple sequence of motions to grasp the object at that
location.</figcaption>
</figure>

# CONCLUSION

We demonstrated that an object detector trained only in simulation can
achieve high enough accuracy in the real world to perform grasping in
clutter. Future work will explore how to make this technique reliable
and effective enough to perform tasks that require contact-rich
manipulation or higher precision.

Future directions that could improve the accuracy of object detectors
trained using domain randomization include:

- Using higher resolution camera frames

- Optimizing model architecture choice

- Introducing additional forms of texture, lighting, and rendering
  randomization to the simulation and training on more data

- Incorporating multiple camera viewpoints, stereo vision, or depth
  information

- Combining domain randomization with domain adaptation

Domain randomization is a promising research direction toward bridging
the reality gap for robotic behaviors learned in simulation. Deep
reinforcement learning may allow more complex policies to be learned in
simulation through large-scale exploration and optimization, and domain
randomization could be an important tool for making such policies useful
on real robots.

::: thebibliography
10

Pieter Abbeel, Morgan Quigley, and Andrew Y Ng. Using inaccurate models
in reinforcement learning. In *Proceedings of the 23rd international
conference on Machine learning*, pages 1--8. ACM, 2006.

Rika Antonova, Silvia Cruciani, Christian Smith, and Danica Kragic.
Reinforcement learning for pivoting task. , 2017.

Berk Calli, Arjun Singh, Aaron Walsman, Siddhartha Srinivasa, Pieter
Abbeel, and Aaron M Dollar. The ycb object and model set: Towards common
benchmarks for manipulation research. In *Advanced Robotics (ICAR), 2015
International Conference on*, pages 510--517. IEEE, 2015.

Alvaro Collet, Dmitry Berenson, Siddhartha S Srinivasa, and Dave
Ferguson. Object recognition and full pose registration from a single
image for robotic manipulation. In *Robotics and Automation, 2009.
ICRA'09. IEEE International Conference on*, pages 48--55. IEEE, 2009.

Alvaro Collet, Manuel Martinez, and Siddhartha S Srinivasa. The moped
framework: Object recognition and pose estimation for manipulation. ,
30(10):1284--1306, 2011.

Alvaro Collet and Siddhartha S Srinivasa. Efficient multi-view object
recognition and full pose estimation. In *Robotics and Automation
(ICRA), 2010 IEEE International Conference on*, pages 2050--2055. IEEE,
2010.

Mark Cutler and Jonathan P How. Efficient reinforcement learning for
robots using informative simulated priors. In *Robotics and Automation
(ICRA), 2015 IEEE International Conference on*, pages 2605--2612. IEEE,
2015.

Mark Cutler, Thomas J Walsh, and Jonathan P How. Reinforcement learning
with multi-fidelity simulators. In *Robotics and Automation (ICRA), 2014
IEEE International Conference on*, pages 3888--3895. IEEE, 2014.

Lixin Duan, Dong Xu, and Ivor Tsang. Learning with augmented features
for heterogeneous domain adaptation. , 2012.

Staffan Ekvall, Danica Kragic, and Frank Hoffmann. Object recognition
and pose estimation using color cooccurrence histograms and geometric
modeling. , 23(11):943--955, 2005.

Ali Ghadirzadeh, Atsuto Maki, Danica Kragic, and Mårten Björkman. Deep
predictive policy training using reinforcement learning. , 2017.

Iryna Gordon and David G Lowe. What and where: 3d object recognition
with accurate pose. In *Toward category-level object recognition*, pages
67--82. Springer, 2006.

Abhishek Gupta, Coline Devin, YuXuan Liu, Pieter Abbeel, and Sergey
Levine. Learning invariant feature spaces to transfer skills with
reinforcement learning. , 2017.

Judy Hoffman, Sergio Guadarrama, Eric Tzeng, Ronghang Hu, Jeff Donahue,
Ross Girshick, Trevor Darrell, and Kate Saenko. Lsda: Large scale
detection through adaptation. In *Neural Information Processing
Symposium (NIPS)*, 2014.

Judy Hoffman, Erik Rodner, Jeff Donahue, Trevor Darrell, and Kate
Saenko. Efficient learning of domain-invariant image representations. ,
2013.

Stephen James and Edward Johns. 3d simulation for robot arm control with
deep q-learning. , 2016.

Diederik Kingma and Jimmy Ba. Adam: A method for stochastic
optimization. , 2014.

J Zico Kolter and Andrew Y Ng. Learning omnidirectional path following
using dimensionality reduction. In *Robotics: Science and Systems*,
2007.

Brian Kulis, Kate Saenko, and Trevor Darrell. What you saw is not what
you get: Domain adaptation using asymmetric kernel transforms. In
*Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference
on*, pages 1785--1792. IEEE, 2011.

Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. ,
521(7553):436--444, 2015.

Sergey Levine, Chelsea Finn, Trevor Darrell, and Pieter Abbeel.
End-to-end training of deep visuomotor policies. , 17(39):1--40, 2016.

Yanghao Li, Naiyan Wang, Jianping Shi, Jiaying Liu, and Xiaodi Hou.
Revisiting batch normalization for practical domain adaptation. , 2016.

Mingsheng Long, Yue Cao, Jianmin Wang, and Michael I Jordan. Learning
transferable features with deep adaptation networks. In *ICML*, pages
97--105, 2015.

David G Lowe. Three-dimensional object recognition from single
two-dimensional images. , 31(3):355--395, 1987.

Yishay Mansour, Mehryar Mohri, and Afshin Rostamizadeh. Domain
adaptation: Learning bounds and algorithms. , 2009.

Chaitanya Mitash, Kostas E Bekris, and Abdeslam Boularias. A
self-supervised learning system for object detection using physics
simulation and multi-view pose estimation. , 2017.

Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel
Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K
Fidjeland, Georg Ostrovski, et al. Human-level control through deep
reinforcement learning. , 518(7540):529--533, 2015.

Igor Mordatch, Kendall Lowrey, and Emanuel Todorov. Ensemble-cio:
Full-body dynamic motion planning that transfers to physical humanoids.
In *Intelligent Robots and Systems (IROS), 2015 IEEE/RSJ International
Conference on*, pages 5307--5314. IEEE, 2015.

Yair Movshovitz-Attias, Takeo Kanade, and Yaser Sheikh. How useful is
photo-realistic rendering for visual learning? In *Computer Vision--ECCV
2016 Workshops*, pages 202--217. Springer, 2016.

Ramakant Nevatia and Thomas O Binford. Description and recognition of
curved objects. , 8(1):77--98, 1977.

Xingchao Peng, Baochen Sun, Karim Ali, and Kate Saenko. Learning deep
object detectors from 3d models. In *Proceedings of the IEEE
International Conference on Computer Vision*, pages 1278--1286, 2015.

Benjamin Planche, Ziyan Wu, Kai Ma, Shanhui Sun, Stefan Kluckner,
Terrence Chen, Andreas Hutter, Sergey Zakharov, Harald Kosch, and Jan
Ernst. Depthsynth: Real-time realistic synthetic data generation from
cad models for 2.5 d recognition. , 2017.

Aravind Rajeswaran, Sarvjeet Ghotra, Sergey Levine, and Balaraman
Ravindran. Epopt: Learning robust neural network policies using model
ensembles. , 2016.

Stephan R Richter, Vibhav Vineet, Stefan Roth, and Vladlen Koltun.
Playing for data: Ground truth from computer games. In *European
Conference on Computer Vision*, pages 102--118. Springer, 2016.

Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer,
James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, and Raia Hadsell.
Progressive neural networks. , 2016.

Andrei A Rusu, Matej Vecerik, Thomas Rothörl, Nicolas Heess, Razvan
Pascanu, and Raia Hadsell. Sim-to-real robot learning from pixels with
progressive nets. , 2016.

Fereshteh Sadeghi and Sergey Levine. (cad) 2 RL: Real single-image
flight without a single real image. , 2016.

John Schulman, Sergey Levine, Pieter Abbeel, Michael I Jordan, and
Philipp Moritz. Trust region policy optimization. In *ICML*, pages
1889--1897, 2015.

Karen Simonyan and Andrew Zisserman. Very deep convolutional networks
for large-scale image recognition. , 2014.

Hao Su, Charles R Qi, Yangyan Li, and Leonidas J Guibas. Render for cnn:
Viewpoint estimation in images using cnns trained with rendered 3d model
views. In *Proceedings of the IEEE International Conference on Computer
Vision*, pages 2686--2694, 2015.

Ioan A Sucan and Sachin Chitta. Moveit! .

Baochen Sun and Kate Saenko. From virtual to reality: Fast adaptation of
virtual object detectors to real domains. In *BMVC*, volume 1, page 3,
2014.

Yaniv Taigman, Adam Polyak, and Lior Wolf. Unsupervised cross-domain
image generation. , 2016.

Jie Tang, Stephen Miller, Arjun Singh, and Pieter Abbeel. A textured
object recognition pipeline for color and depth image data. In *Robotics
and Automation (ICRA), 2012 IEEE International Conference on*, pages
3467--3474. IEEE, 2012.

Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for
model-based control. In *Intelligent Robots and Systems (IROS), 2012
IEEE/RSJ International Conference on*, pages 5026--5033. IEEE, 2012.

Eric Tzeng, Coline Devin, Judy Hoffman, Chelsea Finn, Pieter Abbeel,
Sergey Levine, Kate Saenko, and Trevor Darrell. Adapting deep visuomotor
representations with weak pairwise constraints. In *Workshop on the
Algorithmic Foundations of Robotics (WAFR)*, 2016.

Eric Tzeng, Judy Hoffman, Ning Zhang, Kate Saenko, and Trevor Darrell.
Deep domain confusion: Maximizing for domain invariance. , 2014.

Jur Van Den Berg, Stephen Miller, Daniel Duckworth, Humphrey Hu, Andrew
Wan, Xiao-Yu Fu, Ken Goldberg, and Pieter Abbeel. Superhuman performance
of surgical tasks by robots using iterative learning from human-guided
demonstrations. In *Robotics and Automation (ICRA), 2010 IEEE
International Conference on*, pages 2074--2081. IEEE, 2010.

Melonee Wise, Michael Ferguson, Derek King, Eric Diehr, and David
Dymesich. Fetch and freight: Standard platforms for service robot
applications. In *Workshop on Autonomous Mobile Service Robots*, 2016.

Patrick Wunsch and Gerd Hirzinger. Real-time visual tracking of 3d
objects with dynamic handling of occlusion. In *Robotics and Automation,
1997. Proceedings., 1997 IEEE International Conference on*, volume 4,
pages 2868--2873. IEEE, 1997.

Jun Yang, Rong Yan, and Alexander G Hauptmann. Cross-domain video
concept detection using adaptive svms. In *Proceedings of the 15th ACM
international conference on Multimedia*, pages 188--197. ACM, 2007.

Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. How
transferable are features in deep neural networks? In *Advances in
neural information processing systems*, pages 3320--3328, 2014.

Wenhao Yu, C Karen Liu, and Greg Turk. Preparing for the unknown:
Learning a universal policy with online system identification. , 2017.

Stefan Zickler and Manuela M Veloso. Detection and localization of
multiple objects. In *Humanoid Robots, 2006 6th IEEE-RAS International
Conference on*, pages 20--25. IEEE, 2006.
:::

# APPENDIX {#appendix .unnumbered}

## Randomly generated samples from our method

Figure [7](#fig:random_samples){reference-type="ref"
reference="fig:random_samples"} displays a selection of the images used
during training for the object detectors detailed in the paper.

<figure id="fig:random_samples" data-latex-placement="h">
<img src="example_imgs.png" style="width:92.0%" />
<figcaption>A selection of randomly textured scenes used in the training
phase of our method</figcaption>
</figure>

[^1]: $^{1}$OpenAI and UC Berkeley EECS, `josh@openai.com`

[^2]: $^{2}$OpenAI, `{rfong, aray, jonas, woj}@openai.com`

[^3]: $^{3}$OpenAI, UC Berkeley EECS & ICSI, `pieter@openai.com`

[^4]: Categories for which the best final performance was achieved for
    detector trained from scratch.

[^5]: Overfitting in this setting is more subtle than in the standard
    supervised learning where train and test data come from the same
    distribution. In the standard supervised learning setting
    overfitting can be avoided by using a hold-out set during training.
    We do apply this idea to ensure that we are not overfitting on the
    simulated data. However, since our goal is to learn from training
    data originated in the simulator and generalize to test data
    originated from the real world, we assume to not have any real world
    data available during training. Therefore no validation on real data
    can be done during training.

[^6]: Note the total number of textures is higher than the number of
    training examples in some of these experiments because every scene
    has many surfaces, each with its own texture.

[^7]: Each of the models compared was trained with $20,000$ training
    examples

[^8]: <https://sites.google.com/view/domainrandomization/>
