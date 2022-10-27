#Lista 3 - Estruturas sequenciais

#Exercício 18 - Faça um programa que, dado um conjunto de N números,
                #determine o menor valor, o maior valor e a soma dos valores.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 18 - Maior o Menor e a Soma')
lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = lista.append(float(input("Digite um número: ")))
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))
