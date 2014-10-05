#! /usr/bin/python

import os, sys

# Old method
# transposition
# Column Transposition

class ColumnTransposition(object):
	"""docstring for ColumnTransposition"""
	def __init__(self, key, message):
		newMessage = message.replace(" ", "") #Replace all spaces
		complement = ""
		if ((len(newMessage)%len(key)) != 0):
			for x in range(len(key) - (len(newMessage)%len(key))):
				complement = complement + "."
		self.key = key
		self.message = newMessage + complement
		self.column = self.sortAlpha()

	# Marche pas avec deux fois la meme lettre
	# Retourne le meme indexe
	def sortAlpha(self):
		s = ''.join(sorted(self.key))
		r = []
		for i in self.key:
			r.append(s.index(i)+1)
		return r

	def encrypt(self):
		r = []
		r.append(self.column)
		j = 0
		ligne = 0
		for i in range(len(self.message)):
			if (i%len(self.key) == 0):
				r.append([])
				ligne = ligne + 1
				j = j+1
			r[j].append(self.message[i])
		print r
		temp = []
		self.result = []
		for x in range(len(self.key)):
			temp.append([])
			self.result.append([])
		tempMessage = ""
		for y in range(len(self.key)):
			for x in range(ligne):
				tempMessage += r[x+1][y]
			temp[y].append(tempMessage)
			tempMessage = ""
		print "Avant transposition"
		print temp
		for x in range(len(self.key)):
			self.result[int(r[0][x])-1] = (temp[x])

	def decrypt(self):
		r = []
		r.append(self.column)
		j = 1
		ligne = 0
		caseAjouter = 0
		# Nombre de ligne
		while ((ligne * len(self.key)) != len(self.message)):
			ligne += 1
		print ligne-1
		# En decoupe le texte et on le met dans des cases
		for i in range(len(self.key)):
			tempMessage = ""
			r.append([])
			for x in range(ligne):
				tempMessage += self.message[ligne*i+x]
			r[j].append(tempMessage)
			j = j+1
		# Concatenation into self.result
		self.result = ""
		for x in range(ligne):
			for y in range(len(self.key)):
				self.result += r[r[0][y]][0][x]

	def show(self):
		print "Self.result"
		print self.result

# TEST FOR ENCODE #
w = ColumnTransposition("PERMVTAUION", "RENDEZ VOUS A MIDI PLACE DE LA LIBERTE")
w.encrypt()
w.show()
# TEST FOR DECODE #
print "----------------------------------------------------"
#x = ColumnTransposition("PERMVTAUION", "VAREIAUEEDIIAE.SD.RMLNDLZLEOCTEPB")
x = ColumnTransposition("BANANE", "AEFBCEENJHFAECOLUILRAACAQ")
x.decrypt()
x.show()