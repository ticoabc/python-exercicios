#Lista 5 - Listas
#Exercício 15 - Faça um programa que leia um número indeterminado de valores,
#correspondentes a notas, encerrando a entrada de dados quando for informado um
#valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

#Autor: Tiago de Freias
#Data atual: 11-Nov-22

print('Exercício 15 - Número indeterminado de valores \n')
#Leitura de Variáveis
notas = []
print('Digite -1 para encerrar o programa')

#Lógica cálculos
while True:
    nota = float(input('Digite a nota: '))
    if nota < 0:
        print('O programa foi encerrado')
        break
    notas.append(nota)

media = sum(notas) / len(notas)
acima = 0
abaixo = 0
for n in notas:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1

#Exibição de resultados
print('Quantidade de valores lidos: %d' % (len(notas)))
print('A soma dos valores é: %.2f' % (sum(notas)))
print('Quantidade de valores acima da média %d' % acima)
print('Quantidade de valores abaixo de sete: %d' % abaixo)
