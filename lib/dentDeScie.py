import os, sys

message = sys.argv[1]
message.replace(" ", "")
longueur = len(message)
if (((longueur/2)*2) < longueur):
	colonne = longueur/2+1
	ligne = longueur/2+1
else:
	colonne = longueur/2
	ligne = longueur/2
tab = []
tab.append([])
tab.append([])
for x in range(len(message)):
	if x%2 == 0:
		tab[0].append(message[x])
	else:
		tab[1].append(message[x])
print tab

message = ""
for x in range(len(tab[0])):
    message = message + tab[0][x]
    message = message + tab[1][x]
print message