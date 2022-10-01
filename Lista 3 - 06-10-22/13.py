#Lista 3 - Estruturas de decisão
#Exercício 13 - Faça um Programa que leia um número e exiba o dia
#   correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#       se digitar outro valor deve aparecer valor inválido

#Autor: Tiago de Freias
#Data atual: 30-Set-22

#Leitura de Variáveis
print('Exercício 13 - Dia da semana')
d=float(input('Digite um número: '))

#Lógica e Exibição de Resultados
if d == 1 :
    print('1 - Domingo')
elif d == 2:
    print('2 - Segunda')
elif d == 3:
    print('3 - Terça')
elif d == 4:
    print('4 - Quarta')
elif d == 5:
    print('5 - Quinta')
elif d == 6:
    print('6 - Sexta')
elif d == 7:
    print('7 - Sábado')
else:
    print('Valor Inválido!')
