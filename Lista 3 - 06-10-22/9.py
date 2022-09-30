#Lista 3 - Estruturas de decisão
#Exercício 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
print('Exercício 9 - Três números em ordem decrescente')
n1=float(input('Digite o 1ª número: '))
n2=float(input('Digite o 2ª número: '))
n3=float(input('Digite o 3ª número: '))

#Lógica e Exibição de Resultados
if  n1 > n2 and n1 > n3 and n2 > n3:
    print('Preço mais barato digitado - 3ª preço R$:',n3)
elif n2 > n1 and n2 < n3 and n3 > n1:
    print('Preço mais barato digitado - 1ª preço R$:',n1)
else:
    print('Preço mais barato digitado - 2ª preço R$:',n2)
