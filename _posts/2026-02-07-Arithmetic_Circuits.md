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

    Let's suppose there are leaf edfes, again, since $G$ is connected then at least one vertex of the cycle is included on an non-traversed edge. Let's be this vertex $r$ again (since a cycle can be looped on any point, we can make this assumption without loosing generality) then, $r$ is connected to another vertex $t$ (which can be in the cycle or not) through an non-traversed edge $\Set{r,t}$, since $deg(t) \vert 2$, then we can ensure the existance of another non-traversed edge in which $t$ is included $\Set{t,l}$ (if not, by the logic described above, would be $deg(t)$ odd) let's see that applying the same logic than in the first cycle, this circuit eventually ends up in $r$ conforming another cycle of non-traversed edges that can be continued from the first cycle in an eulerian circuit.
    
    ![cycle1](/assets/images/Maths/DiscreteMath/cycle1.png)

    This way, reaching this point, if no more non-traversed edges last, then we would finished, if not, then we can repeat the same steps into another cycle. 
    
    The point is to understand that, whenever exists a vertex involved in an non-traversed edge, by the features of the graph, this edge goes on in a path with another non-traversed edges that eventually ends up again in the same started vertex, thus our eulerian circuit is a walk that goes through a main cycle and completes subcycles when the access to this ones are presented.

    ![EulerianCircuit](/assets/images/Maths/DiscreteMath/EulerianCircuit.png)

    In the example above, we wold start our walk in $r$, then $e:=r,c_2,t$ and in $t$ we entener in a subcycle $C_t:=t,l,c_7,r,t$, thus is $e:=r,c_2,C_t$.

    Now we continue our walk throught the maincycle until we reach $c_4$ in which we get another subcycle: $C_c:= c_4,c_{41},c_{42},c_4$ thus, $e:=r,c_2,C_t,C_c$ and we finish our main cycle. Our eulerian circuit will look as:

    $$e:=r,c_2,C_t,C_c,l,c_6,c_7,c_8,r$$

    Thus this conditions are sufficent to ensure the existance of an eulerian circuit.

    <br>

Now, taking $G:=(V,E)$ as a connected graph:

$$G \text{ is semi-eulerian } \iff \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$$

- Let's see first that $ \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2 \implies G \text{ is semi-eulerian }$

    In the terms of in/out, having two unique vertex $u,v \in V$ with an odd-degree mean that this two vertex are endpoints, in the sense that you can depart from but never finish back (despite walk iterations over the same vertex), or you can get in but never get out through a non-traversed edge, any of the two cases would implie an even degree.

    Thus, let's consider $P_{uv}$, this is our main walk, if this path covers all edges in $E$, then we would be finish. If not, lets see that we already take in $P_{uv}$ the odd adjacencies, in the sense that, out of $P$, every non-traversal edges involves vertex with an even degree value like in our eulerian graph in the example above. Every non-traversal edge out $P$, let's say $\Set{t,l}$ continues over another non-traversal edge until the starting point $t$ is meeted, completing a cycle. 

    This in conjuntion with the fact that $G$ is connected, (meaning that if there are non-traversed edges by $P$ this can be reachable through $P$; at least one of those non-traversed edges involves a vertex in $P$) makes our eulerian trail as a walk that goes through $P_{uv}$ from $u$, completing subcycles whenever this are presented, ending up in $v$.

    <br>

- Now, check that: $G \text{ is semi-eulerian } \implies \vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$

    If $G$ is semi-eulerian, then it admits an eulerian trail. Thus, necesarily is connected because in a single walk we can traverse all edges, meaning that all vertex are connected. 

    Also, this trail starts and end in two distinct points $u,v \in V$. This are the depart point and the arrival points, and thus this ones have odd-degrees as we said above. Also, any other vertex in $V$ have an in/out edges (despite iterations over the trial) meaning that they have even degree. Thus, $\vert \{x \in V : \deg(x)\ \text{odd}\} \vert = 2$ 

    <br>

##### 2.1.1.3.2. Hamiltonian graphs. Main theorem.

**Main notions and definitions**

Being $G:=(V,E)$ a graph. Then we have the following definitions:

- A *Hamiltonian path*, $P_{H,uv}$ is a path that visits every vertex $t \in V$ exactly once.

