---
layout: post
title: "One variable linear regression model"
subtitle: "Introduction to ML. Linear Regression. Gradient Descent."
date: 2026-03-16 09:00:00 +0000
categories: ['Maths', 'ML']
tags: ['Maths','DeepLearning.ai']
author: German Sanmi
---

# 0. Index.

- 1. Machine Learning.
    - 1.2. Learning Models.
        - 1.2.1. Supervised Learning.
            - 1.2.1.1. Definition.
            - 1.2.1.2.  Linear Regression: The simpliest Supervised Learning Model instantiation.
        - 1.2.2. Unsupervised Learning. Clustering.
- 2. Regression Model.
    - 2.1. Linear Regression Overview.
    - 2.2. Training the machine.
    - 2.3. Cost Function.
        - 2.3.1. Squared Error.
        - 2.3.2. Interpretation. Optimization Problem.

- 3. Gradient Descent.
    - 3.1. Introducing the problem.
    - 3.2. Gradient Descent Algorithm.

    <br>
    
# 1. Machine Learning.

In conventional programming, explicit rules are taught to programs in order to establish solid logic predicates about constraints or bifurcations over the execution flow of the program. Machine Learning is a computer science discipline that interact or modules program logic inverting the order, instead of giving directives, you give to a program input values and desired outputs related by an unknown relation from the program perspective. Then the program objective is to infere that unknown relation in order to aproximate the computation of the inputs as most as posible to the real-desired output.

Mathematically, we would have an unknown function $f$ relation two values, $(x,y) : y =f(x)$. The program aims to find a parameter $\theta$ such the resulting function aproximates $x$ to $y$ as much as posible:

$$\Set{f_\theta : \theta \in \Theta} : f_{\theta}(x) \simeq f(x) = y$$

In some sense, we built an inteligent program which deduce the unknown relation between $x$ and $y$ through an approximation which fails in an acceptable negligible percentaje of the cases.

<br>

In other terms, *Machine Learning* is a field of study that gives computers the ability to learn without being explictly programmed

<br>

## 1.2. Learning Models.

We've alrady formuled the subject, giving a family of parametrized function $\mathcal{H} := \Set{f_\theta : \theta \in \Theta}$ find a $\theta^*$ such:

$$\theta^* = \arg\min_{\theta \in \Theta} \frac{1}{n} \sum_{i=1}^{n} \ell(f_\theta(x_i),y_i)$$

Which means, minimize the error between the aproximation $f_\theta(x)$ to $f(x)$. 

In this context, the *machine learning algorithm* is the strategy followed to find $\theta^*$. Formally is conceptualized as a function which takes a training set of data of related inputs and outputs and return what we call an hipotesis, which a presumibly optime parametrized function:

$$ \begin{gather} A: (\mathcal{X} \times \mathcal{Y)^n} \to \mathcal{H} \\ \ \ \   \Set{(x_i,y_i)}_{i=1}^n \to h\end{gather}$$

<br>

 We distinguish between the following learning frameworks:

- *Supervised Learning*
- *Unsupervised Learning*
- *Reinforcement Learning*

<br>

### 1.2.1. Supervised Learning.

#### 1.2.1.1. Definition.

Supervised Learning is one the three best well-known learning models, which trains a program to infere a relation between two data sets (input and outputs). 

This training model relays on the fact that the program count with a collection of pairs of inputs and outputs related by an unknown rule: $(x,y) \in \mathcal{X} \times \mathcal{Y} : y = f(x)$, and $f$ remains unknown (this function is typically an unknown joint distribution $P(X,Y)$, stochastic relation, the function is a concrete case where all noise vanish). 

In this sense, *supervised* learning refers that during training (algorthim execution), every input, $x$ comes with a label $y$; a correct answer that "supervises" the learning process. 

In this sense, the task of supervised learning is, given the training the set: $\mathcal{D} = \{ (x^{(i)}, y^{(i)}) \}_{i=1}^{n} \subset \mathcal{X} \times \mathcal{Y}$ find some hipotesis $h : \mathcal{X} \to \mathcal{Y}$ of some hipotesis class $\mathcal{H}$ that minimizes the *expected risk* given by: $R(h) = \mathbb{E}_{(X,Y)}\bigl[\ell(h(X),Y)\bigr]$, where the function  $\ell : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\ge 0}$ is the *loss function*; measuring prediction error. 

Also, taking again that $f$ is a simplification of $P$, in general, what is measured is the *empirical risk* instead:

$$\hat{R}(h) = \frac{1}{n} \sum_{i=1}^{n} \ell\bigl(h(x^{(i)}), y^{(i)}\bigr)$$

which basically measure the risk over the gathered sample instead of the entire population (which often is unnaccesible in real problems).

