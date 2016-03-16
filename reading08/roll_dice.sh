#!/bin/sh

ROLLS=10
SIDES=6

while getopts r:s: opt; do
	case $opt in
		r) ROLLS=$OPTARG;;
		s) SIDES=$OPTARG;;
		*) echo "bad flag";;
	esac
done

shift $((OPTIND-1))

until [ $ROLLS -eq 0 ]; do
	shuf -i 1-$SIDES | head -n 1
	$((ROLLS=$ROLLS-1)) 2>/dev/null
done
