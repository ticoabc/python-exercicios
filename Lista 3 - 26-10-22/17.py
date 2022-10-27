#Lista 3 - Estruturas sequenciais

#Exercício 16 - Faça um programa que calcule o fatorial de um número inteiro
                    #fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 17 - Fatorial !N')
numero = int(input("Digite um número: "))
count1 = 0
count = 1
while count1 < numero:
    fatorial = numero * (numero - count)
    count = count - 1
    count1 = count + 1

print(fatorial)
