---
layout: post
title: "1. Linear Equations & Matrix."
subtitle: "Fields, Linear Equations and Matrix on a field."
date: 2026-02-06 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
---

# 0. Index.

1. Fields.
    - 1.1. Number sets.
    - 1.2. Groups.
        - 1.2.1. Intuitive Approach and definition.
        - 1.2.2. Immediate properties.
    - 1.3. Fields.
        - 1.3.1. Intuitive approach and definition.
        - 1.3.2. Properties of a field.
        - 1.3.3. Identities relations lemma.
2. System of Linear Equations.
    - 2.1. Brief introduction. Linear meaning.
    - 2.2. Formal definition.
    - 2.3. Equivalent Systems. Operations between predicates.
        - 2.3.1. System equations as predicates. Equivalence.
        - 2.3.2. Equivalence preservation.
    - 2.4. Exercises.
3. Matrices and Elementary Row Operations.
    - 3.1. Equivalent representation.
    - 3.2. Matrix.
        - 3.2.1. Definition and conceptual meaning.
        - 3.2.2. Elementary operations.
            - 3.2.2.1. Direct operations.
            - 3.2.2.2. Inverse Operations.
        - 3.2.3. Row-equivalence of Matrices and equivalence of system equations.
4. Row-reduced forms.
    - 4.1. Row-reduced.
        - 4.1.1. Definition.
        - 4.1.2. Row-reduced exercises.
    - 4.2. Row-reduced echelon.
        - 4.2.1. Definition.
        - 4.2.2. Properties.
    - 4.3. Augmented Matrix.
        - 4.3.1. Definition.
        - 4.3.2. RREM and Augmented matrix exercises.
5. Matrix Multiplication.
    - 5.1. Definition.
    - 5.2 Properties.
        - 5.2.1. Associativity.
        - 5.2.2. Power of Matrix.
    - 5.3. Elementary Matrix and Elementary Row Operations abstraction.
        - 5.3.1. Identity Matrix.
        - 5.3.2. Elementary Matrix.
    - 5.4. Matrix product exercises.
6. Invertible Matrices.
    - 6.1. Definition. Left, Right and two-sided inverse.
    - 6.2. Important Properties of the inverse.
    - 6.3. Elementary Matrices and Inverse.
        - 6.3.1. Inverse of elementary matrix.
        - 6.3.2. Characterization of invertible matrix.
        - 6.3.3. Invertible Matrix and Linear Equation Systems.
7. Summary.
- 7.1 Summary of the chapter.
- 7.2. Key results.

<br>

# 1. Fields.

## 1.1. Number sets.

A main focus of high-school mathematics lifes in the development of the usual range of numbers, which is developed step by step 

$$\mathbb{N_{0}} \hookrightarrow \mathbb{Z} \hookrightarrow \mathbb{Q} \hookrightarrow \mathbb{R} \hookrightarrow \mathbb{C}$$

But this sets are characterized as algebraic structres with their own structures. For example:

- $N_0$ is also called a *monoid*, a set that allows an operation $+$ with a neutral element 0. But the elements $\neq 0$ do not have an inverse $-a$ with respect to +. (We remember that the inverse of an element $a$ is another element $-a$ that complies with $a + (-a) = 0$).

- If we extend to $\mathbb{Z}$ and add also the multiplication we obtain a *commutative ring* with unit. Most elements do not have a multiplicative inverse.

- Then, again, we can expand $\mathbb{Z}$ to $\mathbb{Q}$ among with the notion of a *fraction* in order to ensure that every element has a multiplicative inverse, this is called a *field*. But then, there exists equations, like $x^2 - 2 = 0$ with no solutions in $\mathbb{Q}$.

- Then, we expand $\mathbb{Q}$ to $\mathbb{R}$ in order to give solution for that equation and forming the notion of irrational numbers; $\sqrt 2, \pi, etc$. This is called a *complete field*. But again, $x^2 + 1 = 0$, for a different reason, this equation also has no roots.

- Now, we expand for $\mathbb{R}$ to $\mathbb{C}$. These now give a completely valued (concept of analysis), algebraically closed (concept of algebra) field.

In summary, one observes that in each step, one starts from an range of numbers already constructed before, in which many natural calculations can be executed, but which still lacks some natural requirement. The extensions of the range of numbers are always aimed to achieve this requirement and indeed each time are realised by the simplest, most obvious way to supplement the existing range of numbers so that it fulfills the additional wish.

<br>

## 1.2. Groups.

### 1.2.1. Intuitive Approach and definition.

A *group* is the abstract structure you get when you isolate the idea of “doing an operation” that:

- It can be repeatedly composed (do it, then do it again).

- Has a "do-nothing" action (identity).

- Lets you undo any action (inverse).

- Composition behaves coherently (associativity).

This is the algebraic backbone behind symmetry, modular arithmetic, many cryptographic constructions, and (indirectly) the algebra meet in elliptic curves.

A formal definition would be; a group is a pair $(G,\circ)$ where:

- $G$ is an non-empty set.

- $\circ : G \times G \to G$ is a binary operation satisfying the following statements:

    1. **Closure**: $\forall a,b \in G \ \ a \circ b \in G$
    2. **Associativity**:   $\forall a,b,c \in G \ \ (a \circ b) \circ c = a \circ (b \circ c) \in G$
    3. **Identity element**: $\exists e \in G : a \circ e = e \circ a = a \ \forall a \in G$. This is what encloses the idea of doing nothing, the operation that leaves all as it is.
    4. **Inverse element**: $\forall a \in G \  \exists a^{-1} \in G : a \circ a^{-1} = a^{-1} \circ a = e$. This is the *undo* posibility any groups lets.

    <br>

### 1.2.2. Immediate properties.

Some immediate facts are:

- The **identity element is unique** in $G$:

    $$a,g \in G : \begin{cases} a \circ e = e \circ a = a \\ a \circ g = g \circ a = a\end{cases} \ \ \forall a \in G$$

    Then, we could reason that $e = e \circ g = g$.

    <br>

- The **inverse element is unique for each $a \in G$**:

   $$a \in G \ \exists b,c \in G : \begin{cases} a \circ b = b \circ a = e \\ a \circ c = c \circ a = e\end{cases}$$

   Then, we can reason again: $b = b \circ e = b \circ (a \circ c) = (b \circ a) \circ c = e \circ c = c$.

   <br>

- **Cancelation**:

    $$\forall a,b,c \in G : \begin{cases} a \circ b = a \circ c \Rightarrow c = b \\ b \circ a = c \circ a \Rightarrow c = b\end{cases}$$

    We gonna demonstrate partially composing by the left:

    $$a \circ b = a \circ c \iff a^{-1} \circ (a \circ b) = a^{-1} \circ (a \circ c) \iff$$
    $$(a^{-1} \circ a) \circ b = (a^{-1} \circ a) \circ c \iff e \circ b = e \circ c \iff b = c$$

    The same can be achieve composing by the right.

    <br>

As a example; the pair $(\mathbb{Z},+)$ is a group, let's demonstrate it:

- Associativity: $a + (b + c) = (a + b) + c \ \ \forall a,b,c \in \mathbb{Z}$
- Identity: $\exists ! \ 0 \in \mathbb{Z} : a + 0 = 0 + a = a \ \ \forall a \in \mathbb{Z}$
- Negative (Inv.): $\forall a \in \mathbb{Z} \ \exists ! \ (-a) \in \mathbb{Z} : a + (-a) = (-a) + a = 0$

<br>


Associated with the *group* is the *abelian group* idea, which is a group satisfying the **conmutativity property**:

$$ \forall a,b \in G \ ( a \circ b = b \circ a) $$

<br>

## 1.3. Fields.

### 1.3.1. Intuitive approach and definition.

A **field** is an algebraic structure in which you can add, subtract, multiply, and divide (by nonzero elements) and the usual arithmetic laws hold.

Formally, a field is a triple $(F,+,·)$ where $F$ is a non-empty set and $+$ and $·$ are binary operations satisfying that $\{F,+\}$ (Additive structure) and $\{F \setminus \{0\}, \ ·\}$ (Muiltiplicative structure) are two compatible abelian groups, meaning:

1. $\{F,+\}$ and $\{F \setminus \{0\}, \ ·\}$ are abelian groups.

2. The addition and multiplicative operations satisfies the *distributive* property:

    $$a \ · (b + c) = a · b + a·c \ \ \forall a,b,c \in F$$

As examples, $\Set{\mathbb{C},+, \ ·}$ and $\Set{\mathbb{R}, + , \ ·}$ are fields.

<br>

### 1.3.2. Properties of a field.

A field $\Set{F,+, \ ·}$, separate as two compatible abelian groups: $\Set{F,+}$ and $\Set{F\setminus \Set{0}, \ ·}$, satisfies the properties.

$\forall x ,y ,z \in F$:

- *Closure*: $\begin{cases} \ x + y \in F \\\\ \ x·y \in F \end{cases}$

- *Associativity*: $\begin{cases} \ (x + y) + z = x + (y + z) \\\\ \ (x·y)·z = x·(y·z) \end{cases}$

- *Conmutativity*: $\begin{cases} \ x + y = y + x \\\\ \ x·y = y·x \end{cases}$

- *Identities*: $\begin{cases} \ \exists! \ 0 \in F : x + 0 = x \\\\ \ \exists! \ 1 \in F : x·1 = x \end{cases}$

- *Negative and Inverse*: $\begin{cases} \ \forall x \in F \ \exists ! \ -x \in F : x + -x = 0 \\\\ \ \forall x \in F \setminus \Set{0} \ \exists ! \ \ x^{-1} \in F : x · x^{-1} = 1 \end{cases} \ \land \ 0 \neq 1$ in order to avoid trivial zero-ring $F:=\Set{0}$.

- *Compatibility*: $\ \ x·(y + z) = x·y + x·z$


- *Cancelation*: $\begin{cases} x + y = x + z \iff y = z \\\\ x · y = x·z \ \land \ x \neq 0 \iff y = z \end{cases}$

<br>

### 1.3.3. Identities relations lemma.

Being $\Set{F,+, \ ·}$ a field.

Let's observe that there are important relations between the identities of the additive and multiplicative structures:

 $$\begin{cases} x · 0 = 0 \\ x·y=0 \iff (x = 0 \ \vee \ y=0) \ \end{cases} \ \forall x,y \in F $$

1. First, lets proof that $x·0 = 0$. Taking the compatibility property of $F$, then:

    $$x · 0 = x · (0 + 0) = x·0 + x·0 \iff x·0 = 0$$

    <br>

2. Now, from (1):

    $$xy = 0 \implies \begin{cases} x \neq 0 \implies \cancel{x}y=\cancel{x}0 = 0 \implies y = 0 \\y \neq 0 \implies x\cancel{y} = 0 \cancel{y} = 0 \implies x = 0 \\ x = 0 \land y = 0\end{cases} \iff (x = 0 \vee y = 0)$$

    <br>
    
    If, $x = 0 \vee y = 0 \implies xy= 0$ trivially from (1). 
    
    Thus, $xy= 0 \iff (x = 0 \vee y = 0)$.

    <br>

3. Let's also observe that: $1_K = 1_F \wedge 0_K = 0_F \ \ \forall K \subset F : \Set{K, +, \ ·}$ is a field.

    In $F$, the identity is $1\_F$, then due to uniqueness of this identity in $F$ is $1\_K = 1\_F$ for the elements of $K$ in $F$, so isolating $K$ from $F$ necesarily is $1\_{F} \in K$ and the same can be applied to $0$, meaning that any subfield inherit the identity of the superfield.

<br>

# 2. System of Linear Equations.

## 2.1. Brief introduction. Linear meaning.

In maths, “Linear” means no interactions between variables and no bending. In this context, a linear combination of a finite set of variables $\Set{x,y,\cdots}$ means:

- No interactions betweem elements in $\Set{x,y,..}$; no products $(xy)$, squares $(x^n): n \in \mathbb{R}$, etc.
- A change in the inputs (“add” or “scale”), provokes a proportional change in the output.

Then, a **system of linear equations** is a collection of constraints or predicates in the form of linear expressions on a finite number of unknowns. The solutions of the whole system are the points that satisfy all constraints at once, the intersection of the predicates.

<br>

## 2.2. Formal definition.

Let be $F$ a field and $m,n \geq 1$, then a finite system of $m$ linear equations in $n$ unknowns over $F$ is specified by:

- Coefficients: $a_{ij} \in F: 1 \leq i \leq m, 1 \leq j \leq n$
- Unknowns:  $x_{j} \in F: 1 \leq j \leq n$
- Constants: $b_i \in F: 1 \leq i \leq m$

Related as:

$$\begin{cases} \displaystyle\sum_{j = 1}^na_{1j}x_{j} = b_1 \\ \ \  \vdots \\ \displaystyle\sum_{j = 1}^na_{mj}x_{j} = b_m\end{cases} \iff \begin{cases} a_{11}x_{1} \cdots + a_{1n}x_{n} = b_1 \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n} = b_m\end{cases} $$

Then, any tuple $(x_1,\cdots,x_n) \in F^n$ that satisfies all the constraints simultaneusly is called a *solution* of the system.

The system is called *homogeneous* if $b_i = 0 \ \forall i \in [m]$.

<br>

## 2.3. Equivalent Systems. Operations between predicates.

### 2.3.1. System equations as predicates. Equivalence.

As we said in the introduction, a lineal equation $a_1x_1\cdots + a_nx_n = b$ in a field $F$, can be understanded as a predicate $P(x):x \in F^n$. 

Then, a finite system of $m$ linear equations in $n$ unknowns over $F$ ($M$) can be understanded as the intersection of each predicate $P_i(x) : i \in [m]$:

<br>

$$M:=\begin{cases} a_{11}x_{11} \cdots + a_{1n}x_{1n} = b_1 \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n} = b_m\end{cases} \ \ \equiv \ \ \bigwedge_{i=1}^m P_i(x) : x \in F^n $$

<br>

In this terms, we can consider the set:

$$S_P := \Set{x \in F_n \ \vert \ P(x) \equiv \top}$$

Thus, the system $M$ describes the those $x \in F^n$ that satisfies the interseccions of the $S_{P_i}$ sets:

$$S:= \bigcap_{i=1}^m S_{P_i} = \Set{x \in F^n \ \vert \ M := \bigwedge_{i=1}^m P_i(x) \equiv \top}$$

We say that two equation systems, $M, M'$ are *equivalents* $M \equiv M'$ if they describes the same solution set $S$:

$$M \equiv M' \iff S = \Set{x \ \vert \ M \equiv \top} = \Set{x \ \vert \ M' \equiv \top}$$

<br>

### 2.3.2. Equivalence preservation.

As we see before, from the first order logic perspective, given a system $M:= P_1 \cdots \land P_m$ make a family of predicates $P_i':i \in [m]$ that preservers $S$ makes $M \equiv M':= P'_1 \cdots \land P'_m$

