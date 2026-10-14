from tqdm.auto import tqdm


def pivotMutations(mutations, clusters, includeVariants):
    mutations.loc[:, 'feature'] = None
    if clusters is None:
        if not includeVariants:
            mutations.loc[:, 'feature'] = mutations['name']
        else:
            mutations.loc[:, 'feature'] = mutations['name'] + '_[' + mutations['var'] + ']'
    else:
            for _, row in tqdm(clusters.sort_values(by='P', ascending=True).iterrows(), total=len(clusters)):
                mask = (mutations['merge'] == row['merge']) & \
                        (mutations['start'] >= row['start']) & \
                        (mutations['end'] <= row['end'])
                if not includeVariants:
                    mutations.loc[mask, 'feature'] = (
                        mutations.loc[mask, 'name'] + 
                        f'_{row["start"]}_{row["end"]}'
                    )
                else:
                    mutations.loc[mask, 'feature'] = (
                        mutations.loc[mask, 'name'] + 
                        '_[' + mutations.loc[mask, 'var'] + ']' +
                        f'_{row["start"]}_{row["end"]}'
                    )

            if not includeVariants:
                mutations.loc[mutations['feature'].isnull(), 'feature'] = (
                    mutations['name'] + '_noCluster'
                )
            else:
                mutations.loc[mutations['feature'].isnull(), 'feature'] = (
                    mutations['name'] + '_[' + mutations['var'] + ']_noCluster'
                )
    pivot = mutations.pivot_table(index='Sample', columns='feature', aggfunc='size', fill_value=0)
    return pivot
