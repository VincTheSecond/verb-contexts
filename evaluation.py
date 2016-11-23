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


# Methods.
def parse_simlex(fields):
    """
    FIXME

    :param fields:
    :return:

    """
    word1 = fields[0]
    word2 = fields[1]
    similarity = float(fields[3])

    return word1, word2, similarity

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Evaluate word vectors over a given similarity dataset.'
parser.add_argument('--vectors', required=True, help='a file with word vectors')
parser.add_argument('--dataset', required=True, help='dataset to evaluate')
args = parser.parse_args()

# Load vocabulary.
logging.info('Loading word vectors...')
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
true_similarities = []
test_similarities = []
logging.info('Evaluating dataset...')
with open(args.dataset, 'r') as fdataset:
    for (n_line, line) in enumerate(fdataset):
        if n_line == 0:
            continue

        fields = line.rstrip().split('\t')

        # Simlex.
        word1, word2, true_similarity = parse_simlex(fields)
        true_similarities.append(true_similarity)

        test_similarity = 0.0
        if word1 in vectors and word2 in vectors:
            test_similarity = cosine_similarity(vectors[word1], vectors[word2])
        test_similarities.append(test_similarity)

        logging.debug('%10s | %10s | %.4f | %.4f', word1, word2, true_similarity, test_similarity)

logging.info('Spearman correlation: %f', spearmanr(true_similarities, test_similarities)[0])
