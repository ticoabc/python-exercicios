#Lista 3 - Estruturas de decisão
#Exercício 24 - Faça um Programa que leia 2 números e em seguida pergunte ao
#usuário qual operação ele deseja realizar. O resultado da operação deve ser
#acompanhado de uma frase que diga se o número é:
    #par ou ímpar;
    #positivo ou negativo;
    #inteiro ou decimal.

#Autor: Tiago de Freias
#Data atual: 02-Out-22

import os

#Leitura de Variáveis
print('Exercício 24 - Qual operação ele deseja realizar?'
'\n1 - par ou ímpar'
'\n2 - positivo ou negativo'
'\n3 - inteiro ou decimal'
'\n0 - Sair')

opcao = int(input('Digite sua opção: '))

if opcao==1:
    print('\n*****Par ou Ímpar ?*****')
    n=int(input('\nDigite um número: '))
    if (n%2)==0:
         print('O número digitado é Par')
    else:
        print('O número digitado é ímpar')
elif opcao==0:
    os.close(1)

if opcao==2:
    print('\n*****Positivo ou Negativo ?*****')
    n=float(input('\nDigite um número: '))
    if n >= 0:
        print('O número digitado é Positivo')
    else:
        print('O número digitado é Negativo')
elif opcao==0:
    os.close(1)
    
if opcao==3:
    print('\n*****Inteiro ou Decimal?*****')
    n=float(input('\nDigite um número: '))
    if n == round(n):
        print('O número digitado é Inteiro')
    else:
        print('O número digitado é Decimal')
        print('O número digitado arredondado para baixo: ', round(n-0.5))
        print('O número digitado arredondado para cima : ', round(n+0.5))
        
elif opcao==0:
    os.close(1)
else:
    print ("Valor invalido")
