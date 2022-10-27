#Lista 3 - Estruturas sequenciais

#Exercício 22 - Altere o programa de cálculo dos números primos,
                    #informando, caso o número não seja primo,
                        #por quais número ele é divisível.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 22 - Números Primos 2')

numero = int(input("\nDigite um número: "))
lista = []


if numero % 2 != 0 or numero == 2:
    print("primo")
else:
    for i in range(numero):
        if numero % (i + 1) == 0:

            lista.append(i + 1)

print("Os números divisiveis por ", numero, " são ", lista)