- A *Hamiltonian cycle*, $C_u$ is a cycle formed through a Hamiltonian path,$P_{H,uv}$ meaning that visits every vertex exactly once with the exception of the starting point: $C_u := P_{H,uv},u$

We say that $G$ is Hamiltonian if admits a *hamiltonian cycle*.

<br>

**Implications (NOT Characterization)**

Being $G:=(V,E)$ a hamiltonian graph, then:

- **$G$ is connected**; If every single vertex is contained in a path, then for every pari of vertex exists a path that contains those vertex so $G$ is connected.

- **$deg(v) \geq 2 \ \ \forall v \in V$**. If the graph admits a hamiltonian cycle, then exists a cycle that traverse al the vertex returning to the starting point, meaning that all vertex $v \in V$ has an in/out edge, thus at least is two although can be more, thus $deg(v) \geq 2$.

- **There are no "cut-vertex"**. Meaning that removing one vertex does not disconnect the graph, because removing a vertex results in the hamiltonian cycle to derive in a hamiltonian path, thus all vertex remains connected:

    ![hamiltonian1](/assets/images/Maths/DiscreteMath/hamiltonian1.png)

    <br>

**Ore's premise and some immediate results**

Ore's premise says something as “if the graph is dense enough, it must be Hamiltonian”: 

$H:=(V,E) : \big( \vert V \vert \geq 3 \wedge deg(u) + deg(v) \geq \vert V \vert \ \forall u,v \in V : u \not \sim v\big) \implies H \text{ is Hamiltonian}$

<br>

Let's start seeing that $H$ as defined, is connected. Being $u,v \in V$, then consider $P_u := \Set{v \in V \vert \exists P_{uv} \subset H}$, 

Observe that: $\nexists P_{uv} \text{ in } H \implies \ P_u \cap P_v = \varnothing \implies \vert P_u \cup P_v \vert = \vert P_u \vert + \vert P_v \vert \leq \vert V \vert$. 

$$deg(t) + deg(l) \leq \vert P_u \vert -1 + \vert P_v \vert -1 = \vert V \vert - 2 < \vert V \vert \ \ \ \forall t \in P_u \wedge \forall l \in P_v$$

Observe that obviously $t \not \sim l$ .

This contradicts the initial Ore's presumption of $H$, so $H$ is connected and we can safely think in a path for any pair of vertex in $V$.

<br>

Let's also observe that $deg(v) \geq 2 \ \ \forall v \in V$. If $H$ is a complete graph then is nothing to proove, then let's suppose that:

$$\exists u,v \in V: u \not \sim v \wedge deg(v) =1 \implies deg(u) + deg(v) = deg(u) + 1 \geq \vert V \vert \implies deg(u) \geq \vert V  \vert - 1$$

Also, since $\vert V \vert > deg(u) \wedge deg(u) \in  \mathbb{N} \implies deg(u) = \vert V \vert -1$

This would mean that  that $N(u) = V \setminus \Set{u} \implies v \in N(u) \implies u \sim v$ contradicting the no adjacency premise. So there are no leafs in $H$.

<br>

Let's also observe that in $H$:

$$N(v) \cap N(u) \neq \varnothing \wedge \vert N(v) \cap N(u) \vert \geq 2 \ \ \forall u,v \in V: u \not \sim v $$

Note that $u \not \sim v \implies \Big(deg(v) + deg(u) = \vert N(u) \vert + \vert N(v) \vert \geq \vert V \vert \Big) \wedge \Big( N(u) \cup N(v) \subset V \setminus \Set{u,v}\Big)$

Then applying $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$, and $deg(u) + deg(v) \geq \vert V \vert$ is: 

$$\vert V \vert -2 \geq \vert N(v) \cup N(u) \vert = \vert N(u) \vert +  \vert N(v) \vert - \vert N(u) \cap N(v) \vert \geq \vert V \vert - \vert N(u) \cap N(v) \vert $$

Meaning that $\vert N(u) \cap N(v) \vert \geq 2$ necesarily. Then, $\exists t,l \in V : t,l \in  N(u) \cap N(v) \ \ \forall u,v \in V: u \not \sim v$.

<br>

**Bondy-Chvátal Lemma**

