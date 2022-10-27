#Lista 3 - Estruturas sequenciais

#Exercício 23 - Faça um programa que mostre todos os primos entre 1 e N
                    #sendo N um número inteiro fornecido pelo usuário.
                        #O programa deverá mostrar também o número de divisões
                            #que ele executou para encontrar os números primos.
                                #Serão avaliados o funcionamento, o estilo e o número
                                    #de testes (divisões) executados.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 23 - Números Primos 2')
numero = int(input("\nDigite um número: "))
lista = []
divisoes = 0

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1
print("Números primos: ", lista)
print("Número de divisões", divisoes)

