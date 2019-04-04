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

- [Preview](#): browse the tutorials from your web browser
- [Get started](#): install and run the tutorials from your own machine

## Preview
The tutorials below are designed to be consumed in sequence, but are modular and can be approached in any order. We provide recommendations to scaffold on users’ prior knowledge and interest. All the noteboooks below assume that pre-processing of the data has been completed. Our resources page has helpful links on learning the basics of fMRI pre-processing.

#### Basics
If you are less familiar with fMRI analyses, Python, or machine learning
<ol start="1">
  <li><a href="#">Setup</a>: Get familiar with running a Jupyter notebook.</li>
  <li><a href="#">Data loading and Normalization</a>: Load data into Python and z-score the data.</li>
  <li><a href="#">Classification</a>: Run a classifier using Leave-One-Run-Out cross-validation.</li>
</ol>

#### Intermediate
If you are familiar with the basics of fMRI and Python but have limited experience
<ol start="4">
  <li><a href="#">Dimensionality Reduction</a>: Apply PCA and other feature selection techniques.</li>
  <li><a href="#">Classifier Optimization</a>: Use cross-validation to optimize classifier hyper-parameters.</li>
</ol>

#### Advanced
If you are familiar with Python, fMRI and machine learning
<ol start="6">
  <li><a href="#">Representational Similarity Analysis</a>: Learn and apply RSA to human and non-human data.</li>
  <li><a href="#">Searchlights</a>: Run a searchlight analysis. Information about managing memory use on clusters is also</li> provided.
  <li><a href="#">Seed Based Connectivity</a>: Perform seed-based functional connectivity.</li>
  <li><a href="#">Full Correlation Matrix Analysis</a>: Perform an unbiased, no seed, full brain correlation analysis.</li> Contrast these results with those from a searchlight analysis.
  <li><a href="#">Inter Subject Correlation</a>: Use inter-subject correlations to reduce noise and get a better estimate</li> of the task-relevant signal for a stimulus.
  <li><a href="#">Shared Response Model</a>: Use a common stimulus (e.g. watching the same movie) across subjects to</li> project the data into a shared space.
  <li><a href="#">Event Segmentation and Hidden Markov Models</a>: Use hidden Markov models to find latent states in a</li> movie-viewing dataset.
  <li><a href="#">Real-Time fMRI</a>: Perform classification on fMRI data  generated in real-time.</li>
</ol>

## Getting Started
Need help deciding which option to choose? We have a [list](https://drive.google.com/file/d/1Kj_hVotoau5dGfEbpG-yc1ZoX08HCd5c/view?usp=sharing) of pros and cons to help you decide for each option.

<h4>Where do you wish to install?</h4>
<label><input type="radio" name="where" value="laptop-desktop"><span></span> Laptop/Desktop</label>
<label><input type="radio" name="where" value="server-cluster"><span></span> Server/Cluster</label>
<label><input type="radio" name="where" value="yet-to-decide"><span></span> Yet to Decide</label>

<div class="conditional" data-cond-option="where" data-cond-value="laptop-desktop">
  <h4> What's your operating system?</h4>
  <label><input type="radio" name="OS" value="windows"><span></span> Windows</label>
  <label><input type="radio" name="OS" value="macos"><span></span> MacOS</label>
  <label><input type="radio" name="OS" value="linux"><span></span> Linux</label>

  <div class="conditional" data-cond-option="OS" data-cond-value="windows">
    Use docker.
  </div>
  <div class="conditional" data-cond-option="OS" data-cond-value="macos">
    Use Docker, Conda, or Pip. If you are not a regular Pip user, then use conda.
  </div>
  <div class="conditional" data-cond-option="OS" data-cond-value="linux">
    Use Docker, Conda, or Pip. If you are not a regular Pip user, then use conda.
  </div>
</div>

<div class="conditional" data-cond-option="where" data-cond-value="server-cluster">
  <h4>Are you new to clusters or SLURM?</h4>
  <label><input type="radio" name="SLURM" value="yes"><span></span> Yes</label>
  <label><input type="radio" name="SLURM" value="no"><span></span> No</label>

  <div class="conditional" data-cond-option="SLURM" data-cond-value="yes">
    Work with your cluster administrator to get set up.
  </div>
  <div class="conditional" data-cond-option="SLURM" data-cond-value="no">
    Use conda or pip and check the SLURM settings for your cluster. Avoid using Docker.
  </div>
</div>

<div class="conditional" data-cond-option="where" data-cond-value="yet-to-decide">
  <h4>How many users do you need to manage?</h4>
  <label><input type="radio" name="users" value="one"><span></span> Just me</label>
  <label><input type="radio" name="users" value="many"><span></span> Many users</label>
  <div class="conditional" data-cond-option="users" data-cond-value="one">
    <h4> What's your operating system?</h4>
    <label><input type="radio" name="OS" value="windows"><span></span> Windows</label>
    <label><input type="radio" name="OS" value="macos"><span></span> MacOS</label>
    <label><input type="radio" name="OS" value="linux"><span></span> Linux</label>

    <div class="conditional" data-cond-option="OS" data-cond-value="windows">
      Use Docker. If you require long-running, resource-intensive jobs, please also consult the server/cluster installation.
    </div>
    <div class="conditional" data-cond-option="OS" data-cond-value="macos">
      Use Docker, Conda, or Pip. If you are not a regular Pip user, then use conda. If you require long-running, resource-intensive jobs, please also consult the server/cluster installation.
    </div>
    <div class="conditional" data-cond-option="OS" data-cond-value="linux">
      Use Docker, Conda, or Pip. If you are not a regular Pip user, then use conda. If you require long-running, resource-intensive jobs, please also consult the server/cluster installation.
    </div>
  </div>

  <div class="conditional" data-cond-option="users" data-cond-value="many">
    <h4>Are you new to clusters or SLURM?</h4>
    <label><input type="radio" name="SLURM" value="yes"><span></span> Yes</label>
    <label><input type="radio" name="SLURM" value="no"><span></span> No</label>

    <div class="conditional" data-cond-option="SLURM" data-cond-value="yes">
      Work with your cluster administrator to get set up.
    </div>
    <div class="conditional" data-cond-option="SLURM" data-cond-value="no">
      Use conda or pip and check the SLURM settings for your cluster. Avoid using Docker.
    </div>
  </div>
</div>


</div>

</div>
<hr class="section-heading-spacer">
<div class="clearfix"></div>

<script>
function ready(callback){
    // in case the document is already rendered
    if (document.readyState!='loading') callback();
    // modern browsers
    else if (document.addEventListener) document.addEventListener('DOMContentLoaded', callback);
    // IE <= 8
    else document.attachEvent('onreadystatechange', function(){
        if (document.readyState=='complete') callback();
    });
}

ready(function(){
  $('.conditional').conditionize();
  console.log("ready");
});
</script>
