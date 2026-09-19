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

## 2.1. Sequence's reminder.

We remind that we understand as a sequence to be a function $f$ whose domain is the positive integerse set:

$$f : \mathbb{Z}^+ \to A$$

Often refered with the symbol $\Set{x_n}$, where $x_n = f(n)$ is the $n$-st term of the sequence.

<br>

We recall that the *range* of a sequence $\Set{p_n} \subset X$ is the set of all his terms $p_n$, and it can be infinite or a finite set, it depends of the definition of the sequence. Think trivially in $f(n) = n$ and $f(n) = 0$.

<br>

## 2.2. Convergence.

### 2.2.1. Definition.

Let be a sequence $\Set{p_n}$ defined over the terms of a metric space $(X,d)$, or simply $\Set{p_n} \subset X$. Then, $\Set{p_n}$ is said to *converge in $X$* if there exists a point $p \in X$ such for any positive real $\mathcal{E}$ there is a positive integer $N$ such $n > N$ implies that the distance of $p_n$ to $p$ is smaller than $\mathcal{E}$.

Formally:

$$\lim_{n \to \infty} p_n = p \iff \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies d(p_n,p) < \mathcal{E})$$

And we say that $p$ is the limit of $\Set{p_n}$ in $X$, we denote it as $\Set{p_n} \to_{X} p$.

<br>

If $\Set{p_n}$ don't have a limit point in $X$ then it says to *diverge in $X$*.

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



<br>

## 3.1. Definition.



## 3.2. Compactness and Subsequences.