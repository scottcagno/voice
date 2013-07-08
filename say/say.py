#!/usr/bin/python
# Copywritght 2013-Present, Scott Cagno (BSD LICENSE)

# basic python program for linux to enable speech to text
# this is the first hack, could use more improvement

import sys, alsaaudio, wave, numpy, os, threading, time, commands, json

arl = []
run = 1

class checkAudio(threading.Thread):
	def run(self):
		while True:
			time.sleep(1)
			if numpy.abs(arl).mean() < 15:
				global run
				run = 0
				exit()
checkAudio().start()

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

w = wave.open('rec.wav', 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(16000)

while run != 0:
    	l, data = inp.read()
    	arl = numpy.fromstring(data, dtype='int16')
    	#print numpy.abs(arl).mean()
    	w.writeframes(data)

os.system('flac --totally-silent -f --fast --endian=little --channels=1 --sample-rate=16000 --delete-input-file rec.wav')
res = commands.getoutput('wget -q -U "Mozilla/5.0" --post-file rec.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v1/recognize?lang=en-us&client=chromium"')
os.remove("rec.flac")

dec = json.loads(res)
print dec["hypotheses"][0]["utterance"]