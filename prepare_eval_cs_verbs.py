#!/usr/bin/env python
#
# Author: (c) 2016 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import sys
import logging
import argparse
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats.stats import spearmanr

# Logging.
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Split translated SimLex-999 to a cross-validation according to given template.'
parser.add_argument('--template', required=True, help='a file with fold template')
parser.add_argument('--original', required=True, help='an original SimLex-999 file')
parser.add_argument('--final', required=True, help='a file with final output')
args = parser.parse_args()

# Load vocabulary.
logging.info('Loading template...')
template = []
with open(args.template, 'r') as ftemplate:
    for line in ftemplate:
        fields = line.rstrip().split(',')
        template.append('%s,%s' % (fields[0], fields[1]))

logging.info('Loading original...')
original = []
with open(args.original, 'r') as foriginal:
    for line in foriginal:
        original.append(line.rstrip())

# Process the final output
logging.info('Creating %s...', args.final)
with open(args.final, 'w') as ffinal:
    for pair_to_add in template:
        for original_data in original:
            fields = original_data.rstrip().split('\t')
            similarity = fields[3].replace(',', '.')
            if '%s,%s' % (fields[0], fields[1]) == pair_to_add:
                try:
                    ffinal.write('%s,%s,%s\n' % (fields[10], fields[11], similarity))
                except:
                    logging.error('A problem occurred for pair %s', pair_to_add)
