#Lista 5 - Listas
#Exercício 5 - Faça um Programa que leia 20 números inteiros e armazene-os
                # num vetor. Armazene os números pares no vetor PAR e
                    # os números IMPARES no vetor impar. Imprima os três vetores.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 5 - 20 números inteiros \n')
ParList = []
NotParList = []
ListNumber = []
number = 0
print('Insira 20 números inteiros')

#Lógica cálculos e exibição de resultados
for i in range(20):
    ListNumber.append((int(input('Número: '+ str(i+1) + ':\n'))))
    number = ListNumber[i]
    #print(number)
if(number%2 == 0):
        ParList.append(number)
else:
 	NotParList.append(number)
print(ListNumber)
print(ParList)
print(NotParList)