<br>

#### 1.2.1.2.  Linear Regression: The simpliest Supervised Learning Model instantiation.

*Linear Regression* is the simpliest instantiation of the Supervised Learning Model. 

Let's take a moment two introduce the *affine* concept. *Linear* and *Affine* are forms to apply transformations over the data on a set of points which satisfies specific conditions. 

- *Linearity* applies a scalar transformation over the data, in linear algebra we did learn that a linear transformation $f$ satisfies:

    $$f(\alpha u + \beta v) = \alpha f(u) + \beta f(v) \implies 0 \to 0$$

    <br>

- *Affinity* can be described as a linear transformation incorporating a *traslation*, being $f: V \to W$ a linear transformation between two vector spaces, then we can consider an *affine transformation* $t: V \to W$ as:

    $$t = f + b : b \in W$$

    Where $b$ takes the rol of the translation.

    <br>

Now, suposse it is: $\mathcal{X} = \mathbb{R}^d \wedge \mathcal{Y} = \mathbb{R}$ the problem, fixed this sets, is predict a real-valued output from a vector of features. The core assumption of linear regression is that the relationship between input and output is *affine*, meaning that the hypothesis class is:

$$\mathcal{H} := \Set{h_\theta : x \to \theta^{\top}x + b \ \vert \ \theta \in \mathbb{R}^d \wedge b \in \mathbb{R}}$$

The reasong for which we force the hipotesis to be an affine transformation is because for many types of relation between a set of parameters and the data, a linear application simply doesn't fit, for example a professional with $0$ years of experience doesn't receive a salary of $0$, the relation between the experience in a professional industry and the salary exists and is documented but is not linear.

Thus, suppose we have $n$ observations, each observation is a pair $(x^{(i)},y^{(i)}) \in \mathcal{X} \times \mathcal{Y}$ where the output is roughly determined by the input, with some noise on top: $y^{(i)} = f(x^{(i)}) + \varepsilon^{(i)}$ (this is the affine relation we talk above), then the linear regression is the decision to search only among affine maps as candidates for $f$:

![regression_lineal](/assets/images/ML/regression_lineal.png)

<br>

#### 1.2.1.3. Clasification Models.

Before, we've introduced Regression models with Linear Regression but we will cover that topic more extensively later.

No we gonna cover the Classification Model, we've already internalized the regression setup: you have a hypothesis $h : \mathcal{X} \times \mathcal{Y}$ that predicts a continuous response, $h$ is continous at any point which only makes sense if $\mathcal{Y}$ is isomorph to some subset of $\mathbb{R}^n : n \in\mathbb{N}$. Classification arises when this hipotesis is no longuer continous, in the sense that $\mathcal{Y}$ is a discrete set. 

In regression we talked about an error aproximation through the loss function $\ell$ which tries to predict how far the prediction is from the desired output in a geometric "metric" sense, you care of the magnitude of the error, how far you are. In classification, being $\mathcal{Y}:= \Set{1,...,k}$ there is no meaningful notion of "distance"; when you predict a wrong class in $Y$, there is no near notion to the correct answer in the sense that class $1$ isn't more closer or much better than class $7$ when the desired output is class $3$, there are only right or wrong answers.

This collapses $\ell$ to the *0-1 loss*, which counts missclasifications:

$$\ell(h(x),y) = \mathbf{1}[h(x) \ne y]$$

In regression you minimize empirical risk with a continuous loss (squared error, absolute error), and the hypothesis class consists of functions $h: \mathcal{X} \to \mathbb{R}$. In classification you minimize empirical risk with a discrete loss (0-1 loss), and the hypothesis class consists of functions $h: \mathcal{X} \to \Set{1,..., k}$

![classification](/assets/images/ML/clasification.png)

Then, basically, clasification models force the machine to recognise previously labeled class (minimizing the error function results) by using the hipotesis $h$ over the input $x$ data and identifying it in some value of the discrete codomain $y$.

<br>

### 1.2.2. Unsupervised Learning. Clustering.

The idea in a high scale is that, in contrast of supervised learning, the labeling of the output $y$ dissapear, there are no wrong answer when apply the hipotesis on the data. The task for the algorith is to find structures in the data; clusters.

In Classification there is a training set $\Set{(x_i​,y_i​)}_{i=1}^n$​ where the labels $y_i$ where given by an oracle, in the sense that is desired output. Then, the task is to find a map that approximates $x \to y$ as much as posible. Observe that the categories exists before the algorithm starts the distinction.

