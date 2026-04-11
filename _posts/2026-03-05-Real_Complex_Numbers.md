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

We will pressume familiarity with $\mathbb{Q}$ (meaning that we assume the sentence "$(\mathbb{Q},+, \ ·)$ is a field and the axioms for the field's algebraic structure applies in its totality." is completely understanded and acknowledge by the reader) and use this knowledge to build $\mathbb{R}$ and then $\mathbb{C}$.

<br>

## 1.1. Rational numbers inadequatness.

Let's start talking about some lackness on the rational numbers.
The rational number system is inadequate for many purposes, both as a
field and as an ordered set since the rational number line is full of gaps. 

For instance, there is no $p \in \mathbb{Q} : p^2 = 2$.

Let's consider that $\exists p \in Q: p^2 = 2 \implies \exists m,n \in \mathbb{Z} : p = \frac{m}{n}$. 


Let's also observe that if $m, n \in \mathbb{2Z}$, then we could divide between $2$ the numerator and denominator and the fraction will still reflects $p$ and $m,n \in \mathbb{2Z}$ so we could divide again, and eventually this iteration process of divide between $2$ must terminate because eventually one of the two must be odd. 

So we can ensure without loss generality that $\exists m,n \in \mathbb{Z} : p = \frac{m}{n}$ and at least one of both is not even. Then, the equation imposes that $m$ is even:

$$p^2 = \left(\frac{m}{n}\right)^2 = \frac{m^2}{n^2} = 2 \iff m^2 = 2n^2 \in 2\mathbb{Z}$$

Let's observe that $m \in \mathbb{2Z} \implies m \vert 2 \implies m^2 \vert 4 \iff 2n^2 \vert 4 \implies n^2 \in \mathbb{2Z}$ and also $n$ is even contradicting the presumption.

<br>

This leads to the introduction of so-called "irrational numbers" which are often written as infinite decimal expansions and are considered to be "approximated" by the corresponding finite decimals. When we talk about aproximations we talk about $1, 1.4, 1.41, 1.414, 1.4142,...$ and so on tends to $\sqrt 2$, but before that we have to define what "tends" or "approximates" means. 

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

In order to elucidate its structure we have to introduce an importante property related to order. So let's start introducing a minimal basis about order in a set.

<br>

## 2.1. Ordered Sets.

Let $S$ be a set. Then, we define as an *order* on $S$ to a binary relation such:

$$< \ \subset S^2 : (x,y) \in \ < \iff x < y$$

For now on we will use the $x<y$ notation. $<$ as a binary relation needs to satisfy the following properties:

1. **Trichotomy**:

    The trichotomy property states that 
    
    $$\forall x \forall y( x \neq y \implies x < y  \vee y < x)$$
    
    Meaning that for any $x,y \in S$, then only one of the following statements is true:

    $$x < y \quad \quad y < x \quad  \quad x = y$$

    <br>

2. **Transitivity**:

    Transitivity states that:

    $$\forall x \forall y \forall z (x < y \wedge y < z \implies x < z)$$

    <br>

Also, from the notation above we build the following notation:

$$x \leq y \iff x < y \vee x = y$$

Satisfying that: 

$$\neg(x < y) \equiv y \leq x$$

<br>

## 2.2. Order in $\mathbb{Q}$.



Let's consider for example $\mathbb{Q}$ the set of rational numbers and the binary relation:

$$< \  := \Set{(p,q) \in \mathbb{Q}^2 \ \vert \ q < p \iff p - q \in \mathbb{Q}^+}$$

Then, this binary relation on $\mathbb{Q}$ satisfies:


- Be $p,q \in \mathbb{Q}$, then $p-q \in \mathbb{Q}^+ \vee -(p-q) = q - p \in \mathbb{Q}^+ \vee p-q = 0$, which essentially give us the trichotomy property.

    <br>

- Also observe that $q < p \wedge t < q \implies p - t = (p - q) + (q - t) \in \mathbb{Q}^+ \implies t < p$ which means that also satisfies transitivity.

<br>

So $<$ is an order on $\mathbb{Q}$.

## 2.3. Bounds. 

Until now, we just defined that an ordered set is simply a set in which an order relation has been defined and also define an order in $\mathbb{Q}$. 

