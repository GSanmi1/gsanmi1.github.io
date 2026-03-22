---
layout: post
title: "The Real and Complex Number Systems"
subtitle: "Real and Complex fields presentation and properties."
date: 2026-03-05 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
---

# 0. Index

# 1. Introduction.

A satisfactory discussion of the main concepts of analysis (such as convergence,
continuity, differentiation, and integration) must be based on an accurately
defined number concept. 

We will pressume familiarity with $\mathbb{Q}$ and use this knowledge to build $\mathbb{R}$ and then $\mathbb{C}$

<br>

## 1.1. Rational numbers inadequatness.

The rational number system is inadequate for many purposes, both as a
field and as an ordered set. For instance, there is no $p \in \mathbb{Q} : p^2 = 2$.

Let's consider that $\exists p \in Q: p^2 = 2 \implies \exists m,n \in \mathbb{Z} : p = \frac{m}{n}$. 


Let's also observe that if $m, n \in \mathbb{2Z}$, then we could divide between $2$ the numerator and denominator and the fraction will still reflects $p$ and $m,n \in \mathbb{2Z}$ so we could divide again, and eventually this iteration process of divide between 2 must terminate and one of the two must be odd. 

So we can ensure without loss generality that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$ and at least one of both is not even. Then, the equation imposes that $m$ is even:

$$p^2 = \left(\frac{m}{n}\right)^2 = \frac{m^2}{n^2} = 2 \iff m^2 = 2n^2 \in 2\mathbb{Z}$$

Let's observe that $m \in \mathbb{2Z} \implies m \vert 2 \implies m^2 \vert 4 \iff 2n^2 \vert 4 \implies n^2 \in \mathbb{2Z}$ and also $n$ is even contradicting the presumption.

<br>


This leads to the introduction of so-called "irrational numbers" which are often written as infinite decimal expansions and are considered to be "approximated" by the corresponding finite decimals. 
 
When we talk about aproximations we talk about "1, 1.4, 1.41, 1.414, 1.4142,..." and so on tends to $\sqrt 2$, but before that we have to define what "tends" or "approximates" means. 

<br>

Let's also observe that we can consider the following sets: $A:= \Set{p \ \vert \ p^2 < 2 }, B:= \Set{p \ \vert \ p^2 > 2 } \subset \mathbb{Q}$ and demonstrates that $A$ no contains smallest number and $B$ no contains greater but none of them contains the point it self (since is not rational):

$$q = p - \frac{p^2 -2}{p+2}: p \in \mathbb{Q}$$

- Check that if $p \in A \implies p^2 < 2 \iff p^2 - 2< 0 \implies q > p$, and also  observe that: 

    $$ q^2 - 2 = \left( p - \frac{p^2 -2}{p+2} \right)^2 - 2 = \left(\frac{2p + 2}{p+2} \right)^2 - 2 = \frac{2(p^2 - 2)}{(p+2)^2}$$

    Hence, $p^2 - 2 < 0 \implies q^2 - 2 < 0 \implies q \in A$. Thus we can ennonce that:

    $$\forall p \in A \ \exists q \in A:  q > p$$

- Let's also observe using the same definition, $p \in B \implies q \in  B \wedge p > q$ which means that also is:

    $$\forall p \in B \ \exists q \in B:  q < p$$


The purpose of the above discussion has been to show that the rational number system has certain gaps, in despite of the fact that between any two rationals there is another:

$$ r,s \in \mathbb{Q} : r < s \implies r < \frac{r + s}{2} < s \wedge \frac{r + s}{2} \in \mathbb{Q}$$

The *real number system* fills these gaps. This is the principal reason for the fundamental role which it plays in analysis.

<br>

# 2. Ordered Set and Fields.

In order to elucidate its structure, as well as that of the complex numbers, we start with a brief discussion of the general concepts of ordered set and field.

<br>

## 2.1. Binary Relations.

**Binary Relations and Orders.**

Given a set $X$, a binary relation on $X$ is a subset: $R \subseteq X \times X$ and we write as a shorthand, being $x,y \in X$, then:

$$xRy \iff (x,y) \in R$$

We call to $R$ as an order, and, defined along certains conditions, we abstract the idea that $x$ preceeds $y$ through $R$ and we represent it such as $(x,y) \in R$

Then, any binary relation $R$ must satisfy the following three condition to be called a *order*:

- **Reflexive**: $xRx \ \ \forall x \in X$
- **Transitive**: $xRy \wedge yRz \implies xRz \ \ \forall x,y,z \in X$
- **Antisimetric**: $xRy \wedge yRx \implies x = y \ \ \forall x,y \in X$

