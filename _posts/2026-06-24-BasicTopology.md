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

2. Finite, Countable and Uncountable Sets.

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

### 2.1.1. Main concepts.

Consider two sets. $A,B \neq \varnothing$. 

Then we define a *function* or application $f$ from $A$ to $B$ and we denote it as:

$$f : A \to B$$

This is a relation which connects each $x \in A$ to one $y \in B$. We denote $f(x)$ to the subset of elements of $B$ related with $x$ by $f$:

$$f(x) := \Set{ y \in B \mid x \ \underbrace{\mapsto}_{f} \ y}$$

Observe that we implicitly define a rule that every function $f$ must satisfy; $f(x)$ is a unary set, it only has one element and thus, through an economization of notation we simply state $f(x) = y$ when $f$ is a function:

$$\forall x \in A \ \exists! y \in B : f(x) = y$$

In this context we state that $A$ is the domain and $B$ is the codomain of $B$ which not necesarily coincide with the set of all the images of $A$ through $f$, denoted by $f(A) := \Set{y \in B \mid \exists x \in A : y = f(x)}$ and called *range* of $f$. 

<br>

### 2.1.2. Injectivity, Surjectivity and Bijectivity.

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

### 2.1.3. Inverse.

Consider $f : A \to B$ to been a relation. In this context we talk about a mappping of $A$ into $B$ through $f$, then we consider the inverse mapping from $B$ to $A$, denoted by $f^{-1}$ as:

$$f^{-1} : B \to A \mid [ \ f^{-1}(y) = x \iff f(x) = y \ ]$$

Let's observe that, if we now turn $f$ to be a function, $f^{-1}$ is a only a function if $f$ is biyective and obviously $f^{-1}$ is biyective as well. Note that:

$$(f \circ f^{-1})(x) = f(f^{-1}(x)) = x = f^{-1}(f(x)) = (f^{-1} \circ f)(x)$$

Thus, we assert that for any function $f$ the inverse function exists if and only if $f$ is biyective.

<br>

## 2.2. Cardinality. Count. Finiteness.

The following section stablishes the mathematically notion of *count*. Let's present the tools used to count.

<br>

First, let's introduce the *cardinality*. Take $A,B \neq \varnothing$, then we say that both sets has the same cardinality if we can define a biyection between them.

Let's observe that:

- We can define a biyection over any set with himself (reflexivity).
- If a biyection is stablished from $A$ to $B$, then the inverse is a biyection of $B$ to $A$ (symmetric).
- If there are biyection from $A$ to $B$ and from $B$ to $C$, the composition of the both is a biyection from $A$ to $C$ (transitivity).

    <br>

Thus, we can define a *equivalent relation* around cardinality; two sets are equivalent if they share his cardinality.

<br>

Now, let's introduce that in mathematics, count consist basically in measure the cardinality of a set, this is, to count is to relate the elements of a set with another set through a biyection. Let's explore this idea formally, let be $A$ some set:

- $A$ is *finite* if exists some $n \in \mathbb{Z}^+ : A \sim [n]$, remember that $[n] = \Set{1,2,\ldots,n}$. In this terms we say that $A$ has cardinality or *cardinal number* of $n$, $[n]$ is the canonical representant of the cardinal-equivalence class of $A$.

- $A$ is *infinite* if its not finite.

- $A$ is *countable* (or enumerable or denumerable) if $A \sim \mathbb{Z}^+$.

- $A$ is *at most countable* if its finite.

- $A$ is *uncountable* if $\nexists S \in \mathcal{P}(\mathbb{Z}^+)  : A \sim S$, note that this involves $\mathbb{Z}^+$ it self.

Note that with this notions two finite cardinal-equivalents sets $A, B$ has the same number of elements, but observe that with infinite sets the idea of have *the same number of elements* becomes quite vague but the biyection idea retains its clarity. 

<br>

Let's see an example with $\mathbb{Z}$ and $\mathbb{Z}^+$ and consider $f: \mathbb{Z}^+ \to \mathbb{Z}$:

$$f(z) := \begin{cases} z/2 \quad z \in 2\mathbb{Z} \\ -\frac{z-1}{2} \quad z \notin 2\mathbb{Z} \end{cases}$$

Observe that this function is injective and suprajective so is a biyection and $\mathbb{Z}$ and $\mathbb{Z}^+$ has the same cardinality.

<br>

Observe that this happens despite the fact that $\mathbb{Z}^+ \subset \mathbb{Z}$, buy a finite set cannot be equivalent to one of its proper subsets. 

<br>

## 2.3. Sequences.

### 2.3.1. Definition.

