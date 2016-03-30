#!/usr/bin/env python2.7

import os
import sys

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
input_file = 0
output_file = 1
bs = 512
count = sys.maxint
seek = 1
skip = 1


# Functions

def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
	error('Could not open {}: {}'.format(path, e))

def read_fd(fd, n):
	try:
		return os.read(fd, n)
	except OSError as e:
	        error('Could not read {} bytes from FD {}: {}'.format(n, fd, e))

def write_fd(fd, data):
	try:
		return os.write(fd, data)
	except OSError as e:
		error('Could not write {} bytes from FD {}: {}'.format(len(data), fd, e))


def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

# Parse Command line arguments


args = sys.argv[1:]

for arg in args:
	names, values = arg.split('=')

	if names == 'if':
		input_file = open_fd(values, os.O_RDONLY)
	if names == 'of':
		output_file = open_fd(values, os.O_WRONLY|os.O_CREAT)
	if names == 'count':
		count = values
	if names == 'bs':
		bs = values
	if (names == 'seek') and (output_file != 0):
		seek = values
		os.lseek(output_file, int(int(seek)*int(bs)), os.SEEK_SET)
	if (names == 'skip') and (input_file != 0):
		skip = values
		os.lseek(input_file, int(int(skip)*int(bs)), os.SEEK_SET)

# Main Execution


data = read_fd(input_file, int(bs))
while (count > 0) and data:
	write_fd(output_file, data)
	data = read_fd(input_file, int(bs))
	count = int(count) - 1

os.close(input_file)
os.close(output_file)
