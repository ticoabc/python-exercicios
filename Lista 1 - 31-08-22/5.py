#Exercício 5 - Troca dos valores inteiros
#Autor: Tiago de Freias
#Data atual: 29-Ago-22

# Ler dois valores inteiros para as variáveis A e B e efetuar
# a troca dos valores de forma que a variável A passe a possuir o
# valor da variável B e a variável B passe a possuir o valor da variável A.
# Apresentar os valores trocados.

import os #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
A=0
B=0
TROCA=0

#Leitura de Variáveis
print('Exercício 5 - Troca dos valores inteiros')
A=int(input('Digite um valor para A: '))
B=int(input('Digite um valor para B: '))

#Cálculos
TROCA=A
A=B
B=TROCA

#Exibir Resultados 
print('Resultado de A: ', A, 'Resultado de B: ', B)

time.sleep(1)

print("\n")
#print("O Programa foi finalizado!!")
os.system('cls') or None
