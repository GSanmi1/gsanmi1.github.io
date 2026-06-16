---
layout: post
title: "1. The Real Number Systems"
subtitle: "Rational and Real fields presentation. Order. Analisis definition."
date: 2026-03-05 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
---

1. Introduction.
    - 1.1. Rational numbers inadequatness. Irrational numbers.

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
    - 5.1. Theorem: Existance of $\mathbb{R}$. Dedekind cuts.
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

We will pressume familiarity with $\mathbb{Q}$ (meaning that we assume the sentence "$(\mathbb{Q},+, \ ·)$ is a field and the axioms for the field's algebraic structure applies in its totality." is completely understanded and acknowledge by the reader) and use this knowledge to build $\mathbb{R}$ and then $\mathbb{C}$.

<br>

## 1.1. Rational numbers inadequatness. Irrational numbers.

Let's start talking about some lackness on the rational numbers. The rational number system is inadequate for many purposes, both as a field and as an ordered set since the rational number line is full of gaps. 

For instance, there is no $p \in \mathbb{Q} : p^2 = 2$. Let's consider that $\exists p \in Q: p^2 = 2$, then this would implie that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$

Let's also observe that if $m, n \in \mathbb{2Z}$, then we could divide between $2$ the numerator and denominator and the fraction will still value $p$ and $m,n \in \mathbb{2Z}$ so we could divide again, and eventually this iteration process of divide between $2$ must terminate because eventually one of the two must be odd. 

So we can ensure without loss generality that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$ and at least one of both is not even. Then, the equation imposes that $m$ is even:

$$p^2 = \left(\frac{m}{n}\right)^2 = \frac{m^2}{n^2} = 2 \iff m^2 = 2n^2 \in 2\mathbb{Z}$$

Let's observe that $2 \vert n^2 \implies 2 \vert n$, if $2 \vert n^2 \wedge 2\not\vert  \ n$ then $n = 2q + 1  \implies n^2 = 2(2q^2 +2q) + 1$ and $2 \not\vert n^2$ contradicting the initial premise. 

So, we have:

$$m \in \mathbb{2Z} \implies 2 \vert m \implies 4 \vert m^2 \iff 4 \vert 2n^2 \implies n^2 \in \mathbb{2Z}$$

and also $n$ is even contradicting the presumption. So there aren't $m,n \in \mathbb{Z} : p = \frac{m}{n}$

<br>

This leads to the introduction of so-called *irrational numbers* which are often written as infinite decimal expansions and are considered to be "approximated" by the corresponding finite decimals, meaning that, for example; $1, 1.4, 1.41, 1.414, 1.4142,\ldots$ tends to $\sqrt 2$. But before that we have to define what "tends" or "approximates" means. 

<br>

To ilustrate better the idea of the irrational number we can consider the following sets: 

$$A:= \Set{p \in \mathbb{Q}^+ \mid p^2 < 2 }, \quad B:= \Set{p \in \mathbb{Q}^+ \mid  p^2 > 2 }$$

Let's demonstrate that $A$ no contains largest number and $B$ no contains smaller but none of them contains the point it self (since is not rational):

$$q = p - \frac{p^2 -2}{p+2}: p \in \mathbb{Q}$$

- Check that if $p \in A \implies p^2 < 2 \iff p^2 - 2< 0 \implies q > p$, and also  observe that: 

    $$ q^2 - 2 = \left( p - \frac{p^2 -2}{p+2} \right)^2 - 2 = \left(\frac{2p + 2}{p+2} \right)^2 - 2 = \frac{2(p^2 - 2)}{(p+2)^2}$$

    Hence, $p^2 - 2 < 0 \implies q^2 - 2 < 0 \implies q \in A$. Thus we can ennonce that:

    $$\forall p \in A \ \exists q \in A:  q > p$$

- Let's also observe using the same definition, $p \in B \implies q \in  B \wedge p > q$ which means that also is:

    $$\forall p \in B \ \exists q \in B:  q < p$$

Then, we can understand the *irrational numbers* as a "never-reached-frontier" of certains segments of rational numbers like $A$ or $B$. 

Observe that we only need one of the two sets because both of them "tends" to the same value. By default, we would prefer $A$ as a standard to present the irrational number to which $A$ and $B$ tends to. 

<br>

Thus, the rational number system or the rational line is full of gaps, despite of the fact that between any two rationals there is another:

$$ r,s \in \mathbb{Q} : r < s \implies r < \frac{r + s}{2} < s \wedge \frac{r + s}{2} \in \mathbb{Q}$$

The *real number system*; $\mathbb{R}$, get those gaps filled, this is the principal reason for the fundamental role which it plays in analysis.

<br>

# 2. Ordered Sets.

In order to introduce $\mathbb{R}$ and why is a preferable option to $\mathbb{Q}$ we have to talk about some important property involved with *order* and thus, first we have to introduce the notion of *ordered sets*. 

So let's start introducing a minimal basis about order in a set.

<br>

First, the mathematical order is an abstraction about primary cognitive operation; compare two objects and decide which of the two go first as we ordinarily do with weight, cronological events or hierarchies. Basically the order is a *binary relation between elements of a domain that codifies "precedence" between the two of them*.

<br>

## 2.1. Binary relations.

### 2.1.1. Definition.

In mathematics, a relation is basically any collection of ordered pairs from a set. 

Formally, given a set $S$, we say that a *binary relation* over $S$ is any $R \subset S^2 = S \times S$. As defined this notion is trivial and lack of any interest and only becomes relevant when the relation forces some conditions.

Being $(x,y) \in R$, we read it as "$x$ is related with $y$ through $R$" and we may write $xRy$ to simplify the notation.

<br>

### 2.1.2. Properties.

Given a binary relation over $R$ over a non-empty set $S$, then $R$ can satisfy the following properties:

- **Reflexivity**: $\forall x \in S,\; xRx \iff \forall x \in S, (x,x) \in R $
- **Irreflexivity**: $\forall x \in S,\; \neg (xRx) \iff \forall x \in S, (x,x) \notin R$

- **Simetric**: $\forall x, y \in S,\; x \mathbin{R} y \Rightarrow y \mathbin{R} x$, observe that this impose reciprocity.

- **Antisimetric**: $\forall x, y \in S,\; (x \mathbin{R} y) \land (y \mathbin{R} x) \Rightarrow x = y$

- **Transitiva**: $\forall x, y, z \in S,\; (x \mathbin{R} y) \land (y \mathbin{R} z) \Rightarrow x \mathbin{R} z$ 

- **Conex**: $\forall x, y \in S,\; (x \mathbin{R} y) \lor (y \mathbin{R} x)$

- **Tricotomic** $\forall x, y \in S$ only one of the following statements are true:

    $$x \mathbin{R} y, \quad y \mathbin{R} x, \quad x = y$$

    <br>

### 2.1.3. Order Types.

**Partial and Total orders**

Be $S$ a set, then a relation $\leq \ \subset S^2$ is a *partial order* if is **reflexive**, **antisimetric** and **transitive**.

As an extension of the partial order we have *total order* if also is **conex**, this means, the comparison criterion can be applied to every element of $S^2$. Observe that, geometrically, this means that all the elements can be sorted in a line as it happens with number sets $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ can all be represented in a line.

<br>

**Strict Orders**

Taking a partial order $\leq \subset S^2$, then we define a *strict order* as:

$$< \ \subset S^2 : (x < y \iff x \leq y \wedge x \neq y)$$

Observe that, as defined this relation verifies:

- **Irreflexivity**: $\neg(x < x) \quad \forall x \in S$
- **Transivity**: Inheritated from $\leq \ \subset S^2$

