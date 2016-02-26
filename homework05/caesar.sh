#!/bin/sh
source="abcdefghijklmnopqrstuvwxyz"
SOURCE="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key=13

if [ $1 ]
        then key=$(($1 % 26))
fi

if [ $key -eq 0 ]
	then
	tr '[A-Za-z]' '[A-Za-z]'
	exit;
fi

if [ $1 ]
	then
	front=$(echo $source | cut -b $(($key + 1))-26)
	back=$(echo $source | cut -b 1-$key)
	target=$(echo $front$back)
	FRONT=$(echo $SOURCE | cut -b $(($key + 1))-26)
	BACK=$(echo $SOURCE | cut -b 1-$key)
	TARGET=$(echo $FRONT$BACK)
	tr $(echo $source) $(echo $target) | tr $(echo $SOURCE) $(echo $TARGET)
else
	tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
fi
