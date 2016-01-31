Reading 03
==========

1. 

2. 

    $ ldd /bin/ls
    
3. 

    $ strace ls
    
4. 

    $ make hello-debug
    $ gdb a.out
    
Then use the different gdb commands to step through the program, check 
values of variables, etc.

5. 

    $ valgrind --leak-check=yes ./a.out
    ==11315== Memcheck, a memory error detector
    ==11315== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
    ==11315== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
    ==11315== Command: ./a.out
    ==11315== 
    Hello, World!==11315== 
    ==11315== HEAP SUMMARY:
    ==11315==     in use at exit: 0 bytes in 0 blocks
    ==11315==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
    ==11315== 
    ==11315== All heap blocks were freed -- no leaks are possible
    ==11315== 
    ==11315== For counts of detected and suppressed errors, rerun with: -v
    ==11315== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
    
6. 

    $ make hello-profile
    $ ./a.out //generates gmon.out file
    $ gprof a.out