#!/usr/bin/env python
# Copyright (c) 2013-Present, Scott Cagno
# All rights reserved. [BSD License]

# imports
import pygst, gst, gobject

# speech to text engine class
class SpeechToTextEngine(gobject.GObject):

	__gsignals__ = {
		'finished' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, (gobject.TYPE_STRING,))
	}

	# constructor
	def __init__(self, models_dir):
		gobject.GObject.__init__(self)
		audiopipe = [
			'autoaudiosrc',
			'audioconvert',
			'audioresample',
			'vader name=vad',
			'pocketsphinx name=asr',
			'appsink sync=false'
		]
		self.pipeline = gst.parse_launch(' ! '.join(audiopipe))

		# audio speech recognition
		asr = self.pipeline.get_by_name('asr')
		asr.connect('result', self.result)
		asr.set_property('lm', models_dir + '/lm')
		asr.set_property('dict', models_dir + '/dic')
		asr.set_property('configured', True)

		# voice activity dector
		self.vad = self.pipeline.get_by_name('vad')
		self.vad.set_property('auto-threshold', True)

	# set state to listen
	def listen(self):
		self.pipeline.set_state(gst.STATE_PLAYING)

	# set state to pause
	def pause(self):
		self.vad.set_property('silent', True)
		self.pipeline.set_state(gst.STATE_PAUSED)

	# set state to listen
	def result(self, asr, hyp, uttid):
		self.emit('finished', hyp)