We can enunciate a set of operations between $P_i:i \in [m]$ that form a equivalent family of predicates that describes $M$ in the same way.

1. **Multiply by an scalar and replace**: $P \in M \wedge \lambda \in F\setminus \Set{0} \implies S_{\lambda P} = S_P $

    Let's observe that, if $P(x):=a_1x_1 \cdots + a_nx_n = y$, we define $\lambda P(x):=\lambda a_1x_1 \cdots + \lambda a_n x_n = \lambda y$, and now observe that be $x = (x_1,...,x_n) \in F^n$:

    $$x\in S_P \iff a_1x_1 \cdots + a_nx_n = y \iff$$
    $$\lambda(a_1x_1 \cdots + a_nx_n) = \lambda a_1 x_1 \cdots + \lambda a_n x_n = \lambda y \iff x \in S_{\lambda P}$$

    Thus, we can replace $S_{\lambda P}$ for $S_P$ without change $S$. 
    
    Then, being $P = P_j$ in $M$, we have that  $M':=  \lambda P \wedge \displaystyle\bigwedge_{i \neq j} P_i \equiv M$.

    <br>

2. **Add two equations and add**: $P,Q \in M \wedge \gamma ,\lambda \in F \setminus \Set{0} \implies S_{\gamma P + \lambda Q} \cap S_Q = S_P \cap S_Q $

    Again, we consider that $P(x):=p_1x_1 \cdots + p_nx_n = y_p$ and $Q(x):=q_1x_1 \cdots + q_nx_n = y_q$ thus:

    $$x \in S_P \cap S_Q \iff \begin{cases} p_1x_1 \cdots + p_nx_n = y_p \\ q_1x_1 \cdots + q_nx_n = y_q\end{cases} \iff  \begin{cases} \gamma p_1x_1 \cdots + \gamma p_nx_n - \gamma y_p = 0 \\ -\lambda q_1x_1 \cdots - \lambda q_nx_n + \lambda y_q = 0\end{cases}$$

    $$ \implies  \gamma p_1x_1 \cdots + \gamma p_nx_n - \gamma y_p = -\lambda q_1x_1 \cdots - \lambda q_nx_n + \lambda y_q  \iff $$

    $$ \iff (\gamma p_1 + \lambda q_1) x_1 \cdots +(\gamma p_n + \lambda q_n) x_n = \gamma y_p + \lambda y_q \iff x \in S_{\gamma P + \lambda Q}$$

    Which means, $S_P \cap S_Q \subseteq S_{\gamma P + \lambda Q}$

    How ever, is not true that $S_{\gamma P + \lambda Q} \subset S_P \cap S_Q$, being $\gamma = \lambda = 1$ and $y_q = y_p = 1$, then being $x \in F^n$ such:
    
    $$\begin{cases}p_1x_1 \cdots p_nx_n = 0 \\ q_1x_1 \cdots q_nx_n = 2 \end{cases}$$

    Then, clearly, $x \in S_{1P_1 + 1Q_1} \subset S_{\gamma P + \lambda Q} \wedge x \notin S_P \cap S_Q$, meaning that we loose information and we cannot replace those sets between them, we only can add it to the global intersection.

    In other words, since $S_P \cap S_Q \subset S_{\gamma P + \lambda Q} \implies (S_P \cap S_Q) \cap S_{\gamma P + \lambda Q} = S_P \cap S_Q$, then:

    $$S := \bigcap_{i=1}^m S_{P_i} = S_{\gamma P + \lambda Q} \cap \bigcap_{i=1}^m S_{P_i} $$

    Implying that the sistem: $ M' := (\gamma P + \lambda Q) \wedge \displaystyle\bigwedge_{i=1}^m P_i \equiv\bigwedge_{i=1}^m P_i = M$ 
    
    Let's also observe that we loose information in the sense that force the addition of two numbers $y_p,y_q$ to be equal to a third, $c$; $y_p + y_q = c$, does not determines neither of the two, exists a variety of solutions for $(y_p,y_q) \in F^2$ but giving a value to any of those, $y_i$ automatically determines the other one $y_j = c - y_i$. 

    This can be extrapoled to or predicates, $x \in F^n:(P + \lambda Q) \wedge Q \implies P$ leading to the correct replacing rule which is $(P + \lambda Q) \wedge Q \iff P \wedge Q$, and in terms of the solution set:
    
    $$S_{\gamma P + \lambda Q} \cap S_Q = S_P \cap S_Q$$

    And, being $P_j = P$, then  $M' := (\gamma P + \lambda Q) \wedge \displaystyle\bigwedge_{i\neq j} P_i \equiv\bigwedge_{i} P_i = M$

Let's observe that two equivalent non-trivial sistems ($S \neq \varnothing$) define the same solutions set by imposing in some sense the same constraints on $F$. Meaning that any predicate on $M$ can be derivated from $M'$ am viceversa. Despite this isn't a mathematical explanation, it is convenient to us to know the following fact:

$$M = \displaystyle\bigwedge_{i}^t P_i \wedge M'=\displaystyle\bigwedge_{i}^l P'_i: M \equiv M' \wedge S \neq \varnothing \implies \forall i \leq t \ \exists \alpha_1,...,\alpha_l \in F: S_{P_i} = S_{\alpha_1P'_1 \cdots + \alpha_lP'_l}$$

The proof for this statement will be presented later.

<br>

## 2.4. Exercises.

### 2.4.1. Verify that the set of complex numbers $F:= \Set{z \ \vert \ \exists x,y \in \mathbb{Q} : z = x + y\sqrt{2}}$ is a subfield of $\mathbb{C}$.

Verifying that $\Set{F,+, \ ·}$ is a subfield of $\mathbb{C}$ requires to verify:

- $F \subset \mathbb{C}$, which is true by definition.
- $\Set{F, + , \ ·}$ is a field which implies to verify that $\Set{F,+}$ and $\Set{F\setminus \Set{0}, \ ·}$ are two compatible abelian groups.

Thus first, $\Set{F, +}$ verifies:

- **Closure**:

    Being $z_1,z_2 \in F$, then, leveraging that $\mathbb{Q}$ is a field: 

    $$z_1 + z_2 = x_1 + y_1\sqrt{2} + x_2 + y_2\sqrt{2} = (x_1 + x_2) + (y_1 + y_2)\sqrt{2}$$
    
    Thus, calling $x_3 = x_1 + x_2$ and $y_3 = y_1 + y_2$, then:
    
    $$\exists x, y \in \mathbb{Q}: z_1 + z_2 = x + y\sqrt{2} \iff z_1 + z_2 \in F$$

    <br>

- **Associativity**:

    Being $z_1,z_2,z_3 \in F$, then:

    $$z_1 + (z_2 + z_3) = [x_1 + (x_2 + x_3)] + [y_1 + (y_2 + y_3)]\sqrt{2} =$$
    
    $$[(x_1 + x_2) + x_3] + [(y_1 + y_2) + y_3]\sqrt{2} = (z_1 + z_2) + z_3$$

    <br>

- **Conmutativity**:

    Being $z_1,z_2 \in F$, then:

    $$z_1 + z_2 = (x_1 + x_2) + (y_1 + y_2)\sqrt{2} =$$
    
    $$(x_2 + x_1) + (y_2 + y_1)\sqrt{2} = z_2 + z_1$$

    <br>

- **Unique Identity**:


    Be $0 = 0 + 0\sqrt{2}$, then $z_1 + 0 = (x_1 + 0) + (y_1 + 0)\sqrt{2} = x_1 + y_1\sqrt{2} = z_1$

    <br>

- **Unique Inverse**: 

    Be $z = x + y\sqrt{2}$, then $-z = -x - y\sqrt{2}$ verifies:

    $$z + (-z) = [x + (-x)] + [y + (-y)]\sqrt{2} = 0 + 0\sqrt{2} = 0$$

    <br>

All this rules confirms that $\Set{F,+}$ is an *abelian group*. Let's begin with $\Set{F\setminus \Set{0}, \ ·}$:

- **Closure**

    Be, $z_1,z_2 \in F$, then proceding like above:

    $$z_1z_2 = (x_1 + y_1\sqrt{2})(x_2 + y_2\sqrt{2}) =\underbrace{(x_1x_2 + 2y_1y_2)}_{x} + \underbrace{(x_1y_2 + y_1x_2)}_{y}\sqrt{2} \in F$$

    <br>

- **Associativity**:

    Be $z_1,z_2,z_3 \in F$, then:

    $$z_1(z_2z_3) = (x_1 + y_1\sqrt{2})\big[(x_2x_3 + 2y_2y_3) + (x_2y_3 + y_2x_3)\sqrt{2}\big]=$$
    
    $$x_1(x_2x_3 + 2y_2y_3) + x_1(x_2y_3 + y_2x_3)\sqrt{2} + y_1\sqrt{2}(x_2x_3 + 2y_2y_3) + y_1\sqrt{2}(x_2y_3 + y_2x_3)\sqrt{2}= $$
    
    $$x_1(x_2x_3 + 2y_2y_3) + 2y_1(x_2y_3 + y_2x_3) + \big[x_1(x_2y_3 + y_2x_3) + y_1(x_2x_3 + 2y_2y_3)\big]\sqrt{2}=$$
    
    $$\big(x_1x_2x_3 + 2x_1y_2y_3 + 2y_1x_2y_3 + 2y_1y_2x_3\big) + \big(x_1x_2y_3 + x_1y_2x_3 + y_1x_2x_3 + 2y_1y_2y_3\big)\sqrt{2}$$


    And also;

    $$(z_1z_2)z_3 = \big[(x_1x_2 + 2y_1y_2) + (x_1y_2 + y_1x_2)\sqrt{2}\big](x_3 + y_3\sqrt{2}) =$$
    
    $$\big(x_1x_2x_3 + 2y_1y_2x_3 + 2x_1y_2y_3 + 2y_1x_2y_3\big)+ \big(x_1x_2y_3 + 2y_1y_2y_3 + x_1y_2x_3 + y_1x_2x_3\big)\sqrt{2}$$

    Thus, $z_1(z_2z_3) = (z_1z_2)z_3$

    <br>

- **Conmutativity**:

    $$z_1z_2 = (x_1 + y_1\sqrt{2})(x_2 + y_2\sqrt{2}) = (x_1x_2 + 2y_1y_2) + (x_1y_2 + y_1x_2)\sqrt{2}$$

    $$z_2z_1 = (x_2 + y_2\sqrt{2})(x_1 + y_1\sqrt{2}) = (x_2x_1 + 2y_2y_1) + (y_2x_1 + x_2y_2)\sqrt{2}$$

    
    And both expressions are equivallent due to conmutativity in $\mathbb{Q}$

    <br>

- **Unique Identity**: 

    Being $1 = 1 + 0\sqrt{2} \neq 0 + 0\sqrt{2} = 0$, then:

    $$z·1 = (x + y\sqrt{2})(1 + 0\sqrt{2}) = x + y\sqrt{2} = z$$

    <br>

- **Unique Inverse**:

    Being $z=x+y\sqrt{2}\in F$, we define the multiplicative inverse of $z$ as an element $z^{-1}\in F$ such that;

    $$z\neq 0 \;\Longrightarrow\; \exists\, z^{-1}\in F:\; z\cdot z^{-1}=1$$

    Equivalently, writing $z^{-1}=u+v\sqrt{2}$ with $u,v\in\mathbb{Q}$, the condition $z\cdot z^{-1}=1$ means
    
    $$(x+y\sqrt{2})(u+v\sqrt{2})=1+0\sqrt{2}$$
    
    $$(xu+2yv) + (xv+yu)\sqrt{2}=1+0\sqrt{2}$$
    
    Hence it is equivalent to the system
    
    $$\begin{cases}xu+2yv=1,\\ xv+yu=0. \end{cases}$$

    <br>


Lets now demonstrate that both abelians groups are compatible, but this is obvious for the arithmetic properties in $\mathbb{Q}$:

$$z_1(z_2 + z_3) = (x_1+y_1\sqrt{2})[(x_2+y_2\sqrt{2} + x_3+y_3\sqrt{2})] = $$

$$(x_1+y_1\sqrt{2})x_2 + (x_1+y_1\sqrt{2})y_3\sqrt{2} + (x_1+y_1\sqrt{2})x_3 + (x_1+y_1\sqrt{2})y_3\sqrt{2}=$$

$$(x_1+y_1\sqrt{2})(x_2 + y_2\sqrt{2}) + (x_1+y_1\sqrt{2})(x_3+y_3\sqrt{2}) = z_1z_2 + z_1z_3$$

<br>

### 2.4.2. Let $F$ be the field of complex numbers. Are the following two systems of linear equations equivalent? If so, express each equation in each system as a linear combination of the equations in the other system.

$$\begin{gather} \ x_1 - x_2 = 0 :P \ \ \ \ \ \ \ \ \ 3x_1 + x_2 = 0 :P'\\ 2x_1 + x_2 = 0 :Q \ \ \ \ \ \ \ \ \ x_1 + x_2 = 0 : Q' \end{gather}$$

<br>

First, to demonstrate that $M$ and $M'$ are equivallents we can solve it describying the sets $S$ and $S'$ and demonstrating that $S = S'$.

Solving $M$ we find that the first equation tell us that $x_1 = x_2$ and the second, $x_1 = 0$ so $S =\Set{(0,0)} \subset F$. Easily we can check that $S' = \Set{(0,0)} = S$, thus $M \equiv M'$.

Let no find $\alpha_1,\beta_1, \alpha_2, \beta_2$ such:

$$S_{\alpha_1P + \beta_1Q} = S_{P'} \\ S_{\alpha_2P + \beta_2Q} = S_{Q'} $$

We can formate a system equation:

$$\alpha_1P + \beta_1Q = P' \iff \alpha_1(x_1 - x_2) + \beta_1(2x_1 + x_2) = 3x_1 +x_2$$

Since we are interested in match coefficients for each unknown, we can form the following equations from the above:

$$\begin{cases} \alpha_1x_1 + \beta_12x_1 = 3x_1 \\ -\alpha_1x_2 + \beta_1x_2 = x_2\end{cases} \iff \begin{cases} \alpha_1+ 2\beta_1 = 3 \\ -\alpha_1 + \beta_1 = 1\end{cases} \iff \alpha_1 = \frac{1}{3} \ \wedge \ \beta_1 = \frac{4}{3}$$

Proceeding the same way with $Q'$; 

From $\alpha_2P + \beta_2Q = Q' \iff \alpha_2(x_1 - x_2) + \beta_2(2x_1 + x_2) = x_1 + x_2 \implies \alpha_2=-\displaystyle\frac{1}{3} \ \wedge \ \beta_2 = \frac{2}{3}$

<br>

### 2.4.3. Test the following systems of equations as in Exercise 2.

