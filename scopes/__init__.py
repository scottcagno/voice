#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

__all__ = [ 'base', 'python', 'sublime' ]

# imports
import subprocess

# type text
class typ(object):
	def __init__(self, txt):
		self.txt = txt
	def run(self):
		do = "xdotool %s '%s'"
		subprocess.call(do % ("type", self.txt), shell=True)

# press key
class key(object):
	def __init__(self, txt):
		self.txt = txt
	def run(self):
		do = "xdotool %s '%s'"
		subprocess.call(do % ("key", self.txt), shell=True)

# run bash command
class bsh(object):
	def __init__(self, bash_cmd):
		self.bash_cmd = bash_cmd
	def run(self):
		subprocess.call("%s" % bash_cmd, shell=True)		

# run sublime snippet
class snp(object):
	def __init__(self, txt):
		self.txt = txt
	def run(self):
		snippet = "xdotool type '%s'; xdotool sleep .1; xdotool key Return"
		subprocess.call(snippet % (self.txt), shell=True)

# run a func/meth by name 
class fun(object):
	def __init__(self, obj, func_n_args):
		self.func_n_args = func_n_args 
	def run(self):
		args = func_n_args.split()
		if len(args) == 0: return
		func = args[0]
		args = args[1:]
		name = 'do_' + func
		if not hasattr(obj, name): return
		func = getattr(obj, name)
		func(*args)