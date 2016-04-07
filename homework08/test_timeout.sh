#!/bin/bash

#get environment used in shebang
SHEBANG=$(cat timeout.py | head -n 1 | cut -d ' ' -f 2 )
N=1

#test if executable
if [[ -x timeout.py ]]
then
	echo "Executable test sucessful!"
else
	echo "Failed Executable Test!"
	exit 1;
fi

#test for python2.7 in shebang
if [[ "$SHEBANG" = "python2.7" ]]
then
	echo "SheBang test successful!"
else
	echo "Failed SheBang Test!"
	exit 1;
fi

#test for proper -h output
OUTPUT="$(./timeout.py -h 2>&1)"

if [[ -z "$OUTPUT" ]] #Test for an empty string AKA no output to std error
then
	echo "Failed -h test!"
	exit 1;
else
	echo "-h test successfu!"
fi

#test for verbose output


#test succesfull exit
#while [ $N -lt 5 ]
#do
#	echo $N
#	OUTPUT=$(./timeout.py -t 5 sleep $N)
#	$(./timeout.py -t 5 sleep $N || echo Success)
#	N=$(($N+1))
#done

#test failure exit
N=2
while [ $N -lt 6 ]
do
	if [[ $(./timeout.py -t 1 sleep $N) ]]
	then
		echo "Failed exit test Failed!"
		exit 1;
	fi
	N=$(($N+1))
done
echo "Failed exit test was a success!"
