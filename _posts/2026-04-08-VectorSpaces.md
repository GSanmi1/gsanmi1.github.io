---
layout: post
title: "2. Introduction to VectorSpaces"
subtitle: "Algebra. Algebraic Structures. Actions. Vector Spaces. Affine Spaces. Vector as geometric objects: Arrows."
date: 2026-04-08 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
---

- 1. Conceptual Approach. Algebra, Algebraics Structures and Vector Spaces.
    - 1.1. Algebra as a discipline.
    - 1.2. Algebraic Structures.
        - 1.2.1. One operation algebraic structures.
        - 1.2.2. Two operations algebraic structures.
- 2. Vector spaces.
    - 2.1. Actions. Algebraic Actions.
        - 2.1.1. Definition.
        - 2.1.2. Group's Action.
    - 2.2. Field's action. Vector Space.
        - 2.2.1. Definition.
        - 2.2.2. Conceptually Approach.
    - 2.3. Examples.
        - 2.3.1. The n-tuple space.
        - 2.3.2. The space of m x n matrices.
        - 2.3.3. The space of functions from a set to a field. 
        - 2.3.4. The space of polynomial functions over a field K.
            - 2.3.4.1. Introduction to polynomials.
            - 2.3.4.2. Vector space of the polynomial functions over a field K
    - 2.4. Immediate Properties from vector spaces.
- 3. Vector Spaces and Geometry.
    - 3.1. Analitic Geometry: The affine space.
        - 3.1.1. Definition.
        - 3.1.2. Isomorphism by origin.
    - 3.2. Vectors as geometric objects: Arrows.
        - 3.2.1. Bound arrows. Vectors as arrows.
        - 3.2.2. Equipolence class: Free vectors.
            - 3.2.2.1. Appex: Equivalence Class.
            - 3.2.2.2. Vector equipolence.
- 4. Summary.

# 1. Conceptual Approach. Algebra, Algebraics Structures and Vector Spaces.

## 1.1. Algebra as a discipline.

Let's start introducing what **Algebra** is, Algebra is the mathematics discipline in charge of the study of what *operating with the elements of a set means*: how items of a set are combined through a operation and what properties emerge from that context. It doesn't study the elements (like arithmetic would do) but the properties of the operations between them.

<br>

## 1.2. Algebraic Structures.

An **algebraic structure** is a a set $(S, \Omega)$ where:

- $S \neq \varnothing$
- $\Omega$ is a collection of operations over $S$ (and maybe other sets as we will see) along with a sequence of rules called *axioms* that this operations satisfies.

This is the minimal basic item of study in algebra; a finite number of operations over a set defined by axioms. Our task is to comprehend how this operations behave through the axioms applying classic logic. 

In the previous section we already provided an introduction to algebraic structures through the number sets and then introduced a solid idea of the group and then the field. Our objective was to present a formalization about linear equations over a field.

We can review and develop the ideas presented in the [Linear Equation section](https://gsanmi1.github.io/posts/2026/02/06/Linear_Equations/) to understand the natural progression and the algebraic structures towards de vector space.

<br>

### 1.2.1. One operation algebraic structures.

Let be $G := (S, \Omega) : \Omega := \Set{\star}$, where $\star : S \times S \to S$ is an internal operation (a function). 

Then we define:

- $G$ (or $S$ by default) is said to be a *Magma* if $\star$ only verifies the closure property:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)

    Observe that this structure is the minimal one, and his only property is forced by $\star$ definition.

    <br>

- $G$ is a *semigroup* if also verifies associativity:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b \in S$ (Associativity)

    <br>

- A *monoid* is a semigroup that also have the identity element $e \in S$ relative to $\star$ verifying:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b \in S$ (Associativity)
    - $ \exists e \in S \ \ \forall a \in S : e \star a = a \star e = a$ (Identity)

    <br>

- Now we enter in the confort zone, a *Group* is a monoid which verifies the existance of an inverse for each item in $S$:

    - $a \star b \in S \ \ \forall a,b \in S$ (Closure)
    - $(a \star b) \star c = a \star (b \star c) \ \ \forall a,b,c \in S$ (Associativity)
    - $ \exists e \in S \ \ \forall a \in S : e \star a = a \star e = a$ (Identity)
    - $\forall a \in S \ \ \exists a' \in S : a \star a' = a' \star a = e$ (Inverse)

    <br>

Let's observe that each axiom let us to do something new in the structure, each new rule is a new capability based on the defining of invariants along the structure; 

- The closure garantees internal compositions, the belonging of any composition to $S$ remains contant. 

- The associativity garantees order-independence as long as the direction in the composition remains the same, meaning that $(a\star b) \star c$ and $a\star (b \star c)$ is the same object in the sense that we can talk about $a\star b \star c$ to refer to any of them, no matter what do you compose first.

- The existance of the identity garantee the existance a way to operate that do nothing concreted in an element of $S$ called the identity. The composition of $e$ by any item of $S$ in any direction remains constant and is the very same item.

- The existance of the inverse make use of the identity to garantee a way to operate that lets you reverse the operation. The composition of any item with his inverse in any direction remains constant and is the identity.

<br>

Observe that this are the main invariants in operations because this are the smallest subset of rules that allow you to define constraints about some elements (equations) and confortly operate to isolate them in order to fully understand to what is equivalent that constraint and how is a valid item.

Suppose there is an interest to find the relation about two elements $a,b \in S$, this is, $b$ is the composition of $a$ with some other element $x \in S$ which we gonna call the *unknown*: $a \star x = b$. Now, let's observe:

$$ a^{-1} \star (a \star x) = a^{-1} \star b$$

Step by step, the closure axiom asserts that $a^{-1} \star (a \star x) = a^{-1} \star b \in S$ and the propousal has sense, the associativity stablish that $a^{-1} \star (a \star x)  = a^{-1} \star a \star x= (a^{-1} \star a) \star x$, or that we can choose the order of the composition as we please. Then, the identity and the inverse cooperates together to simplify the expression, the inverse make $a$ to dissapear, it substitute it for the identity and the identity composed with any other item is any other item, thus:

$$a^{-1} \star (a \star x) = (a^{-1} \star a) \star x = e \star x = x = a^{-1} \star b$$

This four invariantes are summarized in the idea of *group*.

