Homework 05
===========

Activity 1:
----------

1. I constructed the source set by initializing 2 variables containing the set of the alphabet
as all uppercase and lowercase letters.

2. I constructed the target set by using the cut command twice and the key value to split the 
alphabet right at they key letter. Everything before the key value is placed in a $back variable 
and everything after it is placed in a $front variable. I then used echo to concatenate them 
together as the $target variable so the whole aphabet is in the target but it is now properly 
augmented. I repeated the same to create the all caps target.

3. I used both of these sets to perform the encryption by using tr and piping in the phrase from 
standard input. For tr I used the source set as the first argument and the target set as the second 
argument so that every letter in the statement is replaced by its corresponding letter in the 
shifted target set. I then piped it into another tr command that does the same with all of the 
capital letters.

Activity 2:
-----------

1. I filtered URLs and extracted only the useful portion by using grep to filter for every line 
containing the phrase "url": and sed to remove all of the whitespace so they all lined up neatly.

2. I handled the different ordering by using flags and different if statements to append a different 
sorting command for the sed output to be piped into such as head, shuf, and sort before outputting it.

3. The -r flag uses the shuf command to randomize the order of the urls as they are output to stdout.
-n takes in a number as an argument and displays that number of urls as they come in. -s sorts the urls 
alphabetically before it outputs them to stdin.

Activity 3:
------------

1. I removed comments by using sed to search for any string begining with the $CHAR value, which is the 
"comment character" and replacing it with nothing (deleting it).

2. I removed empty lines by creating a function that the sed output is piped into and if the flag is enabled 
it uses sed to replace any lines that contain only white space with nothing (deleting it).

3. The -d flag followed by a character sets the comment character to whatever the command line character is 
given after the -d flag, which is useful for broifying multiple languages. The -W flag is used to not delete 
blank lines. It works by setting the flag variable to 1 so that when the del_whitespace function is called the 
if statement returns false and it skips the sed command which would delete the whitespace and just outputs the 
file with the removed comments.