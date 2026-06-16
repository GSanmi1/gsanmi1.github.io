---
layout: post
title: "Euclidean Spaces"
subtitle: "Introduction to Euclidean Spaces."
date: 2026-03-05 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
---

# 0. Index

# 1. Presentation and Definition. 

An Euclidean space, $\mathbb{R}^k$ is the set of all the ordered real $k$-tuples. This structure is well equiped with all the tools that simultaneously make it a:

- **$\mathbb{R}$-vector space**: $(\mathbb{R},(\mathbb{R}^k,+),·)$, with the operations as follows:

    $$(x_1,...,x_k)+(y_1,...,y_k)=(x_1+y_1,...,x_k+y_k)$$

    $$\alpha · (x_1,...,x_k) = (\alpha x_1,..., \alpha x_k)$$

    Which allows linear combinations.

    <br>

- **Inner product space**: As we see in the [Complex Numbers](https://gsanmi1.github.io/posts/2026/03/05/Complex_Numbers/) post, on $6.3.1$, an inner product space is an object which inyects geometry by defining how a vector express his own direction (norm):

    $$\langle ·,· \rangle : \mathbb{R}^k \times \mathbb{R}^k \to \mathbb{R}$$

    In this case, the instantiation is the *dot product* or *scalar product*:

    $$\quad \quad \langle x,y \rangle = \sum_{i=1}^k x_iy_i$$

    Which inyects geometry, a notion of direction (norm), shared direction (angle) and disjoint direction (pithagoras).

    <br>

- **Normed Space**: As a consecuence of the inner product presence, a norm for each vector $x \in \mathbb{R}^k$ is defined:

    $$\|x\| = \sqrt{\langle x,x \rangle}= \sqrt{\sum_{i=1}^k x_i^2}$$

    Which give us a notion of "longitude" of the vector. Is worth to say that this is specifically true in $\mathbb{R}^k$ where intuitive geometry matchs formal geometry instauration through dot product.

    <br>

- **Metric Space**: As consecuence of the geometry inyected by inner product a notion of proximity is definided which allow as to introduce the notion of limit and develop the analisis.

    <br>

# 2. Metric spaces.

## 2.1. Metric definition. Metric spaces.

A metric abstracts the notion of *distance*. This is an important concept since from this departs all the analisis. From distance notion comes proximity notion then limits gain sense.

A *distance* tries to get how far two points are from each other in a non-empty set $X$. Observe that this is no algebraic structure or algebraic property, contrary to the norm, the distance doesn't need from sume or scale.

<br>

Let be $X$ a non-empty space, then a *metric space* is a pair $(X,d)$ where: $d : X \times X \to \mathbb{R}$ is an application called *distance*, verifying:

- $M1$: Simmetry, the distance is indiferent of the point of measure: 

    $$d(x,y)=d(y,x) \quad \forall x,y \in X$$

    <br>

- $M2$: The distance is zero only if both are the same point:

    $$d(x,y)=0 \iff x = y \quad \forall x,y \in X$$

    <br>

- $M3$: Triangular inequality: 

    $$d(x,z) \leq d(x,y) + d(y,z) \quad \forall x,y,z \in X$$

    <br>

Observe some immediate consecuence of the three axioms:

$$d(x,x) = 0 \leq d(x,y) + d(y,x) = 2d(x,y) \implies 0 \leq d(x,y) \quad \forall x,y \in X$$

<br>

The distance, is always positive as a consecuence from the fact of the triangular ineqaulity an the simmetry.

<br>

## 2.2. Euclidean metric.

Let's consider the vector space $\mathbb{R}^k$ as defined above and also consider the dot product. Then, $\mathbb{R}^k$ is an inner product vector space, consecuently is a normed vector space and let's see how develop a metric to state it as a metric space.

First, at this point, we will develop the metric in $\mathbb{R}^k$ through his norm although we stablished this is not enterely necesary.

<br>

We define the metric in $\mathbb{R}^k$ as, for $x,y \in \mathbb{R}^k$, we have that:

$$d(x,y) = \|x - y\|$$

This is, the distance between two points on $\mathbb{R}^k$ is the longitude of the vector that connects both points. Remember from our knowledge from affine space that $x + \overrightarrow{xy} = y$

Let's see that $(\mathbb{R}^k,d)$ as defined is a metric space:

- **Simmetry**:

    $$d(x,y) = \|x - y\| = \sum_i^k (x_i -y_i)^2 = \sum_i^k (y_i - x_i)^2 = \| y - x \|  = d(y,x)$$

    <br>

- **Zero distance along the same point:**

    $$d(x,y) = \|x - y\| = \sum_i^k (x_i -y_i)^2$$

    Since is a summatory of positive terms, to be zero all the operands has to be zero, this is: 
    
    $$d(x,y) = 0 \iff x_i =y_i \quad i=1,2,...,k \iff x = y \quad \forall x,y \in \mathbb{R}^k$$

    <br>

- **Triangular inequality**: This result come immediately from the inner product. Take $x,y \in \mathbb{R}^k$, then:

    $$\|x+y\|^2 = \|x\|^2 + \|y\|^2 + 2 \langle x,y \rangle$$

    Let's see that, by Cauchy-Schwarz: $\|\langle x,y \rangle\| \leq \|\|x\|\| \|\|y\|\|$, thus

    $$\|x+y\|^2 = \|x\|^2 + \|y\|^2 + 2 \langle x,y \rangle \leq \|x\|^2 + \|y\|^2 + 2\|x\| \|y\| = (\|x\| + \|y\|)^2$$

    Since $\|\|x+y\|\|^2 \geq 0$ and $\|\|x\|\|^2 + \|\|y\|\|^2 \geq 0$ is:

    $$\|x+y\|^2 \leq (\|x\| + \|y\|)^2 \implies \|x+y\| \leq \|x\| + \|y\|$$

    Giving place to the triangular inequality (which is always true in an inner product space).