$$\begin{cases}
-x_1 + x_2 + 4x_3 = 0 :P \ \ \ \ \ \ \ x_1 - x_3 = 0 :P'\\
\ x_1 + 3x_2 + 8x_3 = 0 :Q \ \ \ \ \ \ \ x_2 + 3x_3 = 0:Q'\\
\frac{1}{2}x_1 + x_2 + \frac{5}{2}x_3 = 0 :T\\
\end{cases}$$

Solving the problem we can say that, for $M'$ is:

$$x_1 = x_3 \wedge x_2 = - 3x_3 \wedge x_3 \in F \implies S_{M'}:=\Set{x \in F^3 \ \vert \ x = (\alpha, -3\alpha, \alpha) : \alpha \in F}$$

On the other hand, for $M$ it is:

$$2P - Q = P':-3x_1 -x_2 = 0 \iff x_1 = -\frac{1}{3}x_2$$

Applying this results to $Q,T$, then we get:

$$\begin{cases}
\ x_1 + 3x_2 + 8x_3 = 0 :Q \\
\frac{1}{2}x_1 + x_2 + \frac{5}{2}x_3 = 0 :T
\end{cases} \implies \begin{cases}
\ -\frac{1}{3}x_2 + 3x_2 + 8x_3 = \frac{8}{3}x_2 + 8x_3 = 0 \\
-\frac{1}{6}x_2 + x_2 + \frac{5}{2}x_3 = \frac{5}{6} x_2 + \frac{5}{2} x_3 =  0 
\end{cases} \implies x_2 = -3x_3$$

And $x_3 \in F$, so $S_M = S_{M'}$ and both are equivalent systems. Let's take now the lineal combination of $M$ from $M'$:

$$\alpha_1P' + \beta_1Q' = P \iff \alpha_1(x_1 - x_3) + \beta_1(x_2+3x_3) = -x_1 + x_2 + 4x_3 \implies$$

$$\begin{cases} \alpha_1 x_1 = -x_1 \\ \beta_1x_2 = x_2 \\ -\alpha_1x_3 + 3\beta_1x_3 = 4x_3 \end{cases} \iff \begin{cases} \alpha_1 = -1 \\ \beta_1 = 1 \\ -\alpha_1 + 3\beta_1 = 4 \end{cases}$$

Thus, $-(x_1 - x_3) + (x_2+3x_3) = -x_1 + x_3 + x_2 3x_3 = -x_1 +x_2 + 4x_3$ and we verified the solution is correct.

Also, 

$$\alpha_2P' + \beta_2Q' = Q \iff \alpha_2(x_1 - x_3) + \beta_2(x_2+3x_3) = x_1 + 3x_2 + 8x_3 \implies$$

$$\begin{cases} \alpha_2 x_1 = x_1 \\ \beta_2x_2 = 3x_2 \\ -\alpha_2x_3 + 3\beta_2x_3 = 8x_3 \end{cases} \iff \begin{cases} \alpha_2 = 1 \\ \beta_2 = 3 \\ -\alpha_2 + 3\beta_2 = 8 \end{cases}$$

And: $(x_1 - x_3) + 3(x_2+3x_3) = x_1 +3x_2 + 8x_3$

Lastly:

$$\alpha_3P' + \beta_3Q' = T \iff \alpha_3(x_1 - x_3) + \beta_3(x_2+3x_3) = \frac{1}{2}x_1 + x_2 + \frac{5}{2}x_3 \implies$$

$$\begin{cases} \alpha_3 x_1 = x_1/2 \\ \beta_3x_2 = x_2 \\ -\alpha_3x_3 + 3\beta_3x_3 = \frac{5}{2}x_3 \end{cases} \iff \begin{cases} \alpha_3 = 1/2 \\ \beta_3 = 1 \\ -\alpha_3 + 3\beta_3 = 5/2 \end{cases}$$

We will prove it by: $\frac{1}{2}(x_1 - x_3) + (x_2+3x_3) = \frac{1}{2}x_1 + x_2 + \frac{5}{2}x_3 = 0$

<br>

### 2.4.4. Test the following systems as in Exercise 2.

$$\begin{cases}
2x_1 + (-1+i)x_2 + x_4 = 0:P\ \ \ \ \ \left(1+\frac{i}{2}\right)x_1 + 8x_2 - ix_3 - x_4 = 0:P'\\
3x_2 - 2ix_3 + 5x_4 = 0:Q\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \frac{2}{3}x_1 - \frac{1}{2}x_2 + x_3 + 7x_4 = 0:Q'
\end{cases}$$

Let's try to solve the first system.

First, take sistem $M$, and let's call $x_2 = \lambda$, $x_4 = \gamma$, then the sistem is:

$$\begin{cases} 2x_1 + (-1+i)\lambda + \gamma = 0 \\ 3\lambda - 2ix_3+ 5\gamma = 0\end{cases} \iff \begin{cases} x_1 = \frac{1}{2}((1-i)\lambda - \gamma) \\ x_3 = \frac{1}{2i} (3\lambda+ 5\gamma)\end{cases}$$

Then, $S_M = \Set{x \ \vert \ x = (\frac{1}{2}((1-i)\lambda - \gamma), \lambda,\frac{1}{2i} (3\lambda+ 5\gamma),\gamma) : \lambda, \gamma \in F} \subset F^4$

<br>

In the second system, we again call $x_2 = \lambda$, $x_4 = \gamma$, then the system is:

$$\begin{cases} \left(1+\frac{i}{2}\right)x_1 + 8\lambda - ix_3 - \gamma = 0 \\ \frac{2}{3}x_1 - \frac{1}{2}\lambda + x_3 + 7\gamma = 0\end{cases} \iff \begin{cases} \left(1+\frac{i}{2}\right)x_1 + 8\lambda - ix_3 - \gamma = 0 \\ x_3= \frac{1}{2}\lambda - \frac{2}{3}x_1-7\lambda\end{cases} \implies $$

$$\left(1+\frac{i}{2}\right)x_1 + 8\lambda - i(\frac{1}{2}\lambda - \frac{2}{3}x_1-7\lambda) - \gamma = 0$$

Getting $x_1$ is obvious that both systemas are not equivalent since the solution set $S_M$ and $S_M'$ are not the same.

<br>

### 2.4.5. Be $F := \Set{0,1}$, proof that $\Set{F,+, \ ·}$ is a field.

$$\begin{array}{c|cc}
+ & 0 & 1\\ \hline
0 & 0 & 1\\
1 & 1 & 0
\end{array}
\qquad
\begin{array}{c|cc}
\cdot & 0 & 1\\ \hline
0 & 0 & 0\\
1 & 0 & 1
\end{array}$$



As we see above, we have to see if $\Set{F,+}$ and  $\Set{F \setminus \Set{0}, \ ·}$ are compatible abelian groups:

- Being $\Set{F,+}$, then:

    - **Closure** From the table, the result of any composition of the elements of $F$ through $+$ is an element of $F$.

    - **Associativity**: Let's be $a,b,c \in F$, then let's impose that: $a + (b + c) \neq (a + b) + c$. Without loosing generality we can assume that:

        $$\underbrace{a + (b + c)}_{0} \neq \underbrace{(a + b) + c}_{1}$$

        So we can craft the solutions to the equations:

        $$ a + (b + c) = 0 \implies \begin{cases} a = 1 \wedge b + c = 1 \implies \begin{cases} a \wedge b \wedge \neg c \\ a \wedge \neg b \wedge c\end{cases}\\ a = 0 \wedge b + c = 0 \implies \begin{cases} \neg a \wedge \neg b \wedge \neg c \\ \neg a \wedge b \wedge c \end{cases}\end{cases}$$
        
        
        $$(a + b) + c = 1 \implies \begin{cases} a + b = 0 \wedge c = 1 \implies \begin{cases} a \wedge b \wedge c \\ \neg a \wedge \neg b \wedge c \end{cases} \\ a+b = 1 \wedge c = 0 \implies \begin{cases} a \wedge \neg b \wedge \neg c \\ \neg a \wedge b \wedge \neg c \end{cases}\end{cases}$$

        (The propostional notation, $a, \neg a$ is more than justified assuming that there are only two possible values in $F$)

        Thus, observe that none of the solution matches between the two equations, meaning that since the intersection of the solution set of both equations is empty, there are no values solving the predicate $a + (b + c) \neq (a + b) + c$.

        So we can ensure that $a + (b + c) = (a + b) + c \ \ \ \forall a,b,c \in F$.

        <br>

    - **Identity**: Observe that $0 + a = a + 0 = a \ \ \ \forall a \in F$

    - **Inverse**: For every element $a \in F$, $a$ is his own inverse:

        $$ 0 + 0 = 0 \wedge 1 + 1 = 0$$

        <br>

- Being $\Set{F \setminus \Set{0}, \ ·}$, then lets demonstrate that is a group.

    - **Closure**: By definition, any composition of the elements of $F$ by $·$ is an element of $F$.

        <br>

    - **Associativity**: $1·(1·1) = (1·1)·1 = 1$

        <br>

    - **Identity & Inverse**: Check that $1$ is at the same time the identity and his own inverse: $a·1 = 1·a = a \ \ \forall a \in F \setminus \Set{0}$


        <br>


- Lastly, demonstrate compatibility between the addition and the product define above in $F$. Let's suppose $a,b,c \in F$, then let's force: $a(b+c) \neq ab + ac$ or, in other terms: $a(b+c)  = 0 \wedge ab + ac = 1$.

    Let's see that:

    - $a(b+c) = 0 \implies \neg a \vee [(b \wedge c) \vee (\neg b \wedge \neg c)] : P$
    - $ab + ac \ = 1 \implies  \ \ a \wedge [(b \wedge \neg c) \vee (\neg b \wedge c)]\  : Q$

    Let's note that $Q$ forces $a$ to be $1$ and needs $b$ and $c$ to have different value; $S_Q:=\Set{(1,\alpha, \neg \alpha)}\subset F^3$. 
    
    $P$ admits $a$ to be $1$ but then it forces to $b$ and $c$ to share te same value; $S_P:=\Set{(\alpha,\beta, \gamma): \alpha \rightarrow (\beta = \gamma)}$ 
    
    
    Thus, there is no solution for the system equation since applying $S_P$ condition to $S_Q$ results in a contradiction, or in other terms:
    
    $$S_P \cap S_Q := \Set{(\alpha, \beta, \gamma) \in F^3 \ \vert \  \alpha \wedge (\beta \neq \gamma) \wedge [\alpha \rightarrow (\beta = \gamma)]} = \varnothing$$

    Observe that $\alpha \wedge (\beta \neq \gamma) \equiv \neg [(\neg \alpha) \vee (\beta = \gamma)] \equiv \neg[\alpha \to (\beta = \gamma)] \implies \alpha \wedge (\beta \neq \gamma) \wedge [\alpha \rightarrow (\beta = \gamma)] \equiv \bot$

    The case $a(b+c)  = 1 \wedge ab + ac = 0$ admits an analogous proof. Thus, always is $a(b+c) = ab + ac$

    <br>

### 2.4.6. Prove that if two homogeneous systems of linear equations in two unknowns have the same solutions, then they are equivalent.

Lets consider that first, we can safely assume that we have two system of two equations on two incognits, if there were $m \geq 3$, then there will be $m-2$ redundant equations, meaning that they do not add information to the sistem and can be safely excluded.

Also, in this context, as there are only two unknowns, this equations are expressing predicates over points in $\mathbb{R}^2$, specifically, this systems are four lines on $\mathbb{R^2}$ (we assume indepency between this two equations):

$$\begin{cases}
u_1 x +u_2y = 0 \\
v_1 x +v_2y = 0  
\end{cases} \ \ \ \ \ \begin{cases} w_1x + w_2y = 0\\ p_1x_1 + p_2y = 0 \end{cases}$$


Geometrically is easy to see that there is a lineal combination dependency between the direction vectors:

$$\alpha(u_2,-u_1) + \beta(v_2,-v_1) = (w_2,-w_1)$$

$$\lambda(u_2,-u_1) + \gamma(v_2,-v_1) = (p_2,-p_1)$$

Then, this scalars exists and can be calculated forming an equation system with the coordinates:

$$\begin{cases} \alpha u_2 + \beta v_2 = w_2 \\ \alpha u_1 + \beta v_1 =  w_1  \end{cases}$$

<br>

### 2.4.7. Prove that each subfield of the field of complex numbers contains every rational number. 

Be $\Set{F,+, \ ·} : F \subseteq \mathbb{C}$ a field, then we have to prove that $q \in F \ \ \forall q \in \mathbb{Q}$




Be $q \in \mathbb{Q}$, then $\exists a,b \in \mathbb{Z} : \displaystyle q=\frac{a}{b}$, then we can understand that $\mathbb{Z} \subset F \implies \mathbb{Q} \subset F$ since by the closure property $ab^{-1} \in F$. 

Let's see that 

- $1 + 0i = 1_{\mathbb{C}} \in F$
- $1$ in $F$ is inherited from the superfield $\mathbb{C}$;. 



Let's observe that:

$$1_\mathbb{C} \in F \underbrace{\implies}_{Peano} \mathbb{Z} \subset F\implies \mathbb{Q} \subset F$$

<br>

### 2.4.8. Prove that each field of characteristic zero contains a copy of the rational number field. 

Given a field $F$ of ·characteristic zero".

So we can build a function that design, along with the adition, the sucesor of each element and through an homomorfism $h$, identify $h(\mathbb{Z}) = K$ for some $K \subset F$ due to the fact that this function in $K$ never colapse into 0.

Also, we can think in another homomorfism $k$ that identifies $t(\mathbb{Q}) = T$ for some $T \subset F$. The argument is the same that above, since $F$ is a field, then for each element $a \in F$ exists an inverse $a^{-1} \in F$ and also $\Set{F, \ ·}$ is closed meaning that $ab \in F \ \ \forall a,b \in F$ so a copy of $\mathbb{Q}$ exists in $F$ if a copy $\mathbb{Z}$ can be proved.

$$\exists (K \subset F \wedge h:\mathbb{Z} \to K) : h(a + b)=h(a) + h(b) \ \ \forall a,b \in \mathbb{Z} \implies $$

$$\exists (T \subset F \wedge t:\mathbb{Q} \to T) : h(ab)=h(a) · h(b) \ \ \forall a,b \in \mathbb{Q}$$

<br>

# 3. Matrices and Elementary Row Operations.

## 3.1. Equivalent representation.

When forming linear combinations of linear equations there is only need to compute with the coefficients $a_{ij}: i \in [m] \wedge j \in [n]$ and  scalars $y_i:i \in [m]$ hence there is no need to continue writing the 'unknowns', $x_i : i \in [n]$ since there is only necesary .

Thus, we now abbreviate the system as:

<br>

$$\begin{cases} \displaystyle\sum_{j = 1}^na_{1j}x_{j} = b_1 \\ \ \  \vdots \\ \displaystyle\sum_{j = 1}^na_{mj}x_{j} = b_m\end{cases} \iff \begin{cases} a_{11}x_{1} \cdots + a_{1n}x_{n} = b_1 \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n} = b_m\end{cases} \iff AX = B$$

<br>

Where:

- $A$ is the **matrix of coeficients**:

    $$A= \begin{bmatrix}A_{11} & \cdots & A_{1n}\\\vdots & \ddots & \vdots\\A_{m1} & \cdots & A_{mn}\end{bmatrix}$$

    Strictly speaking, the rectangular array displayed above is not a matrix, but is a representation of a matrix, a concrete display or codification of the mathematical object we don't presente yet.

    <br>

- $X$ is the **matrix of unknowns**:

    $$X= \begin{bmatrix}X_{1} \\\vdots \\ X_{n}\end{bmatrix}$$

    <br>

- $Y$ is the **matrix of constants**:

    $$Y= \begin{bmatrix}Y_{1} \\\vdots \\ Y_{m}\end{bmatrix}$$

    <br>

The whole representation of the same equation system is:

<br>

$$\begin{bmatrix}A_{11} & \cdots & A_{1n}\\\vdots & \ddots & \vdots\\A_{m1} & \cdots & A_{mn}\end{bmatrix}· \begin{bmatrix}X_{1} \\\vdots \\ X_{n}\end{bmatrix} = \begin{bmatrix}Y_{1} \\\vdots \\ Y_{m}\end{bmatrix}$$

<br>

Before getting any deep, let's formally understand what a matrix is.

<br>

## 3.2. Matrix.

### 3.2.1. Definition and conceptual meaning.

**Conceptual approach**

Observe that while linear equation system, defined over a field $F^n$, are linear constraints over points of $F^n$, matrices are sofisticate packages of the linear information storage in the linear system which make it is easier to manipulate and measure.

Then, a *matrix* is a device to package information linearly codified. Is a structured way to record how a linear rule takes inputs to outputs (along with coordinates). 

Lets dedicate a few words about what 'linear' means. As we say above, *linear* refers to no bending. Is a term that refers to the way on how data is formuled to interact; at the simpliest level relative to the addition and the scaling, without products or powers over the unknowns (again, no bending). 

Thus a matrix encode information in a linear rule, respecting addition and scaling in concrete terms. At the most basic level, an $m \times n$ matrix describes a function that ingest an $n$-colum-component and spits out an $m$-colum-component by taking additions and scaling combinations of the input components.

<br>

**Formal definition and representation**

Be $\Set{F,+, \ ·}$ a field and $m,n \in \mathbb{N}$, then, we define a matrix $A$ as a function:

<br>

$$ A : [m] \times [n] \to  F$$

$$A(i,j) = a_{ij}$$

<br>

We say that $A$ is a matrix of $m \times n$ order. 

We denote the set of all matrix of order $m \times n$ over $F$ as $M_{m \times n}(F)$

In this terms, now the representation of the matrix we've seen above gets some sense:

<br>

$$A= \begin{bmatrix}A_{11} & \cdots & A_{1n}\\\vdots & \ddots & \vdots\\A_{m1} & \cdots & A_{mn}\end{bmatrix} = \begin{bmatrix}A(1,1) & \cdots & A(1,n)\\\vdots & \ddots & \vdots\\A(m,1) & \cdots & A(m,n)\end{bmatrix} = \begin{bmatrix} a_{11} & \cdots & a_{1n}\\\vdots & \ddots & \vdots\\ a_{m1} & \cdots & a_{mn}\end{bmatrix} = (a_{ij})_{i,j \in \mathbb{N}}$$

<br>

In the same way:

$$ X : [n] \times [1] \to  F$$

$$X(j) = x_{j}$$

<br>

$$X= \begin{bmatrix}X_{1} \\\vdots \\ \ X_{n} \end{bmatrix} = \begin{bmatrix}X(1) \\ \vdots\\ X(n) \end{bmatrix} = \begin{bmatrix} x_{1}\\\vdots \\ x_{n} \end{bmatrix} = (x_{j})_{j \in \mathbb{N}}$$

<br>

$$ A : [m] \times [1] \to  F$$

$$A(i) = a_{i}$$

$$Y= \begin{bmatrix}Y_{1} \\\vdots \\ \ Y_{m} \end{bmatrix} = \begin{bmatrix}Y(1) \\ \vdots\\ Y(m) \end{bmatrix} = \begin{bmatrix} y_{1}\\\vdots \\ y_{m} \end{bmatrix} = (y_{i})_{i \in \mathbb{N}}$$

<br>

### 3.2.2. Elementary operations.

#### 3.2.2.1. Direct operations.

For the time being, $AX = Y$ is nothing more than a shorthand notation for our system of linear equations. Later, when we have defined a multiplication for matrices, it will mean that $Y$ is the product of $A$ and $X$. 

We wish now to consider operations on the rows of the matrix $A$, which correspond to forming linear combinations of the equations in the system $AX = Y$. We restrict our attention to three elementary row operations on an $m \times n$ matrix $A$ over the field $F$. 


Conceptually these are the three “row moves” that change the representation of a matrix in a controlled way; formally they are functions $\mathcal{E}:M_{m \times n} \to M_{m \times n}$ 

- Multiplication of one row of $A$ by a non-zero scalar $\lambda$. 
- Replace row, $r$ by; $r + \lambda s$
- Swap row $r \leftrightarrow s$

For now on, consider:

- $F$ a field.
- The matrix: 
    $$A:=(a_{ij})_{i \in [m], j \in [n]} \in M_{m \times n}(F)$$
- Some index $r,s \in [m] : r \neq s$ 
- A scalar $\lambda \in F$.

<br>

**Scalar a row.**


We define the process of *scaling* row $r$ through $\lambda \neq 0$ to the definition of the function:

$$\mathcal{E}_{\lambda r}^r(A):=(e_{ij})_{i \in [m], j \in [n]} : e_{ij} := \begin{cases}  \lambda a_{ij} \ \ i = r \\ \   a_{ij} \ \ \ i \neq r\end{cases}$$

<br>

**Row replacement with a linear combination.**

We define the process of *replace* row $r$ with the linear combination $r + \lambda s$ to the definition of the function:

$$\mathcal{E}_{r + \lambda s}^r(A):=(e_{ij})_{i \in [m], j \in [n]} : e_{ij} := \begin{cases}  a_{ij} + \lambda a_{sj} \ \ i = r \\ \  \ \ \ \ \   a_{ij} \ \ \ \ \  \ \ \ i \neq r\end{cases}$$

<br>

**Swap rows.**

We define the process of *swap* the rows $r$ and $s$; $r \leftrightarrow s$ to the definition of the function:

$$\mathcal{E}_{r  \leftrightarrow s}(A):=(e_{ij})_{i \in [m], j \in [n]} : e_{ij} := \begin{cases}  a_{sj}  \ \ \ \ \ \ i = r \\  a_{rj}  \ \ \ \  \ \ i = s \\ a_{ij} \ \ i \notin \Set{r,s}\end{cases}$$

<br>

All this function $\mathcal{E}$ eventually relates $A$ with the matrices $E_{\lambda r}^r, E_{r + \lambda s}^r, E_{r  \leftrightarrow s}$

The definition of this matrices are coherent with the system $AX = Y$, in the sense that the operations preserve system equivalence after apply the same change to $Y$:

$$[AX = Y] \equiv [E_{\lambda r}^rAX = E_{\lambda r}^rY] \equiv [E_{r + \lambda s}^rAX = E_{r + \lambda s}^rY] \equiv [E_{r  \leftrightarrow s}AX = E_{r  \leftrightarrow s}Y]$$

This will make sense when we presentate the matricial product and check that the resulting system of equations is the result of apply a property that respects the equivalence as we saw at the start of this post.

<br>

#### 3.2.2.2. Inverse Operations.

Also observe that each function has a *reverse operation*. 

Let's take: $\mathcal{E}_{\lambda r}^r (·) : \lambda \neq 0$, observe that this function is *injective*. 

Reasoning to the opposite, consider matrix $A, B, C \in M\_{m \times n}(F): \mathcal{E}\_{\lambda r}^r(A) := \Set{(b\_{ij}), (c\_{ij})}$. Then is: 

$$b_{rj} = \lambda a_{rj} = c_{rj} \ \ \forall j \in [n] \implies B = C  \implies \forall A \ \  \exists! B : \mathcal{E}_{\lambda r}^r(A) := B$$

Let's also observe that, since the domain and the codomain coincides, then is also surjective and thus, bijective and we can consider the existance of an inverse; $\mathcal{E}^{-1}$ verifying: $\mathcal{E}^{-1} \circ \mathcal{E} = \mathcal{E} \circ \mathcal{E}^{-1} = I\_{M\_{m \times n} (F)}$

A very similar argument can be provided to $\mathcal{E}\_{r + \lambda s}^r$ and $\mathcal{E}\_{r  \leftrightarrow s}^r$, so lets now present the inverse of each function.

 - For $\mathcal{E}\_{\lambda r}^r$, the function defined as: $\mathcal{E}\_{\lambda^{-1} r}^r(A):=(e\_{ij})\_{i \in [m], j \in [n]} : e\_{ij} := \begin{cases}  \lambda^{-1} a\_{ij} \ \ i = r \\\\ \  \ a\_{ij}  \ \ \ \ \ i \neq r\end{cases}$, verifies:

    $$\mathcal{E}_{\lambda^{-1} r}^r(\mathcal{E}_{\lambda r}^r(A)) = A = \mathcal{E}_{\lambda r}^r(\mathcal{E}_{\lambda^{-1} r}^r(A))$$

    Considering only the operation over the row $r$, is $\lambda^{-1} \lambda a\_{rj} = \lambda \lambda^{-1}a\_{rj} = a\_{rj} \ \ \forall j \in [n]$

    <br>

- For, $\mathcal{E}\_{r + \lambda s}^r$, we can consider: $\mathcal{E}\_{r - \lambda s}^r(A):=(e\_{ij})\_{i \in [m], j \in [n]} : e\_{ij} := \begin{cases}  a\_{ij} - \lambda a\_{sj} \ \ i = r \\\\ \   \ \ \ \ \ a\_{ij}  \ \ \ \ \ \ \ \ \ i \neq r\end{cases}$, which verifies:

    $$\mathcal{E}_{r + \lambda s}^r(\mathcal{E}_{r - \lambda s}^r(A)) = A = \mathcal{E}_{r - \lambda s}^r(\mathcal{E}_{ r + \lambda s}^r(A))$$

    Again, considering only the row $r$; $(a\_{rj}  - \lambda a\_{sj}) + \lambda a\_{sj} = a\_{rj} = (a\_{rj}  + \lambda a\_{sj}) - \lambda a\_{sj}  \ \ \forall j \in [n]$

    <br>

- Lastly, obviously, for, $\mathcal{E}\_{r \leftrightarrow s}^r$, we can consider $\mathcal{E}\_{s \leftrightarrow r}^r$

    <br>

This basically means that any of the three operations are reversible. In other words, the inverse operation (function) of an elementary row operation exists and is an elementary row operation of the same type. 

<br>

### 3.2.3. Row-equivalence of Matrices and equivalence of system equations.

Being $A, B \in M_{m \times n} (F)$ then we say that $A$ and $B$ are *row-equivalent* if one can be obtained from the other through a finite composition of elementary row operations $\mathcal{E} : M\_{m \times n} \to M\_{m \times n}$ formally:

$$A \equiv_r B \iff \exists k \in  \mathbb{N} : \mathcal{E}_1 \cdots \circ \mathcal{E}_k(A) = B $$

Let's observe that the term "equivalence" in row-equivalence is specifically choosen because, if we consider again $A, A' \in M_{m \times n-1} (F)$ and $M, M'$ two equation systems such: $M := AX = Y \wedge M' := A'X = Y'$, then:

$$A \vert Y \equiv_r A'\vert Y' \iff M \equiv M'$$

(Notice that we are not considering inconsistent systems, meaning that $S_M \neq \varnothing$, in the sense that $M$ and $M'$ are not equivalent because they solution set is empty, there are a lot of equation system equivalents because they are incosistent and one cannot be obtained throught the other by elementary row operations)

We gonna see this equivalence choosen one elementary row operation but others admits a similar demonstration.

Where $A\vert Y \in M_{m \times n}(F)$ is the matrix resulting in adding to $A$ the colum $Y \in M_{m \times 1}(F)$. This is obviously because each elementary operation $\mathcal{E}$ can be identified with a change that presevers equivalence between linear systems presented above:

$$\begin{cases} \ \mathcal{E}^r_{\lambda r} & \simeq \big(P_r \in M \wedge \lambda \in F\setminus \Set{0} \implies S_{\lambda P_r} = S_{P_r} \big) \\ \ \mathcal{E}^r_{r+\lambda s} &\simeq \big(P_r,P_s \in M \wedge \lambda \in F \setminus \Set{0} \implies S_{P_r + \lambda P_s} \cap S_{P_s} = S_{P_r} \cap S_{P_s}) \\ \ \mathcal{E}^r_{r \leftrightarrow s} &\simeq \big(P_r,P_s \in M \implies S_{P_r}\cap S_{P_s} = S_{P_s} \cap S_{P_r})\end{cases}$$

<br>

- $\Rightarrow$ 
    
    Consider $M:= \displaystyle\bigwedge_i P_i \equiv [AX = Y]$, then, we form the system $M':=P_{\lambda r} \wedge \displaystyle\bigwedge_{i \neq r}P_i \equiv [A'X = Y']$, until this point we do know that $M \equiv M'$, let's see that $[A \vert Y] \equiv_r [A' \vert Y']$.

    If: 

    $$M := \begin{cases} \ a_{11}x_{1} \cdots + a_{1n}x_{n} = y_1 \\   \ \ \ \ \vdots \\\ a_{r1}x_{1} \cdots + a_{rn}x_{n} = y_r \ \ \ \\ \ \ \  \  \vdots \\ \ a_{m1}x_1 \cdots + a_{mn}x_{n} = y_m\end{cases} \equiv \begin{bmatrix} a_{11} & \cdots & a_{1n}\\ \vdots \\ a_{r1} & \cdots & a_{rn} \\ \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix} \begin{bmatrix} x_{1}\\\vdots \\ x_{n} \end{bmatrix} = \begin{bmatrix} y_{1}\\\vdots \\ y_r \\ \vdots \\ y_{m} \end{bmatrix}$$

    $$M' := \begin{cases} \ a_{11}x_{1} \cdots + a_{1n}x_{n} = y_1 \\   \ \ \ \ \vdots \\\ \lambda a_{r1}x_{1} \cdots + \lambda a_{rn}x_{n} = \lambda y_r \ \ \ \\ \ \ \  \  \vdots \\ \ a_{m1}x_1 \cdots + a_{mn}x_{n} = y_m\end{cases} \equiv \begin{bmatrix} a_{11} & \cdots & a_{1n}\\ \vdots \\ \lambda a_{r1} & \cdots & \lambda a_{rn} \\ \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix} \begin{bmatrix} x_{1}\\\vdots \\ x_{n} \end{bmatrix} = \begin{bmatrix} y_{1}\\\vdots \\ \lambda y_r \\ \vdots \\ y_{m} \end{bmatrix}$$

    And thus:

    $$ [A \vert Y] := \begin{bmatrix} a_{11} & \cdots & a_{1n} \ \ \ y_1\\ \vdots \\ a_{r1} & \cdots & a_{rn} \ \ \ y_r \\ \vdots \\ a_{m1} & \cdots & a_{mn} \ \ \ y_m \end{bmatrix} \ \ \ \  [A \vert Y] := \begin{bmatrix} a_{11} & \cdots & a_{1n} \ \ \ y_1\\ \vdots \\ \lambda a_{r1} & \cdots & \lambda a_{rn} \ \ \ \lambda y_r \\ \vdots \\ a_{m1} & \cdots & a_{mn} \ \ \ y_m \end{bmatrix}$$

    <br>

    And obviously $\mathcal{E}^r_{\lambda r} ([A \vert Y]) = [A' \vert Y'] \implies [A \vert Y] \equiv_r [A' \vert Y']$.

    <br>

- $\Leftarrow$ 

    Observe that this relationship is reciproc, in the sense that from: 

    $$[A \vert Y] , [A' \vert Y'] \in M_{m \times n}(F) : \mathcal{E}^r_{\lambda r} ([A \vert Y]) = [A' \vert Y']$$

    we can craft the systems $[AX = Y]:=\bigwedge P\_i$ and  $[A'X=Y'] :=\bigwedge P'\_i$ and is $P\_i = P'\_i \ \ i \neq r \wedge P\_r = \lambda P\_r$ and, as we see above, is $S\_P = S\_{\lambda P} \implies [AX = Y] \equiv [A'X = Y']$

    Meaning that from *row-equivalent* matrices we can derivate equivalent equation systems and from equivalent (non-inconsistent) equation systems we can derivate row-equivalent matrix. 

    <br>

**Row-equivalent class**

The relation $\equiv_r$ on $M_{m \times n}(F)$ is an equivalence relation (reflexivity, symmetry, and transitivity follow from the identity operation, the existence of inverse operations, and composition of elementary operations respectively). 

Each equivalence class:

$$[A]_r := \Set{B \in M_{m \times n}(F) \mid B \equiv_r A}$$

collects all matrices that encode the same linear constraints on $F^n$, in the sense that if $A \equiv_r B$ then the systems $AX = Y$ and $BX = Y'$ (where $Y'$ is obtained by applying the same sequence of elementary operations to $Y$) share the same solution set $S$. The row-reduced echelon form serves as the canonical representative of each class: every matrix in $[A]_r$ reduces to the same RREF, providing a computable invariant that decides membership in the class. We will introduce this concept in the next section.

