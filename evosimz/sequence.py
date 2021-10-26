"""Protein and nucleotide sequence generators"""

import abc
import random

import logbook
import numpy
import pkg_resources
import scipy.linalg

from . import common

__all__ = (
    'BaseEvolutionSimulator',
    'MultinomialBranchEvolutionSimulator',
    'HeterogeneousBranchEvolutionSimulator',
    'InheritableHeterogeneousBranchEvolutionSimulator',
    'ProteinSimulatorMixin',
    'NucleicAcidSimulatorMixin',
    'MultinomialProteinSequenceSimulator',
    'HeterogeneousProteinSequenceSimulator',
    'InheritableHeterogeneousProteinSequenceSimulator',
)

_MATRIX_FOLDING_FACTOR = 100

_DT = 0.01

_LOG = logbook.Logger(__name__)


class BaseEvolutionSimulator(metaclass=abc.ABCMeta):
    """An abstract sequence simulator."""

    def __init__(self, site_count_range, *, substitution_model):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        site_count_range : tuple[int]
            The upper and lower bounds of substitution sites.
        substitution_model : str
            A substitution model
        """
        self.site_count_range = site_count_range
        self.substitution_model = substitution_model

    def generate_sequences(self, tree, leaves=None):
        """Generate sequences and assign them to the tree nodes.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.
        leaves: list[ete3.PhyloNode] | NoneType
            Limiting simulation to the specified list of leaf nodes,
            ignoring all other leaves. If it is None, simulate all
            nodes. Default is None.
        """
        parameters = self.prepare_parameters()
        if leaves is not None:
            simulating_nodes = set()
            for leaf in leaves:
                node = leaf
                while node is not None:
                    simulating_nodes.add(node)
                    node = node.up
        else:
            simulating_nodes = None
        for node in tree.traverse('preorder'):
            if simulating_nodes is not None and node not in simulating_nodes:
                continue
            if node == tree:
                self._initialize_root(node, **parameters)
            else:
                self._simulate_branch(node, **parameters)
        self.decode_sequences(tree)
        self.clean_up(tree)

    def prepare_parameters(self):
        """Prepare parameters for evolution simulation.

        Returns
        -------
        dict
            A dictionary of simulation parameters.
        """
        r, equilibrium_frequencies = self.load_substitution_model(
            self.substitution_model,
        )
        q = self._calculate_q_matrix(r, equilibrium_frequencies)
        p = self._calculate_p_matrix(q)
        parameters = {
            'site_count': random.randrange(*self.site_count_range),
            'r': r,
            'q': q,
            'p': p,
            'equilibrium_frequencies': equilibrium_frequencies,
        }
        return parameters

    @abc.abstractmethod
    def load_substitution_model(self, model):
        """Load the specified substitution model.

        Parameters
        ----------
        model : str
            The name of the substitution model.

        Returns
        -------
        numpy.ndarray[float]
            The R matrix
        numpy.ndarray[float]
            The equilibrium frequency matrix
        """

    @classmethod
    def _calculate_q_matrix(cls, r, equilibrium_frequencies):
        """Generate Q matrix from R matrix

        Parameters
        ----------
        r: numpy.ndarray
            R matrix, symmetric exchange rates
        equilibrium_frequencies: numpy.ndarray
            specific equilibrium frequency vector

        Returns
        -------
        numpy.ndarray
            Q matrix in sequence evolution
        """
        q = r * equilibrium_frequencies
        numpy.fill_diagonal(q, 0)
        numpy.fill_diagonal(q, -q.sum(axis=1))
        q /= numpy.abs((equilibrium_frequencies * numpy.diag(q)).sum())
        return q

    @classmethod
    def _calculate_p_matrix(cls, q):
        """Generate P matrix

        Parameters
        ----------
        q: numpy.ndarray
            instant rate matrix Q

        Returns
        -------
        numpy.ndarray
            P (transition) matrix in sequence evolution
        """
        return scipy.linalg.expm(q * _DT)

    @classmethod
    @abc.abstractmethod
    def _initialize_root(cls, tree, **__):
        """Generate a sequence for the tree root.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.
        """

    @classmethod
    @abc.abstractmethod
    def _simulate_branch(cls, node, **__):
        """Simulate a sequence for a non-root tree node.

        Parameters
        ----------
        node : ete3.PhyloTreeNode
            A phylogenetic tree.
        """

    @classmethod
    @abc.abstractmethod
    def decode_sequences(cls, tree):
        """Encode all sequences in a tree to bytes.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree with all sequences simulated.
        """

    @classmethod
    def clean_up(cls, tree):
        """Remove extra attributes."""



class MultinomialBranchEvolutionSimulator(BaseEvolutionSimulator,
                                          metaclass=abc.ABCMeta):
    """A basic sequence simulator using multinomial sampling."""

    def prepare_parameters(self):
        """Prepare parameters for evolution simulation.

        Returns
        -------
        dict
            A dictionary of simulation parameters.
        """
        parameters = super().prepare_parameters()
        parameters.update({
            'profile': parameters['equilibrium_frequencies'],
        })
        return parameters

    @classmethod
    def _initialize_root(cls, tree, **parameters):
        """Generate a sequence for the tree root.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.
        """
        sequence = _sample_sequence(parameters['profile'],
                                    parameters['site_count'])
        tree.add_feature('sequence', sequence.astype('i1'))

    @classmethod
    def _simulate_branch(cls, node, **parameters):
        """Evolve the whole sequence along a certain tree branch

        For a specific ancestor state, get multinomial distribution of
        states for all corresponding positions in child node, then sample
        child states for all positions, generate child sequence.

        Parameters
        ----------
        node : ete3.PhyloTreeNode
            A phylogenetic tree.
        p : numpy.ndarray[float]
            The transition matrix.
        """
        ancestor_sequence = node.up.sequence
        folded_p = parameters['p'] / _MATRIX_FOLDING_FACTOR
        numpy.fill_diagonal(folded_p, 0)
        numpy.fill_diagonal(folded_p, 1 - folded_p.sum(axis=1))
        t = node.dist * _MATRIX_FOLDING_FACTOR / _DT
        powered_p = numpy.linalg.matrix_power(folded_p, t)
        frequencies = powered_p[ancestor_sequence, :]
        node.add_feature('sequence', _sample_sequence(frequencies))


class HeterogeneousBranchEvolutionSimulator(BaseEvolutionSimulator,
                                            metaclass=abc.ABCMeta):
    """A sequence simulator for heterogeneous branches"""

    def __init__(self, *args, alpha_range, profile, profile_resampler=None,
                 heterogeneous_branch_ratio='random', rate_swap_ratio='random',
                 profile_swap_model=None, **kwargs):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        site_count_range : tuple[int]
            The upper and lower bounds of substitution sites.
        substitution_model : str
            A substitution model.
        alpha_range : tuple[float]
            The upper and lower range of alpha.
        profile : pathlib.Path | str
            The frequency profile file or name.
        profile_resampler : tuple[str, int] | NoneType
            If it is None, no profile resampling will be performed.
            Otherwise a new profile matrix is generated by resampling.
        heterogeneous_branch_ratio : float | str
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch. If it is
            "random", a random number between 0 and 1 is used instead.
            Default is "random".
        rate_swap_ratio : float | str
            The fraction of site-specific rates to shuffle on a branch.
            If it is "random", a random number between 0 and 1 is used
            instead. Default is "random".
        profile_swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements.
        """
        super().__init__(*args, **kwargs)
        self.alpha_range = alpha_range
        self.profile = profile
        self.profile_resampler = profile_resampler
        self.heterogeneous_branch_ratio = heterogeneous_branch_ratio
        self.rate_swap_ratio = rate_swap_ratio
        self.profile_swap_model = profile_swap_model

    def prepare_parameters(self):
        """Prepare parameters for evolution simulation.

        Returns
        -------
        dict
            A dictionary of simulation parameters.
        """
        parameters = super().prepare_parameters()
        site_count = parameters['site_count']
        equilibrium_frequencies = parameters['equilibrium_frequencies']
        alpha = random.uniform(*self.alpha_range)
        profile = self._generate_profile(
            site_count, equilibrium_frequencies=equilibrium_frequencies,
            profile=self.profile, resampler=self.profile_resampler,
        )
        rates = numpy.random.gamma(alpha, 1 / alpha, size=site_count)
        heterogeneous_branch_ratio = self.heterogeneous_branch_ratio
        if heterogeneous_branch_ratio == 'random':
            heterogeneous_branch_ratio = random.random()
        parameters.update({
            'alpha': alpha,
            'rates': rates,
            'profile': profile,
            'heterogeneous_branch_ratio': heterogeneous_branch_ratio,
            'rate_swap_ratio': self.rate_swap_ratio,
            'profile_swap_model': self.profile_swap_model,
        })
        return parameters

    @classmethod
    def _generate_profile(cls, site_count, *, equilibrium_frequencies,
                          profile, resampler):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        site_count : int
            The number of substitution sites.
        equilibrium_frequencies : numpy.ndarray[float]
            A equilibrium frequency matrix.
        profile : pathlib.Path | str
            The frequency profile file or name.
        resampler : tuple[str, int] | NoneType
            If it is None, no profile resampling will be performed.
            Otherwise a new profile matrix is generated by resampling.
        """
        if profile is None:
            profile = equilibrium_frequencies[None, :]
            return numpy.repeat(profile, site_count, axis=0)
        path = pkg_resources.resource_filename(
            'evosimz', f'heterogeneity_profiles/{profile}',
        )
        count_array = numpy.loadtxt(path) + 1
        profile = count_array / count_array.sum(axis=1, keepdims=True)
        sample = numpy.random.choice(profile.shape[0], site_count)
        profile = profile[sample]
        if resampler is None:
            return profile
        elif not isinstance(resampler, tuple) or len(resampler) != 2:
            raise ValueError(f'invalid resampler: {resampler}')
        elif resampler[0] == 'multinomial':
            for i in range(profile.shape[0]):
                sample = numpy.random.multinomial(
                    resampler[1], profile[i, :]
                ) + resampler[1] / 1e5
                profile[i, :] = sample / sample.sum()
            return profile
        elif resampler[0] == 'dirichlet':
            sample = numpy.random.gamma(profile * resampler[1])
            sample = sample / sample.sum(axis=1, keepdims=True)
            sample = sample.clip(min=numpy.finfo('f4').eps)
            return sample / sample.sum(axis=1, keepdims=True)
        else:
            raise ValueError(f'invalid resampler: {resampler}')

    @classmethod
    def _initialize_root(cls, tree, **parameters):
        """Generate a sequence for the tree root.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        """
        tree.add_feature('sequence', _sample_sequence(parameters['profile']))

    @classmethod
    def _simulate_branch(cls, node, **parameters):
        """Simulate a sequence for a non-root tree node.

        Parameters
        ----------
        node : ete3.PhyloNode
            A phylogenetic tree.
        rates : numpy.ndarray[float]
            The site-specific evolution rates.
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        rate_swap_ratio : float
            The fraction of site-specific rates to shuffle on a branch.
        profile_swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements. If it is None, no swap is
            performed.
        """
        sequence = node.up.sequence.copy()
        heterogeneous_branch_ratio = parameters['heterogeneous_branch_ratio']
        t = node.dist * cls._simulate_branch_rates(
            parameters['rates'], heterogeneous_branch_ratio,
            parameters['rate_swap_ratio'],
        )
        mask = t > 0
        mask_count = mask.sum()
        if mask_count == 0:
            node.add_feature('sequence', sequence)
            return
        profile = cls._generate_branch_profile(
            parameters['profile'], heterogeneous_branch_ratio,
            parameters['profile_swap_model'],
        )
        indices = numpy.arange(profile.shape[1])
        q = parameters['r'] * profile[:, None, :]
        q_diag = q.sum(axis=2) - q[:, indices, indices]
        jump = q / q_diag[..., None]
        jump[:, indices, indices] = 0
        t[mask] -= numpy.random.exponential(numpy.reciprocal(q_diag[mask, sequence[mask]]))
        mask = t > 0
        mask_count = mask.sum()
        while mask_count > 0:
            sequence[mask] = _sample_sequence(jump[mask, sequence[mask]])
            t[mask] -= numpy.random.exponential(numpy.reciprocal(q_diag[mask, sequence[mask]]))
            mask = t > 0
            mask_count = mask.sum()
        node.add_feature('sequence', sequence)

    @classmethod
    def _simulate_branch_rates(cls, rates, heterogeneous_branch_ratio,
                               swap_ratio):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        rates : numpy.ndarray[float]
            The site-specific evolution rates.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        swap_ratio : float
            The fraction of site-specific rates to shuffle on a branch.
        """
        rates = rates.copy()
        if random.random() < heterogeneous_branch_ratio:
            if swap_ratio == 'random':
                swap_ratio = random.random()
            length = rates.shape[0]
            mask = numpy.random.choice(length, round(length * swap_ratio),
                                       replace=False)
            rates[mask] = numpy.random.permutation(rates[mask])
        return rates

    @classmethod
    def _generate_branch_profile(cls, profile, heterogeneous_branch_ratio,
                                 swap_model):
        """Generate a profile matrix for a branch.

        Parameters
        ----------
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements. If it is None, no swap is
            performed.
        """
        profile = profile.copy()
        if (swap_model is not None
                and random.random() < heterogeneous_branch_ratio):
            swap_count = swap_model.rvs(profile.shape[0])
            common.repeated_swap(profile, swap_count)
        return profile


