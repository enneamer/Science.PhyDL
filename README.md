# Phylogeny inference using deep neural network

## Setting up experiment environment

Here are the recommended steps to set up the experiment environment:

1. Install Anaconda or Miniconda.
2. Under the root folder of this project, create a conda environment by
   running `conda env create -p env/ -f environment.yml`.
3. Execute `conda activate env/` to activate the conda environment. Do
   not omit the trailing slash.
4. Run `./setup.py develop` to install evosimz for tree simulation.
5. Create folders `data/trees` and `data/models` under the root folder
   of the project.

Now you can run files under the "bin" folder for experiments.

To quit the environment, run `conda deactivate`.

To reactivate the environment in the future, run `conda activate env/`.
There is no need to run `./setup.py develop` unless files in the evosimz
module are changed.

## Simulating trees

Run `evosimz <simulator> <dataset name> <sample size> <job count>`.

`simulator` can be either the path to a pickled simulator or a simulator
variable defined in `evosimz.simulators`.

`dataset name` will be the folder name. The generated sample folder will
be placed under `data/trees`.

## Training and prediction

Run scripts under `bin/` to train and predict. Take `bin/q10` as an
example:

`bin/q10 train` lists all arguments for training.

`bin/q10 predict` lists all arguments for prediction.

Models will be saved under `data/models/<script name>`.