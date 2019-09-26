import scipy.stats

from .. import tree
from .. import sequence

__all__ = [
    'testlba_F_h0_p02_q10_r001',
    'testlba_F_h0_p02_q10_r002',
    'testlba_F_h0_p02_q10_r005',
    'testlba_F_h0_p02_q10_r010',
    'testlba_F_h0_p02_q10_r020',
    'testlba_F_h0_p02_q10_r050',
    'testlba_F_h0_p02_q10_r100',
    'testlba_F_h0_p02_q20_r001',
    'testlba_F_h0_p02_q20_r002',
    'testlba_F_h0_p02_q20_r005',
    'testlba_F_h0_p02_q20_r010',
    'testlba_F_h0_p02_q20_r020',
    'testlba_F_h0_p02_q20_r050',
    'testlba_F_h0_p02_q20_r100',
    'testlba_F_h0_p02_q50_r001',
    'testlba_F_h0_p02_q50_r002',
    'testlba_F_h0_p02_q50_r005',
    'testlba_F_h0_p02_q50_r010',
    'testlba_F_h0_p02_q50_r020',
    'testlba_F_h0_p02_q50_r050',
    'testlba_F_h0_p02_q50_r100',
    'testlba_F_h0_p02_q100_r001',
    'testlba_F_h0_p02_q100_r002',
    'testlba_F_h0_p02_q100_r005',
    'testlba_F_h0_p02_q100_r010',
    'testlba_F_h0_p02_q100_r020',
    'testlba_F_h0_p02_q100_r050',
    'testlba_F_h0_p02_q100_r100',
    'testlba_F_h0_p05_q10_r001',
    'testlba_F_h0_p05_q10_r002',
    'testlba_F_h0_p05_q10_r005',
    'testlba_F_h0_p05_q10_r010',
    'testlba_F_h0_p05_q10_r020',
    'testlba_F_h0_p05_q10_r050',
    'testlba_F_h0_p05_q10_r100',
    'testlba_F_h0_p05_q20_r001',
    'testlba_F_h0_p05_q20_r002',
    'testlba_F_h0_p05_q20_r005',
    'testlba_F_h0_p05_q20_r010',
    'testlba_F_h0_p05_q20_r020',
    'testlba_F_h0_p05_q20_r050',
    'testlba_F_h0_p05_q20_r100',
    'testlba_F_h0_p05_q50_r001',
    'testlba_F_h0_p05_q50_r002',
    'testlba_F_h0_p05_q50_r005',
    'testlba_F_h0_p05_q50_r010',
    'testlba_F_h0_p05_q50_r020',
    'testlba_F_h0_p05_q50_r050',
    'testlba_F_h0_p05_q50_r100',
    'testlba_F_h0_p05_q100_r001',
    'testlba_F_h0_p05_q100_r002',
    'testlba_F_h0_p05_q100_r005',
    'testlba_F_h0_p05_q100_r010',
    'testlba_F_h0_p05_q100_r020',
    'testlba_F_h0_p05_q100_r050',
    'testlba_F_h0_p05_q100_r100',
    'testlba_F_h0_p10_q10_r001',
    'testlba_F_h0_p10_q10_r002',
    'testlba_F_h0_p10_q10_r005',
    'testlba_F_h0_p10_q10_r010',
    'testlba_F_h0_p10_q10_r020',
    'testlba_F_h0_p10_q10_r050',
    'testlba_F_h0_p10_q10_r100',
    'testlba_F_h0_p10_q20_r001',
    'testlba_F_h0_p10_q20_r002',
    'testlba_F_h0_p10_q20_r005',
    'testlba_F_h0_p10_q20_r010',
    'testlba_F_h0_p10_q20_r020',
    'testlba_F_h0_p10_q20_r050',
    'testlba_F_h0_p10_q20_r100',
    'testlba_F_h0_p10_q50_r001',
    'testlba_F_h0_p10_q50_r002',
    'testlba_F_h0_p10_q50_r005',
    'testlba_F_h0_p10_q50_r010',
    'testlba_F_h0_p10_q50_r020',
    'testlba_F_h0_p10_q50_r050',
    'testlba_F_h0_p10_q50_r100',
    'testlba_F_h0_p10_q100_r001',
    'testlba_F_h0_p10_q100_r002',
    'testlba_F_h0_p10_q100_r005',
    'testlba_F_h0_p10_q100_r010',
    'testlba_F_h0_p10_q100_r020',
    'testlba_F_h0_p10_q100_r050',
    'testlba_F_h0_p10_q100_r100',
    'testlba_F_h0_p20_q10_r001',
    'testlba_F_h0_p20_q10_r002',
    'testlba_F_h0_p20_q10_r005',
    'testlba_F_h0_p20_q10_r010',
    'testlba_F_h0_p20_q10_r020',
    'testlba_F_h0_p20_q10_r050',
    'testlba_F_h0_p20_q10_r100',
    'testlba_F_h0_p20_q20_r001',
    'testlba_F_h0_p20_q20_r002',
    'testlba_F_h0_p20_q20_r005',
    'testlba_F_h0_p20_q20_r010',
    'testlba_F_h0_p20_q20_r020',
    'testlba_F_h0_p20_q20_r050',
    'testlba_F_h0_p20_q20_r100',
    'testlba_F_h0_p20_q50_r001',
    'testlba_F_h0_p20_q50_r002',
    'testlba_F_h0_p20_q50_r005',
    'testlba_F_h0_p20_q50_r010',
    'testlba_F_h0_p20_q50_r020',
    'testlba_F_h0_p20_q50_r050',
    'testlba_F_h0_p20_q50_r100',
    'testlba_F_h0_p20_q100_r001',
    'testlba_F_h0_p20_q100_r002',
    'testlba_F_h0_p20_q100_r005',
    'testlba_F_h0_p20_q100_r010',
    'testlba_F_h0_p20_q100_r020',
    'testlba_F_h0_p20_q100_r050',
    'testlba_F_h0_p20_q100_r100',
    'testlba_F_h0_p40_q10_r001',
    'testlba_F_h0_p40_q10_r002',
    'testlba_F_h0_p40_q10_r005',
    'testlba_F_h0_p40_q10_r010',
    'testlba_F_h0_p40_q10_r020',
    'testlba_F_h0_p40_q10_r050',
    'testlba_F_h0_p40_q10_r100',
    'testlba_F_h0_p40_q20_r001',
    'testlba_F_h0_p40_q20_r002',
    'testlba_F_h0_p40_q20_r005',
    'testlba_F_h0_p40_q20_r010',
    'testlba_F_h0_p40_q20_r020',
    'testlba_F_h0_p40_q20_r050',
    'testlba_F_h0_p40_q20_r100',
    'testlba_F_h0_p40_q50_r001',
    'testlba_F_h0_p40_q50_r002',
    'testlba_F_h0_p40_q50_r005',
    'testlba_F_h0_p40_q50_r010',
    'testlba_F_h0_p40_q50_r020',
    'testlba_F_h0_p40_q50_r050',
    'testlba_F_h0_p40_q50_r100',
    'testlba_F_h0_p40_q100_r001',
    'testlba_F_h0_p40_q100_r002',
    'testlba_F_h0_p40_q100_r005',
    'testlba_F_h0_p40_q100_r010',
    'testlba_F_h0_p40_q100_r020',
    'testlba_F_h0_p40_q100_r050',
    'testlba_F_h0_p40_q100_r100',
    'testlba_F_h1_p02_q10_r001',
    'testlba_F_h1_p02_q10_r002',
    'testlba_F_h1_p02_q10_r005',
    'testlba_F_h1_p02_q10_r010',
    'testlba_F_h1_p02_q10_r020',
    'testlba_F_h1_p02_q10_r050',
    'testlba_F_h1_p02_q10_r100',
    'testlba_F_h1_p02_q20_r001',
    'testlba_F_h1_p02_q20_r002',
    'testlba_F_h1_p02_q20_r005',
    'testlba_F_h1_p02_q20_r010',
    'testlba_F_h1_p02_q20_r020',
    'testlba_F_h1_p02_q20_r050',
    'testlba_F_h1_p02_q20_r100',
    'testlba_F_h1_p02_q50_r001',
    'testlba_F_h1_p02_q50_r002',
    'testlba_F_h1_p02_q50_r005',
    'testlba_F_h1_p02_q50_r010',
    'testlba_F_h1_p02_q50_r020',
    'testlba_F_h1_p02_q50_r050',
    'testlba_F_h1_p02_q50_r100',
    'testlba_F_h1_p02_q100_r001',
    'testlba_F_h1_p02_q100_r002',
    'testlba_F_h1_p02_q100_r005',
    'testlba_F_h1_p02_q100_r010',
    'testlba_F_h1_p02_q100_r020',
    'testlba_F_h1_p02_q100_r050',
    'testlba_F_h1_p02_q100_r100',
    'testlba_F_h1_p05_q10_r001',
    'testlba_F_h1_p05_q10_r002',
    'testlba_F_h1_p05_q10_r005',
    'testlba_F_h1_p05_q10_r010',
    'testlba_F_h1_p05_q10_r020',
    'testlba_F_h1_p05_q10_r050',
    'testlba_F_h1_p05_q10_r100',
    'testlba_F_h1_p05_q20_r001',
    'testlba_F_h1_p05_q20_r002',
    'testlba_F_h1_p05_q20_r005',
    'testlba_F_h1_p05_q20_r010',
    'testlba_F_h1_p05_q20_r020',
    'testlba_F_h1_p05_q20_r050',
    'testlba_F_h1_p05_q20_r100',
    'testlba_F_h1_p05_q50_r001',
    'testlba_F_h1_p05_q50_r002',
    'testlba_F_h1_p05_q50_r005',
    'testlba_F_h1_p05_q50_r010',
    'testlba_F_h1_p05_q50_r020',
    'testlba_F_h1_p05_q50_r050',
    'testlba_F_h1_p05_q50_r100',
    'testlba_F_h1_p05_q100_r001',
    'testlba_F_h1_p05_q100_r002',
    'testlba_F_h1_p05_q100_r005',
    'testlba_F_h1_p05_q100_r010',
    'testlba_F_h1_p05_q100_r020',
    'testlba_F_h1_p05_q100_r050',
    'testlba_F_h1_p05_q100_r100',
    'testlba_F_h1_p10_q10_r001',
    'testlba_F_h1_p10_q10_r002',
    'testlba_F_h1_p10_q10_r005',
    'testlba_F_h1_p10_q10_r010',
    'testlba_F_h1_p10_q10_r020',
    'testlba_F_h1_p10_q10_r050',
    'testlba_F_h1_p10_q10_r100',
    'testlba_F_h1_p10_q20_r001',
    'testlba_F_h1_p10_q20_r002',
    'testlba_F_h1_p10_q20_r005',
    'testlba_F_h1_p10_q20_r010',
    'testlba_F_h1_p10_q20_r020',
    'testlba_F_h1_p10_q20_r050',
    'testlba_F_h1_p10_q20_r100',
    'testlba_F_h1_p10_q50_r001',
    'testlba_F_h1_p10_q50_r002',
    'testlba_F_h1_p10_q50_r005',
    'testlba_F_h1_p10_q50_r010',
    'testlba_F_h1_p10_q50_r020',
    'testlba_F_h1_p10_q50_r050',
    'testlba_F_h1_p10_q50_r100',
    'testlba_F_h1_p10_q100_r001',
    'testlba_F_h1_p10_q100_r002',
    'testlba_F_h1_p10_q100_r005',
    'testlba_F_h1_p10_q100_r010',
    'testlba_F_h1_p10_q100_r020',
    'testlba_F_h1_p10_q100_r050',
    'testlba_F_h1_p10_q100_r100',
    'testlba_F_h1_p20_q10_r001',
    'testlba_F_h1_p20_q10_r002',
    'testlba_F_h1_p20_q10_r005',
    'testlba_F_h1_p20_q10_r010',
    'testlba_F_h1_p20_q10_r020',
    'testlba_F_h1_p20_q10_r050',
    'testlba_F_h1_p20_q10_r100',
    'testlba_F_h1_p20_q20_r001',
    'testlba_F_h1_p20_q20_r002',
    'testlba_F_h1_p20_q20_r005',
    'testlba_F_h1_p20_q20_r010',
    'testlba_F_h1_p20_q20_r020',
    'testlba_F_h1_p20_q20_r050',
    'testlba_F_h1_p20_q20_r100',
    'testlba_F_h1_p20_q50_r001',
    'testlba_F_h1_p20_q50_r002',
    'testlba_F_h1_p20_q50_r005',
    'testlba_F_h1_p20_q50_r010',
    'testlba_F_h1_p20_q50_r020',
    'testlba_F_h1_p20_q50_r050',
    'testlba_F_h1_p20_q50_r100',
    'testlba_F_h1_p20_q100_r001',
    'testlba_F_h1_p20_q100_r002',
    'testlba_F_h1_p20_q100_r005',
    'testlba_F_h1_p20_q100_r010',
    'testlba_F_h1_p20_q100_r020',
    'testlba_F_h1_p20_q100_r050',
    'testlba_F_h1_p20_q100_r100',
    'testlba_F_h1_p40_q10_r001',
    'testlba_F_h1_p40_q10_r002',
    'testlba_F_h1_p40_q10_r005',
    'testlba_F_h1_p40_q10_r010',
    'testlba_F_h1_p40_q10_r020',
    'testlba_F_h1_p40_q10_r050',
    'testlba_F_h1_p40_q10_r100',
    'testlba_F_h1_p40_q20_r001',
    'testlba_F_h1_p40_q20_r002',
    'testlba_F_h1_p40_q20_r005',
    'testlba_F_h1_p40_q20_r010',
    'testlba_F_h1_p40_q20_r020',
    'testlba_F_h1_p40_q20_r050',
    'testlba_F_h1_p40_q20_r100',
    'testlba_F_h1_p40_q50_r001',
    'testlba_F_h1_p40_q50_r002',
    'testlba_F_h1_p40_q50_r005',
    'testlba_F_h1_p40_q50_r010',
    'testlba_F_h1_p40_q50_r020',
    'testlba_F_h1_p40_q50_r050',
    'testlba_F_h1_p40_q50_r100',
    'testlba_F_h1_p40_q100_r001',
    'testlba_F_h1_p40_q100_r002',
    'testlba_F_h1_p40_q100_r005',
    'testlba_F_h1_p40_q100_r010',
    'testlba_F_h1_p40_q100_r020',
    'testlba_F_h1_p40_q100_r050',
    'testlba_F_h1_p40_q100_r100',
    'testlba_T_h0_p02_q10_r001',
    'testlba_T_h0_p02_q10_r002',
    'testlba_T_h0_p02_q10_r005',
    'testlba_T_h0_p02_q10_r010',
    'testlba_T_h0_p02_q10_r020',
    'testlba_T_h0_p02_q10_r050',
    'testlba_T_h0_p02_q10_r100',
    'testlba_T_h0_p02_q20_r001',
    'testlba_T_h0_p02_q20_r002',
    'testlba_T_h0_p02_q20_r005',
    'testlba_T_h0_p02_q20_r010',
    'testlba_T_h0_p02_q20_r020',
    'testlba_T_h0_p02_q20_r050',
    'testlba_T_h0_p02_q20_r100',
    'testlba_T_h0_p02_q50_r001',
    'testlba_T_h0_p02_q50_r002',
    'testlba_T_h0_p02_q50_r005',
    'testlba_T_h0_p02_q50_r010',
    'testlba_T_h0_p02_q50_r020',
    'testlba_T_h0_p02_q50_r050',
    'testlba_T_h0_p02_q50_r100',
    'testlba_T_h0_p02_q100_r001',
    'testlba_T_h0_p02_q100_r002',
    'testlba_T_h0_p02_q100_r005',
    'testlba_T_h0_p02_q100_r010',
    'testlba_T_h0_p02_q100_r020',
    'testlba_T_h0_p02_q100_r050',
    'testlba_T_h0_p02_q100_r100',
    'testlba_T_h0_p05_q10_r001',
    'testlba_T_h0_p05_q10_r002',
    'testlba_T_h0_p05_q10_r005',
    'testlba_T_h0_p05_q10_r010',
    'testlba_T_h0_p05_q10_r020',
    'testlba_T_h0_p05_q10_r050',
    'testlba_T_h0_p05_q10_r100',
    'testlba_T_h0_p05_q20_r001',
    'testlba_T_h0_p05_q20_r002',
    'testlba_T_h0_p05_q20_r005',
    'testlba_T_h0_p05_q20_r010',
    'testlba_T_h0_p05_q20_r020',
    'testlba_T_h0_p05_q20_r050',
    'testlba_T_h0_p05_q20_r100',
    'testlba_T_h0_p05_q50_r001',
    'testlba_T_h0_p05_q50_r002',
    'testlba_T_h0_p05_q50_r005',
    'testlba_T_h0_p05_q50_r010',
    'testlba_T_h0_p05_q50_r020',
    'testlba_T_h0_p05_q50_r050',
    'testlba_T_h0_p05_q50_r100',
    'testlba_T_h0_p05_q100_r001',
    'testlba_T_h0_p05_q100_r002',
    'testlba_T_h0_p05_q100_r005',
    'testlba_T_h0_p05_q100_r010',
    'testlba_T_h0_p05_q100_r020',
    'testlba_T_h0_p05_q100_r050',
    'testlba_T_h0_p05_q100_r100',
    'testlba_T_h0_p10_q10_r001',
    'testlba_T_h0_p10_q10_r002',
    'testlba_T_h0_p10_q10_r005',
    'testlba_T_h0_p10_q10_r010',
    'testlba_T_h0_p10_q10_r020',
    'testlba_T_h0_p10_q10_r050',
    'testlba_T_h0_p10_q10_r100',
    'testlba_T_h0_p10_q20_r001',
    'testlba_T_h0_p10_q20_r002',
    'testlba_T_h0_p10_q20_r005',
    'testlba_T_h0_p10_q20_r010',
    'testlba_T_h0_p10_q20_r020',
    'testlba_T_h0_p10_q20_r050',
    'testlba_T_h0_p10_q20_r100',
    'testlba_T_h0_p10_q50_r001',
    'testlba_T_h0_p10_q50_r002',
    'testlba_T_h0_p10_q50_r005',
    'testlba_T_h0_p10_q50_r010',
    'testlba_T_h0_p10_q50_r020',
    'testlba_T_h0_p10_q50_r050',
    'testlba_T_h0_p10_q50_r100',
    'testlba_T_h0_p10_q100_r001',
    'testlba_T_h0_p10_q100_r002',
    'testlba_T_h0_p10_q100_r005',
    'testlba_T_h0_p10_q100_r010',
    'testlba_T_h0_p10_q100_r020',
    'testlba_T_h0_p10_q100_r050',
    'testlba_T_h0_p10_q100_r100',
    'testlba_T_h0_p20_q10_r001',
    'testlba_T_h0_p20_q10_r002',
    'testlba_T_h0_p20_q10_r005',
    'testlba_T_h0_p20_q10_r010',
    'testlba_T_h0_p20_q10_r020',
    'testlba_T_h0_p20_q10_r050',
    'testlba_T_h0_p20_q10_r100',
    'testlba_T_h0_p20_q20_r001',
    'testlba_T_h0_p20_q20_r002',
    'testlba_T_h0_p20_q20_r005',
    'testlba_T_h0_p20_q20_r010',
    'testlba_T_h0_p20_q20_r020',
    'testlba_T_h0_p20_q20_r050',
    'testlba_T_h0_p20_q20_r100',
    'testlba_T_h0_p20_q50_r001',
    'testlba_T_h0_p20_q50_r002',
    'testlba_T_h0_p20_q50_r005',
    'testlba_T_h0_p20_q50_r010',
    'testlba_T_h0_p20_q50_r020',
    'testlba_T_h0_p20_q50_r050',
    'testlba_T_h0_p20_q50_r100',
    'testlba_T_h0_p20_q100_r001',
    'testlba_T_h0_p20_q100_r002',
    'testlba_T_h0_p20_q100_r005',
    'testlba_T_h0_p20_q100_r010',
    'testlba_T_h0_p20_q100_r020',
    'testlba_T_h0_p20_q100_r050',
    'testlba_T_h0_p20_q100_r100',
    'testlba_T_h0_p40_q10_r001',
    'testlba_T_h0_p40_q10_r002',
    'testlba_T_h0_p40_q10_r005',
    'testlba_T_h0_p40_q10_r010',
    'testlba_T_h0_p40_q10_r020',
    'testlba_T_h0_p40_q10_r050',
    'testlba_T_h0_p40_q10_r100',
    'testlba_T_h0_p40_q20_r001',
    'testlba_T_h0_p40_q20_r002',
    'testlba_T_h0_p40_q20_r005',
    'testlba_T_h0_p40_q20_r010',
    'testlba_T_h0_p40_q20_r020',
    'testlba_T_h0_p40_q20_r050',
    'testlba_T_h0_p40_q20_r100',
    'testlba_T_h0_p40_q50_r001',
    'testlba_T_h0_p40_q50_r002',
    'testlba_T_h0_p40_q50_r005',
    'testlba_T_h0_p40_q50_r010',
    'testlba_T_h0_p40_q50_r020',
    'testlba_T_h0_p40_q50_r050',
    'testlba_T_h0_p40_q50_r100',
    'testlba_T_h0_p40_q100_r001',
    'testlba_T_h0_p40_q100_r002',
    'testlba_T_h0_p40_q100_r005',
    'testlba_T_h0_p40_q100_r010',
    'testlba_T_h0_p40_q100_r020',
    'testlba_T_h0_p40_q100_r050',
    'testlba_T_h0_p40_q100_r100',
    'testlba_T_h1_p02_q10_r001',
    'testlba_T_h1_p02_q10_r002',
    'testlba_T_h1_p02_q10_r005',
    'testlba_T_h1_p02_q10_r010',
    'testlba_T_h1_p02_q10_r020',
    'testlba_T_h1_p02_q10_r050',
    'testlba_T_h1_p02_q10_r100',
    'testlba_T_h1_p02_q20_r001',
    'testlba_T_h1_p02_q20_r002',
    'testlba_T_h1_p02_q20_r005',
    'testlba_T_h1_p02_q20_r010',
    'testlba_T_h1_p02_q20_r020',
    'testlba_T_h1_p02_q20_r050',
    'testlba_T_h1_p02_q20_r100',
    'testlba_T_h1_p02_q50_r001',
    'testlba_T_h1_p02_q50_r002',
    'testlba_T_h1_p02_q50_r005',
    'testlba_T_h1_p02_q50_r010',
    'testlba_T_h1_p02_q50_r020',
    'testlba_T_h1_p02_q50_r050',
    'testlba_T_h1_p02_q50_r100',
    'testlba_T_h1_p02_q100_r001',
    'testlba_T_h1_p02_q100_r002',
    'testlba_T_h1_p02_q100_r005',
    'testlba_T_h1_p02_q100_r010',
    'testlba_T_h1_p02_q100_r020',
    'testlba_T_h1_p02_q100_r050',
    'testlba_T_h1_p02_q100_r100',
    'testlba_T_h1_p05_q10_r001',
    'testlba_T_h1_p05_q10_r002',
    'testlba_T_h1_p05_q10_r005',
    'testlba_T_h1_p05_q10_r010',
    'testlba_T_h1_p05_q10_r020',
    'testlba_T_h1_p05_q10_r050',
    'testlba_T_h1_p05_q10_r100',
    'testlba_T_h1_p05_q20_r001',
    'testlba_T_h1_p05_q20_r002',
    'testlba_T_h1_p05_q20_r005',
    'testlba_T_h1_p05_q20_r010',
    'testlba_T_h1_p05_q20_r020',
    'testlba_T_h1_p05_q20_r050',
    'testlba_T_h1_p05_q20_r100',
    'testlba_T_h1_p05_q50_r001',
    'testlba_T_h1_p05_q50_r002',
    'testlba_T_h1_p05_q50_r005',
    'testlba_T_h1_p05_q50_r010',
    'testlba_T_h1_p05_q50_r020',
    'testlba_T_h1_p05_q50_r050',
    'testlba_T_h1_p05_q50_r100',
    'testlba_T_h1_p05_q100_r001',
    'testlba_T_h1_p05_q100_r002',
    'testlba_T_h1_p05_q100_r005',
    'testlba_T_h1_p05_q100_r010',
    'testlba_T_h1_p05_q100_r020',
    'testlba_T_h1_p05_q100_r050',
    'testlba_T_h1_p05_q100_r100',
    'testlba_T_h1_p10_q10_r001',
    'testlba_T_h1_p10_q10_r002',
    'testlba_T_h1_p10_q10_r005',
    'testlba_T_h1_p10_q10_r010',
    'testlba_T_h1_p10_q10_r020',
    'testlba_T_h1_p10_q10_r050',
    'testlba_T_h1_p10_q10_r100',
    'testlba_T_h1_p10_q20_r001',
    'testlba_T_h1_p10_q20_r002',
    'testlba_T_h1_p10_q20_r005',
    'testlba_T_h1_p10_q20_r010',
    'testlba_T_h1_p10_q20_r020',
    'testlba_T_h1_p10_q20_r050',
    'testlba_T_h1_p10_q20_r100',
    'testlba_T_h1_p10_q50_r001',
    'testlba_T_h1_p10_q50_r002',
    'testlba_T_h1_p10_q50_r005',
    'testlba_T_h1_p10_q50_r010',
    'testlba_T_h1_p10_q50_r020',
    'testlba_T_h1_p10_q50_r050',
    'testlba_T_h1_p10_q50_r100',
    'testlba_T_h1_p10_q100_r001',
    'testlba_T_h1_p10_q100_r002',
    'testlba_T_h1_p10_q100_r005',
    'testlba_T_h1_p10_q100_r010',
    'testlba_T_h1_p10_q100_r020',
    'testlba_T_h1_p10_q100_r050',
    'testlba_T_h1_p10_q100_r100',
    'testlba_T_h1_p20_q10_r001',
    'testlba_T_h1_p20_q10_r002',
    'testlba_T_h1_p20_q10_r005',
    'testlba_T_h1_p20_q10_r010',
    'testlba_T_h1_p20_q10_r020',
    'testlba_T_h1_p20_q10_r050',
    'testlba_T_h1_p20_q10_r100',
    'testlba_T_h1_p20_q20_r001',
    'testlba_T_h1_p20_q20_r002',
    'testlba_T_h1_p20_q20_r005',
    'testlba_T_h1_p20_q20_r010',
    'testlba_T_h1_p20_q20_r020',
    'testlba_T_h1_p20_q20_r050',
    'testlba_T_h1_p20_q20_r100',
    'testlba_T_h1_p20_q50_r001',
    'testlba_T_h1_p20_q50_r002',
    'testlba_T_h1_p20_q50_r005',
    'testlba_T_h1_p20_q50_r010',
    'testlba_T_h1_p20_q50_r020',
    'testlba_T_h1_p20_q50_r050',
    'testlba_T_h1_p20_q50_r100',
    'testlba_T_h1_p20_q100_r001',
    'testlba_T_h1_p20_q100_r002',
    'testlba_T_h1_p20_q100_r005',
    'testlba_T_h1_p20_q100_r010',
    'testlba_T_h1_p20_q100_r020',
    'testlba_T_h1_p20_q100_r050',
    'testlba_T_h1_p20_q100_r100',
    'testlba_T_h1_p40_q10_r001',
    'testlba_T_h1_p40_q10_r002',
    'testlba_T_h1_p40_q10_r005',
    'testlba_T_h1_p40_q10_r010',
    'testlba_T_h1_p40_q10_r020',
    'testlba_T_h1_p40_q10_r050',
    'testlba_T_h1_p40_q10_r100',
    'testlba_T_h1_p40_q20_r001',
    'testlba_T_h1_p40_q20_r002',
    'testlba_T_h1_p40_q20_r005',
    'testlba_T_h1_p40_q20_r010',
    'testlba_T_h1_p40_q20_r020',
    'testlba_T_h1_p40_q20_r050',
    'testlba_T_h1_p40_q20_r100',
    'testlba_T_h1_p40_q50_r001',
    'testlba_T_h1_p40_q50_r002',
    'testlba_T_h1_p40_q50_r005',
    'testlba_T_h1_p40_q50_r010',
    'testlba_T_h1_p40_q50_r020',
    'testlba_T_h1_p40_q50_r050',
    'testlba_T_h1_p40_q50_r100',
    'testlba_T_h1_p40_q100_r001',
    'testlba_T_h1_p40_q100_r002',
    'testlba_T_h1_p40_q100_r005',
    'testlba_T_h1_p40_q100_r010',
    'testlba_T_h1_p40_q100_r020',
    'testlba_T_h1_p40_q100_r050',
    'testlba_T_h1_p40_q100_r100',
]

