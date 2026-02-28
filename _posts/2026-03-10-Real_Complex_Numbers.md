---
layout: post
title: "The Real and Complex Number Systems"
subtitle: "DAGs and its importance in computation"
date: 2026-02-27 09:00:00 +0000
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

## 1.1. Rational numbers is inadequatness.

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