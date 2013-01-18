# -*- coding: utf-8 -*-

class Passageiro(object):
	def __init__ (self, Ssobreviveu, Spclass, Snome, Ssobrenome, Ssexo, Sidade, SirmaosEsposa, SpaisFilhos, Sticket, Starifa, Scabine, Sembarque):
		self.sobreviveu = Ssobreviveu
		self.pclass = Spclass
		self.nome = Snome + Ssobrenome
		self.sexo = Ssexo
		self.idade = Sidade
		self.irmaosEsposa = SirmaosEsposa
		self.paisFilhos = SpaisFilhos
		self.ticket= Sticket
		self.tarifa = Starifa
		self.cabine = Scabine
		self.embarque = Sembarque
