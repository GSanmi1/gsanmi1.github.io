---
layout: post
title: "3. VectorSpaces Properties"
subtitle: "Subspaces, Bases and Dimensions, Coordinates, Row-equivalence summary, Computations Concerning Subspaces."
date: 2026-06-08 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
subject: linear-algebra
lang: en
---

# 0. Index.

1. Introduction.
2. Subspaces.
    - 2.1. Definition and characterization.
    - 2.2. Example of subspaces.
    - 2.3. Combination of vector spaces.
        - 2.3.1. Intersection of subspaces.
        - 2.3.2. Spanned subspace by a set.
        - 2.3.3. Sum of subsets of vector spaces.
    - 2.4 Example of combinated vector spaces.
        - 2.4.1. Subspace defined by equations.
        - 2.4.2. Matrix.
        - 2.4.3. Row-spaces.
        - 2.4.4. Caracterization of the polynomial vectorspace.
        - 2.4.5. Subspaces exercises.
3. Dependence, Basis and Dimension.

<br>


# 1. Introduction.

In the past post; [Vector Spaces](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/), we've introduced that a vector space $(K,V,·)$ is the algebraic structure resulting from using a field $K$ to weigh the compositions of an abelian group $V$, through a field action $·$. Meaning that a vector space is a triple $(K,V, ·)$ where:

- $K$ is a field.
- $V$ is an abelian (commutative) group.
- $· : K \times V - V$ is a field action, which acts over $V$ using $K$'s elements to scale vectors, making families of *proportional vectors*.

The resulting compositions are what we call *linear combinations*, independent contributions of the group's elements mediated by the field's scalars:

$$\alpha v + \beta u : \alpha ,\beta \in \mathbb{R}, v,u \in V$$

We presented some examples of sets which, with proper operations involved, are examples of vector spaces:

- The $n$-tuples space: $F^n$
- The space of $m \times n$ matrices: $M_{m \times n}(F)$ 
- The space of functions from a set $S$ to a field $K$: $K^S$
- The space of polynomial functions over a field K

    <br>

We also developed, surreptitiously, the affine space structure, which is the way in which we use vectors to study a non-empty set in a simply transitive way, and we defined the *arrow* concept as the segment that connects two points of the affine space with magnitude, direction and orientation, which captures the displacement from the point at the base of the segment to the one lying at the end of the arrow.

We also demonstrated that if you fix one point $O$ and consider the family of all possible arrows with base at $O$, then that family has the structure of a vector space, which leaves us with a geometric intuition of what a vector is.

<br>

Then, with this information as a starting point, let's develop the fundamental properties of vector spaces.

<br>

# 2. Subspaces.

## 2.1. Definition and characterization.

In this section we shall introduce some of the basic concepts in the
study of vector spaces. 

**Let $V$ be a $K$-vector space. A subspace of $V$ is a non-empty subset $W$ of $V$ which is itself a vector space over $K$ with the restricted operations of $V$ on $W$.**

<br>

Let's observe something interesting, from the [vector spaces](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/) post, we know that for $(K,V, \cdot)$ to be a vector space; $K$ must be a field, $V$ must be an abelian group and $·$ must be a field's action over $V$. Hence, if $W \subset V : W \neq \varnothing$ then, for the triple $(K,W,·\mid_W)$ to be a vector space there are two structures that must survive, the abelian group and the field's action. 

