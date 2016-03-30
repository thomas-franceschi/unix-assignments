#!/usr/bin/env python2.7

import os
import sys
import re
import fnmatch
import pwd
import stat
from stat import ST_MODE, S_ISREG, S_ISLNK, S_IMODE

try:
	DIR = sys.argv[1]
	if not os.path.isdir(DIR):
		print "not a directory"
except IndexError:
	print "invalid usage"

# Global Variables

totArgs = {}
numArgs = len(sys.argv)
withArgs = ["-name", "-type", "-path", "-regex", "-perm", "-newer", "-uid", "-gid"];
noArgs = ["-executable", "-readable", "-writable", "-empty"];

# Functions
def isSymLink(path):
	try:
		stat = os.stat(path)
	except OSError:
		stat = os.lstat(path)
	return S_ISLNK(stat.st_mode)

# Parse Command line arguments

for args in range(2, numArgs):
	if sys.argv[args] in withArgs:
		try:
    			totArgs[sys.argv[args]] = sys.argv[args+1]
		except IndexError:
			print "missing argument for" + sys.argv[args],
			sys.exit(1)

	elif sys.argv[args] in noArgs:
		totArgs[sys.argv[args]] = ""


def include(path):
	if "-type" in totArgs:
		if totArgs["-type"] == "f":
			if not os.path.isfile(path):
				return
		elif totArgs["-type"] == "d":
			if not os.path.isdir(path) and path != DIR:
				return

	if "-executable" in totArgs:
		if not os.access(path, os.X_OK):
			return

	if "-readable" in totArgs:
		if not os.access(path, os.R_OK):
			return

	if "-writable" in totArgs:
		if not os.access(path, os.W_OK):
			return

	if "-name" in totArgs:
		if not fnmatch.fnmatch(os.path.basename(path), totArgs["-name"]):
			return

	if "-empty" in totArgs:
		if isSymLink(path):
			return
		if os.path.isfile(path) and not os.stat(path).st_size == 0:
			return
		else:
			try:
				if os.path.isdir(path) and not os.listdir(path) == []:
					return
			except OSError:
				return

	if "-path" in totArgs:
		if not fnmatch.fnmatch(os.path.join(root, path), totArgs["-path"]):
			return

	if "-regex" in totArgs:
		match = re.compile(totArgs["-regex"])
		if not match.match(path):
			return

	if "-perm" in totArgs:
		if isSymLink(path):
			return
		try:
			if int(oct(S_IMODE(os.stat(path).st_mode))) != int(totArgs["-perm"]):
				return
		except OSError:
			pass

	if "-newer" in totArgs:
		if isSymLink(path):
			return
		if os.stat(totArgs["-newer"]).st_mtime >= os.stat(path).st_mtime:
			return

	if "-gid" in totArgs:
		try:
			if not int(totArgs["-gid"]) == int(os.stat(path).st_gid):
				return
		except OSError:
			pass

	if "-uid" in totArgs:
		try:
			if not int(totArgs["-uid"]) == int(os.stat(path).st_uid):
				return
		except OSError:
			pass

	print os.path.join(path)

for root, dirs, files in os.walk(DIR, followlinks=True):
	for f in files + dirs:
		include(os.path.join(root, f))
include(os.path.join(DIR))
