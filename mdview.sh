#!/bin/sh

export PATH=/afs/nd.edu/user15/pbui/pub/anaconda-2.3.0/bin:$PATH

if [ $# != 1 ]; then
    echo "usage: $0 path"
    exit 1
fi

if ! command -v markdown_py > /dev/null; then
    echo "error: you need to install markdown_py!"
    exit 2
fi


if ! command -v elinks > /dev/null; then
    echo "error: you need to install elinks!"
    exit 3
fi

exec markdown_py $@ | \
     elinks -force-html -dump -dump-width $(tput cols) -no-numbering -no-references | \
     less
