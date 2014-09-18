#! /usr/bin/python

import sys

# Args allowed
#
# -c cypher
# -d decypher
# -m specify the methode
# -k key for process
# -f file to prossess
# "" the last argument into "" is the message to cipher/decypher
# For now the first arg is the script name,
# the second is either c or d for cypher or decypher,
# the third is the key,
# the fourth is the message.

scriptName = sys.argv[0]
prossess = sys.argv[1]
key = sys.argv[2]
msg = sys.argv[3]

