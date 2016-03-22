import sys
import getopt

COUNT = False
NEWLINE = False
WORD = False

count = 0
new_line = 0
words = 0


try:
	opts, args = getopt.getopt(sys.argv[1:], "clw")
except getopt.GetoptError as e:
	print e

for o, a in opts:
	if o == "-c":
		COUNT = True
	elif o == "-l":
		NEWLINE = True
	elif o == "-w":
		WORD = True
	else:
		print "ERROR: enter valid flag"
	sys.exit(1)

if len(args) == 0:
	args.append('-')

for path in args:
	if path == '-':
		stream = sys.stdin
	else:
		stream = open(path)

	for line in stream:
		count = count + len(line)
		if "\n" in line:
			new_line = new_line + 1
		if WORD:
			words = words + len(line.split())

	if COUNT:
		print count
	if NEWLINE:
		print new_line
	if WORD:
		print words

	stream.close()
