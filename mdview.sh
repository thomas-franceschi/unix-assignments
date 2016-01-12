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

stylize() {
     sed -e 's|pre>|p style="color:green;">|g' \
	 -e 's|<h\([0-9]\)>|<h\1 style="color:yellow;">|g' \
	 -e 's|<strong>|<strong style="color:magenta;">|g'
}

exec markdown_py $@ |
     stylize |
     elinks -force-html -dump -dump-width $(tput cols) -dump-color-mode 1 -no-numbering -no-references |
     less -Rcgm
