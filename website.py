#!/usr/bin/env python3
# vim: set noet ts=4 sts=4 sw=4:

import sys,os
from sh import mkdir

# Yay OS X vs Linux
try:
	from sh import gcp as cp
except ImportError:
	from sh import cp

import jinja2 as jinja
import markdown
import titlecase

import logger
import publications

jinja_env = jinja.Environment(loader=jinja.FileSystemLoader('templates'))

header_tmpl = jinja_env.get_template('header.html')
header_class_tmpl = jinja_env.get_template('header_class.html')
footer_tmpl = jinja_env.get_template('footer.html')

pubs_groups   = publications.init(jinja_env)

mkdir('-p', 'html')

def md_to_html(src_path, dst_path, md_file):
	page = os.path.splitext(md_file)[0]
	with open('html/{}.html'.format(os.path.join(dst_path, page)), 'w') as o:
		logger.info('Processing ' + md_file)
		content = markdown.markdown(open(os.path.join(src_path, md_file)).read(),
				extensions=['extra', 'toc'])
		o.write(header_tmpl.render(active_page=page, content=content))

for md in os.listdir('pages'):
	if md[-3:] == '.md':
		md_to_html('pages', '/', md)

def class_md_to_html(src_path, dst_path, md_file, meta):
	page = os.path.splitext(md_file)[0]
	with open('html/{}.html'.format(os.path.join(dst_path, page)), 'w') as o:
		logger.info('Processing ' + md_file)
		content = markdown.markdown(open(os.path.join(src_path, md_file)).read(),
				extensions=['extra', 'toc'])
		title = '{} - {} {}'.format(meta['course'].upper(), meta['quarter'], meta['year'])
		title = titlecase.titlecase(title)
		o.write(header_class_tmpl.render(content=content, title=title))


static_extensions = [
		'.css', '.js', '.ico', '.ttf', '.eot', '.svg', '.woff',
		'.png', '.jpg', '.pdf', '.pptx', '.doc', '.txt', '.gz',
		'.tgz', '.otf', '.odp', '.webmanifest', '.xml', '.zip',
		]


print('Process classes')
for year in os.listdir('classes'):
	print('  Process', year)
	mkdir('-p', os.path.join('html', 'classes', year))

	for quarter in os.listdir(os.path.join('classes', year)):
		print('    Process', quarter)
		mkdir('-p', os.path.join('html', 'classes', year, quarter))

		for course in os.listdir(os.path.join('classes', year, quarter)):
			print('      Process', course)
			mkdir('-p', os.path.join('html', 'classes', year, quarter, course))

			for filename in os.listdir(os.path.join('classes', year, quarter, course)):
				# Skip hidden
				if filename[0] == '.':
					continue

				if filename[-3:] == '.md':
					print('        Process', filename)
					path = os.path.join('classes', year, quarter, course)
					meta = {
							'year': year,
							'quarter': quarter,
							'course': course,
							}
					class_md_to_html(path, path, filename, meta)

				# Hacks on hacks on hacks
				ext = os.path.splitext(filename)[1]
				if ext in static_extensions:
					# These do not need to be compiled in any way
					# Just copy them
					print('        Copy', filename)
					cp('-u',
							os.path.join('classes', year, quarter, course, filename),
							os.path.join('html', 'classes', year, quarter, course)
							)

logger.info('Building publications database...')
publications.generate_publications_page(pubs_groups, jinja_env)

# Put all static content in the html folder
logger.info('Copying static content...')
for dirpath,dirnames,filenames in os.walk('static'):

	# Create the mirrored folders in the html directory
	if len(dirnames) > 0:
		for dirname in dirnames:
			path = os.path.join(dirpath, dirname)
			path = 'html' + path[6:] # now that there is a hack
			mkdir('-p', path)


	if len(filenames) > 0:
		for filename in filenames:
			ext = os.path.splitext(filename)[1]

			spath = os.path.join(dirpath, filename)
			dpath = 'html' + spath[6:]
			if ext in static_extensions:
				# These do not need to be compiled in any way
				# Just copy them
				#
				# n.b. this assumes linux-like cp (gcp import)
				cp('-u', '--reflink=auto', spath, dpath)
			else:
				logger.debug('Skipping file: ' + spath)
