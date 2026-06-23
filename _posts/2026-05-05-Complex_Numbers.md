---
layout: post
title: "The Complex Number System"
subtitle: "Complex field presentation. Geometric nuance. Inner product spaces. Cauchy-Schwarz."
date: 2026-06-01 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']
tags: ['Maths']
author: German Sanmi
subject: complex-analysis
lang: en
---

# 0. Index

1. Definition and operations.

2. $\mathbb{C}$ as a field.

3. $\mathbb{R}$ in $\mathbb{C}$.

4. Real formulation of $\mathbb{C}$. Imaginary and Real part.

5. Geometric representation of $\mathbb{C}$.
    - 5.1. Axis.
    - 5.2. Absolute Value. Polar Form.
    - 5.3. Geometric Intuition of the operations in $\mathbb{C}$.
        - 5.3.1. Addition as a torsor.
        - 5.3.2. Multiplication as a rotation.

    - 5.4. Conjugate.

6. Important properties of Complex Numbers.
    - 6.1. Conjugate properties.
    - 6.2. Absolute Value properties.
    - 6.3. Cauchy-Schwarz inequality.
        - 6.3.1. Appendix: Inner product. Norm. Orthogonality.
        - 6.3.2. Real definition and conceptual explanation.
        - 6.3.3. Induced Norm.
        - 6.3.4. Proper inner product expression.
        - 6.3.5. Cauchy-Schwarz and angle between two vectors.

    - 6.4. Rudin's 1.35 theorem.

<br>

# 1. Definition and operations.

A complex number is an ordered pair of real numbers. By definition it is:

$$(x,y) := \Set{\Set{x}, \Set{x,y} : x,y \in \mathbb{R}} \in \mathbb{C}$$

Observe that this means that:

$$(x_1,y_1) = (x_2,y_2) \iff x_1 = x_2 \wedge y_1 = y_2$$

<br>

We define two operations in the complex numbers, addition and multiplication as follows. Be $z_1,z_2 \in \mathbb{C}$, then:

$$z_1 + z_2 =(x_1,y_1) + (x_2,y_2) = (x_1+x_2,y_1+y_2)$$

$$z_1z_2=(x_1,y_1)(x_2,y_2) = (x_1x_2 -y_1y_2, x_1y_2 + x_2y_1)$$

<br>

# 2. $\mathbb{C}$ as a field.

These definitions of addition and multiplication turn the set of
all complex numbers into a field in an algebraic sense, with $0^\ast = (0, 0)$ and $1^\ast = (1, 0)$.

Meaning that $(\mathbb{C},+)$, $(\mathbb{C}\setminus \Set{(0,0)}, \ ·)$ are compatible abelian groups.

It is worth mentioning the form of the inverse of a $z \in \mathbb{C}$:

$$z = (x,y) \neq 0 \implies z^{-1} = \left(\frac{x}{x^2+y^2}, \frac{-y}{x^2+y^2}\right)$$

It is easy to prove that $zz^{-1} = 1 \iff z \neq 0$ by operating.

<br>

# 3. $\mathbb{R}$ in $\mathbb{C}$.

Observe that if we take $z\_1,z\_2 \in \mathbb{C} : z\_1 = (a,0), z\_2 = (b,0)$, then $z\_1,z\_2$ behave exactly as real numbers:

$$z_1 + z_2 = (x_1+x_2,0) \quad z_1z_2 = (x_1x_2,0)$$

Thus, we can identify each $\alpha \in \mathbb{R}$ with the complex $(\alpha,0) \in \mathbb{C}$. 

Observe we can consider $\varphi : \mathbb{R} \to \text{Re}$ such that $\varphi(\alpha) = (\alpha,0)$. Note that $\varphi$ is a *field homomorphism*:

- $\varphi(\alpha + \beta) = (\alpha + \beta,0) = (\alpha,0) + (\beta,0) = \varphi(\alpha) + \varphi(\beta)$
- $\varphi(\alpha \beta) = (\alpha \beta,0) = (\alpha,0) (\beta,0) = \varphi(\alpha) \varphi(\beta)$

    <br>

