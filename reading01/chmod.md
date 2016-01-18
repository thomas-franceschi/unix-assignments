TLDR - chmod
==========

Overview
--------

[chmod] is a command line command that is used to adjust user permissions 
assigned to specific files

Examples
--------

- **+** is used to give a user more permissions:

    $ chmod u+x myFile
        
- **-** is used to take away permissions:

    $ chmod u-x myFile
        
- **chmod -c** gives a verbose output when changes are made:

    $ chmod -c
        
- **chmod -f** surpresses error messages:

    $ chmod -f
        
Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/chmod.1.html)

[chmod]: http://man7.org/linux/man-pages/man1/chmod.1.html
