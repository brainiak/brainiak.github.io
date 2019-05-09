---
layout: tutorial
title: Tutorials
---

<div class='stage' id='stage'>
<div class='block-narrow block-default container' markdown="1">
# {{ page.title }}
<hr class="section-heading-spacer">
<div class="clearfix"></div>
Advanced fMRI analyses have the potential to answer questions that mainstream methods cannot. BrainIAK aims to integrate these cutting-edge techniques into a single, accessible Python environment. To help users get started, we have created the following set of tutorials based on courses taught at Princeton and Yale Universities.

- [Preview](#preview): browse the tutorials from your web browser
- [Get started](#getting-started): install and run the tutorials from your own machine
</div>
</div>

<div class="block-narrow block-inverse block-secondary app-code-block" id="about" style="line-height: 1.55;">
<div class="container" markdown="1">
## Preview<a name="preview"></a>
<div class="text-muted">
The tutorials below are designed to be consumed in sequence, but are modular and can be approached in any order. We provide recommendations to scaffold on users’ prior knowledge and interest. All the notebooks are paired with data that has been preprocessed and ready for use. Our resources page has helpful links on learning the basics of fMRI pre-processing.
</div>

<div style="padding-top: 1rem;"></div>
#### Basics
<div class="text-muted">
If you are less familiar with fMRI analyses, Python, or machine learning
<ol start="1">
  <li><a href="/tutorials/01-setup">Setup</a>: Get familiar with running a Jupyter notebook.</li>
  <li><a href="/tutorials/02-data-handling">Data handling</a>: Load, reshape and normalize fMRI data in Python.</li>
  <li><a href="/tutorials/03-classification">Classification</a>: Run a classifier using Leave-One-Run-Out cross-validation.</li>
</ol>
</div>

<div style="padding-top: 0.5rem;"></div>
#### Intermediate
<div class="text-muted">
If you are familiar with the basics of fMRI and Python but have limited experience
<ol start="4">
  <li><a href="/tutorials/04-dimensionality-reduction">Dimensionality Reduction</a>: Apply PCA and other feature selection techniques.</li>
  <li><a href="/tutorials/05-classifier-optimization">Classifier Optimization</a>: Use cross-validation to optimize classifier hyper-parameters.</li>
</ol>
</div>

<div style="padding-top: 0.5rem;"></div>
#### Advanced
<div class="text-muted">
If you are familiar with Python, fMRI and machine learning
<ol start="6">
  <li><a href="/tutorials/06-rsa">Representational Similarity Analysis</a>: Learn and apply RSA to human and non-human data.</li>
  <li><a href="/tutorials/07-searchlight">Searchlight</a>: Run a searchlight analysis. Information about managing memory use on clusters is also provided.</li>
  <li><a href="/tutorials/08-connectivity">Seed Based Connectivity</a>: Perform seed-based functional connectivity.</li>
  <li><a href="/tutorials/09-fcma">Full Correlation Matrix Analysis</a>: Perform an unbiased, no seed, full brain correlation analysis. Contrast these results with those from a searchlight analysis.</li>
  <li><a href="/tutorials/10-isc">Inter Subject Correlation</a>: Use inter-subject correlations to reduce noise and get a better estimate of the task-relevant signal for a stimulus.</li>
  <li><a href="/tutorials/11-SRM">Shared Response Model</a>: Use a common stimulus (e.g. watching the same movie) across subjects toproject the data into a shared space.</li>
  <li><a href="/tutorials/12-hmm">Event Segmentation and Hidden Markov Models</a>: Use hidden Markov models to find latent states in a movie-viewing dataset.</li>
  <li><a href="/tutorials/13-real-time">Real-Time fMRI</a>: Perform classification on fMRI data  generated in real-time.</li>
</ol>
</div>
</div>
</div>

<div class="block-narrow block-secondary app-about-block" id="preview" markdown="1">
<div class="container" markdown="1">
## Getting started<a name="getting-started"></a>
Detailed installation instructions coming soon!
</div>
</div>
