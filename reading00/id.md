TLDR - id
==========

Overview
--------

[Id] is a command used to print real and effective user and group IDs.

Examples
--------

- **id -a** ignore, for compatibility with other versions:

	$ id -a

- **id -Z** prints only the security context of the process:

	$ id -Z
	
- **id -g** prints only the effective group id:

	$ id -g
	
- **id -G** print all group Ids:

	$ id -G

Resources
---------

- [man7.org](http://man7.org/linux/man-pages/man1/id.1.html)
