---
layout: post
title: "The Real Number System"
subtitle: "Rational and Real fields presentation. Order. LUB. Dedekind cuts. Extended real field. Analysis definition."
date: 2026-03-05 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
subject: real-analysis
lang: en
---

1. Introduction.
    - 1.1. Rational numbers inadequacy. Irrational numbers.

2. Ordered Sets.
    - 2.1. Binary relations.
        - 2.1.1. Definition.
        - 2.1.2. Properties.
        - 2.1.3. Order Types.
    - 2.2. Order in $\mathbb{Q}$.

3. Bounds. 
    - 3.1. Upper and Lower bounds of a set. Supremum and Infimum.
    - 3.2. Example of bounds in subsets of $\mathbb{Q}$.
    - 3.3. Least-upper-bound property.

4. Fields.
    - 4.1. Definition and Axioms.
    - 4.2. Immediate properties.
    - 4.3. Ordered fields.
        - 4.3.1. Definition.
        - 4.3.2. Properties of ordered fields.
5. The Real field.
    - 5.1. Theorem: Existence of $\mathbb{R}$. Dedekind cuts.
        - 5.1.1. Cuts.
        - 5.1.2. $\mathbb{R}$ is an ordered set.
        - 5.1.3. $\mathbb{R}$ satisfies the $LUB$ property.
        - 5.1.4. Addition in $\mathbb{R}$.
        - 5.1.5. Multiplication in $\mathbb{R}$.
        - 5.1.6. $\mathbb{Q}$ in $\mathbb{R}$.
    - 5.2. Important Properties from the $\mathbb{R}$ field.
        - 5.2.1. Archimedean property of $\mathbb{R}$.
        - 5.2.2. $\mathbb{Q}$ is dense in $\mathbb{R}$
        - 5.2.3. *nth* roots of positive reals.
    - 5.3. Brief summary about $\mathbb{R}$.

6. The extended Real Number System.
    - 6.1. Definition.
    - 6.2. Operations in $\overline{\mathbb{R}}$.

7. Summary.

    <br>

# 1. Introduction.

A satisfactory discussion of the main concepts of analysis (such as convergence,
continuity, differentiation, and integration) must be based on an accurately
defined number concept. 

We will presume familiarity with $\mathbb{Q}$ (meaning that we assume the sentence "$(\mathbb{Q},+, \ ·)$ is a field and the axioms for the field's algebraic structure apply in their totality." is completely understood and acknowledged by the reader) and use this knowledge to build $\mathbb{R}$ and then $\mathbb{C}$.

<br>

## 1.1. Rational numbers inadequacy. Irrational numbers.

Let's start by talking about some shortcomings of the rational numbers. The rational number system is inadequate for many purposes, both as a field and as an ordered set, since the rational number line is full of gaps. 

For instance, there is no $p \in \mathbb{Q} : p^2 = 2$. Let's consider that $\exists p \in Q: p^2 = 2$, then this would imply that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$

Let's also observe that if $m, n \in \mathbb{2Z}$, then we could divide the numerator and denominator by $2$ and the fraction would still be worth $p$ and $m,n \in \mathbb{2Z}$ so we could divide again, and eventually this iterative process of dividing by $2$ must terminate because eventually one of the two must be odd. 

So we can ensure without loss of generality that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$ and at least one of both is not even. Then, the equation imposes that $m$ is even:

$$p^2 = \left(\frac{m}{n}\right)^2 = \frac{m^2}{n^2} = 2 \iff m^2 = 2n^2 \in 2\mathbb{Z}$$

Let's observe that $2 \vert n^2 \implies 2 \vert n$, if $2 \vert n^2 \wedge 2\not\vert  \ n$ then $n = 2q + 1  \implies n^2 = 2(2q^2 +2q) + 1$ and $2 \not\vert n^2$ contradicting the initial premise. 

So, we have:

$$m \in \mathbb{2Z} \implies 2 \vert m \implies 4 \vert m^2 \iff 4 \vert 2n^2 \implies n^2 \in \mathbb{2Z}$$

and also $n$ is even contradicting the presumption. So there are no $m,n \in \mathbb{Z} : p = \frac{m}{n}$

<br>

This leads to the introduction of so-called *irrational numbers* which are often written as infinite decimal expansions and are considered to be "approximated" by the corresponding finite decimals, meaning that, for example; $1, 1.4, 1.41, 1.414, 1.4142,\ldots$ tends to $\sqrt 2$. But before that we have to define what "tends" or "approximates" means. 

<br>

To illustrate the idea of the irrational number better, we can consider the following sets: 

$$A:= \Set{p \in \mathbb{Q}^+ \mid p^2 < 2 }, \quad B:= \Set{p \in \mathbb{Q}^+ \mid  p^2 > 2 }$$

Let's demonstrate that $A$ contains no largest number and $B$ contains no smallest, but neither of them contains the point itself (since it is not rational):

$$q = p - \frac{p^2 -2}{p+2}: p \in \mathbb{Q}$$

- Check that if $p \in A \implies p^2 < 2 \iff p^2 - 2< 0 \implies q > p$, and also  observe that: 

    $$ q^2 - 2 = \left( p - \frac{p^2 -2}{p+2} \right)^2 - 2 = \left(\frac{2p + 2}{p+2} \right)^2 - 2 = \frac{2(p^2 - 2)}{(p+2)^2}$$

    Hence, $p^2 - 2 < 0 \implies q^2 - 2 < 0 \implies q \in A$. Thus we can state that:

    $$\forall p \in A \ \exists q \in A:  q > p$$

- Let's also observe using the same definition, $p \in B \implies q \in  B \wedge p > q$ which means that also is:

    $$\forall p \in B \ \exists q \in B:  q < p$$

Then, we can understand the *irrational numbers* as a "never-reached-frontier" of certains segments of rational numbers like $A$ or $B$. 

Observe that we only need one of the two sets because both of them "tend" to the same value. By default, we would prefer $A$ as a standard to present the irrational number to which $A$ and $B$ tend. 

<br>

Thus, the rational number system or the rational line is full of gaps, despite the fact that between any two rationals there is another:

$$ r,s \in \mathbb{Q} : r < s \implies r < \frac{r + s}{2} < s \wedge \frac{r + s}{2} \in \mathbb{Q}$$

The *real number system*; $\mathbb{R}$, gets those gaps filled, this is the principal reason for the fundamental role which it plays in analysis.

<br>

# 2. Ordered Sets.

In order to introduce $\mathbb{R}$ and why it is a preferable option to $\mathbb{Q}$ we have to talk about some important properties involved with *order* and thus, first we have to introduce the notion of *ordered sets*. 

So let's start introducing a minimal basis about order in a set.

<br>

First, the mathematical order is an abstraction of a primary cognitive operation: comparing two objects and deciding which of the two goes first, as we ordinarily do with weight, chronological events or hierarchies. Basically the order is a *binary relation between elements of a domain that codifies "precedence" between the two of them*.

<br>

## 2.1. Binary relations.

### 2.1.1. Definition.

In mathematics, a relation is basically any collection of ordered pairs from a set. 

Formally, given a set $S$, we say that a *binary relation* over $S$ is any $R \subset S^2 = S \times S$. As defined this notion is trivial and lacks any interest and only becomes relevant when the relation forces some conditions.

Being $(x,y) \in R$, we read it as "$x$ is related to $y$ through $R$" and we may write $xRy$ to simplify the notation.

<br>

### 2.1.2. Properties.

Given a binary relation over $R$ over a non-empty set $S$, then $R$ can satisfy the following properties:

- **Reflexivity**: $\forall x \in S,\; xRx \iff \forall x \in S, (x,x) \in R $
- **Irreflexivity**: $\forall x \in S,\; \neg (xRx) \iff \forall x \in S, (x,x) \notin R$

- **Symmetric**: $\forall x, y \in S,\; x \mathbin{R} y \Rightarrow y \mathbin{R} x$, observe that this imposes reciprocity.

- **Antisymmetric**: $\forall x, y \in S,\; (x \mathbin{R} y) \land (y \mathbin{R} x) \Rightarrow x = y$

- **Transitive**: $\forall x, y, z \in S,\; (x \mathbin{R} y) \land (y \mathbin{R} z) \Rightarrow x \mathbin{R} z$ 

- **Connected**: $\forall x, y \in S,\; (x \mathbin{R} y) \lor (y \mathbin{R} x)$

- **Trichotomic** $\forall x, y \in S$ only one of the following statements is true:

    $$x \mathbin{R} y, \quad y \mathbin{R} x, \quad x = y$$

    <br>

### 2.1.3. Order Types.

**Partial and Total orders**

Be $S$ a set, then a relation $\leq \ \subset S^2$ is a *partial order* if it is **reflexive**, **antisymmetric** and **transitive**.

As an extension of the partial order we have *total order* if it is also **connected**, this means, the comparison criterion can be applied to every element of $S^2$. Observe that, geometrically, this means that all the elements can be sorted in a line as it happens with number sets $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ can all be represented in a line.

<br>

**Strict Orders**

Taking a partial order $\leq \subset S^2$, then we define a *strict order* as:

$$< \ \subset S^2 : (x < y \iff x \leq y \wedge x \neq y)$$

Observe that, as defined this relation verifies:

- **Irreflexivity**: $\neg(x < x) \quad \forall x \in S$
- **Transitivity**: Inherited from $\leq \ \subset S^2$

If also $\leq \ \subset S^2$ is total, then $<$ is also **trichotomic** and we would call it *strict total order*, this is imposed by the irreflexive property that makes the three statements disjoint between them.

<br>

## 2.2. Order in $\mathbb{Q}$.

Let's consider for example $\mathbb{Q}$ the set of rational numbers and the binary relation:

$$< \  := \Set{(p,q) \in \mathbb{Q}^2 \ \vert \ q - p \in \mathbb{Q}^+}$$

Then, $< \ \subset \mathbb{Q}^2$ is a *strict total order*:

- Since $0 \notin \mathbb{Q}^+ \implies \big[(p,p) \notin \ < \  \ \forall p \in \mathbb{Q}\big]$ so is irreflexive.

    <br>


- Be $p,q \in \mathbb{Q}$, then $q -p \in \mathbb{Q}^+$ or $-(q - p) = p - q \in \mathbb{Q}^+ $  or $p-q = 0$, which essentially give us the trichotomy property.

    <br>

- Also observe that $p < q \wedge q < t \implies t - p = (t - q) + (q - p) \in \mathbb{Q}^+ \implies p < t$ which means that also satisfies transitivity.

<br>

We also can define the following binary relation $\leq \ \subset \mathbb{Q}^2$, as:

$$\leq \ \subset \mathbb{Q}^2 : (x \leq y \iff x < y \oplus x = y)$$


Then, $\leq \ \subset \mathbb{Q}^2$ is a *non-strict total order*.

Observe that this relation is obviously *reflexive* and *transitive* (inherited from $< \ \subset \mathbb{Q}^2$) and also *antisymmetric*, since $x \leq y \wedge y \leq x \implies x = y$, since $x < y$ and $y < x$ are mutually exclusive.

<br>

# 3. Bounds. 

Until now, we just defined that an ordered set is simply a set in which an order relation has been defined and also define an order in $\mathbb{Q}$. 

Let's introduce the concept of *bounds*, and naturally extract the concept of the *minimal bound* for a set.

<br>

## 3.1. Upper and Lower bounds of a set. Supremum and Infimum.

Consider now $S$ an ordered set and $E \subset S$, then we say that:

