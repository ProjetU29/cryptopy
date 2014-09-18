#! /usr/bin/python

# Old method
# transposition
# by bloc

# We count the length of the key
# We define the alphabetical order of the key
# We split the message in blocs equal to the key length
# We reorg the message with as told by the cypher method 
# We slipt the message in blocs with random size

class BlocsTransposition:
    """Class taking care of blos transposition cyphering"""
    def __init__(self, key, message):
        self.k = key
        self.m = message

    def sortAlpha(self):
        s = ''.join(sorted(self.k))
        r = []
        for i in self.k:
            r.append(s.index(i)+1)
        return r


    def splitMsg(self):
        print self.m
        sizeK = len(self.k)
        sizeM = len(self.m)
        loops = sizeM/sizeK
        r = self.sortAlpha()
        
        i = 1
        t = []
        c = []
        while i<=loops:
            t.append(self.m[((i-1)*sizeK):((i-1)*sizeK+sizeK)])
            print "t[i-1] :"
            print t[i-1]

            print "----------------------------------"
            ti = t[i-1]

            j=0
            while j<len(self.k):
                c.append(ti[r[j]-1])
                j = j+1
            print c
            i = i+1

x = BlocsTransposition("loick","monmessageestunpoeme")
#x.sortAlpha()
x.splitMsg()