<br>

# 4. Row-reduced forms.

## 4.1. Row-reduced.

### 4.1.1. Definition.

At this point, we already know that being $A \in M_{m \times n}(F)$, then any elementary row-operation applied to $A$ do not change the solution set of the system $AX = Y$. 

Thus, we can think in the simplier form of $A$ through elementary row operations, this is what get called as *reduced row echelon form* (RREF) $R \equiv_r A$, and can be conceptualized as the matricial representiation of a certain amount of information using a minimal cuantity of resources.

First, let's see the simple *row-reduced* concept

A matrix $R \in M_{m \times n}(F)$ is in reduced row echelon form if:

- the first non-zero entry in each non-zero is equal to 1, 

- the leading 1 is the only nonzero entry in that column (zeros above and below it).

<br>

An example of a row-reduced form is for example:

$$\begin{bmatrix}
2 & -1 & 3 & 2\\
1 & 4 & 0 & -1\\
2 & 6 & -1 & 5
\end{bmatrix} \equiv_r
\left[
\begin{array}{cccc}
0 & 0 & 1 & -\frac{11}{3}\\
1 & 0 & 0 & \frac{17}{3}\\
0 & 1 & 0 & -\frac{5}{3}
\end{array}
\right]$$

This would mean that the equation systems 

$$M:= \begin{cases}
2x_1 - x_2 + 3x_3 = 2,\\
x_1 + 4x_2 + 0x_3 = -1,\\
2x_1 + 6x_2 - x_3 = 5.
\end{cases}, \quad \quad M':=\begin{cases}
0x_1 + 0x_2 + x_3 = -\dfrac{11}{3},\\
x_1 + 0x_2 + 0x_3 = \dfrac{17}{3},\\
0x_1 + x_2 + 0x_3 = -\dfrac{5}{3}.
\end{cases}$$