Being $G:=(V,E) : \vert V \vert = n \geq 3 \wedge deg(u) + deg(v) \geq n$, then we define $G + uv :=(V,E \cup \Set{u,v})$, observe that obviously: $u \sim v \text{ in } G \implies G = G +uv$. 

This lemma stands that:

$$ G \text{ is hamiltonian } \iff G + uv \text{ is hamiltonian }$$

Let's proof the lemme.

- Observe quicly that $ G \text{ is hamiltonian } \implies G + uv \text{ is hamiltonian }$, since adding edges (supposing $u \not \sim v$) does not destroys cycles.

- If $G + uv \text{ is hamiltonian }$, then if the cycles does not use $\Set{u,v}$ then $G \text{ is hamiltonian }$, thus lets suppose that the cycles does use $\Set{u,v}$.

    Consider the hamiltonian path $P_{H,uv} \subset G$ (which exists since $G + uv$ is hamiltonian and the hamiltonian cycle does use $\Set{u,v} \in E$). If we consider that $A:=\Set{i \in \Set{2,...,n}: v_i \sim u} \wedge B:=\Set{i \in \Set{1,...,n-i}: v_i \sim v}$ then, obviously $A$ and $B$ are the set of the neigbourhs shifted by one relative to the other, let's observe that, as we discusse before: 
    
    $$N(u) \cap N(v) \neq \varnothing \implies A - 1 := \Set{i-1: i \in A}\cap B \neq \varnothing \implies \exists i: u \sim v_{i-1} \wedge v_i \sim v$$

    Thus, taking a redirection of the path: $P:=u,...,v_{i-1},v,...,v_i,u$, we have our hamiltonian cycle.

    ![Bondy_Chvatal](/assets/images/Maths/DiscreteMath/Bondy_Chvatal.png)

    The image above pretends to ilustrate the result of the lemma, for simplicity, innecesary edges have been omited.

    <br>

**Ore's theorem**

Let's observe that, from the result before, the Ore's premise garantee $G \text{ is hamiltonian } \iff G + uv \text{ is hamiltonian }$, and this premise can be implemented iteratively, meaning:

$$G \text{ is hamiltonian} \iff G + uv \text{ is hamiltonian}\iff (G + uv) + lt\text{ is hamiltonian} \iff \cdots \iff K_n\text{ is hamiltonian}$$

Observe we eventually reach a complete graph since $V$ is finite and so is the number of edges that can be included. 


<br>

**Dirac's theorem**

Let observe that there is another direct result that can be derivate from Ore's theorem. Being $G:=(V,E) : \vert V \vert = n \geq 3$, then:

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

Observe that this means that the Four Colour theorem exposes $\chi(G) \leq 4 \ \ \forall G$ and the 3-coloring problem ask whether, $\chi(G) \leq 3$.

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

        Simply, considering $c : V_K \to \Set{1,...,i}$ with $ i < n$, then $c$ is *no injective* and it verifies the *pigeonhole principle*:

        $$\exists u,v \in V_K : u \neq v \land c(u) = c(v)$$

        Again, for $\forall u,v \in K_n \ \ u \neq v \iff \Set{u,v} \in E_K$ and thus:

        $$\exists \Set{u,v} \in E_K : c(u) = c(v)$$

        And $c$ is no coloration.

        <br>