class InheritableHeterogeneousBranchEvolutionSimulator(
    BaseEvolutionSimulator, metaclass=abc.ABCMeta,
):
    """A sequence simulator for inheritable heterogeneous branches"""

    def __init__(self, *args, alpha_range, profile, profile_resampler=None,
                 heterogeneous_branch_ratio='random', rate_swap_ratio='random',
                 profile_swap_model=None, **kwargs):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        site_count_range : tuple[int]
            The upper and lower bounds of substitution sites.
        substitution_model : str
            A substitution model.
        alpha_range : tuple[float]
            The upper and lower range of alpha.
        profile : pathlib.Path | str
            The frequency profile file or name.
        profile_resampler : tuple[str, int] | NoneType
            If it is None, no profile resampling will be performed.
            Otherwise a new profile matrix is generated by resampling.
        heterogeneous_branch_ratio : float | str
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch. If it is
            "random", a random number between 0 and 1 is used instead.
            Default is "random".
        rate_swap_ratio : float | str
            The fraction of site-specific rates to shuffle on a branch.
            If it is "random", a random number between 0 and 1 is used
            instead. Default is "random".
        profile_swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements.
        """
        super().__init__(*args, **kwargs)
        self.alpha_range = alpha_range
        self.profile = profile
        self.profile_resampler = profile_resampler
        self.heterogeneous_branch_ratio = heterogeneous_branch_ratio
        self.rate_swap_ratio = rate_swap_ratio
        self.profile_swap_model = profile_swap_model

    def prepare_parameters(self):
        """Prepare parameters for evolution simulation.

        Returns
        -------
        dict
            A dictionary of simulation parameters.
        """
        parameters = super().prepare_parameters()
        site_count = parameters['site_count']
        equilibrium_frequencies = parameters['equilibrium_frequencies']
        alpha = random.uniform(*self.alpha_range)
        profile = self._generate_profile(
            site_count, equilibrium_frequencies=equilibrium_frequencies,
            profile=self.profile, resampler=self.profile_resampler,
        )
        rates = numpy.random.gamma(alpha, 1 / alpha, size=site_count)
        heterogeneous_branch_ratio = self.heterogeneous_branch_ratio
        if heterogeneous_branch_ratio == 'random':
            heterogeneous_branch_ratio = random.random()
        parameters.update({
            'alpha': alpha,
            'rates': rates,
            'profile': profile,
            'heterogeneous_branch_ratio': heterogeneous_branch_ratio,
            'rate_swap_ratio': self.rate_swap_ratio,
            'profile_swap_model': self.profile_swap_model,
        })
        return parameters

    @classmethod
    def _generate_profile(cls, site_count, *, equilibrium_frequencies,
                          profile, resampler):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        site_count : int
            The number of substitution sites.
        equilibrium_frequencies : numpy.ndarray[float]
            A equilibrium frequency matrix.
        profile : pathlib.Path | str
            The frequency profile file or name.
        resampler : tuple[str, int] | NoneType
            If it is None, no profile resampling will be performed.
            Otherwise a new profile matrix is generated by resampling.
        """
        if profile is None:
            profile = equilibrium_frequencies[None, :]
            return numpy.repeat(profile, site_count, axis=0)
        path = pkg_resources.resource_filename(
            'evosimz', f'heterogeneity_profiles/{profile}',
        )
        count_array = numpy.loadtxt(path) + 1
        profile = count_array / count_array.sum(axis=1, keepdims=True)
        sample = numpy.random.choice(profile.shape[0], site_count)
        profile = profile[sample]
        if resampler is None:
            return profile
        elif not isinstance(resampler, tuple) or len(resampler) != 2:
            raise ValueError(f'invalid resampler: {resampler}')
        elif resampler[0] == 'multinomial':
            for i in range(profile.shape[0]):
                sample = numpy.random.multinomial(
                    resampler[1], profile[i, :]
                ) + resampler[1] / 1e5
                profile[i, :] = sample / sample.sum()
            return profile
        elif resampler[0] == 'dirichlet':
            sample = numpy.random.gamma(profile * resampler[1])
            sample = sample / sample.sum(axis=1, keepdims=True)
            sample = sample.clip(min=numpy.finfo('f4').eps)
            return sample / sample.sum(axis=1, keepdims=True)
        else:
            raise ValueError(f'invalid resampler: {resampler}')

    @classmethod
    def _initialize_root(cls, tree, **parameters):
        """Generate a sequence for the tree root.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree.
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        """
        tree.add_feature('profile', parameters['profile'])
        tree.add_feature('rates', parameters['rates'])
        tree.add_feature('sequence', _sample_sequence(parameters['profile']))

    @classmethod
    def _simulate_branch(cls, node, **parameters):
        """Simulate a sequence for a non-root tree node.

        Parameters
        ----------
        node : ete3.PhyloNode
            A phylogenetic tree.
        rates : numpy.ndarray[float]
            The site-specific evolution rates.
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        rate_swap_ratio : float
            The fraction of site-specific rates to shuffle on a branch.
        profile_swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements. If it is None, no swap is
            performed.
        """
        profile = node.up.profile.copy()
        sequence = node.up.sequence.copy()
        heterogeneous_branch_ratio = parameters['heterogeneous_branch_ratio']
        rates = cls._simulate_branch_rates(
            node.up.rates, heterogeneous_branch_ratio,
            parameters['rate_swap_ratio'],
        )
        node.add_feature('rates', rates)
        t = node.dist * rates
        mask = t > 0
        mask_count = mask.sum()
        if mask_count == 0:
            node.add_feature('sequence', sequence)
            return
        profile = cls._generate_branch_profile(
            node.up.profile, heterogeneous_branch_ratio,
            parameters['profile_swap_model'],
        )
        node.add_feature('profile', profile)
        indices = numpy.arange(profile.shape[1])
        q = parameters['r'] * profile[:, None, :]
        q_diag = q[:, indices, indices] - q.sum(axis=2)
        q[:, indices, indices] = q_diag
        scale_f = - (q_diag * node.pi).sum(axis=-1)
        q = q / scale_f[:, None, None]
        q_diag = q.sum(axis=2) - q[:, indices, indices]
        jump = q / q_diag[..., None]
        jump[:, indices, indices] = 0
        t[mask] -= numpy.random.exponential(numpy.reciprocal(q_diag[mask, sequence[mask]]))
        mask = t > 0
        mask_count = mask.sum()
        while mask_count > 0:
            sequence[mask] = _sample_sequence(jump[mask, sequence[mask]])
            t[mask] -= numpy.random.exponential(numpy.reciprocal(q_diag[mask, sequence[mask]]))
            mask = t > 0
            mask_count = mask.sum()
        node.add_feature('sequence', sequence)

    @classmethod
    def _simulate_branch_rates(cls, rates, heterogeneous_branch_ratio,
                               swap_ratio):
        """Create a BaseSequenceSimulator.

        Parameters
        ----------
        rates : numpy.ndarray[float]
            The site-specific evolution rates.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        swap_ratio : float
            The fraction of site-specific rates to shuffle on a branch.
        """
        rates = rates.copy()
        if random.random() < heterogeneous_branch_ratio:
            if swap_ratio == 'random':
                swap_ratio = random.random()
            length = rates.shape[0]
            mask = numpy.random.choice(length, round(length * swap_ratio),
                                       replace=False)
            rates[mask] = numpy.random.permutation(rates[mask])
        return rates

    @classmethod
    def _generate_branch_profile(cls, profile, heterogeneous_branch_ratio,
                                 swap_model):
        """Generate a profile matrix for a branch.

        Parameters
        ----------
        profile : numpy.ndarray[float]
            The frequency profile matrix.
        heterogeneous_branch_ratio : float
            The probability to regenerate profile matrices and
            site-specific evolution rates on a branch.
        swap_model : scipy.stats.rv_discrete | None
            A statistical model to generate the number of swapping
            site-specific profile elements. If it is None, no swap is
            performed.
        """
        profile = profile.copy()
        if (swap_model is not None
                and random.random() < heterogeneous_branch_ratio):
            swap_count = swap_model.rvs(profile.shape[0])
            common.repeated_swap(profile, swap_count)
        return profile

    @classmethod
    def clean_up(cls, tree):
        for node in tree.traverse():
            node.del_feature('profile')
            node.del_feature('rates')