This idea of group can be extended by introducing the *conmutativity* which defines the composition under direction as an invariant:

$$a \star b = b \star a \ \ \forall a,b \in S$$

This allows to reorganize making the simplification of expressions even more confortable.

<br>

### 1.2.2. Two operations algebraic structures.

Until now, we've defined an algebraic structure that contemplates only one operation, lets now introduce algebraic structures with two operations.

<br>

**Rings**

First, the rings, a ringe is a triple $(K,+,\ ·)$ such:

- $(K,+)$ is a group and introduce the four properties seen above.
- $(K, \ ·)$ is a monoid, it drops the existence of the inverse for any element of $R$.
- $+$ and $·$ relates themselves by the distributive law:

    $$a(b+c) = ab + ac \wedge (b+c)a = ba + ca$$

    We say both operations are compatible.

    <br>

The ring introduces the second operation in a soft way, hanging on the existance of the inverse allows to fit in many structures well studied such:

- **Integers ring**; $(\mathbb{Z},+, \ ·)$, where for example $\forall a ( a \in \mathbb{Z} \wedge a \neq \pm 1 \implies a^{-1} \notin \mathbb{Z})$.

    <br>

- **Polynomial ring**; with coefficients in a field $F$; $F[x]$ is a ring 
  but not a field. For instance, $x$ has no multiplicative inverse:

  $\forall q \in F[x] \setminus \{0\} \ \deg(x \cdot q) = 1 + \deg(q) \geq 1 \neq 0 = \deg(1)$

  So the equation $x \cdot q = 1$ has no solution in $F[x]$

    <br>

- **Matrix ring**; we've already seen that $(M\_n(F)\setminus 0, \ ·)$ has no inverse for every element of $M\_n(F)$, remember that we already seen that not every matrix is invertible only those row-equivalent to the identity $I\_n$

    <br>

The mathematical world is full of structures with two operations where division fails.

<br>


**Field**

Then the concept of the field can be thought as an extension of the ring where each element has an inverse for the product operation except the zero element.

However, we want to present another perspective of a field. 

Above we built step by step from the smallest algebraic structure *Magma* to the *Group* and his four axioms and we conclude the importance of such structure was that it allows to present and solve equations:

$$a \star x = b \iff x = a^{-1} \star b$$

Then, the field $K$ aims to extend the same idea for two operations departing from the group structure. This means that a field is a triple $(K,+, \ ·)$ such:

- $(K, +)$ is an abelian group.
- $(K \setminus \Set{0}, \ ·)$ is an abelian group.
- $+$ and $·$ are compatible.
- $1 \neq 0$

This basically means that the field intends to be the structure in which equations can be defined and solved in two operations simultaneously, the motivation was to build an algebraic framework for common aritmetic operations in $\mathbb{R}, \mathbb{Q},...$ and another commons fields.
    
<br>

# 2. Vector spaces.

Before we've seen a set of axioms that rules how a set of operations $\Omega$ behaves in a non-empty set $K$. We extend this concept to two sets $(K,V)$ where $K$ is a field and $V$ is a group and both related between them by a field-action.

Let's dive into this.

<br>

## 2.1. Actions. Algebraic Actions.

### 2.1.1. Definition.

First, let's define what an action is. Let be $A$ and $S$ two sets, then we define an action as a function:

$$\varphi: A \times S \to S$$
$$\ \ \ \ \ \ \ (a,s) \to s$$

It grabs two elements, one from $A$ and another from $S$ and it maps it to a third element from $S$.

As defined, this function doesn't have interest at all, it become interesting when $\varphi$ respect the structure of $A$, this way is said that an action transforms $S$ using $A$ algebraic structure.

<br>

### 2.1.2. Group's Action.

**Group's action**

Let be again $(G,S,\varphi)$ such $\varphi : G \times S \to S$, let's suppose now that $G$, is a group for some internal operation $\star : G \times G \to G$. 

In this context, we impose two rules $A1$, $A2$ over $\varphi : A \times S \to S$. In total, the triple $(G,S,\varphi)$ 

- **Closure**: $\varphi(a,s) \in S \ \ \forall a \in G, s \in S$, forced by $\varphi$ definition.

    <br>

- **(A1) Identity**: Be $e \in G$ the identity on $G$ then we require: $\varphi(e,s) = s \ \ \forall s \in S$

    Meaning that the $G$'s identity doesn't move anything through $\varphi$.

    <br>

- **(A2) Associativity**: $\varphi(a,\varphi(b,s)) = \varphi(a \star b,s) \ \ \forall a,b \in G, s \in S$

    Observe that this resembles to the orden invariant we talked in groups, as long as the direction of the composition remains still ($a \to b \to s$) it doesn't matter the order in which order you perform this compositions.

    Composing $b$ with $s$ through $\varphi$ and then this with $a$ is the same that "multiply" $a \star b$ in $G$ and then compose it with $s$ through $\varphi$. Check that if we write $a \star b = ab \wedge \varphi(a,s) = a\ ·s$ then, the rule above states that:

    $$a \ ·(b \ ·s) = (ab)\ ·s \ \ \forall a,b \in G, s \in S $$

    And it appears more familiar.

    <br>


- **Inverse**: Observe this is not labeled as an axiom because it can be deduced from the two above but is included from pedagogic reasons.

    The idea of the inverse on a group intends to formalice the idea of revert a composition or go back. Thus, we are looking to demonstrate that, calling $\varphi_a(s) = \varphi(a,s)$

    $$\forall \varphi_a \ \exists \varphi^{-1}_{a}  \ \forall s \in S: \varphi_a(\varphi^{-1}_{a}(s)) = \varphi^{-1}_{a}(\varphi_a(s)) = s$$

    Let's take $x = a^{-1}$ and observe that applying $A2$, $A1$ and the existance of the inverse in $G$ we get:

    $$a^{-1} \ ·(a \ · s) = (a^{-1}a) \ · s = e \ · s = s$$

    $$a \ · (a^{-1} \ · s) = (aa^{-1}) \ · s = s$$

    Meaning that $\varphi^{-1}\_{a}= \varphi_{a^{-1}} \ \ \forall a \in G$.

    <br>

Thus, this four properties makes that the triple $(G,S,\varphi)$ behaves like a group in the sense that we can define and solve equations over the elements of $S$ which remember, initially wasn't a group:

