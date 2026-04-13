---
layout: post
title: "2. VectorSpaces"
subtitle: "Spaces. Subspaces. Bases and Dimensions. Coordinates. Summary of Row-equivalence. CCS."
date: 2026-04-08 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
---

# 1. Conceptual Approach. Algebra, Algebraics Structures and Vector Spaces.

## 1.1. Algebra as a discipline.

Let's start introducing what **Algebra** is, Algebra is the mathematics discipline in charge of the study of what *operating with the elements of a set means*: how items of a set are combined through a operation and what properties emerge from that context. It doesn't study the elements (like arithmetic would do) but the properties of the operations between them.

<br>

## 1.2. Algebraic Structures.

An **algebraic structure** is a a set $(S, \Omega)$ where:

- $S \neq \varnothing$
- $\Omega$ is a collection of operations over $S$ (and maybe other sets as we will see) along with a sequence of rules called *axioms* that this operations satisfies.

This is the minimal basic item of study in algebra; a finite number of operations over a set defined by axioms. Our task is to comprehend how this operations behave through the axioms applying classic logic. 

In the previous section we already provided an introduction to algebraic structures through the number sets and then introduced a solid idea of the group and then the field. Our objective was to present a formalization about linear equations over a field.

We can review and develop the ideas presented in the [Linear Equation section](https://gsanmi1.github.io/posts/2026/02/06/Linear_Equations/) to understand the natural progression and the algebraic structures towards de vector space.

<br>

### 1.2.1. One operation algebraic structures.

Let be $G := (S, \Omega) : \Omega := \Set{\star}$, where $\star : S \times S \to S$ is an internal operation (a function). 

Then we define:

- $G$ (or $S$ by default) is said to be a *Magma* if $\star$ only verifies the closure property:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)

    Observe that this structure is the minimal one, and his only property is forced by $\star$ definition.

    <br>

- $G$ is a *semigroup* if also verifies associativity:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b \in S$ (Associativity)

    <br>

- A *monoid* is a semigroup that also have the identity element $e \in S$ relative to $\star$ verifying:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b \in S$ (Associativity)
    - $ \exists e \in S \ \ \forall a \in S : e \star a = a \star e = a$ (Identity)

    <br>

- Now we enter in the confort zone, a *Group* is a monoid which verifies the existance of an inverse for each item in $S$:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b,c \in S$ (Associativity)
    - $ \exists e \in S \ \ \forall a \in S : e \star a = a \star e = a$ (Identity)
    - $\forall a \in S \ \ \exists a' \in S : a \star a' = a' \star a = e$ (Inverse)

    <br>

Let's observe that each axiom let us to do something new in the structure, each new rule is a new capability based on the defining of invariants along the structure; 

- The closure garantees internal compositions, the belonging of any composition to $S$ remains contant. 

- The associativity garantees order-independence as long as the direction in the composition remains the same, meaning that $(a\star b) \star c$ and $a\star (b \star c)$ is the same object in the sense that we can talk about $a\star b \star c$ to refer to any of them, no matter what do you compose first.

- The existance of the identity garantee the existance a way to operate that do nothing concreted in an element of $S$ called the identity. The composition of $e$ by any item of $S$ in any direction remains constant and is the very same item.

- The existance of the inverse make use of the identity to garantee a way to operate that lets you reverse the operation. The composition of any item with his inverse in any direction remains constant and is the identity.

<br>

Observe that this are the main invariants in operations because this are the smallest subset of rules that allow you to define constraints about some elements (equations) and confortly operate to isolate them in order to fully understand to what is equivalent that constraint and how is a valid item.

Suppose there is an interest to find the relation about two elements $a,b \in S$, this is, $b$ is the composition of $a$ with some other element $x \in S$ which we gonna call the *unknown*: $a \star x = b$. Now, let's observe:

$$ a^{-1} \star (a \star x) = a^{-1} \star b$$

Step by step, the closure axiom asserts that $a^{-1} \star (a \star x) = a^{-1} \star b \in S$ and the propousal has sense, the associativity stablish that $a^{-1} \star (a \star x)  = a^{-1} \star a \star x= (a^{-1} \star a) \star x$, or that we can choose the order of the composition as we please. Then, the identity and the inverse cooperates together to simplify the expression, the inverse make $a$ to dissapear, it substitute it for the identity and the identity composed with any other item is any other item, thus:

$$a^{-1} \star (a \star x) = (a^{-1} \star a) \star x = e \star x = x = a^{-1} \star b$$

This four invariantes are summarized in the idea of *group*.

This idea of group can be extended by introducing the *conmutativity* which defines the composition under direction as an invariant:

$$a \star b = b \star a \ \ \forall a,b \in S$$

This allows to reorganize making the simplification of expressions even more confortable.

<br>

### 1.2.2. Two operations algebraic structures.

Until now, we've defined an algebraic structure that contemplates only one operation, lets now introduce algebraic structures with two operations.

<br>

**Rings**

First, the rings, a ringe is a triple $(K,+,\ ·)$ such:

- $(K,+)$ is a group and introduce the four properties seen above.
- $(K, \ ·)$ is a monoid, it drops the existence of the inverse for any element of $R$.
- $+$ and $·$ relates themselves by the distributive law:

    $$a(b+c) = ab + ac \wedge (b+c)a = ba + ca$$

    We say both operations are compatible.

    <br>

The ring introduces the second operation in a soft way, hanging on the existance of the inverse allows to fit in many structures well studied such:

- **Integers ring**; $(\mathbb{Z},+, \ ·)$, where for example $\forall a ( a \in \mathbb{Z} \wedge a \neq \pm 1 \implies a^{-1} \notin \mathbb{Z})$.

    <br>

- **Polynomial ring**; with coefficients in a field $F$; $F[x]$ is a ring 
  but not a field. For instance, $x$ has no multiplicative inverse:

  $\forall q \in F[x] \setminus \{0\} \ \deg(x \cdot q) = 1 + \deg(q) \geq 1 \neq 0 = \deg(1)$

  So the equation $x \cdot q = 1$ has no solution in $F[x]$

    <br>

- **Matrix ring**; we've already seen that $(M\_n(F)\setminus 0, \ ·)$ has no inverse for every element of $M\_n(F)$, remember that we already seen that not every matrix is invertible only those row-equivalent to the identity $I\_n$

    <br>

The mathematical world is full of structures with two operations where division fails.

<br>


**Field**

Then the concept of the field can be thought as an extension of the ring where each element has an inverse for the product operation except the zero element.

However, we want to present another perspective of a field. 

Above we built step by step from the smallest algebraic structure *Magma* to the *Group* and his four axioms and we conclude the importance of such structure was that it allows to present and solve equations:

$$a \star x = b \iff x = a^{-1} \star b$$

Then, the field $K$ aims to extend the same idea for two operations departing from the group structure. This means that a field is a triple $(K,+, \ ·)$ such:

- $(K, +)$ is an abelian group.
- $(K \setminus \Set{0}, \ ·)$ is an abelian group.
- $+$ and $·$ are compatible.
- $1 \neq 0$

This basically means that the field intends to be the structure in which equations can be defined and solved in two operations simultaneously, the motivation was to build an algebraic framework for common aritmetic operations in $\mathbb{R}, \mathbb{Q},...$ and another commons fields.
    
<br>

# 2. Vector spaces.

Before we've seen a set of axioms that rules how a set of operations $\Omega$ behaves in a non-empty set $K$. We extend this concept to two sets $(K,V)$ where $K$ is a field and $V$ is a group and both related between them an action.

<br>

## 2.1. Actions.


## 2.2. Vector Space definition.



<br>