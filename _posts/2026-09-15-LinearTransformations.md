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

### 2.5.2. Intuition: Rank-Nullity theorem.

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

### 2.6.5.

**If:** 

$$\begin{cases} a_1 = (1,-1) & b_1 = (1,0) \\ a_2=(2,-1) & b_2 = (0,1) \\ a_3=(-3,2) & b_3 = (1,1)\end{cases}$$

**Is there some linear transformation $T : \mathbb{R}^2 \to \mathbb{R}^2 \mid T(a_i) = b_i \quad \forall i = 1,2,3$?**

Observe that, by theorem $1$ ($2.4.$), since $(1,-1)$ and $(2,-1)$ are two non-proportional vectors of a $2$-dimenional vector space and form a basis of $\mathbb{R}^2$, the linear transformation $T$ that pairs $a_i \to_T b_i : i = 1,2$ is univoquely determinated by this same pairings and the and we only have to see if it satisfies $T(a_3) = b_3$:

$$T(-3,2) = T(-a_1-a_2) = -T(a_1) - T(a_2) = -(1,0) - (0,1)=(-1,-1) \neq b_3$$

Hence, such $T$ does not exist.

<br>

### 2.6.10.

**Consider $V$ the $\mathbb{C}$ set as a $\mathbb{R}$-space. Find a linear operator in $V$ which is not a linear operator in $\mathbb{C}$ as a $\mathbb{C}$-space.**

Take $T:V \to V \mid T(1,0) = (1,0) \wedge T(0,1) = (1,0)$, by theorem $1$, the mapping garantee that $T$ is a linear transformation. But observe that in $\mathbb{C}$ as a $\mathbb{C}$-space only has dimension $1$, hence any non-zero complex element serve as a basis of the vector space. 

Then, if $T$ is as $T(i) = 1$ (which is the equivalent of the second mapping above), again by theorem $1$ that determines $T$ as a linear transformation, then:

$$T(i) = iT(1) = 1 \iff T(1) = \frac{1}{i} = -i \neq 1$$

Hence $T$ as a linear operator in $V$ does not exists a linear transformation in $\mathbb{C}$ as a $\mathbb{C}$-space.

<br>

# 3. The algebra of linear transformations.

Let's explore operations between linear transformations.

<br>

## 3.1. Operations with linear transformations. 

### 3.1.1. Vector space of linear transformations. $L(V,W)$.

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

### 3.1.2. Basis and Dimension of the $L(V,W)$ space.

Let be $V$ and $W$, respectively $n$ and $m$ dimensional $K$-spaces. Then $L(V,W)$ is a $mn$-dimensional $K$-space.

Let's consider $\mathcal{B}=(v_1, \ldots, v_n)$ and $\mathcal{B}' = (w_1, \ldots, w_m)$ two ordered basis of $V$ and $W$. For each $(p,q) \in [n] \times [m]$, we define the linear transformation given by:

$$E^{p,q} : V \to W \mid E^{p,q}(v_i) = \begin{cases} 0  & i \neq q \\ w_p & i  =q\end{cases} = \delta_{iq} w_p$$

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

<br>

### 3.1.3. Composition of linear transformations.

**Let be $V,W,Z$ $K$-spaces and $T : V \to W$, $U : W \to Z$ linear transformations, then $U \circ T : V \to Z$ is a linear transformation:**

$$(U \circ T)(\alpha v + u) = U(\alpha T(v) + T(u)) = \alpha (U \circ T)(u) + (U \circ T)(v)$$

<br>

## 3.2. Linear operators of a vector space.

### 3.2.1. Definition.

In what follows, we shall be primarily concerned with linear transformation of a vector space into itself. Since we would so often have to write $T$ is a linear transformation from $V$ into $V$, we shall replace this with $T$ is a linear operator on $V$.

Let be $V$ a $K$-space, then, any linear transformation $T : V \to V$ is called a *linear operator on V*.

<br>

### 3.2.2. Multiplication between linear operators.

Observe that since the composition respects the linearity we can define some multiplication on $L(V,V)$:

$$·: V \times V \to V \mid UT = U \circ T$$

Observe that this multiplication acts in sinergy with additive group $(L(V,V),+)$:

- *Identity*:

    $$IT = TI = I \quad \forall T \in L(V,V)$$

    <br>

- *Compatibility*:

    $$\begin{cases} U(T + H) = UT + UH \\ (T+H)U = TU + HU\end{cases} \quad \forall U,H,T \in L(V,V)$$

    <br>

- *Conmutativity with scalars*:

    $$\alpha UT = (\alpha U)T = U(\alpha T) \quad \forall \alpha \in K, \forall U,T \in L(V,V)$$

    Observe that this last property comes from the fact that:

    $$(\alpha U)(T(v)) =U(\alpha T(v)) = U((\alpha T)(v))$$

    <br>

### 3.2.3. Examples of linear operators.

Take some $K$-spaces $V$ and $W$ and let be $\mathcal{B}$ and ordered basis of $V$, then consider the transformation $E^{p,q}$:

$$E^{p,q}(v_i) = \delta_{iq}w_p = \begin{cases} 0 & i \neq q \\ w_p & i = q \end{cases} : w_p \in W$$

Then, we have that these $n^2$ linear operators forma a basis of $L(V,V)$:

$$E^{p,q} \circ E^{r,s} = \begin{cases} 0 & r \neq q \\ E^{p,s} & r = q\end{cases}$$

<br>

## 3.3. Invertible linear transformations.

### 3.3.1. Introduction. Invertible function.

There is an interesting question about linear transformation which is, whether there is for some linear transformation $T$ other linear transformation $T^{-1}$ such $TT^{-1} = T^{-1}T = I$?. In this context, $T$ is what we would call *invertible* linear transformation. 

First, let's consider $T \in W^V$, then we say $T$ is invertible when:

- $T$ is an inyective function: $T(u) = T(v) \implies u = v \quad \forall u,v \in V$

- $T$ is a surjective function; the range of $T$ is his codomain: $T(V) = W$

<br>

### 3.3.2. Caracterization of invertible linear transformations.

**We have that the inverse of an invertible linear transformation is a linear transformation.** 

Let $V$ and $W$ be $K$-spaces. Then, formally:

$$T \in L(V,W) :\begin{cases}T(u) = T(v) \implies u = v \quad \forall u,v \in V \\  T(V) = W\end{cases} \implies T^{-1} \in L(W,V)$$

The proove is trivial.

<br>

Observe also that if $T,U \in L(V,W)$ invertibles, then:

$$(U \circ T)^{-1} = T^{-1} \circ U^{-1}$$

<br>

## 3.4. Non-singular linear transformations.

### 3.4.1. Definition.

Let's see that, take some $T \in L(V,W)$, if $T$ is inyective, then it satisfies $T(u) = T(v) \implies u = v$ for any $u,v \in V$. Check that linearity allow us to reformulate the statement as:

$$(T(u) = T(v) \implies u = v \quad \forall u,v \in V) \iff (T(u-v) = 0 \implies u-v = 0 \quad \forall u,v \in V)$$

Or simply: $T(u) = 0 \implies u = 0 \quad \forall u \in V$ (in a vector space any vector is linear combination of others vectors, hence the difference of two vectors reference any vector). 

The opposite implication is direct, so both statements are equivalents and it develops in a biconditional since $\Leftarrow$ is true because linearity needs that $T(0) = 0$, so:

$$T \text{ is inyective } \iff [T(v) = 0 \iff v = 0 \quad \forall v \in V] \iff Ker(T) = \Set{0}$$

Ultimately, if $V$ is finite dimensional and $Ker(T) = \Set{0} \implies dim(Ker(T)) = 0$. then $dim(T(V)) = dimV$ by the range-nullity theorem ($2.5.2$). 

Note that, under this conditions if $dimW = dimV$, then $T(V) \leq W : dimT(V) = dimW  \implies T(V) = W$ and $T$ is also suprayective and hence, invertible.

So, if $V,W$ are two finite-dimensional $K$-spaces:

$$ dimV = dimW \implies \forall T \in L(V,W) \big[Ker(T) = \Set{0} \implies T^{-1} \in L(W,V)\big]$$

<br>

Then, we define the *non-singular* linear transformations to those linear transformations $T \in L(V,W)$ such:

$$T(u) = 0 \implies u = 0 \quad \forall u \in V$$

Note then that, by the described above, non-singular linear transformations are those which do not loose information in the mapping of $V$ onto $W$ since $Ker(T) = \Set{0}$, are those whose nullity ($Ker$ dimension) is $0$. And the rest of the explained above can be broadly summarized in the fact that if $W$ and $V$ are the same finite-direction-size, then any non-singular transformation between them is invertible.

<br>

### 3.4.2. Caracterization of non-singular linear transformations.

Let $T \in L(V,W)$. Then $T$ is non-singular if and only if $T$ carries each linearly independent subset of $V$ onto a linearly independent subset of $W$. 

<br>

- $\Rightarrow$: Take $T$ non-singular, then, let be $S = \Set{v_1,\ldots,v_n}$ an independent subset of $V$:

    $$T(\alpha_1 v_1 \cdots + \alpha_n v_n) = \alpha_1 T(v_1) \cdots + \alpha_n T(v_n) = 0 \implies$$

    $$\implies \alpha_1 v_1 \cdots + \alpha_n v_n = 0$$

    Observe that, since $S$ is an independent set, the second line give us that all $\alpha_i$ are $0$ and this scalars are the same above, so $T(S)$ is also a linear independent subset of $W$, if not $S$ would not be independent since both shares the same scalars in the linear combinations.

    <br>

- $\Leftarrow$: Suppose $T$ carries independent sets to independent sets, then, take some $v \in V$, as a unitary set $\Set{v} \subset V$ is independent iff $v \neq 0$, hence $T(v) = 0 \implies v = 0$ because both share dependence which in unary vector sets is equivalent to be the $0$ vector. 

<br>

### 3.4.3. Relation between invertible transformations and non-singular transformations.

We already catch a glimpse of this statment but lets formalized it in a theorem.

Let be $V, W$ finite-equal-dimensional $K$-spaces ($dimV = dimW \in \mathbb{N}$). Then for ahy $T \in L(V,W)$ the following statements are equivalent:

- $T$ is invertible.
- $T$ is non-singular.
- $T(V) = W$.

We already demonstrate these above, let's also see that under this very conditions, we have also that the following statements are also equivalents to the first ones and between them.

- Let be $\mathcal{B} \subset V$ a basis, then $T(\mathcal{B}) \subset W$ is also a basis ($3.4.2$ and same dimension.)

- There is some basis $\mathcal{B} \subset V$ such $T(\mathcal{B}) \subset W$ is also a basis. This is the most powerful result of all, if for a linear transformation is known that it sends some basis to other basis, then $Ker(T) = 0$ (since $dimT(V) = dimW$) and is a non-singular transformation connecting space of same finite-dimension, hence is invertible.

<br>

## 3.5. Other interesting algebraic structures.

### 3.5.1. The group of invertible linear operators with composition.

Let be $I(V)$ the set of all invertible linear operators of a finite-dimensional space $V$ (which is in fact the set of all non-singular transformations), then $(I(V),\circ)$ is a group, taking $I(v)=v$ as the identity. Consider $T,U,H \in I(V)$

- *Associativity*: $((T \circ U) \circ H)(v) = (T\circ U)(H(v)) = T(U(H(v))) = T(U\circ H(v)) = (T \circ (U \circ H))(v)$

- *Identity*: $IT = TI = T$

- *Inverse*: $TT^{-1} = T^{-1}T = I$

<br>

### 3.5.2. The group of invertible square matrix.

Let be $I \subset M_{n}(K)$ the set of the invertible matrix. Then $(I,\cdot)$ is a group with $I_n = (\delta_{ij})_{i,j \in [n]}$ as the identity. We already seen the associativity and the identity beavior in past sections. The garantee now is that every matrix of $I$ has an inverse.

<br>

# 4. Isomorphism.