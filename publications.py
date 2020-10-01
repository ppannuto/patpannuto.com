import datetime
from pybtex.database.input import bibtex
import os, sys, html, re
import jinja2 as jinja

from sh import cp
from sh import mkdir

import logger

BIB_FILES = ['conferences', 'journals', 'workshops', 'posterdemo']
WORK_TYPES = {'conferences': 'paper',
              'journals':    'paper',
              'workshops':   'paper',
              'posterdemo':  'paper'}
MONTH_CONV = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
              'jul': 7, 'aug': 8, 'sep': 9, 'oct':10, 'nov':11, 'dec':12}

#CONTENT_DIR         = os.path.join('content', 'pubs')
CONTENT_DIR         = 'pubs'
LOCAL_CONTENT_DIR   = os.path.join('html', CONTENT_DIR)
LOCAL_SPOTLIGHT_DIR = os.path.join('html', CONTENT_DIR, '__spotlight')

def get_name (person):
	name = ''
	first   = person.get_part_as_text('first')
	middle  = person.get_part_as_text('middle')
	last    = person.get_part_as_text('last')
	lineage = person.get_part_as_text('lineage')

	name += first
	if middle:
		if name:
			name += '~' + middle
		else:
			name += middle
	if last:
		if name:
			name += '~' + last
		else:
			name += last
	if lineage:
		name += ',~' + lineage
	return name

def hiddens_add_bibtex(hiddens, bibkey, entry, raw_authors):
	raw = '@{}{{{},\n'.format(entry.type, bibkey)
	for f in entry.fields:
		# Skip over some fields we use but aren't appropriate for all
		if f in (
				'abstract',
				'no-abstract',
				'keywords',
				'badge',
				'to-appear',
				'type',
				'display-type',
				'acceptance-percent',
				'acceptance-accepted',
				'acceptance-total',
				):
			continue
		elif f == 'authors':
			with_bf = raw_authors[bibkey]
			# First, strip any \textbf directives (highlighting my name)
			while True:
				match = re.search('\\\\textbf{(\S+)}', with_bf)
				if match is None:
					break
				with_bf = with_bf.replace(match.group(0), match.group(1))
			raw += '\tauthor = {{{}}},\n'.format(with_bf)
		else:
			raw += '\t{} = {{{}}},\n'.format(f, entry.fields[f])
	raw += '}'
	hiddens['bibtex'] = raw

def hiddens_add_abstract(hiddens, bibkey, entry, raw_abstracts):
	try:
		hiddens['abstract']      = raw_abstracts[bibkey]
		hiddens['abstract_html'] = latex_to_html(raw_abstracts[bibkey])
	except KeyError:
		try:
			entry.fields['no-abstract']
		except KeyError:
			logger.warn("Bib entry {} has no abstract.".format(bibkey))
			logger.warn("\tYou need to add an abstract to this bib entry.")
			logger.warn("\tIf this work has no abstract, add the empty key `no-abstract'")
	except NotImplementedError:
		logger.error("Converting abstract for {} failed. Probably need".format(bibkey))
		logger.error("\tto upgrade the latex_to_html() function.")

