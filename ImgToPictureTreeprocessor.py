"""
ImgToPicture Extension for Python-Markdown
==========================================

Automatically replace `<img>` tags with HTML5 `<picture>` tags.
The extension will try to infer all present image types and will
replicate `class` and `alt` text information in each `<img>`.

See <https://Python-Markdown.github.io/extensions/footnotes>
for documentation.

Copyright Pat Pannuto 2022.

License: [BSD](https://opensource.org/licenses/bsd-license.php)
"""

import copy
import os
import sys

from markdown import Extension
from markdown.treeprocessors import Treeprocessor

import xml.etree.ElementTree as etree

class ImgToPictureTreeprocessor(Treeprocessor):
	def __init__(self, md, config):
		super().__init__(md)
		# Cache config as self.VAR state

	def run(self, root):
		seen_img = set()
		for img in root.iter('img'):
			if img in seen_img:
				continue
			seen_img.add(img)

			# Only do jpg and png for now
			basename,ext = os.path.splitext(img.attrib['src'])
			if ext not in ('.jpg', '.png'):
				print("Do not <picture> image: ", img.attrib['src'])
				continue

			# As extensions go, this isn't so re-usable, as it assumes something
			# else makes exactly these alternate image formats:

			# First, save and strip off the tail (as <img /> not <img></img>)
			orig_tail = img.tail
			img.tail = None

			# Save the original img tag without tail as it'll go in <picture>
			orig_img = copy.deepcopy(img)
			seen_img.add(orig_img)

			# Then, create <source> tags for alternate formats
			avif = etree.Element('source', {
				'srcset': basename + '.avif',
				'type': 'image/avif'
				})
			webp = etree.Element('source', {
				'srcset': basename + '.webp',
				'type': 'image/webp'
				})

			# Update the original Element to be a picture instead, and elements
			img.clear()
			img.tag = 'picture'

			img.append(avif)
			img.append(webp)
			img.append(orig_img)

			img.tail = orig_tail

			# View result?
			#etree.dump(img)
			#sys.exit()

class ImgToPictureExtension(Extension):

	ImgToPictureProcessorClass = ImgToPictureTreeprocessor

	def __init__(self, **kwargs):
		self.config = {}
		super().__init__(**kwargs)

	def extendMarkdown(self, md):
		md.registerExtension(self)
		self.md = md
		img_to_picture_extension = self.ImgToPictureProcessorClass(md, self.getConfigs())
		# TODO: How are you supposed to choose priority??
		# md_in_html is 105 according to source; need to run after that at least
		# and I really don't understand priority: md_in_html has three processors:
		#  - md.preprocessors.register(HtmlBlockPreprocessor(md), 'html_block', 20)
		#  - md.parser.blockprocessors.register(MarkdownInHtmlProcessor(md.parser), 'markdown_block', 105)
		#  - md.postprocessors.register(MarkdownInHTMLPostprocessor(md), 'raw_html', 30)
		# Going higher doesn't work (tried 150), going lower does?
		# Okay, if we do 15, we have all the md_in_html img tags, but don't have classes:
		#  <img src="/images/research/tock-logo-square.png" alt="Tock Logo" />{: .img-fluid .d-none .d-md-block }
		# 10 still no classes
		# 8 gets classes
		# This is a silly system :(
		md.treeprocessors.register(img_to_picture_extension, 'img_to_picture', 8)


	def reset(self):
		# self.md.STATE_VAR = INIT_VAL
		return

def makeExtension(**kwargs):
    return ImgToPictureExtension(**kwargs)
