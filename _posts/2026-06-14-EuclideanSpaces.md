---
layout: post
title: "Euclidean Space"
subtitle: "Introduction to Euclidean Spaces. Metric Spaces"
date: 2026-06-16 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
subject: real-analysis
lang: en
---

# 0. Index

1. Presentation and Definition. $\mathbb{R}^k$
2. Metric Spaces.
    - 2.1. Metric definition. Metric spaces.
    - 2.2. Euclidean metric.
    - 2.3. $\mathbb{R}^k$ is a metric space with the euclidean metric.

3. Main properties of the norm in $\mathbb{R}^k$.
4. Summary.

# 1. Presentation and Definition. $\mathbb{R}^k$

A *Euclidean space* is an affine space over the reals such that the associated vector space is a euclidean vector space; a finite-dimensional inner product space over the real numbers. 


Let's consider the affine space $(\mathbb{R}^k,V,+)$ where the associated $\mathbb{R}$-vector space is $V= (\mathbb{R},(\mathbb{R}^k,+),·)$, with the operations as follows:

$$(x_1,...,x_k)+(y_1,...,y_k)=(x_1+y_1,...,x_k+y_k)$$

$$\alpha · (x_1,...,x_k) = (\alpha x_1,..., \alpha x_k)$$

Being $+: \mathbb{R}^k \times V$ a simply transitive action over $\mathbb{R}^k$

<br>

