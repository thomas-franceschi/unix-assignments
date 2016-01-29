Homework 02
===========




(Add this to other commit)
---------------------------


3. The disk usage on the destination machine is 4.0 k

4. 
   # command to use sftp
    $ sftp < command.txt tfrances@remote202.helios.nd.edu

   # command to use rsync
    $ rsync /tmp/tfrances--workspace/data* tfrances@remote203.helios.nd.edu:/tmp/tfrances--workspace

5. When using scp and sftp multiple times, the entire file is sent and 
overwritten every time, whereas with rsync, only the modified section of 
the file is transfered each time. This features is useful because if you 
have extremely large directories that need to be updated across multiple 
servers, instead of recopying every file to sync them, you can save time 
by only copying over the files that are modified and not touch the files 
that are unchanged.

6. I preffer rsync because it has an easy syntax like sftp for transering 
multiple files at once, and it is the quickest if you are just updating a 
few files in a large directory.