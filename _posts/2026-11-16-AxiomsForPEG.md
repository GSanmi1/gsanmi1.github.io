---
layout: post
title: "Axioms for plane Euclidean geometry"
subtitle: "Plane, Lines, Separation, Trinagles, Isommetries and Ortogonality."
date: 2026-11-16 09:00:00 +0000
categories: ['Geometría Básica']
tags: ['Maths']
author: German Sanmi
subject: geometry
lang: en
---

# 0. Index.



<br>

# 1. Introduction.

In this chapter we are going to develop the *Plane Euclidean Geometry* in an axiomatic way. This basically means we will start by announcing some properties assuming them as true or principles (axioms) from which we will develop other properties such theorems, lemma, proposition, etc.

This axioms will be stablished in set theory language, in this sense, we will say that the plane is a set of points, the figures on the plane such lines or triangles are subsets of the plane satisfying some conditions and distances, isommetries and more are applications.

Is important to keep in mind that PEG emerges as an abstraction of what we can draw in a paper with a pencil. The objective of this course is to form the student to instantiate clear or strong intuitions into logically correct and syntactically well-constructed propositions.

<br>

# 2. Axiom P1. The plane's metric space. Distance.

Let's consider the following two objects:

- The non-empty set called *Plain*; $\bold{P}$, whose elements are called *points*; $A,B,C,\ldots$.

- An application $d :  \bold{P}^2 \to \mathbb{R}$, called *distance*.

The axioms $P1 -P7$ for the PEG will characterize or shape $(\bold{P},d)$, starting from the first one:

$$\boxed{\text{ Axiom P1: } (\bold{P},d) \text{ is a metric space}}$$

<br>

# 3. Lines.

In [metric space's](https://gsanmi1.github.io/posts/2026/11/09/MetricSpaces/) post we discuss the concepts of segments and alignment. We know extended them in the plane defining the *line* object.

## 3.1. Line: Definition.

A subset $r \subset \bold{P}$ is called a *line* if the following conditions are meet:

1. $\exists A,B \in r : A \neq B$. 

2. $A,B,C \text{ are aligned } \quad \forall A,B,C \in r : A \neq B \wedge B \neq C \wedge C \neq A$.

3. $\forall A,B \in r : A \neq B, \forall X \ (A,B,X \text{ are aligned } \implies X \in r)$.

This means that lines are non-empty, non-singleton $(1.)$, aligned $(2.)$ subsets $\bold{P}$ that owns any point of the plane aligned with his own points $(3.)$.

![line](/assets/images/Maths/Geometry/line.png)

<br>

## 3.2. Segments and Lines in the plane.

We are going to see that any segment of endpoints included in a line is a subset of the own line. This is a very intuitive result keeping in mind the definition given above. We recall that segments are those points which do not increment the distance between the endpoints when this is measured passing through them, and alignment between three points literally means for one point to be included in the segment of the other two.

Having said that, let be $r \subset \bold{P}$ a line and $A,B \in r : A \neq B$ which exists by $(1.)$ and consider $[A,B]$. By definition of the segment:

$$[\forall X \in [A,B] \quad A,B,X \text{ are aligned } \underbrace{\implies}_{(3.)} X \in r] \implies  [A,B] \subset r$$

Observe that $A = B \implies [A,B] = \Set{A} \subset r$ since $A \in r$ by premise.

Hence, ultimatly, we can state that: $[A,B] \subset r \quad \forall A,B \in r$.

<br>

## 3.3. Axiom P2: More than one line in $\bold{P}$. The line passing through two points.

The following axiom, $P2$, states that in $\bold{P}$ there is more than one single line to consider in $\bold{P}$.

$$\boxed{ \begin{aligned}\text{ Axiom P2:}&  \\  (i) \quad & \exists A,B,C : \neg [Al(A,B,C)] \\  (ii) \quad & \forall A,B(A \neq B \implies \exists !r : A,B \in r)\end{aligned}}$$

Observe directly that:

- $(i)$ of $P2$ let us to consider at least one point not aligned with other two in $\bold{P}$, meaning that the three are not in the same line.

- $(ii)$ of $P2$ let us to consider a line whenever we identify two distinct points of the plane and this line is unique. Note that the uniqness of the line is not necesary, is forced by the alignement logic of the structure (the points of two lines passing through two distinct points are enterely aligned with those two points, hence, each point is in his own line and in the other, thus both lines are in fact the same line).

    <br>

Then, using $P2,(i)$ we can consider three non-aligned points $A,B,C$, (observe that this means they are three distinct points, since one point and two points in the plane are always aligned points). Then, by $P2,(ii)$, we can consider $r$, unique, passing through $A,B$; $g$, unique, passing through $B,C$ and $h$, unique, passing through $A,C$. This three lines are distinct subsets of $\bold{P}$.

![axiomP2](/assets/images/Maths/Geometry/AxiomP2.png)

$P2,(i)$ let's to consider it and $P2, (ii)$ let us to build it.

<br>

For now on, we will design the unique line passing through $A,B \in \bold{P}$ as $r_{AB}$.

<br>

## 3.4. Parallel and Intersecting lines.