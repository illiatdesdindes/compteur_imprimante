
class Comptes:
	def __init__(self, dataFile):
		self.comptes={}
		self.dataFile = dataFile
		
		with open(dataFile, 'r') as fluxdata:
			contenu = fluxdata.readlines()
		for ligne in contenu:
			ligne = ligne.strip
			self.comptes.append(User(data = ligne).nom, User(data = ligne))

    def ajoute(self, nom, compteur = 0):
        comptes[nom] = User(nom, compteur)
    
    def enregistre(self):
        with open(dataFile, 'w') as fluxdata:
            
    def 
class User:
    nbUser = 0

    def __init__(self, nom = '', compteur = 0, data = ''):
        if nom:
            self.nom = nom
            self.compteur = compteur
            self.majData()
        elif data:
            self.data = data
            self.majAttr()
        else:
            raise TypeError('mauvaise initialisation: ni nom, ni data n\' ete fourni')
        User.nbUser += 1
    
    def majData(self):
        self.data = self.serialise()        

    def majAttr(self):
        self.nom, self.compteur = self.deserialise()

    def serialise(self):
        return '{0}:{1}'.format(self.nom, self.compteur)

    def deserialise(self):
        return self.data.split(':')
    
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










    
