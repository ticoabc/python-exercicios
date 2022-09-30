#Lista 3 - Estruturas de decisão
#Exercício 8 - Faça um programa que pergunte o preço de três produtos e informe
#qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
print('Exercício 8 - Três produtos, qual o mais barato?')
n1=float(input('Digite o 1ª preço R$: '))
n2=float(input('Digite o 2ª preço R$: '))
n3=float(input('Digite o 3ª preço R$: '))

#Lógica e Exibição de Resultados 
if  n1 > n2 and n1 > n3 and n2 > n3:
    print('Preço mais barato digitado - 3ª preço R$:',n3)
elif n2 > n1 and n2 < n3 and n3 > n1:
    print('Preço mais barato digitado - 1ª preço R$:',n1)
else:
    print('Preço mais barato digitado - 2ª preço R$:',n2)
