#!/usr/bin/env python
#
# Author: (c) 2016 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import sys
import logging
import argparse

from collections import Counter

# Logging.
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Prune training data by the given vocabulary.'
parser.add_argument('--vocabulary', required=True, help='a vocabulary destination')
parser.add_argument('--threshold', required=True, help='a word frequency threshold')
parser.add_argument('--output', required=True, help='a path where final treining data will be stored')
args = parser.parse_args()

# Load vocabulary.
logging.info('Loading vocabulary...')
vocabulary = dict()
with open(args.vocabulary, 'r') as fvocab:
    for line in fvocab:
        word, frequency = line.rstrip().split('\t')
        vocabulary[word] = frequency
logging.info('Vocabulary size: %d', len(vocabulary))

# Grep training data.
with open(args.output, 'w') as fout:
    for (n_line, line) in enumerate(sys.stdin):
        if (n_line % 1000000) == 0:
            logging.info('Processed %d lines.', n_line)

        target_word, context = line.rstrip().split(' ')
        if target_word not in vocabulary:
            continue

        if vocabulary[target_word] < args.threshold:
            continue

        try:
            context_word, context_deprel = context.split('_')
        except ValueError as exception:
            # logging.error('Invalid line %d: %s', n_line, line.rstrip())
            continue

        if context_word not in vocabulary:
            continue

        if vocabulary[context_word] < args.threshold:
            continue

        fout.write('%s' % line)
