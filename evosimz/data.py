import bisect
import itertools
import pathlib
import pickle
import random

import ete3
import numpy
import torch.utils.data

from . import common

__all__ = [
    'Collator',
    'AdjacencyCollator',
    'PickledDataset',
    'QuartetDataset',
    'PreprunedQuartetDataset',
    'PreprunedAdjacencyDataset',
    'PreprunedQuartetAdjacencyDataset',
    'QuartetAdjacencyDataset',
    'AdjacencyDataset',
    'RandomSampler',
    'RandomChunkSampler',
]

_TREE_PATH = (pathlib.Path(__file__) / '../../data/trees').resolve()


class Collator:
    """A collator that encodes a batch of samples."""

    def __init__(self, sequence_type, *, sample_sites=False):
        """Create a batch collator.

        Parameters
        ----------
        sequence_type : str | numpy.ndarray
            Either `'amino acid'` or `'nucleotide'`. If an numpy.ndarray
            is provided, its flatten version will be treated as the
            alphabet set for hot-one encoding.
        sample_sites : bool
            Whether to sample mutation sites. Default is False.
        """
        self.sequence_type = sequence_type
        self.sample_sites = sample_sites

    def __call__(self, batch):
        """Collate a batch of samples with mutation site sampling.

        If the batch contains taxa of different sequence lengths, a random
        sequence length is selected from all samples in the batch, and all
        sequences are resampled to the selected length.

        Parameters
        ----------
        batch : list
            A batch of samples for collation

        Returns
        -------
        list
            Collated samples.
        """
        trees = []
        sequences = []
        samples = []
        for tree, sequence, *sample in batch:
            trees.extend(tree)
            sequences.append(sequence)
            samples.append(sample)
        if self.sample_sites:
            length = random.choice([sequence.shape[-1]
                                    for sequence in sequences])
            sequences = numpy.stack([common.sample_sites(sequence, length)
                                     for sequence in sequences])
        sequences = common.onehot_encode(sequences, self.sequence_type)
        sequences = torch.utils.data.dataloader.default_collate(sequences)
        # print(sequences.size()) # torch.Size([16, 24, 4, 20, 1591])
        sequences = sequences.view(-1, *sequences.size()[2:])
        # print(sequences.size()) # torch.Size([384, 4, 20, 1591])
        samples = torch.utils.data.dataloader.default_collate(samples)
        # print(0, len(samples), samples[0].size(), samples[1].size()) # 2 torch.Size([16, 24, 4]) 24 length-16 tensors
        samples = [sample.view(-1, *sample.size()[2:]) if not isinstance(sample, list) else sample for sample in samples]
        # print(1, len(samples), samples[0].size(), samples[1].size()) # 2 torch.Size([384, 4]) 24 length-16 tensors
        samples.insert(0, trees)
        samples.insert(1, sequences)
        return samples


