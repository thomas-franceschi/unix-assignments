#!/bin/sh

#resolve system links

if [ -d $1 ];
    then for f in $1/*; do
        if [ -L $f ];
            then echo "$f links to $(readlink $f) "
        fi
    done    
fi