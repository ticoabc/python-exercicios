#Lista 3 - Estruturas sequenciais

#Exercício 13 - Faça um programa que peça dois números, base e expoente,
    #calcule e mostre o primeiro número elevado ao segundo número.
        #Não utilize a função de potência da linguagem.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 13 - Base e Expoente')

base = int(input("Digite a base: "))
expoente = int(input("Digite expoente: "))
resultado = 1

for i in range(expoente):
    resultado = base * base
    resultado = base * resultado

print('primeiro número elevado ao segundo número: ', resultado)
