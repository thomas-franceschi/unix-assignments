#!/bin/sh

CHAR='#'
flag=0

while getopts d:W i
do
	case $i in
	d) CHAR=$OPTARG;;
	W) flag=1;;
	*) echo "Bad flag"
	esac
done

del_whitespace()
{
	if [ $flag -eq 0 ]
		then
		sed '/^s*$/d'
		else
		cat
fi
}

sed "s:$CHAR.*::" | sed "s:[ \t]*$::" | del_whitespace