$$ \varphi_a(x) = s \iff x = \varphi_{a^{-1}}(s)$$

Meaning that we can treat the elements of $S$ as elements over which we can define constraints, relations, etc. 

Although, is worth to remember that $S$ is not a group an neither is the triple $(G,S, \varphi)$, what $S$ has aqcuired through $\varphi$ is a family of reversible parametrized transformations by the group $G$. Is a form to use $G$ in order to study $S$.

<br>

## 2.2. Field's action. Vector Space.

### 2.2.1. Definition.

Now consider again a triple $(K,V,\ ·)$, where $K$ is a field and $V$ is an abelian group and $·: K \times V \to V$ is a field's action. 

As we said before this action respects the algebraic structure of $K$, which remember; is a combined abelian group over two different compatible operations, by forcing the following axioms:

- **M1**: $1_K \ · v = v$. The identity over the product doesn't transform anything.
- **M2**: $\alpha \ · (\beta \ · v) = (\alpha \beta) \ · v \ \ \forall \alpha, \beta \in K, v \in V $. asociativity resembleance, order-independence while direction stays still.
- **D1**: $\alpha \ · (u + v) = \alpha \ · u + \alpha \ · v \ \ \forall \alpha \in K, u, v \in V $. Compatibility between $·$ and $+$ in $V$.
- **D2**: $(\alpha + \beta) \ · v =\alpha \ · v + \beta \ · v \ \ \forall \alpha, \beta \in K, v \in V$. Compatibility between $·$ and $+$ in $K$.

This four axioms plus the four axioms of the group $V$ gives us the eight axioms of the vector space $(K,V, \ ·)$. 

<br>

### 2.2.2. Conceptually Approach.

This time, a field's action over a group doesn't intend to give an algebraic structure to $V$, instead it provides, through $K$ a uniform deformation mechanism. The aritmetic system of $K$ as a field is used to perform richer algebraic manipulations on $V$ as a group.

$·: K \times V \to V$ gives to $V$ a parametric scaling mecanism through $(K,+, \ ·)$ which, ultimately, allows a coherent way to perform linear combinations on the elements of $V$. 

Let's dive into "scaling", "linear" and "linear combination" terms in order to understand what this introduction means.

<br>

**Scaling.**

Scaling is about relating $V$'s elements using $K$'s elements as mediators. The term "scalar" comes from scale; changing the size without changing the essential nature of the object.

Then, being $u,v \in V$ and $\alpha \in K : \alpha \neq 0$, when we say that $u = \alpha \ · v$, we are really saying $u$ is obtained from $v$, keeping his structural information since, thanks to $K$ to be a field and $·$ to respect $K$ properties we can revert this operation and go back from $u$ to $v$. Let's see that by $M2$ and $M1$ we can garantee the existance of some $\beta \in K$ such $\beta \ · u = v$. Take $\beta = \alpha ^{-1}$ and:

$$\alpha^{-1} \ · u = \alpha^{-1} \ · (\alpha \ · v) \underbrace{=}_{M2} (\alpha^{-1} \alpha) \ · v = (1_K) \ · v \underbrace{=}_{M1}  v  $$

In this context we say that $u$ and $v$ are *proportionals*. Specifically, there exists an entire family of elements for which $u$ is proportional to: $\Set{\alpha v : \alpha \in K \wedge \alpha \neq 0} \subseteq V$.

<br>

**Linear & Linear Combinations.**

Linear referes to independant contribution of severals parts which no interfers between them.

In this case, a linear combination is the minimal operation that takes place in the triple $(K,V, \ ·)$; independant contribution of proportional components of $V$. 

Is the most general way to combine while respecting the principle of independent contributions:

$$\alpha v + \beta u: \alpha , \beta \in K \ \ u, v \in V$$

Observe that $D1$ and $D2$ garantees that $K$ and $V$ respects this object on $(K,V,\ ·)$.

<br>

**Vector Space**

Thus, $(K,V, \ ·)$ is the algebraic environment where a set of objects can be combined by independent contributions weighted by a field. A field's action is the mechanism that imports the arithmetic of $K$ as a system of intensities applicable to the elements of $V$. 

A vector space is nothing but, conceptually, a functional linear combination system and his elements are called vectors.

<br>

**Vectors** 

Thus, vectors are elements of an algebraic structure called vector space whose elements relate through linear combinations verifying the eight axioms presented before.

Being the vector space an algebraic structure means that vectors (and vector space) are nothing, as we say on the start of this very notes, algebra cares about how to operate and properties that emerges from a some defined operatable structure.

In other words; vectors are the elements of an abelian group $V$ on which a field $K$ acts through a "deformation" mechanism. This action, the combination o composition of this deformated elements of $V$, is what we call linear combinations: weighted sums where each element of $V$ contributes with an intensity set by $K$.

The corolary from this assert is that what really cares is that there are objects (matrix, polynomials, arrows, etc) that with the right operations, verifies the vector space axioms, thus, they are vectors and all the machinery defined around them works also for this objects.

<br>

## 2.3. Examples.

Let's see a few mathematical objects that algebraicly behaves as vector spaces.

### 2.3.1. The n-tuple space.

Consider $F$ a field, then the algebraic structure $(F^n,+)$ with the addition behaving as:

$$+: F^n \times F^n \to F^n \mid x + y := \begin{pmatrix}x_1 + y_1\\ \vdots \\ x_n+y_n\end{pmatrix} \in F^n$$

Observe that properties of the abelian group $(F,+)$ expands to $(F^n,+)$ so this is also an abelian group.

Thus, defining the function defined as:

$$· : F \times F^n \to F^n$$
$$ (\alpha, \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} ) \to  \begin{pmatrix}\alpha x_1 \\ \vdots \\ \alpha x_n\end{pmatrix}$$

Veryies the field's action axiom:

- **M1**: $1 \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} = \begin{pmatrix}1x_1 \\ \vdots \\ 1x_n\end{pmatrix} = \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} \ \ \forall x \in F^n$

    <br>

- **M2**: $\alpha \ ·( \beta \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix}) = \alpha \ · \begin{pmatrix}\beta x_1 \\ \vdots \\\beta x_n\end{pmatrix} = \begin{pmatrix}\alpha \beta x_1 \\ \vdots \\\alpha \beta x_n\end{pmatrix} = (\alpha \beta) \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} \ \ \forall \alpha, \beta \in F, x \in F^n$

    <br>

