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
- [Getting started](#getting-started): install and run the tutorials on your own machine or in the cloud
</div>
</div>

<div class="block-narrow block-inverse block-secondary app-code-block" id="about" style="line-height: 1.55;">
<div class="container" markdown="1">
## Preview<a name="preview"></a>
<div class="text-muted" markdown="1">
The tutorials below are designed to be consumed in sequence, but are modular and can be approached in any order. We provide recommendations to scaffold on users’ knowledge and skills, though even advanced users have reported benefiting from the full sequence. All of the notebooks are paired with [data](#data-downloads) that have been preprocessed and are ready for use. Our [resources](#resources) page has helpful links on learning the basics of fMRI preprocessing.
</div>

<div style="padding-top: 1rem;"></div>
#### First steps
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
Some guidance for how to access / install the tutorials:
- **I want to try the tutorials for myself**: Use Google Colaboratory, Docker, or Conda.
- **I want to set up for multiple users or use BrainIAK for research (i.e., not just running tutorials)**: Use Conda
</div>
</div>

<div class="block-narrow block-inverse block-secondary app-code-block" id="about" style="line-height: 1.55;">
<div class="container" markdown="1">
## Detailed installation instructions

<ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" id="pills-google-colab-tab" data-toggle="pill" data-target="#pills-google-colab" role="tab" aria-controls="pills-google-colab" aria-selected="true">Google Colaboratory</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-docker-macos-tab" data-toggle="pill" data-target="#pills-docker-macos" role="tab" aria-controls="pills-docker-macos" aria-selected="false">Docker (MacOS)</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-docker-windows-tab" data-toggle="pill" data-target="#pills-docker-windows" role="tab" aria-controls="pills-docker-windows" aria-selected="false">Docker (Windows)</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-conda-macos-tab" data-toggle="pill" data-target="#pills-conda-macos" role="tab" aria-controls="pills-conda-macos" aria-selected="false">Conda (MacOS)</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-server-scotty-tab" data-toggle="pill" data-target="#pills-server-scotty" role="tab" aria-controls="pills-server-scotty" aria-selected="false">Server</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-cluster-spock-tab" data-toggle="pill" data-target="#pills-cluster-spock" role="tab" aria-controls="pills-cluster-spock" aria-selected="false">Cluster</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="pills-cluster-admin-tab" data-toggle="pill" data-target="#pills-cluster-admin" role="tab" aria-controls="pills-cluster-admin" aria-selected="false">Cluster (admin)</a>
  </li>
</ul>
<div class="tab-content" id="pills-tabContent">
  <div class="tab-pane fade show active" id="pills-google-colab" role="tabpanel" aria-labelledby="pills-google-colab-tab" markdown="1">

  <h4>Google Colaboratory</h4>
  To only run the tutorials, you can use Google Colaboratory. You only need a web browser. No other installation is necessary. Follow the Colab instructions below. A few notes:

  1. There is a setup that needs to be completed (install brainiak and dependencies, and download data each time you run the tutorials. This can take between 5-15 minutes depending on the size of the dataset you download.
  2. Google Colab has a session timeout of 12 hours (with browser kept open). After 12 hours, you will need to redo the setup to run a tutorial. If the browser window is closed it will reset in 90 minutes.
  3. When running tutorials that cover Inter-Subject Correlations and the Shared Response Model (which use the Pieman dataset), you should reduce the number of subjects to 5. This will ensure that the data do not exceed the available memory.

  If you want to save your code, you can save a copy of the notebook to Google Drive (accessible from the File menu in Colab).

  **Instructions**
  - In Google Chrome go to: colab.research.google.com
  - In the window click on the Github tab (May need to select File->Open_Notebook for window to appear)

    ![alt](/tutorials/img/colab-01.jpeg){:width="800px"}

  - Enter ‘brainiak tutorials’ in the search box
  - Choose branch master (should be already selected by default)
  - Click on notebook `tutorials/colab-env-setup.ipynb` (you may need to scroll down)

    ![alt](/tutorials/img/colab-02.jpeg){:width="800px"}

  - Run cell “Install Brainiak and code dependencies”
  - A window will pop-up. Uncheck “Reset all runtimes before running”

    ![alt](/tutorials/img/colab-03.jpeg){:width="800px"}

  - After the installation is complete run cell “Git-clone helper files for tutorials”
  - There are many download data cells. Pick only the data cell for your tutorial and run that cell. This may take a few minutes depending on the size of the data.
  - You are now ready to execute your notebook.
  - Open a new tab in Chrome and go to colab.research.google.com
  - Click on File->Open Notebook
  - In the window click on the Github tab
  - Enter "brainiak tutorials" in the search box
  - Pick the notebook that you need to run
  - Execute cell
  - A window will pop-up. Uncheck “Reset all runtimes before running”
  - Continue running notebook

  </div>
  <div class="tab-pane fade" id="pills-docker-macos" role="tabpanel" aria-labelledby="pills-docker-macos-tab" markdown="1">

  <h4>Docker on laptop/desktop (MacOS)</h4>
  - Install [Docker](https://docs.docker.com/docker-for-mac/install/).
  - Resize memory for Docker. click: Docker on Menu Bar -> Preferences -> Advanced

    ![alt](/tutorials/img/docker-advanced-macos.png){:width="480px"}

    The more memory and swap space you can assign, the better. We have tested with 5GB of memory. The default setting of 2GB is too little to load large datasets. Also, increase the swap space to approximately 4-5GB. If your available space is less than 4GB, set the swap space to whatever you have available.


  - [Download data](#data-downloads) for the tutorial
    - Create a folder under Downloads: `brainiak_datasets`
    - Unzip the data file and move it to this folder `brainiak_datasets`
  - Shutdown all running Jupyter terminals on your machine to avoid port conflicts
  - Open Terminal
  - Install the BrainIAK Docker by running this command
  - `docker run -it -p 8899:8899 -v ~/Downloads/brainiak_datasets:/root/brainiak_datasets --name tutorials brainiak/tutorials`
  - Installation Completed 😊

  Note the port that you need to connect to the browser: 8899


  <b>Running Tutorials</b>
  - Open a browser on your machine
  - Go to http://localhost:8899 (it’s the port after the `-p` above. Ignore any other port info)
  - You will be prompted for a “Password/Login Token”.
  - Copy the token as shown below

    ![Login Token](/tutorials/img/jupyter-token.jpeg){:width="800px"}

  - Open tutorials and run.

    ![Login Token](/tutorials/img/open-tutorials.png){:width="800px"}

  </div>
  <div class="tab-pane fade" id="pills-docker-windows" role="tabpanel" aria-labelledby="pills-profile-tab" markdown="1">
  <h4>Docker on laptop (Windows)</h4>
  - Install [Docker](https://docs.docker.com/docker-for-windows/) using Linux containers
  - Resize memory for Docker use. We have tested with 5-7GB of memory on Windows. The default setting of 2GB is too small to load large datasets.
Increase the swap space to approximately 4-5GB. If your available space is less than 4GB, set the swap space to whatever you have available.
  - [Download data](#data-downloads) for the tutorial
    - Unzip data and move it to Downloads/brainiak_datasets
  - Share C drive in Docker (instructions [here](https://docs.docker.com/docker-for-windows/#shared-drives))
  - Run Docker after replacing `USERNAME` with your Windows user name:

    `docker run -it -p 8899:8899 -v C:/Users/USERNAME/downloads/brainiak_datasets:/root/brainiak_datasets --name tutorials brainiak/tutorials`

  <b>Running Tutorials</b>
  - Open a browser on your machine
  - Go to http://localhost:8899 (it’s the port after the `-p` above. Ignore any other port info)
  - You will be prompted for a “Password/Login Token”.
  - Copy the token as shown below

    ![Login Token](/tutorials/img/jupyter-token.jpeg){:width="800px"}

  - Open tutorials and run.

    ![Login Token](/tutorials/img/open-tutorials.png){:width="800px"}

  </div>
  <div class="tab-pane fade" id="pills-conda-macos" role="tabpanel" aria-labelledby="pills-contact-tab" markdown="1">
  <h4>Conda on laptop (MacOS)</h4>
  This option is supported for OSX and Linux. For Windows, please use Colab or Docker.
  - Check if you have conda installed already. Run `conda` in your terminal
  - If you have conda installed, proceed to the next step. Only do these steps if you do not have conda installed.
    - Open Terminal
    - Install [Miniconda with Python 3](https://docs.conda.io/en/latest/miniconda.html)
    - Close this terminal.
    - Open a new terminal.
  - Install brainiak-tutorial conda package:

    `conda create --name mybrainiak python=3.6`

    `conda activate mybrainiak` or `source activate mybrainiak`

    `mv ~/.condarc ~/.condarc.bak`

    `conda install -c pni -c defaults -c conda-forge brainiak_tutorials`

  - In any folder that you would like to store the tutorials run:

      `git clone https://github.com/brainiak/brainiak-tutorials.git`

  - [Download data](#data-downloads) for the tutorial
    - Unzip the data file and move it into this folder `~/Downloads/brainiak_datasets`

  <b>Running Tutorials</b>
  - In Terminal, `cd brainiak_tutorials/tutorials`
  - Check your environment
    - Check file `setup_environment.sh` for `CONDA_ENV=mybrainiak`
    - Set `configuration='local'`
  - In Terminal execute:  `run_jupyter.sh`
  - In the browser, you will see a Jupyter window with a list of files
  - Open (double click) `utils.py`
  - A new tab opens up with this file.
  - Update variable `data_path`  to `~/Downloads/brainiak_datasets/`
  - Change

    `data_path = os.path.join(os.path.expanduser('~'), 'brainiak_datasets')` to

    `data_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'brainiak_datasets')`
  - If you move the dataset to any other path, you will need to modify the data_path to reflect the new location of the dataset.
  - Go back to the “Home” tab with the list of files
  - Open assigned tutorial.
  - Execute it.

  </div>
  <div class="tab-pane fade" id="pills-server-scotty" role="tabpanel" aria-labelledby="pills-server-scotty-tab" markdown="1">

  <h4>Conda on server</h4>
  - Connect to server using Terminal
  - Install [Miniconda with Python 3](https://docs.conda.io/en/latest/miniconda.html)

    **Example** install commands:

    `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

    `bash Miniconda3-latest-Linux-x86_64.sh`

    or run the following command to load pre-installed anaconda:

    Here is an **example**: `module load anacondapy/5.3.1`

  - Create a Conda environment

    `conda create -n mybrainiak`

    `source activate mybrainiak` or `conda activate mybrainiak`

  - Ensure that your .condarc is not interfering:

    `mv ~/.condarc ~/.condarc.bak`

  - Install brainiak-tutorial conda package

    `conda install -c pni -c defaults -c conda-forge brainiak_tutorials`

  - [Download data](#data-downloads) for the tutorial

    `wget --no-check-certificate -r -O 'datasets.zip' 'https://docs.google.com/uc?export=download&id=1ZglrmkYw8isBAfsL53n9JgHEucmrnm4E'`

    `unzip datasets.zip`
  - Change data directory path
  - Move data to `~/brainiak_datasets/`

  - In the terminal clone the tutorial repo:

    `git clone https://github.com/brainiak/brainiak-tutorials.git`

  <b>Running Tutorials</b>

  `cd brainiak_tutorials/tutorials`
  - Check your environment
    - Check file `setup_environment.sh` for  `CONDA_ENV=mybrainiak`
    - Check `configuration='server'`
  - Launch Jupyter on server (steps and screen shots [here](https://github.com/brainiak/tutorials/wiki/Launching-notebooks-from-a-cluster) for Jupyter on server)

    `./run_jupyter_remote_server.sh`

    Enter token printed by script when asked for token/password on the jupyter web page
  </div>
  <div class="tab-pane fade" id="pills-cluster-spock" role="tabpanel" aria-labelledby="pills-cluster-spock-tab" markdown="1">

  <h4>Conda on cluster</h4>

  - Install [Miniconda with Python 3](https://docs.conda.io/en/latest/miniconda.html)
  - Install brainiak-tutorial conda package

    `conda install -c pni -c defaults -c conda-forge brainiak_tutorials`

  - [Download data](#data-downloads) for the tutorial
  - Move data to `~/brainiak_datasets/`
  - In terminal, clone the tutorial repository
    - `git clone https://github.com/brainiak/brainiak-tutorials.git`
  - Check directory path in `utils.py`
    - If you change the download location, you will have to update `data_path` in `utils.py`
  - Check your environment
    - Check file `setup_environment.sh` for  `CONDA_ENV=mybrainiak`
    - Set `configuration='cluster'`

  <b>Running Tutorials</b>
  - Check your environment
    - Check file `setup_environment.sh` for  `CONDA_ENV=mybrainiak`
    - Check `configuration='cluster'`
  - Launch Jupyter on cluster (steps and screen shots [here](https://github.com/brainiak/tutorials/wiki/Launching-notebooks-from-a-cluster) for Jupyter on server)

    `cd brainiak-tutorials/tutorials`

    `./run_jupyter_remote_server.sh` (Verify all SLURM parameters for your cluster)

  </div>
  <div class="tab-pane fade" id="pills-cluster-admin" role="tabpanel" aria-labelledby="pills-cluster-admin-tab" markdown="1">

  <h4>Conda on cluster (admin)</h4>
  This installation is typically performed by cluster administrators. As a user, you only need to update the modules used, and the path to the data directory. You are expected to have knowledge of SLURM parameters, for your cluster, to launch the Jupyter notebooks and run batch jobs. Your cluster administrator can help you with setting the SLURM parameters.

  **Administrator tasks**
  - Open Terminal
  - Login to the cluster
  - Install brainiak-tutorial conda package

    `conda install -c pni -c defaults -c conda-forge brainiak_tutorials`

  - Download tutorial data [brainiak_datasets.zip](https://drive.google.com/open?id=1ZglrmkYw8isBAfsL53n9JgHEucmrnm4E)

    `wget --no-check-certificate -r -O 'datasets.zip' 'https://docs.google.com/uc?export=download&id=1ZglrmkYw8isBAfsL53n9JgHEucmrnm4E'`

    `unzip datasets.zip`

  - Move data to a central location where everyone can access.
  - Provide this data path location to all users.

  **User tasks**
  - Get directory path to data from administrator.
  - Verify SLURM parameters with administrator.
  - Open Terminal
  - Login to the cluster
  - Check access to the repo online:
    `https://github.com/brainiak/brainiak-tutorials.git`
  - In the terminal, clone the tutorial repo:
    `git clone https://github.com/brainiak/brainiak-tutorials.git`

    `cd brainiak-tutorials/tutorials/`

  **Run tutorials**
  Edit file `setup_environment.sh` and add the correct module. Your cluster administrator should provide the names of the module(s) (e.g., module load pyger/0.8) to load.

  - Comment out `CONDA_NAME=mybrainiak`
  - Set `configuration='cluster’`
  - Make the `run_jupyter_remote_server.sh` script executable

    `chmod 711 run_jupyter_remote_server.sh`

  - Initiate a remote Jupyter connection to the server - screenshots here: [Jupyter on server](https://github.com/brainiak/tutorials/wiki/Launching-notebooks-from-a-cluster)
  - Run the script: `./run_jupyter_remote_server.sh`
  - Open `utils.py`
  - Update `data_path` in `utils.py` to the path location of the `brainiak_datasets` folder.
  - You will need to update this line:

    `data_path = os.path.join(os.path.expanduser('~'), 'brainiak_datasets')` with the correct path.

  - Run tutorials

  </div>

</div>
</div>
</div>

<div class="block-narrow block-secondary app-about-block" id="about" style="line-height: 1.55;">
<div class="container" markdown="1">
## Data downloads<a name="data-downloads"></a>

These datasets are pre-processed and ready to use. They have been condensed to keep the file size small, by reducing the number of subjects from the original studies. Each tutorial is paired with a dataset as listed below. The file [brainiak_datasets.zip](https://drive.google.com/open?id=1ZglrmkYw8isBAfsL53n9JgHEucmrnm4E) contains the data for all the tutorials, and in unzipped form uses 18GB of space. If you wish to download data for specific tutorials, use the list below to find the correct dataset to download and use. <b>Note that Colab has its own data download mechanism (see Colab install instructions).</b>

- Tutorial 1: No data download needed
- Tutorial 2:  [vdc](https://drive.google.com/open?id=1PrnucQ4hXqUY8gl6ysGJJiTreYu7KOLz)  (Kim et al., 2017) and [02-data-handling-simulated-dataset](https://drive.google.com/open?id=1tiEjtp96zwIdnl3p726llj5KMETnNJ4A) (this is a simulated dataset)
- Tutorials 3-5: [vdc](https://drive.google.com/open?id=1PrnucQ4hXqUY8gl6ysGJJiTreYu7KOLz)  (Kim et al., 2017)
- Tutorial 6: [NinetySix](https://drive.google.com/open?id=14m-YY-N3mCjCdHGkeVlTS4uA7WJzbQS0) (Kriegeskorte et al., 2008)
- Tutorials 7,9: [face_scene](https://drive.google.com/open?id=1LBhKWx5NSlndUlBev3jP997wNiM6HA9N) (Turk-Browne et al., 2012). For running the extra batch script, that computes searchlights within subject, download the [vdc](https://drive.google.com/open?id=1PrnucQ4hXqUY8gl6ysGJJiTreYu7KOLz) dataset.
- Tutorial 8: [latatt](https://drive.google.com/open?id=1iX5nLZvQsWuM5AmKeiBNoP8QkZjlOY7T) (Hutchinson et al., 2016)
- Tutorial 10: [Pieman2](https://drive.google.com/open?id=1IBA39ZZjeGS1u_DvZdiw1AZZQMS3K5q0) (Simony et al., 2016)
- Tutorial 11: [raider](https://drive.google.com/file/d/1zCQoulK_rlzzRb4n6YMVp2cI8vZpxnwx/view?usp=drive_open) (Haxby et al., 2011) and [Pieman2](https://drive.google.com/open?id=1IBA39ZZjeGS1u_DvZdiw1AZZQMS3K5q0) (Simony et al., 2016)
- Tutorial 12: [Sherlock_processed](https://drive.google.com/open?id=11y9iQUoNVyVLANllKebFUrqdvQt-vsXm) (Chen et al., 2017)
- Tutorial 13: No data download needed

The above data urls point to google drive for faster downloads. The doi reference for these tutorial datasets is [https://doi.org/10.5281/zenodo.2598755](https://doi.org/10.5281/zenodo.2598755).

</div>
</div>

<div class="block-narrow block-secondary app-about-block" id="preview" markdown="1">
<div class="container" markdown="1">
## Resources<a name="resources"></a>
We have compiled a list of useful resources that cover the basics of GitHUB, Python, fMRI, and Machine Learning [here](https://github.com/brainiak/brainiak-tutorials/wiki/Resources).
</div>
</div>
