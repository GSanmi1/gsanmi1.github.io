---
layout: post
title: "Numerical Sequences and Series"
subtitle: "Convergence, Cauchy-Sequences and Completness"
date: 2026-09-15 09:00:00 +0000
categories: ['Analisis Rudin']
tags: ['Maths']
author: German Sanmi
subject: real-analysis
lang: en
---

# 0. Index.

# 1. Introduction.

# 2. Convergent Sequences.

## 2.1. Sequence's reminder. Definition and Intuition.

We remind that we understand as a sequence to be a function $f$ whose domain is the positive integerse set:

$$f : \mathbb{Z}^+ \to A$$

Often refered with the symbol $\Set{x_n}$, where $x_n = f(n)$ is the $n$-st term of the sequence.


We recall that the *range* of a sequence $\Set{p_n} \subset X$ is the set of all his terms $p_n$, and it can be infinite or a finite set, it depends of the definition of the sequence. Think trivially in $f(n) = n$ and $f(n) = 0$.

<br>

The formal definition of a sequence as "a function whose domain is $\mathbb{Z}^+$" is formally correct but conceptually quite poor. In the context of analysis, a sequence is much more than a way of talking about countability.

Intuitively, a sequence is the mathematical abstraction of an object that changes through ordered steps ($\mathbb{Z}^+$ is a good ordered set). In the chapter before, we used it to count, in this chapter we will care about it from a certain point on (through the infinite). Its importance lies in the fact that it is the mechanism by which analysis reduces the infinitely close to finite stages, is the introduction to the limit as a tool.

<br>

## 2.2. Convergence.

### 2.2.1. Definition.

Let be a sequence $\Set{p_n}$ defined over the terms of a metric space $(X,d)$, or simply $\Set{p_n} \subset X$. Then, $\Set{p_n}$ is said to *converge in $X$* if there exists a point $p \in X$ such for any positive real $\mathcal{E}$ there is a positive integer $N$ such $n > N$ implies that the distance of $p_n$ to $p$ is smaller than $\mathcal{E}$.

Formally:

$$\lim_{n \to \infty} p_n = p \iff \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies d(p_n,p) < \mathcal{E})$$

And we say that $p$ is the limit of $\Set{p_n}$ in $X$, we denote it as $\Set{p_n} \to_{X} p$. If $\Set{p_n}$ don't have a limit point in $X$ then it says to *diverge in $X$*.

<br>

Hence, we would say that a sequence if get

<br>

### 2.2.2. Some aclarations of the definition.

Is worth to see that the convergence for a sequence is specific of the metric space in which we are evaluatiung the existance of the limit point.

As a quick example, $\Set{1/n}$ converges to $0$ in $\mathbb{R}$ (we demonstrated this in the Topology post), but it do not converges in $\mathbb{R}^+$.

<br>

### 2.2.3. Bounded sequences.

A sequence is said to be bounded if his range set is bounded in $X$ which is not the same to be infinite. For example, $\Set{1/n}$ tends to $0$, is bounded but has infinite range.

<br>

### 2.2.4. Important properties of convergence.

Let $\Set{p_n}$ be a sequence of a metric space $X$. Then:

- **$\Set{p_n}$ converges to $p \in X$ in $X$ iff every neighbourhood of $p$ contains all but finitely many $n$.** 

    This is that any set of terms of the sequence $\Set{p_n}$ out of some neighbourhood of $p$ is a finite set (the empty set is finite, since the number of elements of $card(\varnothing) = 0$).

    Let's think in some $N_r(p)$, then, since $\lim_n p_n = p$, then for $r$ there is some $N_r \in \mathbb{Z}^+$ such $d(p_n,p) < \mathcal{E} \quad \forall n \geq N_r$. The terms of the sequence $\Set{p_n}$ until $n$ is finite, this is the number of terms that are out of $N_r(p)$, the rest are in the neigbourhood.

    Observe that, if the range of $\Set{p_n}$ is infinite, then $p$ is a limit point. We do need that the range is infinite since the definition of the convergence speaks about index, the index are always infinite since it has the cardinality of $\mathbb{N}$, but all the terms of the sequence can be finite.

    <br>

