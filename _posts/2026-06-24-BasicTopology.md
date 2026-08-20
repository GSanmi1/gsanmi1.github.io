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

The following section stablishes the mathematically notion of *count*. Take some $X$ and consider the set $\mathcal{P}(X)$ and let be $A,B \in \mathcal{P}(X)$.

<br>

In this context, we define the *cardinality* over $\mathcal{P}(X)$ as the invariant between elements related by a biyection.

$$A, B \text{ has the same cardinality } \iff \exists \text{ a biyection } f : A \to B$$

Let's consider the relation between two sets that share cardinality; $A \sim B$. Observe that:

- We can define a biyection over any set with himself (reflexivity); $A \sim A$
- If a biyection is stablished from $A$ to $B$, then the inverse is a biyection of $B$ to $A$ (symmetric).

    $$A \sim B \implies \exists f \in B^A : f \text{ is a biyection } \implies f^{-1} \in A^B \text { is a biyection } \implies B \sim A $$
- If there are biyection from $A$ to $B$ and from $B$ to $C$, the composition of the both is a biyection from $A$ to $C$ (transitivity).

    $$A \sim B \wedge B \sim C \implies \exists f \in B^A, g \in C^B : f,g \text{ are biyections }$$
    
    $$\implies f \circ g \in C^A \text { is a biyection} \implies A \sim C$$

    <br>

Ultimately meaning that "share cardinality", is a equivalence relation. Two sets are equivalent if they share his cardinality. Observe that, when two sets are finite and share cardinality, essentially we are saying that both has the same number of elements.



<br>

Now, let's introduce that in mathematics, count consist basically in measure the cardinality of a set, this is, to count is to relate the elements of a set with another set through a biyection. Let's explore this idea formally, let be $A$ some set:

- $A$ is *finite* if exists some $n \in \mathbb{Z}^+ : A \sim [n]$, remember that $[n] = \Set{1,2,\ldots,n}$. In this terms we say that $A$ has cardinality or *cardinal number* of $n$, $[n]$ is the canonical representant of the cardinal-equivalence class of $A$.

- $A$ is *infinite* if its not finite.

- $A$ is *countable* (or enumerable or denumerable) if $A \sim \mathbb{Z}^+$.

- $A$ is *at most countable* if its finite or countable.

- $A$ is *uncountable* if $\nexists S \in \mathcal{P}(\mathbb{Z}^+)  : A \sim S$, note that this involves $\mathbb{Z}^+$ it self.

Note that with this notions two finite cardinal-equivalents sets $A, B$ has the same number of elements, but observe that with infinite sets the idea of have *the same number of elements* becomes quite vague but the biyection idea retains its clarity. 

The key is that *biyections* abstracts the idea of pairing up. Count is pairing two finite set of elements in the sense that we can say that $A$ has many elements as $B$. This idea how every loose sense when the sets has infinite elements, because there is no finite secuence of naturales to pair up with the set, count this set never ends. How ever, cardinality as the invariant property under biyection retains this sense and its restrictions.

**Cardinality is not the number of elements a set has, it is the perspective that treats two sets as equal insofar as we can pair their elements one-to-one.**

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

We recall that a closed set is a set that contains everything it approaches, abstracted behind the idea of limitness or limit point, those points containing in every possible neighborhood other points of the set.

$$E \subset X \text{ is closed } \iff E' \subset E$$

Then, the perfect sets standsby adding the reverse statement; meaning that a perfect set is a closed set such every point is also a limit point (or, in other words, a closed set without isolated points). In this sense, a perfect set is a closed set that also approachs every point it owns.

$$E \subset X \text{ is perfect } \iff E' = E$$

Is important to warn the nuance that a closed set adds to perfect sets. Be a closed set garantee that every limit point is a point of the set, a perfect set without being closed is just a set without isolated points, but that doesn't means that every limit point is part of the set, it just means that every point of the set is a limit point of the set, giving some blurred perception of the structure.

Perfect sets abstract in some manner an informal idea of density, it owns everything it approachs and every point close enough to the set is in fact a point of the set. 

