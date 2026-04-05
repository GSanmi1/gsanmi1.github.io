---
layout: post
title: "Machine Learning. Regression Model"
subtitle: "Introduction to ML. Linear Regression. Gradient Descent."
date: 2026-03-16 09:00:00 +0000
categories: ['Maths', 'ML']
tags: ['Maths','DeepLearning.ai']
author: German Sanmi
---

# 0. Index.

1. Machine Learning.
    - 1.2. Learning Models.
        - 1.2.1. Supervised Learning.
            - 1.2.1.1. Definition.
            - 1.2.1.2.  Linear Regression: The simpliest Supervised Learning Model instantiation.
        - 1.2.2. Unsupervised Learning. Clustering.
2. Regression Model.
    - 2.1. Linear Regression Overview.
    - 2.2. Training the machine.
    - 2.3. Cost Function.
        - 2.3.1. Squared Error.
        - 2.3.2. Interpretation. Optimization Problem.

3. Gradient Descent.
    - 3.1. Introducing the problem.
    - 3.2. Gradient Descent Algorithm.

    <br>
    
# 1. Machine Learning.

In conventional programming, explicit rules are taught to programs in order to establish solid logic predicates about constraints or bifurcations over the execution flow of the program. 

Machine Learning is a family of algorithms that learn patterns from data instead of following explicitly programmed rules. In other terms, *Machine Learning* is a field of study that gives computers the ability to learn without being explictly programmed.

<br>

## 1.2. Formal Framing.

Let's understand what "learning from data" actually mathematically means; the objective is to find a function that captures the regularity of an observed phenomenon that produces data in order to make predictions on new, unseen inputs of the same nature.

Formally, we hace the following pieces:

- An *input space* the set of all possible inputs. For instance $\mathcal{X} = \mathbb{R}^n$, this each input $x$ is a vector of $n$ features.

- An *output space* $\mathcal{Y}$, which is the set of all posible outputs. This depends on what is being modelized, in clasification problems the output set can be a finite subset of the natural numbers which are the clusters, $\mathcal{Y} = [n]$, for regression, which wants to predict a continuos value is; $\mathcal{Y} = \mathbb{R}$.

- The *target function*, the ideal mapping $\mathcal{X} \to \mathcal{Y}$ that relates each input $x \in \mathcal{X}$ to the desired output $y \in \mathcal{Y}$ which is abstracted in the application $f : \mathcal{X} \to \mathcal{Y}$ and remains unknown.

- The *training set*; a finite subset $\mathcal{D} \subset \mathcal{X} \times \mathcal{Y}$ defined as $\mathcal{D} := \Set{(x_i,y_i)}_{i=1}^m : y_i = f(x_i)$

The goal of ML is to use $\mathcal{D}$ to find a mapping $g_{\mathcal{D}}:\mathcal{X} \to \mathcal{Y} : g_\mathcal{D} \approx f$. Observe that $g_\mathcal{D}$, by definition, allow us to make prediction along all the $\mathcal{X} \times \mathcal{Y}$ space, this is, not only for the inputs from $\mathcal{D}_\mathcal{X}$ but for any $x \in \mathcal{X}$. 

<br>

We don't search across all possible functions $f: \mathcal{X} \to \mathcal{Y}$ that set is unimaginably large and the problem would be ill-defined. Instead, we choose a *hypothesis set*; $\mathcal{H}$, which is a restricted family of candidate functions. A *learning algorithm* select one of the candidates of $\mathcal{H}$ as $g_\mathcal{D}$.

For example, *linear regression* learning model is a supervised learning model (we will see what his is later) in which we assume that $\mathcal{H}$ is the set of all the affine transformations $\mathbb{R}^n \to \mathbb{R}$.

<br>

## 1.3. Learning Algorithm.

As we set in the previous section, we need to develop a mechanism that allow us to select the best candidate from a family of applications $\mathcal{H}$ that mapps correctly - matching our needs - the input $\mathcal{X}$ with the outpus $\mathcal{Y}$ using only the training set $\mathcal{D} \subset \mathcal{X} \times \mathcal{Y}$ established before as a reference. As a overall, this selection is based on the question about what $h \in \mathcal{H}$ minimizes as much as posible the noise or incorrections in the mapping $\mathcal{X} \to \mathcal{Y}$ done by $h$.

