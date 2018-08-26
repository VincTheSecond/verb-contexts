#!/usr/bin/env python
#
# Author: (c) 2017 Vincent Kriz <kriz@ufal.mff.cuni.cz>
#

import sys
import logging
import argparse

# Logging.
logging.basicConfig(format='%(asctime)-15s [%(levelname)7s] %(funcName)s - %(message)s', level=logging.DEBUG)

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.description = 'Remove specified contexts extracted by udapi from the source dataset.'
parser.add_argument('--remove', required=True, help='A comma separated list of bags to remove.')
parser.add_argument('--input', required=True, help='Input contexts.')
parser.add_argument('--output', required=True, help='Output contexts.')
parser.add_argument('--merge_inverse_relations', required=False, default=False, type=bool, help='If true, inverse relations will merged to non-inverse.')
args = parser.parse_args()

context_to_remove = dict()
for relation_name in args.remove.split(','):
    context_to_remove[relation_name] = 1

with open(args.input, 'rb') as input_contexts:
    with open(args.output, 'wb') as output_contexts:
        for (n_line, line) in enumerate(input_contexts):
            if (n_line % 1000000) == 0:
                logging.info('Processed %d contexts', n_line)

            # Source dataset contains invalid lines :-(
            if len(line.split(' ')) != 2:
                continue

            relation_name = line.split(' ')[1].split('_')[0]

            # Provide merging, if needed.
            if args.merge_inverse_relations:
                if relation_name[-1] == 'I':
                    relation_name = relation_name[:-1]

            if relation_name in context_to_remove:
                continue

            output_contexts.write(line)