<br>

**Partial and Total Order**

When we define a binary relation $R$ over a set $X$ then is pertinent to ask if:

$$xRy \vee yRx \ \ \ \forall x,y \in R$$

If $x$ and $y$ are incomparable then we write:

$$\neg(xRy) \wedge \neg (yRx) \iff x \ \vert \vert \ y$$

We say that $R$ defined in $X$ is: 

$$R \text{ is a partial order } \iff \exists x,y \in X : x \ \vert \vert \ y$$
$$R \text{ is a total order } \iff xRy \vee yRx \ \ \ \forall x,y \in R$$

<br>

**Strict and non-strict order**

An order can be defined considering if some element can relate with him self or not ($xRx$) in the sense that if non-strict or strict order.

Being $X$ a set and $R$ a binary relation, then:

$$ R \text{ is non-strict order} \iff xRx \ \forall x \in R$$
$$ R \text{ is strict order} \iff \exists x \in X : (x,x) \notin R$$

Let's observe that, being $M_{xy}$ predicates over $x$ and $y$ that must be satisfied to be $xRy$, then in the non-strict order is always $M_{xx} \equiv \top$, then we can say: 

$$xRy \iff M_{xy} \vee x = y : M_{xy} \otimes M_{yx}$$

Let's observe that by how the predicates $M$ are defined, $R$ as a non-strict order verifies:

$$xRy \wedge yRx \iff x = y$$

Equivalently, if exist at least one $x \in X: (x,x) \notin R$, then $R$ definition must impose diferenciation between two elements for these to be relatable:

$$xRy \iff M_{xy} \wedge x \neq y$$

<br>

## 2.2. Ordered Sets. Bounds. 

**Definition, order in $\mathbb{Q}$**

An ordered set is simply a set in which an order relation has been defined. Let's consider for example $\mathbb{Q}$ the set of rational numbers and the binary relation:

$$\leq \  \subseteq \mathbb{Q} \times \mathbb{Q}: q \leq p \iff p - q \in \mathbb{Q}^+ \cup \Set{0}$$

We consider:

- $p - p = 0 \iff p \leq p \ \ \forall p \in \mathbb{Q}$ (Reflexivity)

- $q \leq p \wedge t \leq q \implies p - t = (p - q) + (q - t) \in \mathbb{Q}^+ \cup \Set{0} \implies t \leq p$ (Transitivity)

- $p \leq q \wedge q \leq p \implies p - q \in \mathbb{Q}^+ \cup \Set{0} \wedge q - p = -(p-q) \in \mathbb{Q}^+ \cup \Set{0} \implies p - q = 0 \iff p = q$ (Antisimetric)

<br>

So $\leq$ is an order, let's see that also is a total order: $p-q \geq 0 \vee q - p \geq 0  \ \ \forall p,q \in \mathbb{Q} \implies p \leq q \vee q \leq p \ \ \forall p,q \in \mathbb{Q}$

<br>

**Bounded. Upper and Lower bounds of a set. Supremum and Infimum.**

Consider now $S$ and ordered set and $E \subset S$, then we say that:

$$E \text{ is upperbounded} \iff \exists \alpha \in S: x \leq \alpha \ \ \ \forall x \in E $$

We define as lower upperbound to  

$$\alpha ' \in S : x \leq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \leq \alpha \ \ \forall \alpha \in S: x \leq \alpha \ \ \forall x \in E )$$

And we denote it as $\alpha ' = sup E$ and call it the supremum of $E$.

This same idea applies to lowerbounds:

$$E \text{ is lowerbounded} \iff \exists \alpha \in S: x \geq \alpha \ \ \ \forall x \in E $$