If also $\leq \ \subset S^2$ is total, then $<$ is also **tricotomic** and we would call it *strict total order*, this is imposed from the irreflexive property that makes the three statements disjoint between them.

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

Observe that this relation is obviously *reflexive* and *transitive* (inherited from $< \ \subset \mathbb{Q}^2$) and also *antisimetric*, since $x \leq y \wedge y \leq x \implies x = y$, since $x < y$ and $y < x$ are mutually exclusive.

<br>

# 3. Bounds. 

Until now, we just defined that an ordered set is simply a set in which an order relation has been defined and also define an order in $\mathbb{Q}$. 

Let's introduce the concept of *bounds*, and naturally extract the concept of the *minimal bound* for a set.

<br>

## 3.1. Upper and Lower bounds of a set. Supremum and Infimum.

Consider now $S$ and ordered set and $E \subset S$, then we say that:

$$E \text{ is upperbounded} \iff \exists \alpha \in S: x \leq \alpha \ \ \ \forall x \in E $$

We define as lower upperbound (or least-upper-bound) as:  

$$\alpha ' \in S : x \leq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \leq \alpha \ \ \forall \alpha \in S: x \leq \alpha \ \ \forall x \in E)$$

And we denote it as $\alpha ' = sup E$ and call it the *supremum* of $E$. 

This same idea applies to lowerbounds:

$$E \text{ is lowerbounded} \iff \exists \alpha \in S: x \geq \alpha \ \ \ \forall x \in E $$

