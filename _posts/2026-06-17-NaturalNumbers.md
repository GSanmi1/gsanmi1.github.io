---
layout: post
title: "Axiomatic presentation of Natural Numbers."
subtitle: "Peano-Dedekind, Induction, Recursion Theorem,  & Good Order, Integers; Divisibility, Bézout, Coprimality"
date: 2026-06-17 09:00:00 +0000
categories: ['Number Systems']
tags: ['Maths']
author: German Sanmi
subject: number-systems
lang: en
---

# 0. Index.

# 1. Introduction: Algebraic structure of natural numbers.

In this post we are going to present the *natural numbers*, usually denoted by $\mathbb{N}$. 

Essentially, **$\mathbb{N}$ abstracts the structure in which count** makes sense. 

Dedekind and Peano isolates a minimal machinery; a starting point, and a unary operation (the successor) that never returns to the origin and never collides with itself, plus a principle of induction which generates a *unique* structure identifiable with an *existing* model of this system.

Let's explain this two points a little further:

- First, the Peano axioms determines a unique structure despite isomorphism. 

    This is exceptional, algebraic axiomatics like vector spaces are deliberately non-categorics, in the sense that there are at least two structures identifiable as vector spaces which are not isomorph between them (think in $\mathbb{R}$ and $\mathbb{R}^2$, both vector spaces of different dimensions, hence, not isomorph).

    We say that **the axiomatic developed by Peano-Dedekind is categoric** because all the structures identifiable with it are indeed isomorph between them, in some sense, the axiomatic system fix completly the structure which is, as a categoric axiomatic system, an **isomorphism class**.

    <br>

- Second, as an isomorphism class, we need a canonical representant of this isomorphism, some model satisfying the axiomatic system to which compare any other structure, this are the Von Neumann Ordinals, which are the canonical representant of $\mathbb{N}$.

    <br>

The resulting structuralist reading is clear: $\mathbb{N}$ is an *isomorphism class*; $\omega$ (the von Neumann finite ordinals) is a canonical representant and *categoricity* ensures that the choice of representative is irrelevant.

<br>

# 2. Peano's system. Induction Principle.

## 2.1. Peano's System.

We define a Peano's system to be a triple $(N,0,S)$ with $N$ a non-empty set, $0 \in N$ and the sucessor function $S : N \to N$, satisfying the following axioms:

- $P1, \nexists n \in N : s(n) = 0$, or in simple terms $0$ isn't the sucessor of any other element.

- $P2, \forall m,n \in N : m \neq n \implies s(m) \neq s(n)$

- $P3$ **Induction Principle**:

    $$\forall A \subseteq N \quad \big[\big(0 \in A \wedge \forall n(n \in A \implies s(n) \in A) \big) \implies A = N\big]$$

    <br>

So, $0$ is the starting point, the sucesor function is inyective, it does not collide which is the same to say that it do not goes back at any moment and it satisfies the *Induction Principle* which asserts that $S$ does not left any element in $N$ by go sucessor to sucessor.

<br>

## 2.2. Induction Principle.

Hence, basically a Peano's system is nothing more that a non-empty set and an inyective function that satisfyies the existance of the zero element and the induction principle.

Let's stop a bit and talk more about the induction principle. Observe that $P1$ garantees an starting point, $P2$ garantees no colission, meaning that $S$ doesn't go back and assign an element the sucessor of other element. Until this point the function takes one element and start assigning successors

<br>


## 2.2. Recursion Theorem (Dedekind). 

Before continue with Peano's system, let's present the recursion theorem. 

<br>

Be $(N,0,S)$ a Peano's system and $X$ a non empty set. Then consider $a \in X$, and any function $f \in X^X$, then exists a unique function $\varphi \in X^N : \varphi(0)=a \wedge \varphi(S(n)) = f(\varphi(n))$.

<br>





## 2.3. Categoricity; isomorphism between two Peano's systems.

We are about to see that the axiomatic system presented before is categoric, in the sense that; **two Peano's systems $(N,0,S), (N',0',S)$ are isomorphs**.

<br>

# 3. Finite von Neumann ordinals.