- **When exists, the convergence point of $\Set{p_n}$ is unique**

    Formally, if $p,q \in X$ are such $\lim_n p_n = p$ and $\lim_n p_n = q$, then $p = q$.

    Observe that if not, we could take $r < d(p,q)/2$ and consider the neigbourhoods $N_r(p), N_r(q) : N_r(p) \cap N_r(p) = \varnothing$. 
    
    By the point above, this two neighbourhoods contains all the terms of the sequence but a finitely many of them in contradiction with the premise about they are disjoint sets of $X$.

    <br>

- **Any convergent sequence is bounded in $X$**

    Take $\lim_n p_n = p$ and consider $r = \max \Set{d(p_i,p) \mid i \in \mathbb{Z}^+}$. Then, in $N_r(p)$, necesarily, any term of the sequence is in the neighbourhood, so the range of the sequence is bounded, hence the sequence it self is bounded.

    <br>

- **Take $E \subset X$ and $p \in E'$, then $\exists \Set{p_n} \subset E : \lim_n p_n = p$**

    Observe that, since $p \in E'$, then $\forall r (N_r(p) \setminus \Set{p} \cap E \neq \varnothing)$. 
    
    Now, take the collection of neighbourhoods $N_{\frac{1}{n}}(p) : n \in \mathbb{Z}^+$. For each $n$, there are in $N_{\frac{1}{n}}(p)$ points from $E$ distinct from $p$. Let's take one of those points for each $n$ and group it in $S$. 

    Then, is obvious that this set is the range of the sequence $\Set{p_n}$ that converges to $p$ by construction.

    <br>

### 2.2.5. Operations with convergent points of sequences.

Consider $\Set{s_n}, \Set{t_n} \subset \mathbb{R}^2 : \lim_n s_n = s \wedge \lim_n t_n = t$. Then:

- $\lim_n (s_n + t_n) = s + t$
- $\lim_n \alpha s_n = \alpha s$
- $\lim_n s_n t_n = st$
- $\nexists n : s_n = 0 \implies lim_n (s_n)^{-1} = s^{-1}$


Observe that we are saying that the step to the limit of a convergent sequence in $\mathbb{R}^2$ respects the operations of $\mathbb{R}^2$ as a field, or in other terms, we can operate between sequences as elements of $\mathbb{R}^2$ and the limit of the resulting operation would be as if we operate in the same way with the limits it self. 

Is easy to demonstrate to each case that the proposed limit respects the convergence definition.

<br>

### 2.2.6. Convergent sequences in $\mathbb{R}^k$.

#### 2.2.6.1 Definition.

Let be $\mathbf{x}_n \in \mathbb{R}^k : \mathbf{x}_n = (x_{1n}, \ldots, x_{kn})$. Consider $\Set{\mathbf{x}_n} \subset \mathbb{R}^k$ and $\mathbf{a} = (a_1, \ldots, a_k)$, then we say that 

$$\Set{\mathbf{x}_n} \to_{\mathbb{R}^k} \mathbf{a} \iff \Set{x_{in}} \to_{\mathbb{R}} a_i \quad \forall i \in [k]$$

This is basically a definition that extendes the sequences to several dimensions.

<br>

#### 2.2.6.2. Properties.

Consider $\Set{\mathbf{x}_n}$, $\Set{\mathbf{y}_n} \subset \mathbb{R}^k : \Set{\mathbf{x}_n} \to_{\mathbb{R}^k} \mathbf{a}  \wedge \Set{\mathbf{y}_n} \to_{\mathbb{R}^k} \mathbf{b}$. Then:

- $\lim_n (\mathbf{x}_n + \mathbf{y}_n) = \mathbf{a} + \mathbf{b}$
- $\lim_n \alpha \mathbf{x}_n = \alpha \mathbf{a}$
- $\lim_n \mathbf{x}_n \cdot \mathbf{y}_n = \mathbf{a} \cdot \mathbf{b}$

    <br>

