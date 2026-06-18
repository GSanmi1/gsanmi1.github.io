---
layout: post
title: "Directed Graphs & DAGs"
subtitle: "DAGs and their importance in computation"
date: 2026-02-27 09:00:00 +0000
categories: ['Graphs']
tags: ['Maths']
author: German Sanmi
subject: graph-theory
lang: en
---

# 0. Index

1. Directed Graphs
   - 1.1. Formal Definition
   - 1.2. Main Notions
        - 1.2.1. Impliance (u → v)
        - 1.2.2. In/Out Neighborhood and In/Out Degree
        - 1.2.3. Directed Walks, Paths, and Cycles

2. Directed Acyclic Graphs (DAGs)
   - 2.1. Definition: Sources and Sinks (existence)
   - 2.2. Order in DAGs
        - 2.2.1. Binary Relations and Orders
        - 2.2.2. Partial vs Total Order
        - 2.2.3. Strict vs Non-strict Order
        - 2.2.4. Reachability Order (≼) induced by a DAG
   - 2.3. Topological Order and Characterization of DAGs
   - 2.4. Basic Properties of DAGs
        - 2.4.1. Maximum Number of Edges
        - 2.4.2. Strongly Connected Components are Trivial
        - 2.4.3. Longest Walks/Paths in DAGs
   - 2.5. Canonical Constructions and Theorems
        - 2.5.1. Transitive Closure
        - 2.5.2. Transitive Reduction

3. Algorithmic Consequences
   - 3.1. DAGs as Dependency Structures (no circular dependencies)
   - 3.2. Local Propagation via Topological Order (forward/backward passes)

   <br>

# 1. Directed graphs.

A *directed acyclic graph* (DAG) is a directed graph that encodes a *one-way dependency* or *precedence relation*; *causality* with no circularity.

As an example, being $u,v$ two predicates related as $u \to v$, then a DAG would represent this relation by an arrow of $u$ to $v$ meaning that $v$ depends on $u$ (or $u$ must happen before $v$). 

Thus, DAGs are a way to abstract implication relationships between multiple agents in a discrete relational structure.

<br>

## 1.1. Formal Definition.

A directed graph gets defined as a pair: $D:= (V,E)$, where:

- $V$ is a finite set of elements.
- $E \subseteq V^2$ is a set of ordered pairs.
<br>

## 1.2. Main notions.

### 1.2.1. Impliance.

The first main notion we want to introduce is how the vertices (which are maintained from the simple graph conception) get related in a directed graph.

Being $G:=(V,E)$ a graph, then $E \subseteq \binom{V}{2}$ is the set of edges $\Set{u,v} \in E$ and we say that $u,v \in V$ are adjacent $u \sim v \iff \Set{u,v} \in E$. This is how two elements get related in the simple graph conception. $\Set{u,v}$, as a simple set, doesn't care about order so the relation is bidirectional, $u$ is adjacent to $v$ exactly as $v$ is adjacent back to $u$.

In the directional conception, there is no adjacency but impliance and this relation gets formalized through ordered sets. Remember that $D := (V,E)$ is a directed graph when $E \subseteq V^2$ meaning that the elements of $E$ are pairs $(u,v)$. In this context, we introduce the notion of *impliance*.

Being $u,v \in V$ then we say $u$ implies $v$, $u \to v \iff (u,v) \in E$. We can also say that $u$ precedes $v$. 

Note that this relation is not reciprocal, $u \to v \not \Rightarrow v \to u$

<br>

### 1.2.2. In/Out neighborhood.

Based on the notion of impliance defined before as a substitute for the adjacency in directed graphs, we consider the following sets:

- *In-neighborhood*; $N^{+}(u)=\{\,v\in V : u\to v\,\}$
- *Out-neighborhood*; $N^{-}(u)=\{\,v\in V : v\to u\,\}$

These are nothing but the parallel concept of neighbourhood in simple graphs $N(v) := \Set{u \ \vert \ u \sim v }$ but based on the order of the impliance.

Also, we can consider the following numbers:

- The *out-degree* to the number: $deg^+(v) := \vert N^{+}(v) \vert$
- The *in-degree* to the number: $deg^-(v) := \vert N^{-}(u) \vert$

<br>

### 1.2.3. Implicated vertex structures.

- **Directed Walk**; is a sequence $(v_0,...,v_k) : v_{i-1} \to v_i \ \ \forall i \in [k] \wedge k \in \mathbb{N}$

