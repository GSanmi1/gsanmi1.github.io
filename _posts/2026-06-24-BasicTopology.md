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

Let's take a brief summary of section $2$. 

First, we introduce the relation and then a specific form or relation which we called *function*, which the image set for any element of the domain is a unary-non-empty set.

Then we introduced the *biyection*, or one-to-one relations and along with it the mathematically conception of *count* which is identify the elements of two sets through a biyection in the sense that we can attach each element with another unique item of other set, stablishing that both sets has the same number of elements, the same cardinality. The cardinality equivalence is a relation equivalence in which the canonical representant is the natural number subsets, $[n]$.

Later, we define what sequences are and define some concepts with sequences and biyections; finitness (biyection with some $[n]$ for some $n \in \mathbb{Z}^+$) and countableness (biyection with $\mathbb{Z}^+$) and by opposition, infinite and uncoutableness.

Then presented the definition of family sets and presented some results involving family of sets and countable sets along with Cantor diagonalization methods with which we try to present to types of infinites, $\mathbb{N}$ for countable sets, every countable sets has the same number of elements than $\mathbb{N}$ and then uncountables sets which has more elements than $\mathbb{N}$, $\mathbb{Q}$ is countable meanwhile $\mathbb{R}$ is uncountable.

<br>

# 3. Metric Spaces.

## 3.1. Reminder.

We shall now introduce what metric spaces were. Be $X$ a set of points, then we define $d:X \times X \to \mathbb{R}$ a function called *distance* or *metric* function, satisfying the following properties:

- **Defined positive**: $d(x,y) > 0  \wedge \big[d(x,y) = 0 \iff x = y\big] \quad \forall x,y \in X$

- **Simetric** $d(x,y) = d(y,x) \quad \forall x,y \in X$

- **Triangle Inequality**: $d(x,z) \leq d(x,y) + d(y,z) \quad \forall x,y,z \in X$

Metric spaces tries to capture structures in which is possible to measure a property between elements that we call distance. For now on, we should think in $\mathbb{R}^2$ or $\mathbb{R}$ as examples of metric spaces.

Observe also that any subset of a metric space is also a metric space.

<br>

## 3.2. Bounded neighborhoods of $\mathbb{R}^k$.

### 3.2.1. $K$-cells.

Let's introduce the following notions:

- We call *segment*, and we denote it as $(a,b)$, to be the collection of all the real numbers from $a$ to $b$ without neither of the two to being included:

    $$(a,b) := \Set{x \in \mathbb{R} : a < x < b}$$

    <br>

- We call *interval* to the segment with his endpoints included:

    $$[a,b] := \Set{x \in \mathbb{R} : a \leq x \leq b}$$

    <br>

- This both definitions can be combined, in what we call *half-open intervals*:

    $$[a,b) := \Set{x \in \mathbb{R} : a \leq x < b}$$

    $$(a,b] := \Set{x \in \mathbb{R} : a < x \leq b}$$

    <br>

Note then that, if $\mathbb{R}$ is a total ordered set, which legitimate to arrange it in line, the real line, then segments and intervales are collections of elements which respects that total order as singular pieces of the real line.

<br>

However, segments and intervals are just the one-dimension representation of those collections. 

Consider now $\mathbb{R}^k$, and $\alpha = (a\_1, \ldots, a\_k), \beta = (b\_1,\ldots, b\_k) \in \mathbb{R}^k : a\_i < b\_i \quad \forall i \in [k]$, then we call as $k$-cell to those $x = (x\_1,\ldots,x\_k)  \in \mathbb{R}^k : a\_i < x\_i < b\_i$.

$$\sigma^{\alpha \beta}_k :=\Set{\mathbf{x} = (x_1, \ldots, x_k) : a_i \le x_i \le b_i \quad \forall i \in [k]}$$

Let's observe some interesting caracterization, $\sigma^{\alpha \beta}_k$ is in fact a cartesian product of real intervals:

$$\sigma^{\alpha \beta}_k := \prod_{i=1}^k [a_i,b_i] = \Set{\mathbf{x} \in \mathbb{R}^k \mid x_i \in [a_i,b_i]}$$

Which delimitates an hipersurface for any $k \geq 2$ caracterized by two points, $a$ and $b$. Essentially, $k$-cells are the generalization of intervals and segments two multiple dimensions which are the collection of common neighborhs that two points of the space share.

<br>

### 3.2.2. Neighboorhood. Balls. Convexity.

**Neighboorhood. Balls.**

Let's start talking about what a neighboorhod is. 

In colloquial language, we usually use the term *neighboor* or *neighboorhood* to talk about those entities, those equals, that are reasonably near between them, it could be people coliving in the same building, in the same town or even in the same city.

