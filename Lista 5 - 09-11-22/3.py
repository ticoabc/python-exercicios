#Lista 5 - Listas
#Exercício 3 - Faça um Programa que leia 4 notas, mostre as notas e a média
                # na tela.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 3 - 4 notas e a média \n')
NoteList = []
average = 0
print('Insira 4 notas')

#Lógica cálculos e exibição de resultados
for i in range(4):
    NoteList.append(float(input('Nota '+ str(i+1) + ':\n')))
    average += NoteList[i]
    average = average / 4
                    
print('Notas', NoteList)
print('Média', average)
