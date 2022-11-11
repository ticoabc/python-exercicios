#Lista 5 - Listas
#Exercício 8 - Faça um Programa que peça a idade e a altura de 5 pessoas,
                #armazene cada informação no seu respectivo vetor. Imprima a idade e a altura
                  #na ordem inversa a ordem lida.

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
idades = []
alturas = []
print('Exercício 8 - idade e a altura de 5 pessoas \n')

#Lógica cálculos e exibição de resultados
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('Ordem inversa')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])

print('Ordem lida')
print('Alturas')
print(alturas)

print('Idades')
print(idades)
