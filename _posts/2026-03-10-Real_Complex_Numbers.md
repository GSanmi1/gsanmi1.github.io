---
layout: post
title: "The Real and Complex Number Systems"
subtitle: "$\mathbb{R} and \mathbb{C} fields presentation and properties."
date: 2026-03-10 09:00:00 +0000
categories: ['analisis_rudin']
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

An ordered set is simply a set in which an order relation has been defined. Let's consider for example $\mathbb{Q}$ the set of rational numbers and the binary relation:

$$\leq \  \subseteq \mathbb{Q} \times \mathbb{Q}: q \leq p \iff \exists t \in \mathbb{Q}^+ :p =  q + t$$

We consider that $0 \in \mathbb{Q}^+$, so:

- $p = p + 0 \iff p \leq p \ \ \forall p \in \mathbb{Q}$ (Reflexivity)

- $q \leq p \wedge t \leq q \implies \exists n,m \in \mathbb{Q} : p = q + n = (t + m) + n = t + (m + n) \implies t \leq p$ (transitivity)

- $p \leq q \wedge q \leq p \implies \exists m,n : \begin{cases} p = q + n \\ q = p + m\end{cases} \implies m -n = 0 \iff m = n \implies p = q$ (Antisimetric)

<br>

So $\leq$ is an order, is easy to see without demonstration that is a partial order, since we can't talk about any two non-comparable rationals