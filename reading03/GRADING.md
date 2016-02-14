Reading 03 - Grading
====================

**Score**: 3.5 / 4
 
Deductions
----------
-.5: the answer to 1 is strings
-0: you forgot the dependencies in your makefile! it should look like this:
all: hello-dynamic hello-static hello-debug hello-profile

hello-dynamic: 	hello.c
	gcc -o hello-dynamic hello.c

hello-static: 	hello.c
	gcc -static -o hello-static hello.c

hello-debug: 	hello.c
	gcc -g -o hello-debug hello.c

hello-profile: 	hello.c
	gcc -pg -o hello-profile hello.c

clean:
	rm -f hello-*


Comments
--------