Here, talking about real numbers in a metric space, we will concrete this grade of nearness by using the distance/metric. Take for example some point $p \in \mathbb{R}^k$, then we delimit the neighboorhod of $p$ to be the set of all the points satisfying not being farest away from some distance:

$$N_r(p) := \Set{ x \in \mathbb{R}^k \mid d(x,p) < r}$$

Which is traduced on some ball of radius $x$ centered on $p$.

<br>

We talk about open/closed balls to refer if the distance is strictly less or less or equal than $r$.

<br>

**Convexity**

We are going to present the *convexity*, which is strongest and simplest form of geoemtric regularity. Despiste this is in a topology section, convexity is an afine property but it fits as an important $\mathbb{R}^k$ property.

<br>

Then, consider now $E \subset \mathbb{R}^k$, then:

$$E \text{ is convex } \iff \lambda x + (1 - \lambda) y \in E \quad  \forall x,y \in E \wedge \lambda \in (0,1)$$

Let's observe carefully here that $\lambda x + (1 - \lambda) y = \lambda(x-y) + y$, calling $\overrightarrow {v} = x - y$, then we are just unwrapping the point-vector equation of the line at $y$ towards $\overrightarrow {v}$ and restricting it to the segment $(y,x)$ by restricting $\lambda$ to $(0,1)$. 

Thus, essentially, we define a subset of the euclidian space to be *convex* when it contains the segment of any two points of the subset.

<br>

Observe for example that balls are convex subsets. We can think in a ball $N_r(p)$ and in two points in it and think in the plane going through those 3 points and then in thre triangle of vertix those three points. Is obvious that no point in the $XY$ side is more than $r$ distance from the center.

Also, we can stablish that, being $q \in (y,x)$, then for some $\lambda \in (0,1)$:

$$|q - p | = |\lambda x + (1 - \lambda) y - p | = |\lambda(x - p) + (1 - \lambda)(y-p)| \leq $$

$$\leq \lambda |x - p| + (1-\lambda)|y-p| < \lambda r + (1-\lambda)r < r $$

Since $\lambda \in (0,1)$.

<br >


## 3.3. Essential topologic notions.

Now we are going to present the vocubulary in which the results of the real analysis are presented.

In generic topology all departs from the family of open the sets, then the general notions in which the rest of the definition are describe departs from open sets. How ever, since we are not interested in toplogy at all but in topology of metric spaces, we leverage the metric or distance to define a natural object; the ball, which will be used to build the complete structure:

<br>

### 3.3.1. Neighborhood.

As we stated above, for some element $p \in X$, we define the neigborhood of $p$ in $X$ to be a ball; $N\_r(p)$. This balls groups those $x \in X$ which are reasonably (arbitrary) near to $p$:

$$N_r(p) := \Set{ x \in \mathbb{R}^k \mid d(x,p) < r}$$

<br>

### 3.3.2. Closed Sets: Limit points and Isolated points.

Let's introduce the *limit points*. These are basically those points upon which $E$ piles up. We consider $p \in X$ to be a *limit point* of $E$ if every neighborhood contains at least some other point of $E$, formally:

$$p \in X \text{ is a limit point of } E \iff  (N_r(p)\setminus \Set{p}) \cap E \neq \varnothing \quad \forall r \in \mathbb{R}^+$$

<br>

We define the *isolated point* notion by negating the idea of limit point, this is an isolated point is that point which is not a limit point formally:

$$p \in X \text{ is an isolated point of } E \iff (\exists r \in \mathbb{R}^+ :  (N_r(p)\setminus \Set{p}) \cap E = \varnothing \wedge p \in E) $$

<br>

Having this two concepts clear, let's introduce the main notion of *closed set*, which abstract the idea of own everything to which it piles up. Taking again $E \subset X$, then $E$ is a *closed* set if every limit point is a point of $E$. Formally;

$$E \subseteq X \text{ is a closed set } \iff \Big[\forall p\big(\forall r[(N_r(p)\setminus \Set{p}) \cap E \neq \varnothing]\implies p \in E \big) \Big]$$

