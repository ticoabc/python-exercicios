#Lista 2 - Estruturas sequenciais

#Exercício 16 - Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
M=0

#Leitura de Variáveis
print('Exercício 16 - Loja de Tintas')
M=float(input('Metragem a ser pintada (m2): '))

#Cálculos
LT= M / 3
PT= LT * 80.00

#Exibir Resultados 
print('Quantidade de latas de tinta: ', round(LT,0))
print('Preço total R$: ', round(PT,2))
