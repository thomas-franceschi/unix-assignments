Homework 08
===========

Activity 1:
-----------

1. 

2.

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

4.