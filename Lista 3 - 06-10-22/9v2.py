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
    print('1ª número:', n1)
    print('2ª número:', n2)
    print('3ª número:', n3)
elif n1 > n2 and n1 > n3 and n2 < n3:
    print('1ª número:', n1)
    print('3ª número:', n3)
    print('2ª número:', n2)
elif n1 < n2 and n2 > n3 and n1 < n3:
    print('2ª número:', n2)
    print('3ª número:', n3)
    print('1ª número:', n1)
elif n1 < n2 and n2 > n3 and n1 > n3:
    print('2ª número:', n2)
    print('1ª número:', n1)
    print('3ª número:', n3)
elif n1 < n3 and n2 < n3 and n1 < n2:
    print('3ª número:', n3)
    print('2ª número:', n2)
    print('1ª número:', n1)
else:
    print('3ª número:', n3)    
    print('1ª número:', n1)
    print('2ª número:', n2)
