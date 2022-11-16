#Lista 5 - Listas
#Exercício 12 - Foram anotadas as idades e alturas de 5 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos
#possuem altura inferior à média de altura desses alunos.

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis

print('Exercício 12 - idades e alturas de alunos\n')

idades = []
alturas = []

for i in range(1, 6):
    idade = int(input('Digite a idade do %dº aluno: ' % i))
    altura = float(input('Digite a altura do %dº aluno: ' % i))
    idades.append(idade)
    alturas.append(altura)

media = sum(alturas) / 6
total = 0
for i in range(0, 6):

    if idades[i] > 13 and alturas[i] < media:
        total += 1

print('Total de alunos com mais de 13 anos e altura inferio a media de altura: %d' % total)
