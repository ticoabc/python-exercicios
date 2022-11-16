#Lista 5 - Listas
#Exercício 14 - Utilizando listas faça um programa que faça 5 perguntas para
                #uma pessoa sobre um crime. As perguntas são:
'''
    a.) "Telefonou para a vítima?"
    b.) "Esteve no local do crime?"
    c.) "Mora perto da vítima?"
    d.) "Devia para a vítima?"
    e.) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada  "Suspeita", entre 3 e 4 como
    "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
print('Exercício 14 - Classificação da pessoa no crime\n')

cont = 0
telefonar = str(input('Você telefonou para a vítima?(s/n) ').lower())
if telefonar == 's':
    cont += 1
estar = str(input('Você esteve no local do crime?(s/n) ').lower())
if estar == 's':
    cont += 1
morar = str(input('Você mora perto da vítima?(s/n) ').lower())
if morar == 's':
    cont += 1
dever = str(input('Você devia para a vítima?(s/n) ').lower())
if dever == 's':
    cont += 1
trabalhar = str(input('Você já trabalhou com a vítima?(s/n) ').lower())
if trabalhar == 's':
    cont += 1

if cont < 2:
    print('Pessoa Inocente!!!')
elif cont == 2:
    print('Pessoa Cúmplice!!')  
elif cont == 3:
    print('Pessoa Cúmplice!!')
elif cont == 4:
    print('Pessoa Cúmplice!!')
elif cont == 5:
    print('Pessoa Assassino')

print('Contador é igual a ',cont)
