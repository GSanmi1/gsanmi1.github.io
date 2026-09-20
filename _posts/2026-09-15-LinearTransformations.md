---
layout: post
title: "4. Linear Transformations"
subtitle: "Linear Transformations: Definition, Intuition and Properties"
date: 2026-09-15 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
subject: linear-algebra
lang: en
---

# 0. Index.



<br>


# 1. Introduction.

A vector space is, in the essence, a set such his elements can be crafted through linear combinations of other elements. Observe that what defines a subspace as a subspace of a vector space is the fact that is closed through linear combinations of his own elements, it contains any linear combinations of his elements by definition.

A basis is in fact a set containing the minimum number of independent vectors you need to generate any other vector of the space through a linear combination. We should say that the information is not the in the set, but in the relation between the elements of the set weighted by the field of scalars.

<br>

Hence, in mathematics a structure is not studied alone but with the functions that preserves it, and in this case, preserve the structure consist in preserve the way  in which the elements relates between them.

This is interesting since through this functions we can stablish when two sets sharing the same structure type are in fact the same structure and we can work with any of them indistinctly. (Isomorphism).

This functions also remains invariants those properties that are genuily structure-dependent. If some property is a natural extension of the structure and the function preserves it, then it would preserve that property, stablishing those properties that are genuines.

<br>

# 2. Linear Transformations. Definition.

## 2.1. Definition.

If vector spaces are algebraic structures in which the natural operation is the linear combination between vectors: $\alpha v + \beta u$, then; linear transformations are nothing but functions between vectors spaces that respects the linear combination as operation between both spaces.

Let be $V,W$ two $K$-spaces, then: $T : V \to W$ is a linear transformation if it is a function satisfying:

$$T(\alpha v + u) = \alpha T(v) + T(u) \quad \forall \alpha \in K, \forall u,v \in V$$

This is, when get the image of the combination in $V$ is as if we combine the images in $W$ with the same scalars. Observe quickly that a linear transformations always preserve null vector:

$$T(0) = 0$$

<br>

## 2.2. Examples.

Let's see a few examples about linear transformations:

- The *identity transformation* $I v = v$ is a linear transformation.
- The *differentiation transformation* over the polynomial functions $f$ si a linear transformation:

    $$f(x) = \sum_{i = 1} \alpha_i x^{i} \quad \text{ then } \quad D(f(x))=\sum_{i = 1} i·\alpha_i x^{i-1}$$

- In $K^{m \times n}$, the function $T(A) = PAQ : P \in K^{m \times m}, Q \in K^{n \times n}$ is a linear transformation.

- In the space of all continous real functions, $T(f(x))= \int_0^x f(x)dt$ is a linear transformation.

<br>

## 2.3. Geometric Interpretation of Linear Transformations.



<br>

## 2.4. Linear transformation through mapping basis.

### 2.4.1. Presentation and demonstration.

**Let be $V$ a finite-dimensional $K$-space and $\mathcal{B} = \Set{v_1,\ldots,v_n}$ an ordered basis of $V$. Then consider some $w_1,\ldots,w_n \in W$ vectors of some $K$-space. Then there is a unique linear transformation $T : V \to W$ verifying:**

$$T(v_i) = w_i \quad \forall i \in [n]$$

Basically, we are saying that we can arbitrarily decide where to send the vectors of a basis, and that determines exactly one and only one linear transformation between the spaces.

Let's observe that, given a function $T : V \to W$. Take any vector $v \in V$, then is $[v]_{\mathcal {B}} = (\alpha_1,\ldots,\alpha_n)$ and we define: 

$$T(v) = \alpha_1 w_1 \ldots + \alpha_n w_n : w_i \in W, \alpha_i \in K \quad \forall i \in [n]$$

This is $T(v)$ is a vector that can be expressed as a linear combinations of some $w_i$ vectors. Observe that, by definition, for any $v_i \in \mathcal{B}$ is $T(v_i) = w_i$. Take then other $u \in V : [u]_{\mathcal{B}} = (\beta_1, \ldots, \beta_n)$ and observe that:

$$[\alpha v + u]_{\mathcal{B}} = (\alpha \alpha_1 + \beta_1, \ldots, \alpha \alpha_n + \beta_n) \implies$$

$$T(\alpha v + u) =  (\alpha \alpha_1 + \beta_1)w_1 \ldots + (\alpha \alpha_n + \beta_n)w_n = (\alpha \alpha_1 + \beta_1)T(v_1) \ldots + (\alpha \alpha_n + \beta_n)T(v_n) = $$

$$ = \alpha T(v) + T(u)$$

