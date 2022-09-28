#Lista 2 - Estruturas sequenciais
#Exercício 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
A=0
B=0
C=0
D=0
M=0

#Leitura de Variáveis
print('Exercício 4 - Média')
A=int(input('Valor de MB1: '))
B=int(input('Valor da MB2: '))
C=int(input('Valor da MB3: '))
D=int(input('Valor da MB4: '))

#Cálculos
M=(A+B+C+D)/4

#Exibir Resultados 
print('MB1: ', A, 'MB2: ', B, 'MB3: ', C, 'MB4: ', D,'Média: ', M)
