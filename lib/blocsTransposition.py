#! /usr/bin/python

# Old method
# transposition
# by bloc

class BlocsTransposition:
    """Class taking care of blos transposition cyphering"""
    def __init__(self, key, message):
        self.k = key
        self.m = message

    def lengthKey(self):
        return len(self.k)

x = BlocsTransposition("loick","lareponseestquarantedeux")
print x.lengthKey()
