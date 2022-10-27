#Lista 3 - Estruturas sequenciais

#Exercício 11 - Altere o programa anterior para mostrar no final a soma dos números.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 11 - Agora a soma dos números')

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

for i in range(n1 + 1, n2):
        print(i)

for i in range(n2 + 1, n1):
        print(i)

print("Soma dos números: ", i + i)
