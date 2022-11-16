#Lista 3 - Estruturas sequenciais

#Exercício 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 24 - Média aritmética de N notas')
numero_notas = int(input("Digite o número de notas que você irá digitar: "))
count = 0
todas_notas = []

while count < numero_notas:
    notas = todas_notas.append(float(input("Digite a nota: ")))
    count += 1

media = sum(todas_notas) / numero_notas
print("A média é igual a ", media)

