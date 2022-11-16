#Lista 5 - Listas
#Exercício 10 - Faça um Programa que leia dois vetores com 5 elementos cada.
#Gere um terceiro vetor de 10 elementos, cujos valores deverão ser compostos
#pelos elementos intercalados dos dois outros vetores.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
print('Exercício 10 - vetores \n')
vetor1 = []
vetor2 = []
vetor3 = []

for elemento in range(0, 5):
    vetor1.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 5):
    vetor2.append(int(input("Digite um elemento: ")))
    
for elemento in range(0, 10):
    vetor3.append(vetor1[elemento])
    vetor3.append(vetor2[elemento])

print(vetor3)