- **Directed Path**; is a directed walk with all vertices distinct.

- **Directed Cycle**; is a directed walk $(v_0,...,v_k,v_0) : (v_0,...,v_k)$ is a path.

![direct_structures](/assets/images/Maths/DiscreteMath/direct_structures.png)

<br>

# 2. Directed Acyclic Graphs (DAGs).

A Directed Acyclic Graph (DAG) is a directed graph with no cycles.

<br>

## 2.1. Definition. Sources and sinks.

Being $D:=(V,E)$ a DAG, then we define:

- **Sources**; a vertex $v \in V : deg^-(v)=0 \iff \nexists u \in V : u \to v$ 
- **Sinks**; a vertex $v \in V : deg^+(v)=0 \iff \nexists u \in V : v\to u$ 

![source_sink](/assets/images/Maths/DiscreteMath/source_sink.png)

In $D$ always exists at least one sink and one source:

$$D:=(V,E) \text{ a DAG } \implies  \exists u,v\in V : \big(deg^-(u)=deg^+(v)=0 \big)$$

Let's consider $\vert V \vert = 1$, then $u \in V$ is an isolated vertex and obviously $deg^-(u)=deg^+(v)=0$. 

Now consider $\vert V \vert \geq 2$; again, if there is some isolated vertex the result is immediate, so let's assume $D$ is connected and reason by contradiction, let's suppose that:

$$\neg \Big(\exists u,v\in V : (deg^-(u)=deg^+(v)=0 \wedge u \neq v)\Big) \iff (deg^+(u) \geq 1 \vee deg^-(v) \geq 1 \vee u = v) \ \ \forall u,v \in V$$

in $D$, we can negate this premise in three ways:

- First, these two vertices do exist, but are the same $\exists u,v\in V : \big(deg^-(u)=deg^+(v)=0 \wedge u = v \big)$, then $u$ is an isolated vertex contradicting connectivity in $D$.

    <br>

- Second, all vertices are sources; $deg^+(u)\geq 1 \ \ \forall u \in V$

    $$\neg \Big(\exists u,v\in V : deg^-(u)=deg^+(v)=0 \wedge u \neq v\Big)\implies  (deg^+(u) \geq 1 \vee deg^-(v) \geq 1) \ \ \forall u,v \in V : u \neq v$$
 
    In this context consider the longest path $P:=(u_1,...,u_k)$

    Due to maximality all out-neighbours of $u_k$ (whose existence is guaranteed due to the premise) are included in $P$ (otherwise you could extend $P$ contradicting maximality), meaning that $\exists i \in [k] : u_k \to u_i \wedge u_i \in P$, thus we can consider the cycle given as $C:= (u_i,...,u_k,u_i)$ since $(u_i,...,u_k) \subset P$ is a path, contradicting acyclicity in $D$.

    <br>

- Third, all vertices are sinks; $deg^-(u)\geq 1 \ \ \forall u \in V$

    Similarly to the argument given before, we can consider the longest path $P := (u_1,...,u_k)$ and due to the premise $N^-(u_1) \neq \varnothing$ and also, due to maximality $v \in P \ \ \forall v \in N^-(u_1)$ meaning that $\exists i \in [k] : u_i \to u_1 \wedge u_i \in P$ and we can consider the cycle $C:=(u_i,u_1,...,u_i)$ (since $(u_1,...,u_i)\subset P $ is a path). 

    <br>

This basically means that $DAG$ as defined always has at least one starting point and one endpoint.

<br>

## 2.2. Order in DAGs.

### 2.2.1. Binary Relations and Orders.

Given a set $X$, a binary relation on $X$ is a subset: $R \subseteq X \times X$ and we write as a shorthand, being $x,y \in X$, then:

$$xRy \iff (x,y) \in R$$

We call $R$ an order, and, defined under certain conditions, we abstract the idea that $x$ precedes $y$ through $R$ and we represent it such as $(x,y) \in R$

Then, any binary relation $R$ must satisfy the following three conditions to be called an *order*:

- **Reflexive**: $xRx \ \ \forall x \in X$
- **Transitive**: $xRy \wedge yRz \implies xRz \ \ \forall x,y,z \in X$
- **Antisymmetric**: $xRy \wedge yRx \implies x = y \ \ \forall x,y \in X$

<br>

### 2.2.2. Partial and Total Order.

When we define a binary relation $R$ over a set $X$ then it is pertinent to ask if:

