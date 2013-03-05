# -*- coding: utf-8 -*-
import math
from Passageiro import Passageiro
from GerentePassageiros import GerentePassageiros
from GerentePassageirosTeste import GerentePassageirosTeste

import os

M = 10

def gravarArquivo(dados):
	arquivo = open("resultadoDoPrograma.dat", "wb")
	arquivo.write(dados)
	arquivo.close()
	
def calculaDistancia (x1, x2, y1, y2):
	x1 = float (x1)
	x2 = float (x2)
	y1 = float (y1)
	y2 = float (y2)
	return math.sqrt( ((x2-x1)**2 ) + (y2-y1)**2)

def lerArquivo(var):
	if (os.path.isfile(var)):
		arquivo = open(var)
		lista =  arquivo.readlines()
		arquivo.close()
		return lista
	return []


#lendo dados de treinamento
dadosTreinamento =GerentePassageiros ("treinamento.csv")



# Lendo dados de teste 
dadosASeremCompletados = GerentePassageirosTeste("teste.csv")
print ("---------aqui a quantidade de dados -----------")
print len (dadosASeremCompletados.getLista())

listaSaida = []
listaDistancias = []
saida = ""

#iniciando computação de dados 
for passageiroIncompleto in dadosASeremCompletados.getLista():
	listaDistancias = []
	for passageiroDeTreinamento in dadosTreinamento.getLista():
		#remove passageiros incompletos
		if (passageiroDeTreinamento.idade == "" or passageiroDeTreinamento.pclass == "" or passageiroDeTreinamento.tarifa == ""): continue   
		if (passageiroIncompleto.idade == ""):
			passageiroIncompleto.idade = 25
		if (passageiroIncompleto.pclass == "" ):
			passageiroInconpleto.pclass = 2
		if (passageiroIncompleto.tarifa == ""):
			passageiroIncompleto.tarifa = 7.25
		#print passageiroIncompleto.nome ," - ",passageiroDeTreinamento.nome

		listaDistancias.append ((calculaDistancia (float (passageiroIncompleto.pclass), float (passageiroDeTreinamento.pclass), float (passageiroIncompleto.tarifa),float ( passageiroDeTreinamento.tarifa)), passageiroDeTreinamento.nome))
	
	listaDosM = []
	passageirosSobreviveram = 0
	passageirosNaoSobreviveram = 0
	#separar os M dados da distancia
	listaDistancias.sort()

	if M <= len (listaDistancias):
		for i in range (0,M):
			listaDosM.append (listaDistancias[i])
	#listaDosM.sort()

	
	#verificar quantidade de passageiros que sobreviveram e que não sobreviveram
	for passageiroDosM in listaDosM:
		for passageiro in dadosTreinamento.getLista():
			if (passageiro.nome == passageiroDosM[1]):
				if (int (passageiro.sobreviveu) == 1):
					passageirosSobreviveram = passageirosSobreviveram + 1
				elif(int (passageiro.sobreviveu) == 0): 
					passageirosNaoSobreviveram = passageirosNaoSobreviveram + 1
				break
	
	sobreviveu = 100
	if (passageirosNaoSobreviveram >passageirosSobreviveram ):
		sobreviveu = 0
	else:
		sobreviveu = 1

	saida += str(sobreviveu)+"\n"
	listaSaida.append((passageiroIncompleto.nome , sobreviveu))


	
gravarArquivo (saida)
dadosReais = lerArquivo ("resposta.txt")
dadosArtificiais = lerArquivo ("resultadoDoPrograma.dat")

contadorAcertos = 0
for i in range (0, len(dadosReais)):
	if dadosArtificiais[i] == dadosReais[i]:
		contadorAcertos += 1

print ("proporcao de acertos:  ", "%.2f"%(100.0*(float(contadorAcertos)/float(len(dadosReais)))), " %")