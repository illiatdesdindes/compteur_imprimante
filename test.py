from comptes import *

#c = Comptes('compteur.list')
#print c.comptes
#c.ajoute('iren')
#print c.comptes
#c.supprime(bob)
#print c.comptes
#c.enregistre()
#print User.nbUser

a = [User('bob'),User('mec',5), User(data='fred:10')]

for i in a:
    print repr(i)