And we define the *ínfimum* of $E$ (and we denote it to $\alpha ' = inf E$) to:

$$\alpha ' \in S : x \geq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \geq \alpha \ \ \forall \alpha \in S: x \geq \alpha \ \ \forall x \in E )$$

<br>
This are the minimal upper/lower bounds of a set and his existance is not garanteed as we will see in the example below. Observe trivially that boths supremum and infimum are unique, the proof is trivial derived from the trichotomy property but is worth to mention this fact for future demonstrations. 

<br>

## 3.2. Example of bounds in subsets of $\mathbb{Q}$.

Let's now observe two examples in which we want to ilustrate two facts about minimal bounds.

**The first one ilustrates that, in $\mathbb{Q}$, minimal bounds are not garanteed to exists for any bounded set $S \subset \mathbb{Q}$, and this is the main reason why $\mathbb{Q}$ is full of gaps.**

The second example pretend to ilustrate that, although the definition of bound do not prohibit a minimal bound of $E$ to be contained in $E$, this is not true in general, a minimal bound often is not a member of the bounded subset.

1. Let's consider again $A:= \Set{p \ \vert \ p^2 < 2 }, B:= \Set{p \ \vert \ p^2 > 2 } \subset \mathbb{Q}^+$. 

    The set $A$ is bounded above. In fact, the upper bounds of $A$ are exactly the members of $B$. Since $B$ contains no smallest member, $A$ has no least upper bound in $\mathbb{Q}$. Similarly, $B$ is lowerbounded and the lower bounds of $B$ are the elements of $A$. But since $\nexists p \in \mathbb{Q} : p^2 = 2$ neither of the two has minimal bound.

    <br>

2. Being $E \subset S$ , then $\exists \alpha = supE$ implies that $\alpha$ may or may not be member of $E$. For instance, $E_1:=\Set{r \ \vert \ r < 0}$ and $E_2:=\Set{r \ \vert \ r \leq 0}$ then $\alpha = supE_1 = supE_2 = 0 \wedge \alpha \notin E_1 \wedge \alpha \in E_2$

    <br>

    Also, let be, $E:=\Set{ \left(\frac{1}{n}\right)_{n \in \mathbb{N}}}$, then $supE = 1 \in E \wedge infE = 0\notin E$

<br>

## 3.3. Least-upper-bound property.

Now, we have presented order, bounds, minimal bounds and we also provided an example to ilustrate that minimal bounds sometimes do not exists. 

Then in this section we are going to present the ***Least-upper-bound property*; this property garantee the existance of the minimal bound for any bounded and non-empty subset.**

<br>

**Definition**

An ordered set $S$ is said to have the least-upper-bound (LUB) property if for any  upperbounded non-empty subset $E \subset S$ the supremum of $E$ exists in $S$. 

Formally: 

$$ \forall E \subseteq S : (E \neq \varnothing \wedge \exists \alpha \in S : x \leq \alpha \ \ \forall x \in E) \implies \exists \alpha_s = supE : \alpha_s \in S $$


<br>

**Theorem**

Now, the following theorem introduces that the LUB property is a sufficent condition to ensure the existance of an *infimum* for any non-empty lowerbounded subset and also offers a characterization of the object.

Let's consider an ordered set $S$ that satisfies the least-upper-bound property and a non-empty, lowerbounded, subset $B \subseteq S$. 

Then, we call $L$ to the set of all the lowerbounds of $B$ in $S$:

$$L_B := \set{\alpha \in S : \alpha \leq x \ \ \forall x \in B}$$

Since $L_B$ is clearly upperbounded by any item of $B$ and $S$ satisfies the least-upper-bound property, then we can talk about an $\alpha_s \in S : \alpha_s = supL_B$. Observe that:
 
$$ \alpha_s = supL_B \implies \begin{cases} \nexists b \in B: b < \alpha_s  \\ \nexists l \in L_B : l > \alpha_s \end{cases} \implies \alpha_s = infB$$

The first condition tell us that $\alpha_s$ is a lowerbound, the second tell us that there isn't any other lowerbound $l$ bigger than $\alpha_s$, thus, it must be the infimum.





Then, we have:

$$ \exists \alpha_s \in S: \alpha_s = supL_B = infB$$

<br>

# 4. Fields.

## 4.1. Definition and Axioms.

A field is a set $F$ with two operations, called addition, $+$ and multiplication, $·$ which satisfy the following so-called *field axioms*:

- *Closure*: $x + y \wedge x ·y \in F \ \ \forall x,y \in F$
- *Conmutativity*: $x+y = y+x \wedge x·y = y·x \ \ \forall x,y \in F$
- *Associativity*: $(x+y)+z = x + (y+z) \wedge (x·y)·z = x·(y·z) \ \ \forall x,y,z \in F$
- *Zero and Unity entities*: $\exists 0,1 \in F :0 \neq 1 \wedge (0 + x = x \wedge 1·x = x \ \ \forall x \in F)$
- *Inverses*: $\forall x \big(\exists (-x) \in F : x + (-x) = 0 \big) \wedge \big(\exists x^{-1} \in F : x·x^{-1}=1\big)$
- *Distributibe law*: $x(y+c) = xy + xz \ \ \forall x,y,z \in F$

<br>

Is worth to mentiont that, is usually to write:

$$x - y, \frac{x}{y}, x + y + z, xyz, x^2, x^3, 2x, 3x,$$

instead of:

$$x + (-y),\ x \cdot \left(\frac{1}{y}\right),\ (x + y) + z,\ (xy)z,\ xx,\ xxx,\ x + x,\ x + x + x$$

Also, the field axioms clearly hold in $\mathbb{Q}$, the set of all rational numbers, if addition and multiplication have their customary meaning.

<br>

## 4.2. Immediate properties.

Although it is not our purpose to study fields (or any other algebraic structures) in detail, it is worthwhile to prove that some familiar properties of $\mathbb{Q}$ are consequences of the field axioms; once we do this, we will not need to do it again for the real numbers and for the complex numbers. 

- *Cancelation*: 

    $$(x + y = x + z \implies y = z) \wedge (xy = xz \wedge x \neq 0 \implies y=z)$$

    <br>

- *Uniqness of unity and zero*: 

    $$(x + y = x \implies y = 0) \wedge (xy=x \wedge x \neq 0\implies y=1)$$

    <br>

- *Uniqness of inverse*:

    $$(x + y = 0 \implies y = -x ) \wedge (xy=1 \wedge x \neq 0\implies y=x^{-1})$$

- $-(-x)= x \wedge \big(x \neq 0 \wedge (x^{-1})^{-1} = x\big)$

<br>

Also, let observe that:

- $0x = 0$. Immediately, we have that $0x = (0x + 0x) = 0x \implies 0x = 0$ by the axiom above.

    <br>

- *Zero has no divisors*:

    Lets observe that $x \neq 0 \wedge y \neq 0 \implies xy \neq 0$. 
    
    Observe that $\neg(\neg p) \equiv p$ in classic logic, so to demonstrate $p$ lets see that is $\neg(\neg p)$ or in other words let's see that $\neg p$ is not true.

    In our case $p$ is an implication $p:= l \to t \equiv \neg l \vee t \iff \neg p := l \wedge \neg t$, (remember that conjuntion and disjuntionrelates each other as:  $\neg (p \wedge q) \equiv \neg p \vee \neg q$) thus, we are considering that $\underbrace{(x \neq 0 \wedge y \neq 0)}\_l \wedge \underbrace{xy = 0}\_{\neg t}$ but this is imposible since: $x \neq 0 \wedge xy = 0 \implies y = 0$ (following the axioms described above) entering in contradiction with the premisse, thus: $x \neq 0 \wedge y \neq 0 \implies xy \neq 0$. 

    Let's also see that: $p \to q \equiv \neg p \vee q \equiv \neg (\neg q) \vee \neg p \equiv \neg q \to \neg p$, applying that to our rule, we can obtain a subtle better expression of the rule: $xy = 0 \implies x = 0 \vee y = 0$
  
    <br>

- $(-x)y = -(xy) = x(-y)$

    Let's consider the case $(-x)y$, a similar argument can be considered with $x(-y)$. 

    $$(-x)y + xy = (-x + x)y = 0 y = 0$$

    Which means $(-x)y = -xy$ due to the uniquity of the inverse in $F$.

    <br>

- $(-x)(-y) = xy$

    Let's observe that as we proved before:

    $$(-x)(-y) + (-xy) = (-x)(-y) + (-x)y = (-x)[(-y) + y] = 0$$

    Which means $(-x)(-y) = -(-xy) = xy$.

    <br>

## 4.3. Ordered fields.

### 4.3.1. Definition.

An *ordered field* is a field $F$ which is also an ordered set. This implies to define a relation between the order and the operations of the field. 

Before relate the operations of $F$ with the order, let's expands the definition of the operations in order to give it some geometric intuition. As a brief reminder, $F$ as a field is a triple $(F,+, \ ·)$ where $(F,+),(F,\ ·)$ are abelian groups and $+, \ ·$ are compatible (which means they both satisfy the distributive property). 

Observe that, since $< \ \subset F$ as defined above is a total strict order, we can dispose the elements of $F$ in a line following the precedence that sets $<$. This give us some geometric intuition about the relation between the operations in the field and the order.

We can understand the $+$ and $·$ operations as the following:

- For each $x \in F$, lets define:

    $$\tau_x : F \to F, \qquad \tau_x(y) = x + y$$

    This is obviuosly a free (without privilege or fixed points) and transitive (each point is moved to other point) biyection and we will call it **traslation of distance $x$**. We can understand it as a movement that sends a point $y$ to the point $x+y$.

    Observe that the operation $+: F \times F  \to F$ and the collection $\Set{\tau\_x}\_{x \in F}$ are equivalents representation of the same composition in $F$, or, in other terms there are equivalent representation of the same composition $(x,y) \mapsto\_+ z$ using both systems.
    
    <br>

- Now, let's consider:

    $$\mu_x : F \to F, \qquad \mu_x(y) = xy$$

    This is an homothety of center $0$ and ratio $x \neq 0$. An *homothety* can be understanded as a dilatation of the space in which is defined, it expands/constraint from the center any point $x$ times. Applied to our line intuition it moves away a value $x$ times is own value, the magnitude of $x$ measures how far it sends the point and it signe the direction of the movement.

    Again, there is a clear equivalence between the family $\Set{\mu\_x}\_{x \in F}$ and the multiplication defined in $F$

    <br>

Thus, having defined this two geometric extrapolations of the operations defined in $F$, lets perform two axiomatic asserts of how operations behaves with $<$.

- **Invariance under traslation**: 

    $$ y < z \implies \tau_x(y) < \tau_x(z) \quad \forall x \in F$$

    Observe that by cancelation we obtain the reciproc, so is bidirectional invariance.
    
    <br>

- **Invariance under homothety of positive ratio**: 

    $$0 < y \implies 0 < \mu_x(y) \quad \forall x \in F : 0 < x$$

    Observe that this axiom is minimalist since, in combination with the axiom above:

    $$0 < z - y \implies  0 < \mu_x(z - y) = \mu_x(z) - \mu_x(y) \iff \mu_x(y) < \mu_x(z) \quad \forall x \in F : 0 < x$$

    Obtaining the same representation than we had with traslations.

    <br>

We also say that $x  \in F$, then:

- $x \text{ is positive } \iff 0 < x$
- $x \text{ is negative } \iff x < 0$

We could thinkg about the positive and negative terms as the direction of the traslation we need to apply to $0$ to reach some value. A right traslation is a positive sign, while a negative sign means left direction. Oberserve that there is no direction for the traslation that sends $0$ to $0$, so $0$ itself have no sign.

<br>

### 4.3.2. Properties of ordered fields.

All the familiar rules for working with inequalities apply in every ordered field: Multiplication by positive/negative quantities preserves/reverses inequalities, no square is negative, etc. 

The following proposition lists some of these. When treat the following demonstration, remember that $<$ is a total order, which allow us to dispose all the elements of the fields in a single line. 

Thus, lets think in a line with the elements of the field $F$ represented on it:

1. **Reflexion over the origin**: $x > 0 \iff -x < 0$

    This bassically means that the opposite of any value of the addiion always has the opposite sign of the original value, or, in geometric terms, opposites by the addition always fails in opposite sides of the line of $F$.

    Let's observe that since $0<x \implies \tau_{-x}(0) = -x < 0 = \tau_{-x}(x)$, or saying it in simple words, we need to move $0$ to the left to reach the opposite of a positive value.

    <br>

    Let's also try to demonstrate it by absurdio reductio which is:

    $$\neg [(x > 0)\leftrightarrow (x<0)] \implies \bot$$

    Let's observe that:

    $$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p) \equiv (\neg p \vee q) \wedge (\neg q \vee p)$$

    This way; $\neg(p \leftrightarrow q) \equiv \neg [(\neg p \vee q) \wedge (\neg q \vee p)] \equiv (p \wedge \neg q) \vee (q \wedge \neg p)$

    Now, lets call $p := x > 0$ and $q := -x <0$, then:

    - $p \wedge \neg q$ stands for $x>0 \wedge -x > 0$, but this statement is impossible, considering the first axiom above:

        $$x > 0 \iff 0 = x + (-x) > 0 + (-x) = -x$$

        So is $-x > 0 \wedge -x < 0 \implies -x = x = 0$ contradicting the premise that suppose $x$ is greater than $0$.

    - A similar argument can be provided to demonstrate the unavaiability of $\neg p \wedge q$ which stands for the statement $x<0 \wedge -x < 0$:

        $$-x < 0 \iff 0 = x - x < x + 0 = x$$

        So we have $x > 0 \wedge x < 0 \implies x = 0$ again.

    This way, $\neg [(x > 0)\leftrightarrow (x<0)] \implies \bot$ and the initial has been demonstrated.

    <br>