class ProteinSimulatorMixin:
    """A protein simulator mix-in."""

    _SUBSTITUTION_MODELS = ('cpREV64', 'dayhoff', 'jones', 'lg', 'wag',
                            'mtArt', 'mtmam', 'mtREV24', 'MtZoa')

    def load_substitution_model(self, name):
        """Read a PAML amino acid substitution model.

        Parameters
        ----------
        name: str
            A PAML substitution model name.

        Returns
        -------
        numpy.ndarray[float]
            The R matrix
        numpy.ndarray[float]
            The equilibrium frequency matrix
        """
        if name == 'random':
            name = random.choice(self._SUBSTITUTION_MODELS)
        amino_acid_count = common.AMINO_ACIDS.size
        path = pkg_resources.resource_filename(
            'evosimz', f'substitution_models/{name}.dat',
        )
        string_list = open(path).read().split()
        i = 0
        r = numpy.zeros((amino_acid_count, amino_acid_count))
        for j in range(amino_acid_count):
            for k in range(j):
                r[j, k] = float(string_list[i])
                i += 1
        r = r + r.T
        equilibrium_frequencies = numpy.zeros(amino_acid_count)
        for j in range(amino_acid_count):
            try:
                equilibrium_frequencies[j] = float(string_list[i])
            except ValueError:
                equilibrium_frequencies = None
                break
            else:
                i += 1
        return r, equilibrium_frequencies

    @classmethod
    def decode_sequences(cls, tree):
        """Encode all sequences in a tree to bytes.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree with all sequences simulated.
        """
        for node in tree.traverse('preorder'):
            if hasattr(node, 'sequence'):
                decoded = common.AMINO_ACIDS[node.sequence].tostring()
                node.add_feature('sequence', decoded)


