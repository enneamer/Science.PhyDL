"""An interface module for tree simulators"""

import abc
import random

import ete3

from . import sequence

__all__ = [
    'BaseTreeSimulator',
    'TreeSimulator',
    'QuartetTreeSubsampler',
    'LBAQuartetTreeSimulator',
    'TreeSimulatorSwitch',
]


class BaseTreeSimulator(metaclass=abc.ABCMeta):
    """An abstract tree simulator."""

    @abc.abstractmethod
    def generate(self):
        """Generate a tree with simulated sequences.

        Returns
        -------
        ete3.PhyloTree
            A generated tree with simulated sequences.
        """


class TreeSimulator(BaseTreeSimulator):
    """A phylogenetic tree simulator."""

    def __init__(self, taxon_count_model, sequence_simulator,
                 internal_branch_model=None, external_branch_model=None):
        """Create a VanillaTreeSimulator.

        Parameters
        ----------
        taxon_count_model : scipy.stats.rv_discrete | NoneType
            The distribution of taxa counts.
        sequence_simulator : sequence.BaseEvolutionSimulator
            A sequence simulator
        internal_branch_model : scipy.stats.rv_continuous | NoneType
            The branch length bounds. Default: Uniform(0, 1).
        external_branch_model : scipy.stats.rv_continuous | NoneType
            The branch length bounds. Default: Uniform(0, 1).
        """
        super().__init__()
        self.taxon_count_model = taxon_count_model
        self.sequence_simulator = sequence_simulator
        if internal_branch_model is None:
            internal_branch_model = scipy.stats.uniform()
        self.internal_branch_model = internal_branch_model
        if external_branch_model is None:
            external_branch_model = scipy.stats.uniform()
        self.external_branch_model = external_branch_model

    def generate(self):
        """Generate a phylogenetic tree.

        Returns
        -------
        ete3.PhyloTree
            A phylogenetic tree.
        """
        tree = self.populate_tree()
        self.assign_sequences(tree)
        return tree

    def populate_tree(self):
        """Generate a random tree.

        The nodes are named to differentiate leaves and internal nodes.

        Returns
        -------
        ete3.PhyloTree
            A generated tree.
        """
        tree = ete3.PhyloTree()
        tree.populate(int(self.taxon_count_model.rvs()), random_branches=True)
        current_internal_index = 0
        current_leaf_index = 0
        for node in tree.traverse("preorder"):
            if node.is_leaf():
                node.name = f"taxon{current_leaf_index:d}"
                node.dist = self.external_branch_model.rvs()
                current_leaf_index += 1
            else:
                node.name = f"node{current_internal_index:d}"
                node.dist = self.internal_branch_model.rvs()
                current_internal_index += 1
        return tree

    def assign_sequences(self, tree, leaves=None):
        """Simulate and assign sequences to the tree.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A tree without sequences assigned.
        leaves : list[ete3.PhyloNode] | NoneType
            A list of leaf nodes to simulate, ignoring all other leaf
            nodes. If it is None, all nodes will be simulated. Default
            is None.
        """
        self.sequence_simulator.generate_sequences(tree, leaves)


