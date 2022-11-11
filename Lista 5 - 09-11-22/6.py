#Lista 5 - Listas
#Exercício 6 - Faça um Programa que peça as quatro notas de 2 alunos,
                # calcule e armazene num vetor a média de cada aluno,
                    # imprima o número de alunos com média maior ou igual a 7.0.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 6 - 4 notas de 2 alunos \n')
noteList = []
notasAlunos = []
#print('Insira 4 notas de 10 alunos')

#Lógica cálculos e exibição de resultados
for i in range(2):
    average = 0
    notasAlunos = []
    print ('Aluno: ' + str(i + 1))
    for j in range(4):
        notasAlunos.append(float(input('Nota: ' + str(j+1) + '\n')))
        average += notasAlunos[j]
        print(average)
        average = average / 4
        noteList.append(average)
