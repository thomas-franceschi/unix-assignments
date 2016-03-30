#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
input_file = 0
output_file = 1
bs = 512
count = sys.maxint
seek = 0
skip = 0


# Functions

def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
        print >>sys.stderr, 'Could not open file {}: {}'.format(path, e)
        sys.exit(1)

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

# Parse Command line arguments


args = sys.argv[1:]

for arg in args:
	names, values = arg.split('=')
	names = values

print input_file
print output_file
print bs
# Main Execution


open(input_file)





close(input_file)
error('{} Not implemented!'.format(PROGRAM_NAME))
