#!/bin/sh

LINES=10
FILE=$1

while getopts n: i
do
	case $i in
		n) LINES=$OPTARG;;
		*) echo "Bad flag, bro"
	esac
done

awk -v lines=$LINES 'NR <= lines'
