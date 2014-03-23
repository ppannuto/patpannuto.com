all:
	./website.py
	$(MAKE) -C cv
	mkdir -p html/cv/
	cp -r cv/www/* html/cv/

local:	all
	pushd html && python3.3 -m http.server 8000; popd

deploy:	all
	rsync -av html/ patpannuto.com:www/

.PHONY: all local deploy