class AdjacencyCollator:
    """A collator that encodes samples and adjacency matrices."""

    def __init__(self, sequence_type, *, sample_sites=False):
        """Create a batch collator.

        Parameters
        ----------
        sequence_type : str | numpy.ndarray
            Either `'amino acid'` or `'nucleotide'`. If an numpy.ndarray
            is provided, its flatten version will be treated as the
            alphabet set for hot-one encoding.
        sample_sites : bool
            Whether to sample mutation sites. Default is False.
        """
        self.sequence_type = sequence_type
        self.sample_sites = sample_sites

    def __call__(self, batch):
        """Collate a batch of samples with mutation site sampling.

        If the batch contains taxa of different sequence lengths, a random
        sequence length is selected from all samples in the batch, and all
        sequences are resampled to the selected length.

        Parameters
        ----------
        batch : list
            A batch of samples for collation

        Returns
        -------
        list
            Collated samples.
        """
        trees = []
        sequences = []
        orders = []
        matrices = []
        for tree, sequence, order, matrix in batch:
            trees.extend(tree)
            sequences.append(sequence)
            orders.append(order)
            matrices.append(matrix)
        taxon_counts = [sequence.shape[1] for sequence in sequences]
        taxon_count = max(taxon_counts)
        lengths = [sequence.shape[2] for sequence in sequences]
        if self.sample_sites:
            length = random.choice(lengths)
            sequences = [common.sample_sites(sequence, length)
                         for sequence in sequences]
        elif any(lengths[0] == length for length in lengths[1:]):
            raise RuntimeError('sequence lengths within a batch must be the '
                               'same if site-sampling is disabled')
        else:
            length = lengths[0]
        # FIXME: Hard-coded protein sequence dimension.
        collated_sequences = numpy.zeros((len(trees), taxon_count, 20, length),
                                         dtype='f4')
        collated_matrices = numpy.zeros((len(trees), taxon_count, taxon_count),
                                        dtype='f4')
        offsets = [random.randint(0, taxon_count - c) for c in taxon_counts]
        for i, (offset, sequence, matrix) in enumerate(zip(offsets, sequences,
                                                           matrices)):
            collated_sequences[i, offset:(offset + sequence.shape[1])] = (
                common.onehot_encode(sequence, self.sequence_type)
            )
            orders[i] = [j + offset for j in orders[i]]
            collated_matrices[i, offset:(offset + sequence.shape[1]),
                              offset:(offset + sequence.shape[1])] = matrix
        sequences = torch.utils.data.dataloader.default_collate(
            [collated_sequences])[0]
        matrices = torch.utils.data.dataloader.default_collate(
            [collated_matrices])[0]
        return [trees, sequences, orders, matrices]


class PickledDataset(torch.utils.data.Dataset):
    """A dataset of pickles."""

    def __init__(self, path):
        """Create a pickle dataset.

        Parameters
        ----------
        path : str | pathlib.Path
            Either the name of the dataset in the data folder, or the
            folder of the trees.
        """
        if (_TREE_PATH / path / 'simulator.pickle').exists():
            path = _TREE_PATH / path
        else:
            path = pathlib.Path(path)
        self.samples = []
        for file in path.glob('*.pickle'):
            try:
                int(file.stem)
            except ValueError:
                continue
            else:
                self.samples.append(file)
        self.samples.sort(key=lambda x: int(x.stem))

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The number of tree samples.
        """
        return len(self.samples)

    def __getitem__(self, item):
        """Fetch the specified tree sample.

        Parameters
        ----------
        item : int
            The index of the sample in the folder.

        Returns
        -------
        object
            The pickled object.
        """
        return pickle.load(self.samples[item].open('rb'))


class _QuartetMixin:

    _ORDERS = numpy.asarray(list(itertools.permutations(range(4))))

    @classmethod
    def _shuffle(cls, tree, random_order=False):
        trees = [tree] * cls._ORDERS.shape[0]
        leaves = tree.get_leaves()
        if random_order:
            random.shuffle(leaves)
        sequences = numpy.asarray([leaf.sequence for leaf in leaves])
        sequences = sequences.view('S1').reshape(len(leaves), -1)
        sequences = sequences[cls._ORDERS, :]
        leaf_list = [[leaves[i] for i in order] for order in cls._ORDERS]
        # print(len(trees), sequences.shape, cls._ORDERS.shape, len(leaf_list), sep='\n')
        # 24, (24, 4, 869), (24, 4), 24
        return trees, sequences, cls._ORDERS, leaf_list

    @classmethod
    def _generate_class_label(cls, leaf_list):
        return torch.tensor([
            [leaves[0].up is leaf.up for leaf in leaves[1:]].index(True)
            for leaves in leaf_list
        ], dtype=torch.long)



class QuartetDataset(_QuartetMixin, torch.utils.data.Dataset):
    """A quartet tree dataset."""


    def __init__(self, dataset, random_order=False):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset
        self.random_order = random_order

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The indices of the quartet tree conformation.
        """
        tree = self.dataset[index]
        if len(tree.children) == 2:
            common.unrootz(tree)
        trees, sequences, order, leaf_list = self._shuffle(tree, self.random_order)
        leaf_names = tuple([x.name for x in leaf_list[0]])
        return trees, sequences, order, self._generate_class_label(leaf_list), leaf_names