The *learning algorithm* is the procedure that actually performs this search. In practice, for the vast majority of modern ML, this reduces to a continuous optimization problem: minimize a real-valued function (the *loss function*; the one that measures the error over the predictions) over a space of parameters.

<br>

### 1.3.1. Mathematical Prerrequisites.

#### 1.3.1.1. Functions of Several Variables.

A function of $n$ real variables is a map:

$$f : S \to \mathbb{R} , \quad S \subset \mathbb{R}^{n}$$

Where:

- $S$ is the evaluation domain
- $\mathbb{R}$ is the codomain

Then, the input is a vector with $n$ coordinates $x := (x_1,\cdots,x_n) \in \mathbb{R}^n$ and the image of $x$ through $f, f(x) \in \mathbb{R}$ is a real scalar.

Is worth to visualize that for $n = 2$, the plot of $f(x,y)$ on $x,y$ is a surface given by the parameters $(x,y,f(x,y)) \in \mathbb{R}^3$, $f(x,y)$ is the height in the plane formed by the coordinates $(x,y) \in \mathbb{R}^2$. Now, if $n >3$ the geometric visualization breaks, while the maths holds in the sense that $f(x)$ is the height to each point of $\mathbb{R}^n$.

In ML, the models we work with depend on a vector of adjustable parameters $\boldsymbol{\theta} \in \mathbb{R}^p$ where $p$ depends on the model architecture and can range from a handful to billions. Training these models requires understanding how each parameter affects the output, which demands the machinery of functions of several variables.

<br>

#### 1.3.1.2. Partial Derivatives.

Let be now $ f: S \to \mathbb{R}, \quad S \subseteq \mathbb{R}^n$ a multivariable function, lets choose a point $\mathbf{a}:=(a_1,\ldots,a_n) \in S$.

Then, we define the **partial derivative of $f$ respect to $x_i$ at $\mathbf{a}$** as (provided this limit exists):

$$\frac{\partial f}{\partial x_i}(\mathbf{a}) = \lim_{t \to 0} \frac{f(\mathbf{a} + te_i) - f(\mathbf{a})}{t} =  $$

$$ = \lim_{t \to 0} \frac{f(a_1,\ldots,a_{i-1}, a_i + t, a_{i+1},\ldots,a_n) - f(a_1,\ldots,a_n)}{t} $$

Where $e_i$ is the $i$-th standard basis vector.

Is important to note the partial derivatives is just the extension of the single-variable derivative applied to a multivariable function on one single feature $x_i$ meaning that the scalar $t \in \mathbb{R}$ pertubartes only the $i$-th coordinate (literally an ordinary single-variable derivative applied to a function where all variables except one have been frozen to constants). 

A formal treatment is to define $g_i: \mathbb{R} \to \mathbb{R}$ from $f$ by:

$$g_i(t) = f(a_1,\ldots,a_{i-1},t,a_{i+1},\ldots,a_n)$$

Then, the partial derivative acquire other representation:

$$\frac{\partial f}{\partial x_i}(\mathbf{a}) = g'_i(a_i) = \lim_{h \to 0} \frac{g_i(a_i + h)-g_i(a_i)}{h}$$

A simple exchange $g_i \leftrightarrow f$ returns to us the original definition, but this shape gives a more intuitively approach since we can understand the partial derivative from our understanding from the single-derivative concept with which we are already familiar.

The formula above tell us that the partial derivative tell us how $f$ changes under a minimal (differential) change of the $i$-th feature mantaining the rest variables as constants.

<br>

**Geometric Interpretation**

Let's take the case $n=2$, the graph of $f : \mathbb{R}^2 \to \mathbb{R}$ is a surface on $\mathbb{R}^3$; $(x,y,f(x,y)) \in \mathbb{R}^3$. 

In this context, the function $g_x:\mathbb{R} \to \mathbb{R} \ \vert \ g_x(t) := f(t,y_0)$ describes the curve of $f$ in the plane $(x,f(x,y_0)) \in \mathbb{R}^2$ which is the section given by the plane $y=y_0$ on the surface $(x,y,f(x,y)) \in \mathbb{R}^3$

This way, $\frac{\partial f}{\partial x}(a) = g_x'(a)$ is the slope of the tangent line to that curve at the point $(a_1,a_2,f(a_1,a_2))$. The geometric interpretation of the single-variable derivative carries over directly: you are just reading the slope on a specific *slice* of the surface:

![partial1](/assets/images/ML/partial1.png)

