#Aluno: Tiago de Freias
#12. Efetuar o cálculo e a apresentação do valor de uma prestação em atraso,
# utilizando a fórmula PRESTAÇÃO <-- VALOR + (VALOR * (TAXA/100) * TEMPO)

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas
os.system('cls') or None

#Constantes e Variáveis
p=0
v=0
tax=0
tem=0
c=100

#Leitura de Variáveis
print('Exercício 12 - Prestação em Atraso')
v = float(input('Digite o valor da Prestação: '))
tax = float(input('Digite o valor da taxa: '))
tem = float(input('Digite o valor da tempo: '))

#Cálculos
p = v + ((v + (tax / c) * tem))

#Exibir Resultados 
print('O Valor da Prestação é: %.2f' % p)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
