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
The tutorials below are designed to be consumed in sequence, but are modular and can be approached in any order. We provide recommendations to scaffold on users’ knowledge and skills, though even advanced users have reported benefiting from the full sequence. All of the notebooks are paired with data that have been preprocessed and are ready for use. Our resources page has helpful links on learning the basics of fMRI preprocessing.
</div>

<div style="padding-top: 1rem;"></div>
#### Getting started
<div class="text-muted">
If you are new to fMRI analysis, Python and/or machine learning:
<ol start="1">
  <li><a href="/tutorials/01-setup">Setup</a>: Get familiar with running a Jupyter notebook.</li>
  <li><a href="/tutorials/02-data-handling">Data handling</a>: Load, reshape and normalize fMRI data in Python.</li>
</ol>
</div>

<div style="padding-top: 0.5rem;"></div>
#### General machine learning
<div class="text-muted">
If you are familiar with fMRI analysis and Python, but have limited experience with machine learning:
<ol start="3">
<li><a href="/tutorials/03-classification">Classification</a>: Run a classifier using leave-one-run-out cross-validation.</li>
  <li><a href="/tutorials/04-dimensionality-reduction">Dimensionality Reduction</a>: Apply PCA and other feature selection techniques.</li>
  <li><a href="/tutorials/05-classifier-optimization">Classifier Optimization</a>: Use cross-validation to optimize classifier hyperparameters.</li>
</ol>
</div>

<div style="padding-top: 0.5rem;"></div>
#### Specific advanced tools
<div class="text-muted">
If you are familiar with fMRI analysis, Python and machine learning:
<ol start="6">
  <li><a href="/tutorials/06-rsa">Representational Similarity Analysis</a>: Compare pattern similarity for human and non-human data.</li>
  <li><a href="/tutorials/07-searchlight">Searchlight</a>: Setup and run a parallelized searchlight analysis.</li>
  <li><a href="/tutorials/08-connectivity">Seed-Based Connectivity</a>: Define seeds and compute functional connectivity.</li>
  <li><a href="/tutorials/09-fcma">Full Correlation Matrix Analysis</a>: Perform an unbiased, seedless, full brain correlation analysis.</li>
  <li><a href="/tutorials/10-isc">Inter-Subject Correlation</a>: Calculate correlations between subjects to reduce noise and estimate task-relevant signals.</li>
  <li><a href="/tutorials/11-SRM">Shared Response Modeling</a>: Use a common stimulus to project subjects into a shared functional space.</li>
  <li><a href="/tutorials/12-hmm">Event Segmentation with Hidden Markov Models</a>: Find latent event states in continuous, naturalistic stimuli.</li>
  <li><a href="/tutorials/13-real-time">Real-Time fMRI</a>: Handle and classify fMRI data generated in real-time.</li>
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