- First, let's see that $W$ is a subgroup if $\cdot \mid_W, + \mid_W$ are closed in $W$. From the four axioms of the group, two departs from the universal quantifier $\forall$, hence all the elements inherites the properties from $V$ action, but the *identity* and the *inverse* involves and existential quantifier, $\exists$, let's see that the clausure of $\cdot \mid_W$, garantuee the properties:

    $$\begin{cases} \cdot \in V^{K \times V} \text{ is a field's action } \\ W \subseteq V : W \neq \varnothing \\ \cdot \mid_W \text{ is closed in } W   \end{cases} \implies \begin{cases} \exists v \in V : v \in W \implies 0_Kv = 0_V \in W \\ \forall v(v \in W \implies -1_K v= -v \in W) \end{cases}$$

    <br>

- Second, hence if the restriction of the field's action is closed, then we can assert that $W$ is a subgroup of $V$ if $+ \mid_W$ is also closed:

    $$\begin{cases} \cdot \in V^{K \times V} \text{ is a field's action } \\ W \subseteq V : W \neq \varnothing \\ \cdot \mid_W \text{ is closed in } W   \end{cases} \implies (+\mid_W \text{ is closed in } W \rightarrow W \text{ is a subgroup of V } )$$

    Observe that the despite we don't mention it, the commutativity also get's inheritated so is not necesary to mention.

    <br>

- Ultimately, if $W$ is a subgroup of $V$ and the restriction of the field's action in $V$ is closed on $W$, then the restriction is also a field's action over $W$ since all the axioms departs from the $\forall$ quantifier and the triple $(K,W,·\mid_W)$ is indeed a vector space.


    <br>

This can be summarized in, be $V$ a vector space and $W \subset V : W \neq \varnothing$, then:

$$W \leq V \iff +\mid_W, \cdot \mid_{W} \text{ are closed in } W $$

Which is the same as:

$$\begin{rcases}\forall u \forall v(u,v \in W \implies u + v \in W) \\ \forall u (u \in W \implies \alpha u \in W \quad \forall \alpha \in K)\end{rcases} \iff \forall u \forall v(u,v \in W \implies \alpha u + v \in W \quad \forall \alpha \in K)$$

Essentially, a *subset of vectors is a subspace as long as it retains all the posible linear combinations of his elements*, and it allows to assert if some subset is a subspace without reconstruct the entire structure.

A good observation is to realize that if $W$ is not empty, then $W \leq V \implies -u + u = 0 \in W$, is a necesary but not sufficent condition. Anyways is a good opening point in any comprobation since this is quicly telling that if you can't find the zero element in $W$ this can't be a subspace.

<br>


## 2.2. Example of subspaces.

Let's consider some well-known examples of subspaces. Consider some $V$ a $K$-vector space, then:

1. $V$ is a subspace of $V$.
2. $\Set{0} \subset V$ is the **zero subspace** of $V$; $\alpha 0 + 0 = 0 \in \Set{0} \quad \forall \alpha \in K$ so $\Set{0}$ is a subspace of $V$.

3. $A:= \Set{x \in K^n \mid x_1 = 0}$ is a subspace of $K^n$, check that always $\alpha x + y \in A$, trivially.

    But let's observe that $B := \Set{x \in K^n \mid x_1 = 1 + x_2}$ (the solution of a non-homogeneous equation) does not satisfy the rule, take some $\alpha$ and observe that:

    $$\alpha x + y = (\alpha (1 + x_2) + 1 + y_2), \alpha x_2 + y_2,..., \alpha x_n + y_n)$$

    Then, $\alpha + 1 + \alpha x_2 + y_2 = 1 + \alpha x_2 + y_2 \iff \alpha=0$. 
    
    So we have that $\forall \alpha \neq 0 \quad (x,y \in B \implies \alpha x + y \notin B)$

    <br>

4. The **space of polynomial functions** over $K$; 

    $$\operatorname{Pol}(K, K) := \left\{\, f \in K^K \ \middle|\ \exists n \in \mathbb{N}_0,\ \exists (\alpha_0, \ldots, \alpha_n) \in K^{n+1} : \forall s \in K,\ f(s) = \sum_{i=0}^{n} \alpha_i\, s^i \,\right\}$$

    Is a subspace of $K^K$.

    Observe that, if we get $f,g \in Pol(K,K)$, then is: $ f(s) = \sum_{i=0}^{n} \alpha_i\, s^i$, $g(s) = \sum_{i=0}^{m} \beta_i\, s^i$, consider is $n \leq m$, then we can expand $f(s)$ to $\sum_{i=0}^{m} \alpha_i\, s^i = \sum_{i=0}^{n} \alpha_i\, s^i +\sum_{i=n+1}^{m} 0\, s^i$ and then is:

    $$ (\gamma f + g)(s) = \gamma f(s) + g(s) = \gamma \sum_{i=0}^{m} \alpha_i\, s^i  + \sum_{i=0}^{m} \beta_i\, s^i =$$
    
    $$\sum_{i=0}^{m} \gamma\alpha_i\, s^i + \sum_{i=0}^{m} \beta_i\, s^i = \sum_{i=0}^{m} (\gamma\alpha_i + \beta_i) s^i = \sum_{i=0}^m \varphi_i \, s^i \in Pol(K,K)$$

    <br>

5. Consider $S:=\Set{(a\_{ij})\_{ij} \in M\_n(K) \mid (a\_{ij})\_{ij} = (a\_{ij})\_{ji}}$, the **set of all symmetric matrices** form a subspace of $M\_n(K)$

    Take, $A,B \in S$, then let's see that $\alpha A + B = \alpha (a\_{ij})\_{ij} + (b\_{ij})\_{ij} = (\alpha a\_{ij} + b\_{ij})\_{ij}$, then let's see that this matrix is in $S$ by observing that:

    $$A \in S \implies a_{ij} = a_{ji} \quad \forall i,j \implies \alpha a_{ij} = \alpha a_{ji} \quad \forall i,j  \implies \alpha A \in S$$

    Now, observe that:
    
    $$A,B \in S \implies \begin{cases}a_{ij} = a_{ji} \quad \forall i,j \\ b_{ij} = b_{ji} \quad \forall i,j  \end{cases} \implies a_{ij} + b_{ij} = a_{ji} + b_{ji} \quad \forall i,j \implies A+B \in S$$

    Ultimately concluding $\alpha A + B \in S$, so $S$ is a subspace of $M_n(K)$

    <br>

6. Consider $M\_n(\mathbb{C})$, then we say that $A \in M\_n(\mathbb{C})$ is Hermitian or self-adjoint if $(a\_{ij})\_{ij} = \overline{(a\_{ij})\_{ji}}$, meaning that is equal to the transverse of the conjugate.

    Then, the set $H := \Set{A \in M\_n(\mathbb{C}) \mid (a\_{ij})\_{ij} = \overline{(a\_{ij})\_{ji}} }$ is not a subspace of $M\_n(\mathbb{C})$ check that the diagonal elements impose $(a\_{ii})\_{ii} = \overline{(a\_{ii})\_{ii}}$, since the entries are complex numbers, a complex number is equal with his conjugate when is real.

    Consider some $A \in H$ and observe that $iA \notin H$, since the diagonal is not real and is not an Hermitic matrix, so our criteria $\alpha A +B \in H \quad \forall A,B \in H, \alpha \in \mathbb{C}$ doesn't apply.

    How ever it does applies when $\alpha \in \mathbb{R}$, observe that $(\mathbb{R},(H,+), ·)$ is a $\mathbb{R}$-vector space.

    <br>

7. **The solution space of a system of homogeneous linear equations over $K$**

    Let be $A \in M_{m\times n}(K)$, then consider $W := \Set{X \in M_{n \times 1}(K) \mid AX = 0}$ that's not empty, let's remember that:
    
    $$AX = \begin{pmatrix} a_{11} \cdots a_{1n} \\ \vdots \quad \quad \quad \vdots \\ a_{m1} \cdots a_{mn} \end{pmatrix} \begin{pmatrix} x_1 \\ \vdots \\ x_n\end{pmatrix} = \begin{pmatrix} \sum_{i=1}^n a_{1i}x_i \\ \vdots \\ \sum_{i=1}^n a_{mi}x_i \end{pmatrix} $$

    Then, $X \in W \implies \sum_{i=1}^n a_{ji}x_i = 0\quad \forall j \leq m$

    <br>

    Let's now consider $\alpha X + Y$, then:

    $$A[\alpha X + Y] = \begin{pmatrix} a_{11} \cdots a_{1n} \\ \vdots \quad \quad \quad \vdots \\ a_{m1} \cdots a_{mn} \end{pmatrix} \begin{pmatrix} \alpha x_1 + y_1 \\ \vdots \\ \alpha x_n + y_n\end{pmatrix} = \begin{pmatrix} \sum_{i=1}^n a_{1i}(\alpha x_i + y_i) \\ \vdots \\ \sum_{i=1}^n a_{mi}(\alpha x_i + y_i)  \end{pmatrix} $$

    Observe that, for being $X,Y \in W$:

    $$\sum_{i=1}^n a_{mi}(\alpha x_i + y_i) = \alpha \sum_{i=1}^n a_{ji} x_i + \sum_{i=1}^n a_{ji}y_i = 0 \quad \forall j \leq m$$

    So, $\alpha X +Y \in W$.

    <br>

## 2.3. Combination of vector spaces.

Let's now see that the intersection of vector subspaces is a subspace, the spanned vector space of a subset of vectors is at the same time the intersection of all the subspaces that contains the subset and the set of all linear combinations of the vectors of the subset. 

The the addition or sum of subspaces is a subspace

<br>

### 2.3.1. Intersection of subspaces.

**Let $V$ be a vector space over the field $K$. The intersection of any collection of subspaces of $V$ is a subspace of $V$.**

Consider $V$ a $K$-vector space, then $\Set{W_i}$ a family of subspaces of $V$, consider $\bigcap_i W_i$. Then, observe that for being each $W_i \leq V \implies 0 \in W_i \quad \forall i \implies 0 \in \bigcap_i W_i \neq \varnothing$. Then, consider:

$$u,v \in \bigcap_i W_i \implies u,v \in W_i \leq V \quad \forall i \implies \alpha u +v \in W_i \quad \forall i \implies \alpha u + v \in \bigcap_i W_i$$

And thus, $\bigcap_i W_i \leq V$

<br>

This result gains its importance from the fact that the subspace generated by a subset $S \subset V$ is the intersection of all the subspaces of $V$ that contains $S$, this is in fact the smallest subspace that contains $S$.

<br>

### 2.3.2. Spanned subspace by a set.

**Spanned subspace definition**

Consider again a $K$-space, $V$, and a subset $S$ of $V$.

Then, the **subspace spanned** by $S$ is the intersection of all those subspaces of $V$ which contains $S$, which, as we see above, is a vector space.

When $S$ is a finite set of vectors, $S:=\Set{\alpha_1,..., \alpha_n}$, we shall simply call $W$ the subspace spanned by the vectors $\alpha_1, \alpha_2, ..., \alpha_n$, 

<br>

**Spanned subspace caracterization**

Be $S$ a non-empty subset of a $K$-vector space $V$, then the spanned subspace of $S$, $W$ is the set of all the linear combinations of $S$'s vectors.

- First, let's see that obviously $W \neq \varnothing$: $S \neq \varnothing \implies \exists u \in S$, then $u = 1u \in W \implies W \neq \varnothing$. Lastly, just consider $u,v \in W$, then $\alpha u + v \in W$ so $W \leq V$.

    Let's make an observation, $\varnothing$ vacuosly satisfies the closure on linear combinations, there are no $u,v$ to test so is a null antecedent implication. The fact which separates $W$ from this degenerated case is the fact that $W \neq \varnothing$, meaning that for a vector space is unconditional to be non-empty, linear combination closure is not enough.

    <br>

- Let now be $\Set{W_i \leq V \mid S \subseteq W_i}_{i \in I}$ the family of subspaces of $V$ that contains $S$ let's see that in fact is $W = \bigcap_i W_i$ by demonstrating each set contains the other.

    - $W \subset \cap_i W_i$

        If $w \in W \implies \exists u,v \in S : \alpha u + \beta v = w$. Since $S \subset \cap_i W_i \implies u,v \in \cap_i W_i$ and, since each $W_i \leq V$ and the intersection of vector spaces is a vector space then any linear combination is in $\cap_i W_i$, meaning $w = \alpha u + \beta v \in \cap_i W_i$

        <br>

    - $\cap_i W_i \subset W$

        Let's observe $W$ is the subspace of all the linear combinations of $S$ elements, is contained in each $W_i$ because every vector space contains the linear combinations of the elements of $S$ for being vector spaces.

        Thus, observe that $W$ is the minimum element of the collection which, coincides by definition with his ínfimum which is by definition the spanned vector space this is, the intersection $\cap_i W_i$.

        <br>

### 2.3.3. Sum of subsets of vector spaces.

If $S_1,S_2,\cdots, S_k$ are subsets of a vectror space $V$, then the set of all sums:

$$\sum_{i=1}^k S_i = S_1 + S_2 \cdots + S_k = \Set{\sum_{i=1}^k \alpha_i \mid  \alpha_i \in S_i}$$

Now consider: $W_i \leq V : i = 1,2...,k$, then the set $\sum_{i=1}^k W\_i$ is immediately a subspace. Observe that this spaces is the space spanned by the set $\bigcup_i W_i$.

<br>

## 2.4 Example of combinated vector spaces.

### 2.4.1. Subspace defined by equations.

Let $K$ be a subfield of the field $C$ of complex numbers. Then suppose:

$$\begin{cases} \alpha_1 = (1,2,0,3,0) \\ \alpha_2 = (0,0,1,4,0) \\ \alpha_3 = (0,0,0,0,1) \end{cases}$$

Let's observe that the spanned vector space by $\Set{\alpha_1,\alpha_2, \alpha_3}$, $W$, is the set of al the lineal combinations of $\alpha_1, \alpha_2$ and $\alpha_3$. Hence, a vector 

$$\alpha \in W \iff \exists c_1,c_2,c_3, \in K : \alpha = \sum_{i=1}^5 c_i \alpha_i = (c_1,2c_1,c_2,3c_1 + 4c_2,c_3)$$

Observe that this subspace $W$ can be described using the equations as the solution set of the linear equation system:

$$M := \begin{cases} x_2 = 2x_1 \\ x_4 = 3x_1 + 4x_3\end{cases}$$

<br>

### 2.4.2. Matrix. 

Let be $K$ a subfield of the field $\mathbb{C}$ of complex numb ers, and let $V$ be the vector space of all $2 \times 2$ matrices over $K$. 

Let consider be the subset of $V$ consisting of all matrices of the form:

$$W_1 := \Set{\begin{pmatrix} x & y \\ z & 0\end{pmatrix}: x,y,z \in K}$$

$$W_2 := \Set{\begin{pmatrix} x & 0 \\ 0 & y\end{pmatrix}: x,y \in K}$$

Observe that: $V = W_1 + W_2$, or, in other terms, the linear combinations of the elements of the two spaces can generate any other element in $V$:

$$\begin{pmatrix} x & y \\ z & t\end{pmatrix} = \begin{pmatrix} x & y \\ z & 0\end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & t\end{pmatrix} \in V$$

Also, the intersection subspace is:

$$W_1 \cap W_2 = \Set{\begin{pmatrix} x & 0 \\ 0 & 0\end{pmatrix}: x \in K}$$

<br>

### 2.4.3. Row-spaces.

Let $A \in M\_{m \times n}(K)$. Then, the *row vectors* of $A$ are vectors $\alpha \in K^n$; $A := (\alpha\_1, \ldots, \alpha\_n)$.

In this context we call the *row-space* of $A$ to the spanned vector space, $W \leq K^n$ of the elements $\Set{\alpha\_i \in K^n \mid A = (\alpha\_1,\ldots, \alpha\_n)}$. 

<br>

### 2.4.4. Caracterization of the polynomial vectorspace.

Consider:

$$Pol(K,K) := \Set{f \in K^K \mid \exists n \in \mathbb{N}, \exists (\alpha_1,\ldots, \alpha_n) \in K^n : f(x) = \sum_{i=1}^n \alpha_i x^i \ \forall x \in K}$$

Then, consider now $ S \subset Pol(K,K)$ defined as:

$$S := \Set{f \in K^K \mid \exists i \in \mathbb{N} :f(x)=x^i \ \forall x \in K}$$

Note that the spanned vector space of $S$ is $Pol(K,K)$.

<br>

### 2.4.5. Subspaces exercises.

#### 2.4.5.1. Subspaces of $\mathbb{R}^n$.

1. $\Set{\alpha \in \mathbb{R^n} \mid a\_1 \geq 0}$

    Naturally isn't a vector space. Observe that trivially $A \neq \varnothing$ and $-1·\alpha + 0 = -\alpha \notin A$, since $a\_1 \geq 0 \implies -a\_1 \leq 0$.

    <br>

2. $\Set{\alpha \in \mathbb{R^n} \mid a\_1 + 3a\_2 =a\_3}$

    We already covered this set in $2.2-3/7$, the solution set of any homogeneous linear equation system is a vector space.

    <br>

3.  $\Set{\alpha \in \mathbb{R^n} \mid a\_2 =a^2\_1}$

    Let's see that this equation is not linear, thus, it do not respects linear combinations and is not a subspace. 

    Take for example $\alpha = (1,1,0)$ and consider the linear combination $\alpha + \alpha$ which not satisfies the condition.

    <br>

4. $\Set{\alpha \in \mathbb{R^n} \mid a\_1a\_2=0}$

    Clearly is not a subspace, consider again: $\alpha = (1,0,1)$ and $\beta = (0,1,0)$ and his linear combination $\alpha + \beta$ which, again, do not satisfies the condition. 

    <br>

5. $\Set{\alpha \in \mathbb{R^n} \mid a\_2 \in \mathbb{Q}}$

    Is not a subspace, take $\alpha = (0,1,0)$, then $\sqrt{2}\alpha = (0,\sqrt{2},0)$ do not satisfies the condtion.

    <br>

#### 2.4.5.2. Function subspaces.

Consider again $\mathbb{R}^{\mathbb{R}}:=\Set{f \in \mathcal{P}(\mathbb{R} \times \mathbb{R}) \mid \forall x \in \mathbb{R} \ \exists ! y \in \mathbb{R}: (x,y) \in f}$, with the operations:

$$(f+g)(x) = f(x) + g(x)$$

$$(\alpha f)(x) = \alpha (f(x)) : \alpha \in \mathbb{R}$$

Then, which of the following sets of functions are subspaces of $\mathbb{R}^{\mathbb{R}}$

1. $\Set{f \mid f(x^2) = f(x)^2}$

    Let's observe immediately that $(\alpha f)(x^2) = \alpha f(x^2)= \alpha f(x)^2 \neq (\alpha f)(x)^2 = \alpha^2 f(x)^2$ for any $\alpha \neq 0$, so is not a vector subspace. 

    <br>

2. $\Set{f \mid f(0) = f(1)}$

    Check that $(\alpha f + g)(0) = \alpha f(0) + g(0) = \alpha f(1) + g(1) = (\alpha f + g)(1)$, so is a subspace.

    <br>

3. $\Set{f \mid f(3) = 1 + f(-5)}$

    Check that 
    
    $$(\alpha f + g)(3) = \alpha f(3) + g(3) = \alpha (1 + f(-5))+ 1 + g(-5) = (\alpha f + g)(-5) + 1 + \alpha$$

    Thus, the condition is not meeted for any $\alpha \neq 0$.

    <br>

4. $\Set{f \mid f(-1) = 0}$

    Check that $(\alpha f + g)(-1) = \alpha f(-1) + g(-1) = 0$, so is a subspace.

    <br>

5. $\Set{f \mid f \text{ is continuous}}$

    Naturally yes.

    <br>

#### 2.4.5.3. Spanned vector.

Consider the vector $\alpha = (3,-1,0,-1)$, is spanned by the vectors $u = (2, -1, 3, 2), v = (-1, 1, 1, -3), w = (1, 1, 9, -5)$?

Consider $W$ the vector subspace spanned by the set $S := \Set{u,v,w}$. Then, the statement ask if $\alpha \in W$.

By $2.3.2$, we do know that the spanned vector subspace, $W$ is the intersection of all the subspaces that contains $S$ which coincides with the set of all the linear combinations of the vectors of $S$ which is a subspace it self.

Then, $\alpha$ is an element of $W$ only if is a linear combination of $u,v,w$, formally:

$$\alpha \in W \iff \exists x,y,z \in \mathbb{R}: \alpha = xu + yv + zw$$

Taking coordinate to coordinate, we can form the following equation system on $\mathbb{R}$:

$$\begin{cases} 3 = 2x -y +z \\ -1 = -x + y + z \\0 = 3x + y +9z \\ -1 = 2x -3y -5z \end{cases}$$

<br>

#### 2.4.5.4. Set of spanned subspace.

Consider $W \leq \mathbb{R}^5$ of those $(x\_1,x\_2,x\_3,x\_4,x\_5) \in \mathbb{R}^5$ satisfying the following equation system:

$$M:=\begin{cases} 2x_1 -x_2 + \frac{4}{3}x_3 - x_4 = 0 \\ x_1 + \frac{2}{3} x_3 - x_5 = 0 \\ 9x_1 - 3x_2 + 6x_3 - 3x_4 - 3x_5 = 0 \end{cases}$$

Find a finite set of vector that spans $W$.

<br>

We have to find some set $S$ such the set of the linear combinations of his elements coincides with $W$. Leveraging the exercise before, giving some $\alpha \in \mathbb{R}^5$, we have to find a finite some of vectors $u_1,u_2, \ldots, u_n$ such the equation system on the escalars $t_1,\ldots, t_n \in \mathbb{R} : \alpha = \sum_{i=1}^n t_i u_i$ is equivalent to the one gived by the exercise.

First, let's consider the $RREM$ form of the matrix previous matrix:

$$R := \begin{pmatrix} 1 & 0 & \frac{2}{3} & 0 & -1 \\ 0 & 1 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$

Which leave us with the system:

$$M' := \begin{cases} x_1 + \frac{2}{3}x_3 - x_5 = 0 \\ x_2 + x_4 -2x_5 = 0 \end{cases}$$

Since $M$ and $M'$ has row-equivalent asociated matrix, we do know that both are equivalents; $M \equiv M'$, so both shares the same solution set, $W$. 

Ultimately, let's solve it, the solution of $M'$ is: 

$$x_1 = -\tfrac{2}{3}x_3 + x_5, \quad x_2 = -x_4 + 2x_5$$

Calling; $x_3 = \alpha,\ x_4 = \beta,\ x_5 = \gamma$, then:

$$W := \Set{(\gamma -\frac{2}{3}\alpha,2\gamma - \beta ,\alpha, \beta, \gamma) : \alpha, \beta, \gamma \in \mathbb{R}}$$

Let's observe that:

$$\begin{pmatrix} \gamma -\frac{2}{3}\alpha \\ 2\gamma - \beta \\ \alpha \\ \beta \\ \gamma \end{pmatrix} = \alpha\begin{pmatrix} -\tfrac{2}{3} \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ -1 \\ 0 \\ 1 \\ 0 \end{pmatrix} +\gamma \begin{pmatrix} 1 \\ 2 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$

Hence, any vector of $W$ is a linear combination of $(−2/3​,0,1,0,0), (0,−1,0,1,0), (1,2,0,0,1)$

<br>

In summary, the solution set of a homogeneous linear system is a vector subspace. Writing the solution in its parametrized form yields the vectors that span the subspace.

<br>

#### 2.4.5.5. Matrix subspaces.

Let be $M_{n \times n} (K) : n \geq 2$, which of the following sets $\Phi\_n$ are subspaces?

1. $ \Set{A \in M_{n \times n}(K) \mid \exists A^{-1}}$

    Let's observe that if we consider $A \in \Phi\_n \implies -A \in \Phi_n$ but $A + -A = 0 \notin \Phi\_n$, hence is not a subspace.

    Observe that, we could quicker check that isn't a subspace because is not a vector space since it not contains $0$.

    <br>

2. $\Set{A \in M_{n \times n}(K) \mid \nexists A^{-1}}$

    Let observe that we can consider:

    $$A = \begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix}0 & 0 & 0\\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

    Both of them aren't invertible since they are already their $RREM$ which not coincides with $I\_3$ but $A+B = I\_3 \in \Phi\_n$

    <br>

