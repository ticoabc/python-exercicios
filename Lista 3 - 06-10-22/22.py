#Lista 3 - Estruturas de decisão
#Exercício 22 - Faça um Programa que peça um número inteiro e determine
    #se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

#Autor: Tiago de Freias
#Data atual: 02-Out-22

#Leitura de Variáveis
print('Exercício 22 - Par ou Ímpar?')
n=float(input('Digite um número: '))


#Exibir Resultados 
if (n%2) == 0:
    print('O número digitado é Par')
else:
    print('O número digitado é Ímpar')