And $T$ is a linear transformation. And the dependence of $T$ from the basis $\mathcal{B}$ also demonstrates is unique. Any vector from $V$ has a unique tuple from $\mathcal{B}$, hence, any linear transformation mapping $\mathcal{B}$ over the same vectors in $W$ would generate the same vectors in $W$, the codomain of $T$ is determinated by the basis and the mapped vectors in $W$.


In other terms, **a linear transformation between two spaces is a way to map a basis from one of the spaces over vectors from the other vector space**.

<br>

### 2.4.2. Example: Relation between linear transformation and matrix.

Consider the vector spaces $K^n$ and $K^m$, $2.4$ garantee the existance of some linear transformation $T$ uniquely determined by the vectors $v_1, \ldots, v_n \in K^m$ such $v_i = T(e_i)$ being $\mathcal{B} = \Set{e_1, \ldots, e_n}$ the standard basis of $K^n$.

This is, $T$ is completly determined by the images of the standard basis.

Observe that, if $[v]_{\mathcal{B}} = (\alpha_1, \ldots, \alpha_n) \implies T(v) = \alpha_1 v_1 \ldots + \alpha_n v_n$. Then, let be $\mathcal{B'}$ some independet set of $m$ vectors of $K^m$, we define the matrix: 

$$M_{T_{\mathcal{B'}}} = \begin{pmatrix}[v_1]_{\mathcal{B'}} \\  \vdots \\ [v_n]_{\mathcal{B'}} \end{pmatrix} = \begin{pmatrix} \alpha_{11} & \cdots  & \alpha_{1n} \\  \vdots & & \vdots \\ \alpha_{m1} & \cdots & \alpha_{mn} \end{pmatrix} $$

Satisfies:

$$[T(v)]_{\mathcal{B'}} = [v]_{\mathcal{B}}M_{T_{\mathcal{B'}}}$$

The logic is the same that we used in the change of matrix basis, in further section we will discuss deeper the relation between linear transformations and matrix.

<br>

## 2.5. Rank and Kernel of a Linear Transformation.

### 2.5.1. Definition.

Let be $V$ and $W$ vector spaces over $K$, let's consider some linear transformation $T : V \to W$. 

We call *rank* of $T$ to the set of all vectors in $W$ that are image of some vector of $V$ through $T$:

$$range(T) = \Set{w \in W \mid \exists v \in V : w = T(v)}$$

<br>

We call *kernel* (or null space) of $T$ to the set of those vectors that map's to $0$ through $T$:

$$ker(T) = \Set{ v \in V \mid T(v) = 0}$$

Is clear that the rank and kernel of a linear transformation are indeed subspaces. The rank of $T$ is the subspace of $W$ induced by $V$ through $T$. since all the linear combinations of the vectors of the kernel belongs to the kernel.

<br>

### 2.5.2. Intuition: Rank-Nulity theorem.

Let's see some interesting interpretation of this two subspaces. 

Let be $\mathcal{B}$ some ordered basis of $V$ and consider $T : V \to W$ the linear mapping such $T(v_i) = w_i$ for each $v_i \in \mathcal{B}$. 

First, is clear that $T(V) = range(T) = span(T(\mathcal{B}))$, the rank of $T$ is the spanned subspace generated by the images of the vector of $\mathcal{B}$.

Observe that, if there is some $v \in V : v \neq 0 \wedge T(v) = 0$, then, the linear combination of $T(v)$ in terms of the image of vectors of $\mathcal{B}$ is also $0$:

$$T(v) = T(\alpha_1 v_i \ldots + \alpha_n v_n) = \alpha_i T(v_i) \ldots + \alpha_n T(v_n) = 0$$

This is, the image of the basis $T(\mathcal{B})$ is no longer an independent set in $W$, meaning that the $Ker(T)$ space reflects the information of $V$ that $T$ can't transfer to $W$.

Furthermore, consider $V$ a finite-dimensional space and let be $\|\mathcal{B}\| = n$. Then, $Ker(T) \neq \varnothing \implies T(\mathcal{B})$ is dependent. Let's also suppose that $T(V) \neq \Set{0}$ so we can take out a finite number of vectors $m$ from $T(\mathcal{B})$ until we left an independent subset of vectors. Let's call it $T(S)$, being $S \subset \mathcal{B}$ those vectors whose image belongs to some vector in $T(S)$ ; naturally: $span(T(S)) = range(T)$ and $dim(span(T(S))) = dim V - m$.

Now, consider some basis of $Ker(T)$, $K$. This is an independent subset of $V$ and can be expanded to a basis of $V$. Note that, if we recall $S$ from above, $S \cup \mathcal{K}$ is independent, otherway, $T(S)$ wouldn't be independent (since some linear combination of his vectors would be in $Ker(T)$) or some linear combination of the images of $K$ wouldn't be $0$, in contradiction with the fact that $Ker(T)$ is a vector space. 

Observe that this independent vector set can't be expanded either since neither $S$ or $K$ can be expanded, so is a basis of $V$ and we have:

$$dim V = dim(span(S \cup K)) = dim(span(S) + span(K))= dim(span(S)) + dim(span(K))$$

Remember that $span(S) \cap span(K) = \Set{0}$ and its dimension is $0$, and also that $T(S)$ is also independent, so $dim(span(S)) = dim(span(T(S))) = dim(range(T))$. Thus, we have that:

$$dim V = dim(range(T)) + dim(ker(T))$$

<br>

Let's, see that if we consider $w \in V : D = S \cup K \cup \Set{w}$ is independent, then $T(S) \cup T(w)$ is dependent and therefore:

$$\alpha T(w) + \sum_i \beta_i T(s_i) = T(\alpha w + \sum_i \beta_i s_i)= 0 \implies \alpha w + \sum_i \beta_i s_i \in Ker(T)$$

Note that since, $S \cup \Set{w}$ is independent $\alpha \neq 0$ and we can ensure that:

$$w = \sum_i \alpha_i s_i + \sum_i \beta_i k_i : s_i \in S \wedge k_i \in K \implies w  \in span(S \cup K)$$

In contradiction with the premise that $D$ is independent.

<br>

This theorem allow us to say that $T$ maps $V$ information over $W$ and $Ker(T)$ is the residue of the information of $V$ that $T$ doesn't maps to $W$.

<br>


## 2.6. Section exercises.

### 2.6.3. 

**Describe the range and the null space for the differentiation transformation of Example 2. Do the same for the integration transformation of Example 5.**

Let's take first the differentiation transformation $D : Pol(K,K) \to Pol(K,K)$ given as:

$$D(p(x)) = \frac{dp(x)}{dx}$$

Then, let's try to describe, $range(D)$ and $ker(D)$:

- $range(D) = Pol(K,K)$, since $D(p(x))$ is just the polynomial with one grade less and distinct coefficients, so since there are infinite grades for the polyomials in $Pol(K,K)$, any polynomial is an image of other polynomial by $D$.

- $Ker(D) = \Set{p(x) \mid deg(p(x)) = 0}$, since the differentiation of any $p(x)$ with degree $0$ is the zero function. Note that, the zero-polynomial is also a constant function.


<br>

Let's also see the integration transformation $I : C \to C$, being $C \subset \mathbb{R}^\mathbb{R}$ the space of all real functions which are continues.

$$I(f(x)) = \int_{0}^x f(t) dt$$

Then, the same again:

- $range(I) = \Set{f \in C : f(0) = 0}$. 

    The argument is that, if $f \in C$, then is continuos and by $TFC$ is $F(x) = \int_0^x f(t) dt$ such $F$ is diferentiable at any point with $F' = f$. Also, Barrow tell us that if $F$ is differentiable with $F'$ continuous (which it is, since $F' = f \in C$) then $\int_0^x f(t) dt = F(x) - F(0)$. Since $T$ is a linear transformation, $I(f(0)) = 0 \quad \forall f \in C$, meaning that $F(0) = 0$.

    <br>

- $ker(I) = \Set{0}$

<br>

### 2.6.4.

**Is there a linear transformation $T$ from $R^3$ into $R^2$ such that $T(1, -1, 1) = (1, 0)$ and $T(1, 1, 1) = (0, 1)$?**

<br>

Let's start saying that, theorem $1$ ($2.4$) garantee that if $\mathcal{B}$ is a basis of some vector space $V$, then there is a unique linear transformation $T : V \to W$ sending $\mathcal{B}$ vectors to some other vectors of $W$

<br>

In $\mathbb{R}^3$, $(1,-1,1)$ and $(1,1,1)$ are non-proportional vectors. Hence, let's say $(x,y,z) \in \mathbb{R}^3$ is a third vector linear independent from two above, then the three of them satisfies:

$$\alpha(1,-1,1) + \beta(1,1,1) + \gamma(x,y,z) = 0 \iff \alpha = \beta = \gamma = 0$$

This give us, the following system:

$$\begin{cases} \alpha + \beta + \gamma x = 0 \\ \beta - \alpha + \gamma y = 0 \\ \alpha + \beta + \gamma z = 0\end{cases} \iff x \neq z$$

This means that parametric family: $\Set{(1,1,1),(1,-1,1),(x,y,z) : x \neq z}$ give us basis of $\mathbb{R}^3$ and allow us to define the family of transformations $T : \mathbb{R}^3 \to \mathbb{R}^2$ such satisfies the premise of the exercise:

$$\begin{cases} T(1,-1,1) = (1,0) \\ T(1,1,1) = (0,1) \\ T(x,y,z) = (a,b) : x \neq z\end{cases}$$

<br>

Ultimately, observe that this set gathers all the posible linear transformations satisfying the condition. If $T$ is some linear transformation satisfying the condition, there has to be some vector that form a basis with the other two which is sended to some vector in $\mathbb{R}^2$ and hence it would be included in our set.

<br>

# 3. The algebra of linear transformations.

Let's explore operations between linear transformations.

<br>

## 3.1. Vector space of linear transformations. $L(V,W)$.

Let be $V$, $W$ $K$-spaces, and $T,U: V \to W$ linear transformations, then, let's see that:

- $T+U : V \to W \mid (T+U)(v) = T(v) + U(v)$

   
    Is a linear transformation. To proove it, let's see that:

    $$(T+U)(\alpha v + u) = T(\alpha v + u) + U(\alpha v + u) = $$

    $$= \alpha T(v) + T(u) + \alpha U(v) + U(u) = \alpha[T(u) + U(v)] + [T(v) + U(u)] = $$

    $$ = \alpha(T + U)(v) + (T+U)(u)$$

    <br>

- $(\alpha T)(v) = \alpha T(v)$

    Is a linear transformation, again:

    $$(\alpha T)(\beta v + u) = \alpha T(\beta v + u) = \alpha \beta T(v) + \alpha T(u) = \beta (\alpha T)(v) + (\alpha T)(u)$$


Let's now see that if $L(V,W) \subset W^V$ of the linear transformations, then $(L(V,W),+)$ is an abelian group. This is inheritated by the fact that the addition $+$ is reduced to an addition in $W$ and $(W,+)$ is by definition an abelian group. Let's call $0 :V \to W$ the identity and $(-T) = - T$ the opposite of $T \in L(V,W)$.

The same reasoning can be done with $· : K \times L(V,W) \to L(V,W)$ to assert that is a field action over $L(V,W)$, so $(L(V,W),+,·)$ is a $K$-vector space. 
<br>

Observe that we can argue as well that $W^V$ with the operations defined is also a vector space for which $L(V,W)$ would be a subspace.

<br>

## 3.2. Basis and Dimension of the $L(V,W)$ space.

Let be $V$ and $W$, respectively $n$ and $m$ dimensional $K$-spaces. Then $L(V,W)$ is a $mn$-dimensional $K$-space.

Let's consider $\mathcal{B}=(v_1, \ldots, v_n)$ and $\mathcal{B}' = (w_1, \ldots, w_m)$ two ordered basis of $V$ and $W$. For each $(p,q) \in [n] \times [m]$, we define the linear transformation given by:

$$E^{p,q} : V \to W \mid E^{p,q}(v_i) = \begin{cases} 0  \ \ \quad i \neq q \\ w_p \quad i  =q\end{cases} = \delta_{iq} w_p$$

According to $2.4$ there is only one linear transformation for this basis.

The thing is that we can form $E^{p,q}$ in $nm -1$ ways more, and the case is that each one of them is independent , hence, we can form $nm$ linear transformations of $L(V,W)$ and any other linear transformation we add to it make the set dependent, so $dim(L(V,W)) = nm$.

Consider some $T : V \to W$, then, consider $[T(v_i)]_{\mathcal{B}'} = (\alpha_{1i}\ldots,\alpha_{mi})$ for each $i \in [n]$, observe that:

$$T = \sum_{p=1}^m \sum_{q=1}^n \alpha_{pq} E^{p,q}$$

Remember that $E$ transforms $\mathcal{B} \to \mathcal{B}'$ vectors when index matches:

$$\sum_{p=1}^m \sum_{q = 1}^n\alpha_{pq} E^{p,q}(v_i) = \sum_{p=1}^m \sum_{q=1}^n \alpha_{pq}\delta_{iq} w_p = \sum_{p=1}^m \alpha_{pi}w_p = T(v_i)$$

Hence $\Set{E^{p,q}}_{p \in [n], q \in [m]}$ spans $L(V,W)$. 

<br>

In the other hand, let's try to make:

$$\sum_{p=1}^m \sum_{q=1}^n \alpha_{pq} E^{p,q} = 0$$

Observe that each $\alpha_{pq}$ comes along attached with some $E^{p,q}$ that in at least one iteration of the loop is not $0$, so if at least one $\alpha_{pq} \neq 0$ the summatory can't be zero since each $E^{p,q}$ became a distinct vector from an independent set. 

Hence $\alpha_{pq} = 0 \quad \forall (p,q) \in [n] \times [m]$ and $\Set{E^{p,q}}_{p \in [n], q \in [m]}$ is independent, then is a basis.