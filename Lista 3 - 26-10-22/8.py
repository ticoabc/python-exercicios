#Lista 3 - Estruturas sequenciais

#Exercício 8 - Faça um programa que leia 5 números e informe a soma
                #e a média dos números.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis
print('Exercício 8 - Soma e Média')

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
n5 = float(input("Número 5: "))

soma = n1 + n2 + n3 + n4 + n5
media = soma / 5

print("Soma: ", soma, "\nMedia: ", media)
