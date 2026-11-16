---
layout: post
title: "Kinematics of the single particle."
subtitle: "Fundamentals Magnitudes. Uniform Rectilinear Motion"
date: 2026-06-17 09:00:00 +0000
categories: ['Number Systems']
tags: ['Physics']
author: German Sanmi
subject: dynamics
lang: en
---

# 0. Index.

1. Introduction: Mecanics and Kinematics. Kinematics purpouse.
- 1.1. Kinematics purpouse.
- 1.2. Particle notion.
- 1.3. Motion notion. Absolute and relative motion.
2. Fundamental magnitudes of the kinematics of a single particle.
- 2.1. Parametric time equations.
- 2.2. Position-time equation.
- 2.3. Exchange between Position-time to Parametric forms.
    - 2.3.1. Arc length equation: Parametric to Position-time.
    - 2.3.2. From the Position-time to parametric forms.

        <br>

# 1 Mecanics and Kinematics.

## 1.1. Kinematics purpouse.

Mecanics is the physics discipline that study the state of rest and motion of the bodies. Classics mecanics and by extension classics physics is restrained to big bodies (far bigger than an atom) whose movement is far smaller than speed of light.

Kinematics is the branch of mechanics that studies motion, independently of the causes that produce it, meaning that the study object of kinematics is the understanding, description and prediction of the position, velocity and aceleration of a moving body in function of time.

<br>

## 1.2. Particle notion.

Since kinematics disregards causes in order to focus on motion and its evolution over time, the central concept of kinematics, the particle, disregards, or abstracts away from, any property other than position.

This way, a *particle* is an ideal entity whose volume we consider zero and to which we can add some properties such position, mass, aceleration, etc.

<br>

## 1.3. Motion notion. Absolute and relative motion.

One of the most important notions in physics is the understanding that motion is relative and all ways joint to a reference. Two observers moving one respect the other, without a common fixed reference, cannot say who is moving and who is not.

Then, we say that a particle is moving when his position varies in relation with an axis system which can be fixed (like a house or the ground) or not (like a train), which leads to absolute and relative movement. This means that whenever we describe the movement of a particle, we always have to specify the references to which the motion is taking place.

In everything that follows, the description of the movement is given in relation to an axies system in whose origin lies the observator.

<br>

# 2. Fundamental magnitudes of the kinematics of a single particle.

## 2.1. Parametric time equations.

In order to describe the motion of a particle first we do have to understand how to relate his position in a sistem axis with the time. 

We have several forms to do this, the first is what we call *path*, which consist in describe the position calculate with coodinates in differents moments in time. 

First we settle what we call the *initial conditions*, which is the initial position, $P_0$ of the particle in some instant, commonly $t=0$. This position has associated a position vector, $r_0 \in \mathbb{R}^3$ which is the *initial position vector*: $r_0 = (0,0,0)$.

Then, after some time, the particle will ocuppie a position $r_t = (x(t),y(t),z(t))$, we call this the parametric path equations.

$$r(t) = x\textbf{i} + y\textbf{j} + z\textbf{k} = \begin{cases} x = x(t) \\ y = y(t) \\ z = z(t)\end{cases}$$

<br>

## 2.2. Position-time equation.

A second form of describe the motion of a particle is through the system of equations describing two surfaces whose intersection make the path of the particle. This equation can be obtained by cleaning $t$ in the parametric equations above.

$$\begin{cases} s_1(x,y,z) = 0 \\ s_2(x,y,z) = 0\end{cases}$$

Observe that at this point we have geometric information aboutn the path not related with the time. We want to mix this geometric information with the position of the body at some instant.

With this purpouse we need to distinguish an orientation, this means, to consider a point from which the movement departs, $P_I$ and a point from which the time of the motion starts to run, $P_0$. We make this two entities distinct because both reflects different conceptions but often both are forced to coincide.

This way, the position $P$ of the body at some instant $t$ will become described by the arc $P_0P$ which will be expressed in terms of time by the equation:

$$s = s(t)$$

Which measures the distance traveled by the body in on concrete orientation of the geometrical path.

<br>

## 2.3. Exchange between Position-time to Parametric forms.

### 2.3.1. Arc length equation: Parametric to Position-time.

First of all, let be $r : [a,b] \to \mathbb{R}^3$ continue the application that defines the path of our body. Then, the parametric form of $r$ is:

$$r(t) = (x(t), y(t), z(t))$$

Let's clean $t$ as $2.2$ suggest, getting a system of two equations in three unknowns, let's also parametrized the $y,z$ components in terms of $x$ (when the body is at some $x$, it obviously occuping some $y$ and $z$ values depending directly on $x$), thus obtaining:

$$r(x) = (x,y(x), z(x))$$

Then, the arc length of $r$ is:

$$L(r) = \int_a^b \|\frac{dr}{dx}(x)\| dx = \int_a^b \sqrt{1 + \frac{dy}{dx}(x) + \frac{dz}{dx}(x)} dx$$

Then, the arc length of $P_0P$ is, asuming $P_0({P_x}_0, {P_y}_0)$, $P(P_x,P_y)$, then:

$$L_{{P_x}_0}(P_x) = \int_{x_0}^{x} \sqrt{1 + \frac{dy}{du}(u) + \frac{dz}{du}(u)} du$$

<br>

### 2.3.2. From the Position-time to parametric forms.

If we have:

$$ \begin{cases} s_1(x,y,z) = 0 \\ s_2(x,y,z) = 0\end{cases}, \quad  L_{x_0}(x) = \int_{x_0}^{x} \sqrt{1 + \frac{dy}{du}(u) + \frac{dz}{du}(u)} du$$

Let's observe that, since we are considering only one orientation, $L_{x_0}$ is only a non-null, increasing function, by the local inverse function theorem, $\exists L_{x_0}^{-1}$, then:

$$(r \circ L^{-1}) \circ L = r$$

Then from $s_1,s_2$ we obtain $y(x)$ and $z(x)$ obtaining finally $x(t)$.

<br>

### 2.3.3. Examples.

**Problem 1. The position of a particle moving in a plane is given as a function of time, in SI units, by**

$$\mathbf{r} = (2t^2 - 1)\mathbf{i} + (t^3 + 1)\mathbf{j}$$

**Find:**

1. **The initial position vector.**

    As we know, the initial position vector is $r_0 = (x(0), y(0)) = (-1,1) = \overrightarrow{OP_0}$

    <br>

2. **The distance from the observer (that is, from the origin of the reference frame) 5 s after we start measuring time.**

    Which is more likely asking to us is $r(5)$.

    <br>

3. **The distance traveled by the particle during the third second.**

    Let's get the arc length. First, we take the parametric equations:

    $$\mathbf{r} = (2t^2 - 1)\mathbf{i} + (t^3 + 1)\mathbf{j} =  (2t^2 -1,t^3 +1) = \begin{cases} x = 2t^2 -1 \\ y = t^3 +1\end{cases}$$

    And we obtain the equation of the line in a plane:

    $$y(x) = \sqrt{\frac{(x+1)^3}{8}} - 1 \implies r(x) = (x, \sqrt{\frac{(x+1)^3}{8}} - 1)$$

    Then, the arc length is:

    $$L_{x_0}(x) = \int_{x_0}^x \|r'(u)\|du = \int_{x_0}^x \sqrt{1 + \frac{3(u+1)^2}{2\sqrt{\frac{(u+1)^3}{8} -1}}} du$$

    <br>

