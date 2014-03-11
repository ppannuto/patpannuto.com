all: pannuto.pdf www/pannuto.html ../cv.tar.gz

pannuto.pdf: pannuto.tex *.bib
	pdflatex pannuto.tex
	bibtex pannuto
	pdflatex pannuto.tex
	pdflatex pannuto.tex

pannuto: pannuto.tex *.bib
	latex2html -split 0 -no_navigation -info 0 -image_type png pannuto.tex

www/:
	mkdir -p www

www/pannuto.html: pannuto.tex *.bib www/
	htlatex pannuto.tex "html" "" "-dwww/"
	bibtex pannuto
	htlatex pannuto.tex "html" "" "-dwww/"
	htlatex pannuto.tex "html" "" "-dwww/"

../cv.tar.gz: pannuto.pdf www/pannuto.html
	cd ../ && tar -czf cv.tar.gz cv/

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -rf www/
	rm -rf pannuto/
	rm -f ../cv.tar.gz

.PHONY: clean
