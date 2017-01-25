
Machine learning is computational statistics. 


Getting labelled information extract more information from the dataset and create new labels.

Inducted Bias (Induction) - Going from examples to more general rule

Deductive Bias (Deduction) - Going from a general rule to specific instances. 

Supervised Learning - Function Approximation. 

Usupervised Learning - You have input and you have to derive some sort of structure from it. You label those structures. 

Supervised Learning - Functional Approximation

Unsupervised Learning - Compact Summarisation [How to devide up data] 

Function approcimation makes sense, there is an existing function that you try to approximate or model:

In general, a function approximation problem asks us to select a function among a well-defined class that closely matches ("approximates") a target function in a task-specific way.

I can really see how they belong together. 

Unsupervised learning can be helpful for supervised learning. Super >> Unsuper.  Unsuper + Super > Super. 

Take summaries as input. 

3 types, supervised, unsupervised and reinforcement learning. 

Reinforcement Learning -> Learning from delayed reward, where as supervised learning gets information from the past. 

Reinforcement is harder. 

You can turn any supervised learning problem into an unsupervised learning program. -> All one form of optimisation. 

Forms of Optimisation:
Supervised Learning -> Optimising algorithms for labelling data accurately.
Reinforcement Learning -> Optimising for behaviour that scores well.
Unsupervised Learning -> Making criteria that creates clusters that scores well.

It boils down to one thing: Data. I am not as much a computer scientists as a computationalist. I compute stuff. I know nothing of computer science. 

Algorithms and data are coequals in ML.



Instances/Input - Vectors of values [Pixels and pictures]
Concept: Function -> Mapping inputs to outputs. 
Target Concept -> The answer, what we are trying to find. 
Hypothesis Class - All concepts you are willing to entertain, can be all possible functions. 
Sample -> Training set.
Candiddate -> A potential concept
Testing Set -> Other pseudo-samples. 


Representation is the inputs or features we have to pay attention to. 

Big Data - Is the isseus you get when you have a tremendous amount of data. 

Deep Learning - It is a reboot of neural networks of the past. 

Semi-supervised learning -> A combination of super and unsuper. You label a few pages but not all of them, then you can use unsupervised learning and then create labels. 

Cascade Learning -> small probability occurences. 

Cross-entropy: Investigate this. 

Partially Observable Markov Decision Processses: Don't exately know muc about this. 

Inverse Reinforcement Learning  -> You start from behaviour and then try and identify the award system that some people are working for. Motivations and desires of people. I quite like this too. 

Game Theory:

Mathematics of conflict of interest. 
Multiple instead of single agents.
Incorporate the interest of other people.
Increasing important in ML.

Reinforcement used in decision making. 

Grids for Reinforcement Learning. 


Markov Decision Process -> Single Agent Decision Model.

States - Every state that you can be in. 

Model (Tranasition Function) -> State and Action and another State. (Action set, everythin the robot is allowed to do)

T(s,a,s') ~ P(s'|s,a)   Given that you were in state s and did action a to get there, what is the probabiliy to get to s'. 

Only the present matters. It only depends on the current state s. As long s the current state, s remembers everything from the past. Like stock arkets current price. 

Reward -> A scalar value you get for getting into the state of goal.

R(S), R(s,a), R(s,a,s') -> They are mathematically equivalent, becase the are all present, just different ways to think of it.

Policy: The solution to optimise the amount or expected amount of reward. 

We have (s a r) pairs of training samples with supervised we have  (s a_

Policy is a function that telss you what action you should take. 

Doesnt tell you what sequence you should take, it tells you what you should take once you are in a certain state. From this you can infer a plan. If you have an optimal policy. 

How do we find an MDP optimal policy. 

The notion of rewards and delayed rewards separare super and reinf. 

Take some action and get some reward: It is called the credit assignment problem. (Also called temporal credit assignment problem)

Negative awards -> like being on a hot beach, you don't just want to stand somewhere or step on hot sand, you would rather want to be in the ocean for a dollar. So you have incentives and disincentives. 4 cent everywhere BUT $1 at end. 

Making assumptions:

Assuming infinite horisons. If there was finite horisons you would have done stuff differently to make sure that you can actaully reach the plus one. 

Utility of sequences. If you prefer the states today, you would also prefer them tomorrow. Then you can just add rewards together, because you are allows to thanks to these assumptions. 

You can just add rewards if you have an infintie horison and a utility of sequences. 

Sum R(St) -> Very much like money and accumulation. 

Existential dillema of the immortal -> You don't care about anything, you will live forever. 

Create a formula, create a gamma or alpha that decreases as it goes into the future. [Discounted Rewards]

Singularity, when the computer can design its successor, in this way moors law doubles every second for example. 

This is a theoretical course, so ML is much like finance. It has a theoretical and emperical side. The theorist are more important in finance. 


Optimal policy (pie squared): argmax -> Policy that maximisises expected rewards. 


Reward for a state R(s) - This is small  U(s) - Takes the future utility into account. 

Finding Policy: Max is non-linear. 

We have n equations and n unknowns. 
Start with arbitary utilities
Update utilities based on neighbours
repeat untill convergence



RL API

Take a model, code, then policy comes out [Planning]

Now instead of model, take transitions, it learns and then finds policy [Learning]

Lab rats often gets confronted with reinforcement learning. 

Reward Maximisation (Actually not Reinforcement Learning)

Planner, Learner, Modeler (Output is a Model), Simulator (Output is transitions) -> You can basically flip things around. 

A new type of value function:


There is multiple boolean functions. Decision trees can represent boolean function. I like it. A & B  is communitive. XOR needs three nodes. Or and And has 2 nodes.

ID3. 

Generic algorithm.

Information gain - Reduction in randomness (I have actually done this) 

Continuous attributes -> Classify, interval. 

Issue is when to stop. Noise can be bad becaue then the classifications canbe wrong. 

I will do two more things in this course -> Neural Networks + Ensemble B&B.

-> Then DL .

___________________________________________________________


Neural Networks:

One Unit: 
Sum( Weight * Inputs ) i.e. activation > Firing Thereshold 
yes: y:1, n:0

-> This is a particular neural network unit called a perceptron.

So easy, take weighted inputs compare against benchmark assing a boolean value.. 

Interesting that deeplearning is the easiest implemetnation and works the best.

Awesome with the weights you can perform a DEA analysis. 

Better to do perceptron traning: 
Given examples find weights that map inputs to outputs. 

Two ways to:
Perceptron Rule (Bad when non-linearly separable) 
Gradient Descent Rule


There is perceptron units and sigmoind unit. 

Neural networks -> Whole thing is differentiable. 

A class of classifiers called Ensemble Learning.

Boosting is the best. (Subsets, instead of random choice)































































































































```python

```
