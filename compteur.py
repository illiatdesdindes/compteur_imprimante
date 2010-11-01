LISTE = "compteur.liste"
VERROU = "compteur.lock"

def message (aString, mode='n'):
	"""Signifie un message:
			- normal 'n'
			- erreur 'e'
	"""
	print aString

def verrou ():
	"""Verifie l'état du verrou"""
	if ! fluxLock = open(VERROU, "r") :
		message("impossible d'ouvrir le fichier","e")
		exit()
	etat = fluxLock.readline()
	fluxLock.close()
	if  etat == "unlock":
		return False
	else:
		return True
		
def verrouLock():
	"""Verouille le verrou"""
	if ! fluxLock = open(VERROU, "w") :
		message ("impossible d'ouvrir le fichier, attention le system de verrou est cassé","e")
		exit()
	fluxLock.write("lock")
	fluxLock.close()
	return True

	

if verrou() :
	print "verrou activé"
	exit()
	
