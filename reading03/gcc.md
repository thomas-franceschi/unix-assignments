TLDR - GCC
==========

Overview
--------

[GCC]: GNU C Compiler, used to compile executables form C source code.

Examples
--------

- **-o** allows you to name the executable:

    $ gcc hello.c -o hello
    
- **-g** generates debugging information that can be used in another program:

    $ gcc -g hello.c

- **-pg** generates profiling informationt that can be used to find bottlenecks:

    $ gcc -pg hello.c    

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/gcc.1.html)
