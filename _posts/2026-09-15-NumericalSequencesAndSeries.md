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

Consider a sequence $\Set{p_n} \subset X$ and the $i$-th tail $T_i = \Set{p_n : n \geq i}$ of the sequence. The tail is what remains of the sequence at some index $n$.

<br>

### 4.3.3. Geometric definition.

A sequence $\Set{p_n} \subset X$ is said to be a Cauchy Sequence if, the sequence of the diameter of the tails of $\Set{p_n}$, converges to $0$;

$$\Set{diamT_n} \to_\mathbb{R} 0$$

Let's recall the definition of convergence:

$$\lim_{n \to \infty} diamT_n = 0 \iff \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E})$$

<br>

First, let's recall that: $diamT_n = sup D_{T_n}$, and $D_{T_n} = \Set{d(p,q) \mid p,q \in T_n} = \Set{d(p_s,p_t) \mid s,t \geq n}$, hence, $diamT_n$ is the less upperbound of a set of distances and:

$$n \leq s,t \implies d(p_s,p_t) \leq diamT_n = |diamT_n|$$

Hence

$$\forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E}) \implies$$

$$\implies \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \leq s,t \implies d(p_s,p_t) \leq diamT_n < \mathcal{E}) \implies$$

$$\implies \forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq s,t \implies d(p_s,p_t) < \mathcal{E})$$

Observe that, if we depart from the first definition, we get:

$$m > n\implies T_m \subset T_n \implies diamT_m \leq diamT_n$$

Because the definition impose the far you go the smaller is the distance between the elements:

$$s>m>n \implies d(p_s,p_m)< d(p_m,p_n) \implies sup D_{T_s} \leq sup D_{T_m} \leq sup D_{T_n}$$

Which allow us to say that:

$$\forall \mathcal{E} \in \mathbb{R}^+ \exists N \in \mathbb{Z}^+ : (N \leq n \implies |diamT_n| < \mathcal{E})$$

Both definitions are equivalent for the cauchy sequences.

<br>

### 4.3.4. Properties of the diameter.

- Let be a subset of a metric space: $E \subset X$, then:

    $$diam\overline{E} = diamE$$

    If we take $D_E = \Set{d(p,q) \mid p,q \in E}$ and $D_{\overline{E}} = \Set{d(p,q) \mid p,q \in \overline{E}}$. Let's suppose that, $diam\overline{E} < diamE$, in that case it would be $supD_{\overline{E}} < supD_E \implies \exists a \in \mathbb{R} : supD_{\overline{E}} < a < supD_E \implies a = d(p,q) : p,q \in E\setminus \overline{E}$ which is impossible since $E \subseteq \overline{E}$.

    Hence is $diam\overline{E} \geq diamE$, but if you consider $p,q \in \overline{E}$, then, if both are limit points, there are $p',q' \in E : d(p,p') <\mathcal{E} \wedge d(q,q')< \mathcal{E}$, (if not trivially $p' = p \wedge q' = q$ and we get the same), therefore:

    $$d(p,q) \leq d(p,p') + d(p',q') + d(q',q) < 2\mathcal{E} + d(p',q') \leq 2\mathcal{E} + diamE$$

    Since $\mathcal{E},p,q$ are arbitrary, then $diamE$ is upperbound of $D_{\overline{E}}$ and $diamE = diam\overline{E}$.

    <br>

- If $\Set{K_n}: K_{n+1} \subset K_n \wedge \Set{diamK_n} \to_{X} 0$, then $\cap_1^\infty K_n$ contains exactly one point.

    We remember that in $4.4.4$ of the BasicTopology post, since $K_{n+1} \subset K_n$ any finite intersection of the collection of compact sets is not empty, hence the arbitrary intersection is not empty either.

    If $\cap_1^\infty K_n$ has two (or more) distinct elements, by the metric spaces properties $p \neq q \implies d(p,q) \neq 0$. Also, this two terms would be in any $K_n$; $p,q \in \cap_1^\infty K_n \implies p,q \in K_n \quad \forall n \in \mathbb{Z}^+ $ hence take $0 < \mathcal{E} < d(p,q)$ and observe that, by the said above $diamK_n \geq d(p,q) > \mathcal{E} \quad \forall n \in \mathbb{Z}^+$, and there cannot be some $diamK_n : diamK_n < \mathcal{E}$ so the sequence could not converge to $0$. 

    Hence $\cap_1^\infty K_n$ is not empty and it doesn't have two distinct elements or more.

    <br>

