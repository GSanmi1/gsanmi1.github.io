---
layout: post
title: "Arithmetic Circuits."
subtitle: "Maths fundamentals in arithmetic circuits and appliances in ZKP."
date: 2026-02-06 09:00:00 +0000
categories: ['Fundamentals']
tags: ['ZKP', 'Maths']
author: German Sanmi
subject: logic-set-theory
lang: en
---

# 1. Introduction.

As we established in the [2.Boolean Formulas](https://gsanmi1.github.io/posts/2026/02/02/Boolean_Formulas/) post, any NP problem is Karp reducible to SAT, implying that any instance of an NP problem can be verified by verifying some certain SAT instance, this is; finding a valuation that makes a boolean circuit that models the problem True.

However, bits are very restricted; often a codification of an instance of a problem into a big, complex boolean structure is needed (barring some exceptions) which often leads to inefficient (in terms of space and time) computations as we saw in the examples of the post above. This is why *arithmetic circuits* are far preferable to use instead.

Conceptually, an arithmetic circuit is a system of equations that models a problem in NP. 

<br>

# 2. Prerequisites.

## 2.1. Discrete Math: Graphs and DAGs.

### 2.1.1. Undirected Graphs.

#### 2.1.1.1. Introduction.

*Graph Theory*; is the discipline of mathematics which deals with the study of discrete relational structures and their properties. Conceptually, a *graph* is the minimal object that captures “pairwise relationships” between abstract entities.

Formally, a **graph** (undirected graph) is the pair $G := (V,E)$ where:

- $V$ is a finite non-empty set whose elements are called *vertices*.
- $E \subseteq \binom{V}{2}$ and its elements are called *edges*.

<br>

There are several notions associtated with the idea of a *graph*:

- **Adjacency**: Two vertices $u,v \in V$ are said to be *adjacent*; $u \sim v \iff \Set{u,v} \in E$
- **Neighborhood**: The neighborhood of $v \in V$ is the set $N(v) = \Set{u \in V : v \sim u}$
- **Degree**: The number of adjacent vertices to a given one $v \in V$; $\text{deg}(v) = \vert N(v) \vert$
- **Subgraph** of $G$ is any set: $H := (V_H, E_H) : V_H \subseteq V \land E_H \subseteq E \ \cap \ \binom{V_H}{2}$

- **Induced subgraph**: $G[W] := (W, E \cap \binom{W}{2}): W \subseteq V$

<br>

Regarding a collection of adjacent vertices, we can talk about:

- **Walk**; a finite sequence of adjacent vertices: $v_0...,v_t: v_{i-1} \sim v_i \ \forall i \leq t \in \mathbb{N}$

- **Path** is a walk with all the vertices distinct: $v_0...,v_t:v_{i-1} \sim v_i \ \forall i \leq t \in \mathbb{N} \ \land \ v_i \neq v_j \ \ \forall i,j \in \mathbb{N}$

- **Cycle** is a walk $v_0,...,v_{t-1},v_0$ where $v_0,...,v_{t-1}$ is a path.

- **Connected Vertices**; Two vertices are said to be connected if one can reach the other through a path.

<br>

![walk_path_cycle](/assets/images/Maths/DiscreteMath/walk_path_cycle.png)

<br>

Relative to the state of the vertex in the graph we can talk about:

- **Connected graph**: Every pair of vertices are *connected* vertices.
- **Complete graph**: Every pair of vertices are *adjacent*. They are notated simply as $K_n :=(V,E): \vert V \vert = n$ and satisfies: $u  \sim v \ \ \forall u,v \in V$
- **Tree**: A connected graph with no cycles.



#### 2.1.1.2. Tree characterization.

Let's consider a tree $T:=(V,E)$:

<br>

![tree](/assets/images/Maths/DiscreteMath/tree.png)

<br>

##### 2.1.1.2.1. Leaf lemma.

“Leaf lemma” refers to a basic fact in graph theory about *trees*. A tree is “all branches, no cycles”. If it has at least one edge, you can’t keep walking forever without either repeating a vertex (which would create a cycle) or getting stuck. The “stuck points” at the ends are leaves, and you must have at least two ends.

We define as $L := \Set{v \in V : \vert N(v) \vert = 1}$ the set of the leaves of $T$, then: 

$$\vert V \vert \geq 2 \implies \vert L \vert \geq 2$$

Basically the statement says that in any tree there are at least 2 leaves. 

Let's reason by the longest path. Be $T:=(V,E) : \vert V \vert \geq 2$ a tree; since $T$ is connected we can consider for $l,t \in V$ the path between them, so let's consider by convenience the longest path in $T$, $P_{lt}:=v_0,...,v_k$.

Now consider $v_0$ (we could reason the same way for $v_k$), and let's suppose that $\vert N(v_0) \vert \geq 2$; if it is, then we can consider some $u \in V : u \sim v_0 \land u \neq v_1$, then: 


- If $u \in P \implies C_u:= u,...,v_0,v_1,u \subset T$ contradicting the acyclicness property.
- If $u \notin P$, then $P' = u,v_0,...,v_k$ would be the longest path contradicting the maximality assumption of $P$.

So $deg(v_0) = deg(v_k) = 1$ and both are leaves in $T$.


<br>

##### 2.1.1.2.2. Equivalences statements of Trees.

The following statements are equivalent for a tree $T:=(V,E)$

1. $T$ is **connected** and $\vert E \vert = \vert V \vert - 1$

    First, $T$ is connected by definition. Let's reason by induction.

    - $n = 2$: Consider $T:= (V,E) : V :=\Set{u,v}$. Since $T$ is connected, $u,v \in V$ are connected and thus adjacent; $u \sim v \implies E := \Set{\Set{u,v}} \implies \vert E \vert  = 1 = \vert V \vert - 1$

        <br>

    - Considered true for some $n$, then $T'$ is a tree verifying $\vert V' \vert = n + 1$
    
        Consider a leaf $t \in V' : \vert N(t) \vert = 1$ (by the leaf lemma, we can ensure its existence) and the induced graph:
        
        $$T:= (V,E) : \begin{cases} V = V' \setminus \Set{t} \\ E= E' \cap \binom{V' \setminus \Set{t}}{2}\end{cases}$$
        
        
        Observe that since $t$ is a leaf, then it is an endpoint for some path in $T$ and removing it does not break connectivity.
        
        Thus $T$ is a graph with $n$ vertices and, by $T'$ and the leaf lemma, still connected and acyclic, meaning it remains a tree. Thus $T,T'$ are two trees verifying: $\vert E \vert = n - 1 \land V' = V \cup \Set{t}$

        Let's also observe that:

        $$ E= E' \cap \binom{V' \setminus \Set{t}}{2} = E' \setminus \Set{\Set{l,t} \in E' : l \in V'}$$
        Thus, we have:
        
        $$\vert E' \vert = \vert E\vert + \vert \Set{\Set{l,t} \in E': l \in V'} \vert = (n - 1) + 1 = \vert V' \vert-1$$

        <br>

2. $T$ is **acyclic** and $\vert E \vert = \vert V \vert - 1$. Is immediate from above.

    <br>

3. **Between any two vertices there is a unique path**. Reasoning by contradiction, if between $l,t \in V$ there would exist more than one path, let's say: $t,u_0,...,u_{k-1},l$ and $l,v_0,...,v_{k-1},t$, then $t,u_0,...,u_{k-1},l,v_0,...,v_k{-1},t$ would be a cycle contradicting acyclicity in trees.

    <br>

4. $T$ is **minimally connected**: removing any edge disconnects it.

    Observe that this stems from the uniqueness of the path for any pair of vertices. Meaning that, if $e=\Set{u,v} \in E$, then there exists a *unique* path $P = t,...,u,v,...l$ in $T$ and removing $e$ from $E$ leaves no path between $u$ and $v$, contradicting the connectedness premise on $T$ as a tree.

    <br>

5. $T$ is **maximally acyclic**: adding any missing edge creates a cycle.

    Let's consider $u,v \in V : u \ \cancel{\sim} \ v$, then, since $T$ is connected, exists a path $u,...,v \in T$ and forcing $\Set{u,v} \in E \implies C_u = u,...v,u \subset T$ contradicting acyclicness.

    <br>

##### 2.1.1.2.3. Handshaking lemma for trees.

The *handshaking lemma* states: 

$$\sum_{v \in V} deg(v) = 2 \vert E \vert$$

Let's see that we can prove this by induction:

- Consider: $\vert V \vert = 2 \implies \displaystyle\sum_{v \in V} deg(v) = 2 = 2 \vert E \vert$
- Consider now $\vert V \vert = n+1$, then we can consider by the leaf lemma $t \in V: deg(t) =1$:

    $$ T' :=(V',E'): \begin{cases} V' = V \setminus \set{t} \\ E' = E \cap \binom{V'}{2}\end{cases}$$

    Let's observe that $T'$ is a tree with $n$ vertices, then, by the induction premise $\displaystyle\sum_{v \in V'} deg(v) = 2 \vert E' \vert$, and also, being $u \in V : u \sim t$, then $E = E' \cup \Set{u,t}$ meaning that:

    $$ \sum_{v \in V} deg(v) = \sum_{v \in V'} deg(v) + 2 = 2 \vert E' \vert + 2 = 2(\vert E' \vert + 1) = 2\vert E \vert$$

<br>

Observe that this also means that there is an even number of odd-degrees.

<br>

#### 2.1.1.3. Eulerian and Hamiltonian graphs.

*Eulerian graphs* are a class of graphs that can be traversed using each edge exactly once. *Hamiltonian graphs* are a class of graphs that can be traversed using each vertex exactly once.

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

First, let's see that if $G$:

- $G \text{ is eulerian } \implies  deg(v) \vert 2 \ \ \ \forall v \in V$

    If we consider $G:=(V,E)$ connected that admits an eulerian circuit, then we can think of a walk that traverses every edge without repeating any of them.

    Thus, for the walk not to repeat edges and to end in the same vertex it started, for every vertex $v \in V$ which is not the start of the walk there are at least two edges; one that enters $\Set{u,v}$ and another that gets out from $\Set{v,w}$, for every time the walk visits a vertex in $V$ (this also applies whenever the vertex gets repeated in the walk).
    
    Also, if $r \in V$ is the root vertex from which the walk starts, then if this vertex gets visited more than once the rule above applies, and it also has the first edge from which the walk starts and the last edge of the walk that ends returning to $r$.
    
    So any $v \in V$ is adjacent to an even number of vertices and thus $deg(v) \vert 2$.

<br>

- $ deg(v) \vert 2 \ \ \ \forall v \in V \implies G \text{ admits an eulerian circuit}$

    Let's observe that we can consider a connected subgraph $G'$ so we can assume without ambiguity that $G$ is connected. 
    
    Then, if $G$ is connected and each $v \in V$ verifies $deg(v)\vert 2$, let's see that if we consider a path $P_r$ starting in $r \in V$, then since $deg(v) \vert 2 \ \ \forall v \in V$ there are no leaves and we can't get stuck at any point and can always go through a non-traversed edge until we reach the same starting point $r$. This means that we can consider the cycle $C_r = P_r,r$ of no repeated edges. If $C_r$ goes through every edge in $E$, then it is an eulerian circuit; if not, there are still edges which have not been traversed.

    Let's suppose there are leaf edges; again, since $G$ is connected then at least one vertex of the cycle is included in a non-traversed edge. Let this vertex be $r$ again (since a cycle can be looped on any point, we can make this assumption without losing generality), then $r$ is connected to another vertex $t$ (which can be in the cycle or not) through a non-traversed edge $\Set{r,t}$; since $deg(t) \vert 2$, then we can ensure the existence of another non-traversed edge in which $t$ is included $\Set{t,l}$ (if not, by the logic described above, $deg(t)$ would be odd). Let's see that applying the same logic as in the first cycle, this circuit eventually ends up in $r$, forming another cycle of non-traversed edges that can be continued from the first cycle in an eulerian circuit.
    
    ![cycle1](/assets/images/Maths/DiscreteMath/cycle1.png)

    This way, reaching this point, if no more non-traversed edges remain, then we would be finished; if not, then we can repeat the same steps into another cycle. 
    
    The point is to understand that, whenever there exists a vertex involved in a non-traversed edge, by the features of the graph, this edge goes on in a path with other non-traversed edges that eventually ends up again in the same starting vertex; thus our eulerian circuit is a walk that goes through a main cycle and completes subcycles when the accesses to these ones are presented.

    ![EulerianCircuit](/assets/images/Maths/DiscreteMath/EulerianCircuit.png)

    In the example above, we would start our walk in $r$, then $e:=r,c_2,t$ and in $t$ we enter a subcycle $C_t:=t,l,c_7,r,t$, thus $e:=r,c_2,C_t$.

    Now we continue our walk through the main cycle until we reach $c_4$ in which we get another subcycle: $C_c:= c_4,c_{41},c_{42},c_4$, thus $e:=r,c_2,C_t,C_c$ and we finish our main cycle. Our eulerian circuit will look like:

    $$e:=r,c_2,C_t,C_c,l,c_6,c_7,c_8,r$$

    Thus these conditions are sufficient to ensure the existence of an eulerian circuit.

    <br>

Now, taking $G:=(V,E)$ as a connected graph:

$$G \text{ is semi-eulerian } \iff \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$$

- Let's see first that $ \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2 \implies G \text{ is semi-eulerian }$

    In the terms of in/out, having two unique vertices $u,v \in V$ with an odd-degree means that these two vertices are endpoints, in the sense that you can depart from but never finish back (despite walk iterations over the same vertex), or you can get in but never get out through a non-traversed edge; any of the two cases would imply an even degree.

    Thus, let's consider $P_{uv}$, this is our main walk; if this path covers all edges in $E$, then we would be finished. If not, let's see that we already took in $P_{uv}$ the odd adjacencies, in the sense that, out of $P$, every non-traversed edge involves vertices with an even degree value like in our eulerian graph in the example above. Every non-traversed edge out of $P$, let's say $\Set{t,l}$, continues over another non-traversed edge until the starting point $t$ is met, completing a cycle. 

    This in conjunction with the fact that $G$ is connected (meaning that if there are non-traversed edges by $P$ these can be reachable through $P$; at least one of those non-traversed edges involves a vertex in $P$) makes our eulerian trail a walk that goes through $P_{uv}$ from $u$, completing subcycles whenever these are presented, ending up in $v$.

    <br>

- Now, check that: $G \text{ is semi-eulerian } \implies \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$

    If $G$ is semi-eulerian, then it admits an eulerian trail. Thus, necessarily it is connected because in a single walk we can traverse all edges, meaning that all vertices are connected. 

    Also, this trail starts and ends in two distinct points $u,v \in V$. These are the departure point and the arrival point, and thus these ones have odd-degrees as we said above. Also, any other vertex in $V$ has in/out edges (despite iterations over the trail) meaning that they have even degree. Thus, $\vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$ 

    <br>

##### 2.1.1.3.2. Hamiltonian graphs. Main theorem.

**Main notions and definitions**

Being $G:=(V,E)$ a graph. Then we have the following definitions:

- A *Hamiltonian path*, $P_{H,uv}$ is a path that visits every vertex $t \in V$ exactly once.

- A *Hamiltonian cycle*, $C_u$ is a cycle formed through a Hamiltonian path,$P_{H,uv}$ meaning that it visits every vertex exactly once with the exception of the starting point: $C_u := P_{H,uv},u$

We say that $G$ is Hamiltonian if it admits a *hamiltonian cycle*.

<br>

**Implications (NOT Characterization)**

Being $G:=(V,E)$ a hamiltonian graph, then:

- **$G$ is connected**; If every single vertex is contained in a path, then for every pair of vertices there exists a path that contains those vertices so $G$ is connected.

- **$deg(v) \geq 2 \ \ \forall v \in V$**. If the graph admits a hamiltonian cycle, then there exists a cycle that traverses all the vertices returning to the starting point, meaning that all vertices $v \in V$ have an in/out edge, thus it is at least two although it can be more, thus $deg(v) \geq 2$.

- **There are no "cut-vertices"**. Meaning that removing one vertex does not disconnect the graph, because removing a vertex causes the hamiltonian cycle to derive into a hamiltonian path, thus all vertices remain connected:

    ![hamiltonian1](/assets/images/Maths/DiscreteMath/hamiltonian1.png)

    <br>

**Ore's premise and some immediate results**

Ore's premise says something like “if the graph is dense enough, it must be Hamiltonian”: 

$H:=(V,E) : \big( \vert V \vert \geq 3 \wedge deg(u) + deg(v) \geq \vert V \vert \ \forall u,v \in V : u \not \sim v\big) \implies H \text{ is Hamiltonian}$

<br>

Let's start by seeing that $H$, as defined, is connected. Being $u,v \in V$, then consider $P_u := \Set{v \in V \vert \exists P_{uv} \subset H}$, 

Observe that: $\nexists P_{uv} \text{ in } H \implies \ P_u \cap P_v = \varnothing \implies \vert P_u \cup P_v \vert = \vert P_u \vert + \vert P_v \vert \leq \vert V \vert$. 

$$deg(t) + deg(l) \leq \vert P_u \vert -1 + \vert P_v \vert -1 = \vert V \vert - 2 < \vert V \vert \ \ \ \forall t \in P_u \wedge \forall l \in P_v$$

Observe that obviously $t \not \sim l$ .

This contradicts Ore's initial presumption on $H$, so $H$ is connected and we can safely think of a path for any pair of vertices in $V$.

<br>

Let's also observe that $deg(v) \geq 2 \ \ \forall v \in V$. If $H$ is a complete graph then there is nothing to prove, so let's suppose that:

$$\exists u,v \in V: u \not \sim v \wedge deg(v) =1 \implies deg(u) + deg(v) = deg(u) + 1 \geq \vert V \vert \implies deg(u) \geq \vert V  \vert - 1$$

Also, since $\vert V \vert > deg(u) \wedge deg(u) \in  \mathbb{N} \implies deg(u) = \vert V \vert -1$

This would mean that $N(u) = V \setminus \Set{u} \implies v \in N(u) \implies u \sim v$ contradicting the no adjacency premise. So there are no leaves in $H$.

<br>

Let's also observe that in $H$:

$$N(v) \cap N(u) \neq \varnothing \wedge \vert N(v) \cap N(u) \vert \geq 2 \ \ \forall u,v \in V: u \not \sim v $$

Note that $u \not \sim v \implies \Big(deg(v) + deg(u) = \vert N(u) \vert + \vert N(v) \vert \geq \vert V \vert \Big) \wedge \Big( N(u) \cup N(v) \subset V \setminus \Set{u,v}\Big)$

Then applying $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$, and $deg(u) + deg(v) \geq \vert V \vert$ is: 

$$\vert V \vert -2 \geq \vert N(v) \cup N(u) \vert = \vert N(u) \vert +  \vert N(v) \vert - \vert N(u) \cap N(v) \vert \geq \vert V \vert - \vert N(u) \cap N(v) \vert $$

Meaning that $\vert N(u) \cap N(v) \vert \geq 2$ necessarily. Then, $\exists t,l \in V : t,l \in  N(u) \cap N(v) \ \ \forall u,v \in V: u \not \sim v$.

<br>

**Bondy-Chvátal Lemma**

Being $G:=(V,E) : \vert V \vert = n \geq 3 \wedge deg(u) + deg(v) \geq n$, then we define $G + uv :=(V,E \cup \Set{u,v})$, observe that obviously: $u \sim v \text{ in } G \implies G = G +uv$. 

This lemma stands that:

$$ G \text{ is hamiltonian } \iff G + uv \text{ is hamiltonian }$$

Let's prove the lemma.

- Observe quickly that $ G \text{ is hamiltonian } \implies G + uv \text{ is hamiltonian }$, since adding edges (supposing $u \not \sim v$) does not destroy cycles.

- If $G + uv \text{ is hamiltonian }$, then if the cycle does not use $\Set{u,v}$ then $G \text{ is hamiltonian }$, thus let's suppose that the cycle does use $\Set{u,v}$.

    Consider the hamiltonian path $P_{H,uv} \subset G$ (which exists since $G + uv$ is hamiltonian and the hamiltonian cycle does use $\Set{u,v} \in E$). If we consider that $A:=\Set{i \in \Set{2,...,n}: v_i \sim u} \wedge B:=\Set{i \in \Set{1,...,n-i}: v_i \sim v}$ then, obviously $A$ and $B$ are the sets of the neighbours shifted by one relative to the other; let's observe that, as we discussed before: 
    
    $$N(u) \cap N(v) \neq \varnothing \implies A - 1 := \Set{i-1: i \in A}\cap B \neq \varnothing \implies \exists i: u \sim v_{i-1} \wedge v_i \sim v$$

    Thus, taking a redirection of the path: $P:=u,...,v_{i-1},v,...,v_i,u$, we have our hamiltonian cycle.

    ![Bondy_Chvatal](/assets/images/Maths/DiscreteMath/Bondy_Chvatal.png)

    The image above aims to illustrate the result of the lemma; for simplicity, unnecessary edges have been omitted.

    <br>

**Ore's theorem**

Let's observe that, from the result before, Ore's premise guarantees $G \text{ is hamiltonian } \iff G + uv \text{ is hamiltonian }$, and this premise can be applied iteratively, meaning:

$$G \text{ is hamiltonian} \iff G + uv \text{ is hamiltonian}\iff (G + uv) + lt\text{ is hamiltonian} \iff \cdots \iff K_n\text{ is hamiltonian}$$

Observe we eventually reach a complete graph since $V$ is finite and so is the number of edges that can be included. 


<br>

**Dirac's theorem**

Let's observe that there is another direct result that can be derived from Ore's theorem. Being $G:=(V,E) : \vert V \vert = n \geq 3$, then:

$$deg(v) \geq \frac{n}{2} \ \ \forall v \in V \implies deg(v) + deg(u) \geq n \ \ \forall u,v \in V : u \not \sim v$$

Thus, we can say that:

$$deg(v) \geq \left\lceil \frac{n}{2}\right\rceil \quad \forall v \in V \implies G \text{ is Hamiltonian }$$

Being $\displaystyle\left\lceil \frac{n}{2}\right\rceil \quad := min \Set{z \in \mathbb{Z} \ \vert \ z \geq \frac{n}{2}}$ 

<br>

##### 2.1.1.3.3. Relation.

Eulerian cares about degree parity and edge coverage; Hamiltonian cares about global structure and vertex coverage. 

Eulerian existence has a clean parity characterization. Hamiltonian existence does not have a comparable local invariant characterization; deciding Hamiltonicity is [$NP$-complete](https://gsanmi1.github.io/posts/2026/02/02/Boolean_Formulas/) (even for many restricted graph families).

<br>

#### 2.1.1.4. Graph coloring.

Being, $G := (V,E)$, then a $k\text{-coloring}$ of $G$ is an application:

$$c : V \to \Set{1,...,k} : \forall \Set{u,v} \in E \ \ c(u)  \neq c(v)$$

For $G$, we define his **chromatic number** as the minimum number for which exists a coloration:

$$\chi(G) := min\Set{k | \exists c : V \to \Set{1,...,k} \text{ is a } k\text{-coloring}}$$

Observe that this means that the Four Colour theorem states $\chi(G) \leq 4 \ \ \forall G$ and the 3-coloring problem asks whether $\chi(G) \leq 3$.

<br>

Let's observe that:

1. For a complete graph $K_n$ (where $\vert V_K\vert  = n$), is: $\chi(K_n) = n$.

    - First, let's see that $c : V_K \to \Set{1,...,n}$ is *injective* ($\vert V_K\vert  = \vert \Set{1,...,n}\vert $) and it verifies:

        $$\forall u,v \in V_K : u \neq v \implies c(u) \neq c(v)$$

        Also, since $K_n$ is a complete graph, $\forall u,v \in V_K : u \neq v \iff \Set{u,v} \in E_K$, thus:

        $$\forall \Set{u,v} \in E_K \ \  c(u) \neq c(v)$$

        And $c$ is a coloration.

        <br>

    - Let's see now that $\neg (\exists i < n : c : V_K \to \Set{1,...,i} \text{ is a coloration})$.

        Simply, considering $c : V_K \to \Set{1,...,i}$ with $ i < n$, then $c$ is *not injective* and it verifies the *pigeonhole principle*:

        $$\exists u,v \in V_K : u \neq v \land c(u) = c(v)$$

        Again, for $\forall u,v \in K_n \ \ u \neq v \iff \Set{u,v} \in E_K$ and thus:

        $$\exists \Set{u,v} \in E_K : c(u) = c(v)$$

        And $c$ is not a coloration.

        <br>

2. For a cycle $C_n$, $\chi(C_n) = 2$ if $n$ is even and $\chi(C_n) = 3$ if $n$ is odd.

    First, let's define what a cycle graph is: 
    
    $$C_n := (V_C, E_C) : \begin{cases} V_C = \Set{v_0,...,v_{n-1}} \\ E_C = \Set{\Set{v_{i-1},v_i} : i \in \Set{1,...,n-1}} \cup \Set{\Set{v_{n-1},v_0}} \end{cases}$$

    Let's observe that, as defined, the sequence: $v_0,...,v_{n-1}$ is a path, thus $v_0,...,v_{n-1},v_0$ is a cycle.

    - Now, consider the case $\exists m : n = 2m$, then, we define:

        $$c : V_C \to \Set{1,2} : c(v_i) = \begin{cases}  1 \ \text{ if } i  \text{ is even}\\ 2 \ \text{ if } i  \text{ is odd} \end{cases}$$

        It is clear that even and odd numbers alternate in a consecutive numeric sequence. So:

        $$c(v_{i-1}) \neq c(v_i) \ \ \forall v_{i-1},v_i \in v_0,...,v_{n-1} \implies c(v_{i-1}) \neq c(v_i) \ \ \forall \Set{v_{i-1},v_i} \in E_C $$

        For the same reason, if $n$ is even, then $n-1$ is odd and $c(v_{n-1}) \neq c(v_0)$, thus, in conclusion:

        $$c(u) \neq c(v)  \ \ \forall \Set{u,v} \in E_C$$

        And $c$ is a $2-coloring$ of $C_n$. Obviously since $E_C \neq \varnothing$ it can't be $\chi(C_n) = 1$.

        <br>

    - If $n = 2m + 1$ and we suppose the existence of a $2-coloring$, $c$ over $C_n$, then: 

        $$c(u) \neq c(v) \ \ \forall \Set{u,v} \in E_C \implies c(v_{i-1}) \neq c(v_i) \ \ \forall \Set{v_{i-1},v_i} \in E_C \iff$$
        $$ \iff c(v_{i-1}) \neq c(v_i) \ \ \forall v_{i-1},v_i \in v_0,...,v_{n-1}$$

        Or, in other words, any consecutive vertex in the path $v_0,...,v_{n-1}$ has different image under $c$. 
        
        Thus, it is easy to see that:
        
        - Since in a $2-coloring$ there are only two possible image values 
        
        - And $n-1$ is even (because $n$ is odd), 
        
        Then $v_0$ and $v_{n-1}$ share the same image under $c$ and it is:
        
        $$c(v_{n-1}) = c(v_0) \land \Set{v_{n-1},v_0} \in E_C$$
        
        Triggering a contradiction with the $2-coloring$ requirement.

        Getting the example of $c$ provided above, it is easy to see that:

        $$c : V_c \to \Set{1,2,3} : c(v_i) = \begin{cases}  1 \ \text{ if } i  \text{ is even } \land i \neq n -1\\ 2 \ \text{ if } i  \text{ is odd} \\  3 \end{cases}$$

        Is a $3-coloring$ of $C_n$.

        <br>

3. **Bipartite Graphs**.

    A bipartite graph is a graph $G_B$ satisfying:

    $$G_B := (V_B,E_B): \begin{cases}V_B := A \sqcup B \ \ (V = A\cup B \land A \cap B = \varnothing) \\ E_B \subset \binom{V_B}{2} : a \in A \land b \in B \ \ \forall \Set{a,b} \in E_B \end{cases}$$

    Then, consider 
    
    $$c : V_B \to \Set{1,2} : c(v) =\begin{cases}  1 \ \ \text{ if } v \in A\\ 2 \ \ \text{ if } v \in B \end{cases}$$

    Then:

    $$\forall \Set{u,v} \in E_B \ \  \begin{cases} u \in A  \Rightarrow c(u) = 1 \\ v \in B \Rightarrow c(v) = 2 \end{cases} \implies c(u) \neq c(v)$$

    And $c$ is a $2-coloring$ of $G_B$. Of course, $E_B \neq \varnothing \implies \chi(G_B) \neq 1$.

    <br>

4. **2-colorability theorem**.

    The 2-colorability characterization states that, being $G := (V,E)$ a graph, then:

    $$\chi(G)=2 \iff G \text{ is bipartite } \iff \neg \exists\,\text{cycle } C \subseteq G : |C|\ \text{ is odd} $$

    Observe that we already demonstrated that:

    - $G \text{ is bipartite } \implies \chi(G)=2$
    - $\chi(G)=2 \implies \neg \exists\,\text{cycle } C \subseteq G : \vert C\vert \ \text{ is odd}$ (since every odd cycle has 3 as a chromatic number).
    - $\chi(G)=2 \implies G \text{ is bipartite }$

       Observe that

        $$\chi(G)=2 \implies \exists c :V \to \Set{1,2} : c(u) \neq c(v) \ \ \forall \set{u,v} \in E$$

        We define: 

        $$\begin{cases}A := \Set{u \in V | c(u) = 1} \\ B:= \Set{u \in V | c(u) = 2}\end{cases}$$

        In this context, since $c$ is an application we have:

        - $v \in V \Rightarrow c(v) = 1 \vee c(v) =2 \Leftrightarrow v \in A \vee v \in B \Rightarrow V = A \cup B$

        - $A \cap B = \varnothing$

        - $\forall \Set{u,v} \in E \implies c(u) \neq c(v) \implies  (u \in A \land v \in B) \vee (v \in A \land u \in B)$

        <br>

        Thus, $G$ verifies:
        $$\begin{cases}V := A \sqcup B \ \ (V = A\cup B \land A \cap B = \varnothing) \\ E \subset \binom{V}{2} : a \in A \land b \in B \ \ \forall \Set{a,b} \in E \end{cases}$$

    Now, only last to demonstrate that:

    - $\neg \exists\,\text{cycle } C \subseteq G : \vert C\vert \ \text{ is odd} \implies G$ is bipartite. 

        The premise can be negated in two ways:

        - First, $\neg \exists C \subseteq G : C \text{ is a cycle}$, then consider a vertex we call $r$ and: $A = \Set{u \vert  dist(r,u) \text{ is even}}$ and $B = \Set{u \vert  dist(r,u) \text{ is odd}}$. Then it is pretty obvious that $A \cup B$ and we impose that $A \cap B = \varnothing$; let's observe that this imposition requires no odd cycles.

            Being $C \subseteq G : C \text{ is odd}$, then, $C:=v_0,...,v_{n-1},v_0$ where $v_0,...,v_{n-1}$ is a path and $\Set{v_{n-1},v_0} \in E$. Let's say $r : dist(r,v_0) \land r \notin C$. Then, since $C$ is a cycle there are two paths to measure the distance between $r$ and $v_{n-1}$:

            $$dist(r,v_{n-1}) = dist(r,v_0) + dist(v_0,v_{n-1})$$

            Since $\Set{v_{n-1},v_0} \in E \Rightarrow dist(v_0,v_{n-1}) = 1 \Rightarrow dist(r,v_{n-1}) = 2 \text{ (even)}$, but also, since $C$ is odd, $n-1$ is even (meaning that $dist(v_0,v_{n-1})$ is even and $1 + dist(v_0,v_{n-1}) = dist(r,v_{n-1})$ is odd). So in summary: $A \cap B \neq \varnothing$

           <br>

#### 2.1.1.5. Planar graphs. Drawings and faces. Euler's formula.

A *planar graph* is a graph that admits a graphical representation on a plane such that its edges do not cross each other. For example, the complete graph $K_3$ does admit a representation in which the edges do not cross, but $K_5$ does not.

Let be $G:=(V,E)$ a finite simple graph, then an embedding of $G$ into $\mathbb{R}^2$ is a function $\phi: G \to \mathbb{R}^2$ that:

- $\forall u,v \in V \ \ \left(\phi(u), \phi(v) \in \mathbb{R}^2 \land u \neq v \implies \phi(u) \neq \phi(v) \right)$

- $\forall e, f \in E \ \ \left( \phi(e) = \gamma_{e_1e_2}, \phi(f) = \gamma_{f_1f_2}  \in \mathbb{R}^2 : e \neq f \implies \phi(e) \cap \phi(f) \subseteq \Set{\phi(e_1),\phi(e_2),\phi(f_1),\phi(f_2)} \right)$


Where $\gamma_{uv}$ is a simple arc (non-self-intersecting, continuous curve) from $\phi(u)$ to $\phi(v)$. $\phi$ maps the edges of $G$ ensuring that two different arcs only share endpoints as much.

Then, $G$ is said to be planar if it admits an embedding $\phi$ in $\mathbb{R}^2$ as above.

<br>

Associated with a drawing of a planar graph are the so-called *faces*, grouped in the set $F$; which are regions of the plane $\mathbb{R}^2$ enclosed by the planar drawing of the graph (here the unbounded outer face external to the graph is included). Euler's formula specifies that, for a connected planar graph $G:= (V,E)$, being $F$ the set of the faces of the drawn graph, then:

$$|V| - |E| + |F| = 2$$

<br>

#### 2.1.1.6. Dual graphs.

Given a connected planar graph $G$, the *dual graph* is what you get when you turn faces into vertices in a planar embedding of $G$. 

The drawing (planar embedding) cuts the plane into regions (faces), one unbounded “outside” face plus the bounded ones, then the dual $G^*$ is built by:

- Putting one vertex inside each face of $G$.
- For each $e \in E$ there exists one $e^* \in E^*$ crossing once $e$, connecting two faces.

Formally;

Being $G$ a connected planar graph and $\phi$ its drawing in $\mathbb{R}^2$. Then, we define the dual graph as:

$$G^*:= (V^*,E^*):\begin{cases}V^* &:= F = \Set{f : f \text{ is a face of }(G,\phi)} \\ E^* &:= \Set{\Set{f_1,f_2} | \exists e \in E \text{ between } f_1 \text{ and } f_2 } \subseteq \binom{V^*}{2}\end{cases}$$

It is important to understand that *the dual depends on the embedding*: Two different planar drawings of the same abstract planar graph can produce non-isomorphic duals. The dual is canonical only after you fix the embedding.

In this context, a map coloring is equal to coloring a dual graph. A map representation is in fact a dual graph.

<br>

### 2.1.2. Directed graphs.

A *directed acyclic graph* (DAG) is a directed graph that encodes a *one-way dependency* or *precedence relation*; *causality* with no circularity.

As an example, being $u,v$ two predicates related as $u \to v$, then a DAG would represent this relation by an arrow of $u$ to $v$ meaning that $v$ depends on $u$ (or $u$ must happen before $v$). 

Thus, DAGs are a way to abstract implication relationships between multiple agents in a discrete relational structure.

<br>

#### 2.1.2.1. Formal Definition.

A directed graph gets defined as a pair: $D:= (V,E)$, where:

- $V$ is a finite set of elements.
- $E \subseteq V^2$ is a set of ordered pairs.
<br>

#### 2.1.2.2. Main notions.

**Impliance**

The first main notion we want to introduce is how the vertices (which are maintained from the simple graph conception) get related in a directed graph.

Being $G:=(V,E)$ a graph, then $E \subseteq \binom{V}{2}$ is the set of edges $\Set{u,v} \in E$ and we say that $u,v \in V$ are adjacent $u \sim v \iff \Set{u,v} \in E$. This is how two elements get related in the simple graph conception. $\Set{u,v}$, as a simple set, doesn't care about order so the relation is bidirectional, $u$ is adjacent to $v$ exactly as $v$ is adjacent back to $u$.

In the directional conception, there is no adjacency but impliance and this relation gets formalized through ordered sets. Remember that $D := (V,E)$ is a directed graph when $E \subseteq V^2$ meaning that the elements of $E$ are pairs $(u,v)$. In this context, we introduce the notion of *impliance*.

Being $u,v \in V$ then we say $u$ implies $v$, $u \to v \iff (u,v) \in E$. We can also say that $u$ precedes $v$. 

Note that this relation is not reciprocal, $u \to v \not \Rightarrow v \to u$

<br>

**In/Out neighborhood**

Based on the notion of impliance defined before as a substitute for the adjacency in directed graphs, we consider the following sets:

- *In-neighborhood*; $N^{+}(u)=\{\,v\in V : u\to v\,\}$
- *Out-neighborhood*; $N^{-}(u)=\{\,v\in V : v\to u\,\}$

These are nothing but the parallel concept of neighbourhood in simple graphs $N(v) := \Set{u \ \vert \ u \sim v }$ but based on the order of the impliance.

Also, we can consider the following numbers:

- The *out-degree* to the number: $deg^+(v) := \vert N^{+}(v) \vert$
- The *in-degree* to the number: $deg^-(v) := \vert N^{-}(u) \vert$

<br>

**Implicated vertex structures.**

- **Directed Walk**; is a sequence $(v_0,...,v_k) : v_{i-1} \to v_i \ \ \forall i \in [k] \wedge k \in \mathbb{N}$

- **Directed Path**; is a directed walk with all vertices distinct.

- **Directed Cycle**; is a directed walk $(v_0,...,v_k,v_0) : (v_0,...,v_k)$ is a path.

![direct_structures](/assets/images/Maths/DiscreteMath/direct_structures.png)

<br>

#### 2.1.2.3. Directed Acyclic Graphs (DAGs).

A Directed Acyclic Graph (DAG) is a directed graph with no cycles.

<br>

##### 2.1.2.3.1. Definition. Sources and sinks.

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

- First, these two vertices do exist, but are the same $\exists u,v\in V : \big(deg^-(u)=deg^+(v)=0 \wedge u = v \big)$, then $u$ is an isolated vertex contradicting connection in $D$.

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

##### 2.1.2.3.2. Order in DAGs.

######  2.1.2.3.2.1. Order definition.

**Binary Relations and Orders.**

Given a set $X$, a binary relation on $X$ is a subset: $R \subseteq X \times X$ and we write as a shorthand, being $x,y \in X$, then:

$$xRy \iff (x,y) \in R$$

We call $R$ an order, and, defined under certain conditions, we abstract the idea that $x$ precedes $y$ through $R$ and we represent it such as $(x,y) \in R$

Then, any binary relation $R$ must satisfy the following three conditions to be called an *order*:

- **Reflexive**: $xRx \ \ \forall x \in X$
- **Transitive**: $xRy \wedge yRz \implies xRz \ \ \forall x,y,z \in X$
- **Antisymmetric**: $xRy \wedge yRx \implies x = y \ \ \forall x,y \in X$

<br>

**Partial and Total Order**

When we define a binary relation $R$ over a set $X$ then it is pertinent to ask if:

$$xRy \vee yRx \ \ \ \forall x,y \in R$$

If $x$ and $y$ are incomparable then we write:

$$\neg(xRy) \wedge \neg (yRx) \iff x \ \vert \vert \ y$$

We say that $R$ defined in $X$ is: 

$$R \text{ is a partial order } \iff \exists x,y \in X : x \ \vert \vert \ y$$
$$R \text{ is a total order } \iff xRy \vee yRx \ \ \ \forall x,y \in R$$

<br>

**Strict and non-strict order**

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

**Partial Order in DAGs**

Consider $D$ a $DAG$, then, we can define the following subset 

$$\preceq  \ \subseteq V^2: x \preceq y \longleftrightarrow \exists \text{ a directed path } P_{xy} \ (x \rightsquigarrow y)$$

Observe that this relation is an order since:

- *Reflexive*: $v \preceq v \ \ \forall v \in V$ since $(v,v) \in E$
- *Transitive*: $v \preceq u \wedge u \preceq w \implies P_{vw} = P_{vu},P_{uw} \implies v \preceq w$
- *Antisymmetric*: $v \preceq u \wedge u \preceq v \implies u = v$ since no cycles are allowed.

Observe that the *reflexive* property of $\preceq$ makes it automatically a non-strict order, and we define the strict variant of the partial order as: $\prec \ \subseteq \  V^2 : u \prec v \iff  u \preceq v \wedge u \neq v$. 
<br>

###### 2.1.2.3.2.2. Topological Order. Characterization of DAGs.

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

##### 2.1.2.3.3. Basic Properties in DAGs.

**Maximum number of edges**

Given a directed graph $D$ (no parallel edges) a $DAG$, since no cycles are allowed, then:

$$\neg \big((u,v) \in E \wedge (v,u) \in E\big) \ \ \forall u,v \in V$$

Meaning that for any unordered set $\Set{u,v}$ is at most $(u,v)$ or $(v,u)$ in $E$, meaning that:

$$ \vert E \vert \leq \vert \binom{V}{2} \vert = \binom{\vert V \vert}{2}$$

Meaning that at most one of the two (or none of the two) is present in $E$.

<br>

**Strongly connected components are trivial**

We call a strongly connected component a subgraph $S \subseteq D$ such that $S = K_n : n \leq \vert V \vert$. Obviously for $n \geq 3$, $S$ would allow a cycle, so in a $DAG$ any strongly connected component is reduced to a set of two connected vertices.

<br>

**Longest walks in DAGs**

In a DAG, the longest path $walk$ is $\vert P \vert \leq \vert V \vert -1$ since there can't be cycles; a walk cannot repeat vertices so paths and walks collapse in $DAGs$ and the longest possible walk has at most $\vert V \vert$ vertices or $\vert V \vert-1$ edges.

<br>

##### 2.1.2.3.4. Canonical constructions and theorems.

**Transitive Closure**

The *transitive closure* of a $DAG$, $D:=(V,E)$ is a digraph defined as follows: 

$$D^+:=(V,E'): (u,v) \in E' \iff u \rightsquigarrow_D v$$

This is what you get when you treat reachability as edges in a digraph, obtaining an extension of the impliance relation of the vertices of $D$ in the sense that in $D^+$ $u$ implies $v$ if there exists a chain of impliances from $u$ to $v$ in $D^+$.

<br>

**Transitive Reduction**

The transitive reduction of a $DAG$, $D$ is a minimally reachable version of the graph $R$ on the same vertex set, in the sense that removing an edge breaks the reachability of the graph.

$$R:=(V,E'): E' \subset E \wedge \big[(u,v) \in E \setminus E' \iff  \exists P_{uv} \subset D \setminus \Set{(u,v)} \big]$$

Let's observe that it is the opposite conception of the closure: while the closure saturates the implications on $D$, the *reduction* minimizes those same implications; both of them are variations of the number of connections in the graph maintaining the partial order relation $\preceq$ between the vertices.

<br>

##### 2.1.2.3.5. Algorithmic Consequences.

Until this point, we've seen that a $DAG$ is a dependency structure with no circular dependencies (cycles). No cycles allow us to evaluate/optimize/count and schedule things by a single forward/backward pass without backtracking.

Let's expand this idea. In general, computation consists of taking an object and operating with it in order to extract some value or conclusion, but objects can be dependent on each other, in the sense that often an object is the result of the computation of another object (like getting a point in a field is the result of solving a system of equations since the point must verify some constraints). This dependency can be illustrated in a directed graph $u \to v$.

Then, acyclicity in a directed graph means that you don't get circular dependencies (circular dependencies require computing simultaneously two dependent objects, which translates into complex operations or iteration until convergence). $DAGs$ avoid that; acyclicity turns global problems into local propagation. Observe that in some way this is reflected in the existence of the partial order $\preceq$ and the topological order which basically guarantee the transformation of a $DAG$ into a chain of implications.

<br>

## 2.2. Basic Algebra: Rings and Fields.

## 2.3. Polynomials.

## 2.4. Discrete Probability.

# 3. Arithmetic Circuits.

## 3.1. Formal definition.

## 3.2. Arithmetic Circuits and Complexity Theory.

## 3.3. Arithmetic Circuits and Discrete Probability.