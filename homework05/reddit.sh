#!/bin/bash


num=10
flag=0
SUB=$1

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

if [[ $num =~  ^[A-Za-z_]+$ ]]
	then
	num=10
	SUB=$2
fi

echo "flag is $flag"
echo "num is $num"
echo "subreddit is $SUB"
shift $((OPTIND-1))

if [ $flag -eq 1 ]
	then
	curl -s http://www.reddit.com/r/$SUB/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | shuf | uniq
	exit;
fi

if [ $flag -eq 2 ]
        then
        curl -s http://www.reddit.com/r/$SUB/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | sort | uniq
	exit;
fi

if [ $flag -eq 3 ]
	echo "reached third flag"
	then
       	curl -s http://www.reddit.com/r/$SUB/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | head -n $num
	exit;
fi

curl -s http://www.reddit.com/r/$SUB/.json | python -m json.tool | grep "\"url\":" | sed 's/\s//g' | uniq
exit;
