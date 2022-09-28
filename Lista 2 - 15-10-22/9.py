#Lista 2 - Estruturas sequenciais
#Exercício 9 - Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
C=0
F=0

#Leitura de Variáveis
print('Exercício 9 - Conversão de Temperatura')
F=float(input('Digite a temperatura em graus Fahrenheit: '))

#Cálculos
C = 5 * ((F-32) / 9)

#Exibir Resultados 
print('Temperatura em graus Celsius: ', C)
