#!/usr/bin/env python3
# vim: set noet ts=4 sts=4 sw=4:

import sys,os

import sh
from sh import convert, mkdir, pushd
from sh.contrib import git

# Yay OS X vs Linux
try:
	from sh import gcp as cp
except ImportError:
	from sh import cp

# n.b. remaining imports in __main__ gaurd below

def md_to_html(src_path, dst_path, md_file):
	page = os.path.splitext(md_file)[0]
	with open('html/{}.html'.format(os.path.join(dst_path, page)), 'w') as o:
		logger.info('Rendering ' + md_file)
		content = markdown.markdown(open(os.path.join(src_path, md_file)).read(),
				extensions=['extra', 'toc', 'md_in_html',
					ImgToPictureExtension()])
		o.write(header_tmpl.render(active_page=page, content=content))

def class_md_to_html(src_md, dst_html, meta):
	with open(dst_html, 'w') as o:
		logger.info('Rendering {}'.format(dst_html))
		content = markdown.markdown(open(src_md).read(), extensions=['extra', 'toc', 'md_in_html'])
		title = '{}'.format(meta['folder'])
		o.write(header_class_tmpl.render(content=content, title=title))

# Process worker fn
def _gen_web_image(spath, dpaths):
	for dpath in dpaths:
		convert(spath, dpath)

def gen_web_images(spath, dpath):
	# Operate on absolute paths in case caller is in different dir
	# than the spawned pool process
	spath = os.path.abspath(spath)
	dpath = os.path.abspath(dpath)

	# First, see what of this we can skip
	# This abuses exceptions a bit for control flow; w/e it's a script
	sstat = os.stat(spath)

	# Copy original image
	try:
		dstat = os.stat(dpath)
		if sstat.st_mtime > dstat.st_mtime:
			# Copy original, it's newer
			raise FileNotFoundError
	except FileNotFoundError:
		cp('-u', '--reflink=auto', spath, dpath)

	# Create web-optimized versions
	basename = os.path.splitext(dpath)[0]
	dpaths = list()
	try:
		avstat = os.stat(basename + '.avif')
		if sstat.st_mtime > avstat.st_mtime:
			logger.debug('Updated img will need AVIF ' + spath)
			raise FileNotFoundError
	except FileNotFoundError:
		logger.debug('Creating AVIF for ' + spath)
		dpaths.append(basename + '.avif')
	try:
		wmsat = os.stat(basename + '.webp')
		if sstat.st_mtime > wmsat.st_mtime:
			logger.info('Updated img will need WebP ' + spath)
			raise FileNotFoundError
	except FileNotFoundError:
		logger.debug('Creating WebP for ' + spath)
		dpaths.append(basename + '.webp')
	if dpaths:
		WORKER_JOBS.append(WORKER_POOL.apply_async(_gen_web_image, (spath, dpaths)))

static_extensions = [
		'.css', '.js', '.ico', '.ttf', '.eot', '.svg', '.woff',
		'.pdf', '.pptx', '.doc', '.docx', '.txt',
		'.gz', '.tgz', '.otf', '.odp', '.webmanifest', '.xml',
		'.h', '.c', '.cpp', '.cxx', '.mk', '.ipynb', '.py',
		'.zip', '.webm', '.patch',
		]
image_extensions = [
		'.png', '.jpg',
		]

def handle_static_file(spath, dpath):
	#logger.debug('Static: {} -> {}'.format(spath, dpath))
	ext = os.path.splitext(dpath)[1]

	if ext in image_extensions:
		gen_web_images(spath, dpath)
	elif ext in static_extensions:
		# These do not need to be compiled in any way
		# Just copy them
		#
		# n.b. this assumes linux-like cp (gcp import)
		cp('-u', '--reflink=auto', spath, dpath)
	else:
		logger.debug('Skipping file (ext >>{}<<): {}'.format(ext, spath))


class DirectoryWalker:
	def __init__(self):
		self.root = os.getcwd()
		self.htmlroot = os.path.join(self.root, 'html')
		self.path = []

	def process(self, folder):
		self.recurse(folder)

	def html_dir(self):
		return os.path.join(self.htmlroot, *self.path)

	def recurse(self, folder):
		self.path.append(folder)
		logger.debug('RECURSE path: {}'.format(self.path))

		if len(self.path) > 10:
			raise

		with pushd(folder):
			for dirent in os.scandir():
				# Should we render content found in this folder?
				if os.path.exists('_RENDER'):
					# Defer making output folder to avoid empty ones
					do_render = True
					mkdir('-p', self.html_dir())
				else:
					do_render = False

				# Anything .gitignore'd we can move past immediately
				try:
					git('check-ignore', '-q', dirent.name)
					logger.debug('gitignored: {}'.format(dirent.name))
					continue
				except sh.ErrorReturnCode_1:
					pass

				if dirent.is_dir():
					# sanity check the .gitignore bits
					assert dirent.name != 'nopublish'
					self.recurse(dirent.name)
				elif dirent.is_file():
					if do_render:
						# Maybe: invert for a-zA-Z0-9 ?
						if dirent.name[0] in ('.', '~', '_'):
							continue
						if dirent.name[-3:] == '.md':
							meta = {
									'folder': folder,
									}
							dpath = os.path.join(self.html_dir(), dirent.name[:-3] + '.html')
							class_md_to_html(dirent.name, dpath, meta)
						else:
							dpath = os.path.join(self.html_dir(), dirent.name)
							handle_static_file(dirent.path, dpath)

		self.path.pop()


# Prevent recursion in multiprocess case
if __name__ == '__main__':
	import jinja2 as jinja
	import markdown

	import logger
	import publications

	from ImgToPictureTreeprocessor import ImgToPictureExtension

	from multiprocessing import Pool
	global WORKER_POOL
	global WORKER_JOBS
	WORKER_POOL = Pool()
	WORKER_JOBS = list()

	jinja_env = jinja.Environment(loader=jinja.FileSystemLoader('templates'))

	header_tmpl = jinja_env.get_template('header.html')
	header_class_tmpl = jinja_env.get_template('header_class.html')
	footer_tmpl = jinja_env.get_template('footer.html')

	pubs_groups   = publications.init(jinja_env)

	mkdir('-p', 'html')
	try:
		# https://help.dropbox.com/files-folders/restore-delete/ignored-files
		# xattr -w com.dropbox.ignored 1 /Users/yourname/Dropbox\ \(Personal\)/YourFileName.pdf
		from sh import xattr
		xattr('-w', 'com.dropbox.ignored', '1', 'html/')
	except:
		logger.debug('Not on Mac; not ignoring for Dropbox')
		pass

	for md in os.listdir('pages'):
		if md[-3:] == '.md':
			md_to_html('pages', '/', md)

	logger.info('Process classes')
	DirectoryWalker().process('classes')

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
				spath = os.path.join(dirpath, filename)
				# hack hack hack
				assert spath[:7] == 'static/'
				dpath = os.path.join('html', spath[7:])
				assert(dpath[:4] == 'html')
				handle_static_file(spath, dpath)

	logger.info("Waiting for any outstanding tasks to complete...")
	# Get any errors from jobs (makes join redudant but :shrug:)
	while WORKER_JOBS:
		j = WORKER_JOBS.pop(0)
		if not j.ready():
			logger.info("...waiting for {} jobs".format(len(WORKER_JOBS)))
		j.get()
	WORKER_POOL.close()
	WORKER_POOL.join()

	logger.info("Done!")