And we define the *ínfimum* of $E$ (and we denote it to $\alpha ' = inf E$) to:

$$\alpha ' \in S : x \geq \alpha ' \ \ \ \forall x \in E \wedge (\alpha ' \geq \alpha \ \ \forall \alpha \in S: x \geq \alpha \ \ \forall x \in E )$$

<br>

**Example of bounds in subsets of $Q$**

1. Let's consider again $A:= \Set{p \ \vert \ p^2 < 2 }, B:= \Set{p \ \vert \ p^2 > 2 } \subset \mathbb{Q}$. Note check that both are ordered subsets of the rational numbers.

    The set $A$ is bounded above. In fact, the upper bounds of $A$ are exactly the members of $B$. Since $B$ contains no smallest member, $A$ has no least upper bound in $\mathbb{Q}$. Similarly, $B$ is lowerbounded and the lower bounds of $B$ are the elements of $A$. 

    <br>

2. Being $E \subset S$ , then $\exists \alpha = supE$ implies that $\alpha$ may or may not be member of $E$. For instance, $E_1:=\Set{r \ \vert \ r < 0}$ and $E_2:=\Set{r \ \vert \ r \leq 0}$ then $\alpha = supE_1 = supE_2 = 0 \wedge \alpha \notin E_1 \wedge \alpha \in E_2$

    <br>

3. Let be, $E:=\Set{ \left(\frac{1}{n}\right)_{n \in \mathbb{N}}}$, then $supE = 1 \in E \wedge infE = 0\notin E$

<br>

## 2.3. Fields.

### 2.3.1. Definition and Axioms.

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

Also, The field axioms clearly hold in $\mathbb{Q}$, the set of all rational numbers, if addition and multiplication have their customary meaning.

<br>

### 2.3.2. Immediate properties.

Although it is not our purpose to study fields (or any other algebraic structures) in detail, it is worthwhile to prove that some familiar properties of Q are consequences of the field axioms; once we do this, we will not need to do it again for the real numbers and for the complex numbers. 

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

    In our case $p$ is an implication $p:= l \to t \equiv \neg l \vee t \iff \neg p := l \wedge \neg t$, (remember that conjuntion and disjuntionrelates each other as:  $\neg (p \wedge q) \equiv \neg p \vee \neg q$) thus, we are considering that $\underbrace{(x \neq 0 \wedge y \neq 0)}_l \wedge \underbrace{xy = 0}_{\neg t}$ but this is imposible since: $x \neq 0 \wedge xy = 0 \implies y = 0$ (following the axioms described above) entering in contradiction with the premisse, thus: $x \neq 0 \wedge y \neq 0 \implies xy \neq 0$. 

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

### 2.3.3. Ordered fields.

#### 2.3.3.1. Definition.

An *ordered field* is a field $F$ which is also an ordered set, such
that, being $x,y,z \in F$:

- $x+y < x+z \iff y < z$

- $ xy > 0 \implies x > 0 \wedge y > 0$. 

We also say that $x  \in F$, then:

- $x \text{ is positive } \iff x > 0$
- $x \text{ is negative } \iff x < 0$

<br>

#### 2.3.3.2. Properties of ordered sets.

All the familiar rules for working with inequalities apply in every ordered field: Multiplication by positive/negative quantities preserves/reverses inequalities, no square is negative, etc. 

The following proposition lists some of these, considering:

- $x > 0 \iff -x < 0$

    Let's demonstrate it by absurdio reductio which is:

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

- $x > 0 \wedge y < z \iff xy < xz$

    Let's observe that:

    $$y < z \iff 0 = y + (-y) < z + (-y)$$
    
    This way, counting with $x >0$ and using the second axiom of the ordered fields, we have:

    $$0 = x0 < x(z + (-y)) = xz + x(-y) = xz + (-xy) \iff xy < xz$$

    <br>

- $x < 0 \wedge y < z \implies xy > xz$

    Let's observe that we have $y < z \iff y - z < 0 \iff - (y - z) > 0$, thus, taking the second axiom of ordered fields and that $(-x)(-y) = xy$ is:

    $$\begin{cases} -(y - z) > 0 \\ -x > 0 \end{cases} \implies (-x)[-(y - z)]  = x(y -z )> 0$$

    And ultimately: $xy > xz$

    <br>

- $x \neq 0 \implies x^2 > 0$

    Observe that:
    
    $$x \neq 0 \implies \begin{cases}x>0 \implies xx = x^2 > 0 \\ x < 0 \iff -x < 0 \implies (-x)(-x) = xx = x^2 >0 \end{cases}$$

    As a particular case is $1^2 = 1 > 0$

    <br>

-  $0 < x < y \implies 0 < \displaystyle\frac{1}{x} < \frac{1}{y}$
    
    Observe that, since $x \neq y \neq 0 \implies \exists x^{-1},y^{-1} \in F$. Let's also observe that, before, above, we see that $1 > 0$, then $1=xx^{-1} \wedge x > 0 \implies x^{-1} > 0 \ \ \forall x \in F : x > 0$ and we can argument that:

    $$0 < x < y \iff 0x^{-1} < xx^{-1} = 1 < yx^{-1} \iff y^{-1}0x^{-1}< y^{-1} <y^{-1}yx^{-1} = x^{-1}$$

    Resulting $0 < x < y \iff 0 < y^{-1} < x^{-1}$

    <br>

# 3. The Real field.