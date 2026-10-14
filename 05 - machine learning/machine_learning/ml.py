#!/usr/bin/env python3

import argparse
import configparser
import json
import os
import sys



dir = os.path.dirname(os.path.abspath(__file__))
if dir not in sys.path:
    sys.path.append(dir)
os.chdir(dir + '/../') # TODO: do not do this, but use correct path when opening files

from run_models import run_models


# Read .ini parameters
data = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
data.read('../data.ini')
data = data['DEFAULT']

# Load possible feature selections
with open('../' + data['ml'] + 'tools_features_selection.json', 'r') as file:
    features_selections = json.load(file)


def ml(features=None, inputs=None, transcriptomics_non_filtered=False, optimize='accuracy'):

    if features == None:
        features = [f'"{feature}"' for feature in features_selections.keys()]
    
    if inputs == None:
        inputs = [d for d in os.listdir(f"../{data['ml___input']}") if os.path.isdir(os.path.join(f"../{data['ml___input']}", d))]
    
    # Train models
    run_models(data, features_selections, features, inputs, transcriptomics_non_filtered, optimize)


if __name__ == '__main__':

    # Handle user parameters
    parser = argparse.ArgumentParser(
            description="Run ML models with different combinations of tool feature sets.",
            formatter_class=argparse.RawTextHelpFormatter
        )

    parser.add_argument(
        '-f',
        '--features',
        type = str,
        nargs='*',
        help = (
            f"List of which features (amonge the ones in {data['ml']}tools_features_selection.json) use to train the models.\n"
            "It is possible to combine them with:\n"
            "        +: union;\n"
            "        *: .\n"
            "E.g. -f '\"tool1\" + \"tool2\"' * \"tool3\"' '\"tool1\" * \"tool2\"' \"tool4\"\n"
            "will run the ML models with three sets of features:\n"
            " - the union of the features of tool1 and tool2 intersected with the features of tool3;\n"
            " - the intersection of the features of tool1 and tool2;\n"
            " - the features of tool4.\n"
            "If no features are selected, all single-tool features will be used."
        ),
        default = None
    )

    parser.add_argument(
        '-i',
        '--inputs',
        type = str,
        nargs='*',
        help = f"List of which folders in the input directory ({data['ml___input']}) use to train the models.",
        default = None
    )

    parser.add_argument(
        '-t',
        '--transcriptomics-non-filtered',
        action='store_true',
        help = "Do not apply the feature selection to the transcriptomics data, but mantains all the transcriptomic features.",
        default = False
    )

    parser.add_argument(
        '-o',
        '--optimize',
        type = str,
        nargs = '?',
        help = 'Optimize training on accuracy or mcc.',
        default = 'accuracy'
    )

    args = parser.parse_args()

    # call main function
    ml(args.features, args.inputs, args.transcriptomics_non_filtered, args.optimize)
