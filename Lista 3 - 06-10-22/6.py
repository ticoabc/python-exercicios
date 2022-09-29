#Lista 3 - Estruturas de decisão
#Exercício 6 - Faça um Programa que leia três números e mostre o maior deles.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
print('Exercício 6 - Três números e mostre o maior deles')
n1=float(input('Digite o 1ª Número: '))
n2=float(input('Digite o 2ª Número: '))
n3=float(input('Digite o 3ª Número: '))

#Lógica e Exibição de Resultados 
if  n1 > n2  and n1 > n3:
    print('Maior número digitado - 1ª Número:', n1)
elif n2 > n1 and n2 > n3:
    print('Maior número digitado - 2ª Número:', n2)
else:
    print('Maior número digitado - 3ª Número:', n3)