2. For a cycle $C_n$, $\chi(C_n) = 2$ if $n$ is even and $\chi(C_n) = 3$ if $n$ is odd.

    First, let's define what a cycle graph is: 
    
    $$C_n := (V_C, E_C) : \begin{cases} V_C = \Set{v_0,...,v_{n-1}} \\ E_C = \Set{\Set{v_{i-1},v_i} : i \in \Set{1,...,n-1}} \cup \Set{\Set{v_{n-1},v_0}} \end{cases}$$

    Let's observe that, as defined, the sequence: $v_0,...,v_{n-1}$ is a path, thus $v_0,...,v_{n-1},v_0$ is a cycle.

    - Now, consider the case $\exists m : n = 2m$, then, we define:

        $$c : V_C \to \Set{1,2} : c(v_i) = \begin{cases}  1 \ \text{ if } i  \text{ is even}\\ 2 \ \text{ if } i  \text{ is odd} \end{cases}$$

        It is clear that even and odd numbers alternates each in a consecutive numeric sequence. So:

        $$c(v_{i-1}) \neq c(v_i) \ \ \forall v_{i-1},v_i \in v_0,...,v_{n-1} \implies c(v_{i-1}) \neq c(v_i) \ \ \forall \Set{v_{i-1},v_i} \in E_C $$

        For the same reason, if $n$ is even, then $n-1$ is odd and $c(v_{n-1}) \neq c(v_0)$, thus, in conclusion:

        $$c(u) \neq c(v)  \ \ \forall \Set{u,v} \in E_C$$

        And $c$ is a $2-coloring$ of $C_n$. Obviously since $E_C \neq \varnothing$ it can't be $\chi(C_n) = 1$.

        <br>

    - If $n = 2m + 1$ and we suppose the existence of a $2-coloring$, $c$ over $C_n$, then: 

        $$c(u) \neq c(v) \ \ \forall \Set{u,v} \in E_C \implies c(v_{i-1}) \neq c(v_i) \ \ \forall \Set{v_{i-1},v_i} \in E_C \iff$$
        $$ \iff c(v_{i-1}) \neq c(v_i) \ \ \forall v_{i-1},v_i \in v_0,...,v_{n-1}$$

        Or, in other words, any consecutive vertex in the path $v_0,...,v_{n-1}$ has different image under $c$. 
        
        Thus, is easy to see that:
        
        - Since in a $2-coloring$ there are only two possible images values 
        
        - And $n-1$ is even (because $n$ is odd), 
        
        Then $v_0$ and $v_{n-1}$ share the same image under $c$ and it is:
        
        $$c(v_{n-1}) = c(v_0) \land \Set{v_{n-1},v_0} \in E_C$$
        
        Triggering a contradiction with the $2-coloring$ requirement.

        Getting the example of $c$ provided above, is easy to see that:

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

    The 2-colorability caracterization stands for, being $G := (V,E)$ a graph, then:

    $$\chi(G)=2 \iff G \text{ is bipartite } \iff \neg \exists\,\text{cycle } C \subseteq G : |C|\ \text{ is odd} $$

    Observe that we already demonstrate that:

    - $G \text{ is bipartite } \implies \chi(G)=2$
    - $\chi(G)=2 \implies \neg \exists\,\text{cycle } C \subseteq G : \vert C\vert \ \text{ is odd}$ (since all odd cycle has a 3 as a chromatic number).
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

        - First, $\neg \exists C \subseteq G : C \text{ is a cycle}$, then consider a vertex we call $r$ and: $A = \Set{u \vert  dist(r,u) \text{ is even}}$ and $B = \Set{u \vert  dist(r,u) \text{ is odd}}$. Then is pretty obvius that $A \cup B$ and we impose that $A \cap B = \varnothing$, let's observe that this impossition requires no odd cycles.

            Being $C \subseteq G : C \text{ is odd}$, then, $C:=v_0,...,v_{n-1},v_0$ where $v_0,...,v_{n-1}$ is a path and $\Set{v_{n-1},v_0} \in E$. Lets say $r : dist(r,v_0) \land r \notin C$. Then, since $C$ is a cycle there are two paths to measure the distance between $r$ and $v_{n-1}$:

            $$dist(r,v_{n-1}) = dist(r,v_0) + dist(v_0,v_{n-1})$$

            Since $\Set{v_{n-1},v_0} \in E \Rightarrow dist(v_0,v_{n-1}) = 1 \Rightarrow dist(r,v_{n-1}) = 2 \text{ (even)}$, but also, since $C$ is odd, $n-1$ is even (meaning that $dist(v_0,v_{n-1})$ is even and $1 + dist(v_0,v_{n-1}) = dist(r,v_{n-1})$ is odd). So in summary: $A \cap B \neq \varnothing$

           <br>

#### 2.1.1.5. Plannar graphs. Drawings and faces. Euler's formula.

A *planar graph* is a graph that admits a graphical representation on a plane such its edges do not cross each other. For example, Complete graph $K_3$ do admit a representation in which the edges not cross, but $K_5$ do not.

Let be $G:=(V,E)$ a finite simple graph, then an embedding of $G$ into $\mathbb{R}^2$ is a function $\phi: G \to \mathbb{R}^2$ that:

