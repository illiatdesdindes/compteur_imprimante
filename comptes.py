
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
		if nom