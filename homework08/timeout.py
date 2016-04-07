#!/usr/bin/env python2.7

# Kyle Williams

import getopt
import os
import sys
import signal
import time
import errno

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
SECONDS = 10
VERBOSE = False
ARG = 1

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {} [-t SECONDS] command...

Options:

    -h              Show this help message

    -t SECONDS      Timeout duration before killing command (default is 10 seconds)
    -v              Display verbose debugging output'''
    .format(PROGRAM_NAME), exit_code)

def debug(message, *args):
	if VERBOSE == True:
		''' Print message formatted with args to sys.stderr if VERBOSE is True '''
		print >> sys.stderr, message

def sigchld_handler(signum, frame):
    global ChildPid, ChildStatus
    os.kill(0, 15)
    ChildPid, ChildStatus = os.wait()


# Parse Command line arguments

try:
    options, arguments = getopt.getopt(sys.argv[1:], "ht:v")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    if option == '-t':
        SECONDS = value
	ARG = 3
    if option == '-v':
        VERBOSE = True
	ARG = 2

# Main Execution

try:
    debug("forking...")
    pid = os.fork()
    if pid == 0:
        try:
            os.execvp(sys.argv[ARG], arguments)
	except OSError as e:
      	    error('Unable to exec: {}', e)
    else:
	debug("enabling alarm...")
	signal.alarm(int(SECONDS))
	debug("waiting...")
        signal.signal(signal.SIGCHLD, sigchld_handler)
        try:
            pid, status = os.wait()
        except OSError as e:
            if e.errno == errno.EINTR:
                pid, status = os.wait()
            else:
                error(e)
except OSError as e:
    error('Unable to fork: {}', e)

sys.exit(status)
