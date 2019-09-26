import pathlib
import shutil

import logbook
import numpy
import torch.nn
import torch.optim
import torch.utils.data

__all__ = [
    'PATIENCE',
    'POOL_SIZE',
    'ensure_clean_folder',
    'initialize_weights',
    'is_stagnant',
    'sort_quartet_scores',
    'sort_adjacency_matrices',
]

WARMUP = 3

PATIENCE = 3

POOL_SIZE = 10

_LOSS_CHECK_SIZE = (PATIENCE + 1) * POOL_SIZE

_LOG = logbook.Logger(__name__)

# _TREECODE_MATRIX = numpy.array(
#     [[1, 2, 3],
#      [1, 3, 2],
#      [2, 1, 3],
#      [2, 3, 1],
#      [3, 1, 2],
#      [3, 2, 1],
#      [1, 3, 2],
#      [1, 2, 3],
#      [3, 1, 2],
#      [3, 2, 1],
#      [2, 1, 3],
#      [2, 3, 1],
#      [2, 3, 1],
#      [2, 1, 3],
#      [3, 2, 1],
#      [3, 1, 2],
#      [1, 2, 3],
#      [1, 3, 2],
#      [3, 2, 1],
#      [3, 1, 2],
#      [2, 3, 1],
#      [2, 1, 3],
#      [1, 3, 2],
#      [1, 2, 3]]
# )

# _SORT_MATRIX = numpy.array(
#     [[0, 1, 2],
#      [0, 2, 1],
#      [1, 0, 2],
#      [2, 0, 1],
#      [1, 2, 0],
#      [2, 1, 0],
#      [0, 2, 1],
#      [0, 1, 2],
#      [1, 2, 0],
#      [2, 1, 0],
#      [1, 0, 2],
#      [2, 0, 1],
#      [2, 0, 1],
#      [1, 0, 2],
#      [2, 1, 0],
#      [1, 2, 0],
#      [0, 1, 2],
#      [0, 2, 1],
#      [2, 1, 0],
#      [1, 2, 0],
#      [2, 0, 1],
#      [1, 0, 2],
#      [0, 2, 1],
#      [0, 1, 2]]
# )

# _XX = numpy.repeat(numpy.arange(24), 3).reshape(-1, 3)


def ensure_clean_folder(path):
    """Remove and recreate a folder.

    Parameters
    ----------
    path : pathlib.Path
        The folder to create.
    """
    if path.exists():
        _LOG.warn(f'Remove existing folder {path}.')
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def initialize_weights(model):
    """Initialize all layers in the Torch model.

    Parameters
    ----------
    model : torch.nn.Module
        A model for initialization.
    """
    for module in model.modules():
        if isinstance(module, torch.nn.Conv1d):
            torch.nn.init.kaiming_uniform_(module.weight.data)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.Conv2d):
            torch.nn.init.kaiming_uniform_(module.weight.data)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.Conv3d):
            torch.nn.init.kaiming_uniform_(module.weight.data)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.BatchNorm1d):
            module.weight.data.fill_(1)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.BatchNorm2d):
            module.weight.data.fill_(1)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.BatchNorm3d):
            module.weight.data.fill_(1)
            module.bias.data.zero_()
        elif isinstance(module, torch.nn.Linear):
            module.weight.data.fill_(1)
            module.bias.data.zero_()


def is_stagnant(loss, patience=PATIENCE):
    """Check if the loss is stagnant.

    Parameters
    ----------
    loss : list[float] | tuple[list[float]]
        A list of validation loss scores. If the loss is a tuple of
        lists of multiple scores, only the first score list is used.
    """
    check_size = (patience + 1) * POOL_SIZE
    if isinstance(loss, tuple):
        loss = loss[0]
    return ((len(loss) % POOL_SIZE == 0) and (len(loss) > check_size)
            and (min(loss) < min(loss[-check_size:])))


def sort_quartet_scores(scores, order):
    """Sort the quartet prediction scores.

    Parameters
    ----------
    scores : torch.Tensor
        The prediction score matrix. The shape should be
        $N \times 3$, where $N$ is the number of samples in the
        batch.
    order : torch.Tensor
        The shuffling order of the sequences from the original tree.

    Returns
    -------
    torch.Tensor
        The sorted scores. The shape is the same as the given
        score matrix.
    """
    indices = torch.arange(3).to(scores.device) + 1
    matrix = order[:, 0, None, None] ^ indices == order[:, 1:, None]
    return matrix.float().bmm(scores[..., None])
    # return torch.from_numpy(scores.cpu().data.numpy()[
    #     (_XX.flatten(), _SORT_MATRIX.flatten())
    # ].reshape(-1, 3))


def sort_adjacency_matrices(scores, order):
    """Sort the predicted adjacency matrices.

    Parameters
    ----------
    scores : torch.Tensor
        The prediction adjacency matrices. The shape should be
        $N \times k \times k$, where $N$ is the number of samples in the
        batch, and $k$ is the number of taxa in each sample.
    order : torch.Tensor
        The shuffling order of the sequences from the original tree.

    Returns
    -------
    torch.Tensor
        The sorted adjacency matrices. The shape is the same as the
        given score tensor.
    """
    batch_size, matrix_size, *__ = scores.size()
    indices = torch.arange(batch_size)[:, None].to(scores.device)
    order = numpy.asarray(order).argsort().flatten()
    return scores[indices, order, :][indices, :, order]
