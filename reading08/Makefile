all: report.pdf

report.pdf: report.tex results.png
	pdflatex report.tex

results.png:
	./histogram.plt

clean:
	rm -f report.pdf results.png