def latex_to_html(latex):
	# I tried pytex and plasTeX, but I couldn't get either to work, so I
	# just rolled my own very basic one. Should be enough for our immediate
	# needs, but this solution should be revisited some day.

	def l_gen(latex):
		for l in latex:
			yield l

	h = ''
	scope = []
	dash_count = 0
	newline_count = 0
	lg = l_gen(latex)
	try:
		while True:
			l = next(lg)
			if dash_count:
				if l == '-':
					dash_count += 1
					continue
				else:
					if dash_count == 1:
						h += '-'
					elif dash_count == 2:
						h += '&ndash;'
					elif dash_count == 3:
						h += '&mdash;'
					else:
						logger.error("Greater than 3 dashes in a row?")
						raise NotImplementedError
					dash_count = 0

			if newline_count:
				if l == '\n':
					if newline_count == 1:
						h += '</p><p>'
				else:
					newline_count = 0

			if l == '{':
				l = next(lg)
				if l != '\\':
					scope.append('')

			if l == '\\':
				cmd = ''
				l = next(lg)
				if l in ('!@#$%^&*()-/\\'):
					h += html.escape(l)
					continue
				if l == ',':
					#h += '&thinsp;'
					# thinsp's look terrible, go for the full nbsp instead
					h += '&nbsp;'
					continue
				if l == "'":
					# add ´ to next letter (i.e. \'e -> é)
					l = next(lg)
					if l not in 'aeiouyAEIOUY':
						logger.error("Accent on non-vowel?")
						raise NotImplementedError
					h += '&' + l + 'acute;'
					continue
				if l == "`":
					# add ` to next letter (i.e. \`e -> è)
					l = next(lg)
					if l not in 'aeiouyAEIOUY':
						logger.error("Accent on non-vowel?")
						raise NotImplementedError
					h += '&' + l + 'grave;'
					continue
				while l.isalpha():
					cmd += l
					l = next(lg)
				if l == '{':
					l = next(lg)
				if len(cmd) == 0:
					h += ' '
					continue

				if cmd in ('em', 'emph'):
					h += '<em>'
				elif cmd in ('bf', 'textbf'):
					h += '<strong>'
				elif cmd == 'uA':
					h += '&mu;A'
				elif cmd == 'uW':
					h += '&mu;W'
				elif cmd == 'iic':
					h += 'I<sup>2</sup>C'
				else:
					logger.error("(scope \\\\) Unknown latex command >" + cmd + '<')
					raise NotImplementedError
				scope.append(cmd)
				h += l
			elif l == '}':
				try:
					cmd = scope.pop()
				except IndexError:
					logger.error("Unbalanced braces?")
					raise
				if cmd in ('em', 'emph'):
					h += '</em>'
				elif cmd in ('bf', 'textbf'):
					h += '</strong>'
				elif cmd == 'uA':
					h += '&mu;A'
				elif cmd == '':
					# Braces with no latex command
					pass
				else:
					logger.error("(scope }) Unknown latex command " + cmd)
					raise NotImplementedError
			elif l == '$':
				l = next(lg)
				while True:
					if l.isalnum():
						h += l
					elif l == '>':
						h += '&gt;'
					elif l == '<':
						h += '&lt;'
					elif l == '^':
						h += '<sup>'
						l = next(lg)
						if l == '{':
							l = next(lg)
							while l != '}':
								h += l
						else:
							h += l
						h += '</sup>'
					elif l == '\\':
						cmd = ''
						l = next(lg)
						#while l not in (' ', '.', ',', '?', '!', '$'):
						while l.isalpha():
							cmd += l
							l = next(lg)
						if cmd == 'times':
							h += '&times;'
						elif cmd == 'degree':
							h += '&deg;'
						else:
							logger.error("Unknown math mode command: " + cmd)
							raise NotImplementedError
						continue
					elif l == '$':
						break
					else:
						logger.error("Math mode only supports '^' currently")
						logger.error("Parser got: " + l)
						raise NotImplementedError
					l = next(lg)
			elif l == '-':
				dash_count += 1
			elif l == '\n':
				h += ' '
				newline_count += 1
			elif l == '~':
				h += '&nbsp;'
			elif l == '`':
				l = next(lg)
				if l == '`':
					h += '&ldquo;'
				else:
					h += '&lsquo;' + l
			elif l == "'":
				l = next(lg)
				if l == "'":
					h += '&rdquo;'
				else:
					h += '&rsquo;' + l
			else:
				h += l
	except StopIteration:
		pass
	return h

def invert_string (s):
	ret = ''
	for l in s:
		o = ord(l)
		if (o >= 65 and o <= 90) or (o >= 97 and o <= 122):
			o = 187-o
		ret += chr(o)
	return ret

def sort_papers (p):
	return str(p.date) + invert_string(p.entry.fields['title'])