class QuartetTreeSubsampler(BaseTreeSimulator):
    """A quartet tree subsample.

    The subsampler accepts a larger tree from a base tree simulator and
    subsamples four leaf taxa from the tree, with their two ancestor
    node.
    """

    def __init__(self, base_simulator, lba_ratio):
        """Create a quartet tree subsampler

        Parameters
        ----------
        base_simulator : TreeSimulator
            A base tree simulator.
        lba_ratio : float
            The probability to sample an LBA tree.
        """
        super().__init__()
        self.base_simulator = base_simulator
        self.lba_ratio = lba_ratio

    def generate(self):
        """Generate a quartet tree.

        Returns
        -------
        ete3.PhyloTree
            A generated quartet tree.
        """
        tree = self.base_simulator.populate_tree()
        if random.random() < self.lba_ratio:
            __, leaves = self._find_lba_branches(tree)
        else:
            leaves = random.sample(tree.get_leaves(), 4)
        self.base_simulator.assign_sequences(tree, leaves=leaves)
        tree.prune(leaves, preserve_branch_length=True)
        tree.unroot()
        return tree

    @classmethod
    def _find_lba_branches(cls, tree):
        """Find LBA branches with in a tree.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A full tree.

        Returns
        -------
        float
            A score of the LBA quartet tree.
        tuple[ete3.PhyloNode]
            Four leaf nodes of the LBA quartet tree.
        """
        min_branch_ratio = float('+inf')
        leaves = []
        for node in tree.traverse('preorder'):
            if node.is_leaf() or node.is_root():
                continue
            t = tree.copy('newick')
            t.set_outgroup(t & node.name)
            if t.children[0].is_leaf() or t.children[1].is_leaf():
                continue
            (short1, long1), (sdis1, ldis1) = cls._get_extremes(t.children[0])
            if short1 is None or long1 is None:
                continue
            (short2, long2), (sdis2, ldis2) = cls._get_extremes(t.children[1])
            if short2 is None or long2 is None:
                continue
            internal_distance = t.children[0].dist + t.children[1].dist
            branch_ratio = ((internal_distance + max(sdis1, sdis2))
                            / min(ldis1, ldis2))
            if branch_ratio < min_branch_ratio:
                leaves = [short1, long1, short2, long2]
                min_branch_ratio = branch_ratio
        leaves = [tree & leaf.name for leaf in leaves]
        return min_branch_ratio, leaves

    @classmethod
    def _get_extremes(cls, tree):
        """Find the most LBA-like quartet subtree.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.

        Returns
        -------
        tuple[ete3.PhyloNode]
            The farthest and nearest nodes from the root node of the
            given tree.
        tuple[float]
            The distances of the above nodes to the root node.
        """
        longest_distance = float('-inf')
        shortest_distance = float('+inf')
        nearest = None
        farthest = None
        for node in tree.get_leaves():
            distance = node.get_distance(tree)
            if distance > longest_distance:
                longest_distance = distance
                farthest = node
            if distance < shortest_distance:
                shortest_distance = distance
                nearest = node
        return (nearest, farthest), (shortest_distance, longest_distance)

    @classmethod
    def preprune(cls, tree, count): 
    # Should deprecate because ETE3 unrooting eliminate one internal branch!!!
        pruned = []
        leaves = list(tree.get_leaf_names())
        for __ in range(count):
            nodes = random.sample(leaves, 4)
            subtree = tree.copy('newick')
            subtree.prune(nodes, preserve_branch_length=True)
            subtree.unroot()
            branch_length_ratio = cls.calculate_branch_length_ratio(subtree)
            pruned.append((branch_length_ratio, nodes))
        pruned.sort()
        return pruned

    @classmethod
    def calculate_branch_length_ratio(cls, qtree):
        dis1 = []
        for child in qtree.children:
            if child.is_leaf():
                dis1.append(child.dist)
            else:
                int_dis = child.dist
                dis2 = [x.dist for x in child.children]
        return (int_dis + max([min(dis1), min(dis2)])) / min([max(dis1), max(dis2)])


class LBAQuartetTreeSimulator(BaseTreeSimulator):
    """An LBA quartet tree simulator."""

    def __init__(self, short_branch_range, long_branch_range,
                 internal_branch_range, sequence_simulator,
                 is_farris=False):
        """Create a LBAQuartetTreeSimulator.

        Parameters
        ----------
        short_branch_range : tuple
            The short branch length bounds.
        long_branch_range : tuple
            The long branch length bounds.
        internal_branch_range : tuple
            The internal branch length bounds.
        sequence_simulator : sequence.BaseEvolutionSimulator
            The specification of a sequence simulator.
        is_farris : binary
            Whether to simulate Farris-style quartet or Felsenstein style
        """
        super().__init__()
        self.short_branch_range = short_branch_range
        self.long_branch_range = long_branch_range
        self.internal_branch_range = internal_branch_range
        self.sequence_simulator = sequence_simulator
        self.is_farris = is_farris

    def generate(self):
        """Generate an LBA quartet tree.

        Returns
        -------
        ete3.PhyloTree
            An LBA quartet tree.
        """
        branch0 = random.uniform(*self.short_branch_range)
        branch1 = random.uniform(*self.long_branch_range)
        branch2 = random.uniform(*self.short_branch_range)
        branch3 = random.uniform(*self.long_branch_range)
        branch4 = random.uniform(*self.internal_branch_range) / 2
        branch5 = random.uniform(*self.internal_branch_range) / 2
        if self.is_farris:
            tree = (f'((taxon0:{branch0},taxon1:{branch2})node1:{branch4},'
                    f'(taxon2:{branch1},taxon3:{branch3})node2:{branch5});')
        else:
            tree = (f'((taxon0:{branch0},taxon1:{branch1})node1:{branch4},'
                    f'(taxon2:{branch2},taxon3:{branch3})node2:{branch5});')
        tree = ete3.PhyloTree(tree, format=3)
        self.sequence_simulator.generate_sequences(tree)
        return tree


class TreeSimulatorSwitch(BaseTreeSimulator):
    """A simulator that randomly chooses one of its base simulator."""

    def __init__(self, simulator1, simulator2, ratio):
        """Create a TreeSimulatorSwitch.

        Parameters
        ----------
        simulator1 : BaseTreeSimulator
            The first base tree simulator.
        simulator2 : BaseTreeSimulator
            The second base tree simulator.
        ratio : float
            The ratio of generated trees from the first base simulator.
        """
        super().__init__()
        self.simulator1 = simulator1
        self.simulator2 = simulator2
        self.ratio = ratio

    def generate(self):
        """Randomly choose a simulator to generate a tree.

        Returns
        -------
        ete3.PhyloTree
            A phylogenetic tree.
        """
        if random.random() < self.ratio:
            return self.simulator1.generate()
        else:
            return self.simulator2.generate()
