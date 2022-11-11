#Lista 5 - Listas
#Exercício 8 - Faça um programa que receba a temperatura média de cada mês do ano
# e armazene-as em uma #lista. Após isto, calcule a média anual das temperaturas
# e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
#(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,. . . ).

#Autor: Tiago de Freias
#Data atual: 09-Nov-22

#Leitura de Variáveis
print('Exercício 8 -Temperatura média de cada mês \n')
temperature = []
month = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
average = 0
aboveAverage = []

#Lógica cálculos e exibição de resultados

for i in range(len(month)):
    temperature.append(float(input('Informe a Temperatura media de ' + month[i] + ':\n')))
    average += temperature[i]
    average = average  / len(month)

for i in range(len(month)):
    if(temperature[i] > average):
         aboveAverage.update({month[i] : temperature[i]})

print('Media das temperaturas : Anual -> ' + str(month))
print('Meses com temperaturas acima da media: ' + str(aboveAverage))
