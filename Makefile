all:
	./website.py
	$(MAKE) -C cv
	mkdir -p html/cv/
	cp cv/pannuto.pdf static/cv/

local:	all
	pushd html && python3 -m http.server 8000; popd

deploy:	all
	rsync -av html/ patpannuto.com:www/

.PHONY: all local deploy