testlba_F_h0_p02_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p02_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p05_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p10_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p20_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h0_p40_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p02_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p05_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p10_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p20_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_F_h1_p40_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=False
)

testlba_T_h0_p02_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p02_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p05_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p10_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p20_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h0_p40_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=0.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.20000000, 0.20000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(0.40000000, 0.40000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p02_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(0.50000000, 0.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(2.50000000, 2.50000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p05_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(1.00000000, 1.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(5.00000000, 5.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p10_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(2.00000000, 2.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(10.00000000, 10.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p20_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00100000, 0.00100001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q10_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.10000000, 0.10000001),
    long_branch_range=(4.00000000, 4.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00200000, 0.00200001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.00400000, 0.00400001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.04000000, 0.04000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q20_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.20000000, 0.20000001),
    long_branch_range=(8.00000000, 8.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.00500000, 0.00500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.02500000, 0.02500001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.25000000, 0.25000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q50_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(0.50000000, 0.50000001),
    long_branch_range=(20.00000000, 20.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r001 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.01000000, 0.01000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r002 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.02000000, 0.02000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r005 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.05000000, 0.05000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r010 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.10000000, 0.10000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r020 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.20000000, 0.20000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r050 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(0.50000000, 0.50000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

testlba_T_h1_p40_q100_r100 = tree.LBAQuartetTreeSimulator(
    short_branch_range=(1.00000000, 1.00000001),
    long_branch_range=(40.00000000, 40.00000001),
    internal_branch_range=(1.00000000, 1.00000001),
    sequence_simulator=sequence.HeterogeneousProteinSequenceSimulator(
        site_count_range=(2000, 2001),
        substitution_model='wag',
        alpha_range=(1, 1.00000001),
        profile='all.freq',
        profile_resampler=('dirichlet', 10),
        heterogeneous_branch_ratio=1.0,
        rate_swap_ratio=1.0,
        profile_swap_model=scipy.stats.randint(0, 1),
    ),
    is_farris=True
)

