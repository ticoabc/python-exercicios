#Lista 5 - Listas
#Exercício 7 - Faça um Programa que leia um vetor de 5 números inteiros,
                #mostre a soma, a multiplicação e os números.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
from functools import reduce
print('Exercício 7 - soma, a multiplicação e os números \n')
lista = []
mult = 1

#Lógica cálculos e exibição de resultados
print()
for numeros in range(1, 6):
    num = int(input('Digite o {}º número: '.format(numeros)))
    lista.append(num)

    #mult = reduce(lambda)
    mult = reduce(lambda x, y : x * y, lista)

    soma = sum(lista)

print('\nOs vetores são: {}\nA soma dos vetores é: {}\nA multiplicação dos vetores é: {}'.format(lista, soma, mult))
