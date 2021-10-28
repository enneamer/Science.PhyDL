"""Utility functions"""

import numpy

from ._common import repeated_swap

__all__ = (
    'ETE_FORMAT',
    'AMINO_ACIDS',
    'NUCLEOTIDES',
    'onehot_encode',
    'iterate_fasta',
    'repeated_swap',
    'sample_sites',
    'unrootz',
)

ETE_FORMAT = 3

AMINO_ACIDS = numpy.fromstring('ARNDCQEGHILKMFPSTWYV', dtype='S1')

NUCLEOTIDES = numpy.fromstring('ACGT', dtype='S1')


def onehot_encode(sequences, sequence_type):
    """Hot-one encode the given sequence(s).

    Parameters
    ----------
    sequences : numpy.ndarray
        The sequences to encode. The last axis corresponds to the length
        dimension of the sequence. All other axes are treated as
        different sequences.
    sequence_type : str | numpy.ndarray
        Either `'amino acid'` or `'nucleotide'`. If an numpy.ndarray
        is provided, its flatten version will be treated as the
        alphabet set for hot-one encoding.

    Returns
    -------
    numpy.ndarray
        The one-hot-encoded sequence(s). The alphabet dimension is
        inserted as the second to last dimension.
    """
    if sequence_type == 'amino acid':
        alphabet = AMINO_ACIDS
    elif sequence_type == 'nucleotide':
        alphabet = NUCLEOTIDES
    else:
        alphabet = numpy.asarray(sequence_type).flatten()
    encoded = numpy.expand_dims(sequences, -2) == alphabet[:, None]
    return encoded.astype('f4')


def iterate_fasta(path):
    """Iterate through a FASTA file.

    Parameters
    ----------
    path : pathlib.Path
        A FASTA file.

    Yields
    ------
    str
        A sequence name
    bytes
        A sequence
    """
    name = None
    seq = []
    for line in path.open('rb'):
        line = line.strip()
        if line[0] != ord(b'>'):
            seq.append(line)
            continue
        if name is not None:
            yield name.decode(), b''.join(seq)
        name = line[1:]
        seq = []
    if name is not None:
        yield name.decode(), b''.join(seq)


def sample_sites(sequence, length=None):
    """Bootstrap mutation sites.

    Parameters
    ----------
    sequence : numpy.ndarray
        The sequence(s). The last axis is the length dimension.
    length : int | NoneType
        The target length of the sequence(s). If it is None, then the
        original length is used.

    Returns
    -------
    numpy.ndarray
        The bootstrapped sequence(s).
    """
    if length is None:
        length = sequence.shape[-1]
    site_indices = numpy.random.randint(sequence.shape[-1], size=length)
    return sequence[..., site_indices]


def unrootz(tree):
    """Unroot a tree in place.

    Parameters
    ----------
    tree : ete3.TreeNode
        The tree as ete3 TreeNode object.

    Returns
    -------
    """
    if len(tree.children) > 2:
        return
    if not tree.children[0].is_leaf():
        idx = 0
        idy = 1
    elif not tree.children[1].is_leaf():
        idx = 1
        idy = 0
    else:
        return
    new_children = tree.children[idx].children
    tree.children[idy].dist += tree.children[idx].dist
    __ = tree.children[idx].detach()
    for child in new_children:
        tree.add_child(child)
    return