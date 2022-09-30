#Lista 3 - Estruturas de decisão
#Exercício 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
print('Exercício 7 - Três números e mostre o maior e o menor deles')
n1=float(input('Digite o 1ª Número: '))
n2=float(input('Digite o 2ª Número: '))
n3=float(input('Digite o 3ª Número: '))

#Lógica e Exibição de Resultados 
if  n1 > n2  and n1 > n3 and n3 > n2:
    print('Maior número digitado - 1ª Número:', n1)
    print('Menor número digitado:', n2)
elif n2 > n1 and n2 > n3 and n1 > n3:
    print('Maior número digitado - 2ª Número:', n2)
    print('Menor número digitado:', n3)
else:
    print('Maior número digitado - 3ª Número:', n3)
    print('Menor número digitado:', n1)