class NucleicAcidSimulatorMixin:
    """A nucleic acid simulator mix-in."""

    _SUBSTITUTION_MODELS = ()

    def load_substitution_model(self, name):
        """Read a PAML nucleotide substitution model.

        Parameters
        ----------
        name: str
            A PAML substitution model name.

        Returns
        -------
        numpy.ndarray[float]
            The R matrix
        numpy.ndarray[float]
            The equilibrium frequency matrix
        """
        if name == 'random':
            name = random.choice(self._SUBSTITUTION_MODELS)
        nucleotide_count = common.NUCLEOTIDES.size
        path = pkg_resources.resource_filename(
            'evosimz', f'substitution_models/{name}.dat',
        )
        string_list = open(path).read().split()
        i = 0
        r = numpy.zeros((nucleotide_count, nucleotide_count))
        for j in range(nucleotide_count):
            for k in range(j):
                r[j, k] = float(string_list[i])
                i += 1
        r = r + r.T
        equilibrium_frequencies = numpy.zeros(nucleotide_count)
        for j in range(nucleotide_count):
            try:
                equilibrium_frequencies[i] = float(string_list[i])
            except ValueError:
                equilibrium_frequencies = None
                break
            else:
                i += 1
        return r, equilibrium_frequencies

    @classmethod
    def decode_sequences(cls, tree):
        """Decode all sequences in a tree to bytes.

        Parameters
        ----------
        tree : ete3.PhyloTree
            A phylogenetic tree with all sequences simulated.
        """
        for node in tree.traverse('preorder'):
            if hasattr(node, 'sequence'):
                decoded = common.NUCLEOTIDES[node.sequence].tostring()
                node.add_feature('sequence', decoded)


