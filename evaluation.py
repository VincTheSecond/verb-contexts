#!/usr/bin/env python
# coding=utf-8
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
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.INFO)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Evaluate word vectors over a given similarity dataset.'
parser.add_argument('--vectors', required=True, help='a file with word vectors')
parser.add_argument('--folds', required=True, help='a number of cross-validation folds')
parser.add_argument('--reflexive_verbs', required=True, help='possible values: {remove|merge|asis}')
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
total_pairs = 0
correlations = []
unknown_words = {}
unknown_pairs = {}
for fold in range(1, int(args.folds) + 1):
    true_similarities = []
    test_similarities = []
    logging.info('Evaluating fold %d...', fold)
    filename = '%s_0%d.csv' % (args.dataset, fold)
    with open(filename, 'r') as fdataset:
        for (n_line, line) in enumerate(fdataset):
            if n_line == 0:
                continue

            word1, word2, true_similarity = line.rstrip().split(',')
            true_similarity = float(true_similarity)
            true_similarities.append(true_similarity)

            # Take only first token from word1, word2 to effective ignoring reflexives.
            if args.reflexive_verbs == 'remove':
                word1 = word1.split(' ')[0]
                word2 = word2.split(' ')[0]
            elif args.reflexive_verbs == 'merge':
                word1 = word1.replace(' ', '_')
                word2 = word2.replace(' ', '_')
            elif args.reflexive_verbs == 'asis':
                pass
            else:
                raise ValueError('Unknown value in --reflexive_verbs option.')

            if word1 not in vectors:
                # Try lemmatized version of following words:
                # if 'říct' not in vectors:
                #     word1 = 'říci'
                # if 'neuspět' not in vectors:
                #     word1 = 'uspět'

                # Try lemmatized version of the reflexive word (si->se)
                # if args.reflexive_verbs == 'merge'.
                if args.reflexive_verbs == 'merge':
                    word1 = word1.replace('_si', '_se')
                    if word1 not in vectors:
                        unknown_words[word1] = 1
                        unknown_pairs['%s + %s' % (word1, word2)] = 1
                else:
                    unknown_words[word1] = 1
                    unknown_pairs['%s + %s' % (word1, word2)] = 1

            if word2 not in vectors:
                # Try lemmatized version of following words:
                # if 'říct' not in vectors:
                #     word2 = 'říci'
                # if 'neuspět' not in vectors:
                #     word2 = 'uspět'

                # Try lemmatized version of the reflexive word (si->se)
                # if args.reflexive_verbs == 'merge'.
                if args.reflexive_verbs == 'merge':
                    word1 = word1.replace('_si', '_se')
                    if word1 not in vectors:
                        unknown_words[word1] = 1
                        unknown_pairs['%s + %s' % (word1, word2)] = 1
                else:
                    unknown_words[word2] = 1
                    unknown_pairs['%s + %s' % (word1, word2)] = 1

            test_similarity = 0.0
            if word1 in vectors and word2 in vectors:
                test_similarity = cosine_similarity(vectors[word1], vectors[word2])[0][0]
            test_similarities.append(test_similarity)

            logging.debug('%s + %s | %r | %r', word1, word2, true_similarity, test_similarity)

        total_pairs += len(test_similarities)
        logging.debug('test_similarities = %s', test_similarities)
        logging.debug('true_similarities = %s', true_similarities)
        logging.debug('spearman = %r', spearmanr(true_similarities, test_similarities))

        correlations.append(spearmanr(true_similarities, test_similarities)[0])

logging.debug('Correlations            : %s', correlations)
logging.info('Spearman correlation    : %.4f', np.mean(correlations))
logging.debug('Unknown pairs           : %d', len(unknown_pairs))
logging.info('Number of unknown pairs : %.3f', len(unknown_pairs) / float(total_pairs))

# for unknown_word in unknown_words:
#     print unknown_word
