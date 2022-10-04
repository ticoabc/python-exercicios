#Lista 3 - Estruturas de decisão
#Exercício 25 - 

#Autor: Tiago de Freias
#Data atual: 04-Out-22

#Leitura de Variáveis
print('Exercício 25 - 5 perguntas para uma pessoa')

contagem = 0
tel = str(input('Telefonou para a vítima? '))
if tel == 'sim':
    contagem =+ 1

esteve = str(input('Esteve no local do crime? '))
if esteve == 'sim':
    contagem =+ 1

mora = str(input('Mora perto da vítima? '))
if mora == 'sim':
    contagem =+ 1

deve = str(input('Devia para a vítima? '))
if deve == 'sim':
    contagem =+ 1

trabalhou = str(input('Já trabalhou com a vítima? '))
if trabalhou == 'sim':
    contagem =+ 1

if contagem == 0:
    print('Inocente')
elif contagem == 2:
    print('Suspeita')
elif contagem == 3:
    print('Cúmplice')
elif contagem == 4:
    print('Cúmplice')
elif contagem == 5:
    print('Cúmplice')

print('Contagem = ', contagem)