Let's introduce the concept of *bounds*, and naturally extract the concept of the *minimal bound* for a set.

<br>

### 2.3.1. Upper and Lower bounds of a set. Supremum and Infimum.

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

### 2.3.2. Example of bounds in subsets of $Q$.

Let's now observe two examples in which we want to ilustrate two facts about minimal bounds.

**The first one ilustrates that in $\mathbb{Q}$ minimal bounds are not garanteed to exists for any bounded set $S \subset \mathbb{Q}$, and this is the main reason why $\mathbb{Q}$ is full of gaps.**

The second example pretend to ilustrate that, although the definition of bound do not prohibit a minimal bound of $E$ to be contained in $E$, this is not true in general, a minimal bound often is not a member of the bounded subset.

1. Let's consider again $A:= \Set{p \ \vert \ p^2 < 2 }, B:= \Set{p \ \vert \ p^2 > 2 } \subset \mathbb{Q}$. 

    The set $A$ is bounded above. In fact, the upper bounds of $A$ are exactly the members of $B$. Since $B$ contains no smallest member, $A$ has no least upper bound in $\mathbb{Q}$. Similarly, $B$ is lowerbounded and the lower bounds of $B$ are the elements of $A$. But since $\nexists p \in \mathbb{Q} : p^2 = 2$ neither of the two has minimal bound.

    <br>

2. Being $E \subset S$ , then $\exists \alpha = supE$ implies that $\alpha$ may or may not be member of $E$. For instance, $E_1:=\Set{r \ \vert \ r < 0}$ and $E_2:=\Set{r \ \vert \ r \leq 0}$ then $\alpha = supE_1 = supE_2 = 0 \wedge \alpha \notin E_1 \wedge \alpha \in E_2$

    <br>

    Also, let be, $E:=\Set{ \left(\frac{1}{n}\right)_{n \in \mathbb{N}}}$, then $supE = 1 \in E \wedge infE = 0\notin E$

<br>

### 2.3.3. Least-upper-bound property.

Now, we have presented order, bounds, minimal bounds and we also provided an example to ilustrate that minimal bounds sometimes do not exists. 

Then in this section we are going to present the ***Least-upper-bound property*; this property garantee the existance of the minimal bound for any bounded and non-empty subset of an ordered set in which this property is true.**

<br>

**Definition**

An ordered set $S$ is said to have the least-upper-bound property if the following statement is true: being $E$ an upperbounded non-empty subset of $S$, then the supremum of $E$ exists in $S$. Formally: 

$$ \forall E \subseteq S : (E \neq \varnothing \wedge \exists \alpha \in S : x \leq \alpha \ \ \forall x \in E) \implies \exists \alpha_s = supE : \alpha_s \in S $$


<br>

**Theorem**

Now, the following theorem introduces that the least-upper-bound property is a sufficent condition to ensure the existance of an *infimum* for any non-empty lowerbounded subset of an ordered set that satisfies the so called property and also offers a characterization of the object.

Let's consider an ordered set $S$ that satisfies the least-upper-bound property and a non-empty, lowerbounded, subset $B \subseteq S$. 

Then, we call $L$ to the set of all the lowerbounds of $B$ in $S$:

$$L_B := \set{\alpha \in S : \alpha \leq x \ \ \forall x \in B}$$

Since $L_B$ is clearly upperbounded by any item of $B$ and $S$ satisfies the least-upper-bound property, then we can talk about an $\alpha_s \in S : \alpha_s = supL_B$. Observe that:
 
$$ \alpha_s = supL_B \implies \begin{cases} \nexists b \in B: b < \alpha_s  \\ \nexists l \in L_B : l > \alpha_s \end{cases} \implies \alpha_s = infB$$

The first condition tell us that $\alpha_s$ is a lowerbound, the second tell us that there isn't any other lowerbound $l$ bigger than $\alpha_s$, thus, it must be the infimum.





Then, we have:

$$ \exists \alpha_s \in S: \alpha_s = supL_B = infB$$

<br>

## 2.4. Fields.

### 2.4.1. Definition and Axioms.

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

### 2.4.2. Immediate properties.

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

### 2.4.3. Ordered fields.