Over $V$, we define the following inner product, which we remember from the [Complex Numbers](https://gsanmi1.github.io/posts/2026/03/05/Complex_Numbers/) post, on $6.3.1$, an inner product is the object which injects geometry by defining how a vector expresses its own direction (norm), introducing the orthogonality later:

$$\quad \quad \langle x,y \rangle = x · y =\sum_{i=1}^k x_iy_i$$

In this case, this inner product receives the particular name *dot product*.

<br>

The defined *dot product* gives rise to the *norm*; for each vector $x \in \mathbb{R}^k$ it is defined:

$$\|x\| = \sqrt{ x·x}= \sqrt{\sum_{i=1}^k x_i^2}$$

Which gives us a notion of "length" of the vector. It is worth saying that this is specifically true in $\mathbb{R}^k$ where intuitive geometry matches the formal geometry instituted through the dot product.


<br>

Thus, a euclidean space is the result of injecting geometry into an affine space through a real inner product space; a real vector space with geometry.

As a consequence of the geometry injected by the inner product, we can consider a notion of proximity (metric) between the points in the affine space which allows us to introduce the notion of limit and develop the analysis.

<br>

# 2. Metric spaces.

## 2.1. Metric definition. Metric spaces.

A metric abstracts the notion of *distance*. This is an important concept since from this all the analysis departs. From the distance notion comes proximity and then limits gain sense.

A *distance* tries to capture how far two points are from each other in a non-empty set $X$. Observe that this is not an algebraic structure or algebraic property; contrary to the norm, the distance doesn't need to sum or scale.

<br>

Let $X$ be a non-empty space, then a *metric space* is a pair $(X,d)$ where: $d : X \times X \to \mathbb{R}$ is an application called *distance*, verifying:

- $M1$: Symmetry, the distance is indifferent to the point of measurement: 

    $$d(x,y)=d(y,x) \quad \forall x,y \in X$$

    <br>

- $M2$: Gets null on the diagonal:

    $$d(x,y)=0 \iff x = y \quad \forall x,y \in X$$

    <br>

- $M3$: Triangular inequality: 

    $$d(x,z) \leq d(x,y) + d(y,z) \quad \forall x,y,z \in X$$

    <br>

Observe some immediate consequences of the three axioms:

$$d(x,x) = 0 \leq d(x,y) + d(y,x) = 2d(x,y) \implies 0 \leq d(x,y) \quad \forall x,y \in X$$

<br>

The distance is always positive as a consequence of the triangular inequality and the symmetry.

<br>

## 2.2. Euclidean metric.

Let's consider again the affine space $\mathbb{R}^k$ as defined above with the dot product. Then, $V$ is an inner product vector space and, consequently, a normed vector space. Let's see how we can develop a metric in $\mathbb{R}^k$ to state it as a metric space.

First, at this point, we will develop the metric in $\mathbb{R}^k$ through its norm (depending on the inner product) although we established this is not entirely necessary.

<br>

We define the metric in $\mathbb{R}^k$ as, for $x,y \in \mathbb{R}^k$, we have that:

$$d(x,y) = \|\overrightarrow{xy}\| = \|y - x\|$$

This is, the distance between two points on $\mathbb{R}^k$ is the length of the vector that connects both points. Remember from our knowledge of affine space that $x + \overrightarrow{xy} = y$

<br>

## 2.3. $\mathbb{R}^k$ is a metric space with the euclidean metric.

Let's see that $(\mathbb{R}^k,d)$ as defined is a metric space:

- **Symmetry**:

    $$d(x,y) = \|x - y\| = \sum_i^k (x_i -y_i)^2 = \sum_i^k (y_i - x_i)^2 = \| y - x \|  = d(y,x)$$

    <br>

- **Zero distance along the same point:**

    $$d(x,y) = \|x - y\| = \sum_i^k (x_i -y_i)^2$$

    Since it is a sum of positive terms, to be zero all the operands have to be zero, this is: 
    
    $$d(x,y) = 0 \iff x_i =y_i \quad i=1,2,...,k \iff x = y \quad \forall x,y \in \mathbb{R}^k$$

    <br>

- **Triangle inequality**: This result comes immediately from the inner product. Take $x,y \in \mathbb{R}^k$, then:

    $$\|x+y\|^2 = \|x\|^2 + \|y\|^2 + 2 \langle x,y \rangle$$

    Let's see that, by Cauchy-Schwarz: $\|\langle x,y \rangle\| \leq \|\|x\|\| \|\|y\|\|$, thus

    $$\|x+y\|^2 = \|x\|^2 + \|y\|^2 + 2 \langle x,y \rangle \leq \|x\|^2 + \|y\|^2 + 2\|x\| \|y\| = (\|x\| + \|y\|)^2$$

    Since $\|\|x+y\|\| \geq 0$ and $\|\|x\|\| + \|\|y\|\| \geq 0$ is:

    $$\|x+y\|^2 \leq (\|x\| + \|y\|)^2 \implies \|x+y\| \leq \|x\| + \|y\|$$

    Giving place to the triangular inequality (which is always true in a real inner product space).

    <br>

    Now, observe that:

    $$d(x,z) = \|x -z\| = \|x -y + y-z\| \leq \|x-y\| + \|y-z\| = d(x,y)+d(y,z)$$

    The inequality is guaranteed by the triangle inequality in the norm, preceded by Cauchy-Schwarz.

    <br>

# 3. Main properties of the norm in $\mathbb{R}^k$

Let's evaluate some main properties of the norm of $\mathbb{R}^k$.

1. $\|\|x\|\| \geq 0$, is immediate from the fact that is the square of a real number.
2. $\|\|x\|\| = 0 \iff x = 0$, immediate from norm definition.
3. $\|\|\alpha x \|\| = (\langle \alpha x, \alpha x \rangle)^\frac{1}{2} = (\alpha^2 \langle x,x \rangle)^\frac{1}{2} = \|\alpha\| \|\|x\|\|$
4. $\|\|x · y\|\| \leq \|\|x\|\| \|\|y\|\|$ Immediate from Cauchy-Schwarz.
5. $\|\|x+y\|\| \leq \|\|x\|\| + \|\|y\|\|$ Triangle inequality previously demonstrated.
6. $\|\|x-z\|\| \leq \|\|x-y\|\| + \|\|y-z\|\|$ An extension of the triangle inequality relative to the euclidean metric also demonstrated above.

    <br>

# 4. Summary. 

Thus, we've seen that $\mathbb{R}^k$ as an affine space with $\mathbb{R}^k$ as the associated vector space and the real inner product as the dot product; $x · y$ conforms a Euclidean space; an affine space with a geometry induced by the vector space which crystallizes in the metric $d(x,y) = \|\|\overrightarrow{xy}\|\|$