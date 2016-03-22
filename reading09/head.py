import sys
import getopt

NUM = 10
COUNT = 0

try:
	opts, args = getopt.getopt(sys.argv[1:], "n:")
except getopt.GetoptError as e:
	print e

for o, a in opts:
	if o == '-n':
		NUM = a

for o, a in opts:
	if o == '-':
		args.append('-')

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for line in stream:
		NUM = int(NUM)
		if COUNT < NUM:
			print line,
			COUNT = COUNT + 1
		else:
			sys.exit(1)

	stream.close()
