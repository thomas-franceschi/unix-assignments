TLDR - strings
==========

Overview
--------

[strings] is a command that prints all of the strings of printable characters 
in a file.

Examples
--------

- **-a** scans the whole file (enabled by default):

    $ strings -a hello.c
    
- **-f** prints the name of the source file before each string:

    $ strings -f hello.c

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/strings.1.html)
