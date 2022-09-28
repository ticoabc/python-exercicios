#Aluno: Tiago de Freias
#10. Faça um programa que calcule a área da circunferência.

import os #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
PI=3.14159265359
r=0
A=0

#Leitura de Variáveis
print('Exercício 10 - Área da circunferência')
r = float(input('Digite o valor do raio: '))

#Cálculos
A = PI * (r**2)

#Exibir Resultados 
print('A área da circunferência é: %.2f' % A)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
os.system('cls') or None
