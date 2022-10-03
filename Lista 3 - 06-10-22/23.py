#Lista 3 - Estruturas de decisão
#Exercício 23 - Faça um Programa que peça um número e informe se o número
    #é inteiro ou decimal. Dica: utilize uma função de arredondamento

#Autor: Tiago de Freias
#Data atual: 02-Out-22

#Leitura de Variáveis
print('Exercício 23 - Inteiro ou Decimal?')
n=float(input('Digite um número: '))

#Lógica e Exibição de Resultados 
if n == round(n):
    print('O número digitado é Inteiro')
else:
    print('O número digitado é Decimal')
    print('O número digitado arredondado para baixo: ', round(n-0.5))
    print('O número digitado arredondado para cima : ', round(n+0.5))
