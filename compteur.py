# -*- coding: utf-8 -*-

from Tkinter import *
from comptes import *

LISTE = "compteur.list"
VERROU = "compteur.lock"
LASTUSER = "lastuser"

#-------VERROU---------------------------------

def verrou ():
	"""Verifie l'état du verrou"""
	with open(VERROU, "r") as fluxLock:
		etat = fluxLock.readline()
	if etat == "uself.nlock":
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

def lastUser():
    """retourn le dernier utilisateur"""
    with open(LASTUSER,'r') as flux:
        contenu = flux.read().strip(' \n\r')
    if contenu == '':
        return 'Entrez un nom d\'utilisateur'
    else :
        return contenu

class MyFrame(Frame):
    def __init__(self, titre):
        Frame.__init__(self)
        self.master.title(titre)

        comptes = Comptes(LISTE)

        self.message = Label(self, text='Bonjour').pack()

        boiteh1 = Frame(self)
        boiteh1Texte = Label(boiteh1, text='Liste des utilisateurs :').pack(side="left", padx=5)
        self.liste = Label(boiteh1, text=str(comptes)).pack(side='right', padx=10)
        boiteh1.pack()

        self.user = Entry(self, value=lastUser()).pack()

        self.compteur = Entry(self, value='1').pack()

        self.ok = Button(self, text='Ok').pack()

        self.pack()



if __name__ == "__main__":
    app = MyFrame("Compteur de copies")

    app.mainloop()

