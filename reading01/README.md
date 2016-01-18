Reading 01
==========

1. To create a file **private** that is only readable to me I would 
first use touch to create a new file

    $ touch private
    
Then I would use chmod to alter the priveleges so that only I could access 
and alter it

    $ chmod 700 private
    
2. To create a link to /afs/nd.edu/coursesp.16/cse/cse20189.01 in my home 
directory I would first ensure I was in my home directory then use ln -s 
to create a symbolic link 

    $ ln -s /afs/nd.edu/coursesp.16/cse/cse20189.01 cse20189.01
    
3. To determine the size of a file named BigFile, I would navigate to 
its directory and us ls -l to list its information

    $ ls -l BigFile
    
4. To determine the size of directory named MyFolder, I would navigate to 
its parent directory and us ls -l to list its information

    $ ls -l MyFolder
    
5. 
    $ kill -9 25263
    
6. I would use grep to pull all of the numbers of the processes whose 
names containt "urxvt" and pipe that list to the kill command

    $ kill -9 `ps -ef | grep urxvt | grep -v grep | awk '{print $2}'`
    
7. Run the time command on the program

    $ time simulation
    
8. To peersistently change the default editor open the .bashrc file and 
edit the **export** "EDITOR" line
    $vim ~/.bashrc
    export EDITOR=vim