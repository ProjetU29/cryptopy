#! /usr/bin/python

import os, sys

# Old method
# transposition
# Ceasar Cipher
# in french : "Code de Cesar"

class HebrewCipher:
	"""docstring for HebrewCipher"""
	def __init__(self, codage, line):
		self.codage = codage
		self.line = line.replace(" ", "") #Replace all spaces
		self.atbash = ["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
		self.albam = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
		self.atbah = ["I","H","G","F","N","D","C","B","A","R","Q","P","O","E","M","L","K","J","Z","Y","X","W","V","U","T","S"]

	"""Method to encrypt the message"""
	def encrypt(self):
		result = []
		result.append([])
		for x in range(len(self.line)):
			index = (ord(self.line[x])-65)
			if (self.codage == 1):
				result[0].append(self.atbash[index])
			elif (self.codage == 2):
				result[0].append(self.albam[index])
			elif (self.codage == 3):
				result[0].append(self.atbah[index])
			elif (self.codage == 4):
				result[0].append(self.atbah[ord(self.atbah[index])-65])
			
		self.result = result

	"""Method to decrypt the message"""
	def decrypt(self):
		self.encrypt();

	def show(self):
		print self.result

# TEST FOR ENCODE #
w = HebrewCipher(1,"COUCOU MON COEUR")
w.encrypt()
print "ATBASH"
w.show()
w = HebrewCipher(2,"COUCOU MON COEUR")
w.encrypt()
print "ALBAM"
w.show()
w = HebrewCipher(3,"COUCOU MON COEUR")
w.encrypt()
print "ATBAH"
w.show()
w = HebrewCipher(4,"COUCOU MON COEUR")
w.encrypt()
print "ATBAH x2"
w.show()
# TEST FOR DECODE #
x = HebrewCipher(1,"XLVFI")
x.decrypt()
x.show()
x = HebrewCipher(2,"PBRHE")
x.decrypt()
x.show()
x = HebrewCipher(3,"GMNXJ")
x.decrypt()
x.show()