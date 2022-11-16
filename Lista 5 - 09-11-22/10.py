#Lista 5 - Listas
#Exercício 10 - Faça um Programa que leia dois vetores com 5 elementos cada.
#Gere um terceiro vetor de 10 elementos, cujos valores deverão ser compostos
#pelos elementos intercalados dos dois outros vetores.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis

print('Exercício 10 - vetores \n')

print('Primeiro vetor')
vetor1 = []
for i in range(1, 6):
    n = int(input('Digite %dº número: ' % i))
    vetor1.append(n)

print('Segundo vetor')
vetor2 = []
for i in range(1, 6):
    n = int(input('Digite %dº número: ' % i))
    vetor2.append(n)

vetor3 = []
for i in range(0, 10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor3)
