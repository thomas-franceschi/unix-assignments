import getopt
import sys
import os

DELIM = '\t'
field = False

def usage(status=0):
	print'''usage: cut.py [-d DELIM -f] files...

	-d DELIM use DELIM instead of TAB for field delimiter
	-f FIELDS  select only these FIELDS'''.format(os.path.basename(sys.argv[0]))

try:
	opts, args = getopt.getopt(sys.argv[1:], "hd:f:")
except getopt.GetoptError as e:
	print e
	usage(1)

for o, a in opts:
	if o == '-d':
		DELIM = a
	elif o == '-f':
		field = True
		F = a.split(',')
	else:
		usage(1)

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)
	if not field:
		print "Error: enter a number of fields"
		usage(1)

FF = []
results = []
for field in F:
	FF.append(int(field))

for line in stream.readlines():
	line = line.rstrip()
	mylist = line.split(DELIM)
	for field in FF:
		value = field - 1
		if (value) < len(mylist):
			results.append(mylist[value])

	print DELIM.join(results)
