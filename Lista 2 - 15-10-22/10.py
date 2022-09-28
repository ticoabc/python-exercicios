#Lista 2 - Estruturas sequenciais
#Exercício 10 - Faça um Programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Fahrenheit.
#C = 5 * ((F-32) / 9).
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
C=0
F=0

#Leitura de Variáveis
print('Exercício 9 - Conversão de Temperatura')
C=float(input('Digite a temperatura em graus Celsius: '))

#Cálculos
F = C *(9 / 5) + 32
#C = 5 * ((F-32) / 9)

#Exibir Resultados 
print('Temperatura em graus Fahrenheit: ', F)