Are equivalents, being $M'$ trivial. 

Observe that is easy to see that any matrix $A \in M_{m \times n}(F)$ is row-equivalent to a row-reduced matrix.

<br>

### 4.1.2. Row-reduced exercises.

1. **Find all solutions to the system of equations:**

    $$\begin{cases}
    (1-i)x_{1}-ix_{2}=0,\\
    2x_{1}+(1-i)x_{2}=0.
    \end{cases}$$

    $$A = \begin{bmatrix} 1-i & -i \\ 2 & 1-i \end{bmatrix}$$

    Observe that making: $r_2 := r_2 - (1+i)\,r_1$ we obtain:

    $$(1+i)\,r_1 = \bigl((1+i)(1-i),\; (1+i)(-i)\bigr) = (2,\; 1-i)$$

    $$\begin{bmatrix} 1-i & -i \\ 2-2 & (1-i)-(1-i) \end{bmatrix} = \begin{bmatrix} 1-i & -i \\ 0 & 0 \end{bmatrix}$$

    Meaning basically that this is a redundant system of two equations whose simplified from is:

    -  $r_1 := \dfrac{1}{1-i}\,r_1 = \dfrac{1+i}{2}\,r_1$

    $$\dfrac{1+i}{2}\,r_1 = \left(\dfrac{(1+i)(1-i)}{2},\; \dfrac{(1+i)(-i)}{2}\right) = \left(1,\; \dfrac{1-i}{2}\right)$$

    $$\begin{bmatrix} 1 & \dfrac{1-i}{2} \\ 0 & 0 \end{bmatrix}$$

    <br>

    $$S = \left\{\, t\left(-\dfrac{1-i}{2},\; 1\right) \;\mid\; t \in \mathbb{C} \,\right\}$$

    <br>

2. **Giving $A$ as**:

    $$A= \begin{bmatrix}
    3 & -1 & 2\\
    2 & 1 & 1\\
    1 & -3 & 0
    \end{bmatrix}$$

    **Find all the solutions for $AX = 0$.**
    
    
    We do know that any row-equivalent matrix to A share the solution set for the equation system, so lets produce the row-reduce form of $A$ which is identity $I_3$ and thus the equation system $AX=0$ is trivial; $x=y=z=0$

    <br>

3. **Giving**:

    $$A=
    \begin{bmatrix}
    6 & -4 & 0\\
    4 & -2 & 0\\
    -1 & 0 & 3
    \end{bmatrix}$$

    **over the field $F$, then, solve $AX=2X$ and $AX=3X$ (Assuming that if $c \in F$, then $cX$ is scale every row of $X$ by the scalar $c$)**

    For $AX=2X$ we have the system equation: 

    $$\begin{cases}
    6x - 4y + 0z = 2x \\
    4x - 2y + 0z = 2y\\
    -1x + 0y + 3z = 2z
    \end{cases} \quad \equiv \quad \begin{cases}
                        4x - 4y = 0 \\
                        4x - 4y = 0 \\
                        -x + z = 0
                        \end{cases} \quad \equiv \quad \begin{cases}
                                            x - y = 0 \\
                                            z - x = 0
                                            \end{cases}$$

    Calling $x = \lambda \in F$, then the solution system is $\Set{(\lambda, \lambda, \lambda) \ \vert \ \lambda \in F}$

    <br>

    On the other hand we take: $AX = 3X$:

    $$\begin{cases}
    6x - 4y + 0z &= 3x \\
    4x - 2y + 0z &= 3y\\
    -1x + 0y + 3z &= 3z
    \end{cases} \quad \equiv \quad \begin{cases}
                        3x - 4y & = 0 \\
                        4x - 5y & = 0 \\
                             -x & = 0
                        \end{cases} \quad \equiv \quad \begin{cases}
                                                        y = 0 \\
                                                        x = 0
                                                        \end{cases}$$

    And the solution set is: $\Set{(0,0,\lambda) \ \vert \ \lambda \in F }$

    <br>

4. **Find a row-reduced matrix row-equivalent to:**

    $$A=\begin{bmatrix}
        i & -(1+i) & 0\\
        1 & -2 & 1\\
        1 & 2i & -1
        \end{bmatrix}$$

    **Defined over the field $\mathbb{C}$**

    Let's check that performing elemantal row operations over $A$ we eventually reach:

    $$A=\begin{bmatrix}
    1 & \frac{-(1+i)}{i} & 0\\
    0 & 1 & \frac{1}{-2+\frac{(1+i)}{i}}\\
    0 & 0 & -\frac{1}{2i + \frac{1+i}{i}} - \frac{1}{-2 + \frac{1+i}{í}}
    \end{bmatrix}$$

    In this context, we could think in the error of trivially simplify:

    $$A=\begin{bmatrix}
    1 & \frac{-(1+i)}{i} & 0\\
    0 & 1 & \frac{1}{-2+\frac{(1+i)}{i}}\\
    0 & 0 & -\frac{1}{2i + \frac{1+i}{i}} - \frac{1}{-2 + \frac{1+i}{í}}
    \end{bmatrix} \quad \equiv_r \quad \begin{bmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & -\frac{1}{2i + \frac{1+i}{i}} - \frac{1}{-2 + \frac{1+i}{í}}
    \end{bmatrix}$$

    But this is not correct since the expression $-\frac{1}{2i + \frac{1+i}{i}} - \frac{1}{-2 + \frac{1+i}{í}} = 0$ ($\frac{1+i}{i}=1-i$) so we can't use it to perform the row operation that makes $a_{23} = 0$ and this we cannot use $r_2$ to make $a_{12}=0$. This is a friendly reminder to remember that $\mathbb{C}$ is not a trivial extension of $\mathbb{R}$ and your visual intuition can betray you when decide if some complex expresion do not collapse to 0. 

    As a practice rule, every time simplifie some expression to be sure is not equal to 0.

    <br>

5. **Prove that the follopwing two matrices are not row-equivalent**:

    $$A:= \begin{bmatrix}
    2 & 0 & 0\\
    a & -1 & 0\\
    b & c & 3
    \end{bmatrix}
    \qquad
    B:= \begin{bmatrix}
    1 & 1 & 2\\
    -2 & 0 & -1\\
    1 & 3 & 5
    \end{bmatrix}$$

    Let's observe that $A \equiv_r B \implies M:= [AX = 0] \equiv M':= [BX = 0]$. However, solving $M$ and $M'$ we see that they don't share the same solution set, $S_M := \Set{(0,0,0)}$ and $S_{M'}:= \Set{(-\frac{1}{2}\lambda, - \frac{3}{2}\lambda, \lambda) : \lambda \in F}$

    <br>

6. **Let $A \in M_2(\mathbb{C}): A:=\begin{bmatrix} a & b \\ c & d\end{bmatrix} : \sum a_{ij} = 0 \wedge A \text{ is row-reduced}$. Prove that there are only three such matrices.**

    Let's remember what a row-reduced form is. A row-reduced form is a matrix verifying:

    - The first non-zero entry in each non-zero row is $1$ (pivot).
    - Each column which contains the leading non-zero entry of some row has all its other entries. 

    This imposes a finite forms for $A$. We could think of $A$ as a row-reduced form as a combination of two rows that verifies some conditions; 
    
    $$A:= \begin{cases} r_1:=(a,b) \\ r_2:=(c,d)\end{cases}$$

    In this sense, we can giving values to $a,b,c,d$ and aplying restrictions of the row-reduced form and the premise $\sum a_{ij} = 0$ giving at the end:

    $$\begin{bmatrix} 1 & -1 \\ 0 & 0  \end{bmatrix},  \begin{bmatrix} 0 & 0 \\ 1 & -1 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$

    The rest of forms do not verifies the condition.

    <br>

7. **Prove that the interchange of two rows of a matrix can be accomplished by a
finite sequence of elementary row operations of the other two types.** 

    Let's consider $F$ a field and $A \in M_{m \times n}(F)$ and $r_i, r_j$ two rows of $A$. Then we can operate using the follwing elementary row-operations:

    - $r'_j \to r_j + r_i$
    - $r'_i \to r_i - r'_j$ and then $r''_i \to -r'_i$ resulting efectively in $r''_i = r_j$ 
    - Lastly; $r''_j \to r'_j - r''_i$ resulting in $r''_j = r_i$

    Having ultimately doing $r_i \leftrightarrow r_j$ in $A$ by elementary row-operations different than ordinal swapping. 

    <br>

8. **Consider the system of equations $AX=0$, where**:
    
    $$A \in M_2(F) : A :=\begin{bmatrix} a & b \\ c & d\end{bmatrix}$$

    **Prove the following, being $M:= [AX=0]$, then**:

    - **If** $a_{ij} = 0 \ \ \forall i \forall j \implies   S_M := \Set{(\alpha, \beta) : \alpha, \beta \in F}$

        Let's check quickly that the result is trivial, if al entries are 0, the unique constraing formulated by the system equation $AX=0$ is $0x + 0y = 0$ which is satisfied by any pair $(x,y) \in F^2$

        <br>
    
    - **If** $ad - bc \neq 0 \implies S_M:= \Set{(0, 0)}$

        First let's consider that $a \neq 0$ then, we can reduce:


        $$A :=\begin{bmatrix} a & b \\ c & d\end{bmatrix} \equiv_r \begin{bmatrix} 1 & \frac{b}{a} \\ c & d\end{bmatrix} \equiv_r \begin{bmatrix} 1 & \frac{b}{a} \\ 0 & d - \frac{b}{a} c\end{bmatrix}$$

        Then, $d - \frac{b}{a}c = 0 \ \underbrace{\iff}_{a \neq 0} \ ad - bc = 0$ and let's observe that if $d - \frac{b}{a}c \neq 0$ then the system only accepts the trivial solution $(0,0)$ and if it is 0, the system accepts any solution in $(\lambda, \frac{a}{b} - \lambda)$.

        If $a = 0$ then we can swap rows and we only care about the predicate $b = 0 \vee c = 0$ or not. If not, then observe that $\cancel{ad} -bc = -bc \neq 0$ and the equation system only admits $(0,0)$ as a solution. 

        If the predicate is true, then, first $ad -bc = 0$, and the solution set decays over one of the two forms: $S_M := \Set{(\lambda,0): \lambda \in F}$ o $S_M := \Set{(0,\lambda) : \lambda \in F}$

        In last instance, we can see that $ad - bc \neq 0$ implies $S_M := \Set{(0,0)}$.

        <br>

## 4.2. Row-reduced echelon.

### 4.2.1. Definition.

Let's observe that, meanwhile then *row-reduced* form do maximazes the simplification of the information relative to the system of equations asociated with the equivalent class of those row-equivalent matrix to the mentioned reduced forms.

For example, the exercise $6$ shows: 

$$\begin{bmatrix} 1 & -1 \\ 0 & 0  \end{bmatrix} \quad \quad  \begin{bmatrix} 0 & 0 \\ 1 & -1 \end{bmatrix}$$

Which are two row-reduced forms row-equivalent matrix, thus both are in the same equivalent class and the linear system that represent is the same.

Thus, we introduce a canonical row-reduced representation, is the representant of the equivalent class for any matrix row-equivalent between them. This matrix $R$ satisfies:

1. $R$ is row-reduced.
2. Every row of $R$ with all $0$ entries, is below any row with a non-zero entry.
3. If $1,...,r$ are the non-zero rows of $R$ then, and the first non-zero entry is in the colum $k_i  : i=1,...,r$, then $k_1 < \cdots < k_r$.

As an example of row-reduced echelon matrix:

$$\begin{bmatrix}
0 & 1 & -3 & 0 & \frac{1}{2} \\
0 & 0 & 0 & 1 & 2 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}$$

Let's observe that any row-reduced form is row-equivalent to a RREM through a finite amount of swaps.

<br>

### 4.2.2. Properties.

-  **If $A$ is an $m \times n$ matrix and $m < n$, then the homogeneous system of linear equations $AX = 0$ has a non-trivial solution.** 

    Observe that $A$ is row-equivalent to a RREM $R$, with a number $r \leq m$ of non-zero rows, by the shape of the matrix $R$ is $RX=0$ have non-trivial solution and by the fact that both matrix are row-equivalent, both system verifies: $[AX=0] \equiv [RX=0]$

    <br>

- **$A \in M_{n}(F)$ then $A \equiv_r I_n \iff S_{[AX=0]} := \Set{0 \in F^n}$**

    - $\Rightarrow$ Let's observe that $I_n$ is a RREM, and accept only the trivial solution.
    - $\Leftarrow$ Also $I_nX=0$ accepts only the trivial solution and any system $M$ given by a matrix row-equivalent to $I_n$ share the same solution.

<br>

## 4.3. Augmented Matrix.

### 4.3.1. Definition.

Until now, we've discussed homogeneous systems, equation systems of the form $AX=0$. Let us now ask what elementary row operations do toward solving a system of linear equations $AX = Y: A \in M_{m \times n}(F)$. We already discuss the method but we didn't give it a name, which is form the *augmented matrix*; adding to the matrix of coefficients $A$ the colum of constants $Y$: 

<br>

$$A' = [A | Y] \in M_{m \times n+1}(F): (a'_{ij}):= \begin{cases} a_{ij} \ \ j \leq n \\ y_{ij} \ \  j = n + 1\end{cases}$$

