Homework 07
===========

1. I handled parsing the command line options by running through the arguments, creating 
lists that stored the flags being used, as well as the value each one is set to, then 
using a series of if statements to set the corresponding variable values.

2. I walked the directory tree using the os.walk low-level command for the root as well as all 
files and directories. Within that loop is another loop that goes through all of the files and 
directories within the current directory, so it runs until there are no more directories to 
traverse. Within that loop the include function runs that decides which files to display.

3. I determined whether or not to print an objects filepath using the large include function 
that checks for all of the flags and uses them to filter out which filepaths to print based on 
the if statements within them.

4. My find.py script has 4000 calls to stat and 4 to lstat when run on the /etc directory.
When I strace the find command on the /etc directory on my ubuntu machine there are zero calls 
to either stat or lstat. The find command, however, calls fstat 394 times. It also calls fchdir 
779 times. My guess is it is getting file information by traversing the directories and checking 
the filtype of each file before moving on to the next directory.