Also, it maintains the order; we define in $\text{Re} \subset \mathbb{C}$ the order: $(x,0) < (y,0) \iff x < y$.

Also, it is clear that $\varphi$ is bijective, thus it is an isomorphism of ordered fields, and we can identify $\mathbb{R}$ and $\text{Re}$ or, in other words: $\mathbb{R} \simeq \text{Re} \subset \mathbb{C}$ and $\mathbb{C}$ contains $\mathbb{R}$.

<br>

# 4. Real formulation of $\mathbb{C}$. Imaginary and Real part.

We define $i := (0,1) \in \mathbb{C}$, observe immediately that:

$$i^2 = (-1,0) = \varphi(-1)$$

Or, making an abuse of notation: $i^2 = -1 \in \mathbb{R}$

<br>

Let's also observe that there is a real reformulation for any complex number using $i$ as a toehold. 

Be $z = (x,y) \in \mathbb{C}$, then:

$$z = (x,y) = (x,0) + (0,y) =  (x,0) + (y,0)(0,1) = \varphi(x) + \varphi(y)i \quad \forall z \in \mathbb{C}$$

Or simply: $z = (x,y) = x + yi$

<br>

# 5. Geometric representation of $\mathbb{C}$.

## 5.1. Axis.

Let's observe a phenomenon: we had defined $\mathbb{C}$ basically as an extension of $\mathbb{R}$ to two dimensions, precisely:

$$\mathbb{C} := \Set{(a,b) \mid a,b \in \mathbb{R}}$$

Thus, let's try to represent this set in a coordinate system. A few minor considerations:

- Since we already saw that $\text{Re} := \Set{(x,0) \mid x \in \mathbb{R}} \simeq \mathbb{R}$, the abscissa axis must be the real line.

- Then, $\text{Im}:= \Set{(0,y) \mid y \in \mathbb{R}}$ is what we call the imaginary axis, and it is not a strict copy of $\mathbb{R}$ as $\text{Re}$ is; let's observe that it is not closed under the product: 

    $$(0,y_1)(0,y_2) = [(y_1,0)(y_2,0)][(0,1)(0,1)] = (y_1y_2,0)(-1,0) = (-y_1y_2,0) \notin Im$$

Both axes form:

![complex1](/assets/images/Maths/Analisis/complex1.png)


<br>

## 5.2. Absolute Value. Polar Form.

Let's take some $z$ as in the image above and observe that this is a two-dimensional vector, thus we can identify each $z := (x,y)$ with the vector $\overrightarrow{z}=(x,y)$ and leverage vector space properties and the trigonometric relations of the object.

- First, we call as **absolute value** of $z$ to the vector norm:

    $$| z | := \| \overrightarrow{z} \| = \sqrt{x^2 + y^2}$$

    <br>


- Also, we can consider the angle of the vector with the abscissa axis, $\theta$:

    $$\theta := \arctan(y/x)$$


Observe that $z$ gets completely characterized by these two elements in what we call the **polar form** of the complex numbers:

$$z = |z|_\theta = |z|(\cos\theta + i\sin\theta)$$

![complexpolar](/assets/images/Maths/Analisis/complexpolar.png)

<br>

## 5.3. Geometric Intuition of the operations in $\mathbb{C}$.

In other parts of this same post we asserted that the real numbers were positions on a line, and that this obliges us to interpret the operations of the field with a geometric nuance.

Thus, we stated that in $\mathbb{R}$ the addition was a translation and the product was a homothety. Let's now see how the operations we just defined act in the $Re \times Im$ plane.

<br>

### 5.3.1. Addition as a torsor.

In this case, the abelian group $(\mathbb{C},+)$ behaves in $Re \times Im$ making it a *torsor*. (It is desirable to take a look at the following post to understand the explanation below: [vector spaces](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/)).

Recapitulating, we know that an affine space is the algebraic structure resulting from using *vectors* to study a non-empty set in a simply transitive way. Then, a *torsor* is something prior, more primitive; a torsor is a regular group action of (in this case an abelian) group over a non-empty set, basically an affine space that has forgotten the field's action over the vectors so these can't be scaled and, consequently, you can't scale distances.

