---
layout: post
title: "Topology of Metric Spaces"
subtitle: "Finite,Countable & Uncountable Sets, Metric Spaces, Compact Sets, Perfect Sets, Connected Sets"
date: 2026-06-17 09:00:00 +0000
categories: ['Analisis Rudin']
tags: ['Maths']
author: German Sanmi
subject: topology, real-analysis
lang: en
---

# 0. Index.

1. Introduction.

2. Finite, Countable adn Uncountable Sets.

    <br>

# 1. Introduction.

First, let's explain why there is a topology chapter in an analysis book.

As we asserted in other chapter, Analysis is the study of the *limits*, and the limit is essentially a statement about closeness. Then, the *Topology* is the branch which isolates and study the notions of closeness, proximity or continuity in abstract without appealing to distances or metrics.

Hence, this topology chapter brings to the reader a precise vocabulary-kit in which the terms limit, continuity or convergence have complete sense. The hardest theorems of elementary analysis are, in fact, topological theorems.

Analysis emerges to give foundation to Calculus works which, before analysis, it worked with a non-fully-deployed but intuitive idea of limit, then called *infinitesimals*; $dx$. Primordial analysis stablished a first *limit* definition that, despite being rude, was mathematically accurate:

$$\lim_{x \to a} f(x) = L \quad \Longleftrightarrow \quad \forall\,\varepsilon>0\;\;\exists\,\delta>0\;:\;0<|x-a|<\delta\implies |f(x)-L| < \varepsilon $$

Observe that this first definition involves the metric, this means that this limit idea is not property of the real field, is property of the space in which a proximity notion exists which is what the topology studies.

Later, topologic concepts rebuilt the limit concept in a simplier way, disregarding metrics and epsilons and using heavy geometric nuance.

<br>

Thus, there is three level of abstractions. First let's barely introduce what the *open sets* are; an open set is a set in which all its points are interior points. Intuitively, this means that the set does not contain its boundary, allowing you to approach any element without stepping outside the set's limits.

<br>

Thus:

- A **topologic space**; is a set $X$ along witha a collection of open subsets following three axioms.

- A **metric space**; is a particular case of toplogic space in which the open subsets gets generated with the metric. In some sense, an open set is a set in which every element has an "enviroment" of elements (defined by the metric) within the set, like a circule or sphere centered in the element which enterly falls inside the set.

- A **euclidean space** is a particular case of the metric space in which the metric is the *euclid norm*.

    <br>

Thus, the topology introduced in this section is the *metric spaces topology*. 

<br>

# 2. Finite, Countable and Uncountable Sets.

We begin this section with a definition of the function concept.

<br>

## 2.1. Functions. Applications.

**Main concepts**

Consider two sets. $A,B \neq \varnothing$. 

Then we define a *function* or application $f$ from $A$ to $B$ and we denote it as:

$$f : A \to B$$

To a relation such connect each $x \in A$ to one $y \in B$. Thus, we denote $f(x)$ to the subset of elements of $B$ related with $x$ by $f$:

$$f(x) := \Set{ y \in B \mid x \ \underbrace{\mapsto}_{f} \ y}$$

Observe that we implicitly define a rule that every function $f$ must satisfy, which is that $f(x)$ is a unary set or simply $card(f(x)) = 1$ and thus, through an economization of notation we simply state $f(x) = y$ when $f$ is a function:

$$\forall x \in A \ \exists! y \in B : f(x) = y$$

In this context we state that $A$ is the domain and $B$ is the codomain of $B$ which not necesarily coincide with the set of all the images of $A$ through $f$, denoted by $f(A) := \Set{y \in B \mid \exists x \in A : y = f(x)}$ and called *range* of $f$. 

<br>

**Injectivity, Surjectivity and Bijectivity**

Let's explore three important concepts about how relations connect input with outputs. Be $f : A \to B$ a application, then: 

- **Inyective**: We say that $f$ is *inyective* it verifies no colisions with images, formally:

    $$\forall x,y \in A : x \neq y \implies f(x) \neq f(y)$$

    <br>

- **Surjective**: We say that $f$ is *surjective* when the range of $f$ coincide with the codomain $f(A) = B$, intuitively it has no gaps, every element on the codomain is reached:

    $$\forall y \in B \ \exists x \in A : f(x) = y$$

    <br>

- **Biyective**: We say that $f$ is *biyective* when is a "one-to-one" correspondence between the elements of $A$ and $B$:

    $$\forall y \in B \ \exists ! x \in A : f(x) = y$$

    Let's observe that $f$ is biyective if and only if is at the same time surjective and inyective.


<br>

**Inverse**

Consider $f : A \to B$ to been a relation. In this context we talk about a mappping of $A$ into $B$ through $f$, then we consider the inverse mapping from $B$ to $A$, denoted by $f^{-1}$ as:

$$f^{-1} : B \to A \mid [ \ f^{-1}(y) = x \iff f(x) = y \ ]$$

Let's observe that, if we now turn $f$ to be a function, $f^{-1}$ is a only a function if $f$ is biyective and obviously $f^{-1}$ is biyective as well. Note that:

$$(f \circ f^{-1})(x) = f(f^{-1}(x)) = x = f^{-1}(f(x)) = (f^{-1} \circ f)(x)$$

Thus, we assert that for any function $f$ the inverse function exists if and only if $f$ is biyective.

<br>

## 2.2. Equivalence Relation. Cardinality.



<br>