In general, the graph of $f:\mathbb{R}^n \to \mathbb{R}$ is a hypersurface in $\mathbb{R}^{n+1}$, freezing all coordinates except $x_i$ defines a line in $\mathbb{R}^n$, the image of that line under the graph map $x \mapsto (x, f(x))$  is a curve on the hypersurface, and $D_i​f(\mathbf{a})$ is the slope of the tangent line to that curve.

<br>

In summary, partial derivatives measures how $f$ changes when we adjust one parameter while keeping all others fixed. This is a need to form the gradient which basically is a vector that tells us the movement tend of $f$ at a point in $\mathbb{R}^n$

<br>

#### 1.3.1.3. Directional Derivatives.

**Definition**

Let's barely introduce what the directional derivative is. 

Observe that the partial derivatives we've just presented above measure the change ratio along the coordinate that isn't frozen. In the example we proposed, the curve is the intersection of the surface with the plane $y = y_0$, thus, the partial derivative explore how $f$ changes along the $x$ coordinate axis.

Thus, partial derivatives measure rates of change along coordinate axes, now directional derivatives introduce how to measure this change along virtually any direction. The directional derivative generalizes partial derivatives to arbitrary directions. 

Let $E \subseteq \mathbb{R}^n$ be open, and let $f: E \to \mathbb{R}$ be differentiable at $\mathbf{a} \in E$. Then, we define the *directional derivative* of $f$ at $\mathbf{a}$ with respect to the $i$-th variable is:

$$D_{\mathbf{u}} f(\mathbf{a}) = \lim_{t \to 0} \frac{f(\mathbf{a}+t\mathbf{u}) - f(\mathbf{a})}{t}$$

Where $\mathbf{u}$ is an unit vector, a vector with direction but without magnitud (this is so to speak, the module is $\vert \vert u \vert \vert = 1$, thus it not disturb the magnitud of any other vector). Lets take a closer look. 

If is $\mathbf{u} := (u_1,\ldots,u_n) \in \mathbb{R}^n : \vert \vert u \vert \vert = 1$, then $t\mathbf{u}$ is a scalar multiplication on $\mathbf{u}$, 

$$t\mathbf{u}:=(tu_1,\ldots,tu_n) \implies \mathbf{a} + t\mathbf{u} := (a_1 +tu_1,\ldots, a_n+tu_n)$$

Every coordinate gets perturbed simultaneously, each by the amount $tu_i$​. The vector $\mathbf{u}$ controls the *direction* of the perturbation, and the scalar $t$ controls how far you go in that direction.

<br>

**Geometric Interpretation**

This means that the geometric interpretation remains the same, but now the plane contains the line passing through the point $\mathbf{a}$ with the direction of the unit vector $\mathbf{u}$. This plane is no longer paralel to any coordinate axis but it extends in the direction of $\mathbf{u}$.

As a visual example, for $f:\mathbb{R}^2 \to \mathbb{R}$ the intersection of this plane and the surface give us a *curve* containing $(\mathbf{a},f(\mathbf{a}))$, then $D_uf(\mathbf{a})$ is the slop of the tangent line to the curve at $\mathbf{a}$

![directional1](/assets/images/ML/directional1.png)

<br>


#### 1.3.1.4. Gradient.

**Definition**

Consider now $f: S \subset \mathbb{R}^n \to \mathbb{R}$ and a point $\mathbf{a} \in \mathbb{R}^n: \exists \partial_if(\mathbf{a}) \ \forall i \in [n]$. We define as the *gradient* of $f$ at $\mathbf{a}$ to the vector:

$$\nabla f(\mathbf{a}) := 
\begin{pmatrix}
\frac{\partial f}{\partial x_1}(\mathbf{a})\\
\vdots\\
\frac{\partial f}{\partial x_n}(\mathbf{a})
\end{pmatrix} \in \mathbb{R}^n$$

Observe that the gradient lives in the domain of $f$, $\mathbb{R}^n$, not in the codomain $\mathbb{R}$.

<br>

**Geometric Interpretation**

Now, lets recover the directional derivative definition: 

$$D_{\mathbf{u}} f(\mathbf{a}) = \lim_{t \to 0} \frac{f(\mathbf{a}+t\mathbf{u}) - f(\mathbf{a})}{t}$$