<br>

For this matrix the same properties that we discussed before also applies, in the sense that, suppose we perform a sequence of elementary row operations on $A$, arriving at a row-reduced echelon matrix $R$. If we perform this same sequence of row operations on the augmented matrix A’, we will arrive at a matrix $R’$ whose first $n$ columns are the columns of $R$ and whose last column contains certain scalars $z_1, . . . , z_m$, which results from applying the sequence of row operations to the matrix $Y$. 

<br>

$$R' = [R | Z] : Z = \begin{bmatrix} z_1 \\ \vdots \\ z_m \end{bmatrix}$$

<br>

Let's observe that $[AX = Y] \equiv [RX=Z]$ since both system are row-equivalent so they share their solution set. 

This essentially means that the same rule that we use to simplify the information on an homogeneous system also serves to simplify non-homogeneous systems.

<br>

### 4.3.2. RREM and Augmented matrix exercises.


1. **Find all solutions to the following system of equations by row-reducing the coefficient matrix:**

    $$\begin{cases}
    \frac{1}{3}x_1 + 2x_2 - 6x_3 = 0,\\
    -4x_1 + 5x_3 = 0,\\
    -3x_1 + 6x_2 - 13x_3 = 0,\\
    -\frac{7}{3}x_1 + 2x_2 - \frac{8}{3}x_3 = 0.
    \end{cases}$$

    <br>


    $$A = \begin{pmatrix} \frac{1}{3} & 2 & -6 \\ -4 & 0 & 5 \\ -3 & 6 & -13 \\ -\frac{7}{3} & 2 & -\frac{8}{3} \end{pmatrix} R_1 \leftarrow 3R_1 \begin{pmatrix} 1 & 6 & -18 \\ -4 & 0 & 5 \\ -3 & 6 & -13 \\ -\frac{7}{3} & 2 & -\frac{8}{3} \end{pmatrix} \begin{cases}R_2 \leftarrow R_2 + 4R_1 \\ R_3 \leftarrow R_3 + 3R_1 \\ R_4 \leftarrow R_4 + \tfrac{7}{3}R_1 \end{cases} \begin{pmatrix} 1 & 6 & -18 \\ 0 & 24 & -67 \\ 0 & 24 & -67 \\ 0 & 16 & -\frac{134}{3} \end{pmatrix}$$

    $$\begin{cases}R_3 \leftarrow R_3 - R_2, \\ R_4 \leftarrow R_4 - \tfrac{2}{3}R_2 \end{cases} \begin{pmatrix} 1 & 6 & -18 \\ 0 & 24 & -67 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} R_2 \leftarrow \tfrac{1}{24}R_2 \begin{pmatrix} 1 & 6 & -18 \\ 0 & 1 & -\frac{67}{24} \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} R_1 \leftarrow R_1 - 6R_2 \begin{pmatrix} 1 & 0 & -\frac{5}{4} \\ 0 & 1 & -\frac{67}{24} \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$


    Thus, the solution of the system is the same for the equation system:

    $$\begin{cases} x - \frac{5}{4}z = 0 \\ y - \frac{67}{24}z = 0 \end{cases} \implies \left(\frac{5 \lambda}{4}, \frac{67 \lambda}{24} , \lambda \right)$$

<br>

2. **Find a row-reduced echelon matrix which is row-equivalent to**

    $$A=
    \begin{bmatrix}
    1 & -i\\
    2 & 2\\
    i & 1+i
    \end{bmatrix}.
    $$

    Row-reducin the matrix we get:

    $$\begin{bmatrix}1 & 0\\0 & 1\\0 & 0\end{bmatrix}$$

    Thus, the system $AX=0$ only accepts $(0,0)$ as a solution.

    <br>

3. **Describe explicitly all $2 \times 2$ row-reduced echelon matrices.**

    So, let's check what are the condition of the RREM matrix:

    1. $R$ is row-reduced.
    2. Every row of $R$ with all $0$ entries, is below any row with a non-zero entry.
    3. If $1,...,r$ are the non-zero rows of $R$ then, and the first non-zero entry is in the colum $k_i  : i=1,...,r$, then $k_1 < \cdots < k_r$.

    So let's start by retriving those $M_2(F) : M \text{ is row-reduced}$. A matrix is row-reduced if he first non-zero entry in each non-zero is equal to 1 and if the leading 1 is the only nonzero entry in that column (zeros above and below it).

    $$\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}, \begin{bmatrix}1 & 0\\0 & 0\end{bmatrix}, \begin{bmatrix}0 & 1\\0 & 0\end{bmatrix}, \begin{bmatrix}0 & 0\\1 & 0\end{bmatrix}, \begin{bmatrix}0 & 0\\0 & 1\end{bmatrix} $$

    $$\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}, \begin{bmatrix}1 & \alpha\\0 & 0\end{bmatrix}, \begin{bmatrix}0 & 0 \\1 & \alpha\end{bmatrix}$$

    Now, we apply the second condition, and we only get the following matrix eliminating those that have any 0-row above:

    $$\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}, \begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}, \begin{bmatrix}1 & 0\\0 & 0\end{bmatrix}, \begin{bmatrix}0 & 1\\0 & 0\end{bmatrix}, \begin{bmatrix}1 & \alpha\\0 & 0\end{bmatrix}$$

    Lastly, we eliminate the last matrix applying the last condition:

    $$\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}, \begin{bmatrix}1 & 0\\0 & 0\end{bmatrix}, \begin{bmatrix}0 & 1\\0 & 0\end{bmatrix}, \begin{bmatrix}1 & \alpha\\0 & 0\end{bmatrix}: \alpha \in F \setminus \Set{0}$$

    <br>

4. **Consider the system of equations.**

    $$\begin{cases}
    x_1 - x_2 + 2x_3 = 1,\\
    2x_1 + 2x_3 = 1,\\
    x_1 - 3x_2 + 4x_3 = 2.
    \end{cases}$$

    **Does this system have a solution? If so, describe explicitly all solutions.** 

    Row-reducing we get: 

    $$\begin{bmatrix}
    1 & 0 & 1 & \frac{1}{2} \\
    0 & 1 & -1 & -\frac{1}{2} \\
    0 & 0 & 0 & 0
    \end{bmatrix}$$

    So the solution set is: $\left(\frac{1}{2}-\alpha, -\frac{1}{2}+\alpha, \alpha\right), \quad \alpha \in F$

    <br>

5. **Give an example of a system of two linear equations in two unknowns which has no solution.**

    $$\begin{cases} x + y = 0 \\ x + y = 1 \end{cases}$$

    Observe that this are two lines that do not intersect in any point, so there is no solution.

    <br>

8. **Let be**

    $$A =
    \begin{bmatrix}
    3 & -1 & 2 \\
    2 & 1 & 1 \\
    1 & -3 & 0
    \end{bmatrix}$$

    **For which triples $(y_1,y_2,y_3)$ does the system $AX = Y$ have a solution**

    Let's take the augmented matrix $[A\vert Y]$ and get the row-reduced echelon matrix of the system reaching:

    $$\begin{bmatrix}
    1 & -3 & 0 \\
    0 & 7 & 1 \\
    0 & 0 & \frac{6}{7}
    \end{bmatrix}$$

    Thus, the system has solution and no constraing at all for the 3-tuple.

    <br>

9. **Let be**

    $$A =
    \begin{bmatrix}
    3 & -6 & 2 & -1\\
    -2 & 4 & 1 & 3\\
    0 & 0 & 1 & 1\\
    1 & -2 & 1 & 0
    \end{bmatrix} \in M_{4 \times 4} (\mathbb{Q})$$

    **For which $(y_1, y_2, y_3, y_4)$ does the system of equations $AX = Y$ have a solution?**

    Considering the system $AX=Y$ we row-reduce the augmented matrix $[A \vert Y] \to [R \vert Y']$ knowing that $[AX=Y] \equiv_r [RX=Y']$ reaching

    $$\left[\begin{array}{cccc|c}
    1 & -2 & 0 & -1 & \frac{-y_2 + y_4}{3} \\
    0 & 0 & 1 & 1 & \frac{y_2 + 2y_4}{3} \\
    0 & 0 & 0 & 0 & \frac{3y_3 - y_2 - 2y_4}{3} \\
    0 & 0 & 0 & 0 & \frac{3y_1 + y_2 - 7y_4}{3}
    \end{array}
    \right]$$

    Thus, the system have solution when $(y_1,y_2,y_3,y_4) \in \mathbb{Q}^4$ satisfies:

    $$\begin{cases} \displaystyle\frac{3y_3 - y_2 - 2y_4}{3} = 0 \\  \\\displaystyle\frac{3y_1 + y_2 - 7y_4}{3} = 0 \end{cases}$$

    Otherwise the system would be inconsistent.


    Then, calling $y_2 := \alpha, y_4 := \beta$, then the system has solution for every 4_tuple of the form: 

    $$(\frac{7\beta - \alpha}{3}, \alpha, \frac{2\beta + \alpha}{3}, \beta) \in \mathbb{Q}^4$$

    <br>

8. **Suppose $R$ and $R’$ are $2 \times 3$ row-reduced echelon matrices and that the systems $RX = 0$ and $R’X = 0$ have exactly the same solutions. Prove that $R = R’$.**
    
    Firs't let observe that both have her equivalent class of row-reduced matrix of the form:

    $$[R]_r := \Set{B \in M_{2 \times 3}(F) \mid B \equiv_r R}$$
    
    $$[R']_r := \Set{B \in M_{2 \times 3}(F) \mid B \equiv_r R'}$$

    Also, $[RX = 0] \equiv_r [R'X=0] \implies R \equiv_r R'$,
    
    
    (Observe that this is not a demonstration and we will not cover here this part since that's computational job; we omit the case-by-case verification that distinct 2×3 RREFs yield distinct solution sets, as this follows from direct inspection of the finitely many possible forms enumerated in Exercise 3) 
    
    Note that there are a finite set of RREM matrix of $2 \times 3$ dimensions a few checks can constantate that only equivalents non-inconsistent systems with the same matrix $R$ have equivalents solutions. Meaning that each $RREM$ codifies the information of a linear system in a unique minimal way, any change of the matrix leads to the edition of some valuable information that also change the system.
    
    But the result is stronguer than that, $ R \equiv_r R' \implies R \in [R']_r \wedge R' \in [R]_r$ which means that $[R]_r = [R']_r$. Lastly, since both are $RREM$ and this is the unique representant of the equivalent class it must be: $R = R'$.

    <br>


    <br>

# 5. Matrix Multiplication.

## 5.1. Definition.

Before, when introducing the matrix concept we assume that a matrix is a device to package linear information. Elementary row operations preserve equivalence between lienar systems allowing to simplify the matrix shape while the information within remains untouch.

Lastly, we have to unravel what the $AX = Y$ notation means; what means for $Y$ to be the product of $AX$. Well, we can already tell that due to the shorthand notation nature, $Y$ is the lineal combination of the data given by $A$ and $X$ exactly as the lineal equation system was:

$$\begin{cases} a_{11}x_{1} \cdots + a_{1n}x_{n} = y_1 \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n} = y_m\end{cases} \iff Y := \begin{pmatrix} y_1 \\ \vdots \\ y_m\end{pmatrix} = \begin{pmatrix} a_{11}x_{1} \cdots + a_{1n}x_{n} \\  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n}\end{pmatrix} = AX$$

This give us a first approach about what the product is and what are his elements; $AX$ denotes a row of lineal combinations on the elements of $X$ by the items of $A$. 