3. $\Set{A \in M_{n \times n}(K) \mid AB = BA}$, for some fixed $B$.

    Observe that taking $A, C \in \Phi\_n$ then:

    $$(\alpha A + C)B = \alpha AB + CB = B(\alpha A) + BC = B(\alpha A + C)$$

    Thus, it conforms a subspace

    <br>

4. $\Set{A \in M_{n \times n}(K) \mid A^2 = A}$

    Observe that if $A,B \in \Phi\_n$, then:

    $$(\alpha A + B)^2 = \alpha^2 A^2 + B^2 + \alpha AB + B \alpha A = \alpha^2A + B + \alpha AB + \alpha BA \neq \alpha A + B$$

    
    <br>

#### 2.4.5.6. Subspaces of $\mathbb{R}$.

1. **Prove that the only subspaces of $\mathbb{R}$ are $\mathbb{R}$ and the zero subspace.**

    That $\mathbb{R} \leq \mathbb{R}$ and $\Set{0} \leq \mathbb{R}$ comes immediately from $2.2.$

    Note directly that if there is some subspace $V \leq \mathbb{R}$, then $V$ contains all the linear combinations of himself, so consider some $a \in V \implies 1 = (a/a) \in V$, then since we can multiply $1$ by any scalar, we can reach any element of $\mathbb{R}$ inside of $V$ so $V = \mathbb{R}$.

    <br>

2. **Prove that a subspace of $\mathbb{R}$ is $\mathbb{R}^2$, or the zero subspace, or consists of all scalar multiples of some fixed vector in $\mathbb{R}^2$**.

    First, again that $\mathbb{R} \leq \mathbb{R}$ and $\Set{0} \leq \mathbb{R}$ comes immediately from $2.2.$

    Next, the lines on $\mathbb{R}^2$ are subspaces is also clear, take some not null $v \in R^2$ then any scaled element of $v$ is a linear combination of $v$ so the line contains all the linear combinations of his elements.

    Lastly, let's suppose two elements $u,v \in \mathbb{R}^2: \nexists \alpha \in \mathbb{R} : u = \alpha v$. Then, this two elements doesn't belong to the same line. Suppose  $u = (a,b), v = (c,d)$, hence observe that for some $\alpha, \beta \in \mathbb{R}$ is $\alpha u + \beta v = (\alpha a+ \beta c,0) + (0, \alpha b+ \beta d)$, observe that we can form the following equation system: 

    $$\begin{cases} \alpha a + \beta b = 1 \\ \alpha c + \beta d = 1\end{cases}$$

    Solving it we get:

    $$\alpha=\dfrac{d-c}{ad-bc},\qquad \beta=\dfrac{a-b}{ad-bc}$$

    Observe that the solution has sense, since $u,v$ are no proportionals, $a,c$ and $b,d$ can't be zero at the same time so $ad - bc \neq 0$


    And:

    $$\dfrac{d-c}{ad-bc} u + \dfrac{a-b}{ad-bc} v = (1,0) + (0,1) = e_1 + e_2$$

    Observe that (without the need to invocate orthogonality or basis), we can ensure that, being $w = (x,y) \in \mathbb{R}^2$, then is:

    $$w = \dfrac{x(d-c)}{ad-bc} u + \dfrac{y(a-b)}{ad-bc} v \quad \forall w \in \mathbb{R}^2$$

    Meaning, with two non-proportional vectors, we can reach any other element in $\mathbb{R}^2$ thus the spanned subspace $V$ of the subset $S := \Set{u,v \mid \nexists \alpha \in \mathbb{R} : u = \alpha v} \subset \mathbb{R}^2$ is $\mathbb{R}^2$ it self.

    Thus, observe that for any $W \leq V$, then if $W$ contain at least two non-proportional vectors then $W = \mathbb{R}^2$, since a vector space contain all the linear combination of his vectors, if do not then is either a line or the zero subspace.

    <br>

3. **Can you describe the subspaces of R3?**

    Extending the argumentation in $2.$ is the zero subspace, those subspaces for which exists at least three independant vectors (one vector which is not linear combination of other two) which spans $\mathbb{R}^3$, then those subspaces with at least two non-proportional vectors which are planes and those with all his vectors proportionals which are lines.

    <br>

#### 2.4.5.7. Union of subspaces.

Let $W\_1, W\_2 \leq V$ be subspaces of a vector space such that the set-theoretic
union of $W\_1$ and $W\_2$ is also a subspace. Prove that one of the spaces $W\_i$ is contained in the other. 

<br>

Let's consider some interesting visual approach about the union of subspaces. Consider $\mathbb{R}^2$, then consider two non proportional vectors and the spanned subspaces of each of them, which are two distinct lines crossing in the origin. Is easy to see that a linear combination of the vectors of each line can fall out of each line since the subspace containing two non-proportional vectors coincides with $\mathbb{R}^2$. This means that the union of the two lines doesn't contains all his linear combinations so is not a subspace. For the union to be a subspace, each linear combination should end up as vector of one of the lines wich is pretty much to say that is proportional to one of the vectors of the linear combination but observe that this also implies that the third vector is also proportional so to the two lines are the same.

<br>

Then, generalizing:

$$\bigcup_i W_i \leq V \implies w = u + v \in \bigcup_i W_i \quad \forall u \in W_1, \forall v \in W_2$$

Then, suppose $w \in W_i \implies v  = w - u \in W_i$, observe that this means that we can't consider simulatenously $u \in W_i \setminus W_j$ and $v \in W_j \setminus W_i$ since the last afirmation would be false.

<br>

#### 2.4.5.8. Even and odd function subspaces. Direct Sum.

Consider $\mathbb{R}^\mathbb{R}$ and the following subsets:

$$A := \Set{f \in \mathbb{R}^\mathbb{R} \mid f(-x) = f(x)}$$
$$B := \Set{f \in \mathbb{R}^\mathbb{R} \mid f(-x) = -f(x)}$$

Then, prove that:

1. Both subsets are subspaces of $\mathbb{R}^\mathbb{R}$

    Observe that:

    $$(\alpha f + g)(-x) = \alpha f(-x) + g(-x) = \begin{cases} \alpha f(x) + g(x) = (\alpha f + g)(x) \quad \forall f,g \in A \\ -\alpha f(x) - g(x) = -(\alpha f + g)(x) \quad \forall f,g \in B \end{cases}$$

    So both contains the linear combinations of his own elements so their are subspaces.

    <br>

2. $A + B  = \mathbb{R}^\mathbb{R}$

    Let's suppose that $f \in \mathbb{R}^\mathbb{R}$, then let's suppose also $g \in A$ and $h \in B$ such $f = g + h$, observe that this functions verifies at the same time:

    $$\begin{cases}f(x) = g(x) + h(x) \\ f(-x) = g(-x) + h(-x) = g(x) - h(x) \end{cases}$$

    In this context is, combining both equatlities we get:

    - $g(x) =  \frac{1}{2}[f(x) + f(-x)]$
    - $h(x) =  \frac{1}{2}[f(x) - f(-x)]$

    So is:

    $$f(x) = \frac{1}{2}[f(x) + f(-x)] + \frac{1}{2}[f(x) - f(-x)] $$
   
   <br>

3. $A \cap B = \Set{0}$

    Observe that this is almost immediate, suppose some common function from $A \cap B$, then:

    $$f(x) = \frac{1}{2}(f(-x) - f(-x)) = 0 \quad \forall x \in \mathbb{R}$$

    <br>

