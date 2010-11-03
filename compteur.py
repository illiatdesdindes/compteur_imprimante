# -*- coding: utf-8 -*-

LISTE = "compteur.liste"
VERROU = "compteur.lock"

#-------VERROU---------------------------------

def verrou ():
	"""Verifie l'état du verrou"""
	with open(VERROU, "r") as fluxLock:
		etat = fluxLock.readline()
	if etat == "unlock":
		return False
	else:
		return True

def verrouLock():
	"""Verouille le verrou"""
	with open(VERROU, "w") as fluxLock:
	    fluxLock.write("lock")

def verrouUnlock():
	"""Deverouille le verrou"""
	with open(VERROU, 'w') as fluxLock:
	    fluxLock.write("unlock")


if __name__ == "__main__":

