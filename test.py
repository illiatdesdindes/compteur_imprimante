from comptes import *

c = Comptes('compteur.list')
print c
print User.nbUser
c.ajoute('boi')
c.ajoute('zert',2)
print c
print User.nbUser
c.enregistre()