$$xRy \vee yRx \ \ \ \forall x,y \in R$$

If $x$ and $y$ are incomparable then we write:

$$\neg(xRy) \wedge \neg (yRx) \iff x \ \vert \vert \ y$$

We say that $R$ defined in $X$ is: 

$$R \text{ is a partial order } \iff \exists x,y \in X : x \ \vert \vert \ y$$
$$R \text{ is a total order } \iff xRy \vee yRx \ \ \ \forall x,y \in R$$

<br>

### 2.2.3. Strict and non-strict order.

An order can be defined considering whether some element can relate to itself or not ($xRx$), in the sense of non-strict or strict order.

Being $X$ a set and $R$ a binary relation, then:

$$ R \text{ is non-strict order} \iff xRx \ \forall x \in R$$
$$ R \text{ is strict order} \iff \exists x \in X : (x,x) \notin R$$

Let's observe that, being $M_{xy}$ predicates over $x$ and $y$ that must be satisfied to be $xRy$, then in the non-strict order is always $M_{xx} \equiv \top$, then we can say: 

$$xRy \iff M_{xy} \vee x = y : M_{xy} \otimes M_{yx}$$

Let's observe that by how the predicates $M$ are defined, $R$ as a non-strict order verifies:

$$xRy \wedge yRx \iff x = y$$

Equivalently, if there exists at least one $x \in X: (x,x) \notin R$, then $R$'s definition must impose differentiation between two elements for these to be relatable:

$$xRy \iff M_{xy} \wedge x \neq y$$

<br>

### 2.2.4. Partial Order in DAGs.

Consider $D$ a $DAG$, then, we can define the following subset 

$$\preceq  \ \subseteq V^2: x \preceq y \longleftrightarrow \exists \text{ a directed path } P_{xy} \ (x \rightsquigarrow y)$$

Observe that this relation is an order since:

- *Reflexive*: $v \preceq v \ \ \forall v \in V$ since $(v,v) \in E$
- *Transitive*: $v \preceq u \wedge u \preceq w \implies P_{vw} = P_{vu},P_{uw} \implies v \preceq w$
- *Antisymmetric*: $v \preceq u \wedge u \preceq v \implies u = v$ since no cycles are allowed.

Observe that the *reflexive* property of $\preceq$ makes it automatically a non-strict order, and we define the strict variant of the partial order as: $\prec \ \subseteq \  V^2 : u \prec v \iff  u \preceq v \wedge u \neq v$. 
<br>

## 2.3. Topological Order. Characterization of DAGs.

*Topology* is the branch of mathematics concerned with the properties of a geometric object preserved under continuous deformations, meaning that they are not related to the spatial disposition of the object.

Thus, related to directed graphs, *topological order* is the formal way to sort the vertices of a directed graph based on their *impliance* relation. 

<br>

The formal definition is, given $D:= (V,E): \vert V \vert = n$ a directed graph, then, a *topological order* over $D$ is a bijection:

$$\tau : V \to [n] : \tau(u) < \tau(v) \ \ \forall (u,v) \in E$$

As a useful conceptualization, this topological order allows us to dispose the graph in a natural line, as a sequence $(v_1,...,v_n)$ containing each vertex exactly once, such that for every directed edge; $u \to v$ vertex $u$ appears earlier in the sequence than $v$.

<br>

![torder](/assets/images/Maths/DiscreteMath/torder.png)

<br>

Having presented the topological order, let's see that the existence of a topological order for a directed graph is what ensures that the graph is acyclic:

$$ D \text{ is a DAG } \iff \exists \text{ a bijection } \tau :  V \to [n] : \big(\tau(u) < \tau(v) \ \ \forall (u,v) \in E \big)$$

- $\Rightarrow$

    Let's see that if $D$ is a DAG and there are no cycles, then, being $v \in V$, we call $rank(v) \in \mathbb{Z}$ the number of vertices that precede $v$ on the longest path (observe that by "precede" we mean those that implicate $v$ and also any vertex that implicates those who implicate $v$ and so on). So for example any $v \in V : deg^+(v) = 0$ has $rank(v)=0$. A hypothetical set of vertices such that $v,u,t \in V: v \to u \to t$ has $rank(v) = 0, rank(u) = 1, rank(t)=2$; if it were also $l \in V : l \to t$, the longest path is $v \to u \to t$, thus still $rank(t)=2$.

    In this context, we define a function $f: V \to [n]$ that, calling $R_i = \Set{ u \ \vert \ rank(u) = i}$, $f$ verifies:

    - $max\Set{f(u) : u \in R_{i-1}} < f(u) \ \ \forall u \in \Set{u \ \vert \ rank(u) = i}$

    - $f(u) \neq f(v) \ \ \ \forall u,v \in V : u \neq v$

    Let's observe that this function is injective (we are imposing it) and also, since every vertex has a rank, every vertex has an image through $f$ and since there are $n$ vertices, the function is 'surjective' and is a bijection.

    Also, it is obvious that $u \to v \implies rank(u) < rank(v) \implies f(u) < f(v)$ so $f$ is a topological order over $D$.

    <br>

