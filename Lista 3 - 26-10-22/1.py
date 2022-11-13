#Lista 3 - Estruturas sequenciais

#Exercício 1 - Faça um programa que peça uma nota, entre zero e dez.
    #Mostre uma mensagem caso o valor seja inválido e continue pedindo até
        #que o usuário informe um valor válido.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Constantes e Variáveis
#Leitura de Variáveis

print('Exercício 1 - Continue pedindo...')

n=float(input("informe um numero de 0 a 10: "))

#Cálculos

while n>10 or n<0:
    n=float(input("informe um numero de 0 a 10: "))
else:
	print("Obrigado!!")
