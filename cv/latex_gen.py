#!/usr/bin/env python3.11

import tomllib
from pprint import pprint

from pylatex.utils import escape_latex

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


