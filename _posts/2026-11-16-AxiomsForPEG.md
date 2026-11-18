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

1. Introduction.
2. Axiom P1. The plane's metric space. Distance.
3. Lines.
- 3.1. Line: Definition.
- 3.2. Segments and Lines in the plane.
- 3.3. Axiom $P2$: More than one line in $\textbf{P}$. The line passing through two points.
- 3.4. Parallel and Secant lines.

    <br>

# 1. Introduction.

In this chapter we are going to develop the *Plane Euclidean Geometry* in an axiomatic way. This basically means we will start by announcing some properties assuming them as true or principles (axioms) from which we will develop other properties such theorems, lemma, proposition, etc.

This axioms will be stablished in set theory language, in this sense, we will say that the plane is a set of points, the figures on the plane such lines or triangles are subsets of the plane satisfying some conditions and distances, isommetries and more are applications.

Is important to keep in mind that PEG emerges as an abstraction of what we can draw in a paper with a pencil. The objective of this course is to form the student to instantiate clear or strong intuitions into logically correct and syntactically well-constructed propositions.

<br>

# 2. Axiom P1. The plane's metric space. Distance.

Let's consider the following two objects:

- The non-empty set called *Plain*; $\textbf{P}$, whose elements are called *points*; $A,B,C \ldots$

- An application $d :  \textbf{P}^2 \to \mathbb{R}$, called *distance*.

The axioms $P1 -P7$ for the PEG will characterize or shape $(\textbf{P},d)$, starting from the first one:

$$\boxed{\text{ Axiom P1: } (\textbf{P},d) \text{ is a metric space}}$$

<br>

# 3. Lines.

In [metric space's](https://gsanmi1.github.io/posts/2026/11/09/MetricSpaces/) post we discuss the concepts of segments and alignment. We will know extrapolate them in $\textbf{P}$ defining the *line* object.

<br>

## 3.1. Line: Definition.

A subset $r \subset \textbf{P}$ is called a *line* if the following conditions are meet:

1. $\exists A,B \in r : A \neq B$. 

2. $\forall A,B,C \ [A,B,C \in r \implies Al(A,B,C)] $.

3. $\forall A,B \in r : A \neq B, \forall X \ [Al(A,B,X) \implies X \in r]$.

This means that lines are non-empty, non-singleton $(1.)$, aligned $(2.)$ subsets that owns any point of the plane aligned with his own points $(3.)$.

![line](/assets/images/Maths/Geometry/line.png)

<br>

## 3.2. Segments and Lines in the plane.

We are going to see that any segment of endpoints included in a line is a subset of the own line. This is a very intuitive result keeping in mind the definition given above. We recall that segments are those points which do not increment the distance between the endpoints when this is measured passing through them, and alignment between three points literally means for one point to be included in the segment of the other two.

Having said that, let be $r \subset \textbf{P}$ a line and $A,B \in r : A \neq B$ which exists by $(1.)$ and consider $[A,B]$. By definition of the segment:

$$[\forall X \in [A,B] \ (Al(A,B,X) \underbrace{\implies}_{(3.)} X \in r)] \implies  [A,B] \subset r$$

Observe that $A = B \implies [A,B] = \Set{A} \subset r$ since $A \in r$ by premise.

Hence, ultimately, we can state: $[A,B] \subset r \quad \forall A,B \in r$.

<br>

## 3.3. Axiom $P2$: More than one line in $\textbf{P}$. The line passing through two points.

The following axiom, $P2$, states that in $\textbf{P}$ there is more than one single line to consider in $\textbf{P}$:

$$\boxed{ \begin{aligned}\text{ Axiom P2:}&  \\  (i) \quad & \exists A,B,C : \neg [Al(A,B,C)] \\  (ii) \quad & \forall A,B(A \neq B \implies \exists !r : A,B \in r)\end{aligned}}$$

Observe directly that:

- $(i)$ of $P2$ let us to consider at least one point not aligned with other two in $\textbf{P}$, meaning that the three are not in the same line.

- $(ii)$ of $P2$ let us to consider a line whenever we identify two distinct points of the plane and this line is unique. Note that the uniqness of the line is not necesary, is forced by the alignement logic of the structure (the points of two lines passing through two distinct points are enterely aligned with those two points, hence, each point is in his own line and in the other, thus both lines are in fact the same line).

    <br>

Then, using $P2's (i)$ we can consider three non-aligned points $A,B,C$, (observe that this means they are three distinct points, since one point and two points in the plane are always aligned points). Then, by $P2's(ii)$, we can consider $r$, unique, passing through $A,B$; $g$, unique, passing through $B,C$ and $h$, unique, passing through $A,C$. This three lines are distinct subsets of $\textbf{P}$.

![axiomP2](/assets/images/Maths/Geometry/AxiomP2.png)

$P2's(i)$ let's to consider it and $P2's (ii)$ let us to build it.

<br>

For now on, we will design the unique line passing through $A,B \in \textbf{P}$ as $r_{AB}$.

<br>

## 3.4. Parallel and Secant lines.

### 3.4.1. Parallel and Intersection: Definition.

Let be $r,t \subset \textbf{P}$ two lines, then we say that:

- Both lines are *secant* (or just, both intersect) $\not{\|\|}$ when share a unique point:

    $$r \not{||} \ \ t \iff \exists A \in \textbf{P} : r \cap t = \Set{A}$$

    <br>

- We say both are *parallel* lines $\|\|$ when do not share any points:

    $$r \ \| \ t \iff r \cap t = \varnothing$$

    <br>

### 3.4.2. Theorem 2.7: Characterization of the pairs of lines in $\textbf{P}$.

**Is clear that, given two lines $r,t \subset \textbf{P}$, then, there are three posibilities; both are parallel lines, secant lines, or the same line.** 

As subsets of $\textbf{P}$ if both doesn't share points $r \cap t = \varnothing$, then are parallel, if both share exactly one point $r \cap t = \Set{A}$, then are secant lines.

If both share more than one point, then, let be $A,B \in r \cap t : A \neq B$ and consider $r_{AB}$. The same reasoning is valid for $r$, take some point $X \in t$, then we have by $(2.)$ of lines's definition: $A,B,X \in t \implies Al(A,B,X)$, then also by $(3.)$ $X \in r_{AB}$ and since $X$ is an arbitrary point of $t$, then $t \subseteq r_{AB}$. The same reasoning demonstrates that $r_{AB} \subseteq t$, hence $t = r_{AB} = r$.

<br>

(Observe that we demonstrate this result by forgetting the uniquity statement of $P2$, then the demonstration would be much sorter. But is worth to demonstrated this way in order to remember that uniquity is not necesary).

![linePairs](/assets/images/Maths/Geometry/LinePairs.png)

<br>

## 3.5. Axiom $P3$: Ruler Postulate.

#### 3.5.1. Definition.

We are already familiar with this result, which basically recovers the analysis's fact about real numbers as positions in a line (Dedekind's cut) and transfer it too the line's subsets of $\textbf{P}$.