<br>

### 3.3.5. Bounded Sets.

$E$ is bounded if there is a $M \in \mathbb{R}$ and $q \in X$ such $d(p,q) < M$ for any $p \in E$.

$$E \text{ is bounded } \iff \exists q \exists M: d(p,q) < M \quad \forall p \in X$$

Observe that $E \subset X$ is bounded iff it exists as a subset of a neighbourhood of a point of $X$.

$$E \text{ is bounded } \iff \exists p \exists r: E \subset N_r(p)$$

<br>

### 3.3.6. Dense Sets.

We say that $E \subset X$ is dense in $X$ if any point of $X$ is a point of $E$ or a limit point of $E$. 

$$E \text{ is dense in } X \iff \forall p \Big(p \in E \vee \forall r \big([N_r(p) \setminus \Set{p}] \cap E \neq \varnothing \big) \Big)$$


Think for example that $\mathbb{Q}$ is dense in $\mathbb{R}$, take some point in $\mathbb{R}$, if is not a rational, then is an irrational to which we can approximate through rationals as much as we want.

<br>

## 3.4. Important topologic results.

Let's see some important results around the concepts seen before.

<br>



### 3.4.1. Every neighborhood is an open set.

Let's observe some interesting fact. 

An open set is a set in which every point has enough space to have an environment this applies to the notion of "environment" it self. Any neighborhood is it self an open set and this is a property allowed directly by the triangular inequality satisfied by the metric $d$.

<br>

To formally demonstrate it let's build, for each point of a generic neighbourhood, a ball contained in the neighbourhood.

Let be $(X,d)$ a metric space, consider $p \in X$ and the neighborhood $N_r(p)$ for some $r \in \mathbb{R}^+$. Now consider $q \in N_r(p)$, since $d(p,q) < r \implies \exists t \in \mathbb{R}^+ : d(p,q) + t < r$. Let's consider then consider such $t$ and take the set $N_t(q)$.

Observe then that, for any $h \in N_t(q)$, using the triangular inequality:

$$d(h,p) \leq d(h,q) + d(p,q) < \big(r - d(p,q)\big) + d(p,q) = r \implies h \in N_r(p)$$



Lastly, again, since $h$ and $q$ are arbitrary, the demonstration above applies to each $h$ of some neighborhood of any point $q$ of $N_r(p)$, hence:

$$\forall q \in N_r(p) \ \exists t : \forall h (h \in N_t(q) \implies h \in N_r(p))  \iff \forall q( q \in N_r(p) \implies \exists t: N_t(q) \subset N_r(p))$$


And $N_r(p)$ is an open set. 

<br>

### 3.4.2. Limit points contains infinite points of the set for each neighborhood.

Let's reason to the absurd.

Consider $p \in X$ a limit point of $E \subset X$ and some $N_r(p)$. 

Then, $(N\_r(p)\setminus \Set{p}) \cap E \neq \varnothing$. Let's suppose is finite, then, since $\mathbb{R}$ is a total ordered set, we can consider a minimum distance: 

$$\alpha = \min\Set{d(p,q) \mid q \in  (N_r(p)\setminus \Set{p}) \cap E} \implies \nexists q \in (N_r(p)\setminus \Set{p}) \cap E : d(q,p) < \alpha$$

But observe that, since $p$ is a limit point, again:

$$(N_\alpha(p)\setminus \Set{p}) \cap E \neq \varnothing \implies \exists t \in (N_\alpha(p)\setminus \Set{p}) \cap E : d(p,t) < \alpha < r$$


$$\implies t \in (N_r(p)\setminus \Set{p}) \cap E$$



In contradiction with the fact that $\alpha$ is the minimum distance achiveable in $(N\_r(p)\setminus \Set{p}) \cap E$. 

Hence, finitness in the intersection of any neighborhood with $E$ implies that we can consider a minimum distance leading to a contradiction, so this intersection for any neigborhood is not a finite set.

<br>

### 3.4.3. Examples.

