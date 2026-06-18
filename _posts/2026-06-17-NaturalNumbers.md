---
layout: post
title: "Natural Numbers"
subtitle: "Peano, Induction, Recursion Theorem,  & Good Order, Integers; Divisibility, Bézout, Coprimality"
date: 2026-06-17 09:00:00 +0000
categories: ['Number Theory']
tags: ['Maths']
author: German Sanmi
subject: number-systems
lang: en
---

# 0. Index.

# 1. Introduction.

We are going to present part of the basics of number theory, culminating in the demonstration of the fact that the root of any natural number is rational iff this natural number is a perfect square.

The results shown in the present post are a single deductive chain with no added ingredient that starts from a single premise axiom of the natural numbers $\mathbb{N}$ (good order) and stops at the irrationality of $\sqrt{2}$. The idea that is worth remembering throughout the paper is: the good order produces the division algorithm, the division algorithm produces Bézout, which is a result that translates divisibility into linearity, and that expands to the rest.

<br>

## 1.1. Conventions.

Before starting, let's fix some conventions:

- Being $a,b \in \mathbb{Z}$ then we say "$b$ divides $a$" and write $b \mid a$ when:

    $$b \mid a \iff \exists k \in \mathbb{Z} : a = kb$$

    Let's observe that divisibility respects linearity:

    $$c \mid a \wedge c \mid b \implies c \mid (ma + nb) \quad \forall m,n \in \mathbb{Z}$$

    <br>

- Being $a,b \in \mathbb{Z}: ab  \neq 0$, we call $gcd(a,b) = \max\Set{c \in \mathbb{N} : (c \mid a \wedge c \mid b)}$, this is the maximum integer that divides both numbers at once. Let's observe some interesting facts:

    - $1 \in gcd(a,b) \quad \forall a,b \in \mathbb{Z}$
    - $\max \Set{\|a\|,\|b\|} \geq c \quad \forall c \in gcd(a,b)$, observe immediately that any greater number would not divide both of them so it is not in $gcd(a,b)$.

    - $gcd(a,b) = gcd(b,a) \quad \forall a,b \in \mathbb{Z}$
    - $gcd(a,b) > 0 \quad \forall a,b \in \mathbb{Z}$

        <br>

# 2. Good Order in $\mathbb{N}$. Induction.

## 2.1. Conceptual presentation.

Having clarified these concepts, let's talk about the "good order" and the induction principle. This idea is expressed as a property of a set; a set is said to have good order or be well-ordered if it has a minimum, this is, a least element. In a more generic way; a good order is a total order in which any non-empty subset has a minimum.

The canonical example is the set of the natural numbers. This will be our departure point:

**$\mathbb{N}$ is a well-ordered set**

<br>

Let's now talk about the induction principle which is tightly related to $\mathbb{N}$ and co-implies good order.

<br>

## 2.2. Formal definition. Good order.