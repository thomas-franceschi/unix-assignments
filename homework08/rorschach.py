#!/usr/bin/env python2.7

import getopt
import os
import sys
import re
import yaml
import fnmatch
import shlex
import time
import errno
import string

# Global Variables
NAME = os.path.basename(sys.argv[0])
YAML = '.rorschach.yml'
DIRECTORIES = '.'
SECONDS = 2

VERBOSE = False

# Functions
def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {} [-r YAML -t SECONDS] DIRECTORIES...

Options:

    -r YAML    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message'''
    .format(NAME), exit_code)



def check_file(path, data):
    '''Checks each file to see if it matches the rules and then executes the action if so.'''
    if VERBOSE:
        print "Checking for pattern matches..."
    for x in data:
        if fnmatch.fnmatch(path, x['pattern']):
            execute(path, x)
            
def check_dir(data, dictionary):
    '''Walks the specified directory and checks if each file matches any rules.'''
    for root, dirs, files in os.walk(DIRECTORIES):
        files = [f for f in files if not f[0] == '.']
        for name in files:
            fname = os.path.join(root, name)
            if fname in dictionary:
                if os.path.exists(fname):
                    prev = dictionary[fname]
                    current = os.path.getmtime(fname)
                    if prev < current:
                        dictionary[fname] = current
                        check_file(fname, data)
            else:
                diction[fname] = os.path.getmtime(fname)
                check_file(fname, data)

def execute(path, data):
    '''This function executes the action.'''
    if VERBOSE:
        print "Forking process..."
    command = data['action'].format(path=path)
    arguments = shlex.split(command)
    try:
        pid = os.fork()
        if pid == 0:
            try:
                if VERBOSE:
                    print "Executing command..."
                os.execvp(arguments[0], arguments)
            except OSError as e:
                error('Unable to exec: {}', e)
        else:
            try:
                pid, status = os.wait()
            except OSError as e:
                if e.errno == errno.EINTR:
                    pid, status = os.wait()
                else:
                    error(e)
    except OSError as e:
        error('Unable to fork: {}', e)

# Parse Command line arguments
try:
    options, arguments = getopt.getopt(sys.argv[1:], "hr:t:v")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    if option == '-r':
        YAML = value
    if option == '-t':
        SECONDS = value
    if option == '-v':
        VERBOSE = True

# Main Execution
direct = sys.argv[len(sys.argv) - 1]
if(os.path.isdir(direct)):
    DIRECTORIES = direct

info = open(YAML)
data = yaml.load(info)
info.close()

diction = {}
if VERBOSE:
    print "Determining files already in directory..."
for root, dirs, files in os.walk(DIRECTORIES):
    files = [f for f in files if not f[0] == '.']
    for name in files:
        fname = os.path.join(root, name)
        diction[fname] = os.path.getmtime(fname)

if VERBOSE:
    print "Checking for new or modified files..."

try:
    while True:
        check_dir(data, diction)
except KeyboardInterrupt:
    os.system('clear')
    sys.exit(0)
