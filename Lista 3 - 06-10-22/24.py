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
print('f'Exercício 24 - Qual operação ele deseja realizar?'
'1 - par ou ímpar'
'2 - positivo ou negativo'
'3 - inteiro ou decimal')

n1=float(input('Digite o 1° número: '))
n2=float(input('Digite o 2° número: '))

#Lógica e Exibição de Resultados
if (n%2) == 0:
    print('O número digitado é Par')
else:
    print('O número digitado é Ímpar')



if n1 == round(n1):
    print('O 1° número digitado é Inteiro')
    if n2 == round(n2):
        print('O 2° número digitado é Inteiro')
else:
    print('O 1°número digitado é Decimal')
    print('O número digitado arredondado para baixo: ', round(n-0.5))
    print('O número digitado arredondado para cima : ', round(n+0.5))