class Paper ():
	def __init__ (self, bibkey, entry, bibgroup, raw_authors, raw_abstracts):
		self.bibkey = bibkey
		self.raw_abstract = raw_abstracts

		authors = []
		if 'author' in entry.persons:
			for person in entry.persons['author']:
				authors.append(get_name(person))
		entry.fields['authors'] = ', '.join(authors)

		entry.fields['badge'] = bibgroup[0].upper()
		if entry.fields['badge'] in ('P', 'D'):
			entry.fields['badge'] = 'PD'
		entry.fields['type'] = bibgroup
		entry.fields['display-type'] = WORK_TYPES[bibgroup]


		self.paths = {}

		# Try to copy the PDF to the content directory
		if os.path.exists(os.path.join('static', 'cv', bibkey + '.pdf')):
			cp(os.path.join('static', 'cv', bibkey + '.pdf'), LOCAL_CONTENT_DIR)
			self.paths['pdf'] = os.path.join(CONTENT_DIR, bibkey + '.pdf')
		else:
			if 'to-appear' in entry.fields and entry.fields['to-appear'] == '1':
				logger.warn('No PDF for "To Appear" paper {}'.format(bibkey))
			else:
				logger.critical_leader('Unable to find {}'.format(bibkey + '.pdf'))
				logger.critical_leader('\tYou need to add a copy of your paper to the cv/ direcotry')
				logger.critical('\tYour paper should be named the same as the key to the bib entry')

		# Try to copy the paper source to the content directory
		self.missing_zip = True
		for ext in ['.zip', '.tgz', '.tar.gz']:
			if os.path.exists(os.path.join('cv', bibkey + ext)):
				cp(os.path.join('cv', bibkey + ext), LOCAL_CONTENT_DIR)
				self.paths['tex_source'] = os.path.join(CONTENT_DIR, bibkey + ext)
				self.missing_zip = False
				break

		# Grab a ref to the talk if it exists
		if 'series' in entry.fields:
			# talk named after conference
			series_short = entry.fields['series'].lower().replace(' ', '').replace("'", '')
			if os.path.exists(os.path.join('static', 'talks', series_short+'.pptx')):
				self.paths['talk_pptx'] = '/talks/{}.pptx'.format(series_short)
			if os.path.exists(os.path.join('static', 'talks', series_short+'.pdf')):
				self.paths['talk_pdf'] = '/talks/{}.pdf'.format(series_short)
		if 'talk' not in self.paths:
			# talk named after bibkey
			if os.path.exists(os.path.join('static', 'talks', bibkey+'.pptx')):
				self.paths['talk_pptx'] = '/talks/{}.pptx'.format(bibkey)
			if os.path.exists(os.path.join('static', 'talks', bibkey+'.pdf')):
				self.paths['talk_pdf'] = '/talks/{}.pdf'.format(bibkey)

		# Possibly remove \url{} from the url entry if needed
		try:
			if entry.fields['conference-url'][0:5] == '\\url{':
				entry.fields['conference-url'] = entry.fields['conference-url'][5:-1]
		except KeyError:
			logger.warn("Unable to find conference URL for {}".format(bibkey))
			logger.warn('\tThis entry will be missing a link to the conference')

		# Possibly remove \url{} from the video link if needed
		try:
			if entry.fields['video-url'][0:5] == '\\url{':
				entry.fields['video-url'] = entry.fields['video-url'][5:-1]
		except KeyError:
			pass

		# Construct the best date we can for this publication
		try:
			year = entry.fields['year']
		except KeyError:
			logger.critical_leader("Bib entry {} is missing publication year.".format(bibkey))
			logger.critical("\tPlease add a year entry and try again.")

		try:
			month = entry.fields['month']
		except KeyError:
			try:
				month = entry.fields['mon']
			except KeyError:
				month = None
				logger.warn("Bib entry {} is missing publication month.".format(bibkey))
				logger.warn("\tPublication sort order may be affected. Please add a month entry")
		if month:
			if month.isalpha():
				month = MONTH_CONV[month.lower()[0:3]]
			else:
				month = int(month)

		# good enough to sort
		self.date = 365 * int(year)
		if month:
			self.date += 30 * (month - 1)

		# Get values for content that starts out hidden
		self.hiddens = {}
		hiddens_add_bibtex(self.hiddens, bibkey, entry, raw_authors)
		hiddens_add_abstract(self.hiddens, bibkey, entry, raw_abstracts)

		# Add html-friendly entries; note this must be done *after* generating hiddens
		entry.fields['title-html']   = latex_to_html(entry.fields['title'])

		authors = latex_to_html(entry.fields['authors'])
		if len(authors.split(',')) == 1:
			entry.fields['authors-html'] = authors
		elif len(authors.split(',')) == 2:
			entry.fields['authors-html'] = ' and'.join(authors.split(','))
		else:
			authors = authors.split(',')
			authors.insert(len(authors)-1, ' and')
			entry.fields['authors-html'] = ','.join(authors[:-1]) + authors[-1]

		try:
			entry.fields['booktitle-html'] = latex_to_html(entry.fields['booktitle'])
			try:
				series = latex_to_html(entry.fields['series'])
				series = series.replace(' ', '&nbsp;')
				entry.fields['booktitle-html'] += ' (' + series + ')'
			except KeyError:
				pass
		except KeyError:
			pass

		if 'journal' in entry.fields:
			entry.fields['journal-html'] = latex_to_html(entry.fields['journal'])
			if 'series' in entry.fields:
				series = latex_to_html(entry.fields['series'])
				series = series.replace(' ', '&nbsp;')
				entry.fields['journal-html'] += ' (' + series + ')'
			if 'volume' not in entry.fields:
				logger.error('{}: a volume key is required for journals'.format(bibkey))
			if 'number' not in entry.fields:
				logger.error('{}: a number key (issue) is required for journals'.format(bibkey))

		if 'journal' in entry.fields and 'booktitle' in entry.fields:
			logger.error('{} has a journal and booktitle entry.'.format(bibkey))
			logger.error('This is probably not what your want.')


		try:
			entry.fields['acceptance-percent'] =\
					float(entry.fields['acceptance-percent'])
		except KeyError:
			pass
		try:
			entry.fields['acceptance-percent'] =\
					float(entry.fields['acceptance-accepted']) /\
					float(entry.fields['acceptance-total']) * 100
		except KeyError:
			pass

		self.entry = entry


