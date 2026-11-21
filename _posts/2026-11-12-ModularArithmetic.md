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

    <br>

# 1. Introduction. 

In this section we are going to present several important results about number theory involving modular aritmetic.

Modular aritmetic is the aritmetic operation involving integers refering only of what is left when dividing by some fixed integer *n*, called *remainder*.

<br>

# 2. Euclidiean Division: Reminder.

## 2.1. Euclidean Division.

We have the following theorem in $\mathbb{Z}$. Let $q \geq 1$ a fixed integer, then:

$$\forall p \in \mathbb{Z} \ \exists! n,r \in \mathbb{Z} : (p = nq + r \wedge 0 \leq r < n)$$

This theorem, called Euclidean Division, postulates that any integer can be decomposed in terms of any other integer disregarding a margin we call *reminder*. Essentially, the formal statement above should be read as; fixed some integer, then, any other integer exists inside it a unique amount of times neglecting a marging inferior than that very amount.


<br>

## 2.2. Reminder: Definition.

If is $p = nq + r : 0 \leq r < n$, then $r$ can be legitimatly understanded as what is left from $p$ seen through the optic of $q$ but is convenient to understand it, instead, as what remains of $p$ when all the copies of $q$ are disregarded. The remainder is what $p$ has in common with all those integers builded from $p$ by adding or substracting copies of $q$:

$$ p + mq = (nq + r) + mq = (n+m)q + r \quad \forall m \in \mathbb{Z}$$

And the remainder does not change.

Then, from the fixed integer perspective, the reminder acts as a kind of identifier of the class of integers for which the same marging is left when they are decomposed on copies of himself. This class is interesting because some properties are preserved, which is precisely the properties we study in modular aritmetic. Observe, for example, that the class of multiples of $p$; $np: n\in \mathbb{Z}$, is a particular case of shared reminder for $r=0$, we could say then that the class of integers that shares a reminder can be understanded as the generalization of the concept of multiple in number theory, further more, the class of integers with reminder $r$ is exactly the class of the multiples (reminder $0$) displaced $r$ unities. 

Then, we will give to the remainder a singular nomenclature:

$$r =  a \bmod n \iff n \mid (a - r)$$

Read as: $r$ is the remainder of $a$ modulo $n$, which means $a$ is a multiple of $n$ shifted $r$ times.

<br>

# 3. Definition of $\mathbb{Z}/n\mathbb{Z}$.

## 3.1. Congruence as an equivalence class.

Let be $n \in \mathbb{Z}^+$, then we are going to define 

<br>

## 3.2. Quotient Set of $\mathbb{Z}/n\mathbb{Z}$.
