#!/usr/bin/env python3

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
        o.write(r'\subsection*{' + escape_latex(section['display']) + '}\n')
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

            if 'honoree' in entry:
                r += '\\textbf{Honoree: ' + escape_latex(entry['honoree']) + '}'
                r += '}'
                r += r' \\' + '\n'
                rows.append(r)

                r = ''
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
del awards


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
del teaching


with open('service.toml', 'rb') as f:
    service = tomllib.load(f)

with open('gen/service.tex', 'w') as o:

    o.write('\n' + '%' + '-'*60 + '%' + '\n')
    o.write(       '%' + '-'*60 + '%' + '\n')
    o.write(r'\section*{' + service['display'] + '}' + '\n\n')
    del service['display']

    o.write(r'\renewcommand{\arraystretch}{0.5}' + '\n')

    for context in service:
        # Skip this for now, old CV did
        if context == 'internal':
            continue
        # In future, maybe a subsection here?

        context = service[context]

        # Open table for this service context
        o.write(r'\begin{longtable}{>{\bf}p{2.1cm} l}' + '\n')

        rows = []

        for activity in context:
            activity = context[activity]

            r = ''

            # Year column
            r += '  '
            if 'year' in activity:
                assert 'start' not in activity
                r += '{:14s}'.format(str(activity['year']))
            else:
                if 'end' in activity:
                    r += '{:4s}--{:8s}'.format(str(activity['start']), str(activity['end']))
                else:
                    r += '{:4s}--{:8s}'.format(str(activity['start']), 'present')

            # Activity column
            r += r'& \makecell{'
            r += escape_latex(activity['thing'])

            if 'role' in activity:
                r += ' -- '
                r += escape_latex(activity['role'])

            r += r'} \\' + '\n'

            rows.append(r)

        table_body = (r'  \\' + '\n\n').join(rows)
        o.write(table_body)

        o.write(r'\end{longtable}' + '\n')

    o.write(r'\renewcommand{\arraystretch}{1.0}' + '\n')
del service







# n.b. at some point: advising ~same as service; at least for now
with open('advising.toml', 'rb') as f:
    advising = tomllib.load(f)

with open('advising-rops.toml', 'rb') as f:
    rops = tomllib.load(f)

with open('gen/advising.tex', 'w') as o:

    o.write('\n' + '%' + '-'*60 + '%' + '\n')
    o.write(       '%' + '-'*60 + '%' + '\n')
    o.write(r'\section*{' + advising['display'] + '}' + '\n\n')
    del advising['display']

    for rank in advising:
        rank = advising[rank]
        o.write('\n' + '%' + '-'*60 + '%' + '\n')
        o.write(r'\subsection*{' + escape_latex(rank['display']) + '}\n')
        o.write(r'\renewcommand{\arraystretch}{0.5}' + '\n')
        o.write(r'\begin{longtable}{>{\bf}p{2.1cm} l}' + '\n')

        rows = []

        for mentee in rank:
            mentee = rank[mentee]
            if not isinstance(mentee, dict):
                continue

            r = ''

            # Year column
            r += '  '
            if 'end' in mentee:
                if mentee['start'] == mentee['end']:
                    r += '{:14s}'.format(str(mentee['start']))
                else:
                    r += '{:4s}--{:8s}'.format(str(mentee['start']), str(mentee['end']))
            else:
                r += '{:4s}--{:8s}'.format(str(mentee['start']), 'present')

            # Details column
            r += r'& \makecell{' + '\n'
            r += '    '
            if 'url' in mentee:
                r += r'\href{' + mentee['url'] + '}{' + mentee['name'] + '}'
            else:
                r += mentee['name']

            if 'degree' in mentee:
                if 'discipline' in mentee:
                    r += ' (' + mentee['degree'] + ', ' + mentee['discipline'] + ')'
                else:
                    r += ' (' + mentee['degree'] + ', CSE)'

            if 'coadv' in mentee:
                r += ' [Co-Advised by ' + mentee['coadv'] + ']'

            if 'context' in mentee:
                r += ' (' + escape_latex(mentee['context']) + ')'

            if 'next' in mentee:
                r += r' $\rightarrow$ ' + escape_latex(mentee['next'])

            if 'thesis' in mentee:
                r += r'\\' + '\n    ' + r'Thesis: \emph{' + escape_latex(mentee['thesis']) + '}'

            r += r'} \\' + '\n'

            rows.append(r)

        table_body = (r'  \\' + '\n\n').join(rows)
        o.write(table_body)

        o.write(r'\end{longtable}' + '\n')
        o.write(r'\renewcommand{\arraystretch}{1.0}' + '\n')

    o.write(r'\subsection*{' + escape_latex(rops['display']) + '}\n')
    for rop in rops:
        rop = rops[rop]
        if not isinstance(rop, dict):
            continue

        o.write('\n' + '%' + '-'*40 + '%' + '\n')
        o.write(r'\subsubsection*{' + escape_latex(rop['display']) + '}\n')
        o.write(r'\url{' + rop['url'] + '}\n')

        o.write(r'\begin{itemize}' + '\n')
        for cohort in rop:
            cohort = rop[cohort]
            if not isinstance(cohort, dict):
                continue

            if "mentor" in cohort:
                o.write(r'\item[]{' + escape_latex(cohort['display']) + ', advised by ' + cohort['mentor'] + '}\n')
            else:
                o.write(r'\item[]{' + escape_latex(cohort['display']) + '}\n')
            o.write(r'\begin{itemize}' + '\n')
            for mentee in cohort['mentees']:
                o.write(r'\item ' + mentee + '\n')
            o.write(r'\end{itemize}' + '\n')
        o.write(r'\end{itemize}' + '\n')

del advising
del rops