- **D1**:

    $$\alpha \ · (\begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} + \begin{pmatrix}y_1 \\ \vdots \\ y_n\end{pmatrix}) = \alpha \ · \begin{pmatrix}x_1 +y_1 \\ \vdots \\ x_n + y_n\end{pmatrix} = \begin{pmatrix}\alpha (x_1 + y_1) \\ \vdots \\ \alpha (x_n + y_n)\end{pmatrix} = \begin{pmatrix}\alpha x_1 + \alpha y_1\\ \vdots \\ \alpha x_n + \alpha y_n\end{pmatrix}$$

    $$= \begin{pmatrix}\alpha x_1 \\ \vdots \\ \alpha x_n\end{pmatrix} + \begin{pmatrix}\alpha y_1 \\ \vdots \\ \alpha y_n\end{pmatrix} = \alpha \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} + \alpha \ · \begin{pmatrix}y_1 \\ \vdots \\ y_n\end{pmatrix} \ \ \forall x,y \in F^n, \alpha \in F$$

    <br>

- **D2**: 

    $$(\alpha + \beta)\ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} = \begin{pmatrix}(\alpha + \beta)x_1 \\ \vdots \\ (\alpha + \beta)x_n\end{pmatrix} = \begin{pmatrix}\alpha x_1 + \beta x_1 \\ \vdots \\ \alpha x_n + \beta x_n\end{pmatrix} = \begin{pmatrix}\alpha x_1 \\ \vdots \\ \alpha x_n\end{pmatrix} + \begin{pmatrix}\beta x_1 \\ \vdots \\ \beta x_n\end{pmatrix} $$

    $$= \alpha \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix} + \beta \ · \begin{pmatrix}x_1 \\ \vdots \\ x_n\end{pmatrix}$$


    <br>

Thus, the triple $\big(F,(F^n,+), \ · \big)$ satisfies:

- $F$ being a field.
- $(F^n,+)$ an abelian group.
- $(\ ·)$ is a field's action (an action satisfying $M1,M2,D1,D2$ axioms).

And is a vector space. 

Observe taht, as a special case, $(\mathbb{R},(\mathbb{C}^n,+), \ ·)$ is a vector space.

<br>

### 2.3.2. The space of m x n matrices.

Let's consider the set $M_{m \times n}(F) = F^{m \times n}$ with

$$+: F^{m \times n} \times F^{m \times n} \to F^{m \times n}$$

$$(a_{ij}) + (b_{ij}) := \big((a_{ij} + b_{ij})_{ij} \big)\in F^{m \times n}$$

Observe that again addition in $F^{m \times n}$ is extended from $(F,+)$ which is an abelian group so $(F^{m \times n},+)$ is also an abelian group, the argument is the same, addition in $F^{m \times n}$ are $mn$ additions on $F$.

<br>

Also, consider the action: 

$$· : F \times F^{m \times n} \to F^{m \times n}$$
$$ (\alpha, (a_{ij}) ) \mapsto  (\alpha a_{ij})$$

Observe that:

- **M1**: $1 \ · (a_{ij}) = (1 a_{ij}) = (a_{ij}) \ \ \forall (a_{ij}) \in F^{m \times n}$

    <br>

- **M2**: $\alpha \ · (\beta \ · (a_{ij})) = \alpha \ · (\beta (a_{ij})) = (\alpha \beta (a_{ij})) = (\alpha \beta) \ · (a_{ij}) \ \ \forall \alpha, \beta \in F, (a_{ij}) \in F^{m \times n}$

    <br>

- **D1**: $$\alpha \ · ((a_{ij}) + (b_{ij})) = \alpha \ · \big((a_{ij} + b_{ij})_{ij} \big) = \big(\alpha (a_{ij} + b_{ij})_{ij} \big) = \big(((\alpha a_{ij}) + (\alpha b_{ij}))_{ij} \big)$$

    $$ = (\alpha a_{ij}) + (\alpha b_{ij}) = \alpha \ · (a_{ij}) + \alpha \ · (b_{ij}) \ \ \forall \alpha \in F, (a_{ij}),(b_{ij}) \in F^{m \times n}$$

    <br>

- **D2**: 

    $$(\alpha + \beta) \ · (a_{ij}) = (((\alpha + \beta)a_{ij})_{ij}) = ((\alpha a_{ij} + \beta a_{ij})_{ij}) = (\alpha a_{ij}) + (\beta a_{ij}) \ \ \forall \alpha, \beta \in F, (a_{ij})\in F^{m \times n}$$

    <br>

This way, $F$ is a field, $(F^{m \times n},+)$ is an abelian group and $( \ ·)$ is a field's action of $F$ over $(F^{m \times n},+)$. 

Thus, $\big(F,(F^{m\times n},+), \ · \big)$ is a vector space.

<br>

### 2.3.3. The space of functions from a set to a field. 

Consider now some field $K$ and some set $S \neq \varnothing$, then, remember that being $f : S \to K$ a function, this gets identified with his graph $f \subseteq S \times K : (\forall s \in S \ \exists ! \alpha \in K \mid (s,\alpha) \in f)$. 

Then, lets take the :

$$K^S := \Set{f \in \mathcal{P}(S \times K) \mid \forall s \in S \ \exists ! \alpha \in K : (s,\alpha) \in f}$$

In this context, we convine the notation  $f(s) = \alpha \iff (s,\alpha) \in f$, then let's call:

$$ f = \Set{(s,f(s)) \mid s \in S}$$



This is the set of all the functions from $S$ to $K$ and define an addition over $K^S$ elements as:

$$+ : K^S  \times K^S \to K^S \mid (f,g) \mapsto f+g:= \Set{(s,f(s) + g(s)) \mid s \in S}$$

Observe that, due to the closure in $(K,+)$ we have that $f(s) + g(s) \in K$, so $f+g \in K^S$. Or simply, abreviate it as the formulation: $(f+g)(s) = f(s) + g(s)$.

The addition definition agains get's defined directly against the addition in $K$, so $(K^S,+)$ is an abelian group. Being the neutral element  and the inverse defined as:

$$0 := \Set{(s, 0_K) \mid s \in S}$$
$$-f := \Set{(s, -f(s)) \mid s \in S}$$

<br>