Let's introduce the notion of a *sequence*. Intuitively a sequence is an infinite sorted list. Formally, a sequence is a function $s : \mathbb{Z}^+ \to A : s(n) \in A$, where $A \neq \varnothing$. 

This function contains two objects that characterizes the information and the set:

- An index over the elements of $A$, which is given by the preimage $n \in \mathbb{Z} : x = s(n) \to x\_n$

- To each index, each position, there is only one element ocupping the slot (this is given by the fact that $s$ is a function) which is called the $n$-th term of the sequence. Observe that two terms of distinct index not need to be distinct.

We often call as $\Set{x\_n}$ to the sequence.

<br>

Observe some interesting relation between sequences and countable sets. Since every countable set is the range of a $1-1$ function defined on $\mathbb{Z}^+$, we may regard every countable set as the range of a sequence of distinct terms. Speaking more loosely, we may say that the elements of any countable set can be arranged in a sequence.

<br>

### 2.3.2. Theorem; Every infinite subset of a countable subset is countable.

Take some $A \subset E$, such $E$ is countable and $A$ is not finite. Since $E$ is countable then exists some biyection $f : \mathbb{Z}^+ \to E$, then we can consider $g: \mathbb{Z}^+ \to A$ as follows; since $A \subset E$ then we can consider the range of $f$ over $A$. Then, each element of $f(A)$ has an index, and since $\mathbb{Z}^+ \subset \mathbb{N}$ has good order, then we can consider first some minimum index $m$ and then we can order $f(A)$ items through his index. Then, $g(1) = x\_m$, and the sucesor of $x_m$ in $A$ receives $g(2)$ and so on, ultimately, we crafted a sequence, $g$ in $A$, thus $g$ is a biyection and $A$ is countable.

<br>

## 2.4. Families. Intersection and Union of a family of sets. Countable and Uncountable example sets.

### 2.4.1. Definition.

Let's now introduce the *family* languages, the indexes family sets and define the union and intersection of an arbitrary family set.

<br>

Let $A$ and $\Omega$ be sets such each $\alpha \in A$ is asociated with a subset of $\Omega$, denoted by $E\_\alpha \subset \Omega$. We denote as $\Set{E\_\alpha}$ to set whose elements are the sets $E\_\alpha$ and call it *collection* of sets or *family* of sets.

<br>

### 2.4.2. Union and Intersection of sets.

The union of the sets $E\_\alpha$ is defined as:

$$\bigcup_{\alpha \in A} E_\alpha := \Set{x \in \Omega \mid \exists \alpha \in A : x \in E_\alpha}$$

<br>

The intersection:

$$\bigcap_{\alpha \in A} E_\alpha := \Set{x \in \Omega \mid x \in E_\alpha \quad \forall \alpha \in A}$$

<br>

### 2.4.3. Relation between Union/Intersection and Sum/Product.

Many properties of unions and intersections are quite similar to those of sums and products; in fact, the words sum and product were sometimes used in this connection, and the symbols $\sum$ and $\prod$ were written in place of $\cup$ and $\cap$. The asociativity and distributivity laws comes from this very same laws in disjuntion and conjuntion.

<br>

### 2.4.4. Cantor's diagonal methods and auxiliary results.

We have the following results:

**The arbitrary union of countable sets is a countable set. First Cantor's diagonal method.**

Let' be $\Set{E\_n} : n = 1,2,3,\ldots$ be a collection or family of countable sets, then consider:

$$S = \bigcup_{i=1}^\infty E_n$$

First, since $E\_n$ for each $n =1,2,3,\ldots$ is numerable, then we can consider a biyection $f : \mathbb{Z}^+ \to E\_n$ for each $n$, this biyection allow us to arrange or list the elements of $E\_n$ in a row

$$E_n :=\Set{x_{1n}, x_{2n}, x_{3n}, \ldots}$$

Let's do this for each $n$ obtaining something like a matrix where each row is the sorted $E\_n : n = 1,2,3,\ldots$ 

$$S =\begin{pmatrix} x_{11} & x_{12} & x_{13} & \ldots \\ x_{21} & x_{22} & x_{23} & \ldots \\ x_{31} & x_{32} & x_{33} & \ldots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

Note that the 'matrix' denomination of this structure is just an intuitive approximation and we are not saying that it is properly a matrix at all.

Then, observe we can sort this elements by diagonalizating them, forming the sequence:

$$x_{11}, x_{21},  x_{12},  x_{31},  x_{22},  x_{13}, \ldots $$

Observe then that as an arranged list, we can define a biyection over it, thus $S$ is countable.

<br>

**The at most countable union of at most countable sets is at most countable**