## 4.4. Important properties of Cauchy Sequences.

### 4.4.1. Convergent Sequences are Cauchy Sequences.

Let be $\Set{p_n} \to_X p$, then $\forall \mathcal{E}>0 \exists N \in \mathbb{Z}^+ (N \leq n \implies d(p_n,p)<\mathcal{E})$. Then, take some $\mathcal{E}' = \mathcal{E}/2$, for $\mathcal{E}'$ there is some $N$ as the definition says, take $n,m \geq N$ and observe that, by the triangle inequality:

$$d(p_n,p_m) \leq d(p_n,p) + d(p,p_m) < 2\mathcal{E}' = \mathcal{E}$$

<br>

And $\Set{p_n}$ is a Cauchy Sequence.

<br>

### 4.4.2. In compact metric spaces, any Cauchy Sequence is a Convergence Sequence.

Take some compact metric space $X$ and consider some cauchy sequence $\Set{p_n}$. Then, consider $E = range \Set{p_n}$, if $E$ is finite, $\Set{p_n}$ must converge, otherwise, if the sequence iterates between finite values infinitely it would not be a Cauchy Sequence (just take $\mathcal{E} < \min \Set{d(p,q) \neq 0 \mid p,q \in E}$).

If $E$ is infinite, then, since $X$ is a compact space $E' \neq \varnothing$. Take some $p \in E'$, observe that it contains infinite terms of the sequence. Consider $N_{\mathcal{E}/2}(p)$ and since $\Set{p_n}$ is Cauchy's $\Set{diamT_n} \to_\mathbb{R} 0$ and we can consider some $T_N : diamT_N < \mathcal{E}/2$.

Observe that in one hand, $T_N$ contains all but finite many terms of $\Set{p_n}$ and in the other $N_{\mathcal{E}/2}(p)$ contains infinite terms of $\Set{p_n}$ so, let be $p_t \in N_{\mathcal{E}/2}(p) \cap T_N$, then $d(p_n,p) \leq d(p_n,p_t) + d(p_t,p) < \mathcal{E} \quad \forall n \geq N$, since $\mathcal{E}$ is arbitrary we can state that $\Set{p_n} \to_X p$.

<br>

### 4.4.3. In $\mathbb{R}^k$ every Cauchy Sequence converges.

Let's observe that, if we presume that a Cauchy Sequence is bounded in $\mathbb{R}^k$, then it can be included a compact space (take the clousure of the bounded set) and by the $4.4.2$ it would converge in $\mathbb{R}^k$

<br>

Let be $\Set{p_n}$ a Cauchy Sequence in a metric space. Take some $\mathcal{E}>0$, exists some $N \in \mathbb{Z}^+ : (d(p_n,p_m) < \mathcal{E} \quad \forall n,m \geq N)$. Is clear that $T_N \subset N_\mathcal{E}(p_N)$ and $T_N$ contains all the terms of the sequence but a finite many of them. 

Hence, we can consider $\mathcal{E}' = \max\Set{d(p_t,p_N) \mid t< N}$, then $T_1 \subset N_{\max\Set{\mathcal{E},\mathcal{E}'}+1}(p_N)$ and $\Set{p_n}$ is bounded.

The intuitive idea behind this reasoning is that as we stated above, Cauchy Sequence term's groups around something, groups around himself, and this means that the sequence can be encapsulated at some point (some $N$ for some $\mathcal{E} > 0$ as the Cauchy condition's state) and this capsule can be expanded if is needed.

