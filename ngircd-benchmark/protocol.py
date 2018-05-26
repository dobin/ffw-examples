import random

class Protocol(object):
	def __init__(self):
		self.n = 0

	def onNewIteration(self):
		self.n += 1

	def onPreSend(self, idx, message):
		"""
		The IRC server seems to cache nicknames for some time.
		Always make a new one on each connection attempt.
		"""
		msg = message
		msg = msg.replace('dobin', 'a' + str(self.n))
		#msg = msg.replace('root', 'a' + str(self.n))
		#msg = msg.replace('irc.example.net', 'localhost')
		return msg

	def onPostRecv(self, idx, message):
		return message