class PreprunedQuartetDataset(_QuartetMixin, torch.utils.data.Dataset):
    """A prepruned quartet tree dataset."""

    def __init__(self, dataset):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The indices of the quartet tree conformation.
        """
        tree, prepruned = self.dataset[index]
        branch_length_ratio = random.uniform(prepruned[0][0], prepruned[-1][0])
        sample_index = bisect.bisect_left([ratio for ratio, __ in prepruned],
                                          branch_length_ratio)
        tree.prune(prepruned[sample_index][1], preserve_branch_length=True)
        common.unrootz(tree)
        trees, sequences, order, leaf_list = self._shuffle(tree)
        return trees, sequences, order, self._generate_class_label(y)


class _AdjacencyMixin:

    @classmethod
    def _get_adjacency_matrix(cls, tree, leaves=None):
        """Calculate the adjacency matrix.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.

        Returns
        -------
        numpy.ndarray
            The adjacency matrix over all leaves.
        """
        if leaves is None:
            leaves = tree.get_leaves()
        matrix = numpy.zeros((len(leaves), len(leaves)), dtype='f4')
        for i1, node1 in enumerate(leaves):
            for i2, node2 in enumerate(leaves[:i1]):
                matrix[i1, i2] = node1.get_distance(node2)
        matrix = matrix + matrix.T
        return matrix


class PreprunedAdjacencyDataset(_AdjacencyMixin, torch.utils.data.Dataset):
    """A prepruned quartet tree dataset."""

    def __init__(self, dataset, shuffle=None):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        shuffle : int | NoneType
            The number of shuffled samples to generate. If None, only
            the original sample is returned.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset
        self.shuffle = shuffle

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The indices of the quartet tree conformation.
        """
        tree, prepruned = self.dataset[index // (self.shuffle or 1)]
        branch_length_ratio = random.uniform(prepruned[0][0], prepruned[-1][0])
        sample_index = bisect.bisect_left([ratio for ratio, __ in prepruned],
                                          branch_length_ratio)
        tree.prune(prepruned[sample_index][1], preserve_branch_length=True)
        common.unrootz(tree)
        sequences = numpy.array([leaf.sequence for leaf in tree.get_leaves()])
        sequences = sequences.view('S1').reshape(len(sequences), -1)
        adjacency_matrix = self._get_adjacency_matrix(tree)
        if self.shuffle is None:
            order = numpy.arange(sequences.shape[0])
        else:
            order = numpy.random.permutation(sequences.shape[0])
            sequences = sequences[order, :]
            adjacency_matrix = adjacency_matrix[order, :][:, order]
        return ([tree], sequences[None, :], order[None, :],
                adjacency_matrix[None, :])


class PreprunedQuartetAdjacencyDataset(_QuartetMixin, _AdjacencyMixin,
                                       torch.utils.data.Dataset):
    """A prepruned quartet tree dataset."""

    def __init__(self, dataset):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The indices of the quartet tree conformation.
        """
        tree, prepruned = self.dataset[index]
        branch_length_ratio = random.uniform(prepruned[0][0], prepruned[-1][0])
        sample_index = bisect.bisect_left([ratio for ratio, __ in prepruned],
                                          branch_length_ratio)
        tree.prune(prepruned[sample_index][1], preserve_branch_length=True)
        common.unrootz(tree)
        trees, sequences, order, __ = self._shuffle(tree)
        adjacency_matrix = self._get_adjacency_matrix(tree)
        adjacency_matrices = numpy.stack([
            adjacency_matrix[order, :][:, order]
            for order in self._ORDERS
        ])
        return trees, sequences, order, adjacency_matrices


class QuartetAdjacencyDataset(_QuartetMixin, _AdjacencyMixin,
                              torch.utils.data.Dataset):
    """A quartet tree dataset."""

    def __init__(self, dataset):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The indices of the quartet tree conformation.
        """
        tree = self.dataset[index]
        trees, sequences, order, __ = self._shuffle(tree)
        adjacency_matrix = self._get_adjacency_matrix(tree)
        adjacency_matrices = numpy.stack([
            adjacency_matrix[order, :][:, order]
            for order in self._ORDERS
        ])
        return trees, sequences, order, adjacency_matrices


class AdjacencyDataset(_AdjacencyMixin, torch.utils.data.Dataset):
    """A quartet tree dataset."""

    def __init__(self, dataset, shuffle=None):
        """Create a quartet tree dataset.

        Parameters
        ----------
        dataset : evosimz.PickledDataset | str | pathlib.Path
            The underlying tree dataset. If it is not an
            evosimz.PickledDataset, then the value is passed to create an
            evosimz.PickledDataset object.
        shuffle : int | NoneType
            The number of shuffled samples to generate. If None, only
            the original sample is returned.
        """
        if not isinstance(dataset, PickledDataset):
            dataset = PickledDataset(dataset)
        self.dataset = dataset
        self.shuffle = shuffle

    def __len__(self):
        """Returns the size of the tree dataset.

        Returns
        -------
        int
            The size of the dataset.
        """
        return len(self.dataset) * (self.shuffle or 1)

    def __getitem__(self, index):
        """Fetch and encode the sample.

        Parameters
        ----------
        index : int
            The index of the sample in the folder.

        Returns
        -------
        list[ete3.PhyloTree]
            The original tree.
        numpy.ndarray
            The encoded sequences.
        numpy.ndarray
            The shuffling order of the sequences.
        numpy.ndarray
            The adjacency matrix over the taxa. The adjacency matrix is
            never shuffled.
        """
        tree = self.dataset[index // (self.shuffle or 1)]
        sequences = numpy.array([leaf.sequence for leaf in tree.get_leaves()])
        sequences = sequences.view('S1').reshape(len(sequences), -1)
        adjacency_matrix = self._get_adjacency_matrix(tree)
        if self.shuffle is None:
            order = numpy.arange(sequences.shape[0])
        else:
            order = numpy.random.permutation(sequences.shape[0])
            sequences = sequences[order, :]
            adjacency_matrix = adjacency_matrix[order, :][:, order]
        return ([tree], sequences[None, :], order[None, :],
                adjacency_matrix[None, :])


class RandomSampler(torch.utils.data.RandomSampler):
    """A random sampler.

    The sampler fixes the wrong length in the current PyTorch implementation.
    """

    def __len__(self):
        return self.num_samples


class RandomChunkSampler(torch.utils.data.Sampler):
    """A random chunk sampler.

    The sampler divides the dataset into multiple consecutive chunks. It
    samples the consecutive chunks but keeps the chunks altogether.
    """

    def __init__(self, data_source, chunk_size, chunk_count):
        super().__init__(data_source)
        self.data_source = data_source
        if len(data_source) % chunk_size != 0:
            raise ValueError('the dataset cannot be chunked evenly into '
                             'chunks of {}'.format(chunk_size))
        self.chunk_size = chunk_size
        self.chunk_count = chunk_count

    def __iter__(self):
        total_chunk_count = len(self.data_source) // self.chunk_size
        indices = (numpy.random.randint(total_chunk_count,
                                        size=(self.chunk_count, 1))
                   * self.chunk_size + numpy.arange(self.chunk_size))
        numpy.random.shuffle(indices)
        return iter(indices.flatten())

    def __len__(self):
        return self.chunk_size * self.chunk_count