$$E \text{ is upperbounded} \iff \exists \alpha \in S: x \leq \alpha \ \ \ \forall x \in E $$

We define the least upper bound (or least-upper-bound) as:  

$$\alpha ' \in S : x \leq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \leq \alpha \ \ \forall \alpha \in S: x \leq \alpha \ \ \forall x \in E)$$

And we denote it as $\alpha ' = sup E$ and call it the *supremum* of $E$. 

This same idea applies to lowerbounds:

$$E \text{ is lowerbounded} \iff \exists \alpha \in S: x \geq \alpha \ \ \ \forall x \in E $$

And we define the *infimum* of $E$ (and we denote it $\alpha ' = inf E$) as:

$$\alpha ' \in S : x \geq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \geq \alpha \ \ \forall \alpha \in S: x \geq \alpha \ \ \forall x \in E )$$

<br>
These are the minimal upper/lower bounds of a set and their existence is not guaranteed as we will see in the example below. Observe trivially that both supremum and infimum are unique; the proof is trivially derived from the trichotomy property but it is worth mentioning this fact for future demonstrations. 

<br>

## 3.2. Example of bounds in subsets of $\mathbb{Q}$.

Let's now observe two examples in which we want to illustrate two facts about minimal bounds.

**The first one illustrates that, in $\mathbb{Q}$, minimal bounds are not guaranteed to exist for any bounded set $S \subset \mathbb{Q}$, and this is the main reason why $\mathbb{Q}$ is full of gaps.**

The second example aims to illustrate that, although the definition of bound does not prohibit a minimal bound of $E$ from being contained in $E$, this is not true in general; a minimal bound often is not a member of the bounded subset.

1. Let's consider again $A:= \Set{p \ \vert \ p^2 < 2 }, B:= \Set{p \ \vert \ p^2 > 2 } \subset \mathbb{Q}^+$. 

    The set $A$ is bounded above. In fact, the upper bounds of $A$ are exactly the members of $B$. Since $B$ contains no smallest member, $A$ has no least upper bound in $\mathbb{Q}$. Similarly, $B$ is lowerbounded and the lower bounds of $B$ are the elements of $A$. But since $\nexists p \in \mathbb{Q} : p^2 = 2$ neither of the two has minimal bound.

    <br>

2. Being $E \subset S$ , then $\exists \alpha = supE$ implies that $\alpha$ may or may not be member of $E$. For instance, $E_1:=\Set{r \ \vert \ r < 0}$ and $E_2:=\Set{r \ \vert \ r \leq 0}$ then $\alpha = supE_1 = supE_2 = 0 \wedge \alpha \notin E_1 \wedge \alpha \in E_2$

    <br>

    Also, let be, $E:=\Set{ \left(\frac{1}{n}\right)_{n \in \mathbb{N}}}$, then $supE = 1 \in E \wedge infE = 0\notin E$

<br>

## 3.3. Least-upper-bound property.

Now, we have presented order, bounds, minimal bounds and we also provided an example to illustrate that minimal bounds sometimes do not exist. 

Then in this section we are going to present the ***Least-upper-bound property*; this property guarantees the existence of the minimal bound for any bounded and non-empty subset.**

<br>

**Definition**

An ordered set $S$ is said to have the least-upper-bound (LUB) property if for any  upperbounded non-empty subset $E \subset S$ the supremum of $E$ exists in $S$. 

Formally: 

$$ \forall E \subseteq S : (E \neq \varnothing \wedge \exists \alpha \in S : x \leq \alpha \ \ \forall x \in E) \implies \exists \alpha_s = supE : \alpha_s \in S $$


<br>

**Theorem**

Now, the following theorem introduces that the LUB property is a sufficient condition to ensure the existence of an *infimum* for any non-empty lowerbounded subset and also offers a characterization of the object.

Let's consider an ordered set $S$ that satisfies the least-upper-bound property and a non-empty, lowerbounded, subset $B \subseteq S$. 

Then, we call $L$ to the set of all the lowerbounds of $B$ in $S$:

$$L_B := \set{\alpha \in S : \alpha \leq x \ \ \forall x \in B}$$

Since $L_B$ is clearly upperbounded by any item of $B$ and $S$ satisfies the least-upper-bound property, then we can talk about an $\alpha_s \in S : \alpha_s = supL_B$. Observe that:
 
$$ \alpha_s = supL_B \implies \begin{cases} \nexists b \in B: b < \alpha_s  \\ \nexists l \in L_B : l > \alpha_s \end{cases} \implies \alpha_s = infB$$

The first condition tells us that $\alpha_s$ is a lowerbound, the second tells us that there isn't any other lowerbound $l$ bigger than $\alpha_s$, thus, it must be the infimum.





Then, we have:

$$ \exists \alpha_s \in S: \alpha_s = supL_B = infB$$

<br>

# 4. Fields.

## 4.1. Definition and Axioms.

A field is a set $F$ with two operations, called addition, $+$ and multiplication, $·$ which satisfy the following so-called *field axioms*:

- *Closure*: $x + y \wedge x ·y \in F \ \ \forall x,y \in F$
- *Commutativity*: $x+y = y+x \wedge x·y = y·x \ \ \forall x,y \in F$
- *Associativity*: $(x+y)+z = x + (y+z) \wedge (x·y)·z = x·(y·z) \ \ \forall x,y,z \in F$
- *Zero and Unity entities*: $\exists 0,1 \in F :0 \neq 1 \wedge (0 + x = x \wedge 1·x = x \ \ \forall x \in F)$
- *Inverses*: $\forall x \big(\exists (-x) \in F : x + (-x) = 0 \big) \wedge \big(\exists x^{-1} \in F : x·x^{-1}=1\big)$
- *Distributive law*: $x(y+z) = xy + xz \ \ \forall x,y,z \in F$

<br>

It is worth mentioning that it is usual to write:

$$x - y, \frac{x}{y}, x + y + z, xyz, x^2, x^3, 2x, 3x,$$

instead of:

$$x + (-y),\ x \cdot \left(\frac{1}{y}\right),\ (x + y) + z,\ (xy)z,\ xx,\ xxx,\ x + x,\ x + x + x$$

Also, the field axioms clearly hold in $\mathbb{Q}$, the set of all rational numbers, if addition and multiplication have their customary meaning.

<br>

## 4.2. Immediate properties.

Although it is not our purpose to study fields (or any other algebraic structures) in detail, it is worthwhile to prove that some familiar properties of $\mathbb{Q}$ are consequences of the field axioms; once we do this, we will not need to do it again for the real numbers and for the complex numbers. 

- *Cancellation*: 

    $$(x + y = x + z \implies y = z) \wedge (xy = xz \wedge x \neq 0 \implies y=z)$$

    <br>

- *Uniqueness of unity and zero*: 

    $$(x + y = x \implies y = 0) \wedge (xy=x \wedge x \neq 0\implies y=1)$$

    <br>

- *Uniqueness of inverse*:

    $$(x + y = 0 \implies y = -x ) \wedge (xy=1 \wedge x \neq 0\implies y=x^{-1})$$

- $-(-x)= x \wedge \big(x \neq 0 \wedge (x^{-1})^{-1} = x\big)$

<br>

Also, let's observe that:

- $0x = 0$. Immediately, we have that $0x = (0x + 0x) = 0x \implies 0x = 0$ by the axiom above.

    <br>

- *Zero has no divisors*:

    Let's observe that $x \neq 0 \wedge y \neq 0 \implies xy \neq 0$. 
    
    Observe that $\neg(\neg p) \equiv p$ in classic logic, so to demonstrate $p$ let's see that $\neg(\neg p)$ holds or, in other words, let's see that $\neg p$ is not true.

    In our case $p$ is an implication $p:= l \to t \equiv \neg l \vee t \iff \neg p := l \wedge \neg t$, (remember that conjunction and disjunction relate to each other as:  $\neg (p \wedge q) \equiv \neg p \vee \neg q$) thus, we are considering that $\underbrace{(x \neq 0 \wedge y \neq 0)}\_l \wedge \underbrace{xy = 0}\_{\neg t}$ but this is impossible since: $x \neq 0 \wedge xy = 0 \implies y = 0$ (following the axioms described above) entering in contradiction with the premise, thus: $x \neq 0 \wedge y \neq 0 \implies xy \neq 0$. 

    Let's also see that: $p \to q \equiv \neg p \vee q \equiv \neg (\neg q) \vee \neg p \equiv \neg q \to \neg p$, applying that to our rule, we can obtain a subtle better expression of the rule: $xy = 0 \implies x = 0 \vee y = 0$
  
    <br>

- $(-x)y = -(xy) = x(-y)$

    Let's consider the case $(-x)y$, a similar argument can be considered with $x(-y)$. 

    $$(-x)y + xy = (-x + x)y = 0 y = 0$$

    Which means $(-x)y = -xy$ due to the uniqueness of the inverse in $F$.

    <br>

- $(-x)(-y) = xy$

    Let's observe that as we proved before:

    $$(-x)(-y) + (-xy) = (-x)(-y) + (-x)y = (-x)[(-y) + y] = 0$$

    Which means $(-x)(-y) = -(-xy) = xy$.

    <br>

## 4.3. Ordered fields.

### 4.3.1. Definition.

An *ordered field* is a field $F$ which is also an ordered set. This implies defining a relation between the order and the operations of the field. 

Before relating the operations of $F$ to the order, let's expand the definition of the operations in order to give it some geometric intuition. As a brief reminder, $F$ as a field is a triple $(F,+, \ ·)$ where $(F,+),(F,\ ·)$ are abelian groups and $+, \ ·$ are compatible (which means they both satisfy the distributive property). 

Observe that, since $< \ \subset F$ as defined above is a total strict order, we can dispose the elements of $F$ in a line following the precedence that sets $<$. This gives us some geometric intuition about the relation between the operations in the field and the order.

We can understand the $+$ and $·$ operations as the following:

- For each $x \in F$, let's define:

    $$\tau_x : F \to F, \qquad \tau_x(y) = x + y$$

    This is obviously a free (without privilege or fixed points) and transitive (each point is moved to another point) bijection and we will call it **translation of distance $x$**. We can understand it as a movement that sends a point $y$ to the point $x+y$.

    Observe that the operation $+: F \times F  \to F$ and the collection $\Set{\tau\_x}\_{x \in F}$ are equivalent representations of the same composition in $F$, or, in other terms they are equivalent representations of the same composition $(x,y) \mapsto\_+ z$ using both systems.
    
    <br>

- Now, let's consider:

    $$\mu_x : F \to F, \qquad \mu_x(y) = xy$$

    This is a homothety of center $0$ and ratio $x \neq 0$. A *homothety* can be understood as a dilation of the space in which it is defined; it expands/contracts from the center any point by a factor of $x$. Applied to our line intuition it moves a value away by $x$ times its own value; the magnitude of $x$ measures how far it sends the point and its sign the direction of the movement.

    Again, there is a clear equivalence between the family $\Set{\mu\_x}\_{x \in F}$ and the multiplication defined in $F$

    <br>

Thus, having defined these two geometric extrapolations of the operations defined in $F$, let's perform two axiomatic assertions of how the operations behave with $<$.

- **Invariance under translation**: 

    $$ y < z \implies \tau_x(y) < \tau_x(z) \quad \forall x \in F$$

    Observe that by cancellation we obtain the converse, so it is bidirectional invariance.
    
    <br>

- **Invariance under homothety of positive ratio**: 

    $$0 < y \implies 0 < \mu_x(y) \quad \forall x \in F : 0 < x$$

    Observe that this axiom is minimalist since, in combination with the axiom above:

    $$0 < z - y \implies  0 < \mu_x(z - y) = \mu_x(z) - \mu_x(y) \iff \mu_x(y) < \mu_x(z) \quad \forall x \in F : 0 < x$$

    Obtaining the same representation as we had with translations.

    <br>

We also say that $x  \in F$, then:

- $x \text{ is positive } \iff 0 < x$
- $x \text{ is negative } \iff x < 0$

We could think about the positive and negative terms as the direction of the translation we need to apply to $0$ to reach some value. A right translation is a positive sign, while a negative sign means left direction. Observe that there is no direction for the translation that sends $0$ to $0$, so $0$ itself has no sign.

<br>

### 4.3.2. Properties of ordered fields.

All the familiar rules for working with inequalities apply in every ordered field: Multiplication by positive/negative quantities preserves/reverses inequalities, no square is negative, etc. 

The following proposition lists some of these. When treating the following demonstration, remember that $<$ is a total order, which allows us to dispose all the elements of the field in a single line. 

Thus, let's think of a line with the elements of the field $F$ represented on it:

1. **Reflection over the origin**: $x > 0 \iff -x < 0$

    This basically means that the opposite (under addition) of any value always has the opposite sign of the original value, or, in geometric terms, additive opposites always fall on opposite sides of the line of $F$.

    Let's observe that since $0<x \implies \tau_{-x}(0) = -x < 0 = \tau_{-x}(x)$, or saying it in simple words, we need to move $0$ to the left to reach the opposite of a positive value.

    <br>

    Let's also try to demonstrate it by reductio ad absurdum, which is:

    $$\neg [(x > 0)\leftrightarrow (x<0)] \implies \bot$$

    Let's observe that:

    $$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p) \equiv (\neg p \vee q) \wedge (\neg q \vee p)$$

    This way; $\neg(p \leftrightarrow q) \equiv \neg [(\neg p \vee q) \wedge (\neg q \vee p)] \equiv (p \wedge \neg q) \vee (q \wedge \neg p)$

    Now, let's call $p := x > 0$ and $q := -x <0$, then:

    - $p \wedge \neg q$ stands for $x>0 \wedge -x > 0$, but this statement is impossible, considering the first axiom above:

        $$x > 0 \iff 0 = x + (-x) > 0 + (-x) = -x$$

        So $-x > 0 \wedge -x < 0 \implies -x = x = 0$ contradicting the premise that supposes $x$ is greater than $0$.

    - A similar argument can be provided to demonstrate the unavailability of $\neg p \wedge q$ which stands for the statement $x<0 \wedge -x < 0$:

        $$-x < 0 \iff 0 = x - x < x + 0 = x$$

        So we have $x > 0 \wedge x < 0 \implies x = 0$ again.

    This way, $\neg [(x > 0)\leftrightarrow (x<0)] \implies \bot$ and the initial has been demonstrated.

    <br>

