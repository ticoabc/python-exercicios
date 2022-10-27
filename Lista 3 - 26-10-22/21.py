#Lista 3 - Estruturas sequenciais

#Exercício 21 - Faça um programa que peça um número inteiro e determine se ele
                    #é ou não um número primo. Um número primo é aquele que
                        #é divisível somente por ele mesmo e por 1.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 21 - Número Primo')
numero = int(input("\nDigite um número: "))

if numero % 2 == 0 and numero != 2:
    print("não é um número primo")
else:
    print("É um número primo")

