#Lista 2 - Estruturas sequenciais
#Exercício 13 - Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #a. Para homens: (72.7*h) - 58
    #b. Para mulheres: (62.1*h) - 44.7

#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
var='M'
var='H'
A=0

#Leitura de Variáveis
print('Exercício 13 - Peso Ideal')
G=input('Gênero (M ou H): ')
A=float(input('Digite sua Altura: '))

#Cálculos
if(G=='M'):
    P=(62.1 * A) - 44.7
elif(G=='H'):
    P=(72.7 * A) - 58
else:
    print('Erro, digite novamente')
#Exibir Resultados 
print('Peso Ideal: ', P)

