all: pannuto.pdf

pannuto.pdf: pannuto.tex conf.bib workshop.bib posterdemo.bib
	pdflatex pannuto.tex
	bibtex J.aux
	bibtex C.aux
	bibtex W.aux
	bibtex PD.aux
	pdflatex pannuto.tex
	pdflatex pannuto.tex

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg *.out
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref

.PHONY: clean
