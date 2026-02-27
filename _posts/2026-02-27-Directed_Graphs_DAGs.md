---
layout: post
title: "Direct Graphs & DAGs"
subtitle: "DAGs and its importance in computation"
date: 2026-02-27 09:00:00 +0000
categories: ['Graphs']
tags: ['Maths']
author: German Sanmi
---

# 0. Index

1. Directed Graphs
   1.1. Formal Definition
   1.2. Main Notions
        1.2.1. Impliance (u → v)
        1.2.2. In/Out Neighborhood and In/Out Degree
        1.2.3. Directed Walks, Paths, and Cycles

2. Directed Acyclic Graphs (DAGs)
   2.1. Definition: Sources and Sinks (existence)
   2.2. Order in DAGs
        2.2.1. Binary Relations and Orders
        2.2.2. Partial vs Total Order
        2.2.3. Strict vs Non-strict Order
        2.2.4. Reachability Order (≼) induced by a DAG
   2.3. Topological Order and Characterization of DAGs
   2.4. Basic Properties of DAGs
        2.4.1. Maximum Number of Edges
        2.4.2. Strongly Connected Components are Trivial
        2.4.3. Longest Walks/Paths in DAGs
   2.5. Canonical Constructions and Theorems
        2.5.1. Transitive Closure
        2.5.2. Transitive Reduction

3. Algorithmic Consequences
   3.1. DAGs as Dependency Structures (no circular dependencies)
   3.2. Local Propagation via Topological Order (forward/backward passes)

# 1. Directed graphs.

A *directed acyclic graph* (DAG) is a directed graph that encodes a *one-way dependency* or *precedence relation*; *causality* with no circularity.

As an example, being $u,v$ two predicates related as $u \to v$, then a DAG would represent this relation by an arrow of $u$ to $v$ meaning that $v$ depends on $u$ (or $u$ must happen before $v$). 

Thus, DAGs are a way to abstract implication relationships between multiples agents in a discrete relation structure.

<br>

## 1.1. Formal Definition.

A direct graph gets defined as a pair: $D:= (V,E)$, where:

- $V$ is a finite set of elements.
- $E \subseteq V^2$ is a set of ordered pairs.
<br>

## 1.2. Main notions.

### 1.2.1. Impliance.

The first main notion we want to introduce is how the vertex (which are maintained from the simple graph conception) gets related in a directed graph.

Being $G:=(V,E)$ a graph, then $E \subseteq \binom{V}{2}$ is the set of edges $\Set{u,v} \in E$ and we say that $u,v \in V$ are adjacent $u \sim v \iff \Set{u,v} \in E$. This is how two elementes gets related in the simple graph conception. $\Set{u,v}$, as a simple set, doesn't care about order so the relation is bidirectional, $u$ is adjacent to $v$ exactly as $v$ is adjacent back to $u$.

In the directional conception, there is no adjacency but impliance and this relation gets formalized through ordered sets. Remember that $D := (V,E)$ is a directed graph when $E \subseteq V^2$ meaning that the elements of $E$ are pairs $(u,v)$. In this context, we introduce the notion of *impliance*.

Being $u,v \in V$ then we say $u$ implies $v$, $u \to v \iff (u,v) \in E$. We can also say that $u$ preceds $v$. 

Note that this relation is not reciproc, $u \to v \not \Rightarrow v \to u$

<br>

### 1.2.2. In/Out neighborhood.

Based in the notion of impliance defined before as a substitue of te adjacency for direct graphs, we consider the following sets:

- *In-neighborhood*; $N^{+}(u)=\{\,v\in V : u\to v\,\}$
- *Out-neighborhood*; $N^{-}(u)=\{\,v\in V : v\to u\,\}$

This are nothing but the paralalel concept of neigbourhood in simpe graphs $N(v) := \Set{u \ \vert \ u \sim v }$ but based in the order of the impliance.

Also, we can consider the following numbers:

- The *out-degree* to the number: $deg^+(v) := \vert N^{+}(v) \vert$
- The *in-degree* to the number: $deg^-(v) := \vert N^{-}(u) \vert$

<br>

### 1.2.3. Implicated vertex structures.

- **Directed Walk**; is a sequence $(v_0,...,v_k) : v_{i-1} \to v_i \ \ \forall i \in [k] \wedge k \in \mathbb{N}$

- **Directed Path**; is a directed walk with all vertices distinct.

