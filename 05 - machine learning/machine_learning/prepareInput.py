            # if isinstance(clusters_coordinates, str):
            #     if coordinates_sep is None:
            #         raise ValueError('coordinates_sep must be provided if only one column is provided for clusters_coordinates')
            #     clusters[['start', 'end']] = clusters[clusters_coordinates].str.split(coordinates_sep, expand=True).astype(int)
            # else:
            #     clusters = clusters.rename(columns={clusters_coordinates[0]: 'start', clusters_coordinates[1]: 'end'})


import os
import sys
from typing import Optional

import pandas as pd



dir = os.path.dirname(os.path.abspath(__file__))
if dir not in sys.path:
    sys.path.append(dir)

from pivotMutations import pivotMutations


def prepareInput(sample_pos: list[str],
                 sample_neg: list[str],
                 sample_train: list[str] = None,
                 sample_test: list[str] = None,
                 trainPercentage: float = 0.7,
                 mutations: Optional[pd.DataFrame] = None,
                 includeVariants: bool = False,
                 clusters: Optional[pd.DataFrame] = None,
                 clusters_threshold: float = 1,
                 onlyClusters: bool = False,
                 transcriptomics: Optional[pd.DataFrame] = None,
                 seed: int = 0) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    if (sample_train is None) + (sample_test is None) == 1:
        raise ValueError('sample_train and sample_test must be provided together')

    if mutations is None and transcriptomics is None:
        raise ValueError('At least one of mutations, transcriptomics must be provided')

    if mutations is not None:
        if clusters is not None:
            clusters = clusters[clusters['P'] < clusters_threshold]
        pivot_mut = pivotMutations(mutations, clusters, includeVariants)
        if onlyClusters:
            pivot_mut = pivot_mut.loc[:, ~pivot_mut.columns.str.contains('noCluster')]
    else:
        if clusters is not None:
            raise ValueError('mutations must be provided if clusters is provided')

    if transcriptomics is not None:
        transcriptomics = transcriptomics.reset_index()
        transcriptomics.columns = [x + '_tran' if x != 'Sample' else x for x in transcriptomics.columns]
    
    if mutations is not None and transcriptomics is None:
        matrix = pivot_mut

        matrix_pos = matrix.loc[[s for s in sample_pos if s in matrix.index]]
        matrix_neg = matrix.loc[[s for s in sample_neg if s in matrix.index]]

        if sample_train is not None and sample_test is not None:
            train_pos = matrix_pos.loc[[s for s in sample_train if s in matrix_pos.index]]
            test_pos = matrix_pos.loc[[s for s in sample_test if s in matrix_pos.index]]
            train_neg = matrix_neg.loc[[s for s in sample_train if s in matrix_neg.index]]
            test_neg = matrix_neg.loc[[s for s in sample_test if s in matrix_neg.index]]
        else:
            train_pos = matrix_pos.sample(frac=trainPercentage, random_state=seed)
            test_pos = matrix_pos.drop(train_pos.index)
            train_neg = matrix_neg.sample(frac=trainPercentage, random_state=seed)
            test_neg = matrix_neg.drop(train_neg.index)

        return train_pos, train_neg, test_pos, test_neg
    
    # TODO: HO MANTENUTO LA PARTE SUCCESSIVA FILTRATA CON isin() INVECE CHE CON L'INDEX PERCHÉ AVEVO FATTO COSÌ PRIMA E CAMBIANDOLA CAMBIA L'ORDINE DELLE RIGHE

    if mutations is None and transcriptomics is not None:
        matrix = transcriptomics

    if mutations is not None and transcriptomics is not None:
        matrix = pd.merge(transcriptomics, pivot_mut, how='inner', left_on='Sample', right_on='Sample')

    matrix_pos = matrix[matrix['Sample'].isin(sample_pos)]
    matrix_neg = matrix[matrix['Sample'].isin(sample_neg)]

    if sample_train is not None and sample_test is not None:
        train_pos = matrix_pos[matrix_pos['Sample'].isin(sample_train)].set_index('Sample')
        test_pos = matrix_pos[matrix_pos['Sample'].isin(sample_test)].set_index('Sample')
        train_neg = matrix_neg[matrix_neg['Sample'].isin(sample_train)].set_index('Sample')
        test_neg = matrix_neg[matrix_neg['Sample'].isin(sample_test)].set_index('Sample')
    else:
        train_pos = matrix_pos.sample(frac=trainPercentage, random_state=seed).set_index('Sample')
        test_pos = matrix_pos.drop(train_pos.index).set_index('Sample')
        train_neg = matrix_neg.sample(frac=trainPercentage, random_state=seed).set_index('Sample')
        test_neg = matrix_neg.drop(train_neg.index).set_index('Sample')
    
    return train_pos, train_neg, test_pos, test_neg