class MultinomialProteinSequenceSimulator(
    ProteinSimulatorMixin,
    MultinomialBranchEvolutionSimulator,
):
    """A protein sequence evolution simulator."""


class HeterogeneousProteinSequenceSimulator(
    ProteinSimulatorMixin,
    HeterogeneousBranchEvolutionSimulator,
):
    """A protein sequence simulator with heterogeneity"""


class InheritableHeterogeneousProteinSequenceSimulator(
    ProteinSimulatorMixin,
    InheritableHeterogeneousBranchEvolutionSimulator,
):
    pass


def _sample_sequence(p, n=None):
    """Generate a sequence using multinomial sampling.

    Parameters
    ----------
    p : numpy.ndarray[float]
        If `p` is a 1-D array, `n` must be provided, and the same
        distribution will be applied to all `n` sites. If `p` is a 2-D
        array, `n` will be ignored, and the length of the generated
        sequence will be the first dimension of `p`.
    n : int
        The number of sites. It is only useful when `p` is a 1-D array.

    Returns
    -------
    numpy.ndarray[int]
        A generated sequence index array.
    """
    if p.ndim == 2:
        n = p.shape[0]
    sequence = (numpy.random.random((n, 1)) > p.cumsum(axis=1)).sum(axis=1)
    return sequence.clip(max=(p.shape[-1] - 1)).astype('i1')
