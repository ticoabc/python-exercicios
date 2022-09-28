#Exercício 7 - Tabuada de um número Interiro
#Autor: Tiago de Freias
#Data atual: 29-Ago-22
#Ler um número inteiro positivo e calcular e mostrar a tabuada

import os #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas
os.system('cls');

#Constantes e Variáveis
num=0
cont=0
r=0

#Leitura de Variáveis
print('Exercício 7 - Tabuada de um número Interiro')
num = int(input('Digite um número de 1 a 9: '))

#Cálculos
print()
print('Tabuada do', num)
while cont <= 10:
    r = num*cont
    print(num, 'X', cont, '=', r)
    cont = cont + 1

#Exibir Resultados 
#print(num, 'X', cont, '=', r)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
#os.system('cls') or None