Observe that we have demonstrated that two disjoint subspaces $A,B \leq \mathbb{R}^\mathbb{R}$ sum the total space:

$$A,B \leq \mathbb{R}^\mathbb{R} : A \oplus B \iff (A \cap B =\Set{0} \wedge A + B = \mathbb{R}^\mathbb{R})$$

Observe that this allows to dispose every vector of $\mathbb{R}^\mathbb{R}$ in terms of two componentes of $A$ and $B$.

<br>

#### 2.4.5.9. Property of direct sum.

Let $W_1, W_2$ subspace such are direct sum of $V$. Prove that for each vector $\alpha \in V$ there are unique vectors $\alpha\_1 \in W\_1$ and $\alpha\_2 \in W\_2$ such that $a = \alpha\_1 + \alpha\_2$.

<br>

Take $a \in V$ and suppose that is $a = \alpha\_1 + \alpha\_2 = \beta\_1 + \beta\_2 : \alpha\_i, \beta\_i \in W\_i$ with $i = 1,2$, then observe that it cannot be $\alpha\_i - \beta\_j = 0$ since that would imply $\alpha\_i \in W\_j$ or $\beta\_j \in W\_i$ contradicting the premise that both subspaces do not share not-null vectors, so it can only be $\alpha\_i - \beta\_i = 0 : i = 1,2$, so both vectors are the same exact vector.

<br>

# 3. Dependence, Bases and Dimension.

## 3.1. Conceptal introduction.

Let's first introduce what a basis is, a *basis* is the minimum set of a vector space which contains all the information the vector space is capable to express. Meaning that is the minimum set of vectors that spans the vector space; any vector is reachable trough a linear combination of the elements of a basis and at the same time this set is minimum, any subset of a basis is uncapable to span the vector space.

The *dimension* of the vector space is the number of "degrees of freedom" that a vector space has; the number of independent vector required to specify an arbitrary vector materialized in the cardinal number of the basis set.

This two concepts has a fundamental importance; the dimension is the fundamental invariant that clasifies vector spaces, and the basis what transform linear algebra (operation with vectors) in matrix computations.

<br>

## 3.2. Linearly dependent/independent.

Let first introduce the concept of dependant and independant linearity. 

Let be $V$ a $K$-vector space and $S \subset V$ and $n \in \mathbb{Z}^+$. Then:

- $S$ is said to be *linear dependant* if and only if: 

    $$\exists \alpha_1,\ldots, \alpha_n \in S \text{ distinct}, \exists c_1,\ldots, c_n \in K \text{ not all 0} : \sum_{i=1}^n c_i\alpha_i = 0$$

    <br>

- $S$ is said to be *linear independant* if and only if is not dependant, negating the above we get

    $$\forall \alpha_1,\ldots, \alpha_n \in S \text{ distinct}, \forall c_1,\ldots, c_n \in K \text{ not all 0} : \sum_{i=1}^n c_i\alpha_i \neq 0$$

    Observe that we can convert the statement by quitting the "not all 0" obtaining:

    $$\forall \alpha_1,\ldots, \alpha_n \in S \text{ distinct}, \forall c_1,\ldots, c_n \in K : \sum_{i=1}^n c_i\alpha_i = 0 \iff c_i = 0 \quad \forall i \in [n]$$

    <br>

Let's observe this more carefully, check something interesting, a subset of vectors of a vector space is said to be *dependant* when it can reference the zero vector, $0$ through a non-trivial linear combination.

Take $S$ to have only two vectors, $u,v \neq 0 \in V$, then if $S$ is linear dependant, we have:

$$\exists \alpha,\beta\neq 0 \in K : \alpha u + \beta v = 0 \iff u = \frac{-\beta}{\alpha}v$$


Meaning that linear dependan, in this case refers to *proportionality*, in the sense that we can retrieve one from the other without involve any other vector, so we can say that both contains the same information, both are the same type of vector so to speak and is repeated in $S$. 

Let's suppose that we expand $S$ with $w = tu + lv \neq 0 : t,l \neq 0 \in K$, then observe that this three vectors can again reference the zero vector, $tu + lv -w = 0$ through a finite non-trivial linear combination. We can think in $w$ as a proportional vector to a combination of $u,v$, thus $w$ and $u,v$ contains the same information despite scaling. Observe also that, nevertheless, $w$ could be accompanied with a zero scalar and $S \cup \Set{w}$ would still be a dependant set of vectors.

<br>

Let's also consider that $u = 0$, then $S := \Set{0,v}$ with $v \neq 0$ then observe that $0·v + 1·0 = 0$. This makes $S$ a dependent set, in the sense that again, it contains prescindible information, the $0$ vector does not contains adicional information in any sense, observe that if $span(S)$ is the minimum vector space that contains $S$ (the intersection of all vector spaces containing $S$), then $span(\varnothing) = \Set{0}$, the zero-space is the vector space generated by an empty set, without information.

<br>

Thus, **the essense of linear dependence is linear redundancy**, understanded as information that do not expand what can be expressed by the span of the set and can be free. 

A set of vectors is said to be linear dependent when the whole set can express a part and the counterpart leading to a cancelation through a non-trivial linear combination. Meaning that in some sense one or more vectors carries complete prescindible information, then the scalars allows to modulate how much a vector express him self leading to a linear combination that express a zero reference as we saw above. 

Is easy to see that $S$ in the example before has the same vector two times, (proportionality as repeated information) thus any subset containing $S$ is also dependant since it inheritate the repeated information. In the second example, $S$ just contains the trivial case in which the zero vector refers to him self; $0$ can express at the same time his own and his negative, $0 = 0 + (-0)$, hence is redundant following our criteria. 

Linear independence is just the negation of this statement; a set of vectors is said to be linear independent when all vectors contribute with some non-replicable information, or, in other terms, substract any vector in the set implies to loose information.

Let's see some easy consequences of the definition.

1. Any set which contains a linearly dependent set is linearly dependent.
2. Any subset of a linearly independent set is linearly independent.
3. Any set which contains the 0 vector is linearly dependent; for $1 · 0 = 0$. Observe that $0$ as a vector is prescindible it self and redundant in any context, combine a vector with $0$ doesn't change anything. In fact, observe that $span(\varnothing) = 0$.

    <br>

### 3.2.1. Examples.

Consider $K$ a field, then in $K^3$ the vectors:

$$\begin{cases} \alpha_1 = (3,0,-3) \\ \alpha_2 = (-1,1,2) \\ \alpha_3 = (4,2,-2) \\ \alpha_4 = (2,1,1)\end{cases}$$

Satisfies:

$$2\alpha_1 + 2\alpha_2 - \alpha_3 + 0 · \alpha_4 = 0 $$

So are linear dependant. Note that $\Set{\alpha\_1, \alpha\_2, \alpha\_3}$ are linear dependant as well, hence, any set containing this vectors is also linear dependant.

<br>

The vectors:

$$\begin{cases} \alpha_1 = (1,0,0) \\ \alpha_2 = (0,1,0) \\ \alpha_3 = (0,0,1)\end{cases}$$

Are linear independant.

<br>

## 3.3. Basis definition and examples.

### 3.3.1. Basis definition.

Let $V$ be a vector space. 

A basis, $\mathcal{B}$, of $V$ is a set satisfying:

- $\mathcal{B}$ is linearly independent. Again, loose some vector implies a lost of information.

- $\mathcal{B}$ spans the space $V$. 

Thus, a basis is an independent generator of a vector space; each vector of $\mathcal{B}$ contains some non-replicable information about $V$.

<br>

Let's observe here that we are giving continuity to the dependence/independence frame but we are adding generators sets in the process. A basis is nothing more that the combination of two objects:

- A generator set, this is; a set which contains all the information that the vector space can express.

- An independent set, a set from which you can't free any element without loose information.

This two objects gives us a compress notion; a basis is the minimal generator set of a vector space; substracting a vector make a piece of information to get lost, so the span doesn't hold. This will be explain in a later theorem.

<br>

### 3.3.2. Examples.

#### 3.3.2.1. Standard basis of $K^n$.

Let $K$ be a field and in $K^n$, consider the subset:

$$ \mathcal{B}: = \begin{cases} \alpha_1 = (1,0,0,\ldots, 0) \\ \alpha_2 = (0,1,0,\ldots,0) \\ \alpha_3 = (0,0,1,\ldots,0) \\ \quad \vdots \\ \alpha_n = (0,0,0,\ldots,1) \end{cases}$$

At first, observe that for any $x = (x_1,x_2,\ldots,x_n) \in K^n$ is:

$$x = \sum_{i=1}^n \alpha_i x_i$$

So $\mathcal{B}$ spans $K^n$ and also is linear independent as we see in the particular case with $K^3$. So $\mathcal{B}$ is a basis of $K^n$, particularly called **standard basis**.

<br>

#### 3.3.2.2 Invertible matrix and basis.

Let's consider some $P \in M_n(K)$ invertible. We do know that $P \simeq I_n$, which means that no row in $P$ can be zeroed through a linear combination of the other rows in $P$ so the set of the rows in $P$ forms a linear independent set. Observe that, in more simple terms, be $X \in K^{n\times 1}$, then, by $6.3.3$ in [Linear Equations](https://gsanmi1.github.io/posts/2026/02/06/Linear_Equations/):

$$\exists P^{-1} \iff (PX = 0 \iff X = 0)$$

Thus, $PX = \sum_{i=1}^n x\_iP\_i = 0 \iff x\_i = 0 \quad \forall i \in [n]$, meaning that $\Set{P_1, \ldots, P_n}$ is a linear independent set. 

And also, as we see above, it spans any column on $K^{n \times 1}$ so $\Set{P_1, \ldots, P_n} \subset K^{n \times 1}$ is in fact a basis of $K^{n \times 1}$.

<br>

Let's observe that we are saying that in $K^n$, a basis and an invertible matrix is literally the same object. Is the naturall continuity to the conception of matrix seen as linear-information codified packeges viewed in [Linear Equations](https://gsanmi1.github.io/posts/2026/02/06/Linear_Equations/).

The columns of any invertible matrix become a basis of the same matrix-dimension tuple vector space, in a way that the coordinates of any vector in terms of that basis becomes the solution of a linear equation system. Again from $6.3.3$ in the post above the solution is unique so:

$$\forall Y \in K^{n \times 1} \ \exists ! X \in K^{n \times 1} :  \quad (PX = Y \iff X = P^{-1} Y)$$

<br>

#### 3.3.2.3. Basis of non-squared matrix vector spaces.

Let $A \in M_{m \times n}(K)$ and let $S := \Set{X \mid AX = 0}$ the solution on the homogeneous system. Take the $RREM$, $R \simeq A$, then, $RX=0$ share the space solution. 

Observe that since $R$ is $RREM$, it has $r$ non-zero rows, which allow to clear $r$ unknowns in terms of $n-r$ unknowns, be $J$ the set of the index of the uncleared unknowns, then $RX = 0$ is equivalent to the system:

$$\begin{cases} x_1 = \displaystyle\sum_{i = 1}^J \alpha_{1i} x_i \\ \quad \vdots \\ x_r = \displaystyle\sum_{i = 1}^J \alpha_{ri} x_i\end{cases}$$

All solution are retrieved by giving values to the dependent unknowns assigning arbitrary values to the independent unknows, those with and index in $J$.

Observe then that, be $j \in J$ then consider $E\_j$ the solution by giving $x\_j=1$ and $x_i=0$ for any other $i \in J$. Observe since the solutions are indeed linear combinations of the independent unknowns, then any arbitrary solution are is a linear combination of the family $\Set{E\_j}\_{j \in J}$ as described above and also is clear that are linearly independant so is a basis.

<br>

#### 3.3.2.4. Infinite Basis.