Observe that, by the chain rule, we have the following result (here we assume that $f'(x) = \nabla f(x)$):

$$D_\mathbf{u} f(\mathbf{a}) = \nabla f(\mathbf{a})\ · \mathbf{u}$$

Let see for a moment that in $\mathbb{R}^2$  is $\nabla f(\mathbf{a})\ · \mathbf{u} = \Vert \nabla f(\mathbf{a}) \Vert \Vert \mathbf{u} \Vert \cos\theta$, which means that $D_\mathbf{u} f(\mathbf{a})$ is maximum when $\mathbf{u}$ and $\nabla f(\mathbf{a})$ has the same direction $\cos\theta = 1 \implies \theta = 0 \pmod {2\pi}$. For superior dimensions, this result can be proved by the Cauchy-Schwarz inequality. 

Thus, in general, the gradient $\nabla f(\mathbf{a})$ always points towards the direction in which the slope of the tangent line to the curve (in the surface, as we see in above definitions) $D_\mathbf{u}f(\mathbf{a})$ is maximum, this is what we call the *steepest ascent* direction.

Then $-\nabla f(\mathbf{a})$ always points towards the direction in which the slope is minimum, the *stepest descent* direction. This geometric property justifies the *gradient descent algorithm* we will see later.

<br>

### 1.3.2. Formal Development.

#### 1.3.2.1. Hypothesis Sets.

As we say before, we don't search for an hipotesys $h$ in abstract, we first form a family of candidates $\mathcal{H}$. This is a parameterized by a vector of real numbers $\theta \in  \mathbb{R}^p$:

$$\mathcal{H} := \Set{h_\theta : \mathcal{X} \to \mathcal{Y} \ \vert \ \theta \in \Theta}$$

Where, 

- $\theta = (\theta_1, \ldots, \theta_p) \in \mathbb{R}^p$. 

    Is the parameter vector. Each specific $\theta$ picks out one specific hypothesis $h_{\theta} \in \mathcal{H}$​.

- $p \in \mathbb{R}$, is the number of parameters (in modern deep learning, $p$ can be in the billions).

- $\Theta \subseteq \mathbb{R}^p$ is the parameter space over all $\mathbb{R}^p$

<br>

**Linear Model**

As a brief example, let's take a look over the *linear model*, which, as we said before, is the assumption about $h$ is an affine transformation. Remember that an affine transformation is a linear transformation $y=mx$ plus a traslation $b$, taking the form of the line: $y_{m,b} := b + mx$,then in our parameterized function:

$$h_\theta(\mathbf{x}) := \theta_0 + \boldsymbol{\theta^{\top}} · \  \mathbf{x} = \theta_0 + \sum_{i=1}^p \theta_i x_i$$

Where $\theta_0$ is the bias and $\theta_i \ \forall i \in [p]$ is parameter of the $i$-th feature $x_i$. Observe that each $\theta$ give us a different linear function.

<br>

#### 1.3.2.2. Measuring the error. Cost function.

It is reasonable to ask, for a certain $\theta$, how far the prediction is from the real, labeled, output. Formally; for a pair $(x,y) \in \mathcal{X} \times \mathcal{Y}$, how wrong is the prediction $h_\theta(x)$, let's first formalize the notion of 'wrong' in mathematical terms.

<br>

**Loss Function**

Let's define:

$$L : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\geq 0}$$

$L(y,h_\theta(x))$ takes the true value $y$ and the predicted value $h_\theta(x)$ and returns a non-negative real number: the
penalty for that single prediction. The larger $L(y,h_\theta(x))$, the worse the prediction.

The loss function is a design choice; different losses encode different priorities about what kinds of errors matter in base of the space in which the output set is defined. For example, applied to the linear regression model, the output space is $\mathbb{R}$ which is a metric space, thus, the *loss function* adopts the form of the *squared loss*; penalizes errors proportionally to the square of the deviation; large errors are punished disproportionately.

$$L(y,h_\theta(x)) := (y - h_\theta(x))^2$$

But note that $L$ only measures error at a single point. A model doesn't predict one point; it predicts across the entire input space. We need to aggregate.

<br>

**True Risk**

The natural next question: how wrong is $h_{\boldsymbol{\theta}}$​ across all the input space. 

Ideally, we would measure the *expected loss over the entire data-generating process*. The data comes from some unknown probability distribution $P$ over $\mathcal{X} \times \mathcal{Y}$, this unknown probability pattern associates inputs to outputs in what we call the phenomenon data. Think for example in the height and the age of a person, is the formal way of saying "nature produces input-output pairs according to some pattern".