Let's consider now some subsets of $\mathbb{R}^2$ and let's see what type of topological set they are:

- $E= \Set{z \in \mathbb{C} \mid \|z\| < 1}$

    **$E$ is not closed**.

    Observe that the set is essentially the disk of center $0$ and radious $1$ without the border.

    Let's consider the point $p = (1,0) \notin E$. Let's see $p \in E'$, so $E' \nsubseteq E$ and $E$ is not closed.
    
    Take the set, $S := \Set{(x,y) \mid y = 0 \wedge x \in (0,1)}$, this is, the segment $(0,1)$ of the axis $x$. Naturally, is $S \subset E$.
    
    Then, observe that for any $r \in \mathbb{R}^+$ is $S \cap \big[N_r(p) \setminus \Set{p}\big] \neq \varnothing$

    Observe that is:

    $$q \in S \implies (y= 0 \wedge 0 < x < 1)$$

    $$q \in N_r(p) \setminus \Set{p} \implies 0 < d(q,p) = |(1-x,y)|< r$$

    Ultimately $(x,y)$ is in the intersection if:

    $$\begin{cases} y= 0 \\ 0 < x < 1 \\ 0 < (1 - x)^2 < r^2 \end{cases}$$

    Observe that $0 < 1-x \implies 1-x < r \iff 1 - r < x < 1$. 

    Meaning that, if $1-r< 0$ (when $r > 1$) then any $(x,0) : 0 < x < 1$ is in the intersection, if not, then any $x \in (1 - r,1) : r < 1$ is in the intersection.

    Observe that $ r>0 \iff 1 - r < 1$ and since $\mathbb{R}$ is dense and total ordered, there is always an $x$ satisfying $1 - r < x < 1$. Hence in any case the intersection is not empty and $E$ is not closed.

    <br>

    **$E$ is open**.

    Consider some $q \in E \implies \|q \| = d(q,O) < 1$. Take then $r \in \mathbb{R}^+ : r < 1 - \|q \|$ and consider the ball $N_r(q)$.

    If is $t \in N_r(q)$, then applying the tringular inequality:

    $$|t| = d(t,O) \leq d(t,q) + d(q,O) < r + |q| < (1 - |q|) + |q| = 1 \implies t \in E$$

    Since $t$ is arbitrary, $N_r(q) \subset E$, and we can state:

    $$\forall q \in E \ \exists r \in \mathbb{R}^+ :N_r(q) \subset E \iff E \text{ is an open set}$$

    <br>

    **$E$ is not perfect**

    Since is not close, it cannot be perfect either.

    <br>

    **$E$ is bounded**

    Let's see that is also bounded. Take for example $O$ and $1$, or in orther words, $N_1(O)$. Is clear that $E \subset N_1(O)$ since:

    $$\forall p(p \in E \implies |p| < 1 \implies d(p,O) < 1 \implies p \in N_1(O))$$

    <br>