- **Directed Cycle**; is a directed walk $(v_0,...,v_k,v_0) : (v_0,...,v_k)$ is a path.

![direct_structures](/assets/images/MathWs/DiscreteMath/direct_structures.png)

<br>

# 2. Directed Acyclic Graphs (DAGs).

A Directed Acylic Graph (DAG) is a directed graph with no cycles.

<br>

## 2.1. Definition. Sources and sinks.

Being $D:=(V,E)$ a DAG, then:, we define:

- **Sources**; vertex $v \in V : deg^-(v)=0 \iff \nexists u \in V : u \to v$ 
- **Sinks**; vertex $v \in V : deg^+(v)=0 \iff \nexists u \in V : v\to u$ 

![source_sink](/assets/images/Maths/DiscreteMath/source_sink.png)

In $D$ always exists at least one sink and one source:

$$D:=(V,E) \text{ a DAG } \implies  \exists u,v\in V : \big(deg^-(u)=deg^+(v)=0 \big)$$

Let's consider $\vert V \vert = 1$, then $u \in V$ is an isolated vertex and obviously $deg^-(u)=deg^+(v)=0$. 

Now consider $\vert V \vert \geq 2$, again if there is some isolated vertex the result is immediate, so lets assume $D$ is connected and reason to the opposite, let's suppose that:

$$\neg \Big(\exists u,v\in V : (deg^-(u)=deg^+(v)=0 \wedge u \neq v)\Big) \iff (deg^+(u) \geq 1 \vee deg^-(v) \geq 1 \vee u = v) \ \ \forall u,v \in V$$

in $D$, we can negate this premise in three ways:

- First, this two vertex do exists, but are the same $\exists u,v\in V : \big(deg^-(u)=deg^+(v)=0 \wedge u = v \big)$, then $u$ is an isolated vertex contradicting connection in $D$.

    <br>

- Second, all vertex are sources; $deg^+(u)\geq 1 \ \ \forall u \in V$

    $$\neg \Big(\exists u,v\in V : deg^-(u)=deg^+(v)=0 \wedge u \neq v\Big)\implies  (deg^+(u) \geq 1 \vee deg^-(v) \geq 1) \ \ \forall u,v \in V : u \neq v$$
 
    In this context consider the longuest path $P:=(u_1,...,u_k)$

    Due to maximality all out-neigbourhs of $u_k$ (whose existence is garanteed due to the premise) are included in $P$ (otherwise you could extend $P$ contradicting maximality), meaning that $\exists i \in [k] : u_k \to u_i \wedge u_i \in P$, thus we can consider the cycle given as $C:= (u_i,...,u_k,u_i)$ since $(u_i,...,u_k) \subset P$ is a path contradicting acyclicness in $D$.

    <br>

- Third, all vertex are sinks; $deg^-(u)\geq 1 \ \ \forall u \in V$

    Similarly to the argument given before, we can consider the longuest path $P := (u_1,...,u_k)$ and due to the premisse $N^-(u_1) \neq \varnothing$ and also, due to maximality $v \in P \ \ \forall v \in N^-(u_1)$ meaning that $\exists i \in [k] : u_i \to u_1 \wedge u_i \in P$ and we can consider the cycle $C:=(u_i,u_1,...,u_i)$ (since $(u_1,...,u_i)\subset P $ is a path). 

    <br>

This basically means that $DAG$ as defined always has at least one starting point and one endpoint.

<br>

## 2.2. Order in DAGs.

### 2.2.1. Binary Relations and Orders.

Given a set $X$, a binary relation on $X$ is a subset: $R \subseteq X \times X$ and we write as a shorthand, being $x,y \in X$, then:

$$xRy \iff (x,y) \in R$$

We call to $R$ as an order, and, defined along certains conditions, we abstract the idea that $x$ preceeds $y$ through $R$ and we represent it such as $(x,y) \in R$

Then, any binary relation $R$ must satisfy the following three condition to be called a *order*:

- **Reflexive**: $xRx \ \ \forall x \in X$
- **Transitive**: $xRy \wedge yRz \implies xRz \ \ \forall x,y,z \in X$
- **Antisimetric**: $xRy \wedge yRx \implies x = y \ \ \forall x,y \in X$

<br>

### 2.2.2. Partial and Total Order.

When we define a binary relation $R$ over a set $X$ then is pertinent to ask if:

$$xRy \vee yRx \ \ \ \forall x,y \in R$$