<br>

The population risk, also called *true risk*, of a hypothesis $h$ is:

$$R(h) = \mathbb{E}_{(x,y) \sim P}\big[L(y, h(x))\big]$$

This is a sum (or integral, in the continuous case) over all possible pairs $(x, y) \in \mathcal{X} \times \mathcal{Y}$, each weighted by its probability under $P$. It captures the average error of $h$ across the entire distribution, including inputs you'll never see in your training set.

This the object we truly want to minimize. It captures how well $h$ performs on
all data, including data we haven't seen. 

However, the fundamental problem is we cannot compute $R(h)$ since is based on $P$ and the distribution $P$ is unknown (if we knew it, we would know $f$, and there would be no learning problem). $R(h)$ is a theoretical ideal, not a computable quantity.

<br>

**Empirical Risk**

A reasonable approximation to the *true risk* (based on $P$) is the *empirical risk* based on a dataset we have access to: $\mathcal{D}$. The empirical risk of $h$ on $\mathcal{D}$ is:

$$\hat{R}_{\mathcal{D}}(h) = \frac{1}{m}\sum_{i=1}^{m} L\big(y^{(i)}, h(x^{(i)})\big)$$

Observe that, as a discrete, finite sample, the expected value $\mathbb{E}_{(x,y) \sim P}$ converge to a sum. Each training example gets weight as $\frac{1}{m}$, we treat them all equally because we don't know $P$ so we assume that they are all probably equal.


This is the average loss computed on the $m$ training examples a quantity we can compute, because we know every $(x^{(i)}, y^{(i)}) \in \mathcal{X} \times \mathcal{Y}$ and we can evaluate $h(x^{(i)})$.

The empirical risk is a *finite-sample estimate* of the true risk. Under reasonable conditions, the law of large numbers guarantees that as $m \to \infty \implies \hat{R}_{\mathcal{D}}(h) \to R(h)$. 

<br>

At this point, we would think that an acceptable strategy to chose $h_\theta$ is to choose an $h$  that minimizes $\hat{R}_{\mathcal{D}}$​, is what we call the *Empirical Risk Minimization*:

$$h^* = \arg\min_{h \in \mathcal{H}} \hat{R}_{\mathcal{D}}(h)$$

Let's observe that $\min_{a\in A}​f(a)$ is the minimum value $f$ returns in a subset of his evaluation domain, then $\arg\min_{a\in A}​f(a)$ is the input (the argument) that produces that minimum value.

This is conceptually clean, but still abstract because we're minimizing over a set of functions $\mathcal{H}$. To make this into an actual algorithm we can run on a computer, we need one more step.

<br>

**The Cost Function**

Since every $h \in \mathcal{H}$ is indexed by a parameter vector $\theta \in \mathbb{R}^p$, the empirical risk becomes a function of $\theta$:

$$J: \mathbb{R}^p \to \mathbb{R}, \quad J(\theta) := \hat{R}_{\mathcal{D}}(h_{\theta}) = \frac{1}{m}\sum_{i=1}^{m} L\big(y_i,\; h_{\theta}(x_i)\big)$$

This function measures the global error in the training set between the prediction and the labeled data, is the cost function (also called objective function). Observe carefully that having a provided training set $\mathcal{D}$, and an appropiated loss function $L$, the last free variable is $\theta$.

The learning problem has become to find:

$$\boldsymbol{\theta}^* = \arg\min_{\boldsymbol{\theta} \in \Theta} J(\boldsymbol{\theta})$$

Find the point in $\mathbb{R}^p$ where $J$ attains its minimum. This is a standard optimization problem where all the math presented before applies.

Each step is forced by the limitations of the previous one: $L$ only measures one point, so we average to get $R$; $R$ is not computable, so we approximate with $\hat{R}\_{\mathcal{D}}$​;$\hat{R}\_{\mathcal{D}}$​ is still abstract over $\mathcal{H}$, so we parameterize to get $J(\theta)$, which is a concrete function in $\mathbb{R}^p$ that we can differentiate and minimize with gradient descent.

<br>

### 1.3.3. Gradient Descent Algorithm.



<br>

# 2. Supervised Learning.

#### 1.2.1.1. Definition.

Supervised Learning is one the three best well-known learning models, which trains a program to infere a relation between two data sets (input and outputs). 