- $E= \Set{z \in \mathbb{C} \mid \|z\| \leq 1}$

    **$E$ is closed**.

    Take some $q \in E'$, then $\forall r(N_r(q) \setminus \Set{q} \cap E \neq \varnothing)$. Let's suppose that $q \notin E \implies \|q\| > 1$ and we can think in some $t \in \mathbb{R}^+ : 1 + t < \|q\|$.

    Consider $p \in N_t(q) \setminus \Set{q} \cap E \implies (d(p,O) \leq 1 \wedge d(p,q) < t)$ but:

    $$1 + t < |q| = d(q,O) \leq d(q,p) + d(p,O) < t + 1 = 1 +t$$

    Hence, we reach an absurd and $q \in E$, so $E' \subset E$ and $E$ is closed.

    <br>

    **$E$ is not open**.

    Take $O$ and $p \in E : \|p\| = 1$. Let's now use $d$ to get a parametrized family of points $q$ satisfying:

    $$d(O,q) = d(O,p) + d(p,q) \iff |q| = |p| + |q - p|$$

     Thus, in this context, $\|q\| > 1 \implies q \not \in E$, but $q$ is in any neighbourhood with radius superior to $d(p,q)$. Observe also that as long as this distance is greater than $0$, $q \notin E$ and any neighbourhood of $p$ contains points out of $E$, hence $E$ is not open.

    <br>

    **$E$ is perfect**

    We do know that $E$ is closed.

    Take first $p \in E : \|p\| < 1$, we did see that this set is open, so for $p$ we can consider a neighbourhood $N_r(p) \subset E$. Then, for any $t < r$, $N_t(p) \subset N_r(E) \subset E$ and for any $l > t$, is $N_t(p) \subset N_l(p) \implies N_l(p) \setminus \Set{p} \cap E \neq \varnothing$ and $p \in E'$.

    <br>

    Consider now $p \in E : \|p\| = 1$, then we take the same argument given above and we can think in the parametric family of points $q$ satisfying:

    $$d(O,p) = d(O,q) + d(q,p) \iff |p| = |q| + |q - p|$$

    Observe again that, as long as $q \neq p$, $q \in N_t(p) \setminus \Set{p} \cap E$ where $t \in \mathbb{R}^+ : d(p,q)<t$ and we can make $d(p,q)$ as small as we want. So $p \in E'$. So $E$ is perfect.

    <br> 

    **$E$ is bounded**

    Yes by te same argument as $E$ above is bounded too.

    <br>
    
- **$\exists n \in \mathbb{N} \exists \varphi \in E^{[n]} : \varphi \text{ is a biyection } \wedge E \neq \varnothing$ ($E$ is a finite non-empty set).**

    **$E$ is NOT open**

    Consider any $N_r(p)$ for some $p \in E$.
    
    Since $E$ is finite, observe that then we can consider $d(p,q) = min\Set{d(x,y) \mid x,y \in E }$, then $N_r(p)$ for $r < d(p,q)$ is $N_r(p) \cap E = \varnothing$.

    <br>

    **$E$ is closed**

    Observe that $E$ has no limit points, $E' = \varnothing \subset E$, hence $E$ is closed.

    <br>

    **$E$ is NOT perfect**

    Since $E' \neq E$.

    <br>

    **$E$ is bounded**

    Arguien the same as in the open case, we can consider $d(p,q) = \max\Set{d(x,y) \mid x,y \in E }$, then $E \subset N_r(p)$ for some $r > d(p,q)$ and $E$ is bounded.

    <br>

- $E = \mathbb{Z}$

    **$E$ is NOT open**

    $$\forall z \in \mathbb{Z} \ (r \in (0,1) \implies N_r(z)\setminus \Set{z} \cap \mathbb{Z} = \varnothing) \implies \forall z \in \mathbb{Z} \ \nexists r : N_r(z) \subset \mathbb{Z}$$

    <br>

    **$E$ is closed but is not perfect**

    Arguin the same as above.

    <br>

    **$E$ is NOT bounded**

    Take any $z \in \mathbb{Z}$ and any $r \in \mathbb{R}^+$ and observe that $z + \lceil r \rceil \notin N_r(z)$, hence is not bounded.  

    <br>

- $E := \Set{1/n : n  \in \mathbb{Z}^+}$

    **$E$ is NOT open**

    Take $p = 1$ and $r = 1/2$, then $N_r(p)\setminus \Set{p} \cap E = \varnothing$

## 3.5. Complement of a family of sets.

Let be $\Set{E_\alpha}$ be a finite or infinite family of sets. Then, the complementary of the union is the global intersection of each complementary set:

$$X \setminus\bigcup_\alpha E_\alpha = \bigcap_\alpha (X \setminus E_\alpha)$$

Immediately:

$$p \in X \setminus\bigcup_\alpha E_\alpha \iff \neg \big[\exists \alpha (p \in E_\alpha)\big] \iff \forall \alpha (p \in X \setminus E_\alpha) \iff p \in \bigcap_\alpha X \setminus E_\alpha$$

<br>

## 3.6. Caracterizations.

### 3.6.1. Caracterization of Open sets.