We define the pair $(Re \times Im, +)$ being: 

$$+ : [Re \times Im] \times (\mathbb{C},+) \to [Re \times Im]$$

$$\quad \quad  \quad (x,y) + z \mapsto (x + z_1, y +z_2)$$

<br>

Let's see this is a regular group action:

- $A1$, taking $0 \in \mathbb{C}$, then: $(x,y) + 0 = (x,y) \quad \forall (x,y) \in Re \times Im$. So there is an identity element.

    <br>

- $A2$, the associativity is immediate from the fact that $(\mathbb{R},+)$ is an abelian group:

    $$((x,y) + z)+t = (x+z_1,y+z_2) + t = ([x + z_1] +t_1,[y+z_2]+t_2) = $$

    $$(x + [z_1 +t_1],y+[z_2+t_2]) = (x,y) + (z + t)$$

    <br>

- **Free** and **Transitivity**

    Let's take two points $x,y$ on $Re \times Im$, asking whether $\exists! z \in \mathbb{C} : x + z = y$ is equivalent to ask if the following equation in $\mathbb{R}$, given by the coordinates, has a unique solution:

    $$x_i + z_i = y_i \quad i = 1,2$$

    Since $(\mathbb{R},+)$ is an abelian group, we can assert that $z_i = y_i - x_i \in \mathbb{R} \quad i=1,2$ is a solution for each equation and is unique.

    In other words, we have that $\forall P,Q \in Re \times Im \ \exists ! z \in \mathbb{C} : P + z = Q$, so the group action $+$ is also regular and the structure $(Re \times Im, +)$ is a torsor.

    <br>

Intuitively, we can think that any complex $t \in \mathbb{C}$ is a two-dimensional vector $\overrightarrow{t}$, then it can be identified with an arrow over a plane by selecting an origin, in this case; $0 \in \mathbb{C}$. Thus, leveraging the equivalence class of free vectors, doing $z + t$ is, geometrically, as if we take $\overrightarrow{t}$ and translate its base from $0$ to $z$, and then the point referenced by $z + \overrightarrow{t}$ in an affine space and $z+t$ are the same.

![complex2](/assets/images/Maths/Analisis/complex2.png)

<br>

### 5.3.2. Multiplication as a rotation.

Let's recapitulate and see that we've defined $\mathbb{C}$ as an $\mathbb{R}$-vector space, a two-dimensional vector space, taking $\mathcal{B}:=\Set{e_1 = (1,0), e_2 = (0,1)}$ as the basis; basically we are referring to the fact that $\mathbb{C} = \text{span}(\mathcal{B})$ and any complex $z$ is a linear combination of these two vectors:

$$\forall z \in \mathbb{C} \ \exists \alpha, \beta \in \mathbb{R} : z = \alpha e_1 + \beta e_2$$

This is nothing new and we already worked with this concepts before.

<br>

Let's now fix some $w \in \mathbb{C}$ and consider $M_w(z) = wz$, observe that this application is linear, thanks to the commutative and distributive properties of $\mathbb{C}$:

$$M_w(\alpha z_1 + \beta z_2)=w(\alpha z_1 + \beta z_2) =\alpha(wz_1)+\beta(wz_2) = \alpha M_w(z_1) + \beta M_w(z_2)$$

So, as we know, considering $\mathcal{B}$, there exists some $2 \times 2$ matrix that characterizes $M_w$. Take that if $z = (z_x,z_y)_{\mathcal{B}} = z_x + iz_y \in \mathbb{C}$, then:

$$ M_w(z) = M_w(z_x + iz_y) = z_xM_w(e_1) + z_yM_w(e_2) = (M_w(1) \ M_w(i)) \begin{pmatrix}z_x \\ z_y\end{pmatrix}$$

So, the columns of our matrix $T$ are where the product with $w$ sends $1$ and $i$, but we can get even further, taking $w = (w_x,w_y)_{\mathcal{B}}$, then:

