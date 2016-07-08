#! /usr/bin/env python

from urllib2 import Request, urlopen
from gi.repository import Notify

import os
import json
import sys
import time 

import pyxhook



# Send a 'bubble' notification
def sendMessage(message):
	Notify.init("Translation: ")
	Notify.Notification.new(message).show()
	Notify.uninit()

# Return highlighted text and replace all spaces with dashes ( as API require) 
def getHighlightedText():
	text = os.popen('xsel').read()
	return text.replace(" ", "-")

# API request
def translate(text, langPair='en-ru'):
	initUrl = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160708T103650Z.6cc58e66647cc5a8.1a433736836cb67d351f07ca604cd76cecb7f5dc&'
	apiUrl = initUrl + 'text=' + text + '&lang=' + langPair
	response = urlopen(apiUrl)
	return json.loads(response.read())

def kEvent(event):
	if event.Key == 'P_Begin': # P_Begin is '5' on a numpad
		text = getHighlightedText()
		message = u''.join(translate(getHighlightedText())["text"]).encode('utf-8').strip()
		sendMessage(message.replace("-", " "))

if __name__ == '__main__':
	# Setting up hook manager
	hookManager = pyxhook.HookManager()
	hookManager.KeyDown = kEvent
	hookManager.HookKeyboard()
	hookManager.start()

	# Keep script alive
	while True:
		time.sleep(0.1)
