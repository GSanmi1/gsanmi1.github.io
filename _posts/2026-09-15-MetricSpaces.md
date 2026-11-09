---
layout: post
title: "Metric Spaces"
subtitle: "Metric Spaces. Distance. Isometries."
date: 2026-11-09 09:00:00 +0000
categories: ['Geometría Básica']
tags: ['Maths']
author: German Sanmi
subject: geometry
lang: en
---

# 0. Index.

- 1. Introduction.
- 2. Metric Spaces. Distance.
- 3. Isometries. Isometric Spaces.
    - 3.1. Definition.
    - 3.2. Theorem 1.7. Composition and Inverse of isometries are isometries.

    <br>

# 1. Introduction.

Geometry comes from greek. The term '-metry' refers to measure, because the origins of geometry takes place in how to measure land portions or river floods. In mathematics, the *metric space* is the structure which gives sense to the action to measure.

In mathematics, *measure* aqcuires a more generic form. To measure in mathematics is all about to abstract some property between two elements and translate it to real numbers satisfying some properties forgetting what is being measured and how is being measured.

<br>

# 2. Metric Spaces. Distance.

Let be $M \neq \varnothing$. Then, a function $\delta : M \times M \to \mathbb{R}$ is called *metric* or *distance function* on $M$ if the following conditions are satisfyied by any $x,y,z \in M$:

- **$(M1)$ Positive definiteness**. This is, is always positive for any pair of distinct elements and zero for the same element:


    $$[\delta(x,y) > 0 \iff x \neq y ] \wedge [\delta(x,x) = 0]$$

- **$(M2)$ Simmetric**. The property is intrinsic of the pair, indifferent to the way of measure:

    $$\delta(x,y) = \delta(y,x)$$

- **$(M3)$ Triangular Inequality**: This third axiom stablish how distances relate each others:
    
    $$\delta(x,y) \leq \delta(x,z) + \delta(z,y)$$

    Observe that, $M1$ stays that any distance between two distinct points is positive. $M3$ stays that, further more, the distance between two points is not only positive but equal or greater than the same measured distance passing through an intermediary. 

    In simple terms: taking a detour never shortens the way, it is formalizing the idea that the shortest distance between two points is the one involving only those two points, prescinding any other third party.

    ![Triangular Inequality](/assets/images/Maths/Geometry/TriangularInequality.png)

<br>

The pair $(M, \delta)$ satisying the conditions above is called *Metric Space*.

<br>

# 3. Isometries. Isometric Spaces.

## 3.1. Definition.

We are now going to present those functions preserving distances. Meaning the images of this functions retains invariant the real number given by the metric in each space.

Let be $(M,\delta)$ and $(M',\delta')$ two metric spaces and $g: M \to M'$, then we say that $g$ preserves the distance if:

$$\delta'(g(x),g(y)) = \delta(x,y) \quad \forall x,y \in M$$



Then, $g$ is called *isometry*. Two spaces are called *isometric*, if at least one isometry can be considered between them. In this context, $(M,\delta)$ and $(M',\delta')$ are say to be isometric.

<br>

## 3.2. Theorem 1.7: Composition and Inverse of isometries are isometries.