Also, define the action:

$$· : K \times K^S \to K^S \mid  (\alpha, f) \mapsto \alpha \ · f := \Set{(s,\alpha f(s)) \mid s \in S}$$

And check that satisfies the field's action axiom:

- **M1**: $1 \ · f = \Set{(s,1 f(s)) \mid s \in S} = \Set{(s,f(s)) \mid s \in S} = f$ 

    <br>

- **M2**: 

    $$\alpha \ ·(\beta \ ·f ) =\alpha \ · \Set{(s,\beta f(s)) \mid s \in S} = \Set{(s,\alpha \beta f(s)) \mid s \in S} $$
    
    $$= (\alpha \beta) \ · \Set{(s, f(s)) \mid s \in S} = (\alpha \beta) \ ·f$$

    <br>

- **D1**: 

    $$\alpha \ · (f + g) = \alpha · \Set{(s, f(s) + g(s)) \mid s \in S} = \Set{(s,\alpha f(s) + \alpha g(s)) \mid s \in S}$$

    $$= \Set{(s,\alpha f(s)) \mid s \in S} + \Set{(s,\alpha g(s)) \mid s \in S} = (\alpha \ · f) + (\alpha \ · g)$$

    <br>

- **D2**: 

    $$(\alpha + \beta) \ · f =(\alpha + \beta) \ · \Set{(s, f(s)) \mid s \in S} = \Set{(s,(\alpha+\beta) f(s)) \mid s \in S}$$

    $$=\Set{(s,\alpha f(s)+\beta f(s)) \mid s \in S}= \Set{(s,\alpha f(s)) \mid s \in S} + \Set{(s,\beta f(s)) \mid s \in S}$$

    $$= (\alpha \ ·  f)+  (\beta \ · f)$$

    <br>

Thus, $( \ ·)$ is a field's action and $(K,(K^S,+),\ · )$ is a vector space.

<br>

### 2.3.4. The space of polynomial functions over a field K.

#### 2.3.4.1. Introduction to polynomials.

A polynomial is, elementally, the most simple algebraic expression that can be formed by combining an indeterminated with it self along with scalars of a field $K$ using addition and multiplication operations.

$$\sum_{i=0}^n \alpha_i x^i = \alpha_0 + \alpha_1 x \cdots + \alpha_n x^n$$

The concept of polynomial function emegers when you try to evaluate the expression on entities from a evaluation domain.

Note that we deliberately used *indeterminated* instead of unknown, since this last one resembles to the scalars of a field, but in a polinomial function, usually, the domain can be more than scalars, it can be tuples, matrix, of even other polynomials.

In summary, a polynomial is a generic presentation of a finite secuence of operations over a single object with himself along with two predefined operations.

#### Vector space of the polynomial functions over a field K

Then let's consider a field $K$ and the set:

$$\operatorname{Pol}(K, K) := \left\{\, f \in K^K \ \middle|\ \exists n \in \mathbb{N}_0,\ \exists (\alpha_0, \ldots, \alpha_n) \in K^{n+1} : \forall s \in K,\ f(s) = \sum_{i=0}^{n} \alpha_i\, s^i \,\right\}$$

Let's consider the same operations $+$ and $·$ than in the example before. Let's observe that:

- $\boldsymbol{0} \in Pol(K,K)$, since the function $f (s) = 0 = \sum_{i=0}^n 0 s^i\ \ \forall s \in S$ have a polynomial form.

- $f(s) + g(s) = (f+g)(s) =  \sum_{i=0}^n (\alpha_i + \beta_i)s^i \in Pol(K,K) \ \ \forall f,g \in Pol(K,K)$, so the addition is closed on $Pol(K,K)$.

- $ \forall f (-f \in Pol(K,K))$, just consider: $f(s) = \sum_{i=0}^{n} \alpha_i\, s^i$ other $g(s) = -(f(s)) = - (\sum_{i=0}^{n} \alpha_i\, s^i)$, then, is obvious that $(f + g)(s) = (g + f)(s) = \boldsymbol0$

    <br>

Thus, we've just demonstrated that $(Pol(K,K),+)\leq (K^K,+)$, the abelian condition comes from conmutativity on $(K,+)$, so $(Pol(K,K),+)$ is an abelian group. 

Observe that $\alpha \ · f \in Pol(K,K) \ \ \forall f \in Pol(K,K)$, meaning that it does have sense to define the action $· : Pol(K,K) \to Pol(K,K)$ as a subfunction of $· \in \mathcal{P}(K^K \times K^K)$ defined above. Thus the properties of the field's action $·$ described above already applies to $Pol(K,K)$ since is a subset of $K^K$.

Thus, the triple $(K,Pol(K,K),\ ·)$ is a vector space.

<br>

## 2.4. Immediate Properties from vector spaces.

Let's check some important properties from the vector spaces that are immediately derivated from the axioms. From now on, let's consider $(K,V, \ ·)$ as a vector space.

- Let be: $\boldsymbol{0} \in V, \alpha \in K$ then:

    $$\alpha \ · \boldsymbol{0} = \alpha \ · ( \boldsymbol{0} + \boldsymbol{0} ) = \alpha \ · \boldsymbol{0} + \alpha \ · \boldsymbol{0} \iff \alpha \ · \boldsymbol{0} = \boldsymbol{0} \ \ \forall \alpha \in K$$

    <br>

- Also, be $0 \in K, v \in V$, then:

    $$0 \ · v = (0 + 0) \ · v = 0 \ · v + 0 \ · v  \iff 0 \ · v  = \boldsymbol{0} \ \ \forall v \in V$$

    <br>

- Consider now $\alpha \in K : \alpha \neq 0$ and $v \in V$ such $\alpha \ · v = \boldsymbol{0}$, then observe $\alpha \neq 0 \implies \exists \alpha ^{-1} \in K$, thus

    $$\alpha \ · v = \boldsymbol{0} \iff \alpha^{-1}(\alpha \ · v) = (\alpha ^{-1} \alpha) \ · v = 1 \ · v = v = \alpha ^{-1} \ · \boldsymbol{0} = \boldsymbol{0}$$

    So, $(\alpha \ · v = \boldsymbol{0} \wedge \alpha \neq 0) \implies v = \boldsymbol{0}$ 

    Observe that essentially: $\alpha \ · v = \boldsymbol{0} \implies \alpha = 0 \vee v = \boldsymbol{0} \ \ \forall \alpha \in K, \forall v \in V$

    <br>