- $\Leftarrow$

    It is obvious since if $D$ is a directed graph that admits a bijection defined as above, there can't be cycles or the function requisite: $\tau(u) < \tau(v) \ \forall (u,v) \in E$ wouldn't be satisfied.

    <br>

Note that the topological order is a total order in a $DAG$. This conclusion is obvious taking the lined-up-vertices perspective of $D$.

<br>

## 2.4. Basic Properties in DAGs.

### 2.4.1. Maximum number of edges.

Given a directed graph $D$ (no parallel edges) a $DAG$, since no cycles are allowed, then:

$$\neg \big((u,v) \in E \wedge (v,u) \in E\big) \ \ \forall u,v \in V$$

Meaning that for any unordered set $\Set{u,v}$ is at most $(u,v)$ or $(v,u)$ in $E$, meaning that:

$$ \vert E \vert \leq \vert \binom{V}{2} \vert = \binom{\vert V \vert}{2}$$

Meaning that at most one of the two (or none of the two) is present in $E$.

<br>

### 2.4.2. Strongly connected components are trivial.

We call a strongly connected component a subgraph $S \subseteq D$ such that $S = K_n : n \leq \vert V \vert$. Obviously for $n \geq 3$, $S$ would allow a cycle, so in a $DAG$ any strongly connected component is reduced to a set of two connected vertices.

<br>

### 2.4.3. Longest walks in DAGs.

In a DAG, the longest path $walk$ is $\vert P \vert \leq \vert V \vert -1$ since there can't be cycles; a walk cannot repeat vertices so paths and walks collapse in $DAGs$ and the longest possible walk has at most $\vert V \vert$ vertices or $\vert V \vert-1$ edges.

<br>

## 2.5. Canonical constructions and theorems.

### 2.5.1. Transitive Closure.

The *transitive closure* of a $DAG$, $D:=(V,E)$ is a digraph defined as follows: 

$$D^+:=(V,E'): (u,v) \in E' \iff u \rightsquigarrow_D v$$

This is what you get when you treat reachability as edges in a digraph, obtaining an extension of the impliance relation of the vertices of $D$ in the sense that in $D^+$ $u$ implies $v$ if there exists a chain of impliances from $u$ to $v$ in $D^+$.

<br>

### 2.5.2. Transitive Reduction.

The transitive reduction of a $DAG$, $D$ is a minimally reachable version of the graph $R$ on the same vertex set, in the sense that removing an edge breaks the reachability of the graph.

$$R:=(V,E'): E' \subset E \wedge \big[(u,v) \in E \setminus E' \iff  \exists P_{uv} \subset D \setminus \Set{(u,v)} \big]$$

Let's observe that it is the opposite conception of the closure: while the closure saturates the implications on $D$, the *reduction* minimizes those same implications; both of them are variations of the number of connections in the graph maintaining the partial order relation $\preceq$ between the vertices.

<br>

# 3. Algorithmic Consequences.

Until this point, we've seen that a $DAG$ is a dependency structure with no circular dependencies (cycles). No cycles allow us to evaluate/optimize/count and schedule things by a single forward/backward pass without backtracking.

Let's expand this idea. In general, computation consists of taking an object and operating with it in order to extract some value or conclusion, but objects can be dependent on each other, in the sense that often an object is the result of the computation of another object (like getting a point in a field is the result of solving a system of equations since the point must verify some constraints). This dependency can be illustrated in a directed graph $u \to v$.

Then, acyclicity in a directed graph means that you don't get circular dependencies (circular dependencies require computing simultaneously two dependent objects, which translates into complex operations or iteration until convergence). $DAGs$ avoid that; acyclicity turns global problems into local propagation. Observe that in some way this is reflected in the existence of the partial order $\preceq$ and the topological order which basically guarantee the transformation of a $DAG$ into a chain of implications.