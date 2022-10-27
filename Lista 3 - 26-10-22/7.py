#Lista 3 - Estruturas sequenciais

#Exercício 7 - Faça um programa que leia 5 números e informe o maior número.
        

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis
print('Exercício 7 - 5 números e informe o maior número')
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
n5 = float(input("Número 5: "))

lista = [n1, n2, n3, n4, n5]

print("O maior número é: ", max(lista))
