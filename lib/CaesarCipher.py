#! /usr/bin/python

import os, sys

# Old method
# transposition
# Ceasar Cipher
# in french : "Code de César"

class CaesarChipher:
	"""docstring for CaesarChipher"""
	def __init__(self, rotation, line):
		self.rotation = rotation
		self.line = line
		self.alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	"""Method to encrypt the message"""
	def encrypt(self):
		self.line.replace(" ", "") #Replace all spaces
		result = []
		result.append([])
		for x in range(len(self.line)):
			index = (((ord(self.line[x])-64)+self.rotation-1)%26)
			result[0].append(self.alphabet[index])
		self.result = result

	"""Method to decrypt the message"""
	def decrypt(self):
		message = ""
		tab = []
		tab.append([])
		for x in range(len(self.line)):
			index = (((ord(self.line[x])-64)-self.rotation)%26)
			tab[0].append(self.alphabet[index])
		self.result = tab

	def show(self):
		print self.result

# TEST FOR ENCODE #
w = CaesarChipher(3,"COLYSEE")
w.encrypt()
w.show()
# TEST FOR DECODE #
x = CaesarChipher(4,"FROBVHH")
x.decrypt()
x.show()