# -*- coding: utf-8 -*-
from Passageiro import Passageiro
import os

class GerentePassageiros(object):

	def lerArquivo(self, var):
		if (os.path.isfile(var)):
			arquivo = open(var)
			lista =  arquivo.readlines()
			arquivo.close()
			return lista
		return []

	def funcaoOrdenacao(self,a,b):
		if (a[1] == b[1]):
			return (-1) * cmp(a[0], b[0])
		return cmp(a[1], b[1])

	def criarObjetosNaLista(self,lista):
		listaPassageiros = []
		for i in lista:
			listaPassageiros.append(Passageiro(i[0],i[1], i[2],i[3], i[4], i[5],i[6],i[7],i[8],i[9],i[10],i[11] ))
		return listaPassageiros
		
	def organizarDados(self, dados):
		cont = 0 		
		dadosSplit =[]
		#dando o split nos dados 
		for i in dados:
			if (cont == 0):
				cont = cont + 1
				pass
			dadosSplit.append(i.split(","))
		
		
		
		listaPassageirosSplit = []
		for i in dadosSplit:
			if ((i[0] == "survived")):#"0" )or( i[0]=="1")):
				continue
			listaPassageirosSplit.append(i)
		
		#cria objetos
		listaPassageiros = []
		listaPassageiros = self.criarObjetosNaLista(listaPassageirosSplit)
		return listaPassageiros


		
	def __init__ (self, endereco):
		self.endereco = endereco
		dadosAMinerar = self.lerArquivo(endereco)
		self.lista = self.organizarDados(dadosAMinerar)
		self.mapaPalavras = {}
		
	def getLista (self):
		return self.lista
		