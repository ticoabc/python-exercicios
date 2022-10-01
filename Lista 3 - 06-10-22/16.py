#Lista 3 - Estruturas de decisão
#Exercício 16 - Faça um programa que calcule as raízes de uma equação do
#segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a,
#b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#Três lados formam um triângulo quando a soma de quaisquer dois lados
    #for maior que o terceiro;

#Autor: Tiago de Freias
#Data atual: 30-Set-22

import math

#Leitura de Variáveis
print('Exercício 15 - Três lados de um triângulo\n')
a=float(input('Digite o valor de a: '))
b=float(input('Digite o valor de b: '))
c=float(input('Digite o valor de c: '))

#Lógica cálculos

if a==0:
    print('\nNão é uma equação do 2° grau')
else:
    delta = (b ** 2) - (4 * a * c)
    
if delta < 0:
    print('\nDelta:',delta)
    print('O delta é negativo. Equação não possui raízes reais')
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a

if delta == 0:
    print('1 - Raiz real:', x1)
else:
    print('2 - Raizes reais: ', '\nx1: ',x1, '\nx2: ',x2)
