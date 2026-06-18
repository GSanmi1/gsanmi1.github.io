---
layout: post
title: "Natural Numbers"
subtitle: "Peano, Induction, Recursion Theorem,  & Good Order, Integers; Divisibility, Bézout, Comprimality"
date: 2026-06-17 09:00:00 +0000
categories: ['Number Theory']
tags: ['Maths']
author: German Sanmi
subject: number-systems
lang: en
---

# 0. Index.

# 1. Introduction.

We are going to presentate part of the basics of number theory, culmintaing to the demonstration of the fact that the root of any natural number is rational iff this natural number is a perfect square.

The results shown in the present post are a single deductive chain with no added ingredient that starts from a single premise axiom from natural numbers $\mathbb{N}$, (good order) and stop in the irrationality of $\sqrt{2}$. The idea that is worth to remember along the paper is; the good order produces division algorithm, the division produces Bézout is a result that translates divisibility into linearity which expands for the rest.

<br>

## 1.1. Convetions.

Before starting, let's fix some conventions:

- Being $a,b \in \mathbb{Z}$ then we say "$b$ divides $a$" and write $b \mid a$ when:

    $$b \mid a \iff \exists k \in \mathbb{Z} : a = kb$$

    Let's observe that divisibility respects linearity:

    $$c \mid a \wedge c \mid b \implies c \mid (ma + nb) \quad \forall m,n \in \mathbb{Z}$$

    <br>

- Being $a,b \in \mathbb{Z}: ab  \neq 0$, we call $gdc(a,b) = \max\Set{c \in \mathbb{N} : (c \mid a \wedge c \mid b)}$, this is the maximum integer that divides both numbers at once. Let's observe some interesting facts:

    - $1 \in gdc(a,b) \quad \forall a,b \in \mathbb{Z}$
    - $\max \Set{\|a\|,\|b\|} \geq c \quad \forall c \in gcd(a,b)$, observe immediately that any number greater would not divide both of them so is not in $gcd(a,b)$.

    - $gcd(a,b) = gcd(b,a) \quad \forall a,b \in \mathbb{Z}$
    - $gcd(a,b) > 0 \quad \forall a,b \in \mathbb{Z}$

        <br>

# 2. Good Order in $\mathbb{N}$. Induction.

## 2.1. Conceptual presentation.

Having clear this concepts, let's talk about the "good order" and the induction principle. This idea is expressed as a property of a set, a set is said to have good order or be good ordered if it has a minimum, this is a last element. In a more generic way; a good order is a total order in which any not-empty subset has a minimum.

The canonical example is the set of the natural numbers. This will be our depature point:

**$\mathbb{N}$ is a good ordered set**

<br>

Let's now talk about the induction principle which is tightly related with $\mathbb{N}$ and coimplicates good order.

<br>

## 2.2. Formal definition. Good order.