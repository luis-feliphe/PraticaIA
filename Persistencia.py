# -*- coding: utf-8 -*-
import math
from Passageiro import Passageiro
#import pickle
import os

M = 10

def gravarArquivo(ranking):
	arquivo = open("Ranking.dat", "wb")
	arquivo.write(ranking)
	arquivo.close()
	
def calculaDistancia (x1, x2, y1, y2):
	if (x1 == "" or x2=="" or y1=="" or y2==""or x1 == " "):
		return 1000
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

def funcaoOrdenacao(self,a,b):
	if (a[1] == b[1]):
		return (-1) * cmp(a[0], b[0])
	return cmp(a[1], b[1])

	
	
todosDados= lerArquivo("treinamento.csv")
#linha1 = todosDados[0].split(",")
cont = 0 
dadosSplit =[]
#dando o split nos dados 
for i in todosDados:
	if (cont == 0):
		cont = cont + 1
		pass
	dadosSplit.append(i.split(","))


listaPassageirosSplit =[]

#separando dados como split
for i in dadosSplit:
	if ((i[0] == "0" )or( i[0]=="1")):
		listaPassageirosSplit.append(i)


#cria objetos
listaPassageiros = []
for i in listaPassageirosSplit:
	listaPassageiros.append(Passageiro(i[0],i[1], i[2],i[3], i[4], i[5],i[6],i[7],i[8],i[9],i[10],i[11] ))



#ler dados de teste
#dadosTeste = lerArquivo("teste.csv")
#calcular todas as distancias
Passageiro(i[0],i[1], i[2],i[3], i[4], i[5],i[6],i[7],i[8],i[9],i[10],i[11] )

teste = Passageiro("",3,"O'Sullivan"," Miss. Bridget Mary","female",37,0,0,330909,7.6292,"","Q")
print (teste.idade)

lista = []
for i in listaPassageiros:
	print ("dados\nidade " )
	print(teste.idade )
	print (" class " )
	print (teste.pclass )
	print (" \nidade" )
	print (i.idade )
	if (i.idade == ""): continue   
	print ("  class")
	print (i.pclass )
	print (" nome do segundo elemento ")
	print (i.nome )
	print (" \n------\n")
	lista.append ((calculaDistancia (float (teste.idade), float (teste.pclass), float (i.idade),float ( i.pclass)), i.nome))

lista.sort()
for i in range (0,M):
	print lista[i]	




