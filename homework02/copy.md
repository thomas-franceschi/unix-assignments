Homework 02
===========
Thomas Franceschi
tfrances

1. 
	#create workspace on source machine
	$ mkdir /tmp/tfrances--workspace
	
	#Generate 10MB file of random data
	$ dd if=/dev/urandom of=10MB bs=10M count=1
	
	#create 10 hardlinks to 10MB file
	$ ls 10Mb data0
	$ ls 10Mb data1
	$ ls 10Mb data2
	$ ls 10Mb data3
	$ ls 10Mb data4
	$ ls 10Mb data5
	$ ls 10Mb data6
	$ ls 10Mb data7
	$ ls 10Mb data8
	$ ls 10Mb data9
	
	#create workspace on target machine
	$ ssh tfrances@remote203.helios.nd.edu
	$ mkdir /tmp/tfrances--workspace
	
2. 
	$ du /tmp/tfrances--workspace
	10244

The total disk usage is 11MB.	
I find this surprising because when ls -l is run, it says there are 110MB used, not 11.

3.




$ nmap -Pn -p9000-10000 xavier.h4x0r.space

Starting Nmap 5.51 ( http://nmap.org ) at 2016-01-29 10:27 EST
Nmap scan report for xavier.h4x0r.space (129.74.161.24)
Host is up (0.00085s latency).
Not shown: 997 closed ports
PORT      STATE    SERVICE
9097/tcp  open     unknown
9111/tcp  open     DragonIDSConsole
9876/tcp  open     sd
10000/tcp filtered snet-sensor-mgmt


 wget 129.74.161.24:9111
--2016-01-29 10:34:10--  http://129.74.161.24:9111/
Connecting to 129.74.161.24:9111... connected.
HTTP request sent, awaiting response... 200 No headers, assuming HTTP/0.9
Length: unspecified
Saving to: “index.html.1”

    [ <=>                                                ] 3,067       --.-K/s   in 0s

2016-01-29 10:34:10 (215 MB/s) - “index.html.1” saved [3067]


 wget 129.74.161.24:9876
--2016-01-29 10:35:16--  http://129.74.161.24:9876/
Connecting to 129.74.161.24:9876... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1763 (1.7K) [text/html]
Saving to: “index.html.2”

100%[===================================================>] 1,763       --.-K/s   in 0s

2016-01-29 10:35:16 (79.6 MB/s) - “index.html.2” saved [1763/1763]

cd ~pbui/pub/oracle/tfrances/

base64 -d code
dc8975c04842399a9f567b9354f57143

curl xavier.h4x0r.space:9876/tfrances/dc8975c04842399a9f567b9354f57143

 _________________________________________
/ Ah yes, tfrances... I've been waiting   \
| for you.                                |
|                                         |
| The ORACLE looks forward to talking to  |
| you, but you must first retrieve a      |
| secret message from the SLEEPER.        |
|                                         |
| He can be found in plain sight at       |
| ~pbui/pub/oracle/SLEEPER... You will    |
| need to wake him up and then signal him |
| to HANGUP his connection. If he         |
| recognizes you, he will give you the    |
| message in coded form.                  |
|                                         |
| Once you have the message, proceed to   |
| port 9111 and deliver the message to    |
| the ORACLE.                             |
|                                         |
| Hurry! The ORACLE is wise, but she is   |
\ not patient!                            /
 -----------------------------------------
  \
   \          .
       ___   //
     {~._.~}//
      ( Y )K/
     ()~*~()
     (_)-(_)
     Luke
     Sywalker
     koala

cd ~pbui/pub/oracle

$ SLEEPER &
[1] 15323

kill -1 15323


$ telnet xavier.h4x0r.space 9111
Trying 129.74.161.24...
Connected to xavier.h4x0r.space (129.74.161.24).
Escape character is '^]'.
 ________________________
< Hello, who may you be? >
 ------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
NAME? tfrances
 ___________________________________
/ Hmm... tfrances?                  \
|                                   |
| That name sounds familiar... what |
\ message do you have for me?       /
 -----------------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
MESSAGE? Z3NlbmFwcmY9MTQ1NDA4MzQ3NA==
 ______________________________________
/ Ah yes... tfrances!                  \
|                                      |
| You're smarter than I thought. I can |
| see why the instructor likes you.    |
|                                      |
| You met the SLEEPER about 5 minutes  |
\ ago... What took you so long?        /
 --------------------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
REASON? I was looking up the syntax for telnet
 ______________________________________
/ Hmm... Sorry, kid. You got the gift, \
| but it looks like you're waiting for |
| something.                           |
|                                      |
| Your next life, maybe. Who knows?    |
\ That's the way these things go.      /
 --------------------------------------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||

Congratulations tfrances! You have reached the end of this journey.

