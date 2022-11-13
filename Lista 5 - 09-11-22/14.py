#Lista 5 - Listas
#Exercício 14 - Utilizando listas faça um programa que faça 5 perguntas para
                #uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima?"
#b) "Esteve no local do crime?"
#c) "Mora perto da vítima?"
#d) "Devia para a vítima?"
#e) "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classificado como "Inocente".

#Autor: Tiago de Freias
#Data atual: 10-Nov-22

#Leitura de Variáveis
print('Exercício 14 - Classificação da pessoa no crime\n')

res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

soma_respostas = 0

#Lógica cálculos e exibição de resultados
for i in res: # soma o número de respostas
    soma_respostas += int(i)
    if (soma_respostas < 2):
        print("\nInocente")
    elif (soma_respostas == 2):
        print("\nSuspeita")
    elif (3 <= soma_respostas <= 4):
        print("\nCúmplice")
    elif (soma_respostas == 5):
        print("\nAssassino")

lista_perguntas = ["Telefonou para a vítima? 1/Sim ou 0/Não: ",
"Esteve no local do crime? 1/Sim ou 0/Não: ",
"Mora perto da vítima? 1/Sim ou 0/Não: ",
"Devia para a vítima? 1/Sim ou 0/Não: ",
"Já trabalhou com a vítima? 1/Sim ou 0/Não: "]
res = []
soma_respostas = 0
for i in range(len(lista_perguntas)):
    print(lista_perguntas[i])
    res.append(input()) # adiciona as respostas na lista res
    soma_respostas += int(res[i]) # soma o número de respostas
    status = ["Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]
    if soma_respostas < 2:
        print(status[0])
    else:
        print(status[soma_respostas-1])
