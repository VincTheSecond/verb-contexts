#!/usr/bin/env python
# coding=utf-8
#
# Author: (c) 2018 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import re
import logging
import argparse
import numpy as np

from scipy.spatial.distance import cosine

# Logging.
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.INFO)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Calculate word similarities for given CELEX word pairs.'
parser.add_argument('--celex', required=True, help='celex dictionary')
parser.add_argument('--vectors', required=True, help='a file with word vectors')
parser.add_argument('--report', required=True, help='JSON filename where similarities will be reported')
args = parser.parse_args()

# Load vocabulary.
logging.info('Loading word vectors (%s)...', args.vectors)
vectors = dict()
with open(args.vectors, 'r') as fvectors:
    for (n_line, line) in enumerate(fvectors):
        # Skip first line
        if n_line == 0:
            continue

        if (n_line % 1000) == 0:
            logging.debug('Loaded %d vectors', n_line)

        # Parse other lines.
        fields = line.rstrip().split(' ')
        vectors[fields[0]] = np.array([float(value) for value in fields[1:]])

# Load evaluation data.
results = []
total_pairs = 0
unknown_words = {}
unknown_pairs = {}
with open(args.celex, 'r') as fdataset:
    for (n_line, line) in enumerate(fdataset):
        if n_line == 0:
            continue

        try:
            word1, pos1, word2, pos2 = re.split('\s+', line.rstrip())
        except ValueError as exception:
            continue

        if word1 not in vectors:
            unknown_words[word1] = 1
            unknown_pairs['%s + %s' % (word1, word2)] = 1

        if word2 not in vectors:
            unknown_words[word2] = 1
            unknown_pairs['%s + %s' % (word1, word2)] = 1

        if word1 in unknown_words or word2 in unknown_words:
            # results.append({'word1': word1, 'pos1': pos1, 'word2': word2, 'pos2': pos2, 'similarity': 0.0})
            continue

        similarity = cosine(vectors[word1], vectors[word2])
        results.append({'word1': word1, 'pos1': pos1, 'word2': word2, 'pos2': pos2, 'similarity': similarity})

logging.info('Total word pairs        : %d', len(results))
logging.info('Number of unknown pairs : %d', len(unknown_pairs))
with open(args.report, 'w') as fresults:
    for result in results:
        fresults.write('{};{};{};{};{}\n'.format(result['word1'], result['pos1'], result['word2'], result['pos2'], result['similarity']))
