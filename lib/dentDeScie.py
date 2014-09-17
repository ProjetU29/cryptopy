import os, sys
if (sys.argv[1] == 'e'):
	message = sys.argv[2]
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

if (sys.argv[1] == 'd'):
	message = ""
	tabLigneUne = sys.argv[2]
	tabLigneDeux = sys.argv[3]
	longueur = len(sys.argv[2])
	if (((longueur/2)*2) < longueur):
		test = 1
	else:
		test = 0
	tab = []
	tab.append(tabLigneUne)
	tab.append(tabLigneDeux)
	for x in range(len(tab[0])):
	    message = message + tab[0][x]
	    try:
	    	message = message + tab[1][x]
	    except Exception, e:
	    	toto = 1
	print message