Then, observe that $E$ is closed if every $p \in X$ satisfies a condition, which is if $p$ is a limit point then $p \in E$. Let's call $E' := \Set{p \in X \mid \forall r[(N_r(p)\setminus \Set{p}) \cap E \neq \varnothing] }$, the set of all the limit points of $E$, then, the definition above can be reexpresed as: $E \subset X \text{ is a closed set } \iff[\forall p( p \in E'\implies p \in E)]$, or simply:

$$E \subseteq X \text{ is a closed set } \iff E' \subseteq E$$

<br>

A closed set is basically a set without "gaps", for example, take $\mathbb{Q} \subset \mathbb{R}$, then $\mathbb{Q}$ by the stated in the chapter 1 of the book, $\mathbb{Q}$ is naturally not a closed subset of $\mathbb{R}$. 

Observe that essentially is *stability under limitness*; a closed set contains those points to which other points of $E$ piles up. 

<br>

### 3.3.3. Open Sets: Interior points and Boundary points.

An interior point of $E \subseteq X$ is, intuitively, a "well embebbed" (or strictly inside) point in $E$. A point $p \in X$ is called to be an *interior point* of $E$ if exists some neigborhood of $p$ in $E$, formally:

$$ p \in X \text{ is an interior point of } E \iff \exists r \in \mathbb{R}^+ : N_r(p) \subseteq E$$

We denote as $E^\circ$ to the set of all the interior points of $E$ and we call it, *interior* of $E$. Observe quickly that we have: $p \in E^\circ \implies \exists r : N_r(p) \subseteq E \implies p \in E$, hence $E^\circ \subseteq E$.

<br>

We say that an *open set* is a set such all his points are interior points.

$$E \subseteq X \text{ is an open set } \iff \forall p( p \in E \implies \exists r : N_r(p) \subseteq E) \iff E = E^\circ$$

<br>

Observe something interesting, take $X = \mathbb{R}$ and the set $E := \Set{x \mid x < \sqrt{2}}$, observe then that we can consider as well $X \setminus E := \Set{x \mid x \geq \sqrt{2}}$, but $E^\circ \cup (X \setminus E)^\circ \neq X$, since $\sqrt{2}$ doesn't fall as an interior point of $E$ or his complementary. 

In other words, in general is: $E^\circ \cup (X \setminus E)^\circ \subseteq X$ and we call the *boundary* of $E$, $\partial E$, to those points which aren't interiors nor exteriors (exterior as what is strictly out of $E$, this is; the interior of the complementary of $E$) of $E$:

$$\partial E := X \setminus \big[E^\circ \cup (X \setminus E)^\circ\big] = \Set{ p \in X \mid \nexists r(N_r(p) \subseteq E \vee N_r(p) \subseteq X \setminus E) }$$

<br>

Observe that, by definition is $\partial E \cap E^\circ = \varnothing$. Observe also that the following statements are equivalents

$$\underbrace{\forall E (X = E \sqcup X \setminus E)}_{1} \iff \underbrace{\forall E\forall p(p \in X \implies p \in E \oplus p \in X \setminus E)}_{2} \iff$$

$$\underbrace{\forall E,N \big[ (N \cap E = \varnothing \iff N \subseteq X \setminus E) \wedge (N \cap X \setminus E = \varnothing \iff N \subseteq E) \big]}_{3}$$

$1$ and $2$ coimplies by definition, let's see $2 \leftrightarrow 3$ with generic sets $A,B \subset X$

- $2 \to 3$; Suppose $A,B \subset X : X = A \sqcup B$, then consider some $N \subseteq X$, we have that:

    $$\begin{cases} N \cap A = \varnothing \iff \forall x \in N (x \notin A) \iff \forall x \in N (x \in B) \iff N \subseteq B \\ N \cap B = \varnothing \iff \forall x \in N (x \notin B) \iff \forall x \in N (x \in A) \iff N \subseteq A \end{cases}$$

- $3 \to 2$; Suppose now some $A,B \subset X$ for which the following statement is true:

    $$\forall N \big[ (N \cap A = \varnothing \iff N \subseteq B) \wedge (N \cap B = \varnothing \iff N \subseteq A) \big]$$

    Then, consider some $p \in X$ and call $N = \Set{p}$, for any point and any subset, the point can be in or out of the subset, then:

    $$ \begin{cases} p \in A \iff N \subseteq A \iff N \cap B = \varnothing \iff p \notin B \\ p \notin A \iff N \cap A = \varnothing \iff N \subseteq B \iff p \in B\end{cases}$$

    Hence, in this conditions is $[p \in X \implies (p \in A \oplus p \in B)] \iff X = A \sqcup B$.

<br>

This essentially means that in an disjoint union, any disjoint subset from one part falls enterely in the counter part. We can transport this equivalence to the $\partial E$ definition:

$$\partial E = \Set{ p \in X \mid \nexists r(N_r(p) \subset E \vee N_r(p) \subset X \setminus E) }$$

$$ = \Set{ p \in X \mid \nexists r(N_r(p) \cap X \setminus E = \varnothing\vee N_r(p) \cap E = \varnothing) }$$

$$= \Set{ p \in X \mid \forall r(N_r(p) \cap X \setminus E \neq \varnothing \wedge N_r(p) \cap E \neq \varnothing) } $$

Hence $\partial E$ is the set of those points for which any neigboorhood contains points from $E$ and the complementary of $E$. Observe that, as defined is:

$$\forall E [X = E^\circ \sqcup \partial E \sqcup (X \setminus E)^\circ]$$

Then, an open set is simply a set not containing any point of his boundary:

$$E \subseteq X \text{ is an open set } \iff E \cap \partial E = \varnothing$$

Observe as a brief explanation that $\Rightarrow$ is inmediate, observe that also is $\Leftarrow$ since if we consider some $p \in X$, then it only can be in one and only one of the three sets, we do know that $E$ and $(X \setminus E)^\circ$ are disjoint as well as $E$ and $\partial E$ by the premise so we have that $\forall p(p \in E \implies p \in E^\circ) \implies E = E^\circ$ and $E$ is open.

<br>

### 3.3.4. Perfect Sets.

The *perfect* sets are in some way a restriction of the notion of closed sets.

We recall that a closed set is a set that contains everything it approaches, abstracted behind the idea of limitness or limit point, those containing in every possible neighborhood part of the set (without being the point it self).

<br>

Then, the perfect sets add to the closed sets the reverse statement; meaning that a perfect set is a closed set such every point is also a limit point (or, in other words, a closed set without isolated points). In this sense, a perfect set is a closed set that also approachs every point it owns.

<br>

Is important to warn the nuance that a closed set adds to perfect sets. Be a closed set garantee that every limit point is a point of the set, a perfect set without being closed is just a set without isolated points, but that doesn't means that every limit point is part of the set, it just means that every point of the set is a limit point of the set, giving some blurred perception of the structure.

Perfect sets abstract in some manner an informal idea of density, it owns everything it approachs and every point close enough to the set is in fact a point of the set. 

<br>

### 3.3.5. Bounded Sets.

$E$ is bounded if there is a $M \in \mathbb{R}$ and $q \in X$ such $d(p,q) < M$ for any $p \in E$.

Take as an example $E := (0,2)$, then $E$ is bound since for $2 \in \mathbb{R}$ is $d(2,e)< 2$ for any $e \in E$.

<br>

### 3.3.6. Dense.

We say that $E \subset X$ is dense in $X$ if any point of $X$ is a point of $E$ or a limit point of $E$. Think for example that $\mathbb{Q}$ is dense in $\mathbb{R}$, take some point in $\mathbb{R}$, if is not a rational, then is an irrational to which we can approximate through rationals as much as we want.


## 3.4. Important topologic result.

Let's see some important results around the concepts seen before.

<br>



### 3.4.1. Every neighborhood is an open set.

Let's observe some interesting fact. An open set is a set in which every point has enough space to have an enviroment. Observe that this same applies to an enviroment it self, this is, any neighborhood is it self an open set and this is a property allowed directly by the triangular inequality satisfied by the metric $d$.

<br>

To formally demonstrate it we have to demonstrate that each point of a neigborhood is wrapped in his own ball.

Take some $x \in X$ and consider some generic neighborhood $N_r(x) := \Set{p \mid d(x,p)<r}$ and take some point $p \in N_r(x)$. Now, consider $t \leq r - d(x,p) \in \mathbb{R}$ and $N_t(p)$. Let's see that $N_t(p) \subset N_r(x)$.

Consider the point $q \in N_t(p) \implies d(p,q)< t \leq r - d(x,p)$. Hence:

$$d(x,q) \leq d(x,p) + d(p,q) < d(x,p) + (r - d(x,p)) = r \implies q \in N_r(x)$$

Following the triangular inequality.

<br>

### 3.4.2. Limit points contains infinite points of the set for each neighborhood.

Let's reason to the absurd.

Consider $p \in X$ a limit point of $E \subset X$ and some $N_r(p)$. Then, $(N\_r(p)\setminus \Set{p}) \cap E \neq \varnothing$. Let's suppose is finite, then, since $\mathbb{R}$ is a total ordered set, we can consider a minimum distance: 

$$\alpha = \min\Set{d(p,q) \mid q \in  (N_r(p)\setminus \Set{p}) \cap E} \implies \nexists q \in (N_r(p)\setminus \Set{p}) \cap E : d(q,p) < \alpha$$

But observe that, since $p$ is a limit point, again:

$$(N_\alpha(p)\setminus \Set{p}) \cap E \neq \varnothing \implies \exists t \in (N_\alpha(p)\setminus \Set{p}) \cap E : d(p,t) < \alpha < r$$


$$\implies t \in (N_r(p)\setminus \Set{p}) \cap E$$



In contradiction with the fact that $\alpha$ is the minimum distance achiveable in $(N\_r(p)\setminus \Set{p}) \cap E$. 

Hence, finitness in the intersection of any neighborhood with $E$ implies that we can consider a minimum distance leading to a contradiction, so this intersection for any neigborhood is not a finite set.

<br>


### 3.4.3. Examples.

Let's consider now some subsets of $\mathbb{R}^2$ and let's see what type of topological set they are:



# 4. Compact sets.



<br>