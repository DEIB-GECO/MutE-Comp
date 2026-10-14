## Machine Learning Strategies for Multi-omics Investigation of RAS-Associated Mutations in Colorectal Cancer

This project develops a computational pipeline that leverages machine learning techniques to identify key genomic mutations in RAS-mutated colorectal cancer patients. The pipeline systematically compares diverse feature-encoding strategies by integrating gene-level mutational events, hotspot information, and gene-level transcriptomic data. Various tools for driver gene identification are employed to perform robust feature selection, and feature importance analysis ultimately highlighted the most predictive mutations driving tumorigenesis.

## Structure

- [01 - data preparation](01%20-%20data%20preparation): Contains the code to clean and merging the datasets and to separate RAS-mutated and non RAS-mutated samples.

- [02 - hypo and hyper mutated samples](02%20-%20hypo%20and%20hyper%20mutated%20samples): Contains the code to identify hyper mutated and hypo muated samples.

- [03 - execute tools for feature selections](03%20-%20execute%20tools%20for%20feature%20selections): Contains the code necessary to run all the driver genes identification tools employed for feature selection: input preparation, script to call the tools, and output analysis.

- [04 - hotspot identification](04%20-%20hotspot%20identification): Contains the code necessary to run all the mutational hotspots identification tools employed for feature construction: input preparation, script to call the tools, and output analysis.

- [05 - machine learning](05%20-%20machine%20learning): Contains the code to perform machine learning related tasks: input matrix preparations, models training and testing.

- [06 - feature importance analysis](06%20-%20feature%20importance%20analysis): Contains the notebooks in which feature importance analysis is performed on the best models.

Code parameters and file paths are listed and can be changed in the file [data.ini](data.ini), it can be read from Python with a `ConfigParser` object with `ExtendedInterpolation` and from shell with `source`. [read_ini.m](read_ini.m) and [read_ini.r](read_ini.r) contains function to read it in Matlab and R respectively.
