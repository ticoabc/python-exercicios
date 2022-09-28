#Exercício 8 - Troca idade
#Autor: Tiago de Freias
#Data atual: 29-Ago-22
#Faça um algoritmo que leia a idade de uma pessoa expressa em dias
# e mostre-a expressa em anos, meses e dias.

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
dia=0
dias=0
mes=0
ano=0

#Leitura de Variáveis
os.system('cls');
print('Exercício 8 - Troca idade')
dias = float(input('Digite a idede (em dias) de alguma pessoa: '))

#Cálculos
ano = (dias / 365)
mes = (dias % 365) / 30
dia = (dias % 365) % 30

#Exibir Resultados 
print('A idade em anos: %.2f' % ano)
print('A idade em meses: %.2f' % mes)
print('A idade em dias: %.2f' % dia)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")

