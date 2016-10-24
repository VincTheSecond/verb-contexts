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
parser.description = 'Count token frequencies from the STDIN and build a vocabulary for word2vec.'
parser.add_argument('--threshold', required=True, help='a frequency threshold for ')
parser.add_argument('--output', required=True, help='a path where final vocabulary will be saved')
args = parser.parse_args()

threshold = int(args.threshold)

# Build vocabulary.
vocabulary = Counter()
max_freq = 0
token_buffer = []
for (n_word, word) in enumerate(sys.stdin):
    if (n_word % 10000000) == 0:
        vocabulary.update(token_buffer)
        token_buffer = []

        logging.info('Processed %10d tokens. Vocabulary size: %10d', n_word, len(vocabulary))

    word = word.rstrip()
    token_buffer.append(word)

vocabulary.update(token_buffer)
token_buffer = []

with open(args.output, 'w') as fout:
    for (word, frequency) in vocabulary.iteritems():
        max_freq = max(max_freq, frequency)
        if word == '':
            continue

        if frequency < threshold:
            continue

        fout.write('%s\t%s\n' % (word, frequency))

logging.info('Max_freq = %d', max_freq)
