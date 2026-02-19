---
layout: post
title: "Linear Equations & Matrix."
subtitle: "Fields, Linear Equations and Matrix on a field."
date: 2026-02-06 09:00:00 +0000
categories: ['Linear Algebra']
tags: ['Hoffman&Kunze', 'Algebra']
author: German Sanmi
---

# 1. Fields.

## 1.1. Number sets.

A main focus of high-school mathematics lifes in the development of the usual range of numbers, which is developed step by step 

$$\mathbb{N_{0}} \hookrightarrow \mathbb{Z} \hookrightarrow \mathbb{Q} \hookrightarrow \mathbb{R} \hookrightarrow \mathbb{C}$$

But this sets are characterized as algebraic structres with their own structures. For example:

- $N_0$ is also called a *monoid*, a set that allows an operation $+$ with a neutral element 0. But the elements $\neq 0$ do not have an inverse $-a$ with respect to +. (We remember that the inverse of an element $a$ is another element $-a$ that complies with $a + (-a) = 0$).

- If we extend to $\mathbb{Z}$ and add also the multiplication we obtain a *commutative ring* with unit. Most elements do not have a multiplicative inverse.

- Then, again, we can expand $\mathbb{Z}$ to $\mathbb{Q}$ among with the notion of a *fraction* in order to ensure that every element has a multiplicative inverse, this is called a *field*. But then, there exists equations, like $x^2 - 2 = 0$ with no solutions in $\mathbb{Q}$.

- Then, we expand $\mathbb{Q}$ to $\mathbb{R}$ in order to give solution for that equation and forming the notion of irrational numbers; $\sqrt 2, \pi, etc$. This is called a *complete field*. But again, $x^2 - 1 = 0$, for a different reason, this equation also has no roots.

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

    In $F$, the identity is $1_F$, then due to uniqueness of this identity in $F$ is $1_K = 1_F$ for the elements of $K$ in $F$, so isolating $K$ from $F$ necesarily is $1_{F} \in K$ and the same can be applied to $0$, meaning that any subfield inherit the identity of the superfield.

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

- Coefficients: $a_{ij} \in F: 1 \leq j \leq m, 1 \leq j \leq n$
- Unknowns:  $x_{ij} \in F: 1 \leq j \leq m, 1 \leq j \leq n$
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

$$2P - Q = P':-3x_1 -x_2 = 0 \iff x_1 = -3x_2$$

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

- Being $\Set{F, \ ·}$, then lets demonstrate that is a group.

    - **Closure**: By definition, any composition of the elements of $F$ by $·$ is an element of $F$.

        <br>

    - **Associativity**: Observe that the result in the composition is always $0$ except for the case in which the both elements are $1$, so:

        $$a · (b·c) = \begin{cases} 1 \ \ a = b= c = 1 \\ 0 \end{cases}$$

        $$(a·b)·c = \begin{cases} 1 \ \ a = b= c = 1 \\ 0 \end{cases}$$

        Thus, always $a · (b·c) = (a·b)·c$.

        <br>

    - **Identity**: Check that $a·0 = 0·a = 0 \ \ \forall a \in F$
    - **Inverse**: Observe that $a·a = a \ \ \forall a \in F$

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

A *matrix* is a device to package information linearly codified. Is a structured way to record how a linear rule takes inputs to outputs (along with coordinates). 

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

$$ X : [1] \times [n] \to  F$$

$$X(j) = x_{j}$$

<br>

$$X= \begin{bmatrix}X_{1} \\\vdots \\ \ X_{n} \end{bmatrix} = \begin{bmatrix}X(1) \\ \vdots\\ X(n) \end{bmatrix} = \begin{bmatrix} x_{1}\\\vdots \\ x_{n} \end{bmatrix} = (x_{j})_{j \in \mathbb{N}}$$

<br>

$$ A : [m] \times [1] \to  F$$

$$A(i) = a_{i}$$

$$Y= \begin{bmatrix}Y_{1} \\\vdots \\ \ Y_{m} \end{bmatrix} = \begin{bmatrix}Y(1) \\ \vdots\\ Y(m) \end{bmatrix} = \begin{bmatrix} y_{1}\\\vdots \\ y_{m} \end{bmatrix} = (y_{i})_{i \in \mathbb{N}}$$

<br>

### 3.2.2. Matrix operations.

For the time being, $AX = Y$ is nothing more than a shorthand notation for our system of linear equations. Later, when we have defined a multiplication for matrices, it will mean that $Y$ is the product of $A$ and $X$. 

We wish now to consider operations on the rows of the matrix $A$, which correspond to forming linear combinations of the equations in the system $AX = Y$. We restrict our attention to three elementary row operations on an $m \times n$ matrix $A$ over the field $F$. 


Conceptually these are the three “row moves” that change the representation of a matrix in a controlled way; formally they are functions $M_{m \times n} \to M_{m \times n}$ 

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

$$\mathcal{E}_{r  \leftrightarrow s}^r(A):=(e_{ij})_{i \in [m], j \in [n]} : e_{ij} := \begin{cases}  a_{sj}  \ \ \ \ \ \ i = r \\  a_{rj}  \ \ \ \  \ \ i = s \\ a_{ij} \ \ i \notin \Set{r,s}\end{cases}$$

<br>

All this function $\mathcal{E}$ eventually relates $A$ with the matrices $E_{\lambda r}^r, E_{r + \lambda s}^r, E_{r  \leftrightarrow s}^r$

The definition of this matrices are coherent with the system $AX = Y$, in the sense that the operations preserve system equivalence after apply the same change to $Y$:

$$[AX = Y] \equiv [E_{\lambda r}^rAX = E_{\lambda r}^rY] \equiv [E_{r + \lambda s}^rAX = E_{r + \lambda s}^rY] \equiv [E_{r  \leftrightarrow s}^rAX = E_{r  \leftrightarrow s}^rY]$$

This will make sense when we presentate the matricial product and check that the resulting system of equations is the result of apply a property that respects the equivalence as we saw that the start of this post.