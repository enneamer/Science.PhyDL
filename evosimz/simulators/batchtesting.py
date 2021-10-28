import scipy.stats

from .. import tree
from .. import sequence

__all__ = [
    'test_branch_00',
    'test_branch_01',
    'test_branch_02',
    'test_branch_03',
    'test_branch_04',
    'test_branch_05',
    'test_seqlen_00',
    'test_seqlen_01',
    'test_seqlen_02',
    'test_seqlen_03',
    'test_seqlen_04',
    'test_heterotachy_00',
    'test_heterotachy_01',
    'test_heterotachy_02',
    'test_heterotachy_03',
    'test_heterotachy_04',
    'test_heterogeneity_00',
    'test_heterogeneity_01',
    'test_heterogeneity_02',
    'test_heterogeneity_03',
    'test_heterogeneity_04',
]


# Branch length --------------------------------------------

test_branch_00 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 0.18),
        external_branch_model=scipy.stats.uniform(0.02, 0.18),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

test_branch_01 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.2, 0.2),
        external_branch_model=scipy.stats.uniform(0.2, 0.2),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

test_branch_02 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.4, 0.2),
        external_branch_model=scipy.stats.uniform(0.4, 0.2),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

test_branch_03 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.6, 0.2),
        external_branch_model=scipy.stats.uniform(0.6, 0.2),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

test_branch_04 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.8, 0.2),
        external_branch_model=scipy.stats.uniform(0.8, 0.2),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

test_branch_05 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(1, 1),
        external_branch_model=scipy.stats.uniform(1, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
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

# Sequence length --------------------------------------------

test_seqlen_00 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(100, 200),
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

test_seqlen_01 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(200, 500),
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

test_seqlen_02 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(500, 1000),
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

test_seqlen_03 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 3000),
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

test_seqlen_04 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(3000, 10000),
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

# Heterotachy --------------------------------------------

test_heterotachy_00 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=0,
            profile_swap_model=scipy.stats.randint(0, 1),
        ),
    ),
    lba_ratio=0.0,
)

test_heterotachy_01 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=0.25,
            profile_swap_model=scipy.stats.randint(0, 1),
        ),
    ),
    lba_ratio=0.0,
)

test_heterotachy_02 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 1),
        ),
    ),
    lba_ratio=0.0,
)

test_heterotachy_03 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=0.75,
            profile_swap_model=scipy.stats.randint(0, 1),
        ),
    ),
    lba_ratio=0.0,
)

test_heterotachy_04 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=1.0,
            profile_swap_model=scipy.stats.randint(0, 1),
        ),
    ),
    lba_ratio=0.0,
)
# Heterogeneity --------------------------------------------

test_heterogeneity_00 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.0,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.0,
)

test_heterogeneity_01 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.25,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.0,
)

test_heterogeneity_02 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.5,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.0,
)

test_heterogeneity_03 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=0.75,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.0,
)

test_heterogeneity_04 = tree.QuartetTreeSubsampler(
    base_simulator=tree.TreeSimulator(
        taxon_count_model=scipy.stats.uniform(20, 1),
        internal_branch_model=scipy.stats.uniform(0.02, 1),
        external_branch_model=scipy.stats.uniform(0.02, 1),
        sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
            site_count_range=(1000, 1001),
            substitution_model='random',
            alpha_range=(0.05, 1),
            profile='all.freq',
            profile_resampler=('dirichlet', 10),
            heterogeneous_branch_ratio=1.0,
            rate_swap_ratio=0.5,
            profile_swap_model=scipy.stats.randint(0, 20),
        ),
    ),
    lba_ratio=0.0,
)