- Observe that: $0 = 0 \alpha = (1 - 1) \alpha = \alpha + (-1) \alpha \implies -\alpha = (-1)\alpha$

    <br>

- Lastly observe that, despite we've defined lineal combinations over two elements, the asociative and distrivutive property on the vector space makes that we can think about a lineal combination of $n$ vectors.

    Be $v, u_i \in V   \ \ \forall i \in \mathbb{N}$ and $ \alpha_i \in K : \alpha_i \ \ \forall i \in \mathbb{N}$, satisfying:

    $$ v  = \sum_{i = 1}^n \alpha_i u_i$$

    Then, we say that $v$ is a linear combination of the $u_1,u_2, \ldots,v_n$ vectors.

    <br>

# 3. Vector Spaces and Geometry.

Before concluding this introductory section on vector spaces, we shall consider the relation of vector spaces with geometry or the geometric intuition of vector spaces.

Although we haven't present this result yet, it is true that for any $K$-vector space $V$ with a finite dimension exists some $n \in \mathbb{N}$ for which $K^n$ and $V$ are isomorphic; $V \simeq K^n$, meaning that both are the same vector space and share the same specific properties, this will be completly acknowledge by the reader at the end of this post.

Thus, we can understand the geometric structure of any $K$-vector space by aluding to the geometric construction of $K^n$. 

<br>

## 3.1. Analitic Geometry: The affine space.

### 3.1.1. Definition.

Let's say that $K = \mathbb{R}$, then $\mathbb{R}^n$ is what we call an *affine space*. In this section we gonna explain briefly what an affine space is and how it diverges from the vector space and why this idea is geometrically interesting.

<br>

Let be $V$ a $K$-vector space and $\mathcal{A} \neq \varnothing$, whose items we will call *points*. Then, we define as an *affine space* over $V$ to a pair $(\mathcal{A},+)$ where $+ : \mathcal{A} \times V \to \mathcal{A}$ is a *simple transitive group action*. 

This means that $+$ satisfies group's action axioms:

- **$A1$ (Identity)**: $P + 0_V = P \ \ \forall P \in \mathcal{A}$
- **$A2$ (Associativity)**: $(P + u) + v = P + (u + v) \ \ \forall P \in \mathcal{A}, \forall u,v \in V$ 

Observe that at this point, as we discusse above with the action groups, $+$ offers a family of reversible parametrized transformations by the vector space $V$ that allow us to study the points of $\mathcal{A}$ through the vectors of $V$.

But also this action group is *free* and *transitive* (the combination give us the simple transitive property):

- **Transitivity**: $\forall P, Q \in \mathcal{A} \ \exists v \in V : P + v = Q$

    Every point on $\mathcal{A}$ is reachable by any other point through an $V$'s item. Thus, there are no distinguished, isolated or privileged points on $\mathcal{A}$.

    <br>

- **Free**: $\forall P \forall v (P + v = P \implies v = 0)$

    This essentially means that no points gets translated over itself, each non-zero vector moves one point $P$ over other point $Q$ such $P \neq Q$

    <br>

Observe that, **Transitivity** and **Free** property can be collapsed on:

$$\forall P, Q \in \mathcal{A} \ \exists! \ v \in V : P + v = Q$$

Let's observe that, if we consider $u,v \in V : P + u = P + v$, then $(P + u) + -v = (P + v) + -v$, by $A2$ is $(P + u) + -v = P + (u - v) = (P + v) + -v = P + (v - v) = P + 0_V$ and then, by $A1$, $P + (u - v) =P$, then by the **Free** property $P + (u - v) =P \implies u - v = 0_V$, thus $u = v$, so both properties implies the one above.

<br>

Also observe that if we consider as true the statement above, obviously the **transitivity** property applies but also the uniquity of $v$ implies the **Free** property since by $A1$ the $0_V$ already satisfies $P + 0_V  = P$, thus is $\forall v \in V \ (P + v = P \implies v = 0_V)$. So both statements coimplies themselves and can be substituted.

<br>

Thus, essentially, an affine space is the object resulting of applying vectors to study points of a non-empty set through a simple transitive group's action. 

<br>

### 3.1.2. Isomorphism by origin.

Let's now check some interesting property of affines spaces. The transitive property asserts that, from the $V$ perspective all points in $\mathcal{A}$ are equals, as we said, there are no privileged or distinguished points.

Now, lets take some $O \in \mathcal{A}$, then, we define the application: 

$$\Phi_O : \mathcal{A} \longrightarrow V \qquad P \longmapsto \overrightarrow{OP} : O + \overrightarrow{OP} = P$$

Obviously is a biyection since, fixing $O$ only one vector corresponds to one point $P$.

Let's also consider the following operations over the points of $A$ being $P,Q \in \mathcal{A}$ and $\lambda$ an scalar:

$$\begin{cases}P +_O Q := \Phi_O^{-1}\big(\Phi_O(P) + \Phi_O(Q)\big) \\ \lambda \cdot_O P := \Phi_O^{-1}\big(\lambda \ \Phi_O(P)\big)\end{cases}$$

Basically, we operate with the vectors assigned by $\Phi_O$ and then return the resulting point of $A$ (note that since $\Phi_O$ is biyective, we can consider the inverse $\Phi_O^{-1}$).

Let's see that $(\mathcal{A},+_O, ·_O)$ is a vectorspace:

- $(\mathcal{A},+_O)$ is an abelian group:

    - **Closure**: For any $P, Q \in \mathcal{A}$, $\Phi_O(P), \Phi_O(Q)$ ae defined as vectors of $V$ and since $V$ is a vector space, the lineal combination $\Phi_O(P) + \Phi_O(Q)$ is garanted to be in $V$ and thus, since $\Phi_O$ is biyective, there exists a point $P' \in \mathcal{A} : \Phi_O(P') = \Phi_O(P) + \Phi_O(Q)$, so is $P' = \Phi_O^{-1}(\Phi_O(P) + \Phi_O(Q)) = P +_O Q \in \mathcal{A}$

        <br>

    - **Associativity**: 

        Let's observe that:
        
        $$P +_OQ =\Phi_O^{-1}(\Phi_O(P)) +_O \Phi_O^{-1}(\Phi_O(Q)) = \Phi_O^{-1}\big(\Phi_O(P) + \Phi_O(Q)\big)$$

        Then, applying the same scheme, we have: 

        $$(P +_OQ) +_OT = \Phi_O^{-1}\big(\Phi_O(P) + \Phi_O(Q)\big) +_O \Phi_O^{-1}(\Phi_O(T))$$

        $$= \Phi_O^{-1}\big([\Phi_O(P) + \Phi_O(Q)] + \Phi_O(T)\big)$$

        Thus, by the associativity in $(V,+)$ is:

        $$(P +_OQ) +T = P +(Q +_OT)$$

        <br> 

    - **Identity**: Let's check that $O$ satisfies $\Phi_O(O) = 0 \in V$ (by $A1$ and the simple transitivity property):
    
        $$P +_O O = O +_O P = P \ \ \forall P \in \mathcal{A}$$
        
        <br>

    - **Inverse**: Check that since $(V,+)$ is an abelian group for each $v \in V$ exists one and only one $u \in V$ such $v + u = u + v = 0$ and we say $u = -v$.
    
        Thus since $\Phi_O$ is biyective, for each $P \in \mathcal{A} : \Phi_O(P)=v $ exists a unique $Q$ such $\Phi_O(Q) = -v$. And is:

        $$P +_O Q =\Phi_O^{-1}(v + (-v)) = \Phi_O^{-1}(0) = O$$

        The same $Q +_O P$.

        <br>

    - **Conmutativity**: Immediate from the conmutativity in $(V,+)$.

        <br>

- $·_O:K \times A \to A$ is a field's action. 

    - **M1**: $1 ·_O P = \Phi_O^{-1}(1 · \Phi_O(P)) =  \Phi_O^{-1}(\Phi_O(P)) =P$
    - **M2**: $\alpha ·_O (\beta ·_O P) = \alpha ·_O\Phi_O^{-1}(\beta · \Phi_O(P)) = \Phi_O^{-1}(\alpha\beta · \Phi_O(P)) = (\alpha \beta) ·_O P$
    - **D1**: $\alpha ·_O  (P +_O Q) = \alpha ·_O \Phi_O^{-1}(\Phi_O(P) + \Phi_O(Q)) = \Phi_O^{-1}(\alpha · \Phi_O(P) + \alpha · \Phi_O(Q)) =$

        And by the same property announce in the associativity point, is:

        $= \Phi_O^{-1}(\alpha · \Phi_O(P)) + \Phi_O^{-1}(\alpha · \Phi_O(Q))  = \alpha ·_O P +_O \alpha ·_O Q$

    - **D2**: $(\alpha + \beta) ·_O P = \Phi_O^{-1}((\alpha + \beta) · \Phi_O(P)) = \Phi_O^{-1}(\alpha·\Phi_O(P) + \beta·\Phi_O(P)) = \alpha ·_O P +_O \beta ·_O Q$

    <br>

And by the biyection $\Phi_O$ is isomorph to $V$. This means that when whenever we select an origin $O$ in which define $\Phi$ we automatically instantiate (through $+_O,·_O$) a copy of $V$. **An affine space aqcuires a vector space structure when you fix a point.**

<br>

## 3.2. Vectors as geometric objects: Arrows.
Thus, let's conserve this conception about an affine space. Again an affine space is what result from use vectors to study a non empty set in a simple and transitive way. At this point we have introduced the idea of a vector as an algebraic item, but we know can introduce his natural geometric counterpart.

<br>

### 3.2.1. Bound arrows. Vectors as arrows.

Let's consider the affine space $(\mathcal{A},+)$ over the $K$-vector space $V$ and also, fixed an origin $O \in A$, define $\Phi_O, +_O,·_O$ as above, and subsequently we get the $K$-vector space: $(K,(\mathcal{A},+_O),·_O)$ isomorph to $V$.

In this context, lets get two points $P,Q \in \mathcal{A}$, we subtly introduced before the idea of the *arrow*. When we said in $(A,+)$ there is some $v \in V: P + v = Q$ we were introducing the idea about $v$ being a "displacement" from $P$ to $Q$:

![vector1](/assets/images/Maths/Algebra/vector1.png)

Let's identify $v$ with $P$ and $Q$ through the following application:

$$\delta : \mathcal{A} \times \mathcal{A} \longrightarrow V, \quad (P,Q) \longmapsto v = \overrightarrow{PQ}$$

Observe that $v$ is unique for each pair and that there are a few properties that $\delta$ satisfies that are released from the axioms of the affine space:

- $\overrightarrow{PP} = 0_V$​, from $A1$ and simple transivity.

    <br>

- **Chasles Relation**: $\overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR}$

    Let's quicly observe that: $P + \overrightarrow{PQ} = Q \wedge Q + \overrightarrow{QR} = R$

    Thus, using $A2$ we get: $R = Q + \overrightarrow{QR} = (P + \overrightarrow{PQ}) + \overrightarrow{QR} = P + (\overrightarrow{PQ} + \overrightarrow{QR})$, thus:

    $$P + (\overrightarrow{PQ} + \overrightarrow{QR}) = R \iff \overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR}$$

    <br>

- $\overrightarrow{QP} = -\overrightarrow{PQ}$​. This result is immediate from above: $0_V = \overrightarrow{PP} = \overrightarrow{PQ} + \overrightarrow{QP} \iff \overrightarrow{QP} = -\overrightarrow{PQ}$

    <br>

In this context, we say that the pair $(P,Q)$ or simply $\overrightarrow{PQ}$ is a "bound arrow", which his base in $P$ and his end in $Q$. We formalize this idea applying $\delta$ construction.

A *bound arrow* is a pair $(P,v) \in \mathcal{A} \times V$ often related as $(P,\overrightarrow{PQ})$ and interchangeble with $(P,Q)$ since two elements define the third.

<br>

Let's pull back briefly to the vector space $(K,(\mathcal{A},+_O),·_O)$. 

Let's observe that having fixed $O$, then we can collapse $\delta: A \times A \to V$ to $\delta_O: \mathcal{A} \to V$, verifying:

$$\delta_O( \ ·) = \delta(O, \ · )$$

Since the simple transivity of $+$ imposes a unique displacement from one point to another, fixing one of those points allow us to identify every each point on $A$ with a unique "position relative to $O$" vector in $V$. 

