# -*- coding: utf-8 -*-
import math
from Passageiro import Passageiro
from GerentePassageiros import GerentePassageiros
import os

M = 200

def gravarArquivo(ranking):
	arquivo = open("Ranking.dat", "wb")
	arquivo.write(ranking)
	arquivo.close()
	
def calculaDistancia (x1, x2, y1, y2):
	x1 = float (x1)
	x2 = float (x2)
	y1 = float (y1)
	y2 = float (y2)
	print ("---------")
	print x1 , y1, x2, y2
	return math.sqrt( ((x2-x1)**2 ) + (y2-y1)**2)
	

#teste = Passageiro("",3,"O'Sullivan"," Miss. Bridget Mary","female",100,0,0,330909,7.6292,"","Q")
teste = Passageiro("",2,"Quick, ","Mrs. Frederick Charles (Jane Richards)","female",33,0,2,26360,26,"","S")

lista = []
x =GerentePassageiros ("treinamento.csv")

for i in x.getLista():
	if (i.idade == "" or i.pclass == "" or i.tarifa == ""): continue   
	lista.append ((calculaDistancia (float (teste.idade), float (teste.tarifa), float (i.idade),float ( i.tarifa)), i.nome))


	

#lista.sort()
listaDosM = []

for i in lista:
	print i[0]

passageirosSobreviveram = 0
passageirosNaoSobreviveram = 0
print "-------o lista dos M o-------"
for i in range (0,M):
	listaDosM.append (lista[i])
	print lista[i]

	
#verificar quantidade de passageiros que sobreviveram e que não sobreviveram
for i in listaDosM:
	for passageiro in x.getLista():
		if (passageiro.nome == i[1]):
			if (int (passageiro.sobreviveu) == 1):
				passageirosSobreviveram = passageirosSobreviveram + 1
			elif(int (passageiro.sobreviveu) == 0): 
				passageirosNaoSobreviveram = passageirosNaoSobreviveram + 1
			break

print ("passageiros que não sobreviveram = ",passageirosNaoSobreviveram)
print ("passageiros que sobreviveram = ",passageirosSobreviveram)