2. **Invariance under positive scale**: $x > 0 \wedge y < z \iff xy < xz$

    We already demonstrate this before using the homothety, let's repeate it by multiplication:

    $$y < z \iff 0 = y + (-y) < z + (-y)$$
    
    This way, counting with $x >0$ and using the second axiom of the ordered fields, we have:

    $$0 = x0 < x(z + (-y)) = xz + x(-y) = xz + (-xy) \iff xy < xz$$

    <br>

3. **Reversion under negative scale**: $x < 0 \wedge y < z \implies xy > xz$

    Before dive in this demonstration, let's see something important about homotheties, we have that, since is $\mu_x(y) = xy$, then $\mu_{-x}(y) = \mu_x(-y) = - \mu_x(y)$. Meaning that, applying an homothety of negative ratio is equivallent to displace the negative value with a positive ratio which is the same as applying the homothety of positive ratio in the opposite direction (from the opposite value).

    Thus, we have that:

    $$y<z \wedge x < 0 \iff y<z \wedge 0 < -x \implies \mu_{-x}(y) < \mu_{-x}(z)$$

    Now, observe that the homothety applies the same but in the other side of the line, meaning that the precedence between $y$ and $z$ reverses: $y < z \implies -z < -y$, so:

    $$\mu_{-x}(y) < u_{-x}(z) \iff -\mu_{x}(y) < -\mu_{x}(z)\iff \mu_{x}(z) < \mu_{x}(y)$$

    In summary: $y<z \wedge x < 0 \implies \mu_{x}(z) < \mu_{x}(y)$

    <br>

4. **Positiveness of the squares**: $x \neq 0 \implies x^2 > 0$

    Is natural to think that, if $x$ is positive, an homothety of ratio $x$ will mainting it on the positive side and if $x$ is negative, then $\mu_x$ would be a negative ratio homothety and it would act over $x$ moving it over the point $\mu_{-x}(-x)$ which lives in the opposite side of the origin, so, in any case:
    
    $$0<x^2 = \mu_x(x)$$

    Formally:
    
    $$x \neq 0 \implies \begin{cases}x>0 \implies xx = x^2 > 0 \\ x < 0 \iff -x < 0 \implies (-x)(-x) = xx = x^2 >0 \end{cases}$$

    As a particular case is $1^2 = 1 > 0$

    <br>

5. **Reverse of the inverse**: $0 < x < y \implies 0 < \displaystyle\frac{1}{y} < \frac{1}{x}$
    
    Before dive in this demonstration, let's explore what $\mu_{x^{-1}}$ is for any $ x \neq 0$ from $F$.

    The obvious thing is to think that, $\mu_{x^{-1}}$ as defined, is that homothety that sends $x$ to the multiplicative identity $1$, but this is a weak an useless conception. Let's observe that in fact, for $\mu_{x^{-1}}$, $x$ defines the homothety behaviour.

    Think that, whenever you divide a number, (multiplicate it by an inverse of some integer) you are asking how much times this number fit in the divisor. Thusm, the homothety $\mu_{x^{-1}}$ redefines the line of $F$ as if $x$ was the number relative to which the rest are defined (which by default is $1$) meaning that $\mu_{x^{-1}}(y)$ tells you how many times $y$ is contained in $x$.

    Having this clear, let's observe that is obvious that $x < y \implies \mu_{y^{-1}}(1) < \mu_{x^{-1}}(1)$ which is exactly the statement above.

    <br>

    In algebraic terms, we could reason that, since $x \neq y \neq 0 \implies \exists x^{-1},y^{-1} \in F$. Let's also observe that, before, above, we see that $1 > 0$, then $1=xx^{-1} \wedge x > 0 \implies x^{-1} > 0 \ \ \forall x \in F : x > 0$ and we can argument that:

    $$0 < x < y \iff 0x^{-1} < xx^{-1} = 1 < yx^{-1} \iff y^{-1}0x^{-1}< y^{-1} <y^{-1}yx^{-1} = x^{-1}$$

    Resulting $0 < x < y \iff 0 < y^{-1} < x^{-1}$

    <br>

# 5. The Real field.

We will no present the core theorem of this chapter.

Until now, we presented fields, order, the combination of both in the ordered field and give a geometric interpretation of the operations of the field when an order defined.

Then, we introduced bounds and the $LUB$ property and we see that, despite $\mathbb{Q}$ is an ordered field, it not satisfies the $LUB$ property, giving to the rational line a discontinue appearance; points to which we can approximate as much as we want but we can't touch.

Thus, let's present $\mathbb{R}$ as an ordered field that satisfies the $LUB$ property.

<br>

## 5.1. Theorem: Existance of $\mathbb{R}$. Dedekind cuts.

**There exists an ordered field $\mathbb{R}$ which has the least-upper-bound property which contains $\mathbb{Q}$ as a subfield.** 

To proove this theorem, we will construct $\mathbb{R}$ from $\mathbb{Q}$. We shall divide the construction in several steps.

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

- **A cut doesn't contains his own supreme**:

    $p \in \alpha \implies \exists r \in \alpha : p < r$. 

    <br>

Check that this so called "cuts" are upperbound segments with no lowerbound, in the sense that the second property of the cuts already tell us that $p \in \alpha \implies \forall q(q < p \implies q \in \alpha)$. This feature allows an order in $\mathbb{R}$ relative to the cuts members.

<br>

### 5.1.2. $\mathbb{R}$ is an ordered set.
 
Let $\alpha, \beta \subset \mathbb{Q}$ be two cuts, then we define the binary relation $< \ \subset \mathbb{R}^2$:

$$\alpha < \beta \iff \alpha \subset \beta$$

We say that $\alpha$ is a *proper subset* of $\beta$, which means that any item of $\alpha$ is also an item of $\beta$ but at least one item of $\beta$ do not belongs to $\alpha$, formally:

$$\alpha \subset \beta \iff \alpha \subseteq \beta \wedge \alpha \neq \beta \iff \forall x (x\in \alpha \implies x \in \beta) \wedge \exists b (b\in \beta \wedge b \notin \alpha)$$

Then, $< \ \subset \mathbb{R}^2$ is a *strict total order*:

- **Irreflexivity**: 

    Since $\alpha = \alpha \ \forall \alpha \in \mathbb{R} \implies \neg ( \alpha < \alpha) \ \forall \alpha \in \mathbb{R}$

    <br>

- **Trycothomy**: 

    Let's note that, be $\alpha,\beta \subset \mathbb{Q}$, then, we can think on one of the following posibilities between $\alpha$ and $\beta$

    - First, consider that $\exists b \in \beta : b \notin \alpha$, then the first corolary of the second property asserts that $\forall a(a \in \alpha \wedge b \notin \alpha \implies a < b)$, applying again the second property of the cuts we get that $(b\in \beta \wedge a < b) \implies a \in \beta \implies \alpha \subset \beta$.

    - A similar argument proves that $\exists a \in \alpha : a \notin \beta \implies \beta \subset \alpha$.

    - Now, obviously, if $\neg(\exists b \in \beta : b \notin \alpha) \wedge \neg(\exists a \in \alpha : a \notin \beta)$, counting with the fact that, following the first property of the cuts, $\alpha,\beta \neq \varnothing$ then only can be $\alpha = \beta$.

    In summary, we've just proved the *tricothomy* property for any pair of cuts in $\mathbb{Q}$.

    <br>