- $\forall u,v \in V \ \ \left(\phi(u), \phi(v) \in \mathbb{R}^2 \land u \neq v \implies \phi(u) \neq \phi(v) \right)$

- $\forall e, f \in E \ \ \left( \phi(e) = \gamma_{e_1e_2}, \phi(f) = \gamma_{f_1f_2}  \in \mathbb{R}^2 : e \neq f \implies \phi(e) \cap \phi(f) \subseteq \Set{\phi(e_1),\phi(e_2),\phi(f_1),\phi(f_2)} \right)$


Where $\gamma_{uv}$ is a simple arc (non-self-intersecting, continuous curve) from $\phi(u)$ to $\phi(v)$. $\phi$ maps the edges of $G$ ensuring that two different arcs only share endpoints as much.

Then, $G$ is said to be planar if admits a embedding $\phi$ in $\mathbb{R}^2$ as above.

<br>

Associated to a drawing of a planar graph are the so called *faces*, grouped in the set $F$; which are enclosed regions of the plane $\mathbb{R}^2$ by the planar drawing of the graph (here is included the unbound outer face extranl to the graph). The Euler's formula specifies that, for a complete planar graph $G:= (V,E)$, being $F$ the set of the faces of the drawing graph, then:

$$|V| - |E| + |F| = 2$$

<br>

#### 2.1.1.6. Dual graphs.

Given a connected planar graph $G$, then, the *dual graph* is what you get when you turn faces into vertices in a planar embedding of $G$. 

The drawing (planar embedding) cuts the plane into regions (faces), one unbounded “outside” face plus the bounded ones, then the dual $G^*$ is built by:

- Putting one vertex inside each face of $G$.
- For each $e \in E$ there exists one $e^* \in E^*$ crossing once $e$, connecting two faces.

Formally;

Being $G$ a connected planar graph and $\phi$ his drawing in $\mathbb{R}^2$. Then, we define the dual graph as:

$$G^*:= (V^*,E^*):\begin{cases}V^* &:= F = \Set{f : f \text{ is a face of }(G,\phi)} \\ E^* &:= \Set{\Set{f_1,f_2} | \exists e \in E \text{ between } f_1 \text{ and } f_2 } \subseteq \binom{V^*}{2}\end{cases}$$

Is important to understand that *Dual depends on the embedding*: Two different planar drawings of the same abstract planar graph can produce non-isomorphic duals. The dual is canonical only after you fix the embedding.

In this context, a map coloring is equal to color a dual graph. A map representation is in fact a dual graph.

<br>

### 2.1.2. Directed graphs.

A *directed acyclic graph* (DAG) is a directed graph that encodes a *one-way dependency* or *precedence relation*; *causality* with no circularity.

As an example, being $u,v$ two predicates related as $u \to v$, then a DAG would represent this relation by an arrow of $u$ to $v$ meaning that $v$ depends on $u$ (or $u$ must happen before $v$). 

Thus, DAGs are a way to abstract implication relationships between multiples agents in a discrete relation structure.

<br>

#### 2.1.2.1. Formal Definition.

A direct graph gets defined as a pair: $D:= (V,E)$, where:

- $V$ is a finite set of elements.
- $E \subseteq V^2$ is a set of ordered pairs.
<br>

#### 2.1.2.2. Main notions.

**Impliance**

The first main notion we want to introduce is how the vertex (which are maintained from the simple graph conception) gets related in a directed graph.

Being $G:=(V,E)$ a graph, then $E \subseteq \binom{V}{2}$ is the set of edges $\Set{u,v} \in E$ and we say that $u,v \in V$ are adjacent $u \sim v \iff \Set{u,v} \in E$. This is how two elementes gets related in the simple graph conception. $\Set{u,v}$, as a simple set, doesn't care about order so the relation is bidirectional, $u$ is adjacent to $v$ exactly as $v$ is adjacent back to $u$.

In the directional conception, there is no adjacency but impliance and this relation gets formalized through ordered sets. Remember that $D := (V,E)$ is a directed graph when $E \subseteq V^2$ meaning that the elements of $E$ are pairs $(u,v)$. In this context, we introduce the notion of *impliance*.

Being $u,v \in V$ then we say $u$ implies $v$, $u \to v \iff (u,v) \in E$. We can also say that $u$ preceds $v$. 

