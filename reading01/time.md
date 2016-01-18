TLDR - time
==========

Overview
--------

[time] is a command line command that is used to track the time a specific 
command takes to execute

Examples
--------

- **time -f** is used to format the output using other modifiers:

    $ time -f "%E, %U, %S" myCommand
        
- **time -v** gives verbose output with everything known about the program:

    $ time -v
        
- **time -o** writes output to a specified file:

    $ time -o output.txt myCommand

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/time.1.html)

[time]: http://man7.org/linux/man-pages/man1/time.1.html
