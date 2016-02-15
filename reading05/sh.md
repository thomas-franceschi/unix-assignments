1. Variables
------------
- all variables use a $ before them
- you can use environmental variables that the system already has
    
    $echo $PATH
    
- must declare variables before using them

    x = 2
    echo $x
    
2. Capturing STDOUT
--------------------

- You can redirect STDOUT to a text file using the > character and 
specifying the target file after it

    $ ./hello.sh > hello.txt
    
3. **if** Statement
---------------------
- if commands execute based on the exit status of other commands. If the 
command exits succesfully, the next command will run.

    if echo "hello"; then
    echo "goodbye"
    fi
    
4. Case statement
------------------
- case statements check the value of a variable and run a specific line 
depending on the value of that variable. * can be used to glob together 
any "other" options you don't specify

    $ case $var in
    $    a ) echo "letter a"
    $        ;;
    $    b ) echo "letter b"
    $        ;;
    $    * ) echo "not a or b"
    $ esac


5. **for** loop
----------------
-for loops execute the commands inside of them until it cycles through all 
of the variables in the **in** statement

    $ for letter in a b c d; do
    $    echo $letter
    $ done

6. **while** loop
-----------------
- a while loop exectutes the commands inside of it until the variable 
reaches a specified value

    $ count = 0
    $ 
    $ while [ "$count" -lt 5 ]; do
    $    echo "Count = $count"
    $    count=$((count + 1))
    $ done

7. function
-------------
- A shell function is essentially a script within a script, allowing you 
to execute a set of commands with one call which is useful if executing 
the same set of commands multiple times in a single script. You can execute 
a function by calling  it like anormal variable within the same script it is 
defined in.

    $ say_hello {
    $    echo "hello peter"
    $    echo "hello tijana"
    $ }
    $
    $
    $
    $
    $ $(say_hello)
    $ $(say_hello)



8. trap
----------
- trap allows you to execute a given command when your script receives a 
signal (does not work for SIGKILL (9))

    trap "echo goodbye; exit" SIGHUP SIGINT SIGTERM
