---
layout: post
title: "3. VectorSpaces Properties"
subtitle: "Subspaces, Bases and Dimensions, Coordinates, Row-equivalence summary, Computations Concerning Subspaces."
date: 2026-06-08 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
---

# 1. Introduction.

In the past post; [Vector Spaces](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/), we've introduced that a vector space $(K,V,·)$ is the algebra structure resulting in use a field $K$ to weigh the compositions of an abelian group $V$, through a field's action $·$. Meaning that a vector space is as triple $(K,V, ·)$ where:

- $K$ is a field.
- $V$ is an abelian (conmutative) group.
- $· : K \times V \to V$ is a field action, which acts over $V$ using $K$'s elements to scalar vectors making families of *proportional vectors*.

The resulting compositions is what we suit to call *linear combination*, independant contributions of group's elements mediated by field's scalars:

$$\alpha v + \beta u : \alpha ,\beta \in \mathbb{R}, v,u \in V$$

We presented some examples of some sets which, with proper operations involved, are examples of vectorspaces:

- The $n$-tuples space: $F^n$
- The space of $m \times n$ matrices: $M_{m \times n}(F)$ 
- The space of functions from a set $S$ to a field $K$: $K^S$
- The space of polynomial functions over a field K

    <br>

We also develop surreptitiously the affine space structure, which is the way in which we use the vectors to study a non-empty set in a simply transitive way and we define the *arrow* concept as the segment that connect two points of the affine space with magnitude, direction and orientation, which captures the displacement of the point at the base of the segment to the one laying at the end of the arrow.

We also demonstrated that if you fix one point $O$ and consider the family of all posible arrows with base at $O$, then that family has structure of vector space which leaves us with a geometric intuition of what a vector is.

<br>

Then, with this information as a starting point, let's develop the fundamental properties of vector spaces.

<br>

# 2. 