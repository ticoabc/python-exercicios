#Lista 3 - Estruturas de decisão
#Exercício 1 - Faça um Programa que peça dois números e imprima o maior deles.
#Autor: Tiago de Freias
#Data atual: 28-Set-22

#Constantes e Variáveis
n1=0
n2=0

#Leitura de Variáveis
print('Exercício 1 - Dois números inteiros...')
n1=int(input('Digite o Primeiro: '))
n2=int(input('Digite o Segundo: '))

#Exibir Resultados 
if n1 > n2:
    print('O maior número digitado é:', n1)
elif n1 < n2:
    print('O maior número digitado é:', n2)
else:
    print('Você não digitou um número válido')
