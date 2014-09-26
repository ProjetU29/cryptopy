#! /usr/bin/python

# Old method
# Substitution
# Morse

class morseCode:
    """Class taking care of Morse code substitution"""
    def __init__(self,message):
        self.alphabet = {'A' : '.-' ,'B' : '-...' ,'C' : '-.-.' ,'D' : '-..' ,'E' : '.' ,'F' : '..-.' ,'G' : '--.' ,'H' : '....' ,'I' : '..' ,'J' : '.---' ,'K' : '-.-' ,'L' : '.-..' ,'M' : '--' ,'N' : '-.' ,'O' : '---' ,'P' : '.--.' ,'Q' : '--.-' ,'R' : '.-.' ,'S' : '...' ,'T' : '-' ,'U' : '..-' ,'V' : '...-' ,'W' : '.--' ,'X' : '-..-' ,'Y' : '-.--' ,'Z' : '--..','1' : '.---','2' : '..---','3' : '...--','4' : '....-','5' : '.....','6' : '-....','7' : '--..','8' : '---..','9' : '----.','0' : '-----'}
        self.m = message

    def printAlphabet(self):
        for i,j in sorted(self.alphabet.iteritems()):
            print i,j

    def replaceSpace(self,msg):
        return msg.replace(" ", "|")

    def translateToMorse(self):
        msg = self.m.upper()
        result = []
        for i in range(len(msg)):
            result.append(self.alphabet[msg[i]])
        print " ".join(result)

    def translateFromMorse(self):
        msg = self.m.upper().split(" ")
        result = []
        for i in msg:
            result.append(self.alphabet.keys()[self.alphabet.values().index(i)])
        print " ".join(result)

x = morseCode("monmessageestunpoeme")
x1 = morseCode("-- --- -. -- . ... ... .- --. . . ... - ..- -. .--. --- . -- .")
x2 = morseCode("-.-...---.-.-.-.-----....-.-.-.--.-.-..-.-")
#x.translateToMorse()
x1.translateFromMorse()
#x2.translate()
