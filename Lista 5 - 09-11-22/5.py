#Lista 5 - Listas
#Exercício 5 - Faça um Programa que leia 6 números inteiros e armazene-os
                # num vetor. Armazene os números pares no vetor PAR e
                # os números IMPARES no vetor impar. Imprima os três vetores.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 5 - 6 números inteiros \n')
ParList = []
NotParList = []
ListNumber = []
number = 0
print('Insira 6 números inteiros \n')

#Lógica cálculos e exibição de resultados
for i in range(1, 6):

    n = int(input('Digite o %dº Número: ' %i))
    ListNumber.append(n)
    if(n%2 == 0):
            ParList.append(n)
    else:
            NotParList.append(n)
            
print('\nVetor', ListNumber)
print('vetor PAR', ParList)
print('vetor ÍMPAR', NotParList)
