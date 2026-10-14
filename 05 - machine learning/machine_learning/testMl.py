#!/usr/bin/env python3

import argparse
import configparser
import os
import sys



dir = os.path.dirname(os.path.abspath(__file__))
if dir not in sys.path:
    sys.path.append(dir)
os.chdir(dir + '/../') # TODO: do not do this, but use correct path when opening files

from run_tests import run_tests


# Read .ini parameters
data = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
data.read('../data.ini')
data = data['DEFAULT']

def testMl(models=None, optimized_by='accuracy', out='ml_results.csv'):

    if models == None:
        models = [d for d in os.listdir(f"../{data['ml___models']}optimized_{optimized_by}/") if os.path.isdir(os.path.join(f"../{data['ml___models']}optimized_{optimized_by}/", d))]
    
    # Evaluate models on test set
    run_tests(data, models, optimized_by, out)


if __name__ == '__main__':

    # Handle user parameters
    parser = argparse.ArgumentParser(
            description="Evaluate models on test sets.",
            formatter_class=argparse.RawTextHelpFormatter
        )
    
    parser.add_argument(
        '-m',
        '--models',
        type = str,
        nargs='*',
        help = f"List of which folders in the models directory ({data['ml___models']}) contains the models to evaluate.",
        default = None
    )

    parser.add_argument(
        '-b',
        '--optimized-by',
        type = str,
        nargs = '?',
        help = 'test the models optimized on accuracy or on mcc.',
        default = 'accuracy'
    )

    parser.add_argument(
        '-o',
        '--out',
        type = str,
        nargs = '?',
        help = 'Out file name',
        default = 'ml_results.csv'
    )

    args = parser.parse_args()

    # call main function
    testMl(args.models, args.optimized_by, args.out)
