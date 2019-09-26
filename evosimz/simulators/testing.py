import scipy.stats

from .. import tree
from .. import sequence

__all__ = [
    'testing1_mixed',
    'testing1_nolba',
    'testing1_lba',
    'testing2_mixed',
    'testing2_nolba',
    'testing2_lba',
    'testing3_mixed',
    'testing3_nolba',
    'testing3_lba',
    'testtime_01',
]


testing1_mixed = tree.QuartetTreeSubsampler(
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

testing1_nolba = tree.QuartetTreeSubsampler(
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
    lba_ratio=0.0,
)


testing1_lba = tree.QuartetTreeSubsampler(
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
    lba_ratio=1.0,
)

testing2_mixed = tree.QuartetTreeSubsampler(
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

testing2_nolba = tree.QuartetTreeSubsampler(
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
    lba_ratio=0.0,
)

testing2_lba = tree.QuartetTreeSubsampler(
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
    lba_ratio=1.0,
)

testing3_mixed = tree.QuartetTreeSubsampler(
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

testing3_nolba = tree.QuartetTreeSubsampler(
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
    lba_ratio=0.0,
)

testing3_lba = tree.QuartetTreeSubsampler(
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
    lba_ratio=1.0,
)

testtime_01 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='random',
        alpha_range=(0.5, 0.50000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)