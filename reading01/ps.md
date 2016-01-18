TLDR - ps
==========

Overview
--------

[ps] is a command line command used to report a snapshot of the current 
processes

Examples
--------

- **ps -e, -ef, eF, -ely** is used to display all processes using a standard syntax:

    $ ps -e
        
- **ps ax, axu** is used to print every process using a BSD syntax:

    $ ps ax
        
- **ps -ejH, axjf** prints a process tree:

    $ ps -ejH
        
- **ps -eLf** gets info about threads:

    $ ps -eLf
        
- **ps -eo** gets security info:

    $ ps -eo

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/ps.1.html)

[ps]: http://man7.org/linux/man-pages/man1/ps.1.html
