import sys
import getopt

DISP_COUNT = False
NEWLINE = False
PRINT_WORDS = False

word_count = 0
new_line = 0
words = 0


try:
	opts, args = getopt.getopt(sys.argv[1:], "clw")
except getopt.GetoptError as e:
	print e

for o, a in opts:
	if o == "-c":
		DISP_COUNT = True
	elif o == "-l":
		NEWLINE = True
	elif o == "-w":
		PRINT_WORDS = True
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
		word_count = word_count + len(line)
		if "\n" in line:
			new_line = new_line + 1
		if PRINT_WORDS:
			words = words + len(line.split())

	if DISP_COUNT:
		print word_count
	if NEWLINE:
		print new_line
	if PRINT_WORDS:
		print words

	stream.close()
