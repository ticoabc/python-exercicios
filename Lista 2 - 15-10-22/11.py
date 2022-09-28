#Lista 2 - Estruturas sequenciais
#Exercício 11 - Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre:
    #a. o produto do dobro do primeiro com metade do segundo .
    #b. a soma do triplo do primeiro com o terceiro.
    #c. o terceiro elevado ao cubo.
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
A=0
B=0
C=0
R1=0

#Leitura de Variáveis
print('Exercício 11 - Cálculos com Números Interiros')
A=int(input('Digite um valor para A: '))
B=int(input('Digite um valor para B: '))
C=float(input('Digite um valor para C: '))

#Cálculos
R1 = (A*2) + (B/2)
R2 = (A*3) + C
R3 = (C**3)

#Exibir Resultados 
print('o produto do dobro do primeiro com metade do segundo: ', R1)
print('a soma do triplo do primeiro com o terceiro: ', R2)
print('o terceiro elevado ao cubo: ', R3)