If $x$ and $y$ are incomparable then we write:

$$\neg(xRy) \wedge \neg (yRx) \iff x \ \vert \vert \ y$$

We say that $R$ defined in $X$ is: 

$$R \text{ is a partial order } \iff \exists x,y \in X : x \ \vert \vert \ y$$
$$R \text{ is a total order } \iff xRy \vee yRx \ \ \ \forall x,y \in R$$

<br>

### 2.2.3. Strict and non-strict order.

An order can be defined considering if some element can relate with him self or not ($xRx$) in the sense that if non-strict or strict order.

Being $X$ a set and $R$ a binary relation, then:

$$ R \text{ is non-strict order} \iff xRx \ \forall x \in R$$
$$ R \text{ is strict order} \iff \exists x \in X : (x,x) \notin R$$

Let's observe that, being $M_{xy}$ predicates over $x$ and $y$ that must be satisfied to be $xRy$, then in the non-strict order is always $M_{xx} \equiv \top$, then we can say: 

$$xRy \iff M_{xy} \vee x = y : M_{xy} \otimes M_{yx}$$

Let's observe that by how the predicates $M$ are defined, $R$ as a non-strict order verifies:

$$xRy \wedge yRx \iff x = y$$

Equivalently, if exist at least one $x \in X: (x,x) \notin R$, then $R$ definition must impose diferenciation between two elements for these to be relatable:

$$xRy \iff M_{xy} \wedge x \neq y$$

<br>

### 2.2.4. Partial Order in DAGs.

Consider $D$ a $DAG$, then, we can define the following subset 

$$\preceq  \ \subseteq V^2: x \preceq y \longleftrightarrow \exists \text{ a directed path } P_{xy} \ (x \rightsquigarrow y)$$

Observe that this relation is an order since:

- *Reflexive*: $v \preceq v \ \ \forall v \in V$ since $(v,v) \in E$
- *Transitive*: $v \preceq u \wedge u \preceq w \implies P_{vw} = P_{vu},P_{uw} \implies v \preceq w$
- *Antisimetric*: $v \preceq u \wedge u \preceq v \implies u = v$ since not cycles are allowed.

Observe that the *reflexive* property of $\preceq$ makes it automatically a non-strict order, and we define the strict variant of the partial order as: $\prec \ \subseteq \  V^2 : u \prec v \iff  u \preceq v \wedge u \neq v$. 
<br>

## 2.3. Topological Order. Characterization of DAGs.

*Topology* is the branch of mathematics concerned with the properties of a geometric object preserved under continuous deformations, meaning that are not related with spacial disposition of the object.

Thus, related with direct graphs, *topological order* is the formal way to sort the vertices of a directed graph based on their *impliance* relation. 

<br>

The formal definition is, given $D:= (V,E): \vert V \vert = n$ a direct graph, then, a *topological order* over $D$ is a bijection:

$$\tau : V \to [n] : \tau(u) < \tau(v) \ \ \forall (u,v) \in E$$

As a usefull conceptualization, this topological order allow us to dispose the graph in a natural line, as a sequence $(v_1,...,v_n)$ containing each vertex exactly once, such that for every direct edge; $u \to v$ vertex $u$ appears earlier in the sequence than $v$.

<br>

![torder](/assets/images/Maths/DiscreteMath/torder.png)

<br>

Having presented the topological order, lets see that the existance of a topolofical order for a direct graph is what ensure that his graph is acyclic:

$$ D \text{ is a DAG } \iff \exists \text{ a bijection } \tau :  V \to [n] : \big(\tau(u) < \tau(v) \ \ \forall (u,v) \in E \big)$$

- $\Rightarrow$

    Let's see that if $D$ is a DAG and there are no cycles, then, being $v \in V$, we call $rank(v) \in \mathbb{Z}$ to the number of vertex that preceed $v$ on the larguest path (observe that by "preceed" we mean those who implicates $v$ and also any vertex that implicates those who implicates $v$ and so on). So for example any $v \in V : deg^+(v) = 0$ has $rank(v)=0$. An hipotetic set of vertex such $v,u,t \in V: v \to u \to t$ has $rank(v) = 0, rank(u) = 1, rank(t)=2$, if also it was $l \in V : l \to t$, the larguest path is $v \to u \to t$, thus still $rank(t)=2$.

    In this context, we define a function $f: V \to [n]$ that, calling $R_i = \Set{ u \ \vert \ rank(u) = i}$, $f$ verifies:

    - $max\Set{f(u) : u \in R_{i-1}} < f(u) \ \ \forall u \in \Set{u \ \vert \ rank(u) = i}$

    - $f(u) \neq f(v) \ \ \ \forall u,v \in V : u \neq v$

    Let's observe that this function is injective (we are impossing it) and also, since every vertes has a rank, every vertex has an image through $f$ and since there is $n$ vertex, the function is 'surjective' and is a bijection.

    Also, is obvious that $u \to v \implies rank(u) < rank(v) \implies f(u) < f(v)$ os $f$ is a topological order over $D$.

    <br>

