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
parser.description = 'Split contexts extracted by udapi into several files, one file per relation.'
parser.add_argument('--contexts', required=True, help='Input contexts')
parser.add_argument('--output_dir', required=True, help='Directory for output files')
parser.add_argument('--merge_inverse_relations', required=False, default=False, type=bool, help='If true, inverse relations will merged to non-inverse.')
args = parser.parse_args()


file_handlers = dict()

with open(args.contexts, 'rb') as contexts:
    for (n_line, line) in enumerate(contexts):
        if (n_line % 1000000) == 0:
            logging.info('Processed %d contexts, open %d handlers: %r', n_line, len(file_handlers), file_handlers.keys())

        # Source dataset contains invalid lines :-(
        if len(line.split(' ')) != 2:
            continue

        relation_name = line.split(' ')[1].split('_')[0]

        # Provide merging, if needed.
        if args.merge_inverse_relations:
            if relation_name[-1] == 'I':
                relation_name = relation_name[:-1]

        if relation_name not in file_handlers:
            file_handlers[relation_name] = open('%s/%s.contexts' % (args.output_dir, relation_name), 'wb')

        file_handlers[relation_name].write(line)