Clustering inverts this relationship. The training set consist only in $\Set{x_i​}_{i=1}^n$ (without labels). The task is to discover that there are groups at all, and to assign each point to one. The categories are not predefined; they emerge from the geometric or distributional structure of the data itself. The fundamental assumption behind clustering is that the data is not uniformly spread across $\mathcal{X}$. but concentrates around certain regions. Clustering algorithms formalize different notions of what "concentrate" means:

- *Centroid-based*; structure means proximity to a representative point.

- *Density-based*; structure means regions of high density separated by regions of low density.

- *Distributional*; structure means the data was plausibly generated by a mixture and inference on the latent component assignments.

Each of these is a different inductive bias about what a "cluster" is.

The comparison is more subtle than "one has labels, the other doesn't."

The problem is ill-defined in a way classification is not. 

- In classification, given a loss function and a hypothesis class, the optimal classifier is a well-defined object (the Bayes classifier, the ERM solution, etc.). 

- In clustering, there is no unique "correct" partition, the answer depends on your notion of similarity, the number of clusters $k$ (often a hyperparameter you must choose), and the scale at which you look. Two entirely different clusterings of the same data can both be "valid."

<br>

# 2. Regression Model.

## 2.1. Linear Regression Overview.

Now, we gonna dive in the Linear Regression Model, this is the learning algorithm most widely used and many of the concepts used to explain it applies other training algorithms.

Let's clear that, Linear Regression is an instantiation of what we call Supervised Learning, which is a training model that consist on first train the machine with previously labeled data $(x,y)$, where $x$ is called as the *input feature* data and $y$ is the *output target* variable (the expected output). Also is important to know that we count with a finite number of traning pairs $n$. 

When you finish the training, you let the machine to predict output for new unlabeled data.

<br>

Each training pair is reflected in a *Cartesian coordinate system* forming a cloud of points. As we said before, linear regression consist in the assumption that the relation between each pair is an affin transformation, or simply a line:

![regression_lineal](/assets/images/ML/regression_lineal.png)

The notation $(x^{(i)},y^{(i)}) \in \mathcal{X} \times \mathcal{Y}$ referes that we are treating te i-th pair in the sample. Also, each pair is reflect in a table oppositing $x$ and $y$ in a $n$-row table:


| pair | x | y | 
| - | - | - |
| $1$ | $x^{(1)}$ | $y^{(1)}$ |
| ... | ... | ... |
| $n$ | $x^{(n)}$ | $y^{(n)}$ | 

<br>

## 2.2. Training the machine.

Remember that the training algorthim's job is two form a function $f$ with the provided training set such the transformation of an input feature $x$ by $f$, the prediction; $f(x)=\hat{y}$, is approximated enough to the target $y$; expected output ; $\hat{y} \to y$.

As we say before, *linear regression* assumes that $f$ is represented as a straight line in the graph of the form:

$$\hat{y} = f_{w,b}(x) := wx + b : w,b \in \mathbb{R}$$

Later we will see other forms of regression which involves other forms of non-linear forms in the graph, but as a foundation, the linear mathematical object is fine enough to manipulate.

<br>

## 2.3. Cost Function.

### 2.3.1. Squared Error.

Until now, we stablished that inear regression is about a finite training set that is represented in a coordinate system. We want a line such $y = wx + b$ that represents well enough the relation between the points.

Let's now dive what *well enough* means. Well enough means that minimizes the error in the prediction, let's now see what we call error and how to measure it.

The most natural thing to measure is the *residual*: how far off is the prediction from the true:

$$e^{(i)}= \hat{y}^{(i)} - y ^{(i)}$$

So in intuitive terms, the thing we want to measure is $\displaystyle \sum_{i=1}^{n}e^{(i)}$, but positive and negative terms can cancel out and erase part of the information.

The two natural candidates to solve the problem, $\vert e^{(i)} \vert$ and square $(e^{(i)})^2$, the reason why we decide to square is because is differentiable at any point (we will understand this later);$\displaystyle \sum_{i=1}^{n}(e^{(i)})^2$

Now we take the average (so the cost doesn't scale arbitrarily with dataset size):

$$\displaystyle \frac{1}{n} \sum_{i=1}^{n}(e^{(i)})^2$$

This is the *Mean Squared Error*. It gives you a single number that summarizes how badly the line misses the data on average and is essentially what we are measuring.

In practice you'll almost always see a factor of $\frac{1}{2}$ thrown in front:

$$J(w,b) := \frac{1}{2m} \sum_{i=1}^{m} \bigl(f_{w,b}(x^{(i)}) - y^{(i)}\bigr)^2$$

This doesn't change which $(w,b)$ minimizes $J$ (it's just a positive constant scaling). It's there purely for convenience: when you take the derivative, the exponent $2$ comes down and cancels with the $\frac{1}{2}$​, giving you cleaner gradient expressions.

