#Lista 3 - Estruturas sequenciais

#Exercício 16 - A série de Fibonacci é formada pela
    #seqüência 0,1,1,2,3,5,8,13,21,34,55,...
        #Faça um programa que gere a série até que o valor seja maior que 500.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 16 - Mais uma série de Fibonacci...')
ultimo = 1
penultimo = 1
print(ultimo)
print(penultimo)
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo)
    else:
        print("O proximo valor será maior que 500")
