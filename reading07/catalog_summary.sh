#!/bin/sh

: ${PAGE:="http://catalog.cse.nd.edu:9097/query.text"}

if [ $1 ]
	then
	PAGE=$1
fi

curl -s $PAGE | awk 'BEGIN { numcpu=0; numname=0; proliftype=0; }
	/cpus/ { numcpu+=$2 }
	/name/ { name[$2]++ }
	/type/ { typecount[$2]++ }

	END { {print "Total CPUs:",numcpu }
	{for (i in name) numname++; print "Total Machines:",numname}
	{for(i in typecount) if (proliftype < typecount[i]) proliftype=typecount[i]}
	{for(i in typecount) if (proliftype == typecount[i]) print "Most Prolific Type:", i} }'