<br>

Since $X$ as a metric space is generic, this also applies to $\mathbb{R}^k$ and then, following the reasoining above, every Cauchy Sequence converges in $\mathbb{R}^k$.

<br>

## 4.5. Metric-completness.

A metric space in which every Cauchy sequence converges is said to be *complete*.


- Thus $4.4.3$ says that all compact metric spaces and all Euclidean spaces $\mathbb{R}^k$ are complete. 

- It also implies also that every closed subset $E$ of a complete metric space $X$ is complete. (Every Cauchy sequence in $E$ is a Cauchy sequence in $X$, hence it converges to some $p \in X$, and actually $p \in E$ since $E$ is closed.) 


An example of a metric space which is not complete is the space of all rational numbers $\mathbb{Q}$. 

<br>

Is useful to recall the $LUB$ property presented in [Real Number's post](https://gsanmi1.github.io/posts/2026/03/05/Real_Numbers/) as a distinct form of completness. That is a ordered field's form of completness, often called as *Dedekind's completness*.

These are two distinct concepts, not one concept expressed in two different ways. Dedekind completeness (the least-upper-bound property) is a property of ordered sets, whereas Cauchy completeness is a property of metric spaces. In general, neither implies the other: $(0,1)$ has the least-upper-bound property but is not Cauchy-complete, while $\mathbb{R}((t))$ is Cauchy-complete but lacks that property.

They share the name because they formalize the same intuition—"there are no gaps"—and because in Archimedean ordered fields, particularly in $\mathbb{R}$, they are equivalent. However, that coincidence is a theorem, not a definition.

<br>

## 4.5. Monotonic Sequences of real numbers.

### 4.5.1. Definition.

We stated that boundedness is necesary for Cauchy's and Convergent sequences, but is not sufficent, a Cauchy's sequence is always bounded as we see before but there are not-convergent Cauchy's sequence.

Let's give now the context for which boundedness is sufficent for (or equivalent to) convergence. This is the case of the *monotonic sequences*.

<br>

Let be $\Set{s_n} \subset \mathbb{R}$, then is said to be:

- monotonically increasing if: $s_n \leq s_{n+1} \quad \forall n \in \mathbb{Z}^+$.

- monotonically decreasing if: $s_n \geq s_{n+1} \quad \forall n \in \mathbb{Z}^+$.

<br>

### 4.5.2. Monotonic Sequences converges iff are bounded.

Take $\Set{s_n} \subset \mathbb{R}$ monotonic, concretely, decreasingly monotonic, and bounded. Consider $range\Set{s_n}$, then, since is bounded, in $\mathbb{R}$ has a supremum and an infimum let's call it $i \in \mathbb{R}$.

Then, $i$ verifies $s_n \geq i \quad \forall n \in \mathbb{Z}$. Take $\mathcal{E} > 0$, since $i = \inf range{\Set{s_n}}$, there is always some term behind $i + \mathcal{E}$:

$$\forall \mathcal{E}>0 \exists N \in \mathbb{Z}^+ (i + \mathcal{E} > s_N \geq i )$$

Observe that by the monotonic behaviour $s_N \geq s_{N+1} \geq s_{N+2} \ldots \geq i$, hence $s_n - i < \mathcal{E} \quad \forall n \geq N$ and we can reformulate above as:

$$\forall \mathcal{E}>0 \exists N \in \mathbb{Z}^+ (i + \mathcal{E} > s_n \geq i \quad \forall n \geq N) \iff$$

$$\iff \forall \mathcal{E}>0 \exists N \in \mathbb{Z}^+ (\mathcal{E} > s_n -i \geq 0 \quad \forall n \geq N) \iff$$

$$\iff \forall \mathcal{E}>0 \exists N \in \mathbb{Z}^+ (N \leq n \implies d(s_n,i) < \mathcal{E})$$

Which is exactly our definition of convergence.

<br>

# 5. Upper and Lower limits.



<br>