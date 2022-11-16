#Lista 3 - Estruturas sequenciais

#Exercício 25 - Faça um programa que peça para n pessoas a sua idade,
                    #ao final o programa devera verificar se a média
                        #de idade da turma varia entre 0 e 25,26 e 60
                            #e maior que 60; e então, dizer se a turma é jovem,
                                #adulta ou idosa, conforme a média calculada.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 25 - A turma é Jovem, Adulta ou Idosa')

n_pessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))
lista = []

for i in range(n_pessoas):
    idade = lista.append(int(input("Digite a idade: ")))


if sum(lista) / len(lista) < 25:
    print("jovem")
elif sum(lista) / len(lista) >= 25 and sum(lista) / len(lista) < 60:
    print("adulto")
else:
    print("idosa")
