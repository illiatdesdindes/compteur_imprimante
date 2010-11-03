
class Comptes:
    def __init__(self, dataFile):
        self.comptes={}
        self.dataFile = dataFile

        with open(dataFile, 'r') as fluxdata:
            contenu = fluxdata.readlines()
        for ligne in contenu:
            ligne = ligne.strip(' \n\r')
            try:
                user = User(data = ligne)
                self.comptes[User(data = ligne).nom] = User(data = ligne)
            except TypeError:
                pass #evite d'enregistrer des lignes vides


    def ajoute(self, nom, x):
        if self.comptes.has_key(nom):
            self.incr(nom, x)
        else :
            self.nouveau(nom, x)

    def nouveau(self, nom, compteur):
        self.comptes[nom] = User(nom, compteur)

    def enregistre(self):
        with open(self.dataFile, 'w') as fluxdata:
            fluxdata.write(str(self))

    def incr(self, nom, x):
    	self.comptes[nom].incr(x)

    def __str__(self):
        contenu = ''
        for user in self.comptes.values():
            contenu += user.data+'\n'
        return contenu

    def __repr__(self):
        return self.comptes

class User:
    nbUser = 0
     # s'il ya des probleme dans le nb de users faire attetion a raise TypeError
     # et a __del__() dans le cas de ligne vide dans le fichier .list

    def __init__(self, nom = '', compteur = 0, data = ''):
        User.nbUser += 1
        if nom:
            self.nom = nom
            self.compteur = compteur
            self.majData()
        elif data:
            self.data = data
            self.majAttr()
        else:
            raise TypeError('mauvaise initialisation: ni nom, ni data n\' ete fourni')


    def majData(self):
        self.data = self.serialise()

    def majAttr(self):
        self.nom, self.compteur = self.deserialise()

    def serialise(self):
        return '{0}:{1}'.format(self.nom, self.compteur)

    def deserialise(self):
        tmp = self.data.split(':')
        return tmp[0], int(tmp[1])

    def incr(self, x = 1):
        self.compteur += x
        self.majData()

    def __del__(self):
        User.nbUser -= 1

    def __str__(self):
        return self.data

    def __repr__(self):
        return "{0} - {1} - {2}".format(self.nom,
                                        self.compteur,
                                        self.data)

