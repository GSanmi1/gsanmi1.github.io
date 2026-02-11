---
layout: post
title: "Arithmetic Circuits."
subtitle: "Maths fundamentals in arithmetic circuits and appliances in ZKP."
date: 2026-02-06 09:00:00 +0000
categories: ['Fundamentals']
tags: ['ZKP', 'Maths']
author: German Sanmi
---

# 1. Introduction.

As we established on [2.Boolean Formulas](https://gsanmi1.github.io/posts/2026/02/02/Boolean_Formulas/) post, any NP problem is Karp reductable to SAT implying that any instance of a NP problem can be verified by verifying some certain SAT instance, this is; finding a valuation that makes True a boolean circuit that models the problem.

However, bits are very restricted, often a codification of an instance of a problem to a big-complex boolean structure is needed (quitting some expceptions) which often leads to unefficient (in terms of space and time) computations as we see in the examples of the post above. This is why *arithmetic circuits* are way preferable of use instead.

Conceptually, an arithmetic circuit is a system of equations that models a problem in NP. 

<br>

# 2. Prerequisites.

## 2.1. Discrete Math: Graphs and DAGs.

### 2.1.1. Undirected Graphs.

#### 2.1.1.1. Introduction.

*Graph Theory*; is the discipline of mathematics which occupies about the study of discrete relation's structures and his properties. Conceptually, a *graph* is the minimal object that captures “pairwise relationships” between abstract entities.

Formally a **graph** (undirected graph) to the pair $G := (V,E)$ where:

- $V$ is a finite non-empty set whose elements are called *vertices*.
- $E \subseteq \binom{V}{2}$ and his elements are called *edges*.

<br>

There are several notions associtated with the idea of a *graph*:

- **Adjacency**: Two vertex $u,v \in V$ are said to be *adjacent*; $u \sim v \iff \Set{u,v} \in E$
- **Neighborhood**: The neighborhood of $v \in V$ is the set $N(v) = \Set{u \in V : v \sim u}$
- **Degree**: The number of adjacent vertex to a given one $v \in V$; $\text{deg}(v) = \vert N(v) \vert$
- **Subgraph** of $G$ is any set: $H := (V_H, E_H) : V_H \subseteq V \land E_H \subseteq E \ \cap \ \binom{V_H}{2}$

- **Induced subgraph**: $G[W] := (W, E \cap \binom{W}{2}): W \subseteq V$

<br>

Regarding to a collection of adjacent vertex, we can talk about:

- **Walk**; a finite sequence of adjacent vertices: $v_0...,v_t: v_{i-1} \sim v_i \ \forall i \leq t \in \mathbb{N}$

- **Path** is a walk with all the vertices distinct: $v_0...,v_t:v_{i-1} \sim v_i \ \forall i \leq t \in \mathbb{N} \ \land \ v_i \neq v_j \ \ \forall i,j \in \mathbb{N}$

- **Cycle** is a walk $v_0,...,v_{t-1},v_0$ where $v_0,...,v_{t-1}$ is a path.

- **Conneted Vertex**; Two vertices are said to be connected if one can reach the other through a path.

<br>

![walk_path_cycle](/assets/images/Maths/DiscreteMath/walk_path_cycle.png)

<br>

Relative to the state of the vertex in the graph we can talk about:

- **Connected graph**: Every pair of vertex are *connected* vertex.
- **Complete graph**: Every pairm of vertex are *adjacents*. They are notated simply as $K_n :=(V,E): \vert V \vert = n$ and satisfies: $u  \sim v \ \ \forall u,v \in V$
- **Tree**: A connected graph with no cycles.



#### 2.1.1.2. Tree characterization.

Let's consider a tree $T:=(V,E)$:

<br>

![tree](/assets/images/Maths/DiscreteMath/tree.png)

<br>

##### 2.1.1.2.1. Leaf lemma.

“Leaf lemma” refers to a basic fact in graph theory about *trees*. A tree is “all branches, no cycles”. If it has at least one edge, you can’t keep walking forever without either repeating a vertex (which would create a cycle) or getting stuck. The “stuck points” at the ends are leaves, and you must have at least two ends.

We define as $L := \Set{v \in V : \vert N(v) \vert = 1}$ the set of the leafs of $T$, then: 

$$\vert V \vert \geq 2 \implies \vert L \vert \geq 2$$

Basically the statement stands that in any tree there are at least 2 leafs. 

Let's reason by the longest path. Be $T:=(V,E) : \vert V \vert \geq 2$ a tree, since $T$ is connected with can consider for $l,t \in V$ the path between them, so lets consider by convenience the longest path in $T$, $P_{lt}:=v_0,...,v_k$.

Now consider $v_0$ (we could reason the same way for $v_k$), and let suppose that $\vert N(v_0) \vert \geq 2$, if it is, then we can consider some $u \in V : u \sim v_0 \land u \neq v_1$, then: 


- If $u \in P \implies C_u:= u,...,v_0,v_1,u \subset T$ contradicting the acyclicness property.
- If $u \notin P$, then $P' = u,v_0,...,v_k$ would be the longest path contradicting the maximality asumption of $P$.

So $deg(v_0) = deg(v_k) = 1$ and both are leaf in $T$.


<br>

##### 2.1.1.2.2. Equivalences statements of Trees.

The following statements are equivalent for a tree $T:=(V,E)$

1. $T$ is **connected** and $\vert E \vert = \vert V \vert - 1$

    First, $T$ is connected by definition. Lets reason by induction.

    - $n = 2$: Consider $T:= (V,E) : V :=\Set{u,v}$. Since $T$ is connected, $u,v \in V$ are connected and thus adjacent; $u \sim v \implies E := \Set{\Set{u,v}} \implies \vert E \vert  = 1 = \vert V \vert - 1$

        <br>

    - Considered true for some $n$, then $T'$ is a tree verifying $\vert V' \vert = n + 1$
    
        Consider a leaf $t \in V' : \vert N(t) \vert = 1$ (by the leaf lemma, we can ensure his existance) and the induced graph:
        
        $$T:= (V,E) : \begin{cases} V = V' \setminus \Set{t} \\ E= E' \cap \binom{V' \setminus \Set{t}}{2}\end{cases}$$
        
        
        Observe that since $t$ is a leaft, then is an endpoint for some path in $T$ and removes it does not break connectivity.
        
        Thus $T$ is a graph with $n$ vertices and for $T'$ and the leaf lemma still being connected and acyclice, meaning it remains a tree. Thus $T,T'$ are two trees verifying: $\vert E \vert = n - 1 \land V' = V \cup \Set{t}$

        Let's also observe that:

        $$ E= E' \cap \binom{V' \setminus \Set{t}}{2} = E' \setminus \Set{\Set{l,t} \in E' : l \in V'}$$
        Thus, we have:
        
        $$\vert E' \vert = \vert E\vert + \vert \Set{\Set{l,t} \in E': l \in V'} \vert = (n - 1) + 1 = \vert V' \vert-1$$

        <br>

2. $T$ is **acyclic** and $\vert E \vert = \vert V \vert - 1$. Is immediate from above.

    <br>

3. **Between two any vertices there is a unique path**. Reasoning to the absurd, if between $l,t \in V$ would exists more than one path, lets say: $t,u_0,...,u_{k-1},l$ and $l,v_0,...,v_{k-1},t$, then $t,u_0,...,u_{k-1},l,v_0,...,v_k{-1},t$ would be a cycle contradicting acycling in trees.

    <br>

4. $T$ is **minimally connecte**d: removing any edge disconnects it.

    Observe that this stems from the uniqueness of the path for any pair of vertices. Meaning that, if $e=\Set{u,v} \in E$, then exists a *unique* path $P = t,...,u,v,...l$ in $T$ and removing $e$ from $E$ leaves no path between $u$ and $v$ contradicting the connectness premise on $T$ as a tree.

    <br>

5. $T$ is **maximally acyclic**: adding any missing edge creates a cycle.

    Let's consider $u,v \in V : u \ \cancel{\sim} \ v$, then, since $T$ is connected, exists a path $u,...,v \in T$ and forcing $\Set{u,v} \in E \implies C_u = u,...v,u \subset T$ contradicting acyclicness.

    <br>

##### 2.1.1.2.3. Handshaking lemma for trees.

The *handshaking lemma* stays for: 

$$\sum_{v \in V} deg(v) = 2 \vert E \vert$$

Let's see that we can proof this by induction:

- Consider: $\vert V \vert = 2 \implies \displaystyle\sum_{v \in V} deg(v) = 2 = 2 \vert E \vert$
- Consider now $\vert V \vert = n+1$, then we can consider by the leaf lemma $t \in V: deg(t) =1$:

    $$ T' :=(V',E'): \begin{cases} V' = V \setminus \set{t} \\ E' = E \cap \binom{V'}{2}\end{cases}$$

    Let observe that $T'$ is a tree with $n$ vertices, then, by the induction premise $\displaystyle\sum_{v \in V'} deg(v) = 2 \vert E' \vert$, and also, being $u \in V : u \sim t$, then $E = E' \cup \Set{u,t}$ meaning that:

    $$ \sum_{v \in V} deg(v) = \sum_{v \in V'} deg(v) + 2 = 2 \vert E' \vert + 2 = 2(\vert E' \vert + 1) = 2\vert E \vert$$

<br>

Observe that this also means that there is an even number of odd-degrees.

<br>

#### 2.1.1.3. Eulerian and Hamiltonian graphs.

*Eulerian graphs* is a class of graphs that can be traversed using each edge exactly once. *Hamiltonian graphs* is a class of graph that can be traversed using each vertex exactly once.

<br>

##### 2.1.1.3.1. Eulerian graphs.

**Main notions and definitions**

Be $G:=(V,E)$ a graph, then we define the following terms:

- **Euler walk**, is a walk that goes through every edge of $E$ exactly once.
- **Euler circuit**, is an *eulerian walk* that starts and ends at the same vertex.

Then, 

- $G$ is said to be *semi-eulerian* if it admits an eulerian trail but not an eulerian circuit. 
- $G$ is said to be *eulerian* if it admits an eulerian circuit.

<br>

**Characterization**

Being $G$ a connected graph, then:

$$G \text{ is eulerian } \iff deg(v) \vert 2 \ \ \ \forall v \in V$$

<br>

First, let's that if $G$:

- $G \text{ is eulerian } \implies  deg(v) \vert 2 \ \ \ \forall v \in V$

    If we consider $G:=(V,E)$ connected that admints and eulearian circuit, then, we can think on a walk that traverse every edge without repeat any of it.

    Thus, for the walk to not repeat edges and to end in the same vertex that started, for every vertex $v \in V$ which is not the start of the walk there is at least two edges; one that enters in $\Set{u,v}$ and other that gets out from $\Set{v,w}$, for every time the walk visit a vertex in $V$ (this also applies whenever the vertex gets repeated in the walk).
    
    Also, if $r \in V$ is the root vertex from which the walk start, then if this vertex gets visited more than once then applies the rule above and also has the first edge from which start the walk and the last edge of the walk that ends returning in $r$.
    
    So any $v \in V$ is adjacent to an even number of vertex and thus $deg(v) \vert 2$.

<br>

- $ deg(v) \vert 2 \ \ \ \forall v \in V \implies G \text{ admits and eulerian circuit}$

    Lets observe that we can consider a connected subgraph of $G'$ so we can assume without ambiguity that $G$ is connected. 
    
    Then, if $G$ is connected and each $v \in V$ verifies $deg(v)\vert 2$, let see that if we consider a path $P_r$ starting in $r \in V$, then since $deg(v) \vert 2 \ \ \forall v \in V$ there are no leafs and we can't get stuck in any point and always can go thourgh a non-traversed edge until we reach the same starting point $r$. This means that we can consider the cycle $C_r = P_r,r$ of no repeated edges. If $C_r$ goes through every edge in $E$, then is an eulerian circuit, if not and there are still edges which have not been traversed.
    
    ![cycle1](/assets/images/Maths/DiscreteMath/cycle1.png)

    Let's suppose there are leaf edfes, again, since $G$ is connected then at least one vertex of the cycle is included on an non-traversed edge. Let's be this vertex $r$ again (since a cycle can be looped on any point, we can make this assumption without loosing generality) then, $r$ is connected to another vertex $t$ (which can be in the cycle or not) through an non-traversed edge $\Set{r,t}$, since $deg(t) \vert 2$, then we can ensure the existance of another non-traversed edge in which $t$ is included $\Set{t,l}$ (if not, by the logic described above, would be $deg(t)$ odd) let's see that applying the same logic than in the first cycle, this circuit eventually ends up in $r$ conforming another cycle of non-traversed edges that can be continued from the first cycle in an eulerian circuit.
    
    ![cycle2](/assets/images/Maths/DiscreteMath/cycle2.png) 
    
    This way, reaching this point, if no more non-traversed edges last, then we would finished, if not, then we can repeat the same steps into another cycle. 

    Thus this conditions are sufficent to ensure the existance of an eulerian circuit.

### 2.1.2. Directed graphs.


<br>

## 2.2. Basic Algebra: Rings and Fields.

## 2.3. Polynomies.

## 2.4. Discrete Probability.

# 3. Arithmetic Circuits.

## 3.1. Formal definition.

## 3.2. Arithmetic Circuits and Complexity Theory.

## 3.3. Arithmetic Circuits and Discrete Probability.