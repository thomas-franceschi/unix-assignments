#!/bin/sh

col=1
year=2013

echo "Year	Men	Women"> gender.dat
while [ $year -lt 2019 ];do
	cat demographics.csv | cut -d ',' -f $((2*col-1)) | grep '[MF]' | awk -v year=$year '{gender[$1]++} 
		END{printf("%d	%d	%d\n",year , gender["M"], gender ["F"])}' >> gender.dat
	year=$((year+1))
	col=$((col+1))
done