The proof is similar to the above.

<br>

**If $A$ is countable, then $A^n$ is countable for any $n \in \mathbb{N}$**

Let's proof this result by induction.

Take $n = 1$, then this result is immediate since $A^1$ is $A$.

Then, let's give it true for some $n \in \mathbb{N}$, and consider $A^{n}$, each element is of the form $(a\_1,\ldots, a\_{n-1}, a_n) \in A^n$, calling $\alpha = (a\_1,\ldots,a\_{n-1}) \in A^{n-1}$, then the first is identifiable with the pair $(\alpha,a\_n)$, observe that fixed some $\alpha$, the set of the pairs $(\alpha,a) : a \in A$ can be identified with $A$ it self, meaning that is countable and his elements can be arranged in a row:

$$(\alpha,a_1)_1,(\alpha,a_2)_2,(\alpha,a_3)_3,\ldots $$

Also observe that since $A^{n-1}$ is countable as well, then, for each $a \in A$ the set of the pairs $(\alpha,a) : \alpha \in A^{n-1}$ is countable as well and it can be disposed in a column, obtaining a structure in which we can use the first Cantor diagonal method.

$$(\alpha_1,a_1),(\alpha_1,a_2),(\alpha_1,a_3),\ldots $$

$$(\alpha_2,a_1),(\alpha_2,a_2),(\alpha_2,a_3),\ldots $$

$$(\alpha_3,a_1),(\alpha_3,a_2),(\alpha_3,a_3),\ldots $$

$$\quad \quad \vdots \quad \quad \quad \quad \vdots \quad \quad \quad \quad \vdots \quad \quad \quad$$

Allowing us to create the sequence:

$$(\alpha_1,a_1)_1,(\alpha_2,a_1)_2, (\alpha_1,a_2)_3, (\alpha_3,a_1)_4, (\alpha_2,a_2)_5, (\alpha_1,a_3)_6,\ldots $$

Reidentificating the pair $(\alpha,a)$ with the tuple $(a_1,\ldots,a_n) \in A^n$, we have created a biyection from $\mathbb{Z}^+$ over the elements of $A^n$, so this is is countable as well.

<br>

Essentially observe that we reused the argument provided in the first point since $A^n$ is the countable union of the countable sets $\Set{(\alpha,a) : a \in A}$ for each $\alpha \in A^{n-1}$, so is countable.

<br>

**$\mathbb{Q}$ is countable**

Observe that we can again reuse the argument before. We did see that $\mathbb{Z}$ is countable so each set $E\_m = \Set{n/m : n \in \mathbb{Z}}$ for some $m \neq 0$ is countable, thus:

$$\mathbb{Q} := \bigcup_{m \in \mathbb{Z}^+}E_m$$

Is countable.

<br>

**Uncountable set. Second Cantor's diagonal method. $\mathbb{R}$ is uncountable.**

This is an example of an infinity which is strictly greater than $\mathbb{N}$. Consider the set $A:=\Set{0,1}^\mathbb{N}$, of all the functions $s:\mathbb{N} \to \Set{0,1}$. Observe that each sequence is the *indicator* function of some subset of $\mathbb{N}$, for which is in biyection with $\mathcal{P}(\mathbb{N})$, hence the theorem is $card(\mathbb{N}) \leq card(\mathcal{P}(\mathbb{N}))$.

<br>

Take $E \subseteq A$ as countable consisting in the sequences $s\_1,s\_2,s\_3,\ldots$. Then, take some sequence $s$ crafted as:

If the $n$-th digit in $s\_n$ is $1$, then the $n$-th digit of $s$ is $0$ provoking that $s$ differs from any element of $E$ in at least one place so $s \notin E$ but $s \in A$ since $s$ is composed of $0$ and $1$ so $E \subset A$. Any countable subset of $A$ is a proper subset, thus $A$ can't be countable (or it would be its own countable subset) and is uncountable. 

<br>

Laterly we will see that $\mathbb{R}$ admits a binary representation and this same result will apply to demonstrate that $\mathbb{R}$ is uncountable.

<br>

## 2.5. Summary.

Let's take a brief summary of section $2$. First, we introduce the relation and a concrete form or relation which we called *function*, which is a relation for which the image set for any element of the domain is a unary-non-empty set.

Then we introduced the biyection, or one-to-one relations and along with it the mathematically conception of *count* which is identify the elements of two sets through a biyection in the sense that we can attach each element with another unique item of other set, stablishing that both sets has the same number of elements, the same cardinality. The cardinality equivalence is a relation equivalence in which the canonical representant is the natural number subsets, $[n]$.

Later

# 3. Metric Spaces.



<br>