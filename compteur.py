LISTE = "compteur.liste"
VERROU = "compteur.lock"

def erreur (aString):
	print aString

def verrou ():
	if ! fluxLock = open(VERROU, "r") :
		erreur("impossible d'ouvrir le fichier")
		exit()
	etat = fluxLock.readline()
	fluxLock.close()
	if  etat == "unlock":
		return True
	else:
		return False
		
def verrouLock():
	if ! fluxLock = open(VERROU, "w") :
		erreur ("impossible d'ouvrir le fichier, attention le system de verrou est cassé")
		exit()
	fluxLock.write("true")
	fluxLock.close()
	return True

	

if verrou() :
	print "verrou activé"
	exit()


	