Remember that $(\textbf{P},d)$ is a metric space and since any line is a subset of the plane; $r \subset \textbf{P}$, then the set $(r,d\|_{r \times r})$ inheritates the metric space structure from the first one. Having this said, then:

<br>

$$\boxed{ \text{ Axiom } \text{P3 (Ruler Postulate)}:  \\  Isom((r,d|_{r \times r}),(\mathbb{R},\delta_\mathbb{R})) \neq \varnothing \quad \forall \text{ line } r }$$

<br>

Observe that we are saying that we can measure the distance between two points in any line as we would measure it in $\mathbb{R}$, this is a very powerful statement since this allow us to translate some mathematical properties of the field $(\mathbb{R},+, \cdot)$ to any line.

Observe that $P3$ let us to consider, for any line $r$, some biyection $\gamma \in \mathbb{R}^r$ that preserves the distance between the points of $r$ and the real numbers (measured the last ones with the absoulte value metric we see in Chapter 1):

$$\delta_\mathbb{R}(\gamma(X),\gamma(Y)) = | \gamma(X) - \gamma(Y) | =  d(X,Y) \quad \forall X,Y \in r$$

Then, we are inyecting the real distance to any generic line in the plane.

<br>

#### 3.5.2. Observation 2.8: Midpoint.

Let's define a useful object in the following sections that also serve us as a good application example of the axiom $P3$. Let $r \subset \textbf{P}$ be a line and $A,B \in r : A \neq B$, then:

- $\exists! M \in r : d(A,M) = d(M,B)$ and we call it *midpoint*.

    By $P3$, we know that we can measure $r's$ as if they were real elements, importing an isommetry from $Isom((r,d\|_{r \times r}),(\mathbb{R},\delta_\mathbb{R}))$ which is not empty (by $P3$). So, let be $\gamma \in Isom((r,d\|_{r \times r}),(\mathbb{R},\delta_\mathbb{R}))$, then, let's call $X$ to be the real unknown satisfying:
    
    $$|\gamma(A) - X| = |\gamma(B) - X|$$

    Squaring both parts, dusing the ifference of square's identity and cleaning $X$ (keeping in mind that $A \neq B$ and $\gamma$ is a biyection) we have that this real number is determinated by the expression:

    $$X = \frac{\gamma(A) + \gamma(B)}{2}$$

    Then, since $X$ do exists as a real number, there must exists some unique $M \in r : M = \gamma^{-1}(X) = \gamma^{-1}(\frac{\gamma(A) + \gamma(B)}{2})$.

    <br>

- Observe quicly the result above forces $M \in [A,B]$, if not, $A,B,M \in r \implies Al(A,B,M)$, (by $(2.)$ of the line's properties), and by the alignment definition in a metric space (which state that three alignment elements means for one of them to be in the segment formed by the other two):


    $$M \notin [A,B] \iff (A \in [M,B] \oplus B \in [M,A])$$


    But:

    $$ \begin{aligned} A \in [X,B] \iff d(M,B) = d(M,A) + d(A,B) \underbrace{>}_{A \neq B} d(M,A)\\ \\  B \in [M,A] \iff d(M,A) = d(M,B) + d(A,B) \underbrace{>}_{A \neq B} d(X,B) \end{aligned}$$

    Hence, by the trycotomy property of the real numbers, the only compatible position for $M$ is to be in the segment of endpoints $A,B$.
    
    <br>

Hence, as a summary, $\forall A,B \in \textbf{P} \ \exists! M \in [A,B] : d(A,M) = d(M,B)$, and we call $M$ to be the midpoint between $A, B \in \textbf{P}$; $M = mid[A,B]$. (Note that trivially $A=B \implies mid[A,B] = A = B$).

<br>

## 3.6. Exercise 1.

**Let be $r \subset \textbf{P}$ and $\gamma, \gamma' \in Isom((r,d\|_{r \times r}),(\mathbb{R},\delta_\mathbb{R}))$, then** 

$$\exists a \in \mathbb{R} : [(\gamma' \circ \gamma^{-1} (x) = a + x \quad \forall x \in \mathbb{R}) \oplus (\gamma' \circ \gamma^{-1} (x) = a - x \quad \forall x \in \mathbb{R})]$$

Observe that this result is immediate from the fourth section of the exercise 2 of the post of MetricSpaces.

Since:

$$\delta_\mathbb{R}(x,y) = d(\gamma^{-1}(x), \gamma^{-1}(y)) = \delta_\mathbb{R}(\gamma' \circ \gamma^{-1}(x),\gamma' \circ \gamma^{-1}(y))$$

Then, $\gamma' \circ \gamma^{-1} \in Isom((\mathbb{R},\delta_\mathbb{R}))$ and there exists $\tau \in \mathbb{R}$, $\sigma \in \Set{-1,1}$ such:

$$\gamma' \circ \gamma^{-1}(x) = \sigma x + \tau \quad \forall x \in \mathbb{R}$$

Call $\tau = a$ and conmutate the expression, getting:

$$\gamma' \circ \gamma^{-1}(x) =a + \sigma x  \quad \forall x \in \mathbb{R}$$

<br>

## 3.7. Rays.

### 3.7.1. Definition.

Let be $r \subset \textbf{P}$, $P \in r, \gamma \in Isom((r,d|_{r \times r}),(\mathbb{R},\delta_\mathbb{R}))$, then we define as *ray with vertex $P$* to the sets:

$$\Set{Q \in r \mid \gamma(Q) > \gamma(P)}, \quad \Set{Q \in r \mid \gamma(Q) < \gamma(P)}$$

We often can refer to any of both sets as $\overline{r}$. Observe that both rays doesn't joint in to $r$:

$$\Set{Q \in r \mid \gamma(Q) > \gamma(P)} \cup \Set{Q \in r \mid \gamma(Q) < \gamma(P)} = r \setminus \Set{P}$$

We say two points $S,T$ are on the same side of $P$ when both are in the same ray with vertex $P$.

<br>

### 3.7.2. Observation 2.10. Points in distinct side of a third point.

Two points $X,Y \in r$ are in different sides of $P \in r$ only iff $P \in [X,Y]$.