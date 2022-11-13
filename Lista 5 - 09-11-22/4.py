#Lista 5 - Listas
#Exercício 4 - Faça um Programa que leia um vetor de 10 caracteres,
                # e diga quantas consoantes foram lidas. Imprima as consoantes.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 4 - 10 caracteres e consoantes \n')
CharList = []
consoantes = 0
print('Insira 10 caracteres')

#Lógica cálculos e exibição de resultados
for i in range(10):
    CharList.append((input('Caracter '+ str(i+1) + ':\n')))
    char = CharList[i]
    if(char not in ('a','e','i','o','u')):
        consoantes += 1
print('Consoantes: ', consoantes)

