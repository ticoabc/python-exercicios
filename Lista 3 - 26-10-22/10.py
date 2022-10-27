#Lista 3 - Estruturas sequenciais

#Exercício 10 - Faça um programa que receba dois números inteiros e gere
            #os números inteiros que estão no intervalo compreendido por eles.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 10 - Apenas o intervalo compreendido por eles')

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

for i in range(n1 + 1, n2):
        print(i)
for i in range(n2 + 1, n1):
        print(i)

