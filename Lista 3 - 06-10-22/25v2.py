#Lista 3 - Estruturas de decisão
#Exercício 25 - Faça um programa que faça 5 perguntas para uma pessoa
#sobre um crime. As perguntas são:
                                    #"Telefonou para a vítima?"
                                    #"Esteve no local do crime?"
                                    #"Mora perto da vítima?"
                                    #"Devia para a vítima?"
                                    #"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder:
#positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

#Autor: Tiago de Freias
#Data atual: 04-Out-22

#Leitura de Variáveis

res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

#soma o número de respostas e exibir Resultados
soma_respostas = res1 + res2 + res3 + res4 + res5
if (soma_respostas < 2):
    print("\nInocente")
elif (soma_respostas == 2):
    print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
    print("\nCúmplice")
elif (soma_respostas == 5):
    print("\nAssassino")
