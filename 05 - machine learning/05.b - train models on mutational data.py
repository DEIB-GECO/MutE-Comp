#!/usr/bin/env python3

from machine_learning.ml import ml

# ---------------------------------------------------------------------------
# merged dataset - mutations - optimized for accuracy
ml(
    None,
    [
        'merged_mut',
        'merged_mut_["mutclust - ALL"]',
        'merged_mut_["oncodriveclust_deafultParams - ALL"]',
        'merged_mut_["oncodriveclust_coadreadParams - ALL"]',
        'merged_mut_["onlyMutclust - ALL"]',
        'merged_mut_["onlyOncodriveclust_deafultParams - ALL"]',
        'merged_mut_["onlyOncodriveclust_coadreadParams - ALL"]',
    ],
    optimize='accuracy'
)

# ---------------------------------------------------------------------------
# merged dataset - mutations - optimized for MCC
ml(
    None,
    [
        'merged_mut',
        'merged_mut_["mutclust - ALL"]',
        'merged_mut_["oncodriveclust_deafultParams - ALL"]',
        'merged_mut_["oncodriveclust_coadreadParams - ALL"]',
        'merged_mut_["onlyMutclust - ALL"]',
        'merged_mut_["onlyOncodriveclust_deafultParams - ALL"]',
        'merged_mut_["onlyOncodriveclust_coadreadParams - ALL"]',
    ],
    optimize='mcc'
)