2. **Invariance under positive scale**: $x > 0 \wedge y < z \iff xy < xz$

    We already demonstrated this before using the homothety; let's repeat it by multiplication:

    $$y < z \iff 0 = y + (-y) < z + (-y)$$
    
    This way, counting with $x >0$ and using the second axiom of the ordered fields, we have:

    $$0 = x0 < x(z + (-y)) = xz + x(-y) = xz + (-xy) \iff xy < xz$$

    <br>

3. **Reversion under negative scale**: $x < 0 \wedge y < z \implies xy > xz$

    Before diving into this demonstration, let's see something important about homotheties: we have that, since $\mu_x(y) = xy$, then $\mu_{-x}(y) = \mu_x(-y) = - \mu_x(y)$. Meaning that applying a homothety of negative ratio is equivalent to displacing the negative value with a positive ratio, which is the same as applying the homothety of positive ratio in the opposite direction (from the opposite value).

    Thus, we have that:

    $$y<z \wedge x < 0 \iff y<z \wedge 0 < -x \implies \mu_{-x}(y) < \mu_{-x}(z)$$

    Now, observe that the homothety applies the same but in the other side of the line, meaning that the precedence between $y$ and $z$ reverses: $y < z \implies -z < -y$, so:

    $$\mu_{-x}(y) < u_{-x}(z) \iff -\mu_{x}(y) < -\mu_{x}(z)\iff \mu_{x}(z) < \mu_{x}(y)$$

    In summary: $y<z \wedge x < 0 \implies \mu_{x}(z) < \mu_{x}(y)$

    <br>

4. **Positiveness of the squares**: $x \neq 0 \implies x^2 > 0$

    It is natural to think that, if $x$ is positive, a homothety of ratio $x$ will maintain it on the positive side and if $x$ is negative, then $\mu_x$ would be a negative ratio homothety and it would act over $x$ moving it to the point $\mu_{-x}(-x)$ which lives on the opposite side of the origin, so, in any case:
    
    $$0<x^2 = \mu_x(x)$$

    Formally:
    
    $$x \neq 0 \implies \begin{cases}x>0 \implies xx = x^2 > 0 \\ x < 0 \iff -x < 0 \implies (-x)(-x) = xx = x^2 >0 \end{cases}$$

    As a particular case is $1^2 = 1 > 0$

    <br>

5. **Reverse of the inverse**: $0 < x < y \implies 0 < \displaystyle\frac{1}{y} < \frac{1}{x}$
    
    Before diving into this demonstration, let's explore what $\mu_{x^{-1}}$ is for any $ x \neq 0$ from $F$.

    The obvious thing is to think that $\mu_{x^{-1}}$, as defined, is that homothety that sends $x$ to the multiplicative identity $1$, but this is a weak and useless conception. Let's observe that in fact, for $\mu_{x^{-1}}$, $x$ defines the homothety behaviour.

    Think that, whenever you divide a number (multiply it by an inverse of some integer) you are asking how many times this number fits in the divisor. Thus, the homothety $\mu_{x^{-1}}$ redefines the line of $F$ as if $x$ were the number relative to which the rest are defined (which by default is $1$) meaning that $\mu_{x^{-1}}(y)$ tells you how many times $x$ is contained in $y$.

    Having this clear, let's observe that it is obvious that $x < y \implies \mu_{y^{-1}}(1) < \mu_{x^{-1}}(1)$ which is exactly the statement above.

    <br>

    In algebraic terms, we could reason that, since $x \neq y \neq 0 \implies \exists x^{-1},y^{-1} \in F$. Let's also observe that, above, we saw that $1 > 0$, then $1=xx^{-1} \wedge x > 0 \implies x^{-1} > 0 \ \ \forall x \in F : x > 0$ and we can argument that:

    $$0 < x < y \iff 0x^{-1} < xx^{-1} = 1 < yx^{-1} \iff y^{-1}0x^{-1}< y^{-1} <y^{-1}yx^{-1} = x^{-1}$$

    Resulting $0 < x < y \iff 0 < y^{-1} < x^{-1}$

    <br>

# 5. The Real field.

We will now present the core theorem of this chapter.

Until now, we presented fields, order, the combination of both in the ordered field and gave a geometric interpretation of the operations of the field when an order is defined.

Then, we introduced bounds and the $LUB$ property and we saw that, although $\mathbb{Q}$ is an ordered field, it does not satisfy the $LUB$ property, giving the rational line a discontinuous appearance; points to which we can approximate as much as we want but we can't touch.

Thus, let's present $\mathbb{R}$ as an ordered field that satisfies the $LUB$ property.

<br>

## 5.1. Theorem: Existence of $\mathbb{R}$. Dedekind cuts.

**There exists an ordered field $\mathbb{R}$ which has the least-upper-bound property which contains $\mathbb{Q}$ as a subfield.** 

To prove this theorem, we will construct $\mathbb{R}$ from $\mathbb{Q}$. We shall divide the construction into several steps.

<br>

### 5.1.1. Cuts.

The members of $\mathbb{R}$ will be certain subsets of $\mathbb{Q}$, called *cuts*. A cut is, by definition, any proper set $\alpha \subset \mathbb{Q}$ with the following three properties: 

- **A cut is a non-empty strict subset of $\mathbb{Q}$**:

     $\alpha \neq \varnothing \wedge \alpha \neq \mathbb{Q}$

    <br>

- **A cut extends backwards indefinitely**:

    $p \in \alpha \wedge (q \in \mathbb{Q} : q < p) \implies q \in \alpha$. 

    Note that we are saying that being $\alpha$ a cut and $q \notin \alpha$ then $p < q \ \ \forall p \in \alpha$, otherwise, by the line above it would be $q \in \alpha$. In some manner $\alpha$ is a segment inside $\mathbb{Q}$, without gaps. This result also implies the two followings:

    - $p \in \alpha \wedge q \notin \alpha \implies p < q$
    - $p \notin \alpha \wedge p < q \implies q \notin \alpha$

    <br>

- **A cut doesn't contain its own supremum**:

    $p \in \alpha \implies \exists r \in \alpha : p < r$. 

    <br>

Check that these so-called "cuts" are upper-bounded segments with no lower bound, in the sense that the second property of the cuts already tells us that $p \in \alpha \implies \forall q(q < p \implies q \in \alpha)$. This feature allows an order in $\mathbb{R}$ relative to the cuts' members.

<br>

### 5.1.2. $\mathbb{R}$ is an ordered set.
 
Let $\alpha, \beta \subset \mathbb{Q}$ be two cuts, then we define the binary relation $< \ \subset \mathbb{R}^2$:

$$\alpha < \beta \iff \alpha \subset \beta$$

We say that $\alpha$ is a *proper subset* of $\beta$, which means that any item of $\alpha$ is also an item of $\beta$ but at least one item of $\beta$ does not belong to $\alpha$, formally:

$$\alpha \subset \beta \iff \alpha \subseteq \beta \wedge \alpha \neq \beta \iff \forall x (x\in \alpha \implies x \in \beta) \wedge \exists b (b\in \beta \wedge b \notin \alpha)$$

Then, $< \ \subset \mathbb{R}^2$ is a *strict total order*:

- **Irreflexivity**: 

    Since $\alpha = \alpha \ \forall \alpha \in \mathbb{R} \implies \neg ( \alpha < \alpha) \ \forall \alpha \in \mathbb{R}$

    <br>

- **Trichotomy**: 

    Let's note that, be $\alpha,\beta \subset \mathbb{Q}$, then, we can think of one of the following possibilities between $\alpha$ and $\beta$

    - First, consider that $\exists b \in \beta : b \notin \alpha$, then the first corollary of the second property asserts that $\forall a(a \in \alpha \wedge b \notin \alpha \implies a < b)$, applying again the second property of the cuts we get that $(b\in \beta \wedge a < b) \implies a \in \beta \implies \alpha \subset \beta$.

    - A similar argument proves that $\exists a \in \alpha : a \notin \beta \implies \beta \subset \alpha$.

    - Now, obviously, if $\neg(\exists b \in \beta : b \notin \alpha) \wedge \neg(\exists a \in \alpha : a \notin \beta)$, counting with the fact that, following the first property of the cuts, $\alpha,\beta \neq \varnothing$ then only can be $\alpha = \beta$.

    In summary, we've just proved the *trichotomy* property for any pair of cuts in $\mathbb{Q}$.

    <br>