Is easy to demonstrate to each case that the proposed limit respects the convergence definition.

<br>

# 3. Subsequences.

## 3.1. Definition.

Given a sequence $\Set{p_n}$, consider a sequence $\Set{n_k} \subset \mathbb{Z}^+: n_i \leq n_{i+1} \quad \forall i \in \mathbb{Z}^+$, then $\Set{p_{n_k}} \subset \Set{p_n}$ is called a subsequence of $\Set{p_n}$

<br>

## 3.2. Convergence in terms of subsequences.

Observe that is clear that a sequence converges to $p$ in $X iff any subsequence converges to $p$ in $X$ as well.

$$\Set{p_n} \to_X p \iff \forall \Set{p_{n_k}} \subset \Set{p_n} \Big(\Set{p_{n_k}} \to_X p\Big)$$

<br>

## 3.2. Compactness and Subsequences.

### 3.2.1. Sequences in compact metric spaces.

**Let's consider some $\Set{p_n} \subset X$ being $X$ a compact metric space. Then, there is at least one subsequence $\Set{p_{n_k}} \subset \Set{p_n}$ converging in $X$.**

<br>

Let's consider the range of $\Set{p_n}$, let's call it $E$. In the case that $E$ were finite, trivially, there must be at least one point that appears infinitely in the sequence since the index set is countable, and we can take some subsequence $\Set{p_{n_k}}$ whose range is only one point. This subsequence trivially converges to that very point in $X$.

