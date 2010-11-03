# -*- coding: utf-8 -*-

LISTE = "compteur.liste"
VERROU = "compteur.lock"

def message (aString, mode="n"):
	"""Signifie un message:
			- normal 'n'
			- erreur 'e'
	"""
	code = ''
	if mode == "e":			#passe la couleur en rouge pour les erreurs
		code = "\033[31m"
	print code + aString + "\033[0m"	#remet tout à zero

def verrou ():
	"""Verifie l'état du verrou"""
	fluxLock = open(VERROU, "r")
		#message("impossible d'ouvrir le fichier","e")
		#exit()
	etat = fluxLock.readline()
	fluxLock.close()
	if  etat == "unlock":
		return False
	else:
		return True
		
def verrouLock():
	"""Verouille le verrou"""
	fluxLock = open(VERROU, "w")
		#message ("impossible d'ouvrir le fichier, attention le system de verrou est cassé","e")
		#exit()
	fluxLock.write("lock")
	fluxLock.close()
	return True

def verrouUnlock():
	"""Deverouille le verrou"""
	fluxLock = open(VERROU, "w")
		#message ("impossible d'ouvrir le fichier, attention le system de verrou est cassé","e")
		#exit()
	fluxLock.write("unlock")
	fluxLock.close()
	return True
	
if __name__ == "__main__":
	
	
	
	
	
	
	
	
	
