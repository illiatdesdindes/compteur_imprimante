LISTE = "compteur.liste"
VERROU = "compteur.lock"

def erreur (aString):
	"""Signifie un message d'erreur"""
	print aString

def verrou ():
	"""Verifie l'état du verrou"""
	if ! fluxLock = open(VERROU, "r") :
		erreur("impossible d'ouvrir le fichier")
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
		erreur ("impossible d'ouvrir le fichier, attention le system de verrou est cassé")
		exit()
	fluxLock.write("lock")
	fluxLock.close()
	return True

	

if verrou() :
	print "verrou activé"
	exit()
	
