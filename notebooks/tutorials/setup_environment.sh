#!/bin/bash

# Specify the code necessary to setup your environment to run BrainIAK on a Jupyter notebook. This could involve activating a conda environment (like below) or importing modules.
source activate mybrainiak

# How are you interacting with the notebooks? On a cluster, locally on a laptop, using docker, etc.? This will determine how some functions are launched, such as jupyter and some jobs
configuration='cluster' # includes 'cluster' or 'local' or 'docker'

# Also setup the environment to use some simple visualization tools, like FSL
#module load FSL
