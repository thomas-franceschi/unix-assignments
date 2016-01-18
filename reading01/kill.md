TLDR - kill
==========

Overview
--------

[kill] is a command line command that is used to terminate processes

Examples
--------

- **kill -9** is a forced termination that cannot be trapped:

    $ kill -9 PID
        
- **kill -l** is used to list signal names:

    $ kill -l
        
- **kill -15** is used to terminate a function, but can be trapped:

    $ kill -15 PID
        
- **kill -s** sends a signal:

    $ kill -s mySignal PID

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/kill.1.html)

[kill]: http://man7.org/linux/man-pages/man1/kill.1.html