- $\Leftarrow$

    Is obvious since if $D$ is a direct graph that admits a bijection defined as above, it can't be cycles or the function requisite: $\tau(u) < \tau(v) \ \forall (u,v) \in E$ wouldn't be satisfied.

    <br>

Note that the topological order is a total order in a $DAG$. This conclusion is obvious taking the line-up the vertex perspective of $D$.

<br>

## 2.4. Basic Properties in DAGs.

### 2.4.1. Maximum number of edges.

Given a directed graph $D$ (no parallel edges) a $DAG$, since no cycles are allowed, then:

$$\neg \big((u,v) \in E \wedge (v,u) \in E\big) \ \ \forall u,v \in V$$

Meaning that for any unordered set $\Set{u,v}$ is at most $(u,v)$ or $(v,u)$ in $E$, meaning that:

$$ \vert E \vert \leq \vert \binom{V}{2} \vert = \binom{\vert V \vert}{2}$$

Meaning that at most one of the two (or none of the two) 

<br>

### 2.4.2. Strongly connected components are trivial.

We call a strongly connected component a subgraph $S \subseteq D$ such $S = K_n : n \leq \vert V \vert$. Obviously for $n \geq 3$, $S$ would allow a cycle, so in a $DAG$ any strongly component is reduced to a set of two connected vertex.

<br>

### 2.4.3. Longest walks in DAGs**

In a DAG, the longest path $walk$ is $\vert P \vert \leq \vert V \vert -1$ since there can't be cycles, a walk cannot repeat vertex so path and walks collapses in $DAGs$ and the longuest possible walk has at least $\vert V \vert$ vertex or $\vert V \vert-1$ edges.

<br>

## 2.5. Canonical constructions and theorems.

### 2.5.1. Transitive Closure.

The *transitive closure* of a $DAG$, $D:=(V,E)$ is a digraph defined as follows: 

$$D^+:=(V,E'): (u,v) \in E' \iff u \rightsquigarrow_D v$$

This is what you get when treat reachbility as edges in a digraph, obtaining an ampliation of the impliance relation of the vertex $D$ in the sense that in $D^+$ $u$ implies $v$ if exists a chain of impliances from $u$ to $v$ in $D^+$.

<br>

### 2.5.2. Transitive Reduction.

The transitive reduction of a $DAG$, $D$ is a minimally reachable version of thegraph $R$ on the same vertex set, in the sense that remove an edge breaks the reachability the graph.

$$R:=(V,E'): E' \subset E \wedge \big[(u,v) \in E \setminus E' \iff  \exists P_{uv} \subset D \setminus \Set{(u,v)} \big]$$

Let's observe that is the opposite conception of the closure, while the closure satures the implications on $D$, the *reduction* minimize those same implications, both of them are variations of the number of connections in the graph mainting the partial order relation $\preceq$ between the vertexs.

<br>

# 3. Algorithmic Consequences.

Until this point, we've seeing that a $DAG$ is a dependency structure with no circular dependencies (cycles). No cycles allows to evaluate/optimice/count and schedule things by a single forward/backward pass without backtracking.

Let's expand this idea. In general, computate consist in take an object and operate with it in order to extract some value or conclusion, but objects can be dependant between each others, in the sense that often an object is the result of the computation of other object (like get a point in a field is the result of solving a system equatiom since the point must verify some constraints). This dependency can be ilustrate in a directed graph $u \to v$.

Then, acyclicness in a directed graph means that you don't get circular dependencies (Circular dependencies requires to computate simultaneously two dependant objects which is traduced to a complex operations or iteration until convergence). $DAGs$ avoids that; acyclicity turns global problems into local propagation. Observe that in some way this is reflected in the existance of the partial order $\preceq$ and the topological order which basically garantee the transformation of a $DAG$ into a chain of implications.