class Publications ():
	def __init__ (self, jinja_env):
		self.papers = []

		self.bib_item_tmpl    = jinja_env.get_template('pubs_item.html')
		self.bib_section_tmpl = jinja_env.get_template('pubs_section.html')
		self.checkbox_tmpl    = jinja_env.get_template('checkbox.html')
		self.spotlight_tmpl   = jinja_env.get_template('pubs_spotlight.html')

	def addPaper (self, paper):
		self.papers.append(paper)

	def generatePublicationPageHTML (self):
		filters = {'type': ''}
		years_seen = list()
		types_seen = set()

		now = datetime.datetime.now()
		now_date = (now.year*365) + ((now.month-1)*30)

		bib_html = ''

		for paper in sorted(self.papers, key=sort_papers, reverse=True):
			if paper.entry.fields['year'] not in years_seen:
				try:
					sec_year = years_seen[-1]

					bib_html += self.bib_section_tmpl.render(
							pubs_section=sec_year,
							pubs=bibs,
							groupname=sec_year)
				except IndexError:
					pass

				bibs = ''
				years_seen.append(paper.entry.fields['year'])

			new = (now_date - paper.date) < 60

			bibs += self.bib_item_tmpl.render(pub=paper.entry.fields,
				paths=paper.paths,
				bibkey=paper.bibkey, hiddens=paper.hiddens, new=new)

			if paper.entry.fields['type'] not in types_seen:
				types_seen.add(paper.entry.fields['type'])

		types = list(types_seen)
		types.sort()
		for t in types:
			title=t.title()
			if title == 'Posterdemo':
				title = 'Posters and Demos'
			if title in ('Conferences', 'Journals', 'Workshops'):
				checked = True
			else:
				checked = False
			filters['type'] += self.checkbox_tmpl.render(checked=checked,
				classes='type_chk', value=t.lower(),
				text=title)

		# One final pass to pick up the last year
		sec_year = years_seen[-1]

		bib_html += self.bib_section_tmpl.render(
				pubs_section=sec_year,
				pubs=bibs,
				groupname=sec_year)

		return bib_html, filters

	def generatePublicationSidebarHTML (self, bibkey):
		for paper in self.papers:
			if paper.bibkey == bibkey:
				return self.spotlight_tmpl.render(pub=paper.entry.fields,
					bibkey=paper.bibkey)
		logger.critical('Paper with key {} not found'.format(bibkey))



