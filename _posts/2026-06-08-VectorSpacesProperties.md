---
layout: post
title: "3. VectorSpaces Properties"
subtitle: "Subspaces, Bases and Dimensions, Coordinates, Row-equivalence summary, Computations Concerning Subspaces."
date: 2026-06-08 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
subject: linear-algebra
lang: en
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

**Let $V$ be a vector space over the field $F$. A subspace of $V$ is a subset non-empty $W$ of $V$ which is itself a vector space over $F$ with the operations of vector addition and scalar multiplication on $V$.**

<br>

Let's observe that, from the axioms of vector spaces, if $W$ is a vector space such $W \subset V$, then:

- Closure relative to linear combinations:

    $$v,u \in W \implies (\alpha v + \beta u \in V \ \forall \alpha, \beta \in  F)$$

- Contains zero vector: $0_V \in W$, or $0_W = 0_V$. Remember that $V$ being a vector space means that $(V,+)$ is an abelian group, so $(W,+)$ is an abelian subgroup of $V$ and it inherites $0_v$ from $V$ by the uniquity of this element. (Observe that this also expands associativity, and inverses).

    <br>

Let's take a characterization for any subset non-empty $W \subset V$ to be a vector space. If $V$ is a $K$-vector space, then:

$$W \text{ is a vector space } \iff (\alpha u + v \in W \quad \forall u,v \in W, \alpha \in K)$$

Let's reconstruct the structure:

- $(W,+)$ is an abelian subgroup of $(V,+)$.

    Since $W \neq \varnothing$ (by the premise), we can consider $u,v \in W$, then: $(-1)u + v = v - u \in W$, so is a subgroup of $V$. Let's see that also $W$ inherites conmutativity from $V$ so is an abelian subgroup.

    <br>

- $· \|_W: K \times W \to W$ is a field action:

    - Observe that $-1 u + u = 0 \in W$, thus $1 u + 0 = u \in W$ so the unit in $F$ doesn't change the vector and it falls inside $W$.

    - Take some $v \in W \implies \alpha v + 0 = \alpha v \in W \implies \beta (\alpha v) + 0 = \beta (\alpha v) \in W$. For the same reason $(\alpha \beta)v \in W$. Then observe that in $V$, by associativity, is $\beta (\alpha v) = (\beta \alpha)v$ so both elements are equal in $V$ and the same in $W$ (by unicity of the inverse), thus $\beta (\alpha v) = (\beta \alpha)v$

    - Take $(\alpha + \beta)v + 0 = (\alpha + \beta)v \in W \subset V$, then in $V$ is $(\alpha + \beta)v = \alpha v + \beta v$ so, for the same argument as above, is $(\alpha + \beta)v = \alpha v + \beta v$ in $W$.

    - Take $\alpha v + 0 \in W \implies \exists w = \alpha v \in W$, take now other $u \in W$, then  $\alpha u + w \in W$, again in $V$ is $\alpha u + w = \alpha u + \alpha v = \alpha(u + v)$ and again is $ \alpha(u + v) = \alpha u + \alpha v$ in $W$.

    <br>

## 2.2. Example of subspaces.

Let's consider some well-known example of subspaces. Consider some $V$ a $K$-vector space, then:

- $V$ is a subspace of $V$.
- $\Set{0} \subset V$ is the zero subspace of $V$; $\alpha 0 + 0 = 0 \in \Set{0} \quad \forall \alpha \in K$ so $\Set{0}$ is a subspace of $V$.

- $A:= \Set{x \in K^n \mid x_1 = 0}$ is a subspace of $K^n$, check that always $\alpha x + y \in A$, trivially.

    But let's observe that $B := \Set{x \in K^n \mid x_1 = 1 + x_2}$ do not satisfies the rule, take some $\alpha$ and observe that:

    $$\alpha x + y = (\alpha (1 + x_2) + 1 + y_2), \alpha x_2 + y_2,..., \alpha x_n + y_n)$$

    Then, $\alpha + 1 + \alpha x_2 + y_2 = 1 + \alpha x_2 + y_2 \iff \alpha=0$. 
    
    So we have that $\forall \alpha \neq 0 \quad (x,y \in B \implies \alpha x + y \notin B)$


