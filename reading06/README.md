Reading 06
==========

1.
    $ echo "All your base are belong to us" | tr [:lower:] [:upper:]
    ALL YOUR BASE ARE BELONG TO 
    
2.
    $ cat /etc/passwd | grep root | cut -d :-f 7
    /bin/bash
    
3.
    $ echo "monkeys love bananas" | sed "s/monkeys/gorillaz/g"
    gorillaz love bananas
    
4.
    $ cat /etc/passwd | sed "s/\/bin\/bash/\/usr\/bin\/python/g" | sed "s/\/bin\/csh/\/usr\/bin\/python/g" | sed "s/\/bin\/tcsh/\/usr\/bin\/python/g"  | grep python
    root:x:0:0:root:/root:/usr/bin/python
    mysql:x:27:27:MySQL Server:/var/lib/mysql:/usr/bin/python
    xguest:x:500:501:Guest:/home/xguest:/usr/bin/python
    condor:x:108172:40:Condor Batch System:/afs/nd.edu/user37/condor:/usr/bin/python
    lukew:x:522:40:Luke Westby temp access:/var/tmp/lukew:/usr/bin/python
    
 5.
    $ echo "     monkeys love bananas" | sed "s/^ *//g"
    monkeys love bananas
 
 6.
    cat /etc/passwd | grep :4'[[:digit:]]' | grep '[[:digit:]]'7:
    rtkit:x:499:497:RealtimeKit:/proc:/sbin/nologin
    qpidd:x:497:495:Owner of Qpidd Daemons:/var/lib/qpidd:/sbin/nologin
    uuidd:x:495:487:UUID generator helper daemon:/var/lib/libuuid:/sbin/nologin
    mailnull:x:47:47::/var/spool/mqueue:/sbin/nologin
 
 7.
    $tails -f FILE
 
 8.
    $comm FILE1 FILE2
 