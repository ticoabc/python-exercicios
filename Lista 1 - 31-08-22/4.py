#Exercício 4 - Volume de uma lata de óleo
#Autor: Tiago de Freias
#Data atual: 29-Ago-22
#Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
#VOLUME <-- 3.14159 * RAIO2  * ALTURA.

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

os.system("cls")

#Constantes e Variáveis
PI=3.14159
R=0
A=0

#Leitura de Variáveis
print('Exercício 4 - Volume de uma lata de óleo')
R=float(input('Valor do Raio: '))
A=float(input('Valor de Altura: '))

#Cálculos
V=PI*(R**2)*A

#Exibir Resultados 
print('Raio:   ', R)
print('Altura: ', A)
print('Volume: ', V)


time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
