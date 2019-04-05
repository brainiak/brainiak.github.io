---
layout: default
title: Tutorials
---

# {{ page.title }}
<hr class="section-heading-spacer">
<div class="clearfix"></div>
<div class="row">
<div class="col-md-8" markdown="1">
Advanced fMRI analyses have the potential to answer questions that mainstream methods cannot. BrainIAK aims to integrate these cutting-edge techniques into one a single, accessible Python environment. To help users get started, we have created the following set of tutorials based on courses taught at Princeton and Yale Universities.

- [Preview](#preview): browse the tutorials from your web browser
- [Get started](#getting-started): install and run the tutorials from your own machine

## Preview<a name="preview"></a>
The tutorials below are designed to be consumed in sequence, but are modular and can be approached in any order. We provide recommendations to scaffold on users’ prior knowledge and interest. All the noteboooks below assume that pre-processing of the data has been completed. Our resources page has helpful links on learning the basics of fMRI pre-processing.

#### Basics
If you are less familiar with fMRI analyses, Python, or machine learning
<ol start="1">
  <li><a href="/tutorials/01-setup">Setup</a>: Get familiar with running a Jupyter notebook.</li>
  <li><a href="/tutorials/02-data-handling">Data loading and Normalization</a>: Load data into Python and z-score the data.</li>
  <li><a href="/tutorials/03-classification">Classification</a>: Run a classifier using Leave-One-Run-Out cross-validation.</li>
</ol>

#### Intermediate
If you are familiar with the basics of fMRI and Python but have limited experience
<ol start="4">
  <li><a href="/tutorials/04-dimensionality-reduction">Dimensionality Reduction</a>: Apply PCA and other feature selection techniques.</li>
  <li><a href="/tutorials/05-classifier-optimization">Classifier Optimization</a>: Use cross-validation to optimize classifier hyper-parameters.</li>
</ol>

#### Advanced
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

## Getting Started<a name="getting-started"></a>
Need help deciding which option to choose? We have a [list](https://drive.google.com/file/d/1Kj_hVotoau5dGfEbpG-yc1ZoX08HCd5c/view?usp=sharing) of pros and cons to help you decide for each option.

#### Where do you wish to install?
<table class="table">
  <thead>
    <tr class="d-flex">
      <th class="col-4">Laptop / Desktop</th>
      <th class="col-4">Server / Cluster</th>
      <th class="col-4">Yet to Decide</th>
    </tr>
  </thead>
</table>

#### What's your operating system?
<table class="table">
  <thead>
    <tr class="d-flex">
      <th class="col-4">Windows</th>
      <th class="col-4">MacOS</th>
      <th class="col-4">Linux</th>
    </tr>
  </thead>
  <tbody>
    <tr class="d-flex">
      <td class="col-4">Docker.</td>
      <td class="col-4">Use Docker, Conda, or Pip. If you are not a regular Pip user, then use Conda.</td>
      <td class="col-4">Use Docker, Conda, or Pip. If you are not a regular Pip user, then use Conda.</td>
    </tr>
  </tbody>
</table>

#### How many users?
<table class="table">
  <thead>
    <tr class="d-flex">
      <th class="col-6">Only 1</th>
      <th class="col-6">Many</th>
    </tr>
  </thead>
  <tbody>
    <tr class="d-flex">
      <td class="col-6">Install on Laptop/Desktop</td>
      <td class="col-6">Install on Server/Cluster</td>
    </tr>
  </tbody>
</table>

#### What jobs do you plan to run?
<table class="table">
  <thead>
    <tr class="d-flex">
      <th class="col-6">For Quick Piloting</th>
      <th class="col-6">For Long Running Jobs</th>
    </tr>
  </thead>
  <tbody>
    <tr class="d-flex">
      <td class="col-6">Install on Laptop. Use Docker. You will need 5GB RAM for the larger datasets.</td>
      <td class="col-6">Install on Server/Cluster. Use Conda or Pip. Avoid using Docker.</td>
    </tr>
  </tbody>
</table>

#### Are you new to clusters or SLURM?
<table class="table">
  <thead>
    <tr class="d-flex">
      <th class="col-6">Yes</th>
      <th class="col-6">No</th>
    </tr>
  </thead>
  <tbody>
    <tr class="d-flex">
      <td class="col-6">Work with your cluster administrator.</td>
      <td class="col-6">Use Conda or Pip and check the SLURM settings for your cluster. Avoid using Docker.</td>
    </tr>
  </tbody>
</table>

</div>
</div>
