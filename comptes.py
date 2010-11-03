
class Comptes
	def __init__(self, dataFile):
		self.comptes={}
		
		with open(dataFile, 'r') as fluxdata:
			contenu = fluxdata.readlines()
		for ligne in contenu:
			ligne = ligne.strip
			self.comptes.append(User(data = ligne).nom,
								User(data = ligne))		

class User:
	
	nbUser = 0
	
	def __ini__(self, nom ='' , compteur=0, data=''):
		if nom:
            self.nom = nom
            self.compteur = compteur
            self.majData()
        elif data:
            self.data = data
            self.majAttr()
        else:
            raise TypeError('mauvaise initialisation: ni nom, ni data n\' ete\
                             fourni')
    
    def majData(self):
        self.nom, self.compteur = self.deserialise()

    def majAttr(self):
        self.data = self.serialise()

    def serialise(self):
        return '{0}:{1}'.format(self.nom, str(self.compteur))

    def deserialise(self):
        return self.data.split(':')
    
    def incr(self, x = 1):
        self.compteur += x
        self.majData()












    
