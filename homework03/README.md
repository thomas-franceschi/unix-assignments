Homework 03
===========

Activity 01:
------------

1 
   a. libgcd.so is larger because it is shared, so it contains all of the code 
   from the library so that it can be inserted into the program at runtime
   
   b. gcd-static is much larger because it contains the entire library needed
   to run, whereas gcd-dynamic does not use the library until run-time, keeping 
   the executable file much smaller.
   
2  gcd-static does not depend on any libraries because its a static program, we can 
   see this by looking at the flags used to compile it. Since gcd-dynamic is 
   dynamically compiled using shared libraries, we can use the ldd command 
   
    $ ldd gcd-dynamic
    
   to see that gcd-dynamic depends on libgcd.so, linux-vdso.so.1, libc.so.6, and 
   ld-linux-x86-64.so.2.

3  gcd-dynamic did not run because it said it could not find/load libgcd.so 
since it is not in the libraries folder that the computer is set to look in. 
We could set 
    
    $ setenv LD_LIBRARY_PATH to .:$LD_LIBRRARY_PATH
    
where . refers to the current directory.
    
4 
The advantages of static linking are that everything required to run at 
run-time is contained in the executable, so the program can be easily moved 
to other machines and perform the exact same, and is fast at run-time because 
there is nothing to load other than the program itself. The advantages of 
dynamic linking are that it allows for much smaller executable files since the 
necessary libraries are not included in the executable at compile time, allowing 
for faster compiling and the ability to reuse the same library across multiple 
files without copying the same code over and over again. If I were to create an 
application, I would want it to be dynamic by default since it would cut down on 
the size of the application, and as a project grows, shared libraries may be 
implemented multiple times, compunding this space savings. The static gcd program 
is 10 times larger than the dynamic one, and its only a few lines long. If I were 
making a seriously large program like iTunes or Chrome, I would want it to be as 
small as possible, and the extra space taken up by static libraries would be make 
it a comically large file to download.

Activity 02:
------------

1 To extract the is_palindrome.tar.gz archive I navigated to the directory I wanted 
to save it to, then used:

    $ wget https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is_palindrome.tar.gz
    $ tar -xvf palindrome.tar.gz
    
2 I used the -g, -gdwarf-2, and -pg flags to generate the debugging symbols and allow me to check 
for memory leaks and use gdb and valgrind.

    $ ls -lh is_palindrome*
    -rwxrwxr-x 1 thomas thomas  13K Feb  5 21:06 is_palindrome
    -rw-r--r-- 1 thomas dip    1.1K Feb  5 21:06 is_palindrome.c
    -rw-r--r-- 1 thomas dip      27 Jan 31 13:26 is_palindrome.input
    -rwxrwxr-x 1 thomas thomas 8.9K Feb  5 21:07 is_palindrome-normal
    -rw-r--r-- 1 thomas dip      99 Jan 31 13:26 is_palindrome.output

Including those increased the file size from is_palindrome-normal to is_palindrome by 
about 4k, or roughly a 50% increase in executable size. This is due to the inclusion of 
the information being generated so that debuggin can be done.

3 To address the seg fault I ran the program through gdb to find where it hung up and found that 
it was having issues because the buffer size was not being allocated proper size, so I changed it 
to automatically set the array to the size of the buffer. The memory leak was cause by allocated 
memory that was not being freed, which I found out by runing valgrind and checking for mem leaks. 
I addressed this by adding an expression to free the sanitized strings after they were done being 
used and ran the program through valgrind again to ensure that no leaks were possible. The invalid 
memory access occurs when checking the back of is_palindrome, because it originally has it set to 
check the space after the last allocated character. I fixed this by subtracting 1 from the original 
value to ensure it starts within the bounds of the array.

4 The free bug was the hardest to find since it did not involve changing anything that was already in 
the code, but adding something new, and it didn't occur to me for the longest time that allocated memory 
had to be manually freed.

Activity 03:
-------------

1 Contacting the courier:

    $ /afs/nd.edu/user15/pbui/pub/bin/COURIER

He had the following message:Hmm... you sure you put the package in the right place?

2 Find the package location:

    $ strings COURIER
    
The line right above the response he gave me in the strings output, I notcied that he 
checks for a file called 'NETID'.deaddrop in the /tmp folder of the student machine, so 
I went there.

3 Creating the file:

    $touch tfrances.deaddrop
    
I used touch to create a file of the specified format, then returned to the courier.
His repy when I talked to him this time was: Whoa whoa... you can't give everyone access to the package! Lock it down!

4 Locking it down: 

    $ chmod 700 tfrances.deaddrop
    
I used chmod 700 to give myself full rights but to deny rights to all other users, then returned to the courier.
This time he said: What are you trying to pull here?  The package is the wrong size!

5 Getting the right size:

To get the size I ran an strace, filtering for all of the different system calls, eventually narrowing it down to 
a read call as to where I might find the intended size.

    $ strace -e read COURIER
    
There were only two calls, and among the calls was one that checked for a variable to be equal to 832 that currently 
output as false, so I went back to my file and used dd to fill it with 832 bytes of garbage.

    $ dd if=/dev/urandom of=tfrances.deaddrop bs=1 count=832
    
I then went back to the courier and his new response was:
Well, everything looks good... I'm not sure what '�.��gx>E' means, but I'll pass it on

Referring back to the strings output, I noticed this was the last possible line of output 
so I knew I had definitely reached the end of my trail.

I still dont know what �.��gx>E means...