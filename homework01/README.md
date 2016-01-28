Homework 01
===========
Thomas Franceschi
tfrances

**Excercise 1:**
----------------
1)

    $ cd /afs/nd.edu/user14/csesoft
    
2) 
 
    $ cd ../../user14/csesoft
    
3) 
 
    $ cd ~/../../user14/csesoft
    
4) 
 
    $ ln -s /afs/nd.edu/user14/csesoft
    
**Excercise 2:**
----------------
1) 

    $ mkdir ~/image
    $ cp -r /usr/share/pixmaps/* ~/images
    
2) Yes, I know because when I used the $ ls -l command the names of certain links are red with black backgrounds 
(on my ubuntu machine), which corresponds to a broken symlink. I
think they are broken because the objects they point to no longer
exist.

3)
 
    $ time cp images pixmaps  
    0.000u 0.000s 0:00.00 0.0%	0+0k 0+0io 0pf+0w
    
4) 

    $ time cp pixmaps /tmp/tfrances-pixmaps
    0.003u 0.047s 0:01.14 3.5%	0+0k 0+4800io 0pf+0w
    
This operation is slower because it is actually making new copies of 
the files to a new location on the disk, not just renaming the directory 
they are in.

5)

    $ time rm -r /tmp/tfrances-pixmaps
    0.000u 0.007s 0:00.02 0.0%	0+0k 0+0io 0pf+0w
    
This command is much faster than the copy one because instead of moving 
files from one location to another, it simply has to remove them from a 
single location.

**Exercise 3:**
---------------
1)

    $ ls -lh /afs/nd.edu/user37/ccl/software

2)

    $ ls -lt /afs/nd.edu/user37/ccl/software
    
3) 

    $ cd /afs/nd.edu/user37/ccl/software/cctools/x86_64
    $ ls -1R | wc -l
    2199
Using the -R flag recursively prints all of the contents of each 
subdirectory and -1 lists them all on an individual line, which is then 
piped to the wc -l function that counts the number of lines printed, 
which corresponds to the number of files.

4)

    $ cd /afs/nd.edu/user37/ccl/software/cctools/x86_64
    $ find . -name weaver
It does contain weaver.

5)
 
    $ cd /afs/nd.edu/user37/ccl/software/cctools/x86_64
    $ du -sh *
    23M	osx-10.9
    77M	redhat5
    72M	redhat6
redhat5 is the largest subdirectory by size. The du command lists the disk 
usage and the -s flag puts it in list form and the -h uses human readable 
file sizes. The * ensures that each subdirectory is counted individually.

6) 

    $ cd redhat5
    $ ls -1R | wc -l
    858
I moved to the largest directory then used the same ls and wc commands and 
flags to determine the number of files in that specific directory.

7)

    $ find . -printf '%s %p\n' | sort -nr | head -1
    18534130 ./redhat5/bin/parrot_run_hdfs

8) 

    $ find . -mtime +30 | wc -l
    2026
    
**Exercise 4:**
---------------
1)The user and members of that user's group can read it, but no other users

2) 

    a. $ chmod 600 data.txt
    b. $ chmod 770 data.txt
    c. $ chmod 444 data.txt
    d. $ chmod 000 data.txt
    
3) If there are no permissions on a file, only the root user can delete it.

**Exercise 5:**
---------------
1)
 
    $ fs listacl /afs/nd.edu/user19/tfrances
    Access list for /afs/nd.edu/user19/tfrances is
    Normal rights:
    nd_campus l
    system:administrators rlidwka
    system:authuser l
    tfrances rlidwka
    
    $ fs listacl /afs/nd.edu/user19/tfrances/Private
    Access list for /afs/nd.edu/user19/tfrances/Private is
    Normal rights:
    system:administrators rlidwka
    tfrances rlidwka

    $ fs listacl /afs/nd.edu/user19/tfrances/Public
    Access list for /afs/nd.edu/user19/tfrances/Public is
    Normal rights:
    nd_campus rlk
    system:administrators rlidwka
    system:authuser rlk
    tfrances rlidwka
These three access control lists (ACLs) show who has permissions for each 
folder. For my main folder: members of nd_campus can only look up files, 
administrators and myself have full rights. For my private folder: Only 
myself and administrators have full rights, and nobody else has any access.
For my public folder: Anyone in nd_campus can read, lookup, and lock files, 
as well as authorized users, and and myself and administrators both have full 
access rights.

2)

    $ fs listacl /afs/nd.edu/common
    Access list for /afs/nd.edu/common is
    Normal rights:
    nd_campus rl
    system:administrators rlidwka
    system:authuser rl
 Anyone in nd_campus can read and look up, as well as any authorized users, 
 but admins have full access. 
 
    $ touch /afs/nd.edu/common/tfrances.txt
    touch: cannot touch `/afs/nd.edu/common/tfrances.txt': Read-only file system
I was unable to create a file becuase I only have read access to this file 
system, not write privelidges.

3)
 
    $ fs setacl -dir /afs/nd.edu/user19/tfrances/shared_folder -acl instructor read
    
**Exercise 6:**
---------------
1)
 
    $ umask 000
    $ touch world1.txt
    
2)
 
    $ umask 022
    $ touch world2.txt
    
3)
 
    $ umask 044
    $ touch world3.txt
    
    $ ls -l
    -rw-rw-rw- 1 tfrances dip 0 Jan 22 21:29 world1.txt
    -rw-r--r-- 1 tfrances dip 0 Jan 22 21:29 world2.txt
    -rw--w--w- 1 tfrances dip 0 Jan 22 21:29 world3.txt
    
The permissions of the three files are different because of the masks 
applied to each one, which affect the permissions given when creating 
files. A 000 mask gives all users the normal permissions for each file 
type. The 022 removes the write permissions from the user's group and 
other users, but not the user that created it. The 044 mask only removes 
read permissions from those same groups, but once again not the user that 
created it. Umask applies a general rule about permissions on newly created 
files based on the three numbers of the argument. This is useful because 
if you are working on a project with many files that require the same special 
permisions it saves the time from having to alter the individual permissions 
of each file and instead a mask can be applied before all of the files are 
created and then reverted back to normal permissions when done.
