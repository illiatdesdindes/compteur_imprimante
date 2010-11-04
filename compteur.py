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

def lastUserSave(nom):
    """enregistre l'utilisateur courant pour le prochaine usage"""
    with open(LASTUSER,'w') as flux:
        flux.write(nom)

class MyFrame(Frame):
    def __init__(self, titre):
        Frame.__init__(self)
        self.master.title(titre)

        self.comptes = Comptes(LISTE)

        self.message = Label(self, text='Bonjour').pack()

        boiteh1 = Frame(self)
        Label(boiteh1, text='Liste des utilisateurs :').pack(side="left", padx=5)
        self.liste = Label(boiteh1, text=str(self.comptes))
        self.liste.pack(side='right', padx=10)
        boiteh1.pack()

        self.user = StringVar()
        self.compteur = StringVar()

        user = Entry(self,width = 30,justify="center", textvariable=self.user)
        user.bind('<Return>',self.valider)
        user.bind('<KP_Enter>',self.valider)
        user.bind('<Button-1>', self.effaceUser)
        user.pack()

        compteur = Entry(self,width=10, justify='center', textvariable=self.compteur)
        compteur.bind('<Return>',self.valider)
        compteur.bind('<KP_Enter>',self.valider)
        compteur.bind('<Button-1>', self.effaceCompteur)
        compteur.pack()

        self.user.set(lastUser())
        self.compteur.set('1')

        Button(self, text='Ok', command=self.valider).pack()

        self.pack()

    def valider(self,evt=None):
        self.comptes.ajoute(self.user.get(), self.compteur.get())
        self.comptes.enregistre()
        lastUserSave(self.user.get())
        self.liste.configure(text=str(self.comptes))

    def effaceUser(self,evt):
        self.user.set('')
    def effaceCompteur(self,evt):
        self.compteur.set('')






if __name__ == "__main__":
    app = MyFrame("Compteur de copies")

    app.mainloop()

