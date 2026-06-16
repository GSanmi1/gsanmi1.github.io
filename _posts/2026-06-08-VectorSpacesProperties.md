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

# 2. Subspaces.

## 2.1. Definition and caracterization.

In this section we shall introduce some of the basic concepts in the
study of vector spaces. 

**Let $V$ be a vector space over the field $F$. A subspace of $V$ is a subset $W$ of $V$ which is itself a vector space over $F$ with the operations of vector addition and scalar multiplication on $V$.**

<br>

Let's observe that, from the axioms of vector spaces, if $W$ is a vector space such $W \subset V$, then:

- Closure relative to linear combinations:

    $$v,u \in W \implies (\alpha v + \beta u \in V \ \forall \alpha, \beta \in  F)$$

- Contains zero vector: $0_V \in W$, or $0_W = 0_V$. Remember that $V$ being a vector space means that $(V,+)$ is an abelian group, so $(W,+)$ is an abelian subgroup of $V$ and it inherites $0_v$ from $V$ by the uniquity of this element. (Observe that this also expands associativity, and inverses).

    <br>

Let's take a characterization for any subset $W \subset V$ to be a vector space. If $V$ is a $K$-vector space, then:

$$W \text{ is a vector space } \iff (\alpha u + v \in W \quad \forall u,v \in W, \alpha \in K)$$

Let's reconstruct the structure:

- $(W,+)$ is an abelian subgroup of $(V,+)$.

    Take, $u,v \in W$, then: $(-1)u + v = v - u \in W$, so is a subgroup of $V$. Let's see that also is abelian since $V$ is, take $u,v \in W$ then, $u+v = v + u$ because they are elements of $V$



- $· \|_W: K \times W \to W$ is a field action. 