#! /usr/bin/python

import os, sys

# Old method
# transposition
# Railfence
# in french : "Dents de scie"

class Railfence:
	"""docstring for railfance"""
	def __init__(self, line1, line2 = ""):
		self.line1 = line1
		self.line2 = line2

	"""Method to encrypt the message"""
	def encrypt(self):
		self.line1.replace(" ", "") #Replace all spaces
		length = len(self.line1)
		result = []
		result.append([])
		result.append([])
		for x in range(len(self.line1)):
			if x%2 == 0:
				result[0].append(self.line1[x])
			else:
				result[1].append(self.line1[x])
		self.result = result

	"""Method to decrypt the message"""
	def decrypt(self):
		message = ""
		length = len(self.line1)
		if (((length/2)*2) < length):
			test = 1
		else:
			test = 0
		tab = []
		tab.append(self.line1)
		tab.append(self.line2)
		for x in range(len(tab[0])):
		    message = message + tab[0][x]
		    try:
		    	message = message + tab[1][x]
		    except Exception, e:
		    	toto = 1
		self.result = message

	def show(self):
		print self.result

# TEST FOR ENCODE #
w = Railfence("ABCDEFHG")
w.encrypt()
w.show()
# TEST FOR DECODE #
x = Railfence("TS","ET")
x.decrypt()
x.show()