- **Transitivity**:

    Also consider $\alpha,\beta,\gamma \in \mathbb{Q}: \alpha< \beta \wedge \beta < \gamma$ we can directly infer that through the transitivity property of the subsets:

    $$\begin{cases} \alpha < \beta \iff \alpha \subset \beta \\ \beta < \gamma \iff \beta \subset \gamma\end{cases} \implies \alpha \subset \gamma \implies \alpha < \gamma$$


<br>

### 5.1.3. $\mathbb{R}$ satisfies the $LUB$ property.

Remember that the LUB property ensures, for any ordered set $S$ that satisfies it, that any non-empty upper/lower-bounded subset $E \subset S$ has supremum/infimum in $S$.

First, suppose there exists $A \subset \mathbb{R} : A \neq \varnothing$ upperbounded with $\beta \in \mathbb{R}$ an upperbound of $A$, let's see that we can find a supremum for it. 

Now we define as:

$$\gamma := \bigcup_{\alpha \in A} \alpha = \Set{p \in \mathbb{Q} \ \vert \ \exists \alpha \in A : p \in \alpha}$$

We will see that $\gamma \in \mathbb{R}$, this is, that as a subset it is also a cut, since it satisfies the three properties mentioned above. Then we will demonstrate that $\gamma$ is an upperbound of $A$ and lastly that is the least upperbound and thus, the supremum of $A$.

First, let's see that $\gamma \in \mathbb{R}$:

1. Then, since $A \neq \varnothing \implies \exists \alpha_0 \in A : \alpha_0 \neq \varnothing$ thus $\exists a \in \alpha_0 \subset \gamma \implies \gamma \neq \varnothing$ 

    Now observe that $\beta \in \mathbb{R}$ is an upperbound of $A$. Since $\beta$ is a cut, it satisfies that it encompasses everything to its left, meaning $\forall \alpha (\alpha \in A \implies \alpha < \beta \implies \alpha \subset \beta)$; we say that it is closed to its left, thus it is clear that $\gamma \subset \beta \subset \mathbb{Q}$ and $\gamma \neq \mathbb{Q}$

    <br>

2. Let's consider now $p \in \gamma$ and $q \in \mathbb{Q} : q < p$, immediately we have that 

    $$ p \in \gamma \implies \exists \alpha \in A : p \in \alpha$$

    Since $\alpha \in \mathbb{R}$ then $q < p \implies q \in \alpha \implies q \in \gamma$

    <br>

3. Following the same logic, taking $p \in \gamma$ as before, $p \in \alpha \implies \exists r \in \alpha : p < r$, observe that $r \in \gamma$ for the same reason as $p$, so $\exists r \in \gamma : p < r$

    <br>

Having verified that $\gamma$ is a cut, then since $\forall \alpha(\alpha \in A \implies \alpha \subset \gamma \implies \alpha < \gamma)$ so $\gamma$ is an upperbound of $A$. 

For $\gamma = supA$ it also has to be the least upperbound; formally, $\gamma$ precedes any upperbound of $A$:

$$\forall \delta \in \mathbb{R} \quad ([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta)$$

Then let's proceed by reductio ad absurdum and consider the negation:

$$\neg \forall \delta([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta) \equiv \exists \delta : \neg([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta)$$

Let's remember that, in classical logic, it is: 

$$p \to q \equiv \neg p \vee q \iff \neg(p \to q) \equiv \neg (\neg p \vee q) \equiv p \wedge \neg q$$

Thus exchanging $p = (\alpha < \delta \quad \forall \alpha \in A)$ and $q= \gamma < \delta$ we have that the negation is

$$\exists \delta \in \mathbb{R} : [(\alpha < \delta \quad \forall \alpha \in A) \wedge (\delta < \gamma)]$$

Which means basically that there exists an upperbound that precedes $\gamma$. Thus, let's consider $\delta$ as above: $\exists \delta \in \mathbb{R} : \delta < \gamma \wedge (\alpha < \delta \ \ \forall \alpha \in A)$. Observe that $\delta < \gamma \implies \delta \neq \gamma$ which means that $\exists \alpha \in \gamma : \alpha \nsubseteq \delta \implies \delta < \alpha$ (due to the trichotomy of the order), thus $\delta$ would not be an upperbound contradicting the initial assumption. 

So, by reductio ad absurdum, $\gamma$ has to be the least upper bound; $\gamma = sup A$.

<br>

Thus, we've seen that $\mathbb{R}$ is an ordered set that satisfies $LUB$ property, let's see also that with proper definitions, it can also have field structure, becoming then a complete ordered field.

<br>

### 5.1.4. Addition in $\mathbb{R}$.

If $\alpha, \beta \in \mathbb{R}$ we define: $\alpha + \beta := \Set{a+b \ \vert \ a \in \alpha \wedge b \in \beta}$. We also define $0^\ast \in \mathbb{R}$ as $0^* := \Set{ q \in \mathbb{Q} \ \vert \ q < 0}$, observe that is clear that this last set is a cut.

Now, we verify that the addition's axioms for a field hold in $\mathbb{R}$, with $0^*$ playing the role of $0$. In orther terms, $(\mathbb{R},+)$ is an abelian group:

- **Closure**: $\alpha + \beta \in \mathbb{R} \ \ \forall \alpha, \beta \in \mathbb{R}$. We have to demonstrate that $\alpha + \beta$ is a cut.

    Let's demonstrate that $\alpha + \beta$ satisfies the three properties of a cut. 

    1. $\alpha, \beta \neq \varnothing \implies \alpha + \beta \neq \varnothing$. 
    
        Also suppose that $p,q \in \mathbb{Q}$ are the upperbounds of $\alpha, \beta \in \mathbb{R}$ respectively (we can assume their existence since both of them are cuts and thus proper subsets of $\mathbb{Q}$ so there are indeed elements of $\mathbb{Q}$ out of each subset), then it is clear that $p + q \notin \alpha + \beta \implies \alpha + \beta \neq \mathbb{Q}$. 
        
        Observe that there is something worth saying about upperbounds when speaking about cuts. By definition, $p$ is an upperbound of $X$ iff $x \leq p \ \ \forall x \in X$, but if $X$ were a cut, by the third property if $\exists x_0 : p = x_0 \in X \implies \exists r \in X : p < r$ and $p$ would not be an upperbound; thus, when talking about cuts, all upperbounds are always strict upperbounds, the definition of upperbounds always collapses to $x < p \ \ \forall x \in X$ and the cut does not contain it.

        <br>

    2. $p \in \alpha + \beta \wedge (q \in \mathbb{Q} : q < p) \implies q \in \alpha + \beta $ 

        Write $p = a + b$, since $q < p = a + b \implies q - a < b \in \beta$ and thus we get that $q = (q - a) + a \in \alpha + \beta$.

        <br>

    3. $p \in \alpha + \beta \implies \exists q \in \alpha + \beta : p < q$

        This result is almost immediate since if $p = a + b$ then, exists $a' \in \alpha, b' \in \beta$ verifying both $a < a' \wedge b < b'$, thus calling $q = a' + b'$ clearly is $q \in \alpha + \beta : p < q$

        <br>

- **Commutativity**: $\alpha + \beta = \beta + \alpha \ \ \forall \alpha, \beta \in \mathbb{R}$, it gets immediately derived from commutativity in $\mathbb{Q}$.

    <br>

- **Associativity**: $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma \ \ \forall \alpha, \beta, \gamma \in \mathbb{R}$.

    Let's look at it closely; we have that the objects in $\mathbb{R}$ can be understood as:

    $$\alpha + (\beta + \gamma) := \Set{a + p \mid a \in \alpha \wedge p \in \beta + \gamma}$$

    $$(\alpha + \beta) + \gamma := \Set{q + c \mid q \in \alpha + \beta \wedge c \in \gamma}$$

    Observe that also $p \in \beta + \gamma \implies \exists (b , c) \in \beta \times \gamma : p = b + c$ and we can rewrite the expression $a + p = a + (b + c)$, but in $\mathbb{Q}$ is $a + (b + c) = (a + b) + c$ which means that the object $a+p$ lives in the counterpart. A similar argument gives us the reciprocal inclusion, ultimately standing that: $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma$.

    <br>

- **Identity**: 

    Let's remember that we called $0^\ast:= \Set{q \in \mathbb{Q} \mid q < 0}$, then let's take

    $$t \in \alpha + 0^\ast \implies \exists a \in \alpha \wedge \exists q < 0 : t = a + q$$

    Then, if we consider some other $b \in \alpha : a < b$ (whose existence is guaranteed by the third property of the cuts) then, following the axioms for ordered fields, since $q < 0$, is $t = a + q < a + 0 < b$ and then is $t < b \in \alpha \implies t \in \alpha$ for the second property of the cuts.

    Thus, $\alpha + 0^\ast \leq \alpha$.

    Let's also consider $a \in \alpha$ and, again by the third property of the cuts, take $b \in \alpha : a < b$, observe that $a-b < 0 \implies a-b \in 0^\ast$, and is $ a = b + (a - b) \in \alpha + 0^\ast$.

    Thus, $\alpha \leq \alpha + 0^\ast$, meaning that $\alpha = \alpha + 0^\ast$

    Lastly, by the commutativity property presented before:

    $$0^\ast + \alpha = \alpha + 0^\ast = \alpha \quad \forall \alpha \in \mathbb{R}$$

    <br>

- **Inverse**:

    Fix some $\alpha \in \mathbb{R}$. Then, consider the set:

    $$\beta := \Set{p \in \mathbb{Q} \mid \exists r>0 : -p -r \notin \alpha}$$

    Observe that we are not considering those $p$ whose opposite $-p$ is strictly outside $\alpha$ (this would be $a < -p \ \ \forall a \in \alpha$) but only those $p$ whose opposite has a constant positive gap between themselves and any other element of $\alpha$ abstracted in $r > 0$. Specifically, we are considering the segment symmetric (with respect to the origin) in the rational line to the one that is strictly out by a positive gap from $\alpha$.

    Note that $\beta$ as defined is smaller than $A := \Set{p \in \mathbb{Q} \mid -p \notin \alpha}$ since, $A$ admits a frontier element $p$ for which the elements of $a \in \alpha$ can get as close as wanted. However, with $-p -r \notin \alpha$ the difference between $-p -r$ and $\alpha$, again, can be as small as wanted, but the distance between $-p$ and $\alpha$ can't be smaller than $r$. That gap will always exists between $-p$ and any other element in $\alpha$ so $\beta$'s elements are deeper in $\mathbb{Q} \setminus \alpha$.
    
    Let's see that $\beta \in \mathbb{R}$ and $\alpha + \beta = 0^*$  

    - First, $\beta \in \mathbb{R}$, this means that $\beta \neq \varnothing$ and $\beta \neq \mathbb{Q}$. In order to solve this, let's recover our conception of $\beta$ as the symmetric segment to that one that is strictly out from $\alpha$ by a positive gap.

        <br>

        Thus, first, let's simply consider an element out from $\alpha$. 
        
        Since $\alpha \in \mathbb{R} \implies \alpha \subset \mathbb{Q} \implies \exists q \in \mathbb{Q} \setminus \alpha$, then, consider now $p \in \mathbb{Q} : q < p$ an observe that $q$ is what you get when translate back $p$ the distance $r = p-q>0$, formally we write:
        
        $$q = p -(p - q) = -(-p) -r \in \alpha \implies -p \in \beta$$

        

        This way, we get that $\beta \neq \varnothing$.

        <br>

        Now, consider some $q \in \alpha$, no matters how much translate $q$ back, it always will be in the segment $\alpha$ so is not in $-\alpha$, remember that $\beta$ is composed from the negative of those numbers that can be push back a bit and still out of $\alpha$, so this intuition works. 
        
        Formally $q - r < q \quad \forall r>0$, thus $q \in \alpha \implies q-r \in \alpha \quad \forall r>0$ by the second property of the cuts and this is logically the same that: $\nexists r >0 : -(-q) -r \in \alpha \implies -q \notin \beta$

        So $\beta \neq \mathbb{Q}$ neither.

        <br>

    - Now, the second property, let's observe that, if we consider some $p \in \beta$ and $q \in \mathbb{Q} : q < p$, then, assuming $r : -p -r \notin \alpha$:

        $$q < p \iff -p < -q \iff -p -r < -q -r \implies -q -r \notin \alpha$$

        Since $\alpha$ is a cut, the premise and the second property in $\alpha$ give us the last implication, (note that, otherwise, $-p -r \in \alpha$ too and $p \notin \beta$). Thus $q \in \beta$.

        <br>

    - Lastly, the third property, consider some $p \in \beta$, then, again taking $r : -p -r \notin \alpha$

        $$-p -r = -(p + \frac{1}{2}r) - \frac{1}{2} r \notin \alpha \implies p + \frac{1}{2}r \in \beta$$

        For some $r>0$.

        <br>
    Now, let's see that:

    - $\alpha + \beta \subset 0^*$: 
    
        First, observe that $b \in \beta \implies \exists r > 0 : -b -r \notin \alpha$ and for the second property of the cuts: $a < -b -r \quad \forall a \in \alpha \iff a + b < -r <0 \quad \forall a \in \alpha$

        <br>

    - $0^* \subset \alpha + \beta$: 

        Consider some $p \in 0^*$ and $q = - \frac{p}{2} > 0$.

        Observe, that exists some integer that makes $q$ to cross $\alpha$ as a frontier, formally: 
        
        $$z \in \mathbb{Z} : zq \in \alpha \wedge (z+1)q \notin \alpha$$
        
        Check that, for this $z$, we have that, being $t = - (z+2)q$, then:
        
        $$-t - q = (z+1)q \implies t \in \beta$$

        Observe that, then $p = zq + t$.

        <br>

    Thus, $\beta = - \alpha$

    <br>

With this we already proved that $(\mathbb{R},+)$ is an abelian group. Observe now that this addition can be considered a translation; $\alpha + \beta$ is the set that considers the rational addition between any item of $\alpha$ and $\beta$. Since $\mathbb{Q}$ is an ordered field itself, $+ : \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q}$ is a translation, thus the combination $a + b$ is a translation that displaces $a$ a distance $b$ on the rational line. 

Observe now that, in $\mathbb{R}$ we have the $LUB$ property which allows us to consider, for any non-empty and upperbounded subset $A \subset \mathbb{R}$, a minimal upperbound. Also, since any cut $\alpha \in \mathbb{R}$ can be treated as a subset itself (of $\mathbb{R}$, specifically, that subset that contains all the cuts that precede it) we can consider a supremum in $\mathbb{R}$ for any element of $\alpha \in \mathbb{R}$, we can denote it as $sup(\alpha)$. 

Observe then that $\alpha + \beta$ has its own supremum, $sup(\alpha + \beta)$ which is further than any $a+b: (a,b) \in \alpha \times \beta$ in the rational line, and thus than $sup(\alpha)$ or $sup(\beta)$; essentially $sup(\alpha + \beta) = sup(\alpha) + sup(\beta)$. This is how, geometrically, the addition in $\mathbb{R}$ acquires the form of a translation through the translation conception defined in the ordered field $\mathbb{Q}$.

In summary, if $\alpha \in \mathbb{R}$ then any $a \in \alpha$ is not further than $sup(\alpha)$ and $\tau_b(a) = a + b$ is not further than $sup(\alpha + \beta)$. Essentially this allows us to extrapolate that $\alpha < \beta \implies \alpha + \gamma < \beta + \gamma \quad \forall \gamma \in \mathbb{R}$, so the total strict order $< \ \subset \mathbb{R}^2$ has an invariant through the translations in $\mathbb{R}$.

<br>

### 5.1.5. Multiplication in $\mathbb{R}$.

Let's take the following operation:

$$· : \mathbb{R}^+ \times \mathbb{R}^+ \to \mathbb{R}^+$$
$$(\alpha, \beta) \mapsto \alpha \beta $$

Being: $\alpha \beta := \Set{ p \in \mathbb{Q} \mid \exists (a,b) \in \alpha^+ \times \beta^+ : p \leq ab}$, let's see first that, as defined, $(\mathbb{R}^+, ·)$ is also an abelian group.

From all below, consider $\alpha, \beta \in \mathbb{R}^+$

- **First, $\alpha \beta \in \mathbb{R}$**:

    1. $\alpha \beta \neq \varnothing \wedge \alpha \beta \subset \mathbb{Q}$

        - $\alpha \beta \neq \varnothing$, consider that $\alpha, \beta \in \mathbb{R} \implies \alpha, \beta \neq \varnothing$, let's be $a \in \alpha, b \in \beta$, then $ab -1 \in \alpha \beta$ so this last is not empty.

            <br>

        - $\alpha \beta \neq \mathbb{Q}$, consider now some positive $p \notin \alpha$ and $q \notin \beta$, and observe that 
        
            $$t = (p + 1)(q+1) > ab \quad \forall (a,b) \in \alpha^+ \times \beta^+ \implies t \notin \alpha \beta$$

            <br>

        <br>    

    2. $p \in \alpha \beta \wedge q \in \mathbb{Q} : q < p \implies q \in \alpha \beta$

        Immediately: $p \in \alpha \beta \implies \exists (a,b) \in \alpha^+ \times \beta^+ : p \leq ab \implies q < p \leq ab \implies q \in \alpha \beta$.

        <br>

    3. $ p \in \alpha \beta \implies \exists r \in \alpha \beta : p<r$

        Again, observe that $a \in \alpha \implies \exists r_a \in \alpha : a < r_a$, and the same applies for $b \in \beta$ thus, considering some $p \leq ab < r_ar_b$, observe that this means that $ab \in \alpha \beta$ and also, applying the same argument $r_ar_b \in \alpha \beta$ thus the third property is true, because we can always find an element bigger than other one in $\alpha \beta$

<br>

- **Associativity**; Immediate from associativity in $\mathbb{Q}$
- **Commutativity**; Immediate from commutativity in $\mathbb{Q}$
- **Identitity**; Observe that: $1^\ast:= \Set{t \in \mathbb{Q} \mid t < 1} \subset \mathbb{Q}$, then, consider $\alpha^+ \in \mathbb{R}^+$:

    - $p·t \leq p \quad \forall (p,t) \in \alpha^+ \times 1^\ast \implies p \ · t \in \alpha \implies \alpha · 1^\ast \subset \alpha$, 
    - By the second properties of the cuts:
    
        $$\forall p \in \alpha \ \exists r \in \alpha : p<r \implies p = r \ · \frac{p}{r} \in \alpha \ · 1^\ast \implies \alpha \subset \alpha \ · 1^*$$
    
    Thus, $\alpha \ · 1^* = \alpha$ and $1^\ast$ is our identity.

    <br>

- **Inverse**; Take $\alpha^{-1} := \Set{p \mid p < \frac{1}{y} : (y \notin \alpha \wedge y > 0)}$, observe that, essentially we are saying that the inverse of any cut is any rational inverses behind the non-cut part. Observe that intuitively this is like say that the inverse cut is to consider the inverse of the frontier but this frontier does not exists in $\mathbb{Q}$, thus, we don't have access to it so we talk about what isn't inside the cut.

    Let's see that as defined, $\alpha^{-1}$ is a cut and it satisfyies the role of the inverse in $(\mathbb{R}^+,\ ·)$.

    1. Obviously $\alpha^{-1} \neq \varnothing$ since $\alpha \neq \mathbb{Q}$ and also $\alpha^{-1} \neq \mathbb{Q}$.

    2. Take $p \in \alpha^{-1}$ and $q<p<\frac{1}{y} \implies q \in \alpha^{-1}$.
    3. Take $p \in \alpha^{-1} \implies \exists y \notin \alpha : p < \frac{1}{y}$, then take some $q > y \implies p < \frac{1}{q}< \frac{1}{y} :q,y \notin \alpha$, meaning that $r = 1/q \in \alpha^{-1}$ verifying $p<r$

    Thus, $\alpha^{-1}$ is a cut, let's now see that $\alpha \alpha^{-1} = 1^\ast$:

    - $\alpha \alpha^{-1} \subset 1^\ast$: 
    
        Let's observe that: $\alpha \alpha^{-1}= \Set{p \mid \exists (a,t) \in \alpha^+ \times {\alpha^{-1}}^+ : p \leq at}$, but let's observe: 
        
        $$t \in \alpha^{-1} \implies \exists (y \notin \alpha \wedge y>0) : t < \frac{1}{y} \implies at < \frac{a}{y} < 1$$
        
        Since $a<y$ for being $y \notin \alpha$.

        <br>

    - $1^* \subset \alpha \alpha^{-1}$: 
    
        Let's take note that, demonstrate this inclusion implies to demonstrate that, given any number $p < 1$ we can closer than $p$ to $1$ by finding and multiplicating the elements of a proper pair $(a,t) \in \alpha^+ \times {\alpha^{-1}}^+$.

        First let's take some $p < 1 \implies \exists q > 0 \in \mathbb{Q} : p + q = 1$, so $q$ is the "distance" between $p$ and $1$; let's now take some $\alpha >1$ (we can assume this without losing generality since otherwise it would be $\alpha^{-1}>1$) and consider some $a \notin \alpha : a - q \in \alpha$, observe $a \notin \alpha \implies \frac{1}{a} \in \alpha^{-1}$, thus:

        $$1 > (a-q)\frac{1}{a} = 1 - \frac{q}{a} > 1 - q = p$$

        Observe that $\alpha > 1 \implies a >1 \implies q > \frac{q}{a}$.

        <br>

    At the end, we have that $1^* = \alpha \alpha^{-1}$.

    <br>

Now that we proved that $(\mathbb{R}^+,\ ·)$ is an abelian group, let's extend to $\mathbb{R}$ this same operation.

Observe that $\alpha 0^ = 0^\ast$ and the argument is basically the same we provided with $1^\ast$:

- $\alpha \ · 0^\ast \subset 0^\ast$:

    Consider some $t \in 0^\ast$ and some $p \in \alpha^+ \implies p>0$, then $pt < 0 \in 0^\ast$

    <br>

- $0^\ast \subset \alpha \ · 0^\ast$

    Observe that $\forall p \in 0^\ast \implies p \in \alpha^+$

    <br>

Ultimately, we define:

$$\alpha \beta = \begin{cases} (- \alpha)(- \beta) \quad \alpha < 0^\ast, \beta < 0^\ast \\ -[(-\alpha)\beta] \quad \alpha < 0^\ast, \beta > 0^\ast \\-[\alpha (-\beta)] \quad \alpha > 0^\ast, \beta < 0^\ast\end{cases}$$

We just translate negative multiplications to the negative segment of a positive multiplication. 

Clearly $(\mathbb{R} \setminus \Set{0}, \ ·)$ is an abelian group.

<br>
    
Lastly, $(\mathbb{R},  +)$ and $(\mathbb{R}, \ ·)$ are compatible, this is a result that can be obtained by cases and it comes directly from the distributive law in $\mathbb{Q}$:

$$\alpha(\beta + \gamma) = \alpha \beta + \alpha \gamma$$

<br>

### 5.1.6. $\mathbb{Q}$ in $\mathbb{R}$.

Let's see that $\mathbb{Q} \subset \mathbb{R}$. It is worth making a previous commentary about this statement. Formally it is an abuse of language: in strict terms, $\mathbb{Q}$ is not part of $\mathbb{R}$ because their elements are simply not the same.

Mathematically, we don't care about what things are made of; mathematicians often don't know what they are talking about, but they are pretty sure about what they are saying, which is not the same. In other words, what we care about is how elements relate between them. Thus, two structures whose elements behave exactly the same way are externally indistinguishable and, for any structural purpose, exchangeable.

The object that allows us to identify two equivalent structures is the *isomorphism*, in this case the *field isomorphism*. This is a bijection that allows us to translate one structure to another, identifying pairs of elements from both sets and implicating rules that preserve the behavior through the image of the isomorphism.

Let's consider $\varphi:\mathbb{Q}\xrightarrow{\ \sim\ }\mathbb{Q}^\ast$ such: $q \mapsto q^\ast = \Set{p \mid  p < q}$, is clear that $q^\ast \in \mathbb{R}$ is the cut formed by the behind of $q$.

First, let see that $\varphi$, as defined is a *field homomorphism*:

1. $\varphi(p+q) = \varphi(p) + \varphi(q)$

2. $\varphi(pq) = \varphi(p) \varphi(q)$

    <br>

Observe that this much is true and is already proved above, that the segment of the addition is the addition of the segments and the product of the segment is the segment of the product.

Observe also that each cut $q^\ast \in \mathbb{Q}^\ast$ has a preimage through $\varphi$ and vice versa, so $\varphi$ is bijective and is a field isomorphism, implying that $p\neq q \implies \varphi(p) \neq \varphi(q)$.

Lastly, consider some $p, q \in \mathbb{Q} : p < q$, we already know that $\varphi(p) \neq \varphi(q)$ but also observe that it is pretty clear: $\forall t \big(t \in \varphi(p) \implies t <p < q \implies t \in \varphi(q)\big) \implies \varphi(p) < \varphi(q)$, a similar argument proves $\varphi(p) < \varphi(q) \implies p<q$, thus $p<q \iff \varphi(p) < \varphi(q)$.

So $\varphi$ is an *isomorphism of ordered fields* meaning that $\mathbb{Q} \simeq \mathbb{Q}^\ast \subset \mathbb{R}$ and we can exchange $q$ and $q^\ast$ in the real number context.

<br>

With this, we conclude the presentation of $\mathbb{R}$ as a strict ordered field that also satisfies $LUB$ property, we say then that $\mathbb{R}$ is *ordered* and *complete*.

In fact, although this result will not be proved: any two ordered fields with
the least-upper-bound property are isomorphic, meaning that **$\mathbb{R}$ is THE ordered and complete field**.

<br>

## 5.2. Important Properties from the $\mathbb{R}$ field.

### 5.2.1. Archimedean property of $\mathbb{R}$.

We've found this property before in the construction of $\mathbb{R}$ without properly defining it. This property says that every quantity in $\mathbb{R}$ is reachable by considering a positive value a finite number of times. It is a powerful statement since it basically says that every point on the real line is reachable by any positive value repeated a finite number of times. 

This can be explained in other terms: the archimedean property says that $\mathbb{N}$ is unbounded on $\mathbb{R}$, there is always a natural number that can reach and surpass any real quantity. 

Meaning that $\mathbb{R}$ has no "infinitely large" or "infinitely small" elements; no matter how small a positive number $x$ you pick and no matter how large a target $y$, you can always reach (and surpass) $y$ by adding $x$ to itself enough times. Formally:

$$\forall x\forall y (0 < x \implies  \exists n \in \mathbb{N} : y < nx)$$

By reductio ad absurdum: 

Let's observe that:

$$\neg \forall x\forall y (0 < x \implies  \exists n \in \mathbb{N} : y < nx) \equiv \exists x\exists y (0 < x \wedge  y > nx \quad \forall n \in \mathbb{N})$$


Thus, let's fix $x > 0$ and consider the set $A:=\Set{nx \ \vert \ n \in \mathbb{N}}$ upperbounded by $y$ as the statement says. By the $LUB$ property in $\mathbb{R}$ we can consider $\alpha = sup(A) \in \mathbb{R}$. 

This way, we have that:

$$\alpha - x < \alpha \implies  \exists m \in \mathbb{N} : \alpha - x < mx \iff \alpha < (m+1)x \in A \implies \alpha \neq sup(A)$$

<br>

### 5.2.2. $\mathbb{Q}$ is dense in $\mathbb{R}$

The density of $\mathbb{Q}$ in $\mathbb{R}$ stablish that between two elements of $\mathbb{R}$ a rational always can be found, formally:

$$\forall x, y \in \mathbb{R} : x < y \implies \exists q \in \mathbb{Q} : x < q < y$$

Let's observe that, considering $x \in \mathbb{R}\setminus \mathbb{Q}$, then taking some $q \in y \setminus x$ we have that is $x < q < y$, but observe that this argument doesn't apply to every real, the exception is made when is a rational real:

$$x \in \mathbb{Q} \subset \mathbb{R} \implies x \in y \setminus x$$

The existence of another $q \neq x : x < q < y$ needs to be proved.

To demonstrate it, let's think about $x, y \in \mathbb{R} :x < y$, thus $ 0 < y - x$ so for $1 \in \mathbb{R}$, the archimedean property furnishes the result: $1 < n(y-x)$.

Also, considering $z_1,z_2 \in \mathbb{R}^+ \implies \exists t_1,t_2 \in \mathbb{N}: nx < t_1z_1 \wedge -nx < t_2z_2$. Then, calling $m_i = t_iz_i$ is:

$$-m_2 < nx < m_1$$

We can nail $[-m_2,m_1] \cap \mathbb{Z}$ until find an $m \in \mathbb{N} : m-1 \leq nx < m$, in summary:

$$\begin{cases} 1 < n(y-x)  \iff 1 + nx < y \\ m - 1 \leq nx < m \iff m \leq 1 +nx < m +1  \end{cases} \implies nx < m \leq 1 + nx < ny$$

And thus:

$$x < \frac{m}{n} < y$$

Observe that this means we can approximate any real through rational values. Think that for any $x \in \mathbb{R}$ we can think of $x < x +1 \implies \exists y \in \mathbb{Q} : x < y < x + 1$, but since $\mathbb{Q} \subset \mathbb{R} \implies y \in \mathbb{R}$ and the result tells us that there exists another $q \in \mathbb{Q} : x < q < y$ and so on.

<br>

### 5.2.3. *nth* roots of positive reals.

As we said before, in $\mathbb{Q}$ there isn't any $q \in \mathbb{Q} : q^2 = 2$, we are now going to see that this problem is handled in $\mathbb{R}$.

Specifically, we are going to see that for any positive real and any positive integer exists a unique positive real such $y^n = x$, formally:

$$\forall (x,n) \in \mathbb{R}_{>0} \times  \mathbb{Z}_{>0} \ \exists ! y \in \mathbb{R}_{>0} : y^n = x$$

We say that $y$ is the $n$-th root of $x$ and we denote it as $y = \sqrt[n]{x} = x^{\frac{1}{n}}$.

<br>

That there is at most one such $y \in \mathbb{R}$ is clear, since $\forall y\forall x(0 < y < x \implies y^n < x ^n)$, remember that strict total order $< \ \subset \mathbb{R}^2$ requires irreflexivity, meaning that $y^n < x^n \implies y^n \neq x^n$, obviously.

<br>

Now, let's demonstrate the existence of such a number. Consider now the following set:

$$E := \Set{t \in \mathbb{R} \mid t^n < x}$$

This set is not-empty and has an upperbound:

- First, is not empty, consider $t = \frac{x}{1+x} \implies 0 < t < 1$. Now, let's reason by induction over $n$:

    - If $n = 2$, then, by $4.3.2-(2)$ is $0 < t < 1 \implies 0 < t^2 < t$.
    - Now, considered true by some $n$, again: $0 < t^n < 1 \implies 0 < t^{n+1} < t$

    Thus $t^n < t \ \ \forall n \in \mathbb{N}$ of course, is also $t < x$ as defined so $t \in E$.

    <br>

- Second, it is upperbounded; consider $t \in \mathbb{R} : 1 + x < t \implies x < t \leq t^n$ and $1+x$ is an upperbound of $E$. Thus, we can consider the $y=sup(E)$ verifying necessarily $y^n = x$. (Although the proof of this last affirmation is not provided, as it is too complicated, the result, as presented, is intuitively enough to be accepted).

    <br>

Let's observe that $(ab)^{\frac{1}{n}} = a^{\frac{1}{n}}b^{\frac{1}{n}}$, take $\alpha = a^{\frac{1}{n}} \iff \alpha ^n = (a^{\frac{1}{n}})^n = a$. Thus,  

$$(ab)^{\frac{1}{n}} = ((\alpha \beta)^n)^{\frac{1}{n}} = \alpha \beta = a^{\frac{1}{n}}b^{\frac{1}{n}}$$

The step $\alpha^n \beta^n = (\alpha \beta)^n$ is taken by the commutative property in the abelian group $(\mathbb{R}, \ ·)$.

<br>

## 5.3. Brief summary about $\mathbb{R}$.

Let's make a brief recapitulation about what numbers are and how the conception of number changes when we talk about $\mathbb{R}$.

Maths are abstractions of natural concepts with which we coexist; specifically, numbers in a traditional way represent *quantities*. $\mathbb{N}$ sets up something we call unity or first element (which can be $0$ or $1$ depending on the convention; generally, $0$ is not a natural number) and defines the rest of its elements by *succession*; thus, the place a number occupies in the iterative succession line represents how many times this identity is in this element, which defines its value in an arithmetic sense; $n \in \mathbb{N}$ is literally $n$ times $1$.

Then, the $0$ represents the absence of quantity and the negative numbers the debt, and later the fractions change the unity value (from which we extract the value of the rest of the elements as we saw above) allowing access to intermediate values in the succession line. Thus, $\mathbb{Z}$ and $\mathbb{Q}$ expand the quantity concept but we are still talking about quantities. 

We already explained this in other terms by announcing the $LUB$ property, but we can now bring another perspective conceptually more illustrative of the inadequacy of $\mathbb{Q}$. Since $\mathbb{Q}$ considers quantities it makes its items totally disconnected, meaning that we can make a split of $\mathbb{Q}$ by defining: 

$$U=\{q\in\mathbb{Q}: q^2<2\ \vee \ q<0\},\qquad V=\{q\in\mathbb{Q}: q>0 \vee \ q^2>2\}$$

Observe that $U \cup V = \mathbb{Q}$ and neither of the two contains $p : p^2 = 2$; apparently this gap is never filled in $\mathbb{Q}$, as if there were no bridge between $U$ and $V$ that, however, builds $\mathbb{Q}$. This is a rational question involving rationals without a rational response, meaning that $\mathbb{Q}$ can't represent incommensurable entities despite being "surrounded" by them, and it is worth emphasizing the term "surrounded" because a lot of rationals get squeezed in the neighborhood of $p$ without ever reaching it. These incommensurable entities manifest themselves as non-reachable frontiers to which we can approximate as much as we want.

$\mathbb{R}$ solves this by no longer considering its elements as numbers or quantities, but as *positions* in a line which, by definition, is continuous and any position (any "point") in the line is defined. In some informal sense, this real line is now "complete". 

This is achieved by changing $\mathbb{Q}$'s architecture; technically, $\mathbb{R}$ and $\mathbb{Q}$ share the same substratum, rational numbers, but elements of $\mathbb{R}$ are subsets that satisfy certain properties; segments that "cut" the so-called line at any point. The $LUB$ property offers a guarantee that any bounded aggregation of these segments has a supremum, meaning that any subset that gets near to these frontiers not defined in $\mathbb{Q}$ has a supremum in $\mathbb{R}$ in which the frontier, the non-measurable value, can be instantiated, filling these gaps from $\mathbb{Q}$.

The natural interpretation of a *cut* is an object that points to a position in $\mathbb{R}$ cutting the line in two; this way, this addressed position is characterized by what it has behind (which automatically characterizes what it has in front). So the elements of $\mathbb{R}$ are positions in the line concretized by what surrounds them. This is why, in $4.3.1$ we care about presenting operations of an ordered field with a geometric nuance, because in $\mathbb{R}$ we do operate with positions in a geometric sense; the only kind of "quantities" we could consider in $\mathbb{R}$ are those which can be identified with rational elements as we saw in $5.1.6$.

<br>

Lastly, let's see what the three properties presented in $5.2$ tell us about $\mathbb{R}$:

- **Archimedean Property** states that any position in the line is reachable or surpassable by translating a positive value a finite number of times.

- **$\mathbb{Q}$ density** tells us that we can get close enough to any position in $\mathbb{R}$ with a rational approach.

- **nth-roots of positive real values**; tell us that any positive position is reachable by dilating some positive value a finite number of times.

    <br>

# 6. The extended Real Number System.

## 6.1. Definition.

The extended real number system consists of forming the set $\overline{\mathbb{R}} := \Set{\mathbb{R},+\infty,-\infty}$ defining:

$$-\infty < x < +\infty \quad \forall x \in \mathbb{R}$$

This way, observe that we have defined $-\infty, +\infty$ as lower/upper bounds of any subset of $\mathbb{R}$, **thus any subset in $\mathbb{R}$ is now bounded in $\overline{\mathbb{R}}$ and has a least upper bound**: for example, $E$ is a nonempty set of real numbers which is not bounded above in $\mathbb{R}$, then $\sup E = +\infty$ in the extended real number system. 

<br>

## 6.2. Operations in $\overline{\mathbb{R}}$.

**The extended real number system does not form a field**, but it is customary
to make the following conventions (in the following cases $\infty = +/- \infty$): 

$$\begin{cases} x +/- + \infty = + \infty \\ x +/- - \infty = - \infty \\ \displaystyle\frac{x}{+\infty} = \displaystyle\frac{x}{-\infty} = 0 \\ x \ · + \infty = +\infty \wedge x \ · -\infty = - \infty \quad x > 0 \\ x \ · + \infty = -\infty \wedge x \ · -\infty = + \infty \quad x < 0 \end{cases}$$

In this context, we say that real numbers are *finite*, while $+\infty,-\infty$ are both, *infinite*.

<br>

# 7. Summary. Analysis.

Until now, in basic terms, we've presented the rational numbers $\mathbb{Q}$ and evidenced some flaws in them as we developed in $5.3$. From $\mathbb{Q}$ we developed $\mathbb{R}$ as a complete ordered field ($LUB$) whose elements are no longer measurable quantities but positions in a continuous line, and lastly we stated that it is unique, meaning that any other complete ordered field is isomorphic to $\mathbb{R}$.

Then, let's explain the need for this upgrade and how it relates to Analysis and what Analysis is in fact as a mathematical discipline.

<br>

Analysis is the mathematical field which studies properties or objects by using the **limit**; which is an infinite approximation process that returns a finite output. All of analysis's main objects like derivatives, integrals, continuity, etc. are essentially limits.

For the limit to have sense as an object two main ingredients are needed:

- *Proximity notion*: A *metric*, which in $\mathbb{R}$ emerges from the *order*. However the order is not necessary for a metric to exist and $\mathbb{C}$ is the best example of it.

- *Completeness*: which guarantees that the object of the approximation actually exists. $LUB$ guarantees $\mathbb{R}$'s completeness.

Thus, the limit is gradual approach to an existing object.

<br>

# 8. Exercises.

## 8.1. If $r \neq 0$ is rational and $x$ is irrational, prove that $r + x$ and $rx$ are irrational.

Observe quickly that $r \in \mathbb{Q} \setminus \Set{0} \implies \exists p,q \in \mathbb{Z} : r = p/q$, thus, let's suppose that, being $x$ irrational (this is, not satisfying the implication above), 

- $r+x \in \mathbb{Q} \implies \exists m,n \in \mathbb{Z} : r + x = \frac{m}{n} \implies x = \frac{mq - pn}{qn} \in \mathbb{Q}$ contradicting the premise that $x  \notin \mathbb{Q}$.

A similar argument for $rx$ gives us $x = m/(nr) = (mq)/(np)$ contradicting the premise again

<br>

## 8.2. Prove that there is no rational number whose square is 12. 

Check that $12  = 6· 2$ and from the properties of the powers of positive numbers $5.2.3$ is:

$$\sqrt{12} = \sqrt{3·2^2} =2\sqrt{3} = 2\sqrt{3} \in \mathbb{Q} \implies \sqrt{3} \in \mathbb{Q}$$

But observe that we can take a similar argument of $\sqrt{2} \notin \mathbb{Q}$. Observe that:

$$\sqrt{3} \in \mathbb{Q} \implies \exists m,n \in \mathbb{Z}: (\frac{m^2}{n^2}=3 \wedge [3 \cancel{|} n \vee 3 | \cancel{|} m])$$

But: $m^2 = 3n^2 \implies 3 \| m^2 \implies 3 \| m \implies 3^2 \| m^2 = 3n^2 \implies 3 \| n $, in contradiction with the premise.

Let's make a brief parenthesis: observe that the fraction $\frac{m}{n}$ always expresses the same number, even if it is reducible, meaning that there is the same integer in the denominator and the numerator. This means that if $3 \| m  \wedge 3 \| n$ we can extract and cancel the $3$ in the denominator and the numerator and the fraction will still be $3$. That's why we can suppose that we can iterate until we find some $m^2$ and $n^2$ such that $3$ does not divide both at the same time, which justifies the premise condition that is violated.

Also, observe that $3$ is prime; this justifies that $3 \| m^2 \implies 3 \| m$; observe that for any other composite number this isn't valid: $12 \| 36  =6^2$ but $ 12 \cancel{\|} 6$.

Thus, $\sqrt{3} \notin \mathbb{Q}$. And by exercise one, the product of a rational by an irrational can't be rational, so $\sqrt{12} \notin \mathbb{Q}$.

<br>

Let's also observe some interesting fact.

Consider some $\sqrt{p} \in \mathbb{N}$, suppose that $\sqrt{p} \in \mathbb{Q}$, then there exists some irreducible fraction $\frac{m}{n}=\sqrt{p}$ 

Violating the premise so $\sqrt{p} \notin \mathbb{Q} \setminus \mathbb{N}$, or in other words, $\sqrt{p}\in \mathbb{Q} \implies \sqrt{p} \in \mathbb{N} \iff \exists q \in \mathbb{N} : p = q^2$, ($p$ is a perfect square).

<br>


## 8.3. Prove proposition 1.15. 

This is already demonstrated in $4.2$ and below.

<br>

## 8.4. Let $E$ be a nonempty subset of an ordered set; suppose $\alpha$ is a lower bound of $E$. and $\beta$ is an upper bound of $E$. Prove that $\alpha \leq \beta $.

First, observe that, by definition: $\alpha \leq x \wedge x \leq \beta \quad \forall x \in E$, so we can argue that, by transitivity in order:

$$E \neq \varnothing \implies \exists x \in E : \alpha \leq x \leq \beta \implies \alpha \leq \beta$$

Let's observe that this edge between low and upper bounds take it to the last consecuence means that for any non-empty set $E$ for which we can consider an ínfimum and a supremum, is; $inf E \leq sup E$.

<br>

But let's observe that this result is attained to the fact that $E$ must be non empty. Let's observe that if $E$ where empty then the afirmation $\alpha \leq x \quad \forall x \in E$ is vacuosly true for any $\alpha$, observe that:

$$\forall x \in E, \alpha \leq x \equiv \forall x(x \in E \implies \alpha \leq x)$$

Then, following the truth table of the implication, if $x \in E$ is false (because $E$ is empty) the implication with a false antecedent is always true, this is what we call vacuosly true; a property of how implication works with false antecedent.

And the same happens with the upper bounds $\beta$, meaning that every element of the universe is at the same time an upper bound and a lower bounds, blurring the mathematical notion in it.

<br>

## 8.5. Let $A$ be a nonempty set of real numbers which is bounded below. Let $—A$ be the set of all numbers $—x$, where $x \in A$. Prove that $inf A = —sup(— A)$.

Let's go step by step, consider $-A := \Set{-x \mid x \in A}$, then:

1. $A \neq \varnothing \implies \exists x \in \mathbb{R} : x \in A \implies -x \in -A \implies -A \neq \varnothing$

    <br>

2. Since $A, -A \subseteq \mathbb{R}$ and non-empty, we can apply the combined properties of the operations and the order defined in $\mathbb{R}$. 

    Hence, since $A$ is lowerbounded in $\mathbb{R}$, we can consider some lowerbound $\beta \in \mathbb{R}$ of $A$, verifying, through the properties of the order in $\mathbb{R}$:

    $$\beta \leq x \quad \forall x \in A \iff -\beta \geq -x \quad \forall - x \in -A$$

    Thus, $-\beta$ is an upperbound for $-A$ and this is an upperbounded subset of $\mathbb{R}$.

    <br>

3. By the $LUB$ property of $\mathbb{R}$, any non-empty subset upper/lower bounded has supremum/infimum in $\mathbb{R}$. Meaning we can consider $\inf A \in \mathbb{R}$ and $\sup (-A) \in \mathbb{R}$, verifying:

    $$\beta \leq \inf A \leq x \quad \forall x \in A, \forall  \text{ lowerbound } \beta \in \mathbb{R} \text{ of A}$$

    $$\alpha \geq \sup (-A) \geq - x \quad \forall -x \in -A, \forall  \text{ upperbound } \alpha \in \mathbb{R} \text{ of -A}$$

4. Lastly let's point out that:

    $$\alpha \geq \sup (-A) \geq -x \quad \forall -x \in -A \iff -\alpha \leq -sup(-A) \leq x \quad \forall x \in A$$

    Let be $\beta$ some lowerbound of $A$, then, again $-\beta \geq -x \quad \forall -x \in -A$ which means that $-\beta$ is an upperbound of $-A$ it self, then, calling $\alpha = -\beta \iff -\alpha = \beta \leq -sup(-A)$, as we stated above, so $-\sup(-A)$ is greater than any lowerbound of $A$ being a lowerbound of $A$ it self.
    
    <br>
    
5. Note that, from all above, over $A$ there are two objetcs verifying:

    $$\beta \leq \inf A \leq x \quad \forall x \in A, \forall  \text{ lowerbound } \beta$$

    $$\beta \leq -\sup (- A) \leq x \quad \forall x \in A, \forall  \text{ lowerbound } \beta$$

    Since both $\inf A$ and $-sup(-A)$ are lowerbounds of $A$, the statements above applies to each of them as $\beta$ at the same time, hence:

    $$(-\sup (- A) \leq \inf A \wedge \inf A \leq -\sup (-A)) \implies \inf A = -sup (-A)$$

    Which is the result we wanted to prove.

    <br>

## 8.6. Fix $b > 1$ and prove the following statements:

1. **If $m,n>0,p,q>0 \in \mathbb{Z}$, being $r = m/n = p/q$, then prove that:**

    $$(b^m)^{1/n} = (b^p)^{1/q}$$

    Let's depart from the fact that: 
    
    $$m/n = p/q \iff mq = pn \iff b^{mq} = b^{pn} \iff (b^m)^q = (b^p)^n$$

    The last step is justified by the fact that since $m,q,p,n$ are integers. Take $b^{mq}$ and call $B = b^m$, then $b^{mq} = \prod\_{i=1}^{mq} b = \prod\_{i=1}^q B = B^q = (b^m)^q$, a similar argument can be provided with the counter part.

    Then, now we leverage the fact that by $n$-th root of a positive real is unique by $1.21$, thus we can take:

    $$(b^m)^q = (b^p)^n \iff ((b^m)^q)^{1/q} = b^m = ((b^p)^n)^{1/q} $$

    Also, observe that from the corollary of $1.21$ as well is:

    $$((b^p)^n)^{1/q} = ((b^p)^{1/q})^n$$

    And again by the unicity of the $n$-th root of positive reals numbers is:

    $$(b^m)^{1/n} = (((b^p)^{1/q})^n)^{1/n} = (b^p)^{1/q}$$

    <br>

    Observe that this give sense to the notation:

    $$(b^m)^{1/n} = b^{m/n}$$

    Because we proved that whenever the operator of the fraction are, as long as the fraction remains equivalent, the root points to the same real number.

    <br>

2. **Prove that $b^{r+s} = b^rb^s$ if $r$ and $s$ are rational.** 

    Observe that, taking $r = m/n$ and $s = p/q$ such $m,n,p,q \in \mathbb{Z} : n,q > 0$, then is:
    
    $$r + s = \frac{mq + np}{nq} \iff b^{r+s} = b^{\frac{mq + np}{nq}}$$

    Recovering the notation stablished in $1.$ is:

    $$b^{\frac{mq + np}{nq}} = (b^{mq + np})^{1/nq} = (b^{mq}b^{np})^{1/nq}$$

    The last step is justified for being $m,n,p,q \in \mathbb{Z}$, then, lastly, leveraging the corollary of $1.21$ and taking advantage of the notation develop in $1$:

    $$(b^{mq}b^{np})^{1/nq} = (b^{mq})^{1/nq} (b^{np})^{1/nq} = b^{mq/nq}b^{np/nq} = b^rb^s$$

    <br>

3. **If $x$ is real, define $B(x)$ to be the set of all numbers $b^t$, where $t$ is rational and $t\leq x$. Prove that: $b^r = sup B(r)$.**

    Let's start considering that $B(x) := \Set{b^t \mid t \in \mathbb{R} : t \leq x}$, then, since $b>1$:

    - First, take $a,b \in \mathbb{R} : 1 < a \leq b, n \in \mathbb{N}$ and let's call: $\alpha^n =a, \beta^n = b$, then we have that:

        $$a \leq b \iff 1 \leq (\beta \alpha^{-1})^n \implies 1\leq \beta \alpha^{-1} \iff a^{1/n} \leq b^{1/n}$$

        The implication is sustained by the fact that $1^n = 1 \quad \forall n \in \mathbb{N}$, so the powers tends to distance  positive numbers from $1$, meaning that any power with natural exponent of a positive number smaller than $1$ is always smaller than the number, and any power of natural exponent of a number above $1$ is greater than the number it self. This follows immediately from the properties of the axioms of the multiplication and the order.
        
        Formally: $1 < a \implies 1 < a^n \quad \forall n \in \mathbb{N}$, and $0< a < 1 \implies a^n < 1 \quad \forall n \in \mathbb{N}$ thus, let's suppose that $1<a^n$, if where $a < 1$ then by the above it would be $a^n < 1$, contradicting the premise.

        <br>

        Thus, let's now consider $r,s$ from point $2.$, then suppose $r\leq s$:
        
        $$m/n \leq p/q \iff mq \leq pn \iff b^{mq} \leq b^{pn}$$

        And, making use of what we stated above since $b>1$, we can proceed as in point $1$ concluding: $b^r \leq b^s$.

    - Now, it is clear that $B(x)$ is non-empty for any $x \in \mathbb{Q}$. Consider $b^x$, which clearly satisfies, as we stated above, that: $b^t\leq b^x \quad \forall t \leq x$, then $B(x)$ upperbounded. Let's consider some upperbound $\alpha$ of $B(x)$, then it verifies: $b^t \leq \alpha \quad \forall t \leq x$, since $x \leq x$ then is $b^x \leq \alpha$ so $b^x$ is the least upperbound of $B(x)$; $b^x = \sup B(x)$.

    <br>

    Thus, $b^x = supB(x) \quad \forall x \in \mathbb{R}$

    <br>

4. Lastly, let's proof that $b^{x+y}=b^xb^y$.

    Is almost immediately: $b^{x+y} = supB(x+y) = \Set{b^t \mid t \leq x+y}$ which by the above is $b^xb^y$.

    <br>

## 8.7. The logarithm of $y$ to the base $b$

We are going to prove that $\forall b,y \in \mathbb{R} : b>1, y>0 \ \exists! x \in \mathbb{R} : b^x = y$, which is called logarithm of $y$ in the base $b$; $\log\_b y$ by completing the following outline. 

1. **Bernoulli inequality in multiplicative form**: $b^n - 1 \geq n(b - 1) \quad \forall n \in \mathbb{N}$

    First, let's take the geometric factorization which states that for any conmutative ring elements $x,y$ is:

    $$x^n -y^n = (x-y)\sum_{i=0}^{n-1}(x^{n-1-i}y^i)$$

    Now, take $x = b >1$ and $y=1$, then:

    $$b^n -1 = (b-1)\sum_{i=0}^{n-1}(b^{n-1-i}1^i)= (b-1)\sum_{i=0}^{n-1}b^{n-1-i}$$

    Take now that the question of the exercise is now to verify:

    $$(b-1)\sum_{i=0}^{n-1}b^{n-1-i} \geq n(b - 1) \iff \sum_{i=0}^{n-1}b^{n-1-i} \geq n$$

    But, observe that this result is almost immediately at is follows from the fract that $b^n > b > 1$ for any $n \in \mathbb{Z}^+$, then adding all the inequalities from $1$ to $n$ we have:
    
    
    $$b>1 \implies \sum_{i=1}^n b^{n-i} \geq \sum_{i=1}^n 1 = n \quad \forall n \in \mathbb{Z}^+$$

    Lastly, we just reconstruct: $b>1 \implies b-1 >0$ thus:

    $$(b-1)\sum_{i=1}^n b^{n-i} \geq n(b-1) \quad \forall n \in \mathbb{Z}^+$$

    Ultimately giving, combined with the original result, and considering the case $n=0$:

    $$b^n -1 \geq n(b-1) \quad \forall n \in \mathbb{N}$$

    <br>

2. From $1.$ we take immediately that, calling $B= b^{1/n} > 1$ is $B^n - 1 \geq n(B - 1) \quad \forall n \in \mathbb{Z^+}$, note that obviously $n \neq 0$ so reverting the inequality we have that: $b -1 \geq n(b^{1/n} - 1) \quad \forall n \in \mathbb{Z}^+$

    <br>

3. **If $t>1$ and $n>(b-1)/(t-1)$, then $b^{1/n}<t$**

    Observe that, is also $b>1$, so:

    $$\begin{cases} t> 1 \\ n > \frac{b-1}{t-1}\end{cases} \implies n(t-1)>b-1 \geq n(b^{1/n} - 1) \implies t > b^{1/n}$$

    Since we treat $n \neq 0$, then we cancel $n$ and add $1$ to both sides.

    <br>

4. **If $w \in \mathbb{R} : b^w<y$, then $\exists n \in \mathbb{Z}^+ : b^{w+(1/n)}< y$**

    Observe that $b^w< y \implies y/b^w > 1$ and for the result above we have that exists some $n \in \mathbb{Z}^+$ that $y/b^w > b^{1/n} \iff y = b^{w + 1/n}$

    <br>

5. **If $w \in \mathbb{R} : b^w>y$, then $\exists n \in \mathbb{Z}^+ : b^{w-(1/n)}> y$**

    Observe again that by the point $3$:
    
    $$b^w> y \implies b^w/y > 1 \implies \exists n \in \mathbb{Z}^+ : b^w/y > b^{1/n} \iff b^w/b^{1/n} = b^{w-1/n} > y$$

    <br>

6. **Let $A := \Set{w \mid b^w < y}$, show that $x = \sup A \iff b^x=y$**

    Since $b>1$ then $b^w<b^x \implies w <x$, thus $x : b^x = y$ is an upperbound of $A$. Let's see now that is the least upper bound of $A$. 
    
    Take some $t : b^w < b^t \quad \forall w \in A$. Observe that $t \notin A$, otherwise, by the prior results, it would exists some $n \in \mathbb{Z}^+ : t + 1/n \in A$ and $t$ would not be an upperbound.

    This means basically that $t \notin A \implies y = b^x \leq b^t \implies x \leq t$ and $x$ is the least upper bound of $A$, so $x = supA$ and, by the uniqness of the supreme in a total ordered field like $\mathbb{R}$, $x$ as stated is unique.

    <br>

Let's make an appointment here, the theorem $1.21$. of Rudin's book (or $5.2.3$ in this posts), stated that for any natural exponent $n$ and any positive real $y$ exists only one real $x : x^n = y$ and we called $x$ the $n$-th root of $y$.

This result, along with $8.6$ has extended it to real exponents, first by giving sense to real exponents and later proving that for any positive reals $b>1, y>0$ exists a unique real $x : b^x =y$ and we call it as *the logarithm of $y$ on the base $b$*.

<br>

Let's observe that there is an incremental factor about exponentials, let's consider the function with $a \in \mathbb{R}$ as: 

$$f: A \to \mathbb{R} \mid f_a(x) = a^x : a \in \mathbb{R}^+$$

<br>

- First, we begin defining that, being $x \in \mathbb{R}$, then $x^n : n \in \mathbb{N}$ is $\prod\_{i=1}^n x$, this very number multiplied by itself a finite number of times. Hence, it has sense to consider $A = \mathbb{N}$

- Then, by the properties of the powers with natural exponent, we see that $x^{-a} : a \in \mathbb{Z}^+$ is the power of the inverse: $x^{-a} = (x^{a})^{-1} = 1/x^a$. With this we extended to $A = \mathbb{Z}$

- Now, we introduce the notion of the $n$-th root of a positive real as a way to express power of natural inverses $\sqrt[n]{x} = x^{1/n}$ and in $8.6$ we see that this notion is sufficent to consider rational exponents; $x^{m/n} = (\sqrt[n]{x})^m$ extending to $A = \mathbb{Q}$

- Lastly, with the help of the supremum we stablished real exponents $A = \mathbb{R}$ and we presented the logarithm as the historical tool to calculate non-integer exponents.

    <br>
