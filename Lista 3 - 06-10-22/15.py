#Lista 3 - Estruturas de decisão
#Exercício 15 - Faça um Programa que peça os 3 lados de um triângulo.
    #O programa deverá informar se os valores podem ser um triângulo.
        #Indique, caso os lados formem um triângulo, se o mesmo é:
            #equilátero, isósceles ou escaleno.

#Três lados formam um triângulo quando a soma de quaisquer dois lados
    #for maior que o terceiro;

#Autor: Tiago de Freias
#Data atual: 30-Set-22

#Leitura de Variáveis
print('Exercício 15 - Três lados de um triângulo\n')
l1=float(input('Digite o 1ª lado: '))
l2=float(input('Digite o 2ª lado: '))
l3=float(input('Digite o 3ª lado: '))

#Lógica cálculos

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
    print('\nNão é um triângulo')
elif (l1 == l2) and (l1 == l3):
    print('\nTriângulo Equilátero')
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print('\nTriângulo Isósceles')
else:
    print('\nTriângulo Escaleno')
