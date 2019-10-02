# Phylogenetics by Deep Learning (PhyDL)

## Setting up experiment environment

Here are the recommended steps to set up the experiment environment:

1. Install Anaconda or Miniconda.
2. Under the root folder of this project, create a conda environment by
   running `conda env create -p env/ -f environment.yml`.
3. Execute `conda activate env/` to activate the conda environment. Do
   not omit the trailing slash.
4. Run `./setup.py develop` to install evosimz for tree simulation.
5. Unzip data.zip at the root of the project folder.

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

`bin/dnn1.py train` lists all arguments for training. By default, it uses
GPU for training (you should have one for training).

`bin/dnn1.py predict` lists all arguments for prediction. By default, it
uses CPU for inference. To enable GPU inference, add `--device cuda` to
the command line.

Models will be saved under `data/models/<script name>`.
