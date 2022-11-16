#Lista 5 - Listas
#Exercício 10 - Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 10 elementos, cujos valores deverão ser compostos
#pelos elementos intercalados dos dois outros vetores.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
print('Exercício 10 - vetores \n')

import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(lista1[i])
	lista3.append(lista2[i])

print (lista1)
print (lista2)
print (lista3)
