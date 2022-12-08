#!/usr/bin/env python3.11

import tomllib
from pprint import pprint

from pylatex.utils import escape_latex
import pandoc

import sys

with open('awards.toml', 'rb') as f:
    awards = tomllib.load(f)

with open('gen/awards.tex', 'w') as o:

    o.write(r'\section*{Awards and Honors}' + '\n\n')

    for section in awards:
        section = awards[section]
        o.write('\n' + '%' + '-'*60 + '%' + '\n')
        o.write(r'\subsection*{' + section['display'] + '}\n')
        o.write(r'\renewcommand{\arraystretch}{0.5}' + '\n')
        o.write(r'\begin{tabular}{>{\bf}p{1cm} l}' + '\n')

        rows = []

        for entry in section:
            entry = section[entry]
            if not isinstance(entry, dict):
                continue
            r = ''
            r += '  '
            r += str(entry['year'])
            r += ' & '
            r += r'\makecell{'

            r += escape_latex(entry['display'])
            if 'display-extra' in entry:
                r += ', '
                r += escape_latex(entry['display-extra'])
            if 'money' in entry:
                r += ', '
                r += escape_latex(entry['money'])
            r += '}'
            r += r' \\' + '\n'
            rows.append(r)

        table_body = (r'  \\' + '\n').join(rows)
        o.write(table_body)

        o.write(r'\end{tabular}' + '\n')
        o.write(r'\renewcommand{\arraystretch}{1.0}' + '\n')


with open('teaching.toml', 'rb') as f:
    teaching = tomllib.load(f)

with open('gen/teaching.tex', 'w') as o:

    o.write('\n' + '%' + '-'*60 + '%' + '\n')
    o.write(       '%' + '-'*60 + '%' + '\n')
    o.write(r'\section*{' + teaching['display'] + '}' + '\n\n')
    del teaching['display']

    o.write(r'\renewcommand{\arraystretch}{0.5}' + '\n')
    o.write(r'\begin{tabular}{>{\bf}p{2.1cm} l}' + '\n')

    for institution in teaching:
        institution = teaching[institution]

        rows = []

        for course in institution:
            course = institution[course]

            # Define year column
            r = ''
            r += r'  \makecell*[{{p{2.1cm}}}]{' + '\n'
            r += r'  \raggedright' + '\n'

            # When taught
            r += '\n'.join(escape_latex(t) for t in course['term']) + '\n'

            # Define content column
            r += r'  } & \makecell{' + '\n'

            # What taught
            title = course['dept'] + ' ' + course['number'] + ': ' + course['title']
            r += r'    \textbf{' + course['role'] + '},\n'
            if 'url' in course:
                r += r'    \href{' + course['url'] + '}%\n'
                r += '    {' + escape_latex(title) + '}\n'
            else:
                r += '    ' + escape_latex(title) + '\n'

            # Extra notes?
            if 'extra-md' in course:
                r += r'\\[.5em]'
                md = pandoc.read(course['extra-md'])
                r += pandoc.write(md, format='latex').replace('\n\n', '\n' + r'\\[0.5em]')

            # Close makecell
            r += r'  } \\'

            rows.append(r)

        table_body = ('\n\n').join(rows)
        o.write(table_body)

    o.write(r'\end{tabular}' + '\n')
    o.write(r'\renewcommand{\arraystretch}{1.0}' + '\n')


