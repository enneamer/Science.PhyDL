import multiprocessing
import pathlib
import pickle

import fire
import logbook

from .training import *
from .testing import *
from .batchtesting import *
from .batchtest_lbasb import *
from .batchtest_bl50 import *
from .. import tree

__all__ = (training.__all__ + testing.__all__ + batchtesting.__all__ 
           + batchtest_lbasb.__all__ + batchtest_bl50.__all__)

_LOG = logbook.Logger(__name__)

_TREE_PATH = (pathlib.Path(__file__) / '../../../data/trees').resolve()


def _entrypoint():
    """Main entrypoint."""
    logbook.StderrHandler(level='DEBUG').push_application()
    fire.Fire()


def raw(simulator, name, count=1000, job_count=1):
    """Generate samples and save them to the specified folder.

    Parameters
    ----------
    simulator : str
        The simulator name or a path to its pickle file.
    name : str
        The dataset name.
    count : int
        The number of samples to generate. Default is 1000.
    job_count : int
        The number of parallel processes to create. Default is 1.
    """
    try:
        simulator = globals()[simulator]
    except:
        simulator = pickle.load(open(simulator, 'rb'))
    output_path = _TREE_PATH / name
    output_path.mkdir()
    arguments = ((simulator, output_path / f'{i}.pickle')
                 for i in range(count))
    pool = multiprocessing.Pool(job_count)
    pool.starmap(_generate_sample_batches, arguments, 10)
    pool.close()
    pool.join()
    pickle.dump(simulator, (output_path / 'simulator.pickle').open('wb'))


def quartet(simulator, name, count=1000, job_count=1):
    """Generate samples and save them to the specified folder.

    Parameters
    ----------
    simulator : str
        The simulator name or a path to its pickle file.
    name : str
        The dataset name.
    count : int
        The number of samples to generate. Default is 1000.
    job_count : int
        The number of parallel processes to create. Default is 1.
    """
    try:
        simulator = globals()[simulator]
    except:
        simulator = pickle.load(open(simulator, 'rb'))
    output_path = _TREE_PATH / name
    output_path.mkdir()
    arguments = ((simulator, output_path / f'{i}.pickle')
                 for i in range(count))
    pool = multiprocessing.Pool(job_count)
    pool.starmap(_generate_quartet_sample_batches, arguments, 10)
    pool.close()
    pool.join()
    pickle.dump(simulator, (output_path / 'simulator.pickle').open('wb'))


def _generate_sample_batches(simulator, sample_path):
    """Generate and save a single sample.

    Parameters
    ----------
    simulator : tree.BaseTreeSimulator
        A tree generator
    sample_path : pathlib.Path
        The sample output file.
    """
    pickle.dump(simulator.generate(), sample_path.open('wb'))
    _LOG.debug(f'Generating {sample_path}...')


def _generate_quartet_sample_batches(simulator, sample_path):
    """Generate and save pre-pruned samples.

    Parameters
    ----------
    simulator : tree.BaseTreeSimulator
        A tree generator
    sample_path : pathlib.Path
        The sample output file.
    """
    sample = simulator.generate()
    if (isinstance(simulator, tree.QuartetTreeSubsampler) 
        or isinstance(simulator, tree.LBAQuartetTreeSimulator)):
        pickle.dump(sample, sample_path.open('wb'))
    else:
        prepruned = tree.QuartetTreeSubsampler.preprune(sample, 100)
        pickle.dump((sample, prepruned), sample_path.open('wb'))
    _LOG.debug(f'Generating {sample_path}...')
