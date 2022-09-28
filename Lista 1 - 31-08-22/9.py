#Exercício 9 - TTroca idade 2
#Autor: Tiago de Freias
#Data atual: 29-Ago-22
#Faça um algoritmo que leia a idade de uma pessoa expressa em:
# ano, mês e dia e mostre-as em dias.

import os #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas
os.system('clear');
#Constantes e Variáveis
#anos=0
#mes=0
#dias=0
#total=0

#Leitura de Variáveis
print('Exercício 9 - Troca idade 2')
anos = float(input('Digite a idede (em anos) de alguma pessoa: '))
meses = float(input('Digite quantos meses: '))
dias = float(input('Digite quantos dias: '))

#Cálculos
total = ((anos * 365) + (meses * 30)) + dias

#Exibir Resultados 
print('A idade em dias: %.2f' % total)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
