#!/bin/sh


col=1
date=2013

echo "Year	Caucasian	Oriental	Hispanic	African_American	Native_American	Multiple_Selection	Undeclared"> ethnicity.dat
while [ $date -lt 2019 ];do
        cat demographics.csv | cut -d ',' -f $((2*col)) | grep '[COSBNTU]' | awk -v year=$date '{ethnicity[$1]++} 
                END{printf("%d	%d	%d	%d	%d	%d	%d	%d\n",year , ethnicity["C"], ethnicity["O"], ethnicity["S"], ethnicity["B"], ethnicity["N"], ethnicity["T"], ethnicity["U"])}' >> ethnicity.dat
        date=$((date+1))
        col=$((col+1))
done

