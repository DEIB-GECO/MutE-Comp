## Comparative Analysis of Interpretable Feature Selection and Encoding Strategies for Mutational Data and Multi-Omics Integration in Predictive Tasks

This project develops the computational pipeline of a comparative analytical framework that combines multiple driver gene and hotspot detection methods to derive different encoding options (selection strategies, selection schemes, resolution levels) and obtain many feature spaces from mutational data. Across them, machine learning classifiers are assessed to find overall the most promising feature spaces. Transcriptomic data are also integrated to study mutational contribution also in multi-omics settings. Lastly, feature importance analyses of the best feature spaces and classification models is used to identify and prioritize candidate gene targets for actionability search.
In our application use case the analytical framework aims to identify key genomic mutations in RAS-mutated colorectal cancer patients.

## Structure

- [01 - data preparation](01%20-%20data%20preparation): Contains the code to clean and merging the datasets and to separate the classes of interest to prepare the selection schemes (here, RAS-mutated versus non RAS-mutated samples).

- [02 - hypo and hyper mutated samples](02%20-%20hypo%20and%20hyper%20mutated%20samples): Contains the code to identify hyper mutated and hypo muated samples.

- [03 - execute tools for feature selections](03%20-%20execute%20tools%20for%20feature%20selections): Contains the code necessary to run all the driver genes identification methods employed for feature selection: input preparation, script to call the methods, and output analysis.

- [04 - hotspot identification](04%20-%20hotspot%20identification): Contains the code necessary to run all the mutational hotspots identification methods employed for feature encoding at different resolution levels: input preparation, script to call the tools, and output analysis.

- [05 - machine learning](05%20-%20machine%20learning): Contains the code to perform the machine learning-desired task and comparative evaluation: input matrix preparations, models training and testing.

- [06 - feature importance analysis](06%20-%20feature%20importance%20analysis): Contains the notebooks in which feature importance analysis is performed on the best feature spaces and models.

Code parameters and file paths are listed and can be changed in the file [data.ini](data.ini), it can be read from Python with a `ConfigParser` object with `ExtendedInterpolation` and from shell with `source`. [read_ini.m](read_ini.m) and [read_ini.r](read_ini.r) contains function to read it in Matlab and R respectively.
