#!/usr/bin/env python2.7

import sys
import os
import time
import getopt

COMMAND = sys.argv[len(sys.argv) - 1]
n = 2

def error(message, exit_code=1):
	print>>sys.stderr, message
	sys.exit(exit_code)

def usage(exit_code=0):
	error('''Usage: {}

Options:
	-n Interval	specify update interval in seconds'''
	.format(PROGRAM_NAME), exit_code)



try:
	options, arguments = getopt.getopt(sys.argv[1:], "n:")
except getopt.GetoptError as e:
	error(e)

for option, value in options:
	if option == "-n":
		n = value
	else:
		usage(1)

s = " "
seq = "Every " + str(n) + ".0s: " + COMMAND

try:
	while True:
		os.system('clear')
		print (str(seq))
		os.system(COMMAND)
		time.sleep(float(n))
except KeyboardInterrupt:
	os.system('clear')
	sys.exit(0)