If $E$ is infinite, then, for being $E$ an infinite subset of a compact set, by [$4.4.5$](https://gsanmi1.github.io/posts/2026/06/17/BasicTopology/), there is a limit point $p \in E'$.


Let's depart from the fact that this point verifies that any neigbourhood contains infinite terms of the sequence, and the radius $r$ can have an arbitrary positive value. This way, we could select the terms of the subsequence by decreasing $r$ of $N_r(p)$ narrowing the distance to $p$ of consecutive terms of the subsequence. By selecting:

$$\Set{p_{n_k}} \subset \Set{p_n} : p_{n_i} \in N_{i^{-1}}(p) : n_i < n_{i+1}$$

Observe that:

- We force the index to increase, $n_1< n_2 < n_3 \ldots$, trivially we can do that because there are infinite terms in any neigbourhood and upwards, but there are only finite terms backwards any term of the subsequence.

- The distance of the terms tends below any real positive: 

    $$p_{n_i} \in N_{i^{-1}} \implies d(p_{n_i},p) < \frac{1}{i}$$

    Is well known that $\Set{1/n} \to_{\mathbb{R}} 0$, hence $\Set{d(p_{n_i},p)} \to_{\mathbb{R}} 0$.

    Observe that, in first instance we could fall in the wrong misconception that monotone decrease of $d(p_{n_k},p)$ is what the subsequence does to approximates to $p$. But this is neither necessary nor sufficient for convergence, what is needed is that the radii be prescribed in advance, so that the distances fall below every $\mathcal{E}$.

    Observe that if $\Set{p_n}$ would have several limit points, any sequence or subqecuence would gradually decrease to any of them without garantee convergence. What is needed is distance tending to $0$.

    <br>

In other terms: $\Set{p_{n_k}} \subset \Set{p_n}$ moves on through $\Set{p_n}$ towards $p$. 

Then, take some $\mathcal{E} > 0$, then, by the arquimedean property, there is some $i \in \mathbb{Z}^+ : \mathcal{E} \geq 1/i > 0$ and $p_{n_i} \in N_\mathcal{E}(p)$. 

Let's call $N = n_i$ and observe that any term of the subsequence further than $p_N$ verifies to be in $N_\mathcal{E}(p)$:

$$N = n_i < n_k  \underbrace{\implies}_{\text{increasing index}} i < k \implies d(p_{n_k},p) < k^{-1} < i^{-1} \leq \mathcal{E}$$

Since $\mathcal{E}$ is arbitrary, we can state that:

$$\forall \mathcal{E} > 0 \ \exists N \in \mathbb{Z}^+ : (N \leq {n_k} \implies d(p_{n_k},p) < \mathcal{E}) \iff \Set{p_{n_k}} \to_X p$$

In any case, there is some subsequence converging in some point of $X$.

<br>

### 3.2.2. Bounded sequences in $\mathbb{R}^k$.

**Every bounded sequence in $\mathbb{R}^k$ has a convergent subsequence is $\mathbb{R}^k$**

This comes from the fact that every bounded subset of $\mathbb{R}^k$ lies in some $k$-cell which is compact and from above, any sequence in a compact set has a convergent subsequence.

<br>

# 4. Cauchy Sequences.

## 4.1. Conceptual Introduction.

Until now, we've just seen that a sequence converges when the distance between the terms of the sequence and some point gradually becomes closer and closer to $0$.

In contrast, a Cauchy Sequence is a sequence in whose terms gradually get closer betweem them without referencing a convergent point, it abstracts the behaviour of a convergent sequence in a space in which the convergence point does not necesarily exists.

When for each cauchy sequence in a set exists a convergence point in that very set, then the set is called to be *complete*. Later we will see that the completness definition given in terms of the supremum and this one are equivalent statements.

<br>

## 4.2. Formal Definition.

Let be $(X,d)$ a metric space, then a sequence $\Set{p_n} \subset X$ is said to be a Cauchy Sequence if:

$$\forall \mathcal{E} > 0 \ \exists N \in \mathbb{N} : (N \leq n,m \implies d(p_n,p_m)< \mathcal{E})$$

Meaning that, at some point, the terms of the sequence are arbitrarily near between them.

<br>

## 4.3. Geometrical Definition.

### 4.3.1. Diameter of a set.

Let be $E \neq \varnothing \subset X$, then consider the $D_E \subset \mathbb{R}$ of all the distances between the points of $E$:

$$D_E = \Set{d(p,q) \mid p,q \in E}$$

Then, we call as *diameter* of $E$ to the supremum of $D_E$:

$$diamE = sup D_E$$

Observe that this definition doesn't stablish to the diameter to be a distance between some points, that would be the maximum which is not garantee to exists.

<br>

### 4.3.2. Tail of a sequence.

Consider a sequence $\Set{p_n} \subset X$ and the $i$-th tail $T_i = \Set{p_n : n \geq i}$ of the sequence. 

<br>

### 4.3.3. Geometric definition.

A sequence $\Set{p_n} \subset X$ is said to be a Cauchy Sequence if, the sequence of the diameter of the tails of $\Set{p_n}$, converges to $0$;

$$\Set{diamT_n} \to_\mathbb{R} 0$$

Let's recall the definition of convergence

$$\lim_{n \to \infty} diamT_n = 0 \iff \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E})$$

<br>

First, let's recall that: $diamT_n = sup D_{T_n}$, and $D_{T_n} = \Set{d(p,q) \mid p,q \in T_n} = \Set{d(p_s,p_t) \mid s,t \geq n}$, hence, $diamT_n$ is the less upperbound of a set of distances and:

$$n \leq s,t \implies d(p_s,p_t) \leq diamT_n = |diamT_n|$$

Hence

$$\forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E}) \implies$$

$$\implies \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \leq s,t \implies d(p_s,p_t) < diamT_n < \mathcal{E}) \implies$$

$$\implies \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq s,t \implies d(p_s,p_t) < \mathcal{E})$$

Observe that, if we depart from the first definition, we get:

$$m > n\implies T_m \subset T_n \implies diamT_m < diamT_n$$

Because the definition impose the far you go the smaller is the distance between the elements:

$$s>m>n \implies d(p_s,p_m)< d(p_m,p_n) \implies sup D_{T_s} < sup D_{T_m} < sup D_{T_n}$$

Which allow us to say that:

$$\forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E})$$

Both definitions are equivalent for the cauchy sequences.