- **Transitivity**:

    Also consider $\alpha,\beta,\gamma \in \mathbb{Q}: \alpha< \beta \wedge \beta < \gamma$ we can directly infere that through the transitivity property of the subsets:

    $$\begin{cases} \alpha < \beta \iff \alpha \subset \beta \\ \beta < \gamma \iff \beta \subset \gamma\end{cases} \implies \alpha \subset \gamma \implies \alpha < \gamma$$


<br>

### 5.1.3. $\mathbb{R}$ satisfies the $LUB$ property.

Remember that the LUB property ensures for any ordered set $S$ that satisfy it any non-empty $E \subset S$ subset upper/lower-bounded has supremum/infimum in $S$.

First, suppose there exists $A \subset \mathbb{R} : A \neq \varnothing$ upperbounded with $\beta \in \mathbb{R}$ an upperbound of $A$, let's see that we can find a supremum for it. 

Now we define as:

$$\gamma := \bigcup_{\alpha \in A} \alpha = \Set{p \in \mathbb{Q} \ \vert \ \exists \alpha \in A : p \in \alpha}$$

We will see that $\gamma \in \mathbb{R}$, this is that, as a subset, is also a cut, since it satisfies the three properties mentioned above. Then we will demonstrate that $\gamma$ is an upperbound of $A$ and lastly that is the least upperbound and thus, the supremum of $A$.

First, let's see that $\gamma \in \mathbb{R}$:

1. Then, since $A \neq \varnothing \implies \exists \alpha_0 \in A : \alpha_0 \neq \varnothing$ thus $\exists a \in \alpha_0 \subset \gamma \implies \gamma \neq \varnothing$ 

    Now observe that $\beta \in \mathbb{R}$ is an upperbound of $A$. Since $\beta$ is a cut, it satisfies that it englobes his own left or his behind, meaning $\forall \alpha (\alpha \in A \implies \alpha < \beta \implies \alpha \subset \beta)$ we say that is closed to his left thus is clear that $\gamma \subset \beta \subset \mathbb{Q}$ and is $\gamma \neq \mathbb{Q}$

    <br>

2. Let's consider now $p \in \gamma$ and $q \in \mathbb{Q} : q < p$, immediately we have that 

    $$ p \in \gamma \implies \exists \alpha \in A : p \in \alpha$$

    Since $\alpha \in \mathbb{R}$ then $q < p \implies q \in \alpha \implies q \in \gamma$

    <br>

3. Following the same logic, taking $p \in \gamma$ as before, $p \in \alpha \implies \exists r \in \alpha : p < r$, observe that $r \in \gamma$ for the same reason as $p$ is so $\exists r \in \gamma : p < r$

    <br>

Having verified that $\gamma$ is a cut, then since $\forall \alpha(\alpha \in A \implies \alpha \subset \gamma \implies \alpha < \gamma)$ so $\gamma$ is an upperbound of $A$. 

For $\gamma = supA$ it has also to be the least upperbound, formally, $\gamma$ preceeds any upperbound of $A$:

$$\forall \delta \in \mathbb{R} \quad ([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta)$$

Then let's proceed by reduction absurdio and consider the negation:

$$\neg \forall \delta([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta) \equiv \exists \delta : \neg([\alpha < \delta \quad \forall \alpha \in A] \implies \gamma < \delta)$$

Let's remember that, in classical logic, it is: 

$$p \to q \equiv \neg p \vee q \iff \neg(p \to q) \equiv \neg (\neg p \vee q) \equiv p \wedge \neg q$$

Thus exchanging $p = (\alpha < \delta \quad \forall \alpha \in A)$ and $q= \gamma < \delta$ we have that the negation is

$$\exists \delta \in \mathbb{R} : [(\alpha < \delta \quad \forall \alpha \in A) \wedge (\delta < \gamma)]$$

Which means basically that exists an upperbound that preceeds $\gamma$. Thus, let's consider $\delta$ as above: $\exists \delta \in \mathbb{R} : \delta < \gamma \wedge (\alpha < \delta \ \ \forall \alpha \in A)$. Observe that $\delta < \gamma \implies \delta \neq \gamma$ which means that $\exists \alpha \in \gamma : \alpha \nsubseteq \delta \implies \delta < \alpha$ (due to the trychotomy of the order), thus and $\delta$ would not be an upperbound contradicting the initial assumption. 

So, by reduction absurdio, $\gamma$ has to be the least upper bound; $\gamma = sup A$.

<br>

Thus, we've seen that $\mathbb{R}$ is an ordered set that satisfies $LUB$ property, let's see also that with proper definitions, it can also have field structure, becoming then a complete ordered field.

<br>

### 5.1.4. Addition in $\mathbb{R}$.

If $\alpha, \beta \in \mathbb{R}$ we define: $\alpha + \beta := \Set{a+b \ \vert \ a \in \alpha \wedge b \in \beta}$. We also define $0^\ast \in \mathbb{R}$ as $0^* := \Set{ q \in \mathbb{Q} \ \vert \ q < 0}$, observe that is clear that this last set is a cut.

Now, we verify that the addition's axioms for a field hold in $\mathbb{R}$, with $0^*$ playing the role of $0$. In orther terms, $(\mathbb{R},+)$ is an abelian group:

- **Closure**: $\alpha + \beta \in \mathbb{R} \ \ \forall \alpha, \beta \in \mathbb{R}$. We have to demonstrate that $\alpha + \beta$ is a cut.

    Let's demonstrate that $\alpha + \beta$ satisfies the three properties of a cut. 

    1. $\alpha, \beta \neq \varnothing \implies \alpha + \beta \neq \varnothing$. 
    
        Also suppose that $p,q \in \mathbb{Q}$ are the upperbounds of $\alpha, \beta \in \mathbb{R}$ respectively (we can assume its existance since both of them are cuts and thus proper subsets of $\mathbb{Q}$ so there are indeed elements of $\mathbb{Q}$ out of each subsets), then is clear that $p + q \notin \alpha + \beta \implies \alpha + \beta \neq \mathbb{Q}$. 
        
        Observe that there is something worth to say of upperbounds when speaking about cuts. By definition, $p$ is an upperbound of $X$ iff $x \leq p \ \ \forall x \in X$, but if $X$ were a cut, by the third property if $\exists x_0 : p = x_0 \in X \implies \exists r \in X : p < r$ and $p$ would not an upperbound, thus, when talking about cuts, all upperbounds are always strict upperbounds, the definition of upperbounds always collapses to $x < p \ \ \forall x \in X$ and the cut do not contains it.

        <br>

    2. $p \in \alpha + \beta \wedge (q \in \mathbb{Q} : q < p) \implies q \in \alpha + \beta $ 

        Write $p = a + b$, since $q < p = a + b \implies q - a < b \in \beta$ and thus we get that $q = (q - a) + a \in \alpha + \beta$.

        <br>

    3. $p \in \alpha + \beta \implies \exists q \in \alpha + \beta : p < q$

        This result is almost immediate since if $p = a + b$ then, exists $a' \in \alpha, b' \in \beta$ verifying both $a < a' \wedge b < b'$, thus calling $q = a' + b'$ clearly is $q \in \alpha + \beta : p < q$

        <br>

- **Conmutativity**: $\alpha + \beta = \beta + \alpha \ \ \forall \alpha, \beta \in \mathbb{R}$, it gets immediately derivated from commutativity in $\mathbb{Q}$.

    <br>

- **Asociativity**: $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma \ \ \forall \alpha, \beta, \gamma \in \mathbb{R}$.

    Let's look it closely, we have that the objects in $\mathbb{R}$ can be understanded as:

    $$\alpha + (\beta + \gamma) := \Set{a + p \mid a \in \alpha \wedge p \in \beta + \gamma}$$

    $$(\alpha + \beta) + \gamma := \Set{q + c \mid q \in \alpha + \beta \wedge c \in \gamma}$$

    Observe that also $p \in \beta + \gamma \implies \exists (b , c) \in \beta \times \gamma : p = b + c$ and we can rewrite the expression $a + p = a + (b + c)$, but in $\mathbb{Q}$ is $a + (b + c) = (a + b) + c$ which means that the object $a+p$ lives in the counter part. A similar argument give us the reciproc inclusion ultimately standing that: $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma$.

    <br>

- **Identity**: 

    Let's rememeber that we called $0^\ast:= \Set{q \in \mathbb{Q} \mid q < 0}$, then let's take

    $$t \in \alpha + 0^\ast \implies \exists a \in \alpha \wedge \exists q < 0 : t = a + q$$

    Then, if we consider some other $b \in \alpha : a < b$ (which its existance is garanteed by the third property of the cuts) then, following the axioms for ordered fields, since $q < 0$, is $t = a + q < a + 0 < b$ and then is $t < b \in \alpha \implies t \in \alpha$ for the second property of the cuts.

    Thus, $\alpha + 0^\ast \leq \alpha$.

    Let's also consider $a \in \alpha$ and, again by the third property of the cuts, take $b \in \alpha : a < b$, observe that $a-b < 0 \implies a-b \in 0^\ast$, and is $ a = b + (a - b) \in \alpha + 0^\ast$.

    Thus, $\alpha \leq \alpha + 0^\ast$, meaning that $\alpha = \alpha + 0^\ast$

    Lastly, by the conmutativity property presented before:

    $$0^\ast + \alpha = \alpha + 0^\ast = \alpha \quad \forall \alpha \in \mathbb{R}$$

    <br>

- **Inverse**:

    Fix some $\alpha \in \mathbb{R}$. Then, consider the set:

    $$\beta := \Set{p \in \mathbb{Q} \mid \exists r>0 : -p -r \notin \alpha}$$

    Observe that we are not considering those $p$ whose opposite $-p$ are strictly out from $\alpha$ (this would be $a < -p \ \ \forall a \in \alpha$) but only those $p$ whose opposite has a constant positive gap between themselves and any other element of $\alpha$ abstracted in $r > 0$. Specifically, we are considering the segment simetric (respect the origin) in the rational line to the one that is strictly out by a positive gap from $\alpha$.

    Note that $\beta$ as defined is smaller than $A := \Set{p \in \mathbb{Q} \mid -p \notin \alpha}$ since, $A$ admits a frontier element $p$ for which the elements of $a \in \alpha$ can get as close as wanted. However, with $-p -r \notin \alpha$ the difference between $-p -r$ and $\alpha$, again, can be as small as wanted, but the distance between $-p$ and $\alpha$ can't be smaller than $r$. That gap will always exists between $-p$ and any other element in $\alpha$ so $\beta$'s elements are deeper in $\mathbb{Q} \setminus \alpha$.
    
    Let's see that $\beta \in \mathbb{R}$ and $\alpha + \beta = 0^*$  

    - First, $\beta \in \mathbb{R}$, this means that $\beta \neq \varnothing$ and $\beta \neq \mathbb{Q}$. In order to solve this, let's recover our conception of $\beta$ as the simetric segment to that one that is strictly out from $\alpha$ by a positive gap.

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

With this we already prooved that $(\mathbb{R},+)$ is an abelian group. Observe now that this addition can be considered a traslation, $\alpha + \beta$ is the set that consider the rational addition between any item of $\alpha$ and $\beta$. Since $\mathbb{Q}$ is an ordered field it self, $+ : \mathbb{Q} \times \mathbb{Q} \to \mathbb{Q}$ is a traslation, thus the combination $a + b$ is a traslation that displaces $a$ a $b$ distance on the rational line. 

Observe now that, in $\mathbb{R}$ we have the $LUB$ property which allow us to consider, for any non-empty and upperbounded subset $A \subset \mathbb{R}$ a minimal upperbound. Also, since any cut $\alpha \in \mathbb{R}$ can be treated as a subset it self (of $\mathbb{R}$, specifically, that subset that contains all the cuts that preceds him) we can consider a supreme in $\mathbb{R}$ for any element of $\alpha \in \mathbb{R}$, we can denote it as $sup(\alpha)$. 

Observe then that the own $\alpha + \beta$ has is own supreme, $sup(\alpha + \beta)$ which is furtherest than any $a+b: (a,b) \in \alpha \times \beta$ in the rational line, and thus, that $sup(\alpha)$ or $sup(\beta)$, essentially $sup(\alpha + \beta) = sup(\alpha) + sup(\beta)$. This is how geometrically, the addition in $\mathbb{R}$ adquires form of traslation through the traslation conception defined in the ordered field $\mathbb{Q}$.

In summary, if $\alpha \in \mathbb{R}$ then any $a \in \alpha$ is not further than $sup(\alpha)$ and $\tau_b(a) = a + b$ is not further than $sup(\alpha + \beta)$. Esentally this allow us to extrapole that, be $\alpha < \beta \implies \alpha + \gamma < \beta + \gamma \quad \forall \gamma \in \mathbb{R}$, so the total strict order $< \ \subset \mathbb{R}^2$ has an invariant through the traslations in $\mathbb{R}$.

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

- **Asociativity**; Inmediate from associativity in $\mathbb{Q}$
- **Conmutativity**; Inmediate from conmutativity in $\mathbb{Q}$
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
    
        Let's observe that: $\alpha \alpha^{-1}= \Set{p \mid \exists (a,t) \in \alpha^+ \times {\alpha^{-1}}^+ : p \leq at}$, but let observe: 
        
        $$t \in \alpha^{-1} \implies \exists (y \notin \alpha \wedge y>0) : t < \frac{1}{y} \implies at < \frac{a}{y} < 1$$
        
        Since $a<y$ for being $y \notin \alpha$.

        <br>

    - $1^* \subset \alpha \alpha^{-1}$: 
    
        Let's take note that, demonstrate this inclusion implies to demonstrate that, given any number $p < 1$ we can closer than $p$ to $1$ by finding and multiplicating the elements of a proper pair $(a,t) \in \alpha^+ \times {\alpha^{-1}}^+$.

        First let's take some $p < 1 \implies \exists q > 0 \in \mathbb{Q} : p + q = 1$, so $q$ is the "distance" between $p$ and $1$, let's now take some $\alpha >1$ (we can assume this without loosing generality since otherwise it would be $\alpha^{-1}>1$) and consider some $a \notin \alpha : a - q \in \alpha$, observe $a \notin \alpha \implies \frac{1}{a} \in \alpha^{-1}$, thus:

        $$1 > (a-q)\frac{1}{a} = 1 - \frac{q}{a} > 1 - q = p$$

        Observe that $\alpha > 1 \implies a >1 \implies q > \frac{q}{a}$.

        <br>

    At the end, we have that $1^* = \alpha \alpha^{-1}$.

    <br>

Now that we prooved that $(\mathbb{R}^+,\ ·)$ is an abelian group, let's extend to $\mathbb{R}$ this same operation.

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

Let's see that $\mathbb{Q} \subset \mathbb{R}$. Is worth to make a previous comentary about this statement. Formally is an abuse of language, in strict terms, $\mathbb{Q}$ is not part of $\mathbb{R}$ because their elements are simply not the same.

Mathematically, we don't care about what things are made, mathematicians often don't know about what are they talking about, but they are pretty sure about what are saying which is not the same. In other words, what we care about is how elements relate between them. Thus, two structures whose elements behaves exactly the same way are externally indistinguishable and, for any structural purpouse, exchangeable.

The object that allows us to identify two equivalent structures is the *isomorphism*, in this case *field's isomorphism*. This is a biyection that allows to translate a structure to another, identifying pairs of elements from both set and implicating rules that preserve the behavior through the image of the isomorphism.

Let's consider $\varphi:\mathbb{Q}\xrightarrow{\ \sim\ }\mathbb{Q}^\ast$ such: $q \mapsto q^\ast = \Set{p \mid  p < q}$, is clear that $q^\ast \in \mathbb{R}$ is the cut formed by the behind of $q$.

First, let see that $\varphi$, as defined is a *field homomorphism*:

1. $\varphi(p+q) = \varphi(p) + \varphi(q)$

2. $\varphi(pq) = \varphi(p) \varphi(q)$

    <br>

Observe that this much is true and is already prooved above, that the segment of the addition is the addition of the segments and the product of the segment is the segment of the product.

Observe also that each cut in $q^\ast \in \mathbb{Q}^\ast$ has a preimage through $\varphi$ and reverse, so $\varphi$ is biyective and is and field isomorphism, implying that $p\neq q \implies \varphi(p) \neq \varphi(q)$.

Lastly, consider some $p, q \in \mathbb{Q} : p < q$, we already know that $\varphi(p) \neq \varphi(q)$ but also observe that is pretty clear: $\forall t \big(t \in \varphi(p) \implies t <p < q \implies t \in \varphi(q)\big) \implies \varphi(p) < \varphi(q)$, a similar argument prooves $\varphi(p) < \varphi(q) \implies p<q$, thus $p<q \iff \varphi(p) < \varphi(q)$.

So $\varphi$ is an *isomorphism of ordered fields* meaning that $\mathbb{Q} \simeq \mathbb{Q}^\ast \subset \mathbb{R}$ and we can exchange $q$ and $q^\ast$ in the real number context.

<br>

With this, we conclude the presentation of $\mathbb{R}$ as a strict ordered field that also satisfies $LUB$ property, we say then that $\mathbb{R}$ is *ordered* and *complete*.

In fact, despite this result will not be prooved: any two ordered fields with
the least-upper-bound property are isomorphic, meaning that **$\mathbb{R}$ is THE ordered and complete field**.

<br>

## 5.2. Important Properties from the $\mathbb{R}$ field.

### 5.2.1. Archimedean property of $\mathbb{R}$.

We've nound this property before in the construction of $\mathbb{R}$ without properly defined it. This property says that every cuantity in $\mathbb{R}$ is reachable by considering a positive value a finite number of times. It is a powerful statement since it basically says that every point on the real line is reachable by any positive value repeated a finite number of times. 

This can be explained in other terms, the archimedean property says that $\mathbb{N}$ is unbounded on $\mathbb{R}$, there is always a natural number that can reach and surpass any real cuantitiy. 

Meaning that $\mathbb{R}$ has no "infinitely large" or "infinitely small" elements; no matter how small a positive number $x$ you pick and no matter how large a target $y$, you can always reach (and surpass) $y$ by adding $x$ to itself enough times. Formally:

$$\forall x\forall y (0 < x \implies  \exists n \in \mathbb{N} : y < nx)$$

By absurdio reduction: 

Let's observe that:

$$\neg \forall x\forall y (0 < x \implies  \exists n \in \mathbb{N} : y < nx) \equiv \exists x\exists y (0 < x \wedge  y > nx \quad \forall n \in \mathbb{N})$$


Thus, lets fix $x > 0$ and consider the set $A:=\Set{nx \ \vert \ n \in \mathbb{N}}$ upperbounded by $y$ as the statement says. By the $LUB$ property in $\mathbb{R}$ we can consider $\alpha = sup(A) \in \mathbb{R}$. 

This way, we have that:

$$\alpha - x < \alpha \implies  \exists m \in \mathbb{N} : \alpha - x < mx \iff \alpha < (m+1)x \in A \implies \alpha \neq sup(A)$$

<br>

### 5.2.2. $\mathbb{Q}$ is dense in $\mathbb{R}$

The density of $\mathbb{Q}$ in $\mathbb{R}$ stablish that between two elements of $\mathbb{R}$ a rational always can be found, formally:

$$\forall x, y \in \mathbb{R} : x < y \implies \exists q \in \mathbb{Q} : x < q < y$$

Let's observe that, considering $x \in \mathbb{R}\setminus \mathbb{Q}$, then taking some $q \in y \setminus x$ we have that is $x < q < y$, but observe that this argument doesn't apply to every real, the exception is made when is a rational real:

$$x \in \mathbb{Q} \subset \mathbb{R} \implies x \in y \setminus x$$

The existance of another $q \neq x : x < q < y$ need to be prooved.

To demonstrate it, lets think about $x, y \in \mathbb{R} :x < y$, thus is $ 0 < y - x$ so for $1 \in \mathbb{R}$, the archimedean property furnishes the result: $1 < n(y-x)$.

Also, considering $z_1,z_2 \in \mathbb{R}^+ \implies \exists t_1,t_2 \in \mathbb{N}: nx < t_1z_1 \wedge -nx < t_2z_2$. Then, calling $m_i = t_iz_i$ is:

$$-m_2 < nx < m_1$$

We can nail $[-m_2,m_1] \cap \mathbb{Z}$ until find an $m \in \mathbb{N} : m-1 \leq nx < m$, in summary:

$$\begin{cases} 1 < n(y-x)  \iff 1 + nx < y \\ m - 1 \leq nx < m \iff m \leq 1 +nx < m +1  \end{cases} \implies nx < m \leq 1 + nx < ny$$

And thus:

$$x < \frac{m}{n} < y$$

Observe that this calls for we can approximate any real through rational values. Think that for any $x \in \mathbb{R}$ we can think in $x < x +1 \implies \exists y \in \mathbb{Q} : x < y < x + 1$, but since $\mathbb{Q} \subset \mathbb{R} \implies y \in \mathbb{R}$ and the result tell us that exists another $q \in \mathbb{Q} : x < q < y$ and so on.

<br>

### 5.2.3. *nth* roots of positive reals.

As we said before, in $\mathbb{Q}$ there isn't any $q \in \mathbb{Q} : q^2 = 2$, we are now going to see that this problem is handled in $\mathbb{R}$.

Specifically, we are going to see that for any positive real and any positive integer exists a unique positive real such $y^n = x$, formally:

$$\forall (x,n) \in \mathbb{R}_{>0} \times  \mathbb{Z}_{>0} \ \exists ! y \in \mathbb{R}_{>0} : y^n = x$$

We say that $y$ is the $n$-th root of $x$ and we denote it as $y = \sqrt[n]{x} = x^{\frac{1}{n}}$.

<br>

That there is at most one such $y \in \mathbb{R}$ is clear, since $\forall y\forall x(0 < y < x \implies y^n < x ^n)$, remember that strict total order $< \ \subset \mathbb{R}^2$ requires irreflexivity, meaning that $y^n < x^n \implies y^n \neq x^n$, obviously.

<br>

Now, let's demonstrate the existance if such number. Consider now the following set:

$$E := \Set{t \in \mathbb{R} \mid t^n < x}$$

This set is not-empty and has an upperbound:

- First, is not empty, consider $t = \frac{x}{1+x} \implies 0 < t < 1$. Now, let's reason by induction over $n$:

    - If $n = 2$, then, by $4.3.2-(2)$ is $0 < t < 1 \implies 0 < t^2 < t$.
    - Now, considered true by some $n$, again: $0 < t^n < 1 \implies 0 < t^{n+1} < t$

    Thus $t^n < t \ \ \forall n \in \mathbb{N}$ of course, is also $t < x$ as defined so $t \in E$.

    <br>

- Second, is upperbounded, consider $t \in \mathbb{R} : 1 + x < t \implies x < t \leq t^n$ and $1+x$ is an upperbound of $E$. Thus, we can consider the $y=sup(E)$ verifying necesarily $y^n = x$. (Although the proof of this last afirmation is not provided, is too complicated and the result, as presented, is intuitively enough to be accepted).

    <br>

Let's observe that $(ab)^{\frac{1}{n}} = a^{\frac{1}{n}}b^{\frac{1}{n}}$, take $\alpha = a^{\frac{1}{n}} \iff \alpha ^n = (a^{\frac{1}{n}})^n = a$. Thus,  

$$(ab)^{\frac{1}{n}} = ((\alpha \beta)^n)^{\frac{1}{n}} = \alpha \beta = a^{\frac{1}{n}}b^{\frac{1}{n}}$$

The step $\alpha^n \beta^n = (\alpha \beta)^n$ is taken by the conmutative property in the abelian group $(\mathbb{R}, \ ·)$.

<br>

## 5.3. Brief summary about $\mathbb{R}$.

Let's make a brief recapitulation about what numbers are and how the conception of number changes when we talk about $\mathbb{R}$.

Maths are abstractions of natural concepts with which we colive, specifically, numbers in a traditional way represent *cuantities*. $\mathbb{N}$ setup something we call unity or first element (which can be $0$ or $1$ depending on the convention, generally, $0$ is not a natural number) and define the rest of his elements by *succession*, thus, what place a number occupies in the iterative succession line represents how many time this identity is in this element which defines its value in an aritmetic sense; $n \in \mathbb{N}$ is literally $n$ times $1$.

Then, the $0$ represent the abscense of cuantity and the negative numbers the debt and laterly the fractions changes the unity value (from which we extract the value of the rest of the elements as we see above) allowing to access to intermediate values intermediate values in the succession line. Thus, $\mathbb{Z}$ and $\mathbb{Q}$ expands the cuantity concept but we still talking about cuantities. 

We already explained this in other terms by announcing the $LUB$ property, but we can now bring another perspective conceptually more ilustrative of the inadequatness of $\mathbb{Q}$. Since $\mathbb{Q}$ consider cuantities it makes his items totally disconected, meaning that we can made an split of $\mathbb{Q}$ by defining: 

$$U=\{q\in\mathbb{Q}: q^2<2\ \vee \ q<0\},\qquad V=\{q\in\mathbb{Q}: q>0 \vee \ q^2>2\}$$

Observe that $U \cup V = \mathbb{Q}$ and neither of the two contains $p : p^2 = 2$, as if apparently this gap is never filled in $\mathbb{Q}$, like if there isn't no bridge between $U$ and $V$ that, however, builds $\mathbb{Q}$. This is a rational question involving rationals without a rational response, meaning that $\mathbb{Q}$ can't represent unconmensurable entities despite being "surrounded" by them, and is worth to enphasize the term "surrounded" because a lot of rationals get squeezed on the neighborhood of $p$ without never reach it. This unconmensurable entities manifest them selves as non-reachable frontiers to which we can approximate as much as we want.

$\mathbb{R}$ solves this by stop considering his elements as numbers or cuantities, but as *positions* in a line which, by definition, is continuous and any position (any "point") in the line is defined. In some informal sense, this real line is now "complete". 

This is achieved by changing $\mathbb{Q}$ arquitecture, tecnically, $\mathbb{R}$ and $\mathbb{Q}$ share the same substratum, rational numbers, but elements of $\mathbb{R}$ are subsets that satisfies certains properties; segments that "cut" the so called line at any point. The $LUB$ property offers a garantee that any bounded agrupation of this segments has a supremum, meaning that any subset that gets near to this frontiers non defined in $\mathbb{Q}$ has supremum in $\mathbb{R}$ in which the frontier, the non-measurable value, can be instantiated, filling this gaps from $\mathbb{Q}$.

The natural interpretation of a *cut* is an object that aims to a position in $\mathbb{R}$ cutting in two the line, this way, this so addresed position is characterized by what has back (which automatically characterizes what has in front). So the elements of $\mathbb{R}$ are positions in the line concretized by what surrounds it. This is why, in $4.3.1$ we care about present operations of an ordered field with a geometric nuance, because in $\mathbb{R}$ we do operate with positions in a geometric sense, the unique kind of "cuantities" we could consider in $\mathbb{R}$ are those which can be identified with rational elements as we see $5.1.6$.

<br>

Lastly, let's see what the three properties presented in $5.2$ tell us about $\mathbb{R}$:

- **Arquimedean Property** states that any position in the line is reachable or surpasable by traslating a positive value a finite number of times.

- **$\mathbb{Q}$ density** tell us that we can get closer enough to any position in $\mathbb{R}$ with a rational approach.

- **nth-roots of positive real values**; tell us that any positive position is reachable by dilatating a finite number of times some positive value.

    <br>

# 6. The extended Real Number System.

## 6.1. Definition.

The extended real number sistem consist in form the set $\overline{\mathbb{R}} := \Set{\mathbb{R},+\infty,-\infty}$ defining:

$$-\infty < x < +\infty \quad \forall x \in \mathbb{R}$$

This way, observe that we have defined $-\infty, +\infty$ as lower/upper bounds of any subset of $\mathbb{R}$, **thus any subset in $\mathbb{R}$ is now bounded in $\overline{\mathbb{R}}$ and has a least upper bound**: for example, $E$ is a nonempty set of real numbers which is not bounded above in $\mathbb{R}$, then $\sup E = +\infty$ in the extended real number system. 

<br>

## 6.2. Operations in $\overline{\mathbb{R}}$.

**The extended real number system does not form a field**, but it is customary
to make the following conventions (in the following cases $\infty = +/- \infty$): 

$$\begin{cases} x +/- + \infty = + \infty \\ x +/- - \infty = - \infty \\ \displaystyle\frac{x}{+\infty} = \displaystyle\frac{x}{-\infty} = 0 \\ x \ · + \infty = +\infty \wedge x \ · -\infty = - \infty \quad x > 0 \\ x \ · + \infty = -\infty \wedge x \ · -\infty = + \infty \quad x < 0 \end{cases}$$

In this context, we say that real numbers are *finite*, while $+\infty,-\infty$ are both, *infinite*.

<br>

# 7. Summary. Analisis.

Until now, in  basic terms we've presented the rational numbers $\mathbb{Q}$ and evidenced some flaws in it as we develop in $5.3$. From $\mathbb{Q}$ we develop $\mathbb{R}$ as a complete ordered field ($LUB$) whose elements are no longer measurable cuantities but positiones in a continuous line, and lastly we stated that it is unique, meaning that any other complete ordered field is isomorph to $\mathbb{R}$.

Then, let's explain the need of this upgrade and how it relates with the Analisis and what is in fact Analisis as a mathematician discipline.

<br>

Analisis is the matematician field which studies properties or objects by using the **limit**; which is a infinite aproximation process that returns a finite output. All analisis main's objects like derivates, integrals, continuity, etc are essentially limits.

For the limit to have sense as an object two main ingredients are needed:

- *Proximity notion*: A *metric*, which in $\mathbb{R}$ emerges from the *order*. How ever the order is not necesary for a metric to exists and $\mathbb{C}$ is the best example of it.

- *Completness*: which garantees that the object of the approximation actually exists. $LUB$ garantees $\mathbb{R}$ completness.

Thus, the limit is gradual approach to an existing object.

