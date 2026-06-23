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

# 1. Introduction.

In the past post; [Vector Spaces](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/), we've introduced that a vector space $(K,V,·)$ is the algebraic structure resulting from using a field $K$ to weigh the compositions of an abelian group $V$, through a field action $·$. Meaning that a vector space is a triple $(K,V, ·)$ where:

- $K$ is a field.
- $V$ is an abelian (commutative) group.
- $· : K \times V \to V$ is a field action, which acts over $V$ using $K$'s elements to scale vectors, making families of *proportional vectors*.

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

**Let $V$ be a vector space over the field $F$. A subspace of $V$ is a non-empty subset $W$ of $V$ which is itself a vector space over $F$ with the operations of vector addition and scalar multiplication on $V$.**

<br>

Let's observe that, from the axioms of vector spaces, if $W$ is a vector space such $W \subset V$, then:

- Closure relative to linear combinations:

    $$v,u \in W \implies (\alpha v + \beta u \in V \ \forall \alpha, \beta \in  F)$$

- Contains zero vector: $0_V \in W$, or $0_W = 0_V$. Remember that $V$ being a vector space means that $(V,+)$ is an abelian group, so $(W,+)$ is an abelian subgroup of $V$ and it inherits $0_V$ from $V$ by the uniqueness of this element. (Observe that this also extends to associativity and inverses).

    <br>

Let's take a characterization for any non-empty subset $W \subset V$ to be a vector space. If $V$ is a $K$-vector space, then:

$$W \text{ is a vector space } \iff (\alpha u + v \in W \quad \forall u,v \in W, \alpha \in K)$$

Let's reconstruct the structure:

- $(W,+)$ is an abelian subgroup of $(V,+)$.

    Since $W \neq \varnothing$ (by the premise), we can consider $u,v \in W$, then: $(-1)u + v = v - u \in W$, so it is a subgroup of $V$. Let's see that $W$ also inherits commutativity from $V$ so it is an abelian subgroup.

    <br>

- $· \|_W: K \times W \to W$ is a field action:

    - Observe that $-1 u + u = 0 \in W$, thus $1 u + 0 = u \in W$ so the unit in $F$ doesn't change the vector and it falls inside $W$.

    - Take some $v \in W \implies \alpha v + 0 = \alpha v \in W \implies \beta (\alpha v) + 0 = \beta (\alpha v) \in W$. For the same reason $(\alpha \beta)v \in W$. Then observe that in $V$, by associativity, is $\beta (\alpha v) = (\beta \alpha)v$ so both elements are equal in $V$ and the same in $W$ (by unicity of the inverse), thus $\beta (\alpha v) = (\beta \alpha)v$

    - Take $(\alpha + \beta)v + 0 = (\alpha + \beta)v \in W \subset V$, then in $V$ is $(\alpha + \beta)v = \alpha v + \beta v$ so, for the same argument as above, is $(\alpha + \beta)v = \alpha v + \beta v$ in $W$.

    - Take $\alpha v + 0 \in W \implies \exists w = \alpha v \in W$, take now other $u \in W$, then  $\alpha u + w \in W$, again in $V$ is $\alpha u + w = \alpha u + \alpha v = \alpha(u + v)$ and again is $ \alpha(u + v) = \alpha u + \alpha v$ in $W$.

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

5. Consider $S:=\Set{(a_{ij})_{ij} \in M_n(K) \mid (a_{ij})_{ij} = (a_{ij})_{ji}}$, the **set of all symmetric matrices** form a subspace of $M_n(K)$

    Take, $A,B \in S$, then let's see that $\alpha A + B = \alpha (a_{ij})_{ij} + (b_{ij})_{ij} = (\alpha a_{ij} + b_{ij})_{ij}$, then let's see that this matrix is in $S$ by observing that:

    $$A \in S \implies a_{ij} = a_{ji} \quad \forall i,j \implies \alpha a_{ij} = \alpha a_{ji} \quad \forall i,j  \implies \alpha A \in S$$

    Now, observe that:
    
    $$A,B \in S \implies \begin{cases}a_{ij} = a_{ji} \quad \forall i,j \\ b_{ij} = b_{ji} \quad \forall i,j  \end{cases} \implies a_{ij} + b_{ij} = a_{ji} + b_{ji} \quad \forall i,j \implies A+B \in S$$

    Ultimately concluding $\alpha A + B \in S$, so $S$ is a subspace of $M_n(K)$

    <br>

6. Consider $M_n(\mathbb{C})$, then we say that $A \in M_n(\mathbb{C})$ is Hermitian or self-adjoint if $(a_{ij})_{ij} = \overline{(a_{ij})_{ji}}$, meaning that is equal to the transverse of the conjugate.

    Then, the set $H := \Set{A \in M_n(\mathbb{C}) \mid (a_{ij})_{ij} = \overline{(a_{ij})_{ji}} }$ is not a subspace of $M_n(\mathbb{C})$ check that the diagonal elements impose $(a_{ii})_{ii} = \overline{(a_{ii})_{ii}}$, since the entries are complex numbers, a complex number is equal with his conjugate when is real.

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

Let's now see finite composition or combinations of vector spaces that still being vector spaces.

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

    - 

