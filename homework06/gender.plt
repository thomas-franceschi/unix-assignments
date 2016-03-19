set xtics rotate out
set yrange [0:100]
set style data histogram
set style histogram cluster
set style fill solid border
set terminal png size 550,550
set output "gender.png"
plot for [COL=2:3] 'gender.dat' using COL:xticlabels(1) title columnheader
