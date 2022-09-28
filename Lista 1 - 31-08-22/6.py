#Exercício 6 - Quadrado de um número Interiro
#Autor: Tiago de Freias
#Data atual: 29-Ago-22

# Efetuar a leitura de um número inteiro e apresentar o resultado
# do quadrado do mesmo.

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
A=0
R=0

#Leitura de Variáveis
print('Exercício 6 - Quadrado de um número Interiro')
A=int(input('Digite um valor para A: '))

#Cálculos
R = A**2

#Exibir Resultados 
print('O Quadrado de ', A, 'é: ', R)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
os.system('cls') or None
