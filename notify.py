#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
import pynotify

# notification class
class Notify(object):

	# constructor
	def __init__(self):
		pynotify.init('notifications')
		self.message = pynotify.Notification('','')

	# display growl type notification
	def show(self, title, message):
		self.message.update(title, str(message))
		self.message.show()