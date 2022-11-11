#Lista 5 - Listas
#Exercício 9 - Faça um Programa que leia um vetor A com 10 números inteiros,
                #calcule e mostre a soma dos quadrados dos elementos do vetor.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
numeros = []



print('Exercício 9 - soma dos quadrados dos elementos \n')

#Lógica cálculos e exibição de resultados
for i in range(1, 11):
    n = int(input('Digite %dº número: ' % i))
    numeros.append(n)

for num in numeros:
    print('%d^2 = %d' % (num, (num**2)))
