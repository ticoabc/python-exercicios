#Aluno: Tiago de Freias
#11. Faça um programa que receba um número e mostre o resto da divisão por 6.

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
r=0
d=0

#Leitura de Variáveis
os.system('cls') or None
print('Exercício 11 - Resto da Divisão por 6')
r = float(input('Digite o valor: '))

#Cálculos
d = r % 6

#Exibir Resultados 
print('O resto da divisão é: %.2f' % d)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")

