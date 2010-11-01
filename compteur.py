# -*- coding: utf-8 -*-

LISTE = "compteur.liste"
VERROU = "compteur.lock"

#--------AFFICHAGE-----------------------------

def message (aString, mode="n"):
	"""Signifie un message:
			- normal 'n'
			- erreur 'e'
	"""
	code = ''
	if mode == "e":			#passe la couleur en rouge pour les erreurs
		code = "\033[31m"
	print code + aString + "\033[0m"	#remet tout à zero
def afficheTout():
	fluxList = open(LISTE,'r')
	for line in fluxList.readline():
		message(line.strip(' \n'))
	flux.close()

def afficheUser(user):
	message (user(user))
	
#-------COMPTES----------------------------
def isUser(user):
	"""renvoye le numero de ligne du compte ou False si inconnu"""
	fluxList = open(LISTE,'r')
	for i, compte in enumerate(fluxList.readline()): 
		if user == compte.split(':')[0]:
			return i
	fluxList.close()
	return False

def user(user):
	"""renvoye le compte de user"""
	fluxList = open(LISTE,'r')
	for compte in fluxList.readline(): 
		if user == compte.split(':')[0]:
			return compte
	fluxList.close()
	return False

def enregistrer(compte):
	if

#-------VERROU---------------------------------

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

#-------INPUT---------------------------------
appendUser(compte, user):
	compte = compte.strip()
	if compte[0] == ':':
		return user+compte
	else :
		return entrer
	
if __name__ == "__main__":
	# On verifie si le verrou est activer, auquel cas on stop
	afficheTout()
	
	while verrou() :
		message( "verrou activé, Veuillez patienter" ) 
		choix = raw_input("arreter 'a' ou reesayer 'r'")
		if choix == 'a': exit()
	
	verrouLock()
	
	lastUser = lastUser()
	print "dernier utilisateur '"+lastUser+"'"
	entrer = raw_input("'user:numberOfCopy' laisser user vide si vous êtes le dernier utilisateur:  >")
	compte = appenduser(entrer,lastUser)
	enregistrer(compte)
	afficheUser(user)
	verrouUnlock()
	