From this approach, we can extend the operation to any two matrix $A \in M_{m \times p}(F)$, $B \in M_{p \times n}(F)$. Let's break down $B$ as an ordered set of columns $\beta_i \in M_{p \times 1} (F): i \in [n]$, then the product stands as:

$$AB = (A \beta_1, ..., A \beta_n) \in M_{m \times n} (F)$$

Where $A \beta_i \in M_{m \times 1} (F) : i=1,...,n$. **This is that $AB$ denotes the lineal combinations on the elements of the columns $\beta_i \subset B$ by the elements of $A$.**

Let's observe that the number of rows of $A$ and the number of columns of $B$ must match.

Each entry can have a singular definition as:

$$(ab_{ij})_{i \in [m], j \in [n]} := \sum_{k = 1}^p a_{ik}b_{kj} $$

<br>

It is important to observe that the product of two matrices need not be defined; the product is defined if and only if the number of columns in the first matrix coincides with the number of rows in the second matrix. Frequently we shall write products such as AB without explicitly mentioning the sizes of the factors and in such cases it will be understood that the product is defined. From (d), (e), (f), (g) we find that even when the products AB and BA.

<br>

## 5.2 Properties.

Let's see that the products of matrix satisfies the following properties:

<br>

### 5.2.1. Associativity.

Observe that, for each entry is:

$$[a(bc)]_{ij}
= \sum_{r} a_{ir}(bc)_{rj}
= \sum_{r} a_{ir} \sum_{s} b_{rs}c_{sj}
= \sum_{r} \sum_{s} a_{ir} b_{rs} c_{sj}=$$

$$= \sum_{s} \left( \sum_{r} a_{ir} b_{rs} \right) c_{sj}
= \sum_{s} (ab)_{is} c_{sj}
= [(ab)c]_{ij}$$

Thus is: $A(BC) = (AB)C$

Observe that, going back to the matrix product definition, the associativity property essentially tells us that linear combinations of linear combinations of $C$ ($A(BC)$) are, ultimately, lineal combinations of $C$ $(AB)C$.

<br>

### 5.2.2. Power of Matrix.

When $A$ is an $n \times n$ (square) matrix, the product $AA$ is defined. We shall denote this matrix by $A^2$. 

Observe that by the associativity (AA)A = A(AA) or $A^2A = AA^2$, so that the product $AAA$ is unambiguously defined. This product we denote by A3. 

In general, the product $AA \ldots A$ ($k$ times) is
unambiguously defined, and we shall denote this product by $A^k$. 

<br>

## 5.3. Elementary Matrix and Elementary Row Operations abstraction.

Now that we've introduced the matrix product and its properties we gonna see that every set of elementary row operations over a matrix $A \in M_{m \times n} (F)$ can be abstracted in a matrix product $EA$ where the matrix $E \in M_{m \times m}(F)$ is a matrix obtained by aplicating elementary row operations to the identity, what we call an elementary matrix.

The logic behind is simple, the identity matrix $I$ behaves as a identity , in the sense that if $A$ and $I$ and two matrix such their product is correctly defined, then $IA = A$. Then, applying to $I$ elementary operations forming $E$ and performing the product $EA$ applies the elementary row operation to $A$.

<br>

### 5.3.1. Identity Matrix.

We define the identity matrix $I_n \in M_{n} (F)$ as:

$$I_n :=  (\delta_{ij})_{i,j \in [n]} \ \vert \ \delta_{ij} :=\begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}$$

As the codification, the identity matrix would be:

$$I_n := \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \in F^{n \times n}$$

Let's now check carefully its behaviour. Considering $I_n$ and $A \in F^{n \times m}$, then the product $IA$ as we defined above would be:

$$IA = (I\alpha_1,\ldots,I\alpha_m) \ \vert \ I\alpha_t := \begin{pmatrix} \displaystyle\sum_{i=1}^n\delta_{1i}a_{it} \\  \vdots \\ \displaystyle\sum_{i=1}^n\delta_{ni}a_{it}\end{pmatrix} $$

Let's observe that by the definition of $I_n$, each item of $I \alpha_t$ is: $\displaystyle\sum_{i=1}^n\delta_{ji}a_{it} = \delta_{jj}a_{jt} = a_{jt} : j \in [n]$, thus:

$$I\alpha_t := \begin{pmatrix} \displaystyle\sum_{i=1}^n\delta_{1i}a_{it} \\  \vdots \\ \displaystyle\sum_{i=1}^n\delta_{ni}a_{it}\end{pmatrix} = \begin{pmatrix} \cancel{\delta_{11}}a_{1t} \\  \vdots \\ \cancel{\delta_{nn}}a_{nt}\end{pmatrix} = \alpha_t$$

And in summary: $IA = (I\alpha_1,\cdots,I\alpha_m) = (\alpha_1,\cdots,\alpha_m) = A$

<br>

The proof that $AI_m = A$  for $A \in F^{n \times m}$ is analogous and omitted here.

<br>

### 5.3.2. Elementary Matrix.

Now, let's introduce what an elementary matrix is.

An $E \in F^{n \times n}$ matrix is said to be an elementary matrix if it can be obtained from the $I_n$ identity matrix by means of a single elementary row operation.

Formally, elementary row operations are $\mathcal{E}:M_{m \times n} \to M_{m \times n}$ functions of the following type:

<br>

- $\mathcal{E}\_{\lambda r}^r(A):=(e\_{ij})\_{i \in [m], j \in [n]} : e\_{ij} := \begin{cases}  \lambda a\_{ij} \ \ i = r \\ \   a\_{ij} \ \ \ i \neq r\end{cases} : \lambda \neq 0$

- $\mathcal{E}\_{r + \lambda s}^r(A):=(e\_{ij})\_{i \in [m], j \in [n]} : e\_{ij} := \begin{cases}  a\_{ij} + \lambda a\_{sj} \ \ i = r \\ \  \ \ \ \ \   a\_{ij} \ \ \ \ \  \ \ \ i \neq r\end{cases}$

- $\mathcal{E}\_{r  \leftrightarrow s}(A):=(e\_{ij})\_{i \in [m], j \in [n]} : e\_{ij} := \begin{cases}  a\_{sj}  \ \ \ \ \ \ i = r \\  a\_{rj}  \ \ \ \  \ \ i = s \\ a\_{ij} \ \ i \notin \Set{r,s}\end{cases}$

<br>

Thus, we define that a matrix $E \in M_n(F)$ is an elementary matrix if $\exists \theta: \mathcal{E}_\theta(I_n) = E$. Observe that for example, for $n = 2$ there can only be the following forms for elementary matrix:

<br>

$$\begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix},\quad
\begin{bmatrix}1 & c \\ 0 & 1\end{bmatrix},\quad
\begin{bmatrix}1 & 0 \\ c & 1\end{bmatrix},\quad
\begin{bmatrix}c & 0 \\ 0 & 1\end{bmatrix},\ c\ne 0,\quad
\begin{bmatrix}1 & 0 \\ 0 & c\end{bmatrix},\ c\ne 0$$

<br>

Then, let $\mathcal{E}\_\theta$ be an elementary row operation and let $E\_\theta \in F^{m \times m}$ elementary matrix $E\_\theta = \mathcal{E}\_\theta(I)$. Then, for every $m \times n$ matrix $A$, is $\mathcal{E}\_\theta(A) =E\_\theta A$.

As we did to see the behaviour of the identity matrix, lets take a closer look on how $E\_\theta$ behaves. For simplicity, lets take $A \in M\_{2 \times 2}(F)$

$$A := \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}, \quad E^1_{21} := \mathcal{E}^1_{21}(I_2) = \begin{pmatrix}2 & 0 \\ 0 & 1 \end{pmatrix}$$

This, way, when perform the product we have:

$$E^1_{21}A = \begin{pmatrix}2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \left[\begin{pmatrix}2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}a_{11} \\ a_{21} \end{pmatrix},  \begin{pmatrix}2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}a_{12} \\ a_{22} \end{pmatrix}\right]$$

$$ = \left[ \begin{pmatrix} 2a_{11} + 0a_{21} \\ 0a_{11} +1a_{21}\end{pmatrix}, \begin{pmatrix} 2a_{12} + 0a_{22} \\ 0a_{12} +1a_{22}\end{pmatrix} \right] = \begin{pmatrix}2a_{11} & 2a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \mathcal{E}^1_{21}(A)$$

A similar proof can be provided for any other $\theta$ and can be extrapoled for an arbitrary dimension $m\times n$. The point is that we've just seen above how $I$ matrix, due to his structure, behaves in the product with other matrix $A$, the $ij$ entry of $IA$ is determined by the $i$-th row of $I$ and the $j$-th column of $I$ but since $I$ has all his row-entries $0$ except the $i$-th one, then all the $j$-th row-entries except the $i$-th one are cancelled (multiplied by 0):

$$IA := (e_{ij})_{i \in [m],j \in [n]} : e_{ij} := \delta_{ii}a_{ij}$$

This formulation is enough to understand how $\mathcal{E}\_\theta(I)$ affects $E\_\theta A$. Observe that:

- $\theta \mapsto \lambda r \implies e_{rj} := \lambda \delta_{rr}a_{rj} = \lambda a_{rj}$ (observe that the row $i$ gets fixed to the $r$ one)

- $\theta \mapsto r + \lambda s \implies e_{rj} := \delta_{rr}a_{rj} + \lambda \delta_{ss}a_{sj}$ (observe that now in the $r$-th row of $I$ tehre are to non-zero elements due to the elementary operation).

- $\theta \mapsto r \leftrightarrow s \implies e_{rj} := \delta_{ss}a_{sj} \wedge e_{sj} := \delta_{rr}a_{rj}$

<br>

Let's also observe some immediate and interesting fact, and is that every $EA$ is row-equivalent with $A$ and between them. 

Formally:

$$A \in [R]_r \implies \forall \theta \ (E_\theta A \in [R]_r)$$

We can extend this result as:

$$ A \equiv_r B \iff \exists k : \left(\prod_{i=1}^k E_{\theta_k}\right)A = B $$

Immediately, from 3.2.3, $A \equiv\_r B \iff \exists k : \mathcal{E}\_k \cdots \circ \mathcal{E}\_1(A) = B$, then taking and rolling back each composition as $\mathcal{E}\_i (A) = E\_{\theta\_i}A$, we have that $ E\_{\theta\_k} \cdots  E\_{\theta\_1}A = \left(\prod\_{i=1}^k E\_{\theta\_k}\right)A =  B$

<br>

## 5.4. Matrix product exercises.

1. **Find two different $2 \times 2$ matrices A such that $A^2 = 0$ but $A\neq 0$.**

    Let $A :=  \begin{pmatrix}a & b \\ c & d \end{pmatrix}$, then, $A^2:= \begin{pmatrix}a^2 +bc & ab + bd \\ ac + dc & cb + d^2\end{pmatrix}$ and we can form the following constraings around the points of $\mathbb{R}$ that, must satisfy to be $0$:

    $$A^2 = 0 \iff \begin{cases} a^2 + bc = 0 \\ ab + bd = 0 \\ ac +dc = 0 \\ cb + d^2 = 0\end{cases} \iff \begin{cases} a^2 = - bc \\ b(a+d) = 0 \\ c(a+d) = 0 \\ d^2 = - cb\end{cases}$$

    Thus, we get assuming the decision that no point can be $0$:

    $$\begin{cases} a^2 = - bc \\ a = -d \\ d^2 = - cb\end{cases}$$

    Taking $(-1,-1,1,1), (1,1,-1,-1) \in \mathbb{R}^4$ we have the matrix:

    $$A_1 :=  \begin{pmatrix}-1 & 1 \\ -1 & 1 \end{pmatrix}, \quad A_2 :=  \begin{pmatrix}1 & -1 \\ 1 & -1 \end{pmatrix}$$

    <br>

2. **Let $A \in M_{m \times n}(F)$ and $B \in M_{n \times k}(F)$ matrix. Show that the columns of $AB$ are linear combinations of the columns of $A$**

    Let's first check this result in a $2 \times 2$ and then extrapole it a general result.

    Be $A:= \begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix},B:= \begin{pmatrix}b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} \in M_2(F)$, then check that:

    $$AB := (A\beta_1, A \beta_2) = \begin{pmatrix}a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\ a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22} \end{pmatrix}$$

    Thus, $AB = (\gamma_1, \gamma_2)$ with:

    $$\begin{cases} \gamma_1 = \begin{pmatrix} a_{11} \\ a_{21} \end{pmatrix} b_{11} + \begin{pmatrix} a_{21} \\ a_{22} \end{pmatrix}b_{21} = \alpha_1 b_{11} + \alpha_2 b_{21} \\ \gamma_2 = \begin{pmatrix} a_{11} \\ a_{21} \end{pmatrix} b_{12} + \begin{pmatrix} a_{21} \\ a_{22} \end{pmatrix}b_{22} = \alpha_1 b_{12} + \alpha_2 b_{22} \end{cases}$$


    Thus, the generic case for $A \in M_{m \times n}(F), B \in M_{n \times k}(F)$ is that:

    $$AB := (\gamma_1,\ldots,\gamma_k): \gamma_i := \sum_{r=1}^n \alpha_r b_{ri}$$

    <br>

# 6. Invertible Matrices.

Suppose $P \in M_m(F)$ matrix which is a product of elementary matrices. For each $A \in M_{m \times n}(F)$ is true that $PA = B \equiv_r A \implies \exists Q \in M_m(F) : QB = A$. 

In particular this is true when $A =  I_m$. In other words, $\exists Q \in M_m(F) : QP = I_m$, which is itself a product of elementary matrix. 

More specifically the existence of a $Q : QP = I_m$ is equivalent to the
fact that $P$ is a product of elementary matrices. 

<br>

## 6.1. Definition. Left, Right and two-sided inverse.

Let $A \in M_n(F)$ (square) matrix over the field $F$. 

- An $B \in M_n(F) : BA = I_n$ is called a *left inverse* of $A$.

- An $B \in M_n(F) : AB = I_n$ is called a *right inverse* of $A$. 

- If $AB = BA = I$, then $B$ is called a two-sided inverse of $A$ and $A$ is said to be *invertible*. 

Note the following interesting result. Suppose in the context before that $B$ is a left inverse and $C$ is the right inverse for a matrix $A$, then:

$$B = BI = B(AC) = (BA)C = IC = C$$

So when te left and the right inverse exists, both matrix are the same and in general the matrix is two-side inversible. We then call it $A^{-1}$:

$$A^{-1} \in M_n{F} : A^{-1}A = AA^{-1} = I$$

<br>

## 6.2. Important Properties of the inverse.

Let be $A,B \in M_n(F)$, then:

- $\exists A^{-1} \implies (A^{-1})^{-1} = A$. 

    Observe that calling $A^{-1} = C$, then $AC =CA = I$, thus $C^{-1} = (A^{-1})^{-1} = A$

    <br>

