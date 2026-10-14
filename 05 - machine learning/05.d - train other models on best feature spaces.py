#!/usr/bin/env python3

from machine_learning.ml import ml

# best feature spaces
features = [
    '"maxmif HN - onlyRAS_onlyNonRAS"',
    '"maxmif HN S - onlyRAS_onlyNonRAS"'
]

# ---------------------------------------------------------------------------
# tcga dataset - filtered transcriptmics

print('tcga dataset - filtered transcriptmics')

ml(
    features,
    [
        'TCGA_tran',
    ],
    optimize='accuracy'
)

# ---------------------------------------------------------------------------
# tcga dataset - filtered transcriptmics and mutations

print('tcga dataset - filtered transcriptmics and mutations')

ml(
    features,
    [
        'TCGA_tran&mut_["mutclust - ALL"]',
        'TCGA_tran&mut_["oncodriveclust_coadreadParams - ALL"]',
    ],
    optimize='accuracy'
)

# ---------------------------------------------------------------------------
# tcga dataset - non filtered transcriptmics

print('tcga dataset - non filtered transcriptmics')

ml(
    features,
    [
        'TCGA_tran',
    ],
    optimize='accuracy',
    transcriptomics_non_filtered=True
)

# ---------------------------------------------------------------------------
# tcga dataset - non filtered transcriptmics and mutations

print('tcga dataset - non filtered transcriptmics and mutations')

ml(
    features,
    [
        'TCGA_tran&mut_["mutclust - ALL"]',
        'TCGA_tran&mut_["oncodriveclust_coadreadParams - ALL"]',
    ],
    optimize='accuracy',
    transcriptomics_non_filtered=True
)

# ---------------------------------------------------------------------------
# others

print('others')

ml(
    features,
    [
        # merged dataset - mutations with variants
        'merged_mutVar_["mutclust - ALL"]',
        'merged_mutVar_["oncodriveclust_coadreadParams - ALL"]',

        # tcga dataset - mutations
        'TCGA_mut_["mutclust - ALL"]',
        'TCGA_mut_["oncodriveclust_coadreadParams - ALL"]',

        # tcga dataset - mutations with variants
        'TCGA_mutVar_["mutclust - ALL"]',
        'TCGA_mutVar_["oncodriveclust_coadreadParams - ALL"]',

        # tcga dataset - filtered transcriptmics and mutations with variants
        'TCGA_tran&mutVar_["mutclust - ALL"]',
        'TCGA_tran&mutVar_["oncodriveclust_coadreadParams - ALL"]',
    ],
    optimize='accuracy'
)
