from comptes import *

c = Comptes('compteur.list')

c.ajoute('boi')
c.ajoute('zert',2)
c.incr('boi')
c.incr('zert',2)
c.enregistre()

print c