Note that this relation is not reciproc, $u \to v \not \Rightarrow v \to u$

<br>

**In/Out neighborhood**

Based in the notion of impliance defined before as a substitue of te adjacency for direct graphs, we consider the following sets:

- *In-neighborhood*; $N^{+}(u)=\{\,v\in V : u\to v\,\}$
- *Out-neighborhood*; $N^{-}(u)=\{\,v\in V : v\to u\,\}$

This are nothing but the paralalel concept of neigbourhood in simpe graphs $N(v) := \Set{u \ \vert \ u \sim v }$ but based in the order of the impliance.

Also, we can consider the following numbers:

- The *out-degree* to the number: $deg^+(v) := \vert N^{+}(v) \vert$
- The *in-degree* to the number: $deg^-(v) := \vert N^{-}(u) \vert$

<br>

**Implicated vertex structures.**

- **Directed Walk**; is a sequence $(v_0,...,v_k) : v_{i-1} \to v_i \ \ \forall i \in [k] \wedge k \in \mathbb{N}$

- **Directed Path**; is a directed walk with all vertices distinct.

- **Directed Cycle**; is a directed walk $(v_0,...,v_k,v_0) : (v_0,...,v_k)$ is a path.

![direct_structures](/assets/images/MathWs/DiscreteMath/direct_structures.png)

<br>

#### 2.1.2.3. Directed Acyclic Graphs (DAGs).

A Directed Acylic Graph (DAG) is a directed graph with no cycles.

<br>

##### 2.1.2.3.1. Definition. Sources and sinks.

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

##### 2.1.2.3.2. Order in DAGs.

######  2.1.2.3.2.1. Order definition.

**Binary Relations and Orders.**

Given a set $X$, a binary relation on $X$ is a subset: $R \subseteq X \times X$ and we write as a shorthand, being $x,y \in X$, then:

$$xRy \iff (x,y) \in R$$

We call to $R$ as an order, and, defined along certains conditions, we abstract the idea that $x$ preceeds $y$ through $R$ and we represent it such as $(x,y) \in R$

Then, any binary relation $R$ must satisfy the following three condition to be called a *order*:

- **Reflexive**: $xRx \ \ \forall x \in X$
- **Transitive**: $xRy \wedge yRz \implies xRz \ \ \forall x,y,z \in X$
- **Antisimetric**: $xRy \wedge yRx \implies x = y \ \ \forall x,y \in X$

<br>

**Partial and Total Order**

When we define a binary relation $R$ over a set $X$ then is pertinent to ask if:

$$xRy \vee yRx \ \ \ \forall x,y \in R$$

If $x$ and $y$ are incomparable then we write:

$$\neg(xRy) \wedge \neg (yRx) \iff x \ \vert \vert \ y$$

We say that $R$ defined in $X$ is: 

$$R \text{ is a partial order } \iff \exists x,y \in X : x \ \vert \vert \ y$$
$$R \text{ is a total order } \iff xRy \vee yRx \ \ \ \forall x,y \in R$$

<br>

**Strict and non-strict order**

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

**Partial Order in DAGs**

Consider $D$ a DAG, then, we can define the following subset 

$$\preceq  \ \subseteq V^2: x \preceq y \longleftrightarrow \exists \text{ a directed path } P_{xy}$$

Observe that this relation is an order since:

- *Reflexive*: $v \preceq v \ \ \forall v \in V$ since $(v,v) \in E$
- *Transitive*: $v \preceq u \wedge u \preceq w \implies P_{vw} = P_{vu},P_{uw} \implies v \preceq w$
- *Antisimetric*: $v \preceq u \wedge u \preceq v \implies u = v$ since not cycles are allowed.

<br>

###### 2.1.2.3.2.2. Topological Order. Characterization of DAGs.

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

Note that the topological order is a total order in a DAG. This conclusion is obvious taking the line-up the vertex perspective of $D$.

<br>

## 2.2. Basic Algebra: Rings and Fields.

## 2.3. Polynomies.

## 2.4. Discrete Probability.

# 3. Arithmetic Circuits.

## 3.1. Formal definition.

## 3.2. Arithmetic Circuits and Complexity Theory.

## 3.3. Arithmetic Circuits and Discrete Probability.