Let's note first that an infinite basis do not introduce infinite sums, each vector gets obtained through a finite linear combination. Which is infinite is the generator engine, the basis it self which, algebraicly speacking, means that there is only no finite basis at all. The richness of infinite-dimensional theory (functional analysis, operators) lies not in the vector space structure itself, but in the additional structure superimposed upon it.

<br>

Take some subfield $W \subset \mathbb{C}$, and consider $Pol(W,W)$, remember:

$$Pol(W,W) := \Set{f \in W^W \mid \exists n \in \mathbb{N}:(\exists \alpha \in \mathbb{C}^n : f(x) = \sum_{i=0}^n \alpha_i x^i \quad \forall x \in W )}$$

Note then that, for any $f \in Pol(W,W)$, it takes the form:

$$f(x) = \alpha_0 + \alpha_1 x + \ldots + \alpha_n x^n$$

Let's call $f\_n(x) = x^n$, then the family $\Set{f\_n}\_{n \in \mathbb{N}}$ is a basis over $Pol(W,W)$. 

First, is clear that it can generate any element of $Pol(W,W)$, but let's also see that they are independent. We do know that a set is independent if any linear combination of his elements is $0$, it would be sufficent to proove that for any $n$, the finite family $\Set{f\_0,f\_1,\ldots,f\_n}$ is independent, then, for some $n$ is:

$$\sum_{i=0}^n \alpha_i f_i = \alpha_0 + \alpha_1 x + \cdots + \alpha_n x^n = 0$$

We assume that the reader knows that a polynomial of degree $n$ with complex coefficients cannot have more than $n$ distinct roots. It follows that $\alpha\_0 = \cdots = \alpha\_n = 0$. 

<br>

## 3.3. Dependence, Basis and Dimension results.

### 3.3.1. Maximum independent vectors of a spanned vector space.

**Let be $V$ the vector space spanned by $v_1,\ldots, v_n$, then the maximum number of independent vectors in $V$ is no greater than $n$.**

Take some $A \subset V : \| A \| = m > n$ and $S=\Set{v_i}_{i \in [n]}$ the generator subset of $V$, then:

$$\forall i \in [m] \ \exists \alpha_{i1},\ldots,\alpha_{in} \in K : u_i = \sum_{j=1}^n \alpha_{ij}v_j \in A$$

Giving place to the following linear equation system:

$$\begin{cases}\alpha_{11}v_1 \cdots + \alpha_{1n}v_n = u_1 \\ \quad \vdots \\ \alpha_{m1}v_1 \cdots + \alpha_{mn}v_n = u_m \end{cases} \iff \begin{pmatrix} \alpha_{11} & \cdots & \alpha_{1n} \\ \ \vdots & \quad  & \vdots \\ \alpha_{m1} & \cdots & \alpha_{mn}\end{pmatrix} \begin{pmatrix} v_1 \\ \vdots \\ v_n\end{pmatrix} =\begin{pmatrix} u_1 \\ \vdots \\ u_n\end{pmatrix}$$

Note that since $m > n$, then the $RREM$ form of the matrix has at least $m-n$ zero rows, meaning that, exists $m-n$ non-trivial linear combinations over some $u$ vectors referencing $0$, so exists scalars, not all zero, such: $x_1u_1 \cdots +x_mu_m = 0$, so $A$ is dependent.

<br>

Essentially, since $S$ spans $A$, then we can't extend $S$ with non linear vectors, thus in $V$ which is $S$ aloing with all his linear combinations there cannot exists more linear independents vectors than the number of independent vectors in $S$.

<br>

### 3.3.2. Basis elements. Dimension.

**Two basis of the same vector space has the same number of elements.**

From the result above, neither of them can have more elements than the other since both are generators subsets with all his elements independent by definition, so if $\mathcal{B}_1, \mathcal{B}_2$ are two basis, from above we have:

$$\|\mathcal{B}_1\| \leq \|\mathcal{B}_2\| \wedge \|\mathcal{B}_2\| \leq \|\mathcal{B}_1\| \iff \|\mathcal{B}_1\| = \|\mathcal{B}_2\|$$

<br>

**Dimension**

Let observe that this allow us to present the *dimension* of a vector space definition as the number of vectors any basis of the vector space has.

Observe then, be $V$ a vector space with $dimV = n$, then any subset with more than $n$ vectors is dependant and no subset with less than $n$ vectors can span $V$.

<br>

An important minor example about dimensions is that the zero vector space $\Set{0}$ has dimension $0$. Observe that $\Set{0}$ is a dependent set so it cant be a basis, hence as a vector space $\Set{0}$ is spanned by the empty set. Observe that the intersection of all vector spaces containing the empty set (which is a subset of any set) is literally $\Set{0}$.

<br>

Let's also observe that if $V$ as a $K$-space has finite dimension, $dim V$ **is the amount of irreducible information that must be specified to determine an element of $V$, measured in terms of the field.** 

This basically means that *dimension* doesn't lives in the group, lives in the relation between the field and the group. If you change the field, the relation changes. 

- Consider for example $(\mathbb{C}, \mathbb{C}, ·)$, since the relation between the group and the field is one-to-one, you only need one component to express any other element and the dimension is $1$. 

- Consider now $(\mathbb{R}, \mathbb{C},·)$, this vectorspace has dimension $2$, hence you need two components, you need two refer two time s to $\mathbb{R}$ to map any complex. This is not coincidence, since the complex set is defined as the set of pairs of reals numbers, two reals for one complex.

- Observe now $(\mathbb{Q}, \mathbb{R}, ·)$, in this case, this space has no finite dimension, this is because $\mathbb{R}$ get's formed through segments of $\mathbb{Q}$, in the sense that $\mathbb{R}$ is $\mathbb{Q}$ an infinite number of times.

<br>

### 3.3.3. Independent set extension.

**Consider $V$ a vector space and $S$ a subset of independent vectors of $V$. Consider $v \in V : v \notin span(S)$, then $S \cup \Set{v}$ is a set of independent vectors of $v$.** 

<br>

Is immediate, if not, it would be a non-trivial linear combination referencing zero involving $S$ elements plus $v$, which will allow us to put $v$ as a linear combination of the vectors of $S$ contradicting the premise of $v \notin span(S)$ or in other hand $S$ is a dependant set it self contradicting again the premise.

<br>

### 3.3.4. Basis of subvector-spaces.


**Consider some finite-dimensional vector space $V$ and $W \leq V$, then any finite linearly independent subset of $W$ is finite and part of a basis of $V$.**

<br>

Take $V : dimV = n$ and let's obvious the case in which $W = V$, then the result would be trivial and immediate.

In $V$ there cannot be more than $n$ independentent vectors from $3.5.1$, and by the fact that $W \subset V$ for being a strict subspace, any set of independent vectors of $W$ is a set of independent vectors in $V$ so in $W$ it cannot exists more than $n$ indenpendent vector as well, hence, any subset of independent vectors in $W$ is finite.

<br>

Now, consider some subset of independent vectors of $S \subset W$. As much is $span(S) \subseteq W < V$.

Thus, $span(S) \subset V$ and exists at least one vector $v \in V \setminus span(S)$. 

By $3.5.3$, $v \notin span(S) \implies S \cup \Set{v} \text{ is indepedent }$. Then we repeat the argument, if $S \cup \Set{v}$ doesnt group $n$ vectors, then by $3.5.2$ it can't be a basis of $V$ so it do not span $V$ and again: 

$$span(S \cup \Set{v}) \neq V \implies \exists u \in V \setminus S \cup \Set{v} : S \cup \Set{u,v} \text{ is independent }$$

and so on, observe that this implies that $u,v$ are independent as well.

Eventually, we will get some finite set of independent vectors $L \subset V \setminus S : \mathcal{B} = S \cup L$ groups $n$ independent vectors, if $\mathcal{B}$ does not generate $V$ it would exists some $w \in V : \mathcal{B} \cup \Set{w}$ is independent but that cannot be since by $3.5.2$, in $V$ cannot exists more than $n$ independent vectors so $\mathcal{B}$ is a basis from which $S$ is part of it.

<br>

Observe that basically we are saying that: *In a finite-dimensional vector space $V$ every non-empty linearly independent set of vectors is part of a basis.*

<br>

**Consider some finite-dimensional vector space $V$ and $W \leq V$, then any finite linearly independent subset of $W$ is finite and part of a basis of $W$.**

Is the theorem above but changing $V$ with $W$. Observe that in this case we cannot refugee our selves in the dimension argumento to stop de iteration.

However, we can argue nearly the same. Consider some $S \subset W$ independent set then, if $span(S) \neq W$, there is some $w \in W: S \cup \Set{w} = S^\ast$ is independent. Observe that there is somepoint in which we cannot consider such $w \in W$ from the fact we stated above (everly linear independent set is finite), that would mean that $span(S^\ast)$ can generate any vector in $W$ so $W \subset span(S^\ast)$, and by definition is $S^\ast \subset span(S^\ast) \subset W$, so $span(S^\ast)=W$ and $S^\ast$ is a basis of $W$ taht contains $S$.


$$\big(\nexists\, w\in W:\ S^\ast\cup\{w\}\ \text{indep.}\big)\ \underset{\neg\exists=\forall\neg}{\equiv}\ \big(\forall w\in W:\ S^\ast\cup\{w\}\ \text{dep.}\big)\ \overset{\text{contra-}3.5.3}{\Longrightarrow}\ \forall w\in W:\ w\in\operatorname{span}(S^\ast)$$

<br>

**If $W$ is a proper subspace of a finite-dimensional vector space $V$, then $W$ is a finite-dimensional and $dim W < dim V$**

Suppose $W < V$ and $dim V, dim W \in \mathbb{N}$. Then:

- Suppose $dim W = dim V = n$. Immediately, any basis of $W$ would be a basis of $V$, hence it has to be both the same vector space $V = span(S) = W$, in contradiction with the premise $W < V$.

- It cannot be $dim W > dim V$ as well by the result above, any independent set of vectors of $W$ cannot be superior in number to $dim V$.

    <br>

So it has to be $dim W < dim V$ and $W$ is finite-dimensional.

<br>

### 3.3.5. Invertible Matrix and independent vectors.

Extending our example of $3.3.2.$ invertible matrix and basis, observe that an immediate result from above is that if $A \in M\_n(K)$ such the set of his $\Set{\alpha\_i}\_{i \in [n]}$ conforms a linear independent set, then $A \simeq I\_n$, if not, $A$ would be equivalent to some $RREM$ with a finite number of zero rows. With an argument similar than the one provided in the example, this would mean that it would exists some non-trivial linear combination of the rows of $A$ refering the zero-row, so $\Set{\alpha_i}\_{i \in [n]}$ would be a dependent set.

<br>

### 3.3.6. Characterization of the dimension of sum of subspaces.

**Take $U, W \leq V$ finite-dimensional subspaces, then $W + U$ is finite dimensional satisfying:**

$$dim (W + U) = dim W + dim U - dim (W \cap U) $$

<br>

First, remember that $W \cap U$ is a subspace of $V$ and is it self a subset of $W,U$, then since $V$ is a finite-dimensional vector space, $W\_1 \cap W\_2$ is as well finite dimensional and any basis of it, as a linear independent set ($3.5.4$), is part of a basis of $W\_1$ and $W\_2$. 

We can think in $\mathcal{B}\_1 : span(\mathcal{B}\_1) = W\_1$, $\mathcal{B}\_2: span(\mathcal{B}\_2) = W\_2$, and $\mathcal{B}\_3: span(\mathcal{B}\_3) =  W\_1 \cap W\_2$ such is $\mathcal{B}\_3 \subset \mathcal{B}\_1$ and $\mathcal{B}\_3 \subset \mathcal{B}\_2$.

Observe that, as constructed, $B\_1 \cup B\_2$ is linear independent (the common information exists in $\mathcal{B}\_3$, which has been used to form $\mathcal{B}\_1$ and $\mathcal{B\_2}$), is easy to prove by contridiction. We can make the partition:

$$\mathcal{B}_1 \cup \mathcal{B}_2 = (\mathcal{B}_1 \setminus \mathcal{B}_3) \sqcup (\mathcal{B}_2 \setminus \mathcal{B}_3) \sqcup \mathcal{B}_3$$

Observe naturally that: $W\_1 + W\_2 = span(\mathcal{B}\_1 \cup \mathcal{B}\_2) = span\big((\mathcal{B}\_1 \setminus \mathcal{B}\_3) \sqcup (\mathcal{B}\_2 \setminus \mathcal{B}\_3) \sqcup \mathcal{B}\_3\big)$, also each block form a completly disjoint subspace, then the sum of those subspaces are direct sum:

$$ span\big((\mathcal{B}_1 \setminus \mathcal{B}_3) \sqcup (\mathcal{B}_2 \setminus \mathcal{B}_3) \sqcup \mathcal{B}_3\big) = span\big(\mathcal{B}_1 \setminus \mathcal{B}_3\big) \oplus span\big(\mathcal{B}_2 \setminus \mathcal{B}_3\big) \oplus span\big( \mathcal{B}_3\big) = $$

$$= [W_1 \setminus (W_1 \cap W_2)] \oplus [W_2 \setminus (W_1 \cap W_2)] \oplus (W_1 \cap W_2)$$

<br>

As a brief commentary, remember that f is $W < V$, then $V \setminus W = V \cap \overline{W}$, which is a subspace as we know and is completly legit to consider a dimension of it.  Furthermore, $V$ is direct sum of both subspaces $V = (V \setminus W) \oplus W$, since is the union of complementary subsets, hence, if we consider a basis of each subspace we have that the union (which is disjoint) form a basis of $V$: $\mathcal{B}\_V = \mathcal{B}\_{V \setminus W} \sqcup \mathcal{B}\_W$, then:

$$W < V \implies dim V = dim(V \setminus W) + dim W \iff dim (V \setminus W) =  dim V - dim W$$

Thus:

$$dim (W_1 + W_2) = [dim W_1 - dim (W_1 \cap W_2)] + [dim W_2 - dim (W_1 \cap W_2)] + dim (W_1 \cap W_2) =$$

$$=dim W_1 + dimW_2 - dim (W_1 \cap W_2)$$

<br>

## 3.4. Exercises.

### 3.4.1. Prove that if two vectors are linearly dependent, one of them is a scalar multiple of the other. 

Consider some $V$ a $K$-space, then consider some set $S := \Set{u,v}$ and asume is dependent. Then, exists a non-trivial linear combination equal to zero:

$$\alpha u + \beta v = 0$$

Then, one of the scalar is not zero, suppose is $\alpha$, then:

$$u = \frac{- \beta}{\alpha} v$$

<br>

### 3.4.2. Are the following vectores linearly independent in $\mathbb{R}^4$:

$$\alpha_1=(1,1,2,4), \alpha_2=(2,-1,-5,2), \alpha_3=(1,-1,-4,0), \alpha_4=(2,1,1,6)$$

In order to check whether the vectors are linear dependendent or independent consist to prove if there exists a non-trivial linear combination (with not all scalars $0$) that reference the $0$ vector with the vectors of the exercise.

This eventually lead to form an homogeneous system with an associated matrix $AX = 0$. If this system has trivial solution, then $A$ is row-equivalent to $I\_4$ and the system is linear dependent, if not, this non-trivial linear combination exists and the set is linear dependent.

<br>

### 3.4.3. Find a basis for the subspace of $\mathbb{R}^4$ spanned by the four vectors of the previous exercise.

Doing the exercise before,we get that the range of the matrix is $2$ and the subspace formed by those 4 vectors is a plane. Reducing the matrix give us the following relation between the vectors:

$$\begin{cases} \alpha_1 - 2\alpha_2 + 3\alpha_3 = 0 \\ -4\alpha_1 - \alpha_2 + 3\alpha_4 = 0\end{cases}$$

Observe then that, $\alpha_3, \alpha_4$ can be expressed as linear combinations of $\alpha_1, \alpha_2$ and this two vectors are not proportionals, hence are linear independent.

Thus, $span(\alpha_1,\alpha_2, \alpha_3,\alpha_4) = span(\alpha_1,\alpha_2)$ and $\Set{\alpha_1, \alpha_2}$ is a basis of the proposed subspace of the exercise for be a independent generator set of the subspace.

<br>

### 3.4.4. Show that the following vectors form a basis on $\mathbb{R}^3$, express each vector from the standard basis as linear combinations of this ones:

$$u = (1,0,-1), \quad v = (1,2,1), \quad w = (0,-3,2)$$

Forming the equation system is clear that the only escalar that makes the linear combination $0$ is $0$ for each vector, so the linear combination is trivial and these are three independent vectors. Since the dimension of $\mathbb{R}^3$ is also $3$, you cannot expand the set $\Set{u,v,w}$ with more independent vectors from $\mathbb{R}^3$, or in other terms, $span(\Set{u,v,w}) = \mathbb{R}^3$ and the set is a basis of $\mathbb{R}^3$.

Lastly, we can again force a system to find each linear combiation to produce the canonical base $\Set{e_1,e_2,e_3}$.

<br>

### 3.4.5. Find three vectors in $\mathbb{R}^3$ which are linearly dependent, and are such that any two of them are linearly independent. 

$$\Set{(1,0,0),(0,1,0),(1,1,0)}$$

<br>

### 3.4.6. Respond the following questions. 

Take $V = M\_{2}(K)$, consider:

$$A := \Set{\begin{pmatrix} a_1 & -a_1 \\ a_2 & a_3\end{pmatrix} \mid a_i \in K \ \forall i \in [3]} \quad B:= \Set{\begin{pmatrix} b_1 & b_2 \\ -b_1 & b_3\end{pmatrix} \mid b_i \in K \ \forall i \in [3]}$$

Then:

**Prove that both sets are subspaces of $V$.**

Observe first that $A, B \neq \varnothing$. Thus, is inmediate that $u,v \in A \implies \alpha u + v \in A$ and the same with $B$. So $A,B \leq M_2(K)$.

<br>

**Find the dimension for: $A, B, A + B, A \cap B$.**

Let's observe that:

$$\forall u \in A \ \exists \alpha, \beta, \gamma  \in K : u = \begin{pmatrix} \alpha & -\alpha \\ \beta & \gamma \end{pmatrix} = \alpha \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} + \beta\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + \gamma \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} $$

$$= \alpha e_1 + \beta e_2 + \gamma e_3$$

Hence $span(\Set{e_1, e_2,e_3}) = A$. Also:

$$\alpha e_1 + \beta e_2 + \gamma e_3 = \begin{pmatrix} \alpha & -\alpha \\ \beta & \gamma \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0\end{pmatrix} \iff \alpha = \beta = \gamma = 0$$

So this set is a linear independent generator of $A$, this is; a basis of $A$.

<br>

Observe also that: $\forall u(u \in A \iff u^t \in B) \iff \Set{e_1^t,e_2^t,e_3^t} \text{ is a basis of } B$. 

Hence, we have that $dim A = dim B = 3$.

<br>

Also, take $A \cap B$, then:

$$u = \begin{pmatrix} u_1 & u_2 \\ u_3 & u_4 \end{pmatrix}  \in A \cap B \iff \begin{cases} u \in A \implies  u_2 = -u_1 \\ u \in B \implies u_3 = -u_1 \\ u_4 \in K \end{cases}$$

Thus, calling $u_1 = \lambda, u_4 = \varphi$, we have that:

$$\forall u \in A \cap B \ \exists \lambda, \varphi \in K : u = \begin{pmatrix} \lambda & - \lambda \\ - \lambda & \varphi \end{pmatrix} = \lambda \begin{pmatrix} 1 & - 1 \\ - 1 & 0 \end{pmatrix} + \varphi \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

Meaning that $\Set{e_1^\ast,e_3}$ is a basis of $A \cap B$. So, $dim A \cap B = 2$ and 

$$dim A + B = dim A + dim B - dim A \cap B = 4$$

<br>

### 3.4.7. 

**Again let $V$ be the space of $2 \times 2$ matrices over $F$. Find a basis $\Set{A_1, A_2, A_3, A_4}$ for $V$ such that $A_i^2 = A_i$ for each $i$.** 

Observe that be $A:=(a_{ij})_{i,j \in [2]}$, then: $AA = (\alpha_{ij})_{i,j \in [2]} : \alpha_{ij} = \sum_{k=1}^p a_{ik}a_{kj}$. Hence, let's call:

$$A := \begin{pmatrix}a_1 & a_2 \\ a_4 & a_3 \end{pmatrix}$$

Then, we define:

$$E_i:= A : \begin{cases} a_i = 1 \\ a_j = 0 \quad \forall j \neq i \in [4]\end{cases}$$

Is clear $\Set{E_i}_{i \in [4]}$ is a basis of $V = M_2(K)$, but also: $E_i^2 = 0 \quad \forall i \in [4]$. Hence, let's then define $H_i := E_i + E_{i+1}$. Clearly $\Set{H_i}_{i \in [4]}$ is a basis and $H_i^2 = H_i$ for each $i$.

<br>

### 3.4.8. Linear independence invariance under combination.

**Let $V$ be a vector space over a subfield $F$ of the complex numbers. Suppose $\alpha$, $\beta$, and $\gamma$ are linearly independent vectors in $V$. Prove that $(\alpha +  \beta), (\beta + \gamma)$ and $(\gamma + \alpha)$ are linearly independent.**

Is clear that be:

$$a,b,c \in F : a(\alpha +  \beta) + b(\beta + \gamma) + c(\gamma + \alpha) = 0 \iff 2a = 2b = 2 c = 0$$

Since $F \leq \mathbb{C} \implies 2 \neq 0$, thus $a = b = c = 0$ and the three vectors are linear independent.

<br>

### 3.4.9. Finite dimensional spaces.

**Let $V$ be a $K$-vector space. Suppose there are a finite number
of vectors $v_1, \ldots , v_n \in V : span(\Set{v_1, \ldots v_n}) = V$. Prove that V is finite-dimensional.**

Observe that, if $S = \Set{v_1,\ldots,v_n}$ spans $V$, then in $V$ there is as much $\| \Set{v_1,\ldots,v_n}\|$ independent vectors, or any independent subset of vectors of $V$ have as much $n$ vectors.

Since any basis is by definition an independent set, no basis can have more than $n$ vectors, hence is finite and $dimV$, as the number of vectors of a basis, is a natural number, thus $V$ is finite-dimensional.

<br>

### 3.4.10. 

Let $V$ be:

$$V := \Set{(a_{ij})_{i,j \in \mathbb{N}} \in M_2(\mathbb{C}) \mid \sum_{i}a_{ii} = 0}$$

Then, prove:

**V is a $\mathbb{R}$ vector space with the usual operation of adding and scaling**

In basic terms, the statement is asking us to prove that:

- $(V,+)$ is an abelian group.
- $\cdot : \mathbb{R} \times V \to V$ is a field's action over $V$.

    <br>

First, let's see that $(V,+)$ is a subgroup of $(M_2(\mathbb{C}),+)$. 

- $V$ is not empty, $0 \in V$. Also, is clear that $V \subset M_2(\mathbb{C})$ by definition.

- Lastly, $V$ contains the composition of any pairs of elements in $V$.

    $$(a_{ij}),(b_{ij}) \in V \implies \Big( \sum_i a_{ii} = 0 \wedge \sum_i b_{ii} = 0 \Big)\implies$$
    
    $$\implies \sum_i (a_{ii} + b_{ii}) = 0 \implies (a_{ij}) + (b_{ij}) = (a_{ij} + b_{ij}) \in V$$

    <br>