def parse_raw_abstracts_and_authors(fname):
	"""
	Hack to grab the unadultered 'abstract' and 'author' keys from bib files.
	"""

	def fgenerator(fname):
		for line in open(fname):
			yield line

	raw_abstracts = {}
	raw_authors = {}

	proc = None
	fg = fgenerator(fname)
	for line in fg:
		if line[0] == '@':
			line = line.rstrip()
			if line[-1] != ',':
				logger.critical_leader('Citation declaration must be on its own line')
				logger.critical_leader('This line must end with a comma')
				logger.critical_leader('Offending line:')
				logger.critical_leader('\t>>>'+line+'<<<')
				logger.critical('Failed to parse ' + fname)
			proc = line.split('{')[1].split(',')[0]
		line = line.lstrip()
		if line[0:6] == 'author':
			if proc is None:
				logger.critical_leader('Found an author before a citation?')
				logger.critical_leader('Something has gone wrong. I found this line:')
				logger.critical_leader('\t>>>'+line.rstrip()+'<<<')
				logger.critical_leader('Outside of a citation?')
				logger.critical('Failed to parse ' + fname)
			raw_authors[proc] = ''
			line = line.split('=')[1].lstrip()[1:]
			scope = 1 # We have already stripped the leading '{'
			while True:
				scope += line.count('{') - line.count('}')
				line = line.lstrip()
				if scope == 0:
					line = line.rstrip()
					if line[-2:] != '},':
						logger.critical_leader('Author last line must end with "},"')
						logger.critical_leader('Instead, I think the author ends with line:')
						logger.critical_leader('\t>>>'+line+'<<<')
						logger.critical('Failed to parse ' + fname)
					line = line[:-2]
					raw_authors[proc] += line
					break
				else:
					if len(line) == 0:
						raw_authors[proc] += '\n'
					else:
						raw_authors[proc] += line
					line = next(fg)
		elif line[0:8] == 'abstract':
			if proc is None:
				logger.critical_leader('Found an abstract before a citation?')
				logger.critical_leader('Something has gone wrong. I found this line:')
				logger.critical_leader('\t>>>'+line.rstrip()+'<<<')
				logger.critical_leader('Outside of a citation?')
				logger.critical('Failed to parse ' + fname)
			raw_abstracts[proc] = ''
			line = line.split('=')[1].lstrip()[1:]
			scope = 1 # We have already stripped the leading '{'
			while True:
				scope += line.count('{') - line.count('}')
				line = line.lstrip()
				if scope == 0:
					line = line.rstrip()
					if line[-2:] != '},':
						logger.critical_leader('Abstract block last line must end with "},"')
						logger.critical_leader('Instead, I think the abstract ends with line:')
						logger.critical_leader('\t>>>'+line+'<<<')
						logger.critical('Failed to parse ' + fname)
					line = line[:-2]
					raw_abstracts[proc] += line
					break
				else:
					if len(line) == 0:
						raw_abstracts[proc] += '\n'
					else:
						raw_abstracts[proc] += line
					line = next(fg)
			proc = None

	return raw_abstracts, raw_authors


def init (jinja_env):

	mkdir('-p', LOCAL_CONTENT_DIR)
	mkdir('-p', LOCAL_SPOTLIGHT_DIR)

	pubs = Publications(jinja_env)

	for bib in BIB_FILES:
		bib_items = {}

		parser   = bibtex.Parser()
		bib_data = parser.parse_file(os.path.join('cv', bib + '.bib'))

		raw_abstracts, raw_authors = parse_raw_abstracts_and_authors(os.path.join('cv', bib + '.bib'))

		for bibkey,entry in bib_data.entries.items():
			pubs.addPaper(Paper(bibkey, entry, bib, raw_authors, raw_abstracts))

	# Warn about missing zips
	missing_zips = []
	for paper in pubs.papers:
		if paper.missing_zip:
			missing_zips.append(paper.bibkey)

	# Disable this warning, didn't turn out to be a great idea
	if False: #len(missing_zips):
		logger.warn("Could not find zip'd sources for the following papers:")
		s = ''
		for p in missing_zips:
			s += p + ' '
			if len(s) > 60:
				logger.warn('\t' + s)
				s = ''
		logger.warn('\t' + s)
		logger.warn('')
		logger.warn('\tYou need to add a zipped copy of the paper to the cv/ directory')
		logger.warn('\tYour zip should be named the same as the key to the bib entry')

	return pubs

def generate_publications_page (pubs, jinja_env):
	pub_tmpl    = jinja_env.get_template('pubs.html')
	footer_tmpl = jinja_env.get_template('footer.html')

	bib_html, filters = pubs.generatePublicationPageHTML()
	html = pub_tmpl.render(pubs=bib_html, filters=filters,
		footer=footer_tmpl.render())
	with open('html/publications.html', 'w') as f:
		f.write(html)



