#Lista 5 - Listas
#Exercício 2 - Faça um Programa que leia um vetor de 10 números reais
                    # e mostre-os na ordem inversa.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 1 - Vetor 5 Números \n')
VectorList = []
print('Insira 5 números')

#Lógica cálculos e exibição de resultados
for i in range(5):
    VectorList.append(input('Número '+ str(i+1) + ':\n'))
    VectorList.reverse() #ordem inversa
print(VectorList)
