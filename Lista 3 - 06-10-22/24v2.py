#Lista 3 - Estruturas de decisão
#Exercício 24 - Faça um Programa que leia 2 números e em seguida pergunte ao
#usuário qual operação ele deseja realizar. O resultado da operação deve ser
#acompanhado de uma frase que diga se o número é:
    #par ou ímpar;
    #positivo ou negativo;
    #inteiro ou decimal.

#Autor: Tiago de Freias
#Data atual: 02-Out-22

#Leitura de Variáveis
print('Exercício 24 - Qual operação ele deseja realizar?'
'\n1 - par ou ímpar'
'\n2 - positivo ou negativo'
'\n3 - inteiro ou decimal'
'\n0 - Sair')
n=int(input('Digite sua opção: '))
while n !=0:
    if n==1:
        n1=float(input('Digite um número: '))
        if (n1%2) == 0:
            print('O número digitado é Par')
        else:
            print('O número digitado é Ímpar')

    elif n==0:
        break
