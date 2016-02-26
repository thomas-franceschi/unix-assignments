#!/bin/bash


num=10
flag=0

while getopts rsn: i
do
	case $i in
		n) flag=3
		num=$OPTARG;;
		r) flag=1;;
		s) flag=2;;
		*) echo "bad flag!";;
	esac
done

shift $((OPTIND-1))

if [ $flag -eq 1 ]
	then
	curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | sed 's/\"url\"://g' | shuf | uniq
	exit;
fi

if [ $flag -eq 2 ]
        then
        curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | sed 's/\"url\"://g' | sort | uniq
	exit;
fi

if [ $flag -eq 3 ]
	then
       	curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | sed 's/\"url\"://g' |head -n $num
	exit;
fi

curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | sed 's/\"url\"://g' | uniq
exit;
