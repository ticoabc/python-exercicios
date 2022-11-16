#Lista 5 - Listas
#Exercício 11 - Altere o programa anterior, intercalando 3 vetores de
                #10 elementos cada.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
print('Exercício 11 - vetores \n')

import random

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(random.randint(1,100))
	lista4.append(lista1[i])
	lista4.append(lista2[i])
	lista4.append(lista3[i])

print (lista1)
print (lista2)
print (lista3)
print (lista4)
