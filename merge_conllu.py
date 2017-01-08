#!/usr/bin/env python
#
# Author: (c) 2016 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import sys
import logging
import argparse

# Set logging
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Merge parsing data from the reduced Conllu into the given full Conllu file.'
parser.add_argument('--reduced_file', required=True, help='a reduced CoNLLU file with parsing data')
parser.add_argument('--full_file', required=True, help='a full CoNLLU file with the rest of data')
parser.add_argument('--output_file', required=True, help='an output file')
args = parser.parse_args()

# Merge file
with open(args.reduced_file, 'r') as reduced:
    with open(args.full_file, 'r') as full:
        with open(args.output_file, 'w') as final:
            while 42:
                reduced_line = reduced.readline().rstrip()
                full_line = full.readline().rstrip()

                if reduced_line == '':
                    final.write('\n')
                    continue

                reduced_fields = reduced_line.split('\t')
                full_fields = full_line.split('\t')

                full_fields[6] = reduced_fields[3]
                full_fields[7] = reduced_fields[4]

                final_line = '\t'.join(full_fields)
                final.write('%s\n' % final_line)