$$\begin{cases} M_w(1) = (w_x,w_y)(1,0) = (w_x,w_y) \\ M_w(i) = (w_x,w_y)(0,1) = (-w_y,w_x)\end{cases} \implies T_{\mathcal{B}} = (M_w(1) \ M_w(i)) =  \begin{pmatrix}w_x &-w_y \\ w_y & w_x \end{pmatrix}$$

<br>

Thus, $M\_w(z) = T\_{\mathcal{B}}·z = \begin{pmatrix}w\_x &-w\_y \\ w\_y & w\_x \end{pmatrix}\begin{pmatrix}z\_x \\ z\_y\end{pmatrix} $, but let's be careful for a moment and take a closer look. We do know, from the polar form, that for any complex number $z\_x = \|z\|\cos\theta$ and $z\_y = \|z\|\sin\theta$, meaning:

$$M_w(z) = \begin{pmatrix}w_x &-w_y \\ w_y & w_x \end{pmatrix}\begin{pmatrix}z_x \\ z_y\end{pmatrix} = |w||z| \begin{pmatrix}\cos\theta_w &-\sin\theta_w \\ \sin\theta_w & \cos\theta_w \end{pmatrix}\begin{pmatrix}\cos\theta_z \\ \sin\theta_z\end{pmatrix}$$

Observe that, using trigonometric identities:

$$\begin{pmatrix}\cos\theta_w &-\sin\theta_w \\ \sin\theta_w & \cos\theta_w \end{pmatrix}\begin{pmatrix}\cos\theta_z \\ \sin\theta_z\end{pmatrix} = \begin{pmatrix}\cos\theta_w \cos\theta_z - \sin\theta_w \sin\theta_z \\ \sin\theta_w \cos\theta_z + \cos\theta_w \sin\theta_z \end{pmatrix} = \begin{pmatrix} \cos(\theta_w + \theta_z) \\ \sin(\theta_w + \theta_z) \end{pmatrix}$$

Meaning that, essentially:

$$wz =M_w(z) = |w||z|[\cos(\theta_w + \theta_z) + i · \sin(\theta_w + \theta_z)] = (|w||z|)_{\theta_w + \theta_z}$$

Observe that, to the original $z = \|z\|(\cos\theta\_z + i · \sin\theta\_z)$, the product $w·z$ has scaled it by $\|w\|$ and added the angle $\theta\_w$ to $\theta\_z$. 

Thus the product of complex numbers is basically a homothety centered at $0$ with ratio $\|w\| \in \mathbb{R}$ composed with a rotation of $\theta\_w$ about $0$.

![complexrotation](/assets/images/Maths/Analisis/complexrotation.png)

<br>

## 5.4. Conjugate.

The conjugate is one of the most fundamental symmetries in $\mathbb{C}$.  Given $z \in \mathbb{C}$, we define the *conjugate* of $z$, $\overline{z}$ as the complex number obtained by reflecting it across the real axis, $Re$:

![complexconjugate](/assets/images/Maths/Analisis/complexconjugate.png)

According to the definition we have two equivalent representations. Given: $z \in \mathbb{C}$, then:

$$\overline{z} := \begin{cases} z_x - i z_y \\ |z|_{-\theta_z} \end{cases}$$

<br>

The crucial importance of the conjugate is that it captures the invariance for complex solutions to real polynomial equations, this is, if a complex number $z$ is a solution for some real polynomial, then $\overline{z}$ is also a solution.

<br>

# 6. Important properties of Complex Numbers.

We have introduced some important notions about complex numbers, let's mix them up in order to present important results about complex numbers:

<br>

## 6.1. Conjugate properties.

Let's start by saying that, although an algebraic proof will be provided, most of the properties of the conjugate take place by understanding that the real axis acts as a mirror reflecting what happens on each side of the axis onto the other side.

Thus, the conjugate of the addition is the addition of the conjugates and the conjugate of the product is the product of the conjugate:

- $\overline{z}+\overline{w}=(z\_x - iz\_y) + (w\_x -iw\_y) = (z\_x + w\_x) - i(z\_y+w\_y) = \overline{z+w}$

