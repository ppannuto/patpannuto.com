# vim: set noet ts=4 sts=4 sw=4:
import colorlog
import logging
import sys

formatter = colorlog.ColoredFormatter(
	'{log_color}{levelname:8}{reset} {message}',
	datefmt=None,
	style="{",
	reset=True,
	log_colors={
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red',
	}
)

l = logging.getLogger()

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
#Temporarily disable due to
#  https://github.com/borntyping/python-colorlog/issues/36
#stream.setFormatter(formatter)

l = logging.getLogger()
l.setLevel(logging.INFO)
l.addHandler(stream)

sh_logger = logging.getLogger('sh')
sh_logger.setLevel(logging.WARN)

def debug (s):
	l.debug(s)

def info (s):
	l.info(s)

def warn (s):
	l.warning(s)

def error (s):
	l.error(s)

def critical (s):
	l.critical(s)
	l.critical('')
	l.critical('Critical error. Website NOT successfully built. Quitting.')
	sys.exit(1)

def critical_leader (s):
	l.critical(s)
