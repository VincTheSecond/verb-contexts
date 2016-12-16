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
parser.description = 'Split CoNNLU file into several smaller files.'
parser.add_argument('--input', required=True, help='an input file')
parser.add_argument('--sentences', required=True, help='a number of sentences per each file')
parser.add_argument('--pattern', required=True, help='an output pattern for files')
args = parser.parse_args()


# A method for reading one sentence.
def read_sentence(filehandler):
    lines = []
    while 42:
        one_line = filehandler.readline().rstrip()
        lines.append(one_line)
        if one_line == '':
            return lines


sentence_counter = 0
with open(args.input, 'r') as fin:
    while 42:
        sentences = []
        for i in range(int(args.sentences)):
            sentence_counter += 1
            sentence = read_sentence(fin)
            if len(sentence) == 0:
                break

            sentences.append(sentence)

        output_file = '%s_%d_%d.conllu' % (args.pattern, sentence_counter - int(args.sentences), sentence_counter)
        logging.info('Creating %s', output_file)
        with open(output_file, 'w') as fout:
            for sentence in sentences:
                fout.write('\n'.join(sentence))
                fout.write('\n')

        if len(sentences) != int(args.sentences):
            break
