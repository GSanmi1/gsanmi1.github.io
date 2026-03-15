---
layout: post
title: "Mathematics in Machine Learning"
subtitle: "The importance of the maths in ML. Introduction of MML book."
date: 2026-03-14 09:00:00 +0000
categories: ['Maths', 'MML']
tags: ['Maths']
author: German Sanmi
---


# 1. Introduction.

## 1.1. Introducing machine learning.

Machine learning is about designing algorithms that automatically extract valuable information from data. The emphasis here is on “automatic”, machine learning is concerned about general-purpose methodologies that can be applied to many datasets, while producing something that is meaningful. 

There are three concepts that are at the core of machine learning: data, a model, and learning.

- Since machine learning is inherently data driven, *data* is at the core data of machine learning. 

    The goal of machine learning is to design generalpurpose methodologies to extract *valuable patterns* from data, ideally without much domain-specific expertise. For example, given a large corpus of documents (e.g., books in many libraries), machine learning methods can be used to automatically find relevant topics that are shared across documents.

    <br>

-  To achieve this goal, we design *models* that are typically related to the process that generates data, similar to model the dataset we are given. 

    For example, in a regression setting, the model would describe a function that maps inputs to real-valued outputs. To paraphrase Mitchell (1997): A model is said to learn from data if its performance on a given task improves after the data is taken into account. The goal is to find good models that generalize well to yet unseen data, which we may care about in the future. 

    <br>

- *Learning* can be understood as a learning way to automatically find patterns and structure in data by optimizing the parameters of the model.

    <br>


While machine learning has seen many success stories, and software is readily available to design and train rich and flexible machine learning systems, we believe that the mathematical foundations of machine  learning are important in order to understand fundamental principles upon which more complicated machine learning systems are built. Understanding these principles can facilitate creating new machine learning solutions, understanding and debugging existing approaches, and learning about the inherent assumptions and limitations of the methodologies we are working with.

<br>

## 1.2. Finding words for intuitions.

A challenge we face regularly in machine learning is that concepts and words are slippery, and a particular component of the machine learning system can be abstracted to different mathematical concepts.

For example, the word “algorithm” is used in at least two different senses in the context of machine learning:

-  In the first sense, we use the phrase “machine learning algorithm” to mean a system that makes predictions based on input data. We refer to these algorithms as *predictors*.

-  In the second sense, we use the exact same phrase “machine learning algorithm” to mean a system that adapts some internal parameters of the predictor so that it performs well on future unseen input data. Here we refer to this adaptation as *training* a system.

We attempt to make the context sufficiently clear to reduce the level of ambiguity.

A *model* is typically used to describe a process for generating data, similar to the dataset at hand. Therefore, good models can also be thought of as simplified versions of the real (unknown) data-generating process, capturing aspects that are relevant for modeling the data and extracting hidden patterns from it. A good model can then be used to predict what would happen in the real world without performing real-world experiments.

We now come to the crux of the matter, the learning component of machine learning. 

Assume we are given a dataset and a suitable model. Training the model means to use the data available to optimize some parameters of the model with respect to a utility function that evaluates how well the model predicts the training data. Most training methods can be thought of as an approach analogous to climbing a hill to reach its peak. In this analogy, the peak of the hill corresponds to a maximum of some desired performance measure. However, in practice, we are interested in the model to perform well on unseen data. Performing well on data that we have already seen (training data) may only mean that we found a good way to memorize the data. However, this may not generalize well to unseen data, and, in practical applications, we often need to expose our machine learning system to situations that it has not encountered before.

Let us summarize the main concepts of machine learning that we cover in this book:

- We represent data as vectors.
- We choose an appropriate model, either using the probabilistic or optimization view.
- We learn from available data by using numerical optimization methods with the aim that the model performs well on data not used for training.