Second, let's see that $\cdot : \mathbb{R} \times V \to V$ is a field's action.

Observe that we can consider $· : \mathbb{R} \times M_2(\mathbb{C}) \to M_2(\mathbb{C})$ which is a field's action, then consider the restriction $·\mid_V$, let's see that $v \in V \implies  \alpha v \in V$ since $\sum_i \alpha v_{ii} = \alpha (\sum_i v_{ii}) = \alpha 0 = 0$, thus the codomain is $V$. And we can consider $·\mid_V$ as a field's action over $V$.

<br>

**Find a basis for $V$**

Consider: 

$$e_1 =\begin{pmatrix}1 & 0 \\ 0 & -1 \end{pmatrix}, \quad e_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad e_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$

<br>

Then, is obvious that $\Set{e_1, e_2, e_3}$ is an independent set. Then:


$$\forall v ( v\in span(\Set{e_1, e_2, e_3}) \implies \sum_i v_{ii} = 0 \implies v \in V)$$

Take then $v \in V \implies \sum_i v_{ii} = 0 \iff v_{22} = -v_{11}$, thus:

$$v = \begin{pmatrix}v_{11} & v_{12} \\ v_{21} & -v_{11} \end{pmatrix} = v_{11}\begin{pmatrix}1 & 0 \\ 0 & -1 \end{pmatrix} + v_{12}\begin{pmatrix}0 & 1 \\ 0 & 0 \end{pmatrix} + v_{21}\begin{pmatrix}0 & 0 \\ 1 & 0 \end{pmatrix} = $$

$$= v_{11}e_1 + v_{12}e_2 + v_{21}e_3 : v_{11},v_{12},v_{21}$$

Observe that this entries are complex numbers, each $v_{ij} = a_{ij} +b_{ij}i$ but the field's action do not contemplate complex expressions, this means that we need to extend our previous basis with:

$$e_4 =\begin{pmatrix}i & 0 \\ 0 & -i \end{pmatrix}, \quad e_5 = \begin{pmatrix} 0 & i \\ 0 & 0 \end{pmatrix}, \quad e_6 = \begin{pmatrix} 0 & 0 \\ i & 0 \end{pmatrix}$$


To state: 

$$v = v_{11}e_1 + v_{12}e_2 + v_{21}e_3 =$$

$$ = a_{11}e_1 + b_{11}e_4 + a_{12}e_2 + b_{12}e_5 + a_{21}e_3 + b_{21}e_6 : a_{ij},b_{ij} \in \mathbb{R} \ \forall i,j \in [2]$$

<br>

In other words, $V$ is a $3$ dimension $\mathbb{C}$-space or a $6$ dimensional $\mathbb{R}$-space. This means that the dimension is not a property of the set, as long as you restrain the scalars field, you need more vectors to express the same information.

<br>

**Consider the set $W := \Set{ (a_{ij}) \in V \mid a_{21} = - \overline{a_{12}}}$, prove that $W \leq V$**

First, $W$ is not empty, since $0 \in W$, also, by definition $W \subset V$, ultimately:

$$u,v \in W \implies u_{21} + v_{21} = (-\overline{u_{12}}) + (-\overline{v_{12}}) = -(\overline{u_{12}} + \overline{v_{12}}) = - (\overline{u_{12} + v_{12}}) \implies u + v \in W$$

And $W \leq V$.

<br>


# 4. Coordinates.

## 4.1. Ordered pair. Tuples.

Let's consider some superset $X$ and $a,b \in X$, then we define

$$(a,b) := \Set{\Set{a},\Set{a,b}}$$

This is what we call an *ordered pair*. Recursively, taking some $n \in \mathbb{Z}^+ : n > 2$ we define the *$n$-tuple* as:

$$(a_1,a_2, \ldots, a_n) : = (a_1,(a_2, \ldots a_n)) = \Set{\Set{a_1}, \Set{a_1,(a_2,\ldots,a_n)}}$$

If $a_i \in X$ for each $i \in [n]$, we should call $X^n$ to the set off all the $n$-tuples of elements of $X$.

Then, let's observe that a set is simply a collection of elements from the superset according to some criterion. This is, given some criteria about some universe of elements, then a set gather all the posible instantiations of the criterion in terms of the elements of the universe. Think for example in $\mathbb{Z}$ and take $2\mathbb{Z}$ which is the collection of those integers such the integer is even. (Also a set can be defined "by extension", this is; giving a complete enumeration of his elements, in that case, the criterion gets autodefined; an element is in the set if and only if it coincides with one of the enumerated elements).

In any case, giving some criterion, a "set" stablish what distinct elements exists or can be contemplated according to the criterion's perspective.

<br>

Now, an ordered pair is a set of two sets; one of them containing an element and the other both. 

This is, relative to the two elements, an ordered pair stablish a preference between the two elements, asserting that you can consider the first alone or both but never the second alone, since is not at the same level than the first one. The tuple extend this preference relation to all the list by nesting the elements inside the two elements set and so on.

$$(a_1,a_2, \ldots, a_n) = \Set{\Set{a_1},\Set{a_1,\Set{\Set{a_2},\Set{a_2,...\Set{\Set{a_{n-1}},\Set{a_{n-1},a_n}}}}}}$$

<br>

Observe that if $a \neq b$, while $\Set{a,b} = \Set{b,a}$ is $(a,b) \neq (b,a)$ and:

$$(a,b) = (c,d) \iff a = c \wedge b = d$$

Which extends to the tuple as:

$$(a_1,\ldots,a_n) = (b_1,\ldots,b_n) \iff a_i = b_i \quad \forall i \in [n]$$

Ultimately a tuple disregard the criterion comparison and prorize the preference relation to distinguish between elements. Observe that an element of the tuple is caracterized by the position and the value, but it prefers position before value; since distinct positions elements are never compared to stablish equality between tuples so repeated values do not mean same tuple if at least two of thems are in different nesting levels.

<br>

## 4.2. Linear dependence in Tuples.

Until now, we defined the linear dependence with sets. We said that linear dependence abstracts linear redundance. A set of vectors is linear dependent if there is a non-trivial linear combination referencing the $0$ vector.

<br>

Then, we define the linear dependence of tuples as follows. Be the $K$-space $V$, then we say that:

$$(v_1, \ldots, v_n) \text{ is linear dependent } \iff \exists (\alpha_1,\dots,\alpha_n) \in K^n \setminus \Set{0} : \sum_{i = 1}^n \alpha_iv_i = 0$$

By negation we obtain:

$$(v_1, \ldots, v_n) \text{ is linear independent } \iff \forall (\alpha_1,\dots,\alpha_n) \in K^n \setminus \Set{0} : \sum_{i = 1}^n \alpha_iv_i \neq 0$$

$$ \iff \Big( \sum_{i = 1}^n \alpha_iv_i = 0 \iff (\alpha_1, \ldots, \alpha_n) = 0 \in K^n \Big)$$

As we discuss before, $(v_1, \ldots, v_n)$ distinguish not only between value but also by position, two same values in different positions are different elements. Let's form from the tuple $(v_1, \ldots, v_n)$ the set of his elements $\Set{v_1,\ldots,v_n}$ note that this set do not tolerate different elements and:

Hence, is clear that:

$$(v_1,\ldots,v_n) \text{ is linear independent } \implies \Set{v_1,\ldots,v_n} \text{ is linear indepent}$$

And negating it:

$$\Set{v_1,\ldots,v_n} \text{ is linear dependent} \implies (v_1,\ldots,v_n) \text{ is linear dependent}$$

However and this is the key of the matter it is possible that $(v_1,\ldots,v_n)$ is linear dependent while $\Set{v_1,\ldots,v_n}$ is linear independent..

<br>

## 4.3. Ordered Basis. Coordinates.

If $V$ is a $n$-dimensional $K$-space, an ordered basis for $V$ is a linear independent $n$-tuple of vectors that spans $V$.

$$\mathscr{B} := (v_1,\ldots,v_n) \text{ is a basis of } V \iff \begin{cases} (v_1,\ldots,v_n) \text{ is linear independent } \\ span(\Set{v_1,\ldots,v_n}) = V \end{cases}$$

Then, an ordered a *coordinate system* is what you get when you define an isormorphism $\varphi_{\mathscr{B} }$ between a $V$ and an standard model, in this case and for the purpouses of the section; $K^n$ through $\mathscr{B}$.

$$\varphi_\mathscr{B}  : K^n \to V  \mid  \varphi_{\mathscr{B} }(\alpha_1,\ldots,\alpha_n) = \sum_{i=1}^n \alpha_i v_i : v_i \in \Set{v_1,\ldots,v_n}  \quad \forall i \in [n]$$

Let's see first that $\varphi_{\mathscr{B}}$ is an isormorphism by demostrating is a biyective homomorphism:

- First, let's see that is biyective. Take a given ordered basis $\mathscr{B}$. Then, for any vector there is a tuple, becuase the basis span $V$. Let's see also that there is a unique tuple for any vector, this immediate from the tuple definition:

    $$(\alpha_1,\ldots,\alpha_n) = [v]_{\mathscr{B}} =  (\beta_1,\ldots,\beta_n) \iff \alpha_i = \beta_i \quad \forall i \in [n]$$

    Hence, $\varphi_{\mathscr{B}}$ is a biyection.

    <br>
    
    
- Second, take two tuples and consider their images, is easy to see that $\varphi_\mathscr{B}$ respects linearity between vectors, hence is an homomorphism.

<br>

From now on, we will use:

$$[v]_{\mathscr{B}} = \begin{pmatrix}\alpha_1 \\ \vdots \\\alpha_n \end{pmatrix}: \alpha_i \in K \quad \forall i \in [n]$$

Hence, we define: $v = [v]_{\mathscr{B}} \mathscr{B}$

$$v = \mathscr{B} [v]_{\mathscr{B}} = \begin{pmatrix}v_1, \cdots, v_n\end{pmatrix}  \begin{pmatrix}\alpha_1 \\ \vdots \\\alpha_n \end{pmatrix} $$

To refer to the same object, he coordinate matrix of $u$ relative to the ordered basis $\mathscr{B}$.

<br>

## 4.4. Change of basis matrix.

**Let' be $V$ an $n$-dimensional $K$-space and two ordered basis, $\mathscr{B}, \mathscr{B}'$, then:**

$$\exists P! \in M_n(K) : P \simeq I_n \ \Big([v]_{\mathscr{B}} = P [v]_{\mathscr{B}'} \iff P^{-1}[v]_{\mathscr{B}} = [v]_{\mathscr{B'}} \quad \forall v \in V \Big)$$

**$P$ is called *change of basis* matrix.**

<br>

Take that $\mathscr{B}:= (u_1,\ldots,u_n)$ and $\mathscr{B}':=(w_1,\ldots,w_n)$, then each $w_i$ can be put in terms of $\mathscr{B}$ as:

$$\begin{cases} w_1 = x_{11}u_1 + \cdots x_{1n}u_n = [w_1]_{\mathscr{B}} \\ \quad \vdots \\ w_n = x_{n1}u_1 + \cdots x_{nn}u_n = [w_n]_{\mathscr{B}}\end{cases} \implies P = \begin{pmatrix}[w_1]_{\mathscr{B}}, \ldots, [w_n]_{\mathscr{B}} \end{pmatrix}$$

Then, at this point, let's call $P$ to the *matrix of the coordinates of $\mathscr{B}'$ in terms of $\mathscr{B}$*, observe that $P$ is unique since the scalars are unique for each vector. Then let's take some $v \in V$, again, since the tuple is unique for each ordered basis is:

$$v =\mathscr{B}' [v]_{\mathscr{B}'} =  \begin{pmatrix}w_1, \cdots, w_n\end{pmatrix} \begin{pmatrix}\alpha_1 \\ \vdots \\ \alpha_n \end{pmatrix} = \begin{pmatrix}u_1, \cdots, u_n\end{pmatrix} \begin{pmatrix}x_{11} & \cdots & x_{n1} \\ \vdots &  & \vdots \\ x_{1n} & \cdots & x_{nn}\end{pmatrix}  \begin{pmatrix}\alpha_1 \\ \vdots \\ \alpha_n \end{pmatrix} = $$

$$ = \begin{pmatrix}u_1, \cdots, u_n\end{pmatrix} \begin{pmatrix}\sum\alpha_i x_{i1} \\ \vdots \\ \sum \alpha_i x_{in}\end{pmatrix}  = \mathscr{B}[v]_{\mathscr{B}}$$

Hence this matrix chang from $\mathscr{B}'$ to $\mathscr{B}$. Observe that, since the basis are formed by independent vectors, then, the $RREM$ form of $P$ is $I_n$ (otherwise the basis would be linear dependent), so exists $P^{-1}$ and we can stablish:

$$[v]_{\mathscr{B}}=P[v]_{\mathscr{B}'} \iff [v]_{\mathscr{B}'}= P^{-1}[v]_{\mathscr{B}}$$


Let's, observe some interesting fact, let's take some invertible matrix $P \in M_n(K)$ and some ordered basis $\mathscr{B}$ from $V$, then, from the construction above the $n$-tuple $\mathscr{B}' = \mathscr{B}P$ is independent since $P$ is invertible, hence the vectors of the $n$-tuple are a set of $n$ independent vectors of the $K$-space $V$ which is $n$-dimensional so is a basis. And since it is the result of a equation system with an invertible asociated matrix, this result is unique, this is, $\mathscr{B}'$ is univocaly determinated by $\mathscr{B}$ and $P$.

<br>

As a brief summary and before see some examples, we can think about the coordinates of a vector as *labeling* in terms of an ordered basis. In the sense that the coordinates is a description of some vector $v \in V$ in terms of the vectors of the basis $\mathscr{B}$. Appliying the change of basis $\mathscr{B} \underbrace{\to}_{P} \mathscr{B}'$ matrix consist in change this description while $v$ remains the same, it only changes the perspective from which you see it.

<br>

## 4.5. Examples.

### 4.5.1. Standard ordered basis.

Take some field $K$ and consider $v \in K^n$, this means that $v$ can be identified with some tuple of elements of $K$; $(\alpha_1, \ldots, \alpha_n) = v$. Then, take the standard basis of $K$; $\mathcal{B}:=\Set{e_1,\ldots,e_n}$, such  

$$e_i =(\alpha_1,\ldots,\alpha_n) : \alpha_j =\begin{cases} 0 \quad j \neq i \\ 1 \quad j = i\end{cases}$$

And form the ordered basis in crecesent order: $\mathscr{B} := (e_1,\ldots,e_n)$. 

Then: 

$$[v]_{\mathscr{B}} = \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_n \end{pmatrix}$$

<br>

### 4.5.2. Rotation matrix.

In $\mathbb{R}^2$ consider the matrix:

$$P = \begin{pmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} : \theta \in \mathbb{R}$$

Take the standard basis $\mathscr{B} = (e_1,e_2)$ and let's multiply in order to obtain a new basis:

$$\mathscr{B}' = \mathscr{B} P = (v_1,v_2) : \begin{cases} v_1 = \cos\theta e_1 + \sin\theta e_2 \\ v_2 = \cos\theta e_2 - \sin \theta e_1\end{cases}$$

According to the euclid geometry in $\mathbb{R}^2$, observe that $v_1$ and $v_2$ are now the projections of $e_1$ and $e_2$ a long the axis regard some angle, $\theta$.

<br>

Note that $P$ is invertible, this is coherent since we should undo a rotation.

## 4.6. Exercises.

### 4.6.1. 

**1. Show that the vectors**

$$\alpha_1 = (1, 1, 0, 0), \qquad \alpha_2 = (0, 0, 1, 1)$$

$$\alpha_3 = (1, 0, 0, 4), \qquad \alpha_4 = (0, 0, 0, 2)$$

form a basis for $\mathbb{R}^4$. Find the coordinates of each of the standard basis vectors in the ordered basis $\{\alpha_1, \alpha_2, \alpha_3, \alpha_4\}$.

<br>

We simply form the equation system: $\sum_{i=1}^4 x_i\alpha_i=0$ and conclude that $x_i=0 \quad \forall i \in [4]$. Now, taking the standard basis in $\mathbb{R}^4: \Set{e_1,e_2,e_3,e_4}$, for each $j \in [4]$ we form the equation $\sum_{i=1}^4 x_{ji} e_i = \alpha_j$. Solving it we get:

$$\begin{cases} \alpha_1 = e_1 + e_2 \\ \alpha_2 = e_3 + e_4 \\ \alpha_3 = e_1 + 4e_4 \\ \alpha_4 = 2e_4 \end{cases}$$

<br>

### 4.5.2.

**2.** Find the coordinate matrix of the vector $(1, 0, 1)$ in the basis of $\mathbb{C}^3$ consisting of the vectors $(2i, 1, 0)$, $(2, -1, 1)$, $(0, 1 + i, 1 - i)$, in that order.

We take that, coordinate to coordinate is: $(1,0,1) = \alpha (2i,1,0) + \beta(2,-1,1) + \gamma (0,1+i.1-i)$, and we form the following equation system in $\mathbb{C}$:

<br>

$$\begin{cases} 2i \alpha + 2 \beta = 1 \\ \alpha - \beta + (1+i) \gamma = 0 \\ \beta + (1-i) \gamma = 1\end{cases}$$

<br>

Obtaining:

$$\alpha = -\frac{1+i}{2}, \qquad \beta = \frac{i}{2}, \qquad \gamma = \frac{3+i}{4}$$

<br>

The coordinate matrix is: $\left(-\frac{1+i}{2},\ \frac{i}{2},\ \frac{3+i}{4}\right)^{t}$.

<br>

### 4.5.3. 

**3. Let $\mathcal{B} = \Set{\alpha_1, \alpha_2, \alpha_3}$ be the ordered basis for $\mathbb{R}^3$ consisting of**

$$\alpha_1 = (1, 0, -1), \qquad \alpha_2 = (1, 1, 1), \qquad \alpha_3 = (1, 0, 0)$$

**What are the coordinates of the vector $(a, b, c)$ in the ordered basis $\mathcal{B}$?**

Observe that $[v]_\mathcal{(e_1,e_2,e_3)} = (a,b,c)$, then from the perspective of the standard basis, the change of basis matrix is:

$$P = [\mathcal{B}]_{(e_1,e_2,e_3)} = ([\alpha_1]_{(e_1,e_2,e_3)}, [\alpha_2]_{(e_1,e_2,e_3)}, [\alpha_3]_{(e_1,e_2,e_3)}) = \begin{pmatrix}1 & 1 & 1 \\ 0 & 1 & 0 \\ -1 & 1 & 0 \end{pmatrix}$$

This is the change of basis matrix from $\mathcal{B}$ to $(e_1,e_2,e_3)$. Hence:

$$P[v]_\mathcal{B}=[v]_{(e_1,e_2,e_3)} \iff [v]_\mathcal{B} = P^{-1}[v]_{(e_1,e_2,e_3)}$$


$$[v]_{(e_1,e_2,e_3)} = \begin{pmatrix}0 & 1 & -1 \\ 0 & 1 & 0 \\ 1 & -2 & 1 \end{pmatrix} \begin{pmatrix}a \\ b \\ c \end{pmatrix} = \begin{pmatrix}b - c  \\ b \\ a + c - b \end{pmatrix}$$

### 4.5.4.

**4. Let $W$ be the subspace of $\mathbb{C}^3$ spanned by $\alpha_1 = (1, 0, i)$ and $\alpha_2 = (1 + i, 1, -1)$.**

- **(a)** Show that $\alpha_1$ and $\alpha_2$ form a basis for $W$.

    Since $W = span\Set{\alpha_1, \alpha_2}$, it only remains to prove that this two vectors are not dependent, which is obvious since are not proportionals.

    <br>

- **(b)** Show that the vectors $\beta_1 = (1, 1, 0)$ and $\beta_2 = (1, i, 1 + i)$ are in $W$ and form another basis for $W$.

    Firs't let's see that $\beta_1 = \alpha_1 + i^{-1} \alpha_2$ and $\beta_2 = (2-i)\alpha_1 + i \alpha_2$, hence are in $W$ and they are not proportional, hence form a basis of $W$.

    <br>

- **(c)** What are the coordinates of $\alpha_1$ and $\alpha_2$ in the ordered basis $\{\beta_1, \beta_2\}$ for $W$?

    Let's call $\mathscr{B}=(\alpha_1,\alpha_2)$ and $\mathscr{B}'=(\beta_1,\beta_2)$, then:

    $$[\mathscr{B}']_{\mathscr{B}} = ([\beta_1]_\mathscr{B}, [\beta_2]_\mathscr{B}) = \begin{pmatrix} 1 & 2 - i \\ -i & i \end{pmatrix}$$

    And we can state that:

    $$[\mathscr{B}']_{\mathscr{B}}^{-1} = [\mathscr{B}]_{\mathscr{B'}} = \begin{pmatrix} 1 & 2 - i \\ -i & i \end{pmatrix}^{-1} = \frac{1}{10}\begin{pmatrix} 3+i & 1 + 7i \\ 3+i & 1 -3i \end{pmatrix}$$

    Thus:

    $$\begin{cases} [\alpha_1]_\mathscr{B'} = ((3+i)/10,(3+i)/10) \\ [\alpha_2]_\mathscr{B'} = ((1+7i)/10,(1-3i)/10)\end{cases}$$

    <br>

### 4.5.5.

**5.** Let $\alpha = (x_1, x_2)$ and $\beta = (y_1, y_2)$ be vectors in $\mathbb{R}^2$ such that

$$x_1 y_1 + x_2 y_2 = 0, \qquad x_1^2 + x_2^2 = y_1^2 + y_2^2 = 1$$

Prove that $\mathcal{B} = \{\alpha, \beta\}$ is a basis for $\mathbb{R}^2$. Find the coordinates of the vector $(a, b)$ in the ordered basis $\mathcal{B} = \{\alpha, \beta\}$. (The conditions on $\alpha$ and $\beta$ say, geometrically, that $\alpha$ and $\beta$ are perpendicular and each has length 1.)

For the first part, let's see that $\alpha$ and $\beta$ can't be proportionals, otherwise, it cannot be perpendicular (the first equation is not solvable for two not null and non-proportionals vectors). Hence is a set of two independent vectors and form a basis in $\mathbb{R}^2$.

Now, let's form the change of basis matrix:

$$P =[(\alpha,\beta)]_{(e_1,e_2)} = \begin{pmatrix} x_1 & y_1 \\ x_2 & y_2\end{pmatrix} \iff [(e_1,e_2)]_{(\alpha_1,\alpha_2)} = P^{-1}$$

Observe that, the two equations above, fixing one of the two components allow us to derive one vector from the other, hence we can simplify $\beta$ in terms of $\alpha$ and get the inverse of $P^{-1}$.

$$P = \begin{pmatrix} x_1 & -x_2 \\ x_2 & x_1 \end{pmatrix}$$

<br>

### 4.5.6.

**6.** Let $V = \mathbb{C}^{\mathbb{R}}$ and let $f_1(x) = 1$, $f_2(x) = e^{ix}$, $f_3(x) = e^{-ix}$.

- **Prove that $f_1$, $f_2$, and $f_3$ are linearly independent.**

    First, 

- **(b)** Let $g_1(x) = 1$, $g_2(x) = \cos x$, $g_3(x) = \sin x$. Find an invertible $3 \times 3$ matrix $P$ such that

$$
g_j = \sum_{i=1}^{3} P_{ij} f_i.
$$