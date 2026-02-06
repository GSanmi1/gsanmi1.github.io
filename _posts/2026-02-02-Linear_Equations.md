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

 $$\begin{rcases} x · 0 = 0 \\ x·y=0 \iff (x = 0 \ \vee \ y=0) \ \end{rcases} \ \forall x,y \in F $$

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

In maths, “Linear” means no interactions between variables and no bending. In this context, a linear combination of a finite set of variables $\Set{x,y,...}$ means:

- No interactions betweem elements in $\Set{x,y,..}$; no products $(xy)$, squares $(x^n): n \in \mathbb{R}$, etc.
- A change in the inputs (“add” or “scale”), provokes a proportional change in the output.

<br>