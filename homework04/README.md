Homework 04
===========

Activity 01:
-------------

1.
a) I handled setting variables by declaring them at the top of my script as well as their 
default values using the VAR=value format.

b) I iterated it using a for loop that looped through every file in the current directory 
using the proper suffix by globbing and then using the argument variable as the filename 
when it came time to compile.

c) I handled the verbose variable using the ${VEBOSE:-0} syntax to set its default value to 
zero but allow for it to be changed at runtime to a 1 to enable verbose output.

d) I allowed for early exit by testing for a bad return from the compile function, and if 
it came out false, then it exited

2.
bake is goodfor compiling a bunch of small programs at the same time, and allows to compile 
regardless of name, whereas make is targeted at specific files and you need to go into the 
make file to change which source code it compiles, but it is better for compiling more complex
programs with multiple dependencies.

Activity 02:
------------
 1.
 a) I parsed the command line argument using the getopts command in a whileloop to take in 
 all of the flags and return values for variables associated with each flag. 
 
 b) I handled the case of no command line argument by only running the commands when arguments 
 are present, just ending the program if it detects no arguments.
 
 c) I processed each directory argument by including the -a argument for the du command when 
 the -a flag is called at runtime
 
 d) I incorporated the command line arguments to print the top N lines by piping the du output
 to the head command using N as the number input after the -n flag as the argument to restrict 
 the number of entries printed
 
 2.
 The hardest part about writting this script was incorporating the number of lines after the -n 
 flag into the commands to ensure it didn't take it as just another variable. The taking in of 
 the flags and parsing the input took up the bulk of my code which was surprising because I 
 thought that incorporating the different output option commands would take more code to implement.
 
 Activity 03:
 ------------
 
 1.
 a) I handled different signals using the trap function and declaring a different trap and command 
 to be run for each signal received.
 
 b) I passed along messages to cowsay by using a different call to cowsay in each trap and typing 
 what to output in the speach bubble immediately after the cowsay call
 
 c) I handled timeout by putting a 10 second sleep call after all of my traps that displayed a taunt 
 cowsay if there was no signal received for 10 seconds.
 
 2.
 
 I prefer writing c commands to shell scripts because it is very easy to include functions from 
 libraries, whereas in shell scripting alot of functions such as sleep and cowsay must be present on 
 the current machine in a specified path for it to execute properly. C code is much more portable and 
 the syntax makes much more sense to me. It also seems more flexible in the things you can do within 
 the program, whereas shell scripting seems much more flexible for altering other files on the machine 
 it is being run on. You would use a cprogram when you need to ensure it can run on any machine and if
 it doesnt require altering many sytem files. You would use shell scripting for when you need to automate 
 command line processes and other functions.