#### 2.4.3.1. Definition.

An *ordered field* is a field $F$ which is also an ordered set, such
that, being $x,y,z \in F$:

- $x+y < x+z \iff y < z$

- $ xy > 0 \implies x > 0 \wedge y > 0$. 

We also say that $x  \in F$, then:

- $x \text{ is positive } \iff x > 0$
- $x \text{ is negative } \iff x < 0$

<br>

#### 2.4.3.2. Properties of ordered fields.

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

We now state the existence theorem which is the core of this chapter. 

<br>

## 3.1. Theorem: Existance of $\mathbb{R}$. Dedekind cuts.

**There exists an ordered field $\mathbb{R}$ which has the least-upper-bound property which contains $\mathbb{Q}$ as a subfield.** 

To proove this theorem, we will construct $\mathbb{R}$ from $\mathbb{Q}$. We shall divide the construction in several steps.

<br>

**Step 1. Cuts**

The members of $\mathbb{R}$ will be certain subsets of $\mathbb{Q}$, called *cuts*. A cut is, by definition, any proper set $\alpha \subset \mathbb{Q}$ with the following three properties: 

- $\alpha \neq \varnothing \wedge \alpha \neq \mathbb{Q}$
- $p \in \alpha \wedge (q \in \mathbb{Q} : q < p) \implies q \in \alpha$. 

    Note that we are saying that being $\alpha$ a cut and $q \notin \alpha$ then $p < q \ \ \forall p \in \alpha$, otherwise, by the line above it would be $q \in \alpha$. In some manner $\alpha$ is a segment inside $\mathbb{Q}$, without gaps. This result also implies the two followings:

    - $p \in \alpha \wedge q \notin \alpha \implies p < q$
    - $p \notin \alpha \wedge p < q \implies q \notin \alpha$

- $p \in \alpha \implies \exists r \in \alpha : p < r$. There is no "larguest" member.

<br>

Check that this so called "cuts" are upperbounds segments with no lowerbound, in the sense that the second property of the cuts already tell us that $p \in \alpha \implies \forall q(q < p \implies q \in \alpha)$. This feature allows an order in $\mathbb{R}$ relative to the cuts members.

<br>

**Step 2. $\mathbb{R}$ is an ordered set**.

Let $\alpha, \beta \subset \mathbb{Q}$ be two cuts, then we define:

$$\alpha < \beta \iff \alpha \subset \beta$$

We say that $\alpha$ is a *proper subset* of $\beta$, which means that any item of $\alpha$ is also an item of $\beta$ but at least one item of $\beta$ do not belongs to $\alpha$, formally:

$$\alpha \subset \beta \iff \alpha \subseteq \beta \wedge \alpha \neq \beta \iff \forall x (x\in \alpha \implies x \in \beta) \wedge \exists b (b\in \beta \wedge b \notin \alpha)$$

The reason why we care about giving a special notation to this familiar concept is because it defines an order inside $\mathbb{R}$.

Let's note that, be $\alpha,\beta \subset \mathbb{Q}$, then, we can think on one of the following posibilities between $\alpha$ and $\beta$

- First, consider that $\exists b \in \beta : b \notin \alpha$, then the first corolary of the second property asserts that $\forall a(a \in \alpha \wedge b \notin \alpha \implies a < b)$, applying again the second property of the cuts we get that $(b\in \beta \wedge a < b) \implies a \in \beta \implies \alpha \subset \beta$.

- A similar argument proves that $\exists a \in \alpha : a \notin \beta \implies \beta \subset \alpha$.

- Now, obviously, if $\neg(\exists b \in \beta : b \notin \alpha) \wedge \neg(\exists a \in \alpha : a \notin \beta)$, counting with the fact that, following the first property of the cuts, $\alpha,\beta \neq \varnothing$ then only can be $\alpha = \beta$.


In summary, we've just proved the *tricothomy* property for any pair of cuts in $\mathbb{Q}$.

Also consider $\alpha,\beta,\gamma \in \mathbb{Q}: \alpha< \beta \wedge \beta < \gamma$ we can directly infere that through the transitivity property of the subsets:

$$\begin{cases} \alpha < \beta \iff \alpha \subset \beta \\ \beta < \gamma \iff \beta \subset \gamma\end{cases} \implies \alpha \subset \gamma \implies \alpha < \gamma$$

Thus, we've demonstrated that $<$ relative to cuts in $\mathbb{R}$ is an order since it satisfies tricothomy and transivity.

<br>

**Step 3. $\mathbb{R}$ satisfies the least-upper-bound property**.

Remember that the least-upper-bound property ensures for any ordered set $S$ that satisfy it any non-empty $E \subset S$ subset upper/lower-bounded has supremum/infimum in $S$.

First, suppose there exists $A \subset \mathbb{R} : A \neq \varnothing$ upperbounded with $\beta \in \mathbb{R}$ an upperbound of $A$, let's see that we can find a supremum for it. 

Now we define as:

$$\gamma := \bigcup_{\alpha \in A} \alpha \iff \gamma := \Set{p \in \mathbb{Q} \ \vert \ \exists \alpha \in A : p \in \alpha}$$

We will see that $\gamma \in \mathbb{R}$, this is, is also a cut, since it satisfies the three properties mentioned above. Then we will demonstrate that $\gamma$ is an upperbound of $A$ and lastly that is the least-upper-bound and thus, the supremum of $A$.

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

Having verified that $\gamma$ is a cut, then since $\forall \alpha(\alpha \in A \implies \alpha \subset \gamma) \implies \alpha < \gamma \ \ \forall \alpha \in A$ so $\gamma$ is an upperbound of $A$. 

For $\gamma = supA$ it has also to be the least upperbound: $\forall \delta(\alpha < \delta \ \forall \alpha \in A \implies \gamma < \delta)$, then let's proceed by reduction absurdio and consider:

$$\neg \forall \delta(\alpha < \delta \ \forall \alpha \in A \implies \gamma < \delta) \equiv \exists \delta : \neg(\alpha < \delta \ \forall \alpha \in A \implies \gamma < \delta)$$

Let's remember that, in classical logic it is: $p \to q \equiv \neg p \vee q \iff \neg(p \to q) \equiv \neg (\neg p \vee q) \equiv p \wedge \neg q$, thus calling:

$$\begin{cases}p := \alpha < \delta \ \forall \alpha \in A \\ q:= \gamma < \delta\end{cases}, \quad p \wedge \neg q \iff \alpha < \delta \ \ \forall \alpha \in A \wedge \delta < \gamma$$

Let's consider $\delta$ as above: $\exists \delta \in \mathbb{R} : \delta < \gamma \wedge (\alpha < \delta \ \ \forall \alpha \in A)$. Observe that $\delta < \gamma \implies \delta \neq \gamma$ which means that $\exists \alpha \in \gamma : \alpha \nsubseteq \delta \implies \delta < \alpha$ (due to the trychotomy of the order), thus and $\delta$ would not be an upperbound contradicting the initial assumption. 

So, by reduction absurdio, $\gamma$ has to be the least upper bound; $\gamma = sup A$.

<br>

**Step 4. Addition in $\mathbb{R}$.**

If $\alpha, \beta \in \mathbb{R}$ we define: $\alpha + \beta := \Set{a+b \ \vert \ a \in \alpha \wedge b \in \beta}$. We also define $0^* \in \mathbb{R}$ as $0^* := \Set{ q \in \mathbb{Q} \ \vert \ q < 0}$, observe that is clear that this last set is a cut.

Now, we verify that the addition's axioms for a field hold in $\mathbb{R}$, with $0^*$ playing the role of $0$. In orther terms, $(\mathbb{R},+)$ is an abelian group:

- **Closure**: $\alpha + \beta \in \mathbb{R} \ \ \forall \alpha, \beta \in \mathbb{R}$. We have to demonstrate that $\alpha + \beta$ is a cut.

    Let's demonstrate that $\alpha + \beta$ satisfies the three properties of a cut. 

    1. $\alpha, \beta \neq \varnothing \implies \alpha + \beta \neq \varnothing$. 
    
        Also suppose that $p,q \in \mathbb{Q}$ are the upperbounds of $\alpha, \beta \in \mathbb{R}$ respectively, then is clear that $p + q \notin \alpha + \beta \implies \alpha + \beta \neq \mathbb{Q}$. 
        
        Observe that there is something worth to say of upperbounds when speaking about cuts. By definition, $p$ is an upperbound of $X$ iff $x \leq p \ \ \forall x \in X$, but if $X$ were a cut, by the third property if $\exists x_0 : p = x_0 \in X \implies \exists r \in X : p < r$ and $p$ would not an upperbound, thus, when talking about cuts, all upperbounds are always strict upperbounds, the definition of upperbounds always collapses to $x < p \ \ \forall x \in X$ and the cut do not contains it.

    <br>

    2. $p \in \alpha + \beta \wedge (q \in \mathbb{Q} : q < p) \implies q \in \alpha + \beta $ 

        Let's take that $p = a + b$, since $q < p = a + b \implies q - a < b \in \beta$ and thus we get that $q = (q - a) + a \in \alpha + \beta$.

        <br>

    3. $p \in \alpha + \beta \implies \exists q \in \alpha + \beta : p < q$

        This result is almost immediate since if $p = a + b$ then, exists $a' \in \alpha, b' \in \beta$ verifying both $a < a' \wedge b < b'$, thus calling $q = a' + b'$ clearly is $q \in \alpha + \beta : p < q$

        <br>

- **Conmutativity**: $\alpha + \beta = \beta + \alpha \ \ \forall \alpha, \beta \in \mathbb{R}$
- **Asociativity**: $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma \ \ \forall \alpha, \beta, \gamma \in \mathbb{R}$ 
## 3.2. Important Properties from the $\mathbb{R}$ field.

### 3.2.1. Archimedean property of $\mathbb{R}$.

The Archimedean property says that $\mathbb{R}$ has no "infinitely large" or "infinitely small" elements: no matter how small a positive number $x$ you pick and no matter how large a target $y$, you can always reach (and surpass) $y$ by adding $x$ to itself enough times. Formally:

$$\forall x,y \in \mathbb{R} :  0 < x \  \exists n \in \mathbb{N} : y < nx$$

Let's reason by the reduction to absurdity, let be $A:=\Set{nx \ \vert \ n \in \mathbb{N}}$ then if the statement above isn't true, $y$ would be an upperbound of $A$ and since $A \neq \varnothing$ and $\mathbb{R}$ has the $LUB$ property, then $A$ has a supremum on $\mathbb{R}$ let be $\alpha = supA$.

Let's observe that $ 0 < x \iff - x < 0 \iff \alpha - x < \alpha$ and $\alpha - x$ is not an upperbound so there exists some natural $m \in \mathbb{N} : \alpha -x < mx$, but then $\alpha < m (x+1) \in A \implies \alpha \neq supA$

<br>

Let's observe that this rules out the existence of infinitesimals; positive numbers so tiny that no finite sum of copies ever reaches $1$. It is the formal guarantee that the integers "go to infinity".

<br>


### 3.2.2. $\mathbb{Q}$ is dense in $\mathbb{R}$

The density of $\mathbb{Q}$ in $\mathbb{R}$ stablish that between two elements of $\mathbb{R}$ a rational always can be found, formally:

$$\forall x, y \in \mathbb{R} : x < y \implies \exists q \in \mathbb{Q} : x < q < y$$

To demonstrate it, lets think about $x, y \in \mathbb{R} :x <y$, thus is $ 0 < y - x$ so for $1 \in \mathbb{R}$, the archimedean property furnishes the result: $1 < n(y-x)$.

Also, considering $z_1,z_2 \in \mathbb{R}^+ \implies \exists t_1,t_2 \in \mathbb{N}: nx < t_1z_1 \wedge -nx < t_2z_2$. Then, calling $m_i = t_iz_i$ is:

$$-m_2 < nx < m_1$$

We can nail $[-m_2,m_1] \cap \mathbb{Z}$ until find an $m \in \mathbb{N} : m-1 \leq nx < m$, in summary:

$$\begin{cases} 1 < n(y-x)  \iff 1 + nx < y \\ m - 1 \leq nx < m \iff m \leq 1 +nx < m +1  \end{cases} \implies nx < m \leq 1 + nx < ny$$

And thus:

$$x < \frac{m}{n} < y$$

<br>