A set $E$ is open if and only if its complement is closed. Formally:

$$E \text{ is open} \iff X \setminus E \text{ is closed}$$


<br>

Consider some $A$ and call $B = X \setminus A$.

- $\Rightarrow$ 

    First, $A$ is open. Consider:
    
    $$p \in B' \implies \forall r(N_r(p) \setminus \Set{p} \cap B \neq \varnothing) \implies p \notin A \implies p \in B$$
    
    Observe that $p \notin A$ otherwise the statement above wouldn't apply since $A$ is open so $p \in B$. 
    
    Thus, $B' \subset B$ and $B$ is closed.

    <br>

- $\Leftarrow$

    Now, $B$ is closed, then $B' \subset B$. Consider some $p \in A$, then $p \notin B' \subset B$ hence:

    $$\neg[\forall r(N_r(p) \setminus \Set{p} \cap B \neq \varnothing)] \ \underbrace{\implies}_{p \notin B} \ \exists r : N_r(p) \cap B = \varnothing \underbrace{\implies}_{A = X \setminus B} \exists r : N(r) \subset A$$

    And $A$ is open.

    <br>

### 3.6.2. Caracterization of Closed sets.

Observe that there is an immediate corollary; 

$$E \text{ is closed} \iff X \setminus E \text{ is open}$$

<br>

### 3.6.3. Some families caracterization.

We have the following immediate results:

- For any collection $\Set{O_a}$ of open sets, $\bigcup_a O_a$ is an open set.
- For any collection $\Set{C_a}$ of closed sets, $\bigcap_a C_a$ is an closed set.

<br>

Also,

- For any finite collection of open sets, $O_1,\ldots, O_n: n \in \mathbb{N}$, the intersection $\bigcap_{i=1} O_i$ is open.

- For any finite collection of closed sets $C_1, \ldots, C_n$, the union $\bigcup_{i=1}^n C_i$ is closed.

    <br>

## 3.7. Closure of a set.

Be $X$ a metric space and $E \subset X$. Then we define the *closure* of $E$ as the set 

$$\overline{E} = E \cup E'$$

This is, the set along with the acumulation set of $E$.

<br>