This means that we can treat each point on $A$ as an arrow from $O$, the identity of the abelian group $(A,+_O)$. **In other words, the collection of arrows from an origin has a structure of vector space**. This allow us to think in vectors as arrows in a, line, plane, space and so on.

<br>

### 3.2.2. Equipolence class: Free vectors.

Let's observe that bound vectora, conceptualized as a displacement, has magnitude, direction and an orientation in the direction. Thus, despite the point of application, two bound vectors are equal if both matches this three features.

This leads to the construction of the notion of the *free vector* as a equivalent class of those bound vectors that share this three features.

<br>

#### 3.2.2.1. Appex: Equivalence Class.

An *equivalence class* is the set of all elements in a set that we consider "equal" under a certain criterion of equality. The idea is that when we declare certain objects to be interchangeable for our purposes (even if they are not literally the same object), we group together all those that share that quality. That group is the class.

Their importance is structural: equivalence classes are the mechanism that allows us to quotient a set, that is, to create a new set whose points are precisely those packages.

<br>

Formally, be $X$ a non-empty set, a *equivalence relation* is binary relation $\sim \ \subseteq X\times X$ satisfying:

- *Reflexivity*: $\forall x \in X \quad x \sim x$
- *Simetry*: $\forall x,y \in X \quad x \sim y \implies y \sim x$
- *Transitivity*: $\forall x,y,z \quad x \sim y \wedge y \sim z \implies x \sim z$

In this conditions, this equivalence relation defines our criterion to build the equivalence classes $[x]$, formally:

$$[x] :=\ \Set{ y \in X : y \sim x }$$

We say that $x$ is the representant of the class. Observe that the following immediate properties are satisfied by the equivalence class:

- $x \in [x] \ \ \forall x \in X$
- $x \sim y \iff [x] = [y]$
- $\forall x,y \in X \ (x \sim y \oplus x \not \sim y \implies [x] = [y] \oplus [x] \cap [y] = \varnothing)$

    This means that two elements of $X$ are equivalent or not are equivalent at all, following the second property, this means that his equivalence classes are disjoints or are the same.

- $\displaystyle\bigcup_{x \in X} [x] = X$

    <br>

Lastly, we define the cocient set as:

$$X/\sim := \Set{[x] : x \in X}$$

This are the set whose elements are the group of elements that are qualitative different according with the $\sim$ criterion.

<br>

#### 3.2.2.2. Vector equipolence.

Now, let's say that $X = A \times A$, then we define in $A \times A$ the relation:

$$(P,Q) \sim (P',Q') \iff \overrightarrow{PQ} = \overrightarrow{P'Q'}$$

Observe that reflexivity, simetry and transivity are immediate from $=$ in $V$. Thus, two bound vectors are equal as long as they displacement is the same in magnituted, direction and orientation despite the application point.

<br>

This criterion allow us to define the cocient set:

$$\mathfrak{F}(\mathcal{A}) := (\mathcal{A} \times \mathcal{A})/\sim$$

Whose equivalent class are $[(P,Q)]$. Let's now observe carefully that this structure has a vector space structure.

First, let's fix an origin in $\mathcal{A}$, $O$ and consider the vector space $(K,(\mathcal{A},+_O),·_O)$ and observe that for each equivalence class $[(P,Q)]$, there is some $T \in \mathcal{A} : (O,T) \in [(P,Q)] \iff [(O,T)] = [(P,Q)]$, meaning that we can define:

$$\iota_O : \mathcal{A} \longrightarrow \mathfrak{F}(\mathcal{A}), \qquad P \longmapsto [\,(O,P)\,]$$

This function is biyective since $O$ is fixed and we can transport $(+_O, \cdot_O)$ to the cocient set $\mathfrak{F}(\mathcal{A})$ by operating with the canonical representant of each class. 

So $(K, (\mathfrak{F}(\mathcal{A}),+_O),·_O)$ is a vectorspace and this ultimately means that, in an affine space, whenever we treat a vector $v$ we catch the canonical representant of his equivalence class relative to an origin $O$, and work with it as if both where the same vector.

As an example, observe that this matchs some known operation with points and vectors. Consider $P,Q \in \mathcal{A}$, we can identify each point with his vector from the origin, $\overrightarrow{OP}, \overrightarrow{OQ}$. Then, by Chasles:

$$\overrightarrow{PQ} = \overrightarrow{PO} +\overrightarrow{OQ} = - \overrightarrow{OP} + \overrightarrow{OQ} \iff \overrightarrow{OP} + \overrightarrow{PQ} = \overrightarrow{OQ}$$

Meaning that substract $P$ to $Q$ (from any arbitrary point) give us the displacement from $P$ to $Q$ formalized in $\overrightarrow{PQ}$ and the thing is that we would not work directly with $\overrightarrow{PQ}$ but with the canonical representant of his equivalence class, $\overrightarrow{OT} : \overrightarrow{OT} \sim \overrightarrow{PQ}$

![vector1](/assets/images/Maths/Algebra/vector1.png)

<br>

# 4. Summary.

As a brief summary of the post, we have define Algebra as a mathematic discipline that occupies the study of the properties of operations. In this context, we develop an algebraic definition of the vector space as an algebraic structure in which a deformation mechanism acts on an abelian group standarizating the "linear combinations" as the natural operation of this space, understanded those as independants and weighted by a field contributions of elements from the abelian group. 

Later, we explore the geometric intuition behind the vector spaces. For that, first we define the affine space as the object resulting of use a vector space in a simple and transitive way to study a non-empty set. We also see that the affine space is a "point-uniform" structure and whenever you fix one point as a source of vectors, the affine space aqcuires a vector space.

Then, we build the concept of "bound vector" as a displacement between two points in the affine space and identify such bound vector with the mathematical object we call "arrow". This wat, with an origin fixed, we define a biyective application that identifies any point with a certain vector from the origin. Thus, the collection of all possible arrows that stems from a point in an affine space has structure of vector space and that is the precise visual representation we were searching.

Ultimately we formalize the bound vector as a "free vector" being this the equivalence class of all the bound vectors that share magnitude, direction and orientation. The set of all free vectors has also a vector space structure which allow us to identify any bound vector on the affine space with his canonical class representant and operate with it as if both were the same vector.