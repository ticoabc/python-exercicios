#Lista 2 - Estruturas sequenciais

#Exercício 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador
#para controlar o rendimento diário de seu trabalho. Toda vez que ele traz
#um peso de peixes maior que o estabelecido pelo regulamento de pesca do
#estado de São Paulo(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na
#variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
P=0
L=50
M=4.00

#Leitura de Variáveis // #Exibir Resultados
print('Exercício 14 - Peso de peixes e calculo do excedente')
P=float(input('Digite o Peso do Pescado: '))

#Cálculos
if(P > L):
    E = P - L
    EXC = E * M
    print('Está além do limite em:', E,'kg')
    print('Multa pelo excesso de peso R$:', EXC)
else:
    print('Parabéns!! Está dentro do limite de peso:', P,'kg')   