1. Note first that $\overline{E}$ is closed. 

    Consider $p \in \overline{E}'$. Then: $\forall r(N_r(p) \setminus \Set{p} \cap \overline{E} \neq \varnothing)$, which means that for each $r \in \mathbb{R}^+$:
    
    
    $$(N_r(p) \setminus \Set{p} \cap E \neq \varnothing) \vee (N_r(p) \setminus \Set{p} \cap E' \neq \varnothing)$$
    
    But $N_r(p) \setminus \Set{p} \cap E' \neq \varnothing$, means that $\exists q \in N_r(p) \setminus \Set{p} : \forall t(N_t(q) \setminus \Set{q} \cap E \neq \varnothing)$, hence, we can take some $t : N_t(q) \subset N_r(p)$ and assert $N_r(p) \cap E \neq \varnothing$.
    
    - If $p \in E \implies p \in \overline{E}$.
    - If $p \notin E$ then $N_r(p) \setminus \Set{p} \cap E \neq \varnothing$ and this applies from above for each $r \in \mathbb{R}^+$ and $p \in E' \implies p \in \overline{E}$.

    In any case, $\overline{E}' \subset \overline{E}$, and $\overline{E}$ is closed.

    <br>

2. The smallest closed set that contains $E$. To prove it, let's demonstrate that any closed set containing $E$ contains $\overline{E}$ as well. Formally:

    $$\forall  A \subset X : A' \subset A \quad [E \subset A \implies \overline{E} \subset A]$$

    First, take some $A \subset X : (E \subset A \wedge A' \subset A)$, then consider some $e \in E'$ (the case $e \in E \subset A$ is trivial), then observe that, since $E \subset A$ is:

    $$\forall r(N_r(e) \setminus \Set{e} \cap E \neq \varnothing) \implies \forall r(N_r(e) \setminus \Set{e} \cap A \neq \varnothing)  \implies e \in A ' \subset A$$

    Hence, $E \cup E' = \overline{E} \subset A$.

    <br>


3.  $E = \overline{E} \iff E \text{ is closed }$. Is immediate.

    <br>

## 3.8. Caracterization of the supreme as the maximum of the reals.

Let be $E \subset R : E \neq \varnothing$ and $E$ is bounded above. Then we can consider $y = supE$ and $y \in \overline{E}$.

This result is almost immediate, since $y$ is the least upperbound of $E$, $y \notin E \implies y \in E' \subset \overline{E}$.



And we have $E \text { is closed } \implies y \in E$.

<br>

## 3.9. Relative open subsets.

### 3.9.1. Definition.

Let be $(X,d)$ a metric space, then be $Y \subset X$, $(Y,d)$ is as well a metric space. In this context, we define

$$E \subseteq Y \subseteq X \text{ is open relative to } Y \iff \forall p(p \in E \implies \exists r [N_r(p) \cap Y \subset E])$$

Naturally, in $(X,d)$, all open sets are relative open to $X$, but observe that set $E \subset Y \subset X$ can be open relative to $Y$ without necesarily being open in $X$. 

Let's think for example in $\mathbb{R}^2$ with the distance $d(x,y) = \mid x - y \mid$, then let's consider the subset of $X $ as, $N = \Set{x \mid \|x \| < r}$, now for any $x \in \mathbb{R}^2$, we define: $\lceil \|x\| \rceil = \min\Set{z \in \mathbb{Z}:  z\geq\|x\|}$ and consider $Y = \Set{x \mid \lceil \|x\| \rceil \in 2 \mathbb{Z}}$. Observe that $E = N \cap Y$ is open relative to $Y$ but is not open in $\mathbb{R}^2$.

<br>




### 3.9.2. Caracterization.

**Suppose $Y \subset X$. A subset $E \subseteq Y$ is *open relative* to $Y$ if and only if $E = Y \cap G$ where $G$ is an open set of $X$.**

$$E \subseteq Y \subseteq X \text{ is open relative to } Y \iff \exists \text{ an open set } G \subseteq X  : E = Y \cap G$$

One hand, if there is $E$ open relative to $Y$, then, for each $p \in E$ exists a neighbourhood $N_p \cap Y \subset E$, then we call $G = \bigcup_{p \in E} N_p$ and $E = Y \cap G$.

<br>

On the other hando, if $E = Y \cap G$ for some open set $G$, then, for each $p \in E$ there is some neighbourhood $N_p \subset G \implies (N_p \cap Y) \subset (G \cap Y = E)$ and $E$ is open relative to $Y$.

<br>

# 4. Compact sets.

## 4.1. Open Covers.

Take some subset of a metric space $E \subseteq X$. Then we say that a collection of open sets $\Set{G_\alpha}$ is an open cover of $E$ iff $\displaystyle E \subseteq \bigcup_{\alpha} G_\alpha$.

<br>

## 4.2. Compact Formal Definition.

Then, we say that a subset of a metric space $E \subseteq X$ is compact if every open cover of $K$ contains an open subcover.

$$E \subseteq X \text{ is compact } \iff \exists n \in \mathbb{N} : \Set{G_i}_{i \in [n]} \text{ is an open cover of } E$$

<br>

## 4.3. Compactness intuition and historic motivation.

In brief terms, compactness is the topological abstraction of finitness, understanded it as the capability of extrapolate local information to global information.

Note that any finite set is compact, and that a finite set has properties that some infinite set loss, like for example, the reachness of the maximum in the set. Compactness property isolate those infinite sets which mantain thoses properties.

<br>

### 4.3.1. Topology prolegomena.

Until now, we have only seen that metric spaces are those spaces where a mathematically precise notion of *distance* is defined, meaning that metric spaces provide a quantitative notion of proximity, which allows to reference local structures in quantitative terms.

Topology spaces are a more general scenario which try to clear what means to be in the surroundings of a point, this is; admits a qualitative reference for local structures. If metric spaces references it through the distance (this is, translating the property as some real number value), then topology spaces references it in qualitative terms through the notion of open sets.

More precisely, a topologic space $(X,\mathcal{T})$ is formed by a non-empty set $X$ and a topology $\mathcal{T}$ which is a description of those subsets of $X$ for which is valid to consider the surroundings of any point, open sets. 

<br>

### 4.3.2. Open sets and Neigbourhoods.

Let be $(X, \mathcal{T})$ a topologic space (remember that $\mathcal{T}$ is a set of open sets defined by extension), then, we stablish that:

$$N \subseteq X \text{ is a neighbourhood of } x \iff \exists U \in \mathcal{T} : x \in U \subseteq N$$

This is a set is a neigbourhood of a point if contains some open set containing each point. We refer to the family of all neigbourhoods of $x$ as $\mathcal{N}(x) := \Set{ N \subseteq X \mid \exists U \in \mathcal{T} : x \in U \subseteq N}$. 

Hence, observe that *open sets* are those sets that are neighbourhoods for all his points.

$$U \in \mathcal{T} \iff \forall x( x \in U \implies U \in \mathcal{N}(x))$$

In this sense, they are "ample for everything inside it".

<br>

Then, we call a system of neighbourhoods over $X$ to an asignation $x \mapsto \mathcal{N}(x) \neq  \varnothing$ that satisfies:

- $N1 \ -$ **Every neighbourhood of $x$ owns $x$**, formally: 

    $$\forall N(N \in \mathcal{N}(x) \implies x \in N)$$

- $N2 \ -$ **$\mathcal{N}(x)$ owns any set contaning a neigbourhood of $x$**; or in more simpler terms, any set containing a neigbourhood is also a neigbourhood it self. 

    $$\forall N \in \mathcal{N}(x) \ \forall M \big[N \subseteq M \implies M \in \mathcal{N}(x)\big]$$

- $N3 \ -$ **$\mathcal{N}(x)$ owns any finite intersection of neigbourhoods of $x$**

    $$\forall N,M \big[N,M \in \mathcal{N}(x)  \implies N\cap M \in \mathcal{N}(x)\big]$$

    Observe that by associativity, $N3$ works for any finite intersection of neighbourhoods of $x$. 

- $N4 \ - $ **Any neighbourhood $N$ of a point $x$ contains some other neighbourhood $M$ of $x$ for which $N$ is a neighbourhood of any point of $M$**:

    $$\forall N \in \mathcal{N}(x) \exists M \in \mathcal{N}(x) \big[M \subseteq N \wedge \forall y( y \in M \implies  N \in \mathcal{N}(y))\big]$$

    <br>

Observe that $N4$ es the only axiom that speaks about two distinct points of $X$, basically saying that for any neighbourhood $N$ of a $x$ we can find a narrower neighbourhood $M$ of $x$ for whose elements $N$ is a neighbourhood as well. Meaning that a neighborhood allows you to speak of a local community of points, in the sense that you cannot single out a privileged point upon which the structure is centered; they all lay claim to the neighborhood as their own.

This axiom system over $N(x)$ codifies a proximity notion over $x$. Observe also that:

$$\forall N,N' \in \mathcal{N}(x) \big[N' \subset N  \iff N' \text{ is more restrictive than } N\big]$$

With this in mind observe that

- In one hand, $N1 - N3$ states what a local structure or enviroment of a point $x$ is by defining how it behaves; it contains $x$, is stable with the expansion and finite intersection retains a surrounding of the point. 

- On the other hand, $N4$ states some notion of proximity by asserting that any neighbourhood $N \in \mathcal{N}(x)$ is simultaneously a neighbourhood for any point $y$ in a narrower $M \in \mathcal{N}(x)$. 

    Then, $N$ is a common local structure of any point of $M$ (including $x$). Any $y \in M$ is in the neighbourhood of $x$ as much as $x$ is in $y$'s and in that sense, $x$ and $y$ are "suficiently close" relative to $N$. In summary, these points share a set that all call as "his own neighbourhood", in this sense all are part of the same descentrilized local structure.

    Hence any neighbourhood of $x$ is a common local structure for some "sufficently close" amount of points among which $x$ is incluyded. Which gives sense to the term "surroundings" of $x$.

    <br>


This means that, in contrast with metric spaces, topologic proximity is comparative between a point an a set; topology answer when a point belongs or not to a set with the subsequent conclusion that a point could belong or not to the neighbourhood of other point, and $N4$ ensures that both are in the surroundings of the other.

This allows to talk about *local properties*, this is, properties that points satisfies regards his surrondings.

<br>

### 4.3.4. Local information. Local property. Local to Global properties.

Let's consider a topologic space, $(X,\mathcal{T})$ and an structure over it, for example a function. We refer as *local information on $x$* to what remains of the structure when you restrict it over the surroundings of $x$.

This is where the vocabulary developed with the open sets takes place which allows to refer to the local structure in which a point is embebed and look it closely to see how some property behaves. Formally, if $M_x$ is a property satisfied by a point $x \in X$, then,  if:

$$ M_x \text{ is a local property of } x \iff \exists U \in  \mathcal{N}(x) : \forall y \big( y \in U \implies M_y\big)$$

We could state that $U_x$ is the neighbourhood in which the local property $M_x$ is true, then the problem begins with the fact that you cannot extrapolate a local property satisfied by every point as a global property:

$$\exists M_x : \forall x \exists U_x \quad \cancel{\Longrightarrow}  \quad \exists  M_x : \exists U_x \forall x $$

What get's broken here is that the arbitrary intersection doesn't garantee neighborhood preservation, meaning that ultimately, finitness must be introduced in some way.

<br>

### Compactness arisness and local properties: Finitness and Discretness.



<br>

# Exercises.

## 1. The empty set is a subset of every set.



We can think that, be $X$ a superset and $A \subseteq X$, then by the properties of the union is: 

$$\varnothing \subset A \cup \varnothing = A$$

<br>

## 2. Algebraic complex numbers.

We have that:

$$z \in \mathbb{C} \text{ is said to be algebraic} \iff \exists (a_1,\ldots,a_n) \neq 0 \in \mathbb{Z}^n : \sum_{i = 1}^n z^{n+1 -i}a_i = 0$$

Prove that the set of all algebraic numbers is countable. Hint: For every positive
integer $N$ there are only finitely many equations with:

$$n + |a_0| + |a_1| + \cdots + |a_n| = N$$

<br>


Llevo un rato dándole vueltas y estoy pensando que para cada complejo algebraico, la condicion se desdobla en dos ecuaciones de la forma:

$$n + |a_0| + |a_1| + \cdots + |a_n| = 0$$


Y para $N = 0$, solo hay un número finito de ecuaciones y por tanto debería de haber solo un número finito de tuplas que identificasen un número finito de complejos. Pero claro, cada conjunto finito de tuplas es por número de elementos de la tupla, es decir, para n = 2 una familia finita, para n =3 una familia finita, y así. Por lo que, al final, el numero total de algebraicos es una union contable de conjuntos finitos, que se traduce en un conjunto contable. 

<br>

## 3. Prove that there exist real numbers which are not algebraic.

If don't then, the real subset of $\mathbb{C}$ would be an infinity subset of a countable set, and by $2.3.2$ then it would be countable, and we do know that $\mathbb{R}$ is uncountable so that's not possible. So there must be not-algebraic numbers in $\mathbb{R}$.

<br>

## 4. Uncountableness of irrational numbers.

Is the set of all irrational real numbers countable?

No, since $\mathbb{R}$ is the union of the rational set and irrational set and the irrational set is countable, if the irrational set was countable as well, then $\mathbb{R}$ would be a finite union of countable sets, and by $2.4.4$, the at most countable union of at moust countable sets is at most countable, but $\mathbb{R}$ is uncountable.

<br>

## 5. Construct a bounded set of real numbers with exactly three limit points.

