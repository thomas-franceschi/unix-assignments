#!/usr/bin/gnuplot

set xrange [0:7]
set yrange [0:200]
set style fill solid
set boxwidth 0.8
set grid
set terminal png size 800,600 enhanced font "Helvetica,20"
set output "results.png"
plot "results.dat" with boxes
