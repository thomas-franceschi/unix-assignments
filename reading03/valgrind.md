TLDR - valgrind
==========

Overview
--------

[valgrind] is a program that is used to debug linux executables.

Examples
--------

- **-v** gives verbose output:

    $ valgrind -v ./a.out
    
- **--leak-check=yes** checks profile for memory leaks:

    $ valgrind --leak-check=yes ./a.out  

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/valgrind.1.html)