This training model relays on the fact that the program count with a collection of pairs of inputs and outputs related by an unknown rule: $(x,y) \in \mathcal{X} \times \mathcal{Y} : y = f(x)$, and $f$ remains unknown (this function is typically an unknown joint distribution $P(X,Y)$, stochastic relation, the function is a concrete case where all noise vanish). 

In this sense, *supervised* learning refers that during training (algorthim execution), every input, $x$ comes with a label $y$; a correct answer that "supervises" the learning process. 

In this sense, the task of supervised learning is, given the training the set: $\{ (x^{(i)}, y^{(i)}) \}\_{i=1}^{n} \subset \mathcal{X} \times \mathcal{Y}$ find some hipotesis $h : \mathcal{X} \to \mathcal{Y}$ of some hipotesis class $\mathcal{H}$ that minimizes the *expected risk*. However, taking again that $f$ is a simplification of $P$, in general, what is measured is the *empirical risk* instead which we call:

$$\hat{R}(h) = \frac{1}{n} \sum_{i=1}^{n} \ell\bigl(h(x^{(i)}), y^{(i)}\bigr)$$

which basically measure the risk over the gathered sample instead of the entire population (which often is unnaccesible in real problems).

Let's observe that this empirical risk is a template with three factors:

- The hypothesis class $h$ that makes the prediction agains the labeled data.
- The loss function $\ell$ which measures the error between each pair $(h(x)^{(i)},y^{(i)})$
- Apply a convenience scaling $\frac{1}{n}$, for convenience we can scale the empirical risk to simplify the result.

Later we will select each one of the three factors to instantiate the empirical risk into the *cost function* $J$.

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

## 2.2. Training the machine. Linear regression.

Remember that the training algorthim's job is two form a function $f$ with the provided training set such the transformation of an input feature $x$ by $f$, the prediction; $f(x)=\hat{y}$, is approximated enough to the target $y$; expected output ; $\hat{y} \to y$.

As we say before, *linear regression* assumes that $f$ is represented as a straight line in the graph of the form:

$$\hat{y} = f_{w,b}(x) := wx + b : w,b \in \mathbb{R}$$

Is worth to note that this parameters tell to us how $\hat{y}$ is built from $x$:

- $w$ represent how much $x$ contributes to $\hat{y}$, this will be clearer when linear regression model for multiple variables gets introduced; $x$ and $w$ are vectors related in $f$ by the dot product. This way each $w_i \in w$ tell us how much $x_i \in x$ feature contribute in the value of $\hat{y}$.

- $b$ as well represent how much $y$ is independant from $x$ since is a constant value not related with the input. Observe that when $x = 0$, then $\hat{y} = b$ exactly showing that this is the value that separates $\hat{y}$ from any $wx$.

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

For a simple system, for example a continous one-variable function on a real segment, we would calculate $\nabla J(\theta) = 0$:

$$\nabla J(\theta) :=
    \begin{pmatrix}
    \frac{\partial J}{\partial \theta_1}(\theta)\\
    \frac{\partial J}{\partial \theta_2}(\theta)\\
    \vdots\\
    \frac{\partial J}{\partial \theta_n}(\theta)
    \end{pmatrix}\quad \underbrace{\implies}_{n=1} \quad \nabla J(\theta) = \frac{\partial J}{\partial \theta}(\theta) = \frac{dJ(\theta)}{d\theta} = J'(\theta) = 0$$

<br>

![delta0](/assets/images/ML/delta0.png)

But in the moment the parameter space grows, that closed-form solution either doesn't exist or becomes computationally prohibitive. An iterative method is needed.

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

Observe that applying this two our linear regression model:

$$J(w,b) := \frac{1}{2m} \sum_{i=1}^{m} \bigl(f_{w,b}(x^{(i)}) - y^{(i)}\bigr)^2 \implies \nabla J(w,b) := \begin{pmatrix} \frac{\partial J(w,b)}{\partial w} \\ \frac{\partial J(w,b)}{\partial b}  \end{pmatrix}$$

Where:

$$\begin{cases}\frac{\partial J(w,b)}{\partial w} =\frac{1}{m} \sum_{i=1}^{m} \bigl(f_{w,b}(x^{(i)}) - y^{(i)}\bigr)x \\ \frac{\partial J(w,b)}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} \bigl(f_{w,b}(x^{(i)}) - y^{(i)}\bigr)  \end{cases}$$