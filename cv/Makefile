all: pannuto.pdf

GENS := gen/awards.tex gen/teaching.tex gen/service.tex gen/advising.tex
BIBS := books.bib conferences.bib workshops.bib journals.bib posterdemo.bib

pannuto.pdf: pannuto.tex $(GENS) $(BIBS) biblatex.cfg
	pdflatex pannuto.tex
	biber pannuto
	pdflatex pannuto.tex
	@echo; echo; echo $$(tput bold)Last Run$$(tput sgr0); echo; echo
	pdflatex pannuto.tex

gen/%.tex: %.toml latex_gen.py
	./latex_gen.py


clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg *.out
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -f *.xml *.bcf

.PHONY: clean all
