all: report.pdf

report.pdf: report.tex ethnicity.png gender.png
	pdflatex report.tex

ethnicity.png:
	gnuplot ./ethnicity.plt

gender.png:
	gnuplot ./gender.plt

clean:
	rm -f report.pdf ethnicity.png gender.png


