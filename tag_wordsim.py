#!/usr/bin/env python
#
# Author: (c) 2016 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#
# As WordSim353 does not provide the POS tags, we adopt the same
# strategy as was used in the SimLex-999 dataset. For each word form
# we obtain the most frequent POS from the tagged corpora.

import sys
import logging
import argparse

from collections import defaultdict


# Logging.
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)


# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Train most frequent POS tags for each word form.'
parser.add_argument('--dataset', required=True, help='a WordSim to be tagged')
parser.add_argument('--lang', required=True, help='a WordSim mutation (cs, en)')
parser.add_argument('--output', required=True, help='a modified WordSim')
args = parser.parse_args()


# Methods.
def pos_frequencies():
    return defaultdict(int)


def parse_wordsim_en(line):
    fields = line.rstrip().split('\t')
    word1 = fields[0]
    word2 = fields[1]

    return word1, word2


def parse_wordsim_cs(line):
    fields = line.rstrip().split('\t')
    word1 = fields[6]
    word2 = fields[7]

    return word1, word2

def tag_word(word):
    max_frequency = 0
    max_frequent_pos = 0
    for pos in dictionary[word]:
        if dictionary[word][pos] > max_frequency:
            max_frequency = dictionary[word][pos]
            max_frequent_pos = pos

    logging.info('Tagging %s by POS %s', word, max_frequent_pos)
    return max_frequent_pos


# Parse a dataset and obtain a list of words to be tagged.
vocabulary = dict()
logging.info('Loading WordSim.')
with open(args.dataset, 'r') as fdataset:
    for (n_line, line) in enumerate(fdataset):
        if n_line == 0:
            continue

        if args.lang == 'en':
            word1, word2 = parse_wordsim_en(line)
        elif args.lang == 'cs':
            word1, word2 = parse_wordsim_cs(line)
        else:
            raise NotImplementedError('Unsupported WordSim mutation.')

        vocabulary[word1] = 1
        vocabulary[word2] = 1
logging.info('Loaded %d different word forms to tag.', len(vocabulary))

# Read STDIN and count frequencies
logging.info('Counting frequencies.')
dictionary = defaultdict(pos_frequencies)
for (n_line, line) in enumerate(sys.stdin):
    if (n_line % 10000000) == 0:
        logging.info('Processed %10d tokens', n_line)

    word, pos = line.rstrip().split('\t')

    if args.lang == 'en':
        word = word.split('_')[0]

    if word in vocabulary:
        dictionary[word][pos] += 1


# Save results.
with open(args.output, 'w') as fout:
    with open(args.dataset, 'r') as fdataset:
        for (n_line, line) in enumerate(fdataset):
            if n_line == 0:
                fout.write('%s\tPOS 1\tPOS 2\n' % line.rstrip())
                continue

            if args.lang == 'en':
                word1, word2 = parse_wordsim_en(line)
            elif args.lang == 'cs':
                word1, word2 = parse_wordsim_cs(line)
            else:
                raise NotImplementedError('Unsupported WordSim mutation.')

            pos1 = tag_word(word1)
            pos2 = tag_word(word2)

            fout.write('%s\t%s\t%s\n' % (line.rstrip(), pos1, pos2))
