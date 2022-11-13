#Exercício 21 - Faça um programa que carregue uma lista com os modelos de cinco carros
#(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o
#consumo desses carros, isto é, quantos quilômetros cada um desses carros faz
#com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para
#percorrer uma distância de 1000 quilômetros e quanto isto custará,
#considerando um que a gasolina custe R$ 2,25 o litro.

# Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeot        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

#Autor: Tiago de Freias
#Data atual: 13-Nov-22

print('Exercício 21 - O menor consumo é...? \n')

modelos = []
consumos = []

for i in range(1, 6):
    print('Veículo %d' % i)
    modelos.append(input('Nome: '))
    consumos.append(float(input('Km por litro: ')))

print('\nRelatório Final')
cont, consumo, custo = 0, 0, 0
gasto = 0
menorModelo = ''
menor = 0
for m in modelos:
    custo = 1000 / consumos[cont]
    gasto = custo * 2.25
    print('%s  -  %.1f  -  %.1f litros  - R$ %.2f' % (m, consumos[cont], consumo, gasto))
    if cont == 0:
        menor = custo
        menorModelo = m
    if menor < custo:
        menor = custo
        menorModelo = m
    cont += 1
print('O menor consumo é do %s.' % (menorModelo))
