---
layout: post
title: "Linear Algebra for Machine Learning"
subtitle: "Linear Algebra Chapter in MML book."
date: 2026-03-14 09:00:00 +0000
categories: ['Maths', 'MML']
tags: ['Maths','MMLbook']
author: German Sanmi
---

# 1. Introduction.

When formalizing intuitive concepts, a common approach is to construct a set of objects (symbols) and a set of rules to manipulate these objects. This is known as an *algebra*; the study of symbolic manipulation and relation of structures. Essentially, algebra studies what is preserved under operations and mappings. 

*Linear Algebra* is the study of those properties that are preserved under linear transformations (transformations that respect addition and scalar multiplication), these are: vectors spaces.

A *vector* is an element of a *vector space*. A vector space is not a bare set; it is a set $S$ equipped with two operations (addition and scalar multiplication over a field $F$) satisfying eight axioms. The definition is purely structural: vectors have no privileged concrete representation. Arrows, tuples, polynomials, and matrices can all be vectors when you define the right operations on them and verify the axioms.

In general, vectors are special objects that can be added together and multiplied by scalars to produce another object of the same kind. From an abstract mathematical viewpoint, any object that satisfies these two properties can be considered a vector. Some examples of such vector objects are *geometric vectors*, *polynomials*, *tuples of $\mathbb{R}^n$* or *matrices*.


<br>

# 2. System of Linear Equations.

## 2.1. Formal definition.

A system of linear equations over a field $F$ is a finite collection of equations of the form:

$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i, \qquad i = 1,\ldots,m$$

Where the $a_{ij}, b_i \in F$ are given scalars and $x_1, \ldots, x_n$​ are unknowns. They are basically a set of constraints that points of $F^n$ must satisfy simultaneously.

The solution set is $S = \{x \in F^n : Ax = b\}$. Three things can happen:

- $S = \varnothing$  (inconsistent)

- $\vert S \vert = 1$ (unique solution)

- $\vert S \vert = \infty$

When $b = 0$ (the homogeneous case), $S$ is always nonempty (it contains $0 \in F^n$) and is in fact a subspace of $F^n$.

<br>

## 2.2. Geometric Interpretation of System Linear Equations.


As an ilustrative example of how this systems works as constraints over points, lets talk about the geometric interpretation of a system of linear equations in two variables.

In a system of linear equations with two variables $x1, x2$, each linear equation defines a line on the $x1x2$-plane.

![plane1](/assets/images/ML/plane1.png)

Since a solution to a system of linear equations must satisfy all equations simultaneously, the solution set is the intersection of these lines. 
 
This intersection set can be a line (if $\vert S \vert = \infty$ and the equations describe the same line), a point (if $\vert S \vert = 1$, unique solution), or empty ($S = \varnothing$ , when the lines are parallel).

 Similarly, for three
variables, each linear equation determines a plane in three-dimensional
space. When we intersect these planes, i.e., satisfy all linear equations at
the same time, we can obtain a solution set that is a plane, a line, a point
or empty (when the planes have no common intersection).

<br>

# 3. Matrices.

For a systematic approach to solving systems of linear equations, we will introduce a useful compact notation. We collect the coefficients $a_{ij}$ into vectors and collect the vectors into matrices. In other words, we write the system from above in the following form:

$$x_1
\begin{bmatrix}
a_{11}\\
\vdots\\
a_{m1}
\end{bmatrix}
+
x_2
\begin{bmatrix}
a_{12}\\
\vdots\\
a_{m2}
\end{bmatrix}
+ \cdots +
x_n
\begin{bmatrix}
a_{1n}\\
\vdots\\
a_{mn}
\end{bmatrix}
=
\begin{bmatrix}
b_1\\
\vdots\\
b_m
\end{bmatrix} \iff$$


$$ \iff \begin{bmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots &        & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{bmatrix}
\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}
=
\begin{bmatrix}
b_1\\
\vdots\\
b_m
\end{bmatrix}$$



PAGINA 28