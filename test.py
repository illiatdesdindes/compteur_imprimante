from comptes import *

c = Comptes('compteur.list')
print c.comptes
c.ajoute('iren')
print c.comptes
c.supprime(bob)
print c.comptes
c.enregistre()
#print User.nbUser