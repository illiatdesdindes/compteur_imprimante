from comptes import *

c = Comptes('compteur.list')
print c
c.ajoute('jack')
c.ajoute('boris',2)
print c
c.enregistre()

