import sys
import getopt
import os
from collections import Counter

NUMOCCUR = False
countList = []

def usage(status=0):
    print '''usage: {} [-c] files...

    -c displays the number of occurences of each string'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)


try:
    opts, args = getopt.getopt(sys.argv[1:], "c")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-c':
        NUMOCCUR = True
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

for path in args:
	if path == '-':
		file = sys.stdin
	else:
		file = open(path)

	with file as f:
		countList = [line.strip() for line in f]

countDict = Counter(countList)

for key, value in countDict.items():
	if NUMOCCUR == True:
		print value, key
	else:
		print key

