TLDR - git
==========

Overview
--------

[Git] is a distributed version control system.

Examples
--------

- **Clone** a remote *repository*:

        $ git clone git@bitbucket.org:CSE-20189-SP16/assignments.git
        
- **Status** is used to determine which files are in which state:

        $ git status
        On branch master
        nothing to commit, working directory clean
        
- **Add** to begin tracking new files:
        
        $ git add README
        
- **Tag** to mark or find *release points*:

        $ git tag -a v1.0 -m "version 1.0"
        
- **Push** to manually push new tags to remote servers:

        $ git push origin v1.0

Resources
---------

- [Pro Git](https://git-scm.com/book/en/v2)

[git]: https://git-scm.com/
