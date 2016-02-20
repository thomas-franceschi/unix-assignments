#!/bin/sh

SUFFIXES=.c
CC=gcc
CFLAGS="-std=c99 -Wall"
VERBOSE=${VERBOSE:-0}

for argument in *$SUFFIXES
	do $CC $CFLAGS $argument -o ${argument%.c}
	if [ $VERBOSE -eq 1 ]
	then
		echo "$CC $CFLAGS $argument -o ${argument%.c}"
	fi
done
