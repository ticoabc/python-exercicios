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
"""print('Exercício 24 - Qual operação ele deseja realizar?'
'\n1 - par ou ímpar'
'\n2 - positivo ou negativo'
'\n3 - inteiro ou decimal'
'\n0 - Sair')
n=int(input('Digite sua opção: '))"""

def function1():
    print("par ou ímpar")
    n=int(input('Digite um número: '))
    if (n%2)==0:
        print('O número digitado é Par')
    else:
        print('O número digitado é ímpar')
        
def function2():
    print("Case 2 selected")

def default():
    print("Value default")

def switch(case):
    if case == "1":
        return function1
    elif case == "2":
        return function2
    elif case == "3":
        return function3
    elif case == "0":
        return function0
    else:
        return default

if __name__ == "__main__":
    #function = switch(case="1")
    function = switch(int(input('Digite sua opção: ')))
    function()
