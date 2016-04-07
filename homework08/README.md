Homework 08
===========

Activity 1:
-----------

1. The role of the parent process is to watch the operation of the child as it executes the given 
command. The parent accomplishes its task using os.wait and sigchld to monitor if it is still 
running or not. The child uses low level system calls to execute the command given as an argument.

2. The timeout mechanism worked by using an alarm that counted down from a set time and if 
the proccess had not ended itself by the time the alarm was up, it was sent a SIGINT and 
the child was killed.

3. The test script verifies the correctness of the program by running two while loops, one 
for a set of tests that are supposedto exit succesfully, and a set that are supposed to fail. 
Both iterate an integer N and use it as the wait time. For the first set, it runs the script 
with the given wait time and if it fails, it outputs "test failed" and exits. If every test 
in the loop is done successfully, it prints out a successmessage and moves on to the second 
loop. The second loop does the same thing, but exits if any test is run successfully ( as they 
should all fail), if not then it prints a success message and moves on. It tests both the -v and 
-h flags by capturing the output to stderr from each in seperate instances to a variable string 
and then checks to see if the string is empty. If the string is empty then it didn't output 
properly and it returns a failure message and exits the test. If the string is not empty then 
output was correctly sent to stderr, it displays a success message, and moves on to the next test.

4. When you set seconds and the sleep argument to the same duration as the command it throws an 
error because everything times out at the same time the parent dies and since the parent takes 
precedence over the child the program isnt sure if there is a child to kill when it goes to 
terminate the child process

Activity 2:
----------

3. What data structure did you use to help detect changes to files and the logic 
you used determine if a file was new or modified.

1. I scanned the filesystem to ensure I checked the files in specific directories by using a 
directories variable and starting there and walking all of the sub-directories in a function, 
then using another function to check each individual file against the rules.

2. I loaded the rules using a yaml file with a specified path, opening a stream to it, loading its 
contents into a variable, then using the extracted information as the pattern to be checked against 
in the functions for mathcing files.

3. I used a dictionary to help detect changes to files and in order to determine if they were new or 
modified I checked the modified time on each file against the epoch time when the program started and 
if it was greater than (ie more recent) then the file must have been modified.

4. I executed each action by taking the action command from the yaml data and making it a variable, 
then forking the process and executing a system call that runs it with execvp.

5. Busy waiting means that the programcontinues looping even when there is nothing to do. Under the 
context of rorschach.py, this is when it is just watching the files and not executing any commands. 
Busy waiting is not good because it wastes processor time and power that could be used on other 
processes. This challenge could be alleviated by using system calls to block the processfrom running 
until it is needed again, or to use a sleep timer so it runs on a consistent interval.

Cache invalidation is when cache entries are explicitly deleted. This is useful because with rorschach.py 
we are traversing a large number of files and as the number grows it may slow the system as it tries 
to keep track of all of them. It could be implemented as a simple purge after each search cycle, or to 
refresh the cache with each cycle.