#!/bin/sh

./roll_dice.sh -r 1000 | awk '{count[$1]++}END{for(i in count) print i,"\t"count[i]""}' | tee results.dat
