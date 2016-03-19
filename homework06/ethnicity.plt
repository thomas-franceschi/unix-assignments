set xtics rotate out
set yrange [0:120]
set style data histogram
set style histogram cluster
set style fill solid border
set terminal png size 550,550
set output "ethnicity.png"
plot for [COL=2:8] 'ethnicity.dat' using COL:xticlabels(1) title columnheader