<br>

### 2.3.2. Interpretation. Optimization Problem.

Let's observe that $J(w,b)=0$ means that every single squared residual is zero, which forces each prediction to coincide with the labeled value; $f_{w,b}(x^{(i)}) = y^{(i)} \ \ \forall (x^{(i)},y^{(i)}) \in P(x,y)$ 

As $J$ increases, the line deviates more. This way, $J$ defines an ordering on parameter pairs $(w,b)$ lower $J$ means a better-fitting line. Finding the best line is now a clean optimization problem; minimize $J$ over $(w,b) \in \mathbb{R}^2$.

One thing worth noting: $J$ being zero is typically impossible (or undesirable) with real data, since the data has noise. But the key property holds $J$ is non-negative, equals zero only at perfect fit, and increases monotonically with the aggregate deviation of predictions from targets.

<br>

# 3. Gradient Descent.

We just saw that, in linear regression model we assume that exists an affine transformation $f_{w,b}(x) := wx + b$ that makes a solid prediction over the labeled points $(x,y) \in \mathcal{X} \times \mathcal{Y}$. We also say that a way to measure how "solid" is this line is to build our Cost Function reprented as: $J(w,b) = \frac{1}{2m} \sum_{i=1}^{m} \bigl(f_{w,b}(x^{(i)}) - y^{(i)}\bigr)^2$ and we stablish it as an optimization problem over the $(w,b) \in \mathbb{R}^2$ that minimizes $J$ value as much as posible.

Now, *Gradient Descent* taught us an way to consistently seach about $(w,b)$ pairs.

<br>

## 3.1. Introducing the problem.

We have the *Mean Squared Error*; $J(\theta)$, which measures the average distance-error between the predicted values $\hat{y}$ and the labeled values $y$, and we want to find that parameter $\theta^*$ that minimizes that error. 

For a simple system, for example a continous one-variable function on a real segment, we calculate $\nabla J(\theta) = 0$:

$$\nabla J(\theta) :=
    \begin{pmatrix}
    \frac{\partial J}{\partial \theta_1}(\theta)\\
    \frac{\partial J}{\partial \theta_2}(\theta)\\
    \vdots\\
    \frac{\partial J}{\partial \theta_n}(\theta)
    \end{pmatrix}\quad \underbrace{\implies}_{n=1} \quad \nabla J(\theta) := \frac{\partial J}{\partial \theta}(\theta) = \frac{dJ(\theta)}{d\theta} = J'(\theta) = 0$$

<br>

![delta0](/assets/images/ML/delta0.png)

But the moment the parameter space grows, that closed-form solution either doesn't exist or becomes computationally prohibitive. An iterative method is needed.

<br>

## 3.2. Gradient Descent Algorithm.

Gradient Descent exploits one fundamental fact from calculus: the gradient $\nabla J(\theta)$ points in the direction of steepest ascent of $J$ at $\theta$, meaning that "decrease" $J$ implies move $\theta$ towards the opposite direction of $\nabla J$:


$$\theta^{(t+1)} := \theta^{(t)} - \alpha \,\nabla J(\theta^{(t)}): \alpha \in \mathbb{R}^+$$

Where $\alpha$ is the *learning rate* and controls the step size.

This way, computing $\nabla_\theta J$ gives you *a concrete vector that tells you how each parameter contributes to the error*. In the sense that each component $\frac{\partial J}{\partial \theta_j}$​ tells you how $J$ (the error) changes, let's have in mind the image above, $\theta$ always advance from left towards right, this means that:

- If $\frac{\partial J}{\partial \theta_j} > 0$, then the function is ascending and is moving away from the minimum, $\theta$ has overshot the minimum to the right so subtract a positive value $\alpha · \frac{\partial J}{\partial \theta}$ to $\theta$ nudges $\theta$ to the left, hence $J$ towards the minimum.

- If $\frac{\partial J}{\partial \theta_j} < 0$, then the function is descending and is approaching to the minimum, $\theta$ has the minimum in front, to the right, so subtract a negative value $\alpha · \frac{\partial J}{\partial \theta}$ is like add a positive one, nudging $\theta$ forward and hence $J$ towards the minimum.

So, the sign always corrects the direction in both cases.

It is worth to note that convexity matters. For linear regression, $J$ is convex, there's a single global minimum and gradient descent will find it (given a reasonable $\alpha$). For neural networks, $J$ is non-convex with many local minima and saddle points.

<br>

It is also worth noting that, as $J$ gets closer to the minimum, the derivative term gets smaller in absolute terms, meaning that the term substracted to $\theta$ is smaller, so $J$ advance more slowly to the minimum as it gets closer through Gradient Descent.

<br>

