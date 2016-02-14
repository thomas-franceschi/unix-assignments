#!/bin/sh

#say hello

echo "you start with $# positional parameters"

while [ "$1" != "" ]; do
    echo "Hello, $1!"
    shift
    
done