- $\overline{z} · \overline{w} = \|z\|\_{-\theta\_z}\|w\|\_{-\theta\_w} = \|zw\|\_{(-\theta\_z + - \theta\_w)}  = \|zw\|\_{-(\theta\_z + \theta\_w)} = \overline{z·w}$

    <br>

![conjugateaddition](/assets/images/Maths/Analisis/conjugateaddition.png)

![conjugateproduct](/assets/images/Maths/Analisis/conjugateproduct.png)

<br>

Also, observe that adding a complex to its conjugate basically collapses the value onto the real line, so:

- $z + \overline{z} = (z\_x + z\_x) + i(z\_y - z\_y) = 2Re(z)$

And, by the same argument, the subtraction eliminates the real part:

- $z - \overline{z} = z + - \overline{z} = (z\_x - z\_x) + i(z\_y + z\_y) = 2Im(z)$

    <br>

![conjugate2](/assets/images/Maths/Analisis/conjugate2.png)

<br>

Also, let's consider $z\overline{z}$, intuitively, we have that we are making over $\overline{z}$ a rotation that negates its own angle, thus it ends up in the positive part of the real axis:

- $z \neq 0 \implies z\overline{z} \in \mathbb{R}^+$

    Since, $z\overline{z} = \|z\overline{z}\|\_{\theta -\theta} = \|z\overline{z}\|\_0$

    <br>

    ![conjugate3](/assets/images/Maths/Analisis/conjugate3.png)

    <br>

    Lastly, observe also that $z\overline{z} = \|z\|^2 \implies \|z\| = \sqrt{z\overline{z}}$. 
    
    Thus $z \in \mathbb{R} \iff z = \overline{z}$  
    
    $$|z| = \begin{cases} z \quad z \geq 0 \\ -z \quad z < 0\end{cases}$$

    <br>

## 6.2. Absolute Value properties.

Note that, we have the following properties of the absolute value:

- $\|z\| \geq 0 \wedge (\|z\| = 0 \iff z = 0)$

- $\|z\| = \|\overline{z}\|$

- $\|zw\| = \|z\| \|w\|$

The three properties are immediate as we just see until now.

- Observe $-1 \leq \cos\theta \leq 1 \iff -\|z\| \leq \|z\| \cos\theta \leq \|z\| \implies \| Re(z) \| \leq \|z\|$

    <br>

Lastly, let's consider two points $z,w \in \mathbb{C}$ and consider $z+w$. Then, draft $\triangle(0,z,z+w)$ and observe that the relation between $\|z+w\|$ and $\|z\|+\|w\|$ given by the cosine theorem is:

$$|z+w|^2 = |z|^2 + |w|^2 - 2|z||w|\cos(\pi - (\theta_w - \theta_z)) =|z|^2 + |w|^2 + 2|z||w|\cos(\theta_w - \theta_z)$$

Meaning that $\|z+w\|$ is $\|z\|+\|w\|$ plus an angle correction; let's argue then:

Since, again $\|\cos\theta\| \leq 1$, then:


$$|z+w|^2 \leq |z|^2 + |w|^2 + 2|z||w| = (|z\| + |w|)^2 \implies |z+w|  \leq |z| + |w|$$

observe that this implication can be asserted since we are always dealing with the square of positive quantities; $\|z\| \geq 0 \quad \forall z \in \mathbb{C}$

<br>

## 6.3. Cauchy-Schwarz inequality.

### 6.3.1. Appendix: Inner product. Norm. Orthogonality.

Before defining the Cauchy-Schwarz inequality, let's talk a bit about *inner products*, which are, essentially, the structure that transforms linear algebra into geometry.

<br>