- $\exists A^{-1},B^{-1} \implies (AB)^{-1} =B^{-1}A^{-1}$

    Check that $ABB^{-1}A^{-1} = AIA^{-1} = AA^{-1} = I$ and also $B^{1}A^{-1}AB = I$

    As a corollary, in general, any product of invertible matrices is invertible, being the inverse:

    $$(\prod_{i=1}^n A_i)^{-1} = \prod_{i=1}^n A_{n-i+1}^{-1}$$

<br>

## 6.3. Elementary Matrices and Inverse.

### 6.3.1. Inverse of elementary matrix.

Let's start seeing that any elementary matrix $E$ is invertible. Observe that $\mathcal{E}\_\theta(I)=E\_\theta$, we know that we can think about revert this operation by calling the elementary row-operation $\mathcal{E}\_{\theta^{-1}}$ (check the section 3.2.2.2), observe that naturally $\mathcal{E}\_{\theta^{-1}} \circ \mathcal{E}\_{\theta}(I) =\mathcal{E}\_{\theta} \circ \mathcal{E}\_{\theta^{-1}}(I) = I$ meaning that if we call $\mathcal{E}\_{\theta^{-1}}(I) = E\_{\theta^{-1}}$ it verifies: $E\_{\theta^{-1}}E\_\theta = E\_\theta E\_{\theta^{-1}} =I$ and we can safely say $E\_{\theta^{-1}} =E\_\theta^{-1}$

<br>

### 6.3.2. Characterization of an invertible matrix. Gauss Method.

We are now going to present a result that is characterization of any invertible matrix as a product of elementary matrix. The following statements are equivalent for $A \in M_n(F)$:

1. $\exists A^{-1}$
2. $ A \equiv\_r I\_n (\text{or } A \in [I\_n])$
3. $\exists k \in \mathbb{N} : A = \prod\_{i=1}^k E\_i$

Meaning that a matrix $A$ is invertible only iff row-equivalent to the identity and by the characterization of the elementary matrix made before this also means that a matrix is invertible only iff is a product of elementary matrix.


Observe that $1 \to 2$: 

$$A \in [R]_r \iff \exists k \in \mathbb{N} : A = \left(\prod_{i=1}^k E_i\right) R \iff \left(\prod_{i=1}^k E_{k-i+1}^{-1}\right)A = R$$

By the last result of the section above we know that a product of invertible matrix is an invertible matrix, since $A$ is invertible $R$ must be but observe that this is only posible if $R$ has no zero-rows otherwise no product could produce $I$, thus $R = I$ and $A \in [I\_n]$

Then, immediately $2 \to 3$, 

$$A \in [I_n]_r \iff \exists k \in \mathbb{N} : A = \left(\prod_{i=1}^k E_i\right) I_n = \prod_{i=1}^k E_i$$

And $3 \to 1$

$$\left(\prod_{i=1}^k E_{k-i+1}^{-1}\right) \left(\prod_{i=1}^k E_i\right) = \left(\prod_{i=1}^k E_i\right) \left(\prod_{i=1}^k E_{k-i+1}^{-1}\right) = I_n$$

And we say $\left(\prod\_{i=1}^k E\_{k-i+1}^{-1}\right) = A^{-1}$ and $A$ is invertible.

With this characterization, we can extend our characterization of row-equivalent matrix. If any product of elementary matrix can be abstracted in an invertible matrix $P$, then for $A,B \in M\_{m \times n} (F)$:

$$A \equiv_r  B \iff \exists P \in [I_n] : AP =B$$

<br>

**Gauss Method to obtain the inverse**

Observe that also the last result give us a mechanism to obtain $A^{-1}$. If for $A \in M_{n}(F)$ is:

$$\exists A^{-1} \iff A \in [I_n] \iff \exists k \in \mathbb{N} : \prod_{i=1}^k E_i = A$$

Then, the idea is if $A$ is invertible, you can transform it into $I_n$ by a sequence of elementary row operations:

$$\mathcal{E'}_k \cdots \circ \mathcal{E'}_1 (A) = \left(\prod_{i=1}^k E'_i \right) A = I_n $$

Observe that by definition, the product of elementary matrix that multiplicated by $A$ gives $I_n$ is infact $A^{-1}$, so to speak:

$$\prod_{i=1}^k E'_i = \mathcal{E'}_k \cdots \circ \mathcal{E'}_1 (I_n) = A^{-1}$$

This way the method is to form the $n \times 2n$ augmented matrix $[A \ \vert \ I\_n]$ and apply to it the sequence $\mathcal{E'}\_k \cdots \circ \mathcal{E'}\_i$ in order to obtain $[I\_n \ \vert \ A^{-1}]$, formally:

$$\mathcal{E'}_k \cdots \circ \mathcal{E'}_i([A \ \vert \ I_n]) = [I_n \ \vert \ A^{-1}] $$

In other words, we apply to $A$ in $[A \ \vert \ I\_n]$ elementary row-operations until we obtain the RREM (which is $I_n$ since $A \in [I\_n]$) and that will give us as result $A^{-1}$ in $[I_n \ \vert \ A^{-1}]$.


<br>

### 6.3.3. Invertible Matrix and Linear Equation Systems.

In this section we will nail down all the inverse matrix purpouse which is simplify the linear equation system expresion towards a unique solution. 

The following theorem states how the inverse help to solve and discuss linear equation systems.

<br>

The following statements are equivalent for a $A \in M_n(F)$:

1. $\exists A^{-1}$
2. The homogeneous system $AX = 0$ only has the trivial solution $X = 0$
3. The system of equations $AX = Y$ has a solution $X$ for each $n \times 1$ matrix $Y$

Observe that $1 \to 3$:

$$AX = Y \wedge \exists A^{-1} \implies A^{-1}A X = I_n X = X = A^{-1}Y$$

Also that $3 \to 2$ making $Y=0$ and also $2 \to 1$ using $4.2.2$ getting the whole equivalence.

<br>

Observe that first, lets say we have $M := [AX = Y]$ a linear system of $n$ equations in $n$ unknowns, this system doesn't englobe all the posible linear systems equations (the discussion of any system need more tools) but it give us a first approach to the system type that give us a chance for the information of the system to be complete.

We can get some properties from $M$ by studying $A$ and applying the concepts we've study in this chapter.

- First, if $A \in [I_n]$, then, knowing that $M$ and $M' := [I\_n X = Y']$ share the same solution (being $Y'$ the matrix obtained in the process $[A \ \vert \ Y] \to [I_n \ \vert \ Y']$) since both are equivalent and by $4.2.2$ we can assert that $S\_{M'}  \neq \varnothing \wedge \vert S\_{M'} \vert = 1$. 

    So, at first, studying the RREM of $A$ we can know if the solution exists as a unique point of $F^n$.

    <br>

- Also, $A \in [I_n] \iff \exists A^{-1}$ and the inverse give us a characterization of the unique element of the set $S_{M'}:=\Set{X \in F^n \ \vert \ X = A^{-1}Y}$.

    The inverse, which exists as we've seen above, give us the solution whose existance has been assert in the previous point.

    <br>

# 7. Summary.

## 7.1 Summary of the chapter.

In this chapter we have seen that a system of linear equations

$$M := \bigwedge_i P_i$$

over a field $F$ is, in essence, a collection of linear constraints over points of $F^n$. This system synthesizes information about $F^n$ materialized in the solution set of the system:

$$S := \{x \in F^n \mid M \equiv \top\}$$

So that two systems $M, M'$ are equivalent when they contain the same information about $F^n$, that is; they describe the same $S$.

We have seen that certain operations between the predicates of the system such as scaling $S_{\lambda P} = S_P$, linearly combining while keeping the original $S_{\gamma P + \lambda Q} \cap S_Q = S_P \cap S_Q$, and permuting, preserve this equivalence; they keep the information of the system intact.

We use matrices to encode and abbreviate the information contained by systems of linear equations. Specifically, in the system $M \equiv [AX = 0]$ the coefficient matrix $A$ packages most of this information, eliminating the redundancy of writing the unknowns $X$.

We have seen that we can simplify these packages without altering the information they contain through elementary row operations, which are the direct transfer of the operations between predicates:

$$\mathcal{E}_\theta : M_{m \times n}(F) \to M_{m \times n}(F)$$

These operations are bijections with inverses of the same type, that is, reversible.

We have formalized the relationship between all those matrices that encode the same linear constraints over $F^n$ through the equivalence relation $\equiv_r$ induced by finite composition of these row operations:

$$A \equiv_r B \iff \exists k \in  \mathbb{N} : \mathcal{E_\theta}_1 \cdots \circ \mathcal{E_\theta}_k(A) = B $$

And we have grouped matrices of the same type into equivalence classes $[A]_r$ whose canonical representative is the RREF, which is the simplest form in which the information of the system can be expressed, where the solution can be read directly and is shared by any other matrix in the same class.

Finally, we created a computational way of expressing the previous concepts through the matrix product, whose definition is forced by the notation $AX = Y$ (each entry reproduces exactly the linear combination of the $i$-th row over the unknowns of $X \in M_{n \times 1}(F)$).

This operation turns these sequences of operations into algebraic objects: each $\mathcal{E}\_\theta$ materializes as multiplication by an elementary matrix $E\_\theta = \mathcal{E}\_\theta(I)$, so that $\mathcal{E}\_\theta(A) = E\_\theta A$.

This allows us to condense a finite sequence of elementary operations on a matrix into a single product and consequently redefine the equivalence relation:

$$A \equiv_r B \iff \exists P \in M_n(F) : B = PA \wedge \left(\exists k \in \mathbb{N} : P = \prod_{i=1}^k E_{\theta_i}\right)$$

And lastly, we have introduced the concept of the inverse of a matrix $A^{-1}$ with the purpose of characterizing the unique solution of the system $M$ when $A$ is invertible:

$$AX = Y \wedge A \in [I_n] \implies X = A^{-1}Y$$

The chapter culminates with the chain of equivalences that characterizes the invertibility of $A \in M_n(F)$ so that $A$ is invertible if and only if $A$ is a product of elementary matrices.

This chain connects four apparently distinct ideas, one algebraic (factorization), one computational (row reduction), and two about systems of equations (homogeneous and general), into a single notion, and is the central result of the chapter that will be expanded throughout the book.

<br>

## 7.2. Key results.

**Equivalence of systems**

- **Equivalence means same solution set (§2.3.1):** $M \equiv M' \iff S = S'$.

- **Scaling preserves solutions (§2.3.2):** $\lambda \in F \setminus \{0\} \implies S_{\lambda P} = S_P$.

- **Replacement rule (§2.3.2):** $S_{\gamma P + \lambda Q} \cap S_Q = S_P \cap S_Q$. The combined equation alone is strictly weaker: $S_P \cap S_Q \subseteq S_{\gamma P + \lambda Q}$, but keeping $Q$ in the system recovers $P$.

- **Linear combination characterization of equivalence (§2.3.2):** If $M \equiv M'$ and $S \neq \varnothing$, then every predicate $P_i \in M$ can be expressed as a linear combination of the predicates in $M'$ and vice versa.

<br>

**Elementary row operations and row-equivalence**

- **Elementary row operations are bijections (§3.2.2.2):** Each $\mathcal{E}\_\theta : M\_{m \times n}(F) \to M\_{m \times n}(F)$ is invertible, and the inverse is an elementary row operation of the same type.

- **Row-equivalence is an equivalence relation (§3.2.3):** $\equiv_r$ on $M_{m \times n}(F)$ is reflexive, symmetric, and transitive.

- **Row-equivalence $\iff$ system equivalence (§3.2.3):** $[A \mid Y] \equiv_r [A' \mid Y'] \iff [AX = Y] \equiv [A'X = Y']$.

<br>

**Row-reduced forms**

- **Existence of RREF (§4.1.1 + §4.2.1):** Every $A \in M_{m \times n}(F)$ is row-equivalent to a row-reduced echelon matrix $R$, and $R$ is the unique canonical representative of $[A]_r$.

- **More unknowns than equations (§4.2.2):** If $A \in M_{m \times n}(F)$ with $m < n$, then $AX = 0$ has a non-trivial solution.

- **Square matrix criterion (§4.2.2):** $A \in M_n(F) \implies (A \equiv_r I_n \iff S_{[AX=0]} = \{0\})$.

- **$2 \times 2$ determinant criterion (§4.1.2, ex. 8):** For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$: $ad - bc \neq 0 \implies S_{[AX=0]} = \{(0,0)\}$.

<br>

**Matrix product**

- **Definition forced by $AX = Y$ (§5.1):** $(AB)\_{ij} = \sum\_{k=1}^p a\_{ik}b\_{kj}$, and $AB = (A\beta\_1, \ldots, A\beta\_n)$ where $\beta\_j$ are the columns of $B$.

- **Associativity (§5.2.1):** $A(BC) = (AB)C$.

- **Columns of $AB$ are linear combinations of columns of $A$ (§5.4, ex. 2):** $\gamma\_j = \sum\_{r=1}^n \alpha\_r b\_{rj}$.

- **Elementary matrices implement row operations (§5.3.2):** $\mathcal{E}\_\theta(A) = E\_\theta A$ where $E\_\theta = \mathcal{E}\_\theta(I)$.

- **Row-equivalence via matrix product (§5.3.2):** $A \equiv\_r B \iff \exists k : \left(\prod\_{i=1}^k E\_{\theta\_i}\right) A = B$.

<br>

**Invertible matrices**

- **Left = right inverse (§6.1):** If $BA = I$ and $AC = I$, then $B = C$. So when both exist, the inverse is unique: $A^{-1}$.

- **Inverse of a product (§6.2):** $(AB)^{-1} = B^{-1}A^{-1}$.

- **Every elementary matrix is invertible (§6.3.1):** $E\_\theta^{-1} = E\_{\theta^{-1}}$.

- **Characterization of invertibility (§6.3.2):** For $A \in M\_n(F)$, the following are equivalent: (i) $A$ is invertible. (ii) $A \equiv\_r I\_n$. (iii) $A = \prod\_{i=1}^k E\_i$ for some elementary matrices $E\_i$.

- **Invertibility and linear systems (§6.3.3):** For $A \in M\_n(F)$, the following are equivalent: (i) $A$ is invertible. (ii) $S\_{[AX=0]} = \{0\}$. (iii) For every $Y \in M\_{n \times 1}(F)$, the system $AX = Y$ has a solution. Moreover, when $A$ is invertible, the solution is unique: $X = A^{-1}Y$.

- **Row-equivalence via invertible matrix (§6.3.2, corollary):** $A \equiv\_r B \iff \exists P$ invertible with $B = PA$.

- **Corollary: square matrix with one-sided inverse is invertible (§6.3.3):** If $A \in M\_n(F)$ has a l

<br>