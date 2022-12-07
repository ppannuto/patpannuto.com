all: pannuto.pdf

pannuto.pdf: pannuto.tex books.bib conferences.bib workshops.bib journals.bib posterdemo.bib biblatex.cfg | clean
	pdflatex pannuto.tex
	biber pannuto
	pdflatex pannuto.tex
	@echo; echo; echo $$(tput bold)Last Run$$(tput sgr0); echo; echo
	pdflatex pannuto.tex

pannuto.tex: latex_gen.py awards.toml
	./latex_gen.py

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg *.out
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -f *.xml *.bcf

.PHONY: clean all
