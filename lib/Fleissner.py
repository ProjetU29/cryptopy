#! /usr/bin/python

import os, sys

# Old method
# transposition
# Fleissner

class Fleissner(object):
	
	"""docstring for Fleissner"""
	def __init__(self, message):
		newMessage = message.replace(" ", "") #Replace all spaces
		tmp = []
		tmp.append([])
		tmp.append([])
		tmp.append([])
		tmp.append([])
		tmp.append([])
		tmp.append([])
		for x in xrange(len(newMessage)):
			if (x<6):
				tmp[0].append(newMessage[x])
			elif (x<12):
				tmp[1].append(newMessage[x])
			elif (x<18):
				tmp[2].append(newMessage[x])
			elif (x<24):
				tmp[3].append(newMessage[x])
			elif (x<30):
				tmp[4].append(newMessage[x])
			else:
				tmp[5].append(newMessage[x])
		print tmp
		self.message = tmp

	def encrypt(self):
		result = []
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		for x in xrange(36):
			if (x<6):
				result[0].append('')
			elif (x<12):
				result[1].append('')
			elif (x<18):
				result[2].append('')
			elif (x<24):
				result[3].append('')
			elif (x<30):
				result[4].append('')
			else:
				result[5].append('')
		result[0][1] = self.message[0][0]
		result[0][3] = self.message[0][1]
		result[0][5] = self.message[0][2]
		result[1][4] = self.message[0][3]
		result[2][2] = self.message[0][4]
		result[3][1] = self.message[0][5]
		result[3][4] = self.message[1][0]
		result[4][5] = self.message[1][1]
		result[5][3] = self.message[1][2]
		result[1][2] = self.message[1][3]
		result[1][5] = self.message[1][4]
		result[2][3] = self.message[1][5]
		result[3][0] = self.message[2][0]
		result[3][5] = self.message[2][1]
		result[4][2] = self.message[2][2]
		result[4][4] = self.message[2][3]
		result[5][1] = self.message[2][4]
		result[5][5] = self.message[2][5]
		result[0][2] = self.message[3][0]
		result[1][0] = self.message[3][1]
		result[2][1] = self.message[3][2]
		result[2][4] = self.message[3][3]
		result[3][3] = self.message[3][4]
		result[4][1] = self.message[3][5]
		result[5][0] = self.message[4][0]
		result[5][2] = self.message[4][1]
		result[5][4] = self.message[4][2]
		result[0][0] = self.message[4][3]
		result[0][4] = self.message[4][4]
		result[1][1] = self.message[4][5]
		result[1][3] = self.message[5][0]
		result[2][0] = self.message[5][1]
		result[2][5] = self.message[5][2]
		result[3][2] = self.message[5][3]
		result[4][0] = self.message[5][4]
		result[4][3] = self.message[5][5]
		self.result = result
		
	def decrypt(self):
		result = []
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		result.append([])
		for x in xrange(36):
			if (x<6):
				result[0].append('')
			elif (x<12):
				result[1].append('')
			elif (x<18):
				result[2].append('')
			elif (x<24):
				result[3].append('')
			elif (x<30):
				result[4].append('')
			else:
				result[5].append('')
		result[0][0] = self.message[0][1]
		result[0][1] = self.message[0][3]
		result[0][2] = self.message[0][5]
		result[0][3] = self.message[1][4]
		result[0][4] = self.message[2][2]
		result[0][5] = self.message[3][1]
		result[1][0] = self.message[3][4]
		result[1][1] = self.message[4][5]
		result[1][2] = self.message[5][3]
		result[1][3] = self.message[1][2]
		result[1][4] = self.message[1][5]
		result[1][5] = self.message[2][3]
		result[2][0] = self.message[3][0]
		result[2][1] = self.message[3][5]
		result[2][2] = self.message[4][2]
		result[2][3] = self.message[4][4]
		result[2][4] = self.message[5][1]
		result[2][5] = self.message[5][5]
		result[3][0] = self.message[0][2]
		result[3][1] = self.message[1][0]
		result[3][2] = self.message[2][1]
		result[3][3] = self.message[2][4]
		result[3][4] = self.message[3][3]
		result[3][5] = self.message[4][1]
		result[4][0] = self.message[5][0]
		result[4][1] = self.message[5][2]
		result[4][2] = self.message[5][4]
		result[4][3] = self.message[0][0]
		result[4][4] = self.message[0][4]
		result[4][5] = self.message[1][1]
		result[5][0] = self.message[1][3]
		result[5][1] = self.message[2][0]
		result[5][2] = self.message[2][5]
		result[5][3] = self.message[3][2]
		result[5][4] = self.message[4][0]
		result[5][5] = self.message[5][3]
		self.result = result
		 

	def show(self):
		print self.result

# TEST FOR ENCODE #
w = Fleissner("ABCDEFHGIJKLMNOPQRSTUVWXYZ0123456789")
w.encrypt()
w.show()
# TEST FOR DECODE #
x = Fleissner("1ASB2CT3J4DK5UELV6MF7WHN8XO9PGYQZI0R")
x.decrypt()
x.show()