We do know, from [this post](https://gsanmi1.github.io/posts/2026/04/08/VectorSpaces/)  that vectors from vector spaces are weighted elements from an abelian group through a field's action. They can compound among themselves to generate other vectors and they can be dilated as much as is convenient using the field's scalars, but they can't say much about themselves. 

Observe that, through the notion of affine space we acquired a geometric notion about vectors as arrows; the family of all possible vectors emerging from a single origin has vector space structure. Then, intuitively as vectors, these arrows can reference any other arrow in the family and, furthermore, they can also serve as models for other arrows emerging from other points (free vector class) but they can't talk about properties relative to their own relative disposition or what properties remain invariant after a transformation (despite being the subject of these questions) without appealing to geometric statements living in the euclidean space. The only thing that two vectors can say about themselves is whether they are proportional or not, a binary geometrical statement.

<br>

This is where the inner product enters; it is the minimal mathematical object that injects this geometric kit onto vector spaces.

<br>

### 6.3.2. Real definition and conceptual explanation.

Consider $V$ an $\mathbb{R}$-vector space, an *inner product* over $V$ is an application: $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$, satisfying:

- $I1$ **Linearity on first argument**: $\langle x+y,z\rangle = \langle x,z\rangle + \langle y,z\rangle$ and $\langle \alpha x,z\rangle = \alpha\langle x,z\rangle$ such $\alpha \in \mathbb{R}$.
- $I2$ **Symmetry**: $\langle x,y\rangle = \langle y,x\rangle$, observe that this means that the linearity also applies to the second argument, it is **bilinear**.
- $I3$ **Positive definite** $\langle x,x\rangle\geq 0$ and $\langle x,x\rangle = 0 \iff x = 0$ 

Let's observe how a geometric structure distills from these axioms.

<br>

### 6.3.3. Induced Norm.

First, we consider that the root of the inner product of a vector with itself behaves in a special way, we define it as the *norm* of a vector:

$$\langle x,x \rangle = \|x\|^2$$

Consider two proportional vectors; $x,y \in V: x = \alpha y, \ \alpha \in \mathbb{R}$, from the vector space perspective, $x$ is a deformed version of $y$, then we have that:

$$\langle x,x \rangle = \langle  \alpha y,  \alpha y \rangle = \alpha^2 \langle y,y \rangle \implies  \frac{\|x\|}{\|y\|}= | \alpha |$$

Meaning that the quotient of the norms of two proportional vectors expresses their proportionality factor. Let's consider now: 

$$e = \frac{1}{\|x\|}x \implies \|e\| = \frac{\|x\|}{\|x\|}  = 1$$

Thus, we can consider a proportional vector $e$ to $x$ with norm $1$ and say that the norm of any vector expresses the absolute value of the dilation factor relative to a proportional vector of unit norm:

$$x = \alpha ' e \implies \|x\| = |\alpha '| \|e\| = |\alpha '|$$

How amplified or narrowed $x$ is expresses the same information as $e$. And this is what we have agreed to call "magnitude". 



<br>

### 6.3.4. Proper inner product expression.

Let's now consider $x,y \in V$ non nulls, and consider the norm of $x+y$, then, the inner product $\langle x,y \rangle$ acquires the following form:


$$\|x+y\|^2 = \langle x+y,x+y \rangle = \langle x,x \rangle + \langle y,y \rangle + 2 \langle x,y \rangle = \|x\|^2 + \|y\|^2 + 2\langle x,y \rangle$$

Concluding:

$$\langle x,y \rangle = \frac{1}{2}\big[\|x+y\|^2 - (\|x\|^2 + \|y\|^2)\big]$$

This is, in terms of magnitude, the inner product measures the defect of the squared magnitude of the composition relative to the addition of each individual squared magnitude of the combined vectors.

Let's explain this idea more deeply. Consider the subspace spanned by $x,y$ which is a real subspace of dimension $2$ and isometric to $\mathbb{R}^2$ (in which euclidean geometry applies) and consider some inner product. 

Then, select $u,v \in \mathbb{R}^2 : \langle u,v \rangle = 0$ and observe that:

$$\langle u,v \rangle = 0 \iff \|u+v\|^2 = \|u\|^2 + \|v\|^2$$

So, identifying the norm of the vector with its geometric length, by Pythagoras, this is equivalent to asserting that $u \perp v$. The inner product introduces geometry in vector spaces by introducing the notion of *disjoint direction*; orthogonality is algebraic perpendicularity. 

Let's explain it a little more, recapitulating; the inner product gives rise to the norm of a vector which is a quantitative factor of how much it dilates the direction in which the inner product situates it (along with all its proportional vectors). Then, it uses this substratum to understand the relation between the vectors' directions by measuring how much each vector's norm factor contributes to the norm of the combined vector. 

If each norm is an expression of its vector's direction, direction interference would affect the norm of the combined vector as the inner product expresses: 

$$\|u+v\|^2 = \|u\|^2 + \|v\|^2 + 2 \langle u,v \rangle$$


Identifying the norm with the length in the euclidean plane, perpendicular directions satisfy the Pythagorean theorem as we indicated above. Considering overlapped directions, the same orientation would be expressed as an expansion, $\langle u,v \rangle > 0$, opposite orientation would appear as a retraction $\langle u,v \rangle < 0$ and perpendicular directions will make $\langle u,v \rangle = 0 \iff u \perp v$

It is important to note that what the norm is, is defined by the inner product itself; the geometry inserted (this disjoint notion) depends entirely on how the norm of a vector gets measured, meaning that, depending on the inner product selected, non-perpendicular vectors can still be mathematically orthogonal (extend through disjoint directions) from the product's perspective.

<br>

Thus, it is enough to say at this point that $\langle x,y \rangle$ measures how much direction both share or simply how aligned they are in terms of direction and norm.

<br>

### 6.3.5. Cauchy-Schwarz and angle between two vectors.

With a basic notion about what inner product is, let's check what Cauchy-Schwarz asserts.

<br>

There are two presentations of the same statement, both are mathematically equivalent but admit distinct immediate readings:

<br>

Let $x,y \in V$, and $\alpha$ a scalar of the field, then:

$$|\langle x,y \rangle| \leq \|x\| \|y\| \wedge \big(| \langle x,y \rangle| = \|x\| \|y\| \iff \exists \alpha: x = \alpha y \big)$$

According to how we understand the inner product, the Cauchy-Schwarz inequality has a direct meaning; the maximum expression of shared direction is proportionality.

Observe that: 

$$x = \alpha y \implies |\langle x,y \rangle| = |\alpha| \langle x,x \rangle = |\alpha| \|x\|\|x\| = \|x\| \|y\| $$

<br>

Directly derived from above we have the following expression:

$$\frac{|\langle x,y\rangle|}{\|x\|\,\|y\|} \in [0,1]$$

<br>

We finally state that the angle between two vectors is;

$$\theta = \arccos{\frac{|\langle x,y\rangle|}{\|x\|\,\|y\|}}$$

<br>

## 6.4. Rudin's 1.35 theorem.

Observe that the $1.35$ theorem in Baby Rudin basically takes $\mathbb{C}^n$ as a vector space and an inner product as:

$$\langle x ,y \rangle = \sum_{i=1}^nx_iy_i$$



Then, our previous expression takes the form:

$$|\langle x,y \rangle| \leq \|x\| \|y\| \iff  \left|\sum_{i=1}^nx_iy_i\right| \leq \left|\sum_{i=1}^nx_i \right| \left| \sum_{i=1}^ny_i\right|$$

Let's see now a demonstration. The demonstration is a little tricky, so to speak. The motivation is an orthogonal projection from which denominators have been subtracted. Essentially, the Cauchy-Schwarz inequality asserts the Pythagorean theorem.

Consider $a,b \in \mathbb{C}^n$ and: 

$$C = \langle a,b \rangle, \quad B = \langle b,b \rangle = \|b\|^2, \quad A = \|a\|^2$$

Now, let's ask ourselves a question: what is the exact part of $b$ in $a$? Or, in other words, what is that $t$ such that $\langle a -tb,b \rangle = 0$? Check that:

$$\langle a -tb,b \rangle = \langle a,b \rangle - t\langle b,b \rangle = 0 \iff t = \frac{\langle a,b \rangle}{\langle b,b \rangle} = \frac{C}{B}$$

This quotient measures the common direction of $a,b$ in terms of the direction of $b$, or in other words, how much $b$'s magnitude occupies in the shared direction of $a$ with $b$.

Check then, calling $r = a - \frac{C}{B}b$:

$$\langle r,\frac{C}{B}b \rangle = 0 \iff \|r +\frac{C}{B}b\| ^2 = \|a\|^2 = \|r\|^2 + \|\frac{C}{B}b\|^2 = \|r\|^2 + \left|\frac{C}{B} \right|^2\|b\|^2$$

Which means:

$$\|r\|^2 = A - \frac{C^2}{B} \geq 0 \iff A B \geq C^2$$

Now, just changing each part:

$$AB = \|a\|^2\|b\|^2 \geq C^2 = \langle a,b \rangle^2 \implies \|a\| \|b\| \geq |\langle a,b \rangle|$$

<br>

# 7. Exercises.

## 7.1. Prove that no order can be defined in the complex field that turns it into an ordered field.

Let's make a brief reminder about what an ordered field is. An ordered field is a field which is also an ordered set and an ordered se which is a non-empty set in which there is defined a binary relation satisfying *reflexivity*, *antisymmetry* and *trychotomy*.

Let's observe a simple fact, given any order $< \subseteq \mathbb{C}^2$, then since $\mathbb{C}$ is a field it satisfies the axiom of the product with the order; this is positive order closure, meaning that the product of any pair of positive numbers should be positive but observe that $i$ simply doesn't fit on it. 

It doesnt care how we define it, always this invariance get's transgresed:

- $i>0 \implies i^2 >0$, but by definition $i^2 = -1 <0$

- $i< 0 \implies -i>0 \implies (-i) (-i) = i^2 >0$, but again $i^2 = -1 <0$

Thus, $\mathbb{C}$ can't be an ordered field because $i$ simply don't fit on it.

<br>

Let's take a closer look on this fact. The real field is a total ordered set, we discussed that total orders allows to dispose all elements in a sequence along a line. We talk that a representation of this order is the positiveness and negativeness of a number which determines on what side of the $0$ this number lies. Then, we stablished that the multiplication had a geometric nuance as an homothety; in the sense that is an operation with a fixed point from which it dilitates each other point in the set. We defined that an homothety of positive ratio respects the sign and negative ratio reverses it, as a consecuence, any squared number is always positive; if the number it self is positive it stills positive and if not, then his own negativeness make his square positive and this is precisely the rule that $i$ brokes as we saw above. 

This is because in $\mathbb{C}$ the product is a homothety combined with a rotation which takes number out of the line, breaking the total order.

<br>

## 7.2. Lexicographic order.

Take $z=(a,b),w=(c,d) \in \mathbb{C}$, then we define the *lexicographic order* as:

$$(a,b) < (c,d) \iff [a < c \vee  (a = c \wedge b < d)]$$

Does $(\mathbb{C}, <)$ have the $LUB$ property?

Let's remember that $LUB$ property stays that for any non-empty upperbounded subset exists the least upperbound element in the universe set.

We can think in the set $A := \Set{z =(a,b) \in \mathbb{C} : a < 1}$, obviously is upperbounded since any $(1,b) \in \mathbb{C}$ is greater than any other element in $A$ so it is upperbounded, but there is not least upper bound, since for any upperbound $(p,q) : p \geq 1$, $(p,q-1)$ is also an upperbound smaller than the first one.

<br>

Let's observe that $\mathbb{C}$ is often presented without an order, not only because with the order it can't be an ordered field but also because there even total orders doesn't make it complete.

<br>

## 7.3. Dual complex roots.

Suppose $z = a +bi$, $w = u + iv$ such:

$$a = \left( \frac{|w| + u}{2} \right), \quad b = \left( \frac{|w| - u}{2} \right)$$

1. Prove that $z^2 = w$ if $v \geq 0$

2. Prove that $\overline{z}^2 = w$ if $v \leq 0$

3. Conclude that every complex number (with one exception!) has two complex square roots.

