#Lista 5 - Listas
#Exercício 6 - Faça um Programa que peça as quatro notas de 2 alunos,
                # calcule e armazene num vetor a média de cada aluno,
                    # imprima o número de alunos com média maior ou igual a 7.0.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 6 - 4 notas de 2 alunos \n')
averages = []

#Lógica cálculos e exibição de resultados
for i in range(1, 3):
    soma, average = 0, 0
    for j in range(1, 5):
        nota = float(input('Digite a %dº nota do %dº aluno: ' %(i, j)))
        soma += nota
    average = soma / 4
    averages.append(average)
        
print('\nMédias: ', average)

alunos = 0
for k in averages:
    if k >= 7:
        alunos += 1
print('\nNúmero de alunos com média maior ou igual a 7: %d' % alunos)
