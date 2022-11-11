#Lista 5 - Listas
#Exercício 7 - Faça um Programa que leia duas listas com 10 elementos cada.
#Gere uma terceira lista de 20 #elementos, cujos valores deverão ser compostos
#pelos elementos intercalados das duas outras listas

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 7 - 3 Listas \n')
ListOne = []
ListTwo = []
InterList = []


#Lógica cálculos e exibição de resultados

#ListOne
for i in range(10):
    print ('ListOne: ')
    ListOne.append(input('Element: ' + str(i+1) + '\n'))

#ListTwo
for j in range(10):
 	print ('ListTwo: ')
 	ListTwo.append(input('Element: ' + str(i+1) + '\n'))

#InterList
for m in range(10):
 	InterList.append(ListOne[m])
 	InterList.append(ListTwo[m])

print (ListOne)
print (ListTwo)
print (InterList)
