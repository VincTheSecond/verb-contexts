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
parser.description = 'Add sentence IDs into the CoNLLU file.'
parser.add_argument('--input_file', required=True, help='an input file')
parser.add_argument('--output_file', required=True, help='an output file')
args = parser.parse_args()


sentence_counter = 0
with open(args.input_file, 'r') as fin:
    with open(args.output_file, 'w') as fout:
        sentence = []
        for one_line in fin:
            one_line = one_line.rstrip()
            sentence.append(one_line)

            if one_line == '':
                sentence_counter += 1
                if (sentence_counter % 10000) == 0:
                    logging.info('Processed %d sentences.', sentence_counter)

                sent_id = 'en%09d' % sentence_counter
                fout.write('# sent_id %s\n' % sent_id)
                fout.write('\n'.join(sentence))
                fout.write('\n')

                sentence = []
