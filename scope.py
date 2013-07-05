#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
import inspect, scopes, notify

# scope class
class Scope(object):

	# constructor
	def __init__(self, notification_sys):
		for module in scopes.__all__: 
			__import__('scopes.' + module)
		self.notify = notification_sys
		self.scope_list = {}
		self.load_scopes()

	# load scopes
	def load_scopes(self):
		for sid, scope in scopes.__dict__.iteritems():
			if inspect.ismodule(scope):
				if sid in scopes.__all__:
					self.scope_list[scope.name] = scope

	# show live scopes
	def live_scopes(self):
		live_scopes = []
		for sid, scope in self.scope_list.items():
			if scope.live == True:
				live_scopes.append(sid)
		self.notify.show("LIVE SCOPES", live_scopes)

	# toggle scope live status
	def toggle(self, scope):
		if scope.live == False:
			scope.live = True
		else:
			scope.live = False
		self.notify.show("TOGGLED %s" % scope.name, "LIVE: %s" % scope.live)


	# run an action based on a command
	def execute(self, cmd):
		for sid, scope in self.scope_list.items():
			if cmd == scope.togg:
				self.toggle(scope)
			if cmd == "LIVE-SCOPES":
				self.live_scopes()
			if scope.live == True:
				if scope.cmds.has_key(cmd):
					for actn in scope.cmds[cmd]:
						actn.run()
	'''

	** UNSURE OF THESE AT THE MOMENT **

	# check if scope exists
	def exists(self, sid):
		return self.scope_list.has_key(sid)

	# activate scope
	def activate(self, sid):
		if self.exists(sid):
			self.scope_list[sid].live = True

	# deactivate scope
	def deactivate(self, sid):
		if self.exists(sid):
			self.scope_list[sid].live = False
	'''