---
layout: post
title: "Linear Equations."
subtitle: "Fields and Linear Equations in a field."
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

2. The addition and multiplicative operations get related through:

    $$a \ · (b + c) = a · b + a·c \ \ \forall a,b,c \in F$$

As examples, $\Set{\mathbb{C},+, \ ·}$ and $\Set{\mathbb{R}, + , \ ·}$ are fields.

<br>

### 1.3.2. Properties of a field.

A field $\Set{F,+, \ ·}$, separate as two compatible abelian groups: $\Set{F,+}$ and $\Set{F\setminus \Set{0}, \ ·}$, satisfies the properties.

$\forall x ,y ,z \in F$:

- *Closure*: $\begin{cases} \ x + y \in F \\ \ x·y \in F \end{cases}$

- *Associativity*: $\begin{cases} \ (x + y) + z = x + (y + z) \\ \ (x·y)·z = x·(y·z) \end{cases}$

- *Conmutativity*: $\begin{cases} \ x + y = y + x \\ \ x·y = y·x \end{cases}$

- *Identities*: $\begin{cases} \ \exists! \ 0 \in F : x + 0 = x \\ \ \exists! \ 1 \in F : x·1 = x \end{cases}$

- *Negative and Inverse*: $\begin{cases} \ \forall x \in F \ \exists ! \ -x \in F : x + -x = 0 \\ \ \forall x \in F \setminus \Set{0} \ \exists ! \ \ x^{-1} \in F : x · x^{-1} = 1 \end{cases} \ \land \ 0 \neq 1$ in order to avoid trivial zero-ring $F:=\Set{0}$.

- *Compatibility*: $\ \ x·(y + z) = x·y + x·z$


- *Cancelation*: $\begin{cases} x + y = x + z \iff y = z \\ x · y = x·z \ \land \ x \neq 0 \iff y = z \end{cases}$

<br>

### 1.3.3. Identities relations lemma.

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

# 2. System of Linear Equations.

## 2.1. Brief introduction. Linear meaning.

In maths, “Linear” means no interactions between variables and no bending. In this context, a linear combination of a finite set of variables $\Set{x,y,\cdots}$ means:

- No interactions betweem elements in $\Set{x,y,..}$; no products $(xy)$, squares $(x^n): n \in \mathbb{R}$, etc.
- A change in the inputs (“add” or “scale”), provokes a proportional change in the output.

Then, a **system of linear equations** is a collection of constraints or predicates of the form of linear expressions on a finite number of unknowns. The solutions of the whole system are the points that satisfy all constraints at once, the intersection of the predicates.

<br>

## 2.2. Formal definition.

Let be $F$ a field and $m,n \geq 1$, then a finite system of $m$ linear equations in $n$ unknowns over $F$ is specified by:

- Coefficients: $a_{ij} \in F: 1 \leq j \leq m, 1 \leq j \leq n$
- Unknowns:  $x_{ij} \in F: 1 \leq j \leq m, 1 \leq j \leq n$
- Constants: $b_i \in F: 1 \leq i \leq m$

Related as:

$$\begin{cases} \displaystyle\sum_{j = 1}^na_{1j}x_{j} = b_1 \\ \ \  \vdots \\ \displaystyle\sum_{j = 1}^na_{mj}x_{j} = b_m\end{cases} \iff \begin{cases} a_{11}x_{11} \cdots + a_{1n}x_{1n} = b_1 \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \vdots \\ a_{m1}x_1 \cdots + a_{mn}x_{n} = b_m\end{cases} $$

Then, any tuple $(x_1,\cdots,x_n) \in F^n$ that satisfies all the constraints simultaneusly is called a *solution* of the system.

The system is called *homogeneous* if the unique solution available is $0 \in F^n$.

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


<br>

**Exercises**

1. Verify that the set of complex numbers $F:= \Set{z \ \vert \ \exists x,y \in \mathbb{Q} : z = x + y\sqrt{2}}$ is a subfield of $\mathbb{C}$.

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

        $$z_1 + (z_2 + z_3) = [x_1 + (x_2 + x_3)] + [y_1 + (y_2 + y_3)]\sqrt{2} = \\ [(x_1 + x_2) + x_3] + [(y_1 + y_2) + y_3]\sqrt{2} = (z_1 + z_2) + z_3$$

        <br>

    - **Conmutativity**:

        Being $z_1,z_2 \in F$, then:

        $$z_1 + z_2 = (x_1 + x_2) + (y_1 + y_2)\sqrt{2} = \\ (x_2 + x_1) + (y_2 + y_1)\sqrt{2} = z_2 + z_1$$

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
        
        $$x_1(x_2x_3 + 2y_2y_3) + x_1(x_2y_3 + y_2x_3)\sqrt{2} + y_1\sqrt{2}(x_2x_3 + 2y_2y_3) + y_1\sqrt{2}(x_2y_3 + y_2x_3)\sqrt{2}=$$
        
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


    Lets now demonstrate that both abelians groups are compatible;

    $$z


