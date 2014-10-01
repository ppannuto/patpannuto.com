all: pannuto.pdf

pannuto.pdf: pannuto.tex conf.bib workshop.bib posterdemo.bib
	pdflatex pannuto.tex
	biber pannuto
	pdflatex pannuto.tex
	pdflatex pannuto.tex

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg *.out
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -f *.xml *.bcf

.PHONY: clean
