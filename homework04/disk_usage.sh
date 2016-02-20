#!/bin/sh

nopt=10
aopt=''

while getopts an: name
do
	case $name in
		a)aopt='-a';;
		n)nopt=$OPTARG;;
		*)echo "invalid flag";;
	esac
done


shift $(($OPTIND - 1))

while [ $# -gt 0 ]
do
	du -h $aopt $1 2>/dev/null | sort -hr | head -n $nopt
	shift
done
