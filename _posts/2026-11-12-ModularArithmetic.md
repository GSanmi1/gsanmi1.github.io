---
layout: post
title: "Modular Arithmetic"
subtitle: "Greatest Common Divisor, Extended GCD, Modular Arithmetic, Modular Inverting, Quadratic Residues, Legendrel Symbol, Modular Square Root, Remainder Theorem, Adrien's Sings, Modular Binomials."
date: 2026-06-17 09:00:00 +0000
categories: ['Number Systems']
tags: ['Maths']
author: German Sanmi
subject: number-systems
lang: en
---

# 0. Index.

1. Introduction.
2. Euclidean Division: Reminder.
- 2.1. Euclidean division.
- 2.2. Reminder: Definition.

3. Definition of $\mathbb{Z}/n\mathbb{Z}$.
- 3.1. Congruence as an equivalence relation.

    <br>

# 1. Introduction. 

In this section we are going to present several important results about number theory involving modular aritmetic.

Modular aritmetic is the aritmetic operation involving integers refering only of what is left when dividing by some fixed integer *n*, called *remainder*.

<br>

# 2. Euclidiean Division: Reminder.

## 2.1. Euclidean Division.

We have the following theorem in $\mathbb{Z}$. Let $q \geq 1$ a fixed integer, then:

$$\forall p \in \mathbb{Z} \ \exists! n,r \in \mathbb{Z} : (p = nq + r \wedge 0 \leq r < n)$$

This theorem, called Euclidean Division, postulates that any integer can be decomposed in terms of any other integer disregarding a margin we call *remainder*. Essentially, the formal statement above should be read as; fixed some integer, then, any other integer exists inside it a unique amount of times neglecting a marging inferior than that very amount.


<br>

## 2.2. Reminder: Definition.

If is $p = nq + r : 0 \leq r < n$, then $r$ can be legitimatly understanded as what is left from $p$ seen through the optic of $q$ but is convenient to understand it, instead, as what remains of $p$ when all the copies of $q$ are disregarded. The remainder is what $p$ has in common with all those integers builded from $p$ by adding or substracting copies of $q$:

$$ p + mq = (nq + r) + mq = (n+m)q + r \quad \forall m \in \mathbb{Z}$$

And the remainder does not change.

Then, from the fixed integer perspective, the remainder acts as a kind of identifier of the class of integers for which the same marging is left when they are decomposed on copies of himself. This class is interesting because some properties are preserved, which is precisely the properties we study in modular aritmetic. Observe, for example, that the class of multiples of $p$; $np: n\in \mathbb{Z}$, is a particular case of shared remainder for $r=0$, we could say then that the class of integers that shares a remainder can be understanded as the generalization of the concept of multiple in number theory, further more, the class of integers with remainder $r$ is exactly the class of the multiples (remainder $0$) displaced $r$ unities. 

Then, we will give to the remainder a singular nomenclature:

$$r =  a \bmod n \iff n \mid (a - r)$$

Read as: $r$ is the remainder of $a$ modulo $n$, which means $a$ is a multiple of $n$ shifted $r$ times.

<br>

# 3. Definition of $\mathbb{Z}/n\mathbb{Z}$.

## 3.1. Congruence as an equivalence relation.

Let $n \in \mathbb{Z}^+$. We define the relation $\equiv \ \subseteq \mathbb{Z} \times \mathbb{Z}$ by

$$a \equiv b \pmod{n} \iff a \bmod n = b \bmod n$$

Read as $a$ is congruent with $b$ modulo $n$, which means $a$ and $b$ shares remainder when are decomposed through $n$.

Note that there is an equivalent shortest equivalent characterization:

$$a \bmod n = b \bmod n \iff n \mid (b -a )$$

The first one has an immediate lecture, while the second is more standarized, for now on we will use the second as the preference.

Let's see this relation is an equivalence relation in $\mathbb{Z}$. The following points are written in a poor riguriously way in the interest of time, we are only focusing in the relevant part:

- $a \sim a$, since $a - a = 0$
- $a \sim b \iff b \sim a$ since $b -a  =qn \iff a -b = (-q) n$
- $(a \sim b \wedge b \sim c \implies a \sim c )$ since $c - a = (c - b) + (b - a) = pn + qn = (p+q)n$

<br>

An equivalence relation declares certain elements to be indistinguishable. Along with an equivalence relation there are the class of $a$; $[a]$; which is the set of everything that is indistinguishable from $a$ from the relation perspective. In this case; 

$$[a]= a + n\mathbb{Z}:= \Set{b \in \mathbb{Z} \mid b \equiv a \pmod n} = \Set{b \in \mathbb{Z} \mid b = a+kn : k \in \mathbb{Z} }$$

Or simply: $a + n\mathbb{Z}:= \Set{a+kn : k \in \mathbb{Z}}$, the multiples of $n$ shifted $a$ unities.

<br>

Observe directly that since the remainder is a non-negative integer smaller than $n$, there are exactly $n$ relation class clustered in the quotient set:

$$\mathbb{Z}/n\mathbb{Z} := \Set{[0],[1]\ldots,[n -1]}$$

Note then that the modulo let us to decompse an infinite set as $\mathbb{Z}$ in a finite number of distinct parts, the equivalence class relative to a fixed integer. (Note that here the Euclid Division still plays an important role, the existance of the remainder assert the existance of each class and the uniquity asserts that there are no repeated class.)

<br>

## 3.2. Quotient Set of $\mathbb{Z}/n\mathbb{Z}$.



<br>