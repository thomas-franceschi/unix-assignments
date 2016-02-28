//Thomas Franceschi
//awk.md
//2/28/2016

1. Printing specific fields.

	$ awk '/line_with_this_text/' {print} /path/to/file

2. Modifying FS to control input field separator.

	$ awk 'BEGIN { FS=":"; }
	{ print $2; }' /path/to/file

3. Using BEGIN and END.

	$ awk 'BEGIN { FS=":"; }
	{ print $1; print $3; print "nobody cares about $2" }
	END{ print "Its over" }'


4. Using pattern matching.

	$ awk '/^Thomas/' names.txt

5. Using special variables such as NF and NR.

	awk 'NR <= 2' /path/to/file

6. Using associative arrays.


	awk 'BEGIN { item[""]=0;}
	{item[$2]++;}
	END {for (i in username) {if (i != "") {print username[i], i;} } }'
