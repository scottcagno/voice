#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
import scope, stte, gobject, signal, sys, os, inspect, notify, subprocess

# voice operated interpolated coding engine
class Voice(object):

	# constructor
	def __init__(self, notification_sys):
		self.notify = notification_sys
		self.scopes = scope.Scope(notification_sys)
		self.update_corpus(["LIVE-SCOPES"])
		self.engine = stte.SpeechToTextEngine('models')
		self.engine.connect('finished', self.parse)
		

	# updating corpus
	def update_corpus(self, corpus_extras):
		self.notify.show('UPDATING CORPUS','Just a moment...')
		with open('utils/vocab.corpus', 'w') as fd:
			for item in corpus_extras:
				fd.write(item + '\n')
			for _, scp in self.scopes.scope_list.items():
				fd.write(scp.togg + '\n')
				for cmd, actn in scp.cmds.items():
					fd.write(cmd + '\n')
		subprocess.check_call('cd utils; ./corpus.sh; cd ..', shell=True)

	# parse hypothesis, issue command
	def parse(self, stt, hyp):
		hyp = hyp.split(' ')
		self.notify.show("HYPOTHESIS", hyp)
		for cmd in hyp:
			self.scopes.execute(cmd)