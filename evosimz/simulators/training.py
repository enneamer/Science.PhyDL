import scipy.stats

from .. import tree
from .. import sequence

__all__ = [
    'training1',
    'training2',
    'training3',
]


training1 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(5, 100),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(100, 3000),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.9,
            rate_swap_ratio='random',
            profile_swap_model=scipy.stats.randint(10, 20),
        ),
    ),
    lba_ratio=0.15,
)


training2 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(5, 100),
        internal_branch_model=scipy.stats.gamma(a=1, scale=0.1/1),
        external_branch_model=scipy.stats.gamma(a=2, scale=0.2/2),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(100, 3000),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.9,
            rate_swap_ratio='random',
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.15,
)


training3 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(5, 100),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(100, 3000),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio='random',
            rate_swap_ratio='random',
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.15,
)
