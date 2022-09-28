#Exercício 13 - Conversão Monetária
#Autor: Tiago de Freias
#Data atual: 29-Ago-22
#Elaborar um programa que efetue a apresentação do valor da conversão em real
# de um valor lido em dólar. O programa deve solicitar o valor da cotação do dólar
#  e também a quantidade de dólares disponível com o usuário, para que seja apresentado
#   o valor em moeda brasileira.

import os   #Funções do sistema operacional
import time #Módulo que contém funções de tempo
import math #Módulo que contém funções matemáticas

#Constantes e Variáveis
dol=0
qtd=0
real=0

#Leitura de Variáveis
print('Exercício 13 - Conversão Monetária ')
dol = float(input('Digite o valor da cotação do Dólar hoje: '))
qtd = float(input('Digite a quantidade de dólares (US$) disponíveis: '))

#Cálculos
real = dol * qtd

#Exibir Resultados 
print('O Valor da conversão em Reais(R$) é: %.2f' % real)

time.sleep(1)

print("\n")
print("O Programa foi finalizado!!")
os.system('cls') or None
