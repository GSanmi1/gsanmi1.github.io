---
layout: post
title: "Euclidean Spaces"
subtitle: "Introduction to Euclidean Spaces."
date: 2026-03-05 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
---

# 0. Index

# 1. Presentation and Definition. 

An Euclidean space, $\mathbb{R}^k$ is the set of all the ordered real $k$-tuples. This structure is well equiped with all the tools that simultaneously make it a:

- **$\mathbb{R}$-vector space**: $(\mathbb{R},(\mathbb{R}^k,+),·)$, with the operations as follows:

    $$(x_1,...,x_k)+(y_1,...,y_k)=(x_1+y_1,...,x_k+y_k)$$

    $$\alpha · (x_1,...,x_k) = (\alpha x_1,..., \alpha x_k)$$

    Which allows linear combinations.

    <br>

- **Inner product space**: As we see in the [Complex Numbers](https://gsanmi1.github.io/posts/2026/03/05/Complex_Numbers/) post, on $6.3.1$, an inner product space is an object which inyects geometry by defining how a vector express his own direction (norm):

    $$\langle ·,· \rangle : \mathbb{R}^k \times \mathbb{R}^k \to \mathbb{R}$$

    In this case, the instantiation is the *dot product* or *scalar product*:

    $$\quad \quad \langle x,y \rangle = \sum_{i=1}^k x_iy_i$$

    Which inyects geometry, a notion of direction (norm), shared direction (angle) and disjoint direction (pithagoras).

    <br>

- **Normed Space**: As a consecuence of the inner product presence, a norm for each vector $x \in \mathbb{R}^k$ is defined:

    $$\|x\| = \sqrt{\langle x,x \rangle}= \sqrt{\sum_{i=1}^k x_i^2}$$

    Which give us a notion of "longitude" of the vector. Is worth to say that this is specifically true in $\mathbb{R}^k$ where intuitive geometry matchs formal geometry instauration through dot product.

    <br>

- **Metric Space**: As consecuence of the geometry inyected by inner product a notion of proximity is definided which allow as to introduce the notion of limit and develop the analisis.

    <br>

# 2. Metric spaces.

## 2.1. Metric definition.

<br>