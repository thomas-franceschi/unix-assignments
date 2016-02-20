#!/bin/sh

PATH=/afs/nd.edu/user15/pbui/pub/bin/cowsay
SLEEPPATH=/bin/sleep

$PATH hey buddy

trap '$PATH bitch you got me fucked up!; exit' SIGINT

trap '$PATH You tryna fight dirty?!?! get outta here!; exit' SIGTERM

trap '$PATH I see you bae, hmu with the code KJFHLKSJDGHLA; exit' SIGHUP

$SLEEPPATH 10

$PATH "You SNOOZE you lose ;)"
