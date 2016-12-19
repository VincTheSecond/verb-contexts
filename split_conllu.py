#!/usr/bin/env python
#
# Author: (c) 2016 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import sys
import logging
import argparse


# Logging.
from wheel.metadata import requires_to_requires_dist

logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)


# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Split CoNNLU file into several smaller files.'
parser.add_argument('--input_file', required=True, help='an input file')
parser.add_argument('--output_dir', required=True, help='an output dir')
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
with open(args.input_file, 'r') as fin:
    while 42:
        sentence = read_sentence(fin)
        if len(sentence) == 0:
            break

        if (sentence_counter % 10000) == 0:
            logging.info('Processed %d sentences.', sentence_counter)

        sentence_counter += 1
        if sentence[0][:9] == '# sent_id':
            sent_id = sentence[0][10:]
            if sent_id[-3:] == '/cs':
                sent_id = sent_id[:-3]

        output_file = '%s/%s.conllu' % (args.output_dir, sent_id)
        logging.debug('File: %s', output_file)
        with open(output_file, 'w') as fout:
            fout.write('\n'.join(sentence))
            fout.write('\n')
