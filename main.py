#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
import voice, gobject, sys, signal, notify, datetime, inspect, subprocess

if __name__ == '__main__':

	# instantiating
	notification_sys = notify.Notify()
	gobject.threads_init()
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	v = voice.Voice(notification_sys)

	# starting voice
	v.engine.listen()
	date = str(datetime.datetime.now().date()).split('-')[0]
	notification_sys.show("VOICE IS RUNNING", "Copyright %s, Scott Cagno\nVersion 1.0b" % date)

	# continue running voice
	mainloop = gobject.MainLoop()
	try:
		mainloop.run()
	except:
		mainloop.quit()
		sys.exit()