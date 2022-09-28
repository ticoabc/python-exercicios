#Lista 2 - Estruturas sequenciais

#Exercício 17 - Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
#de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
#preços em 3 situações:
    #comprar apenas latas de 18 litros;
    #comprar apenas galões de 3,6 litros;
    #misturar latas e galões, de forma que o desperdício de tinta seja menor.
    #Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    #considere latas cheias.


#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
M=0

#Leitura de Variáveis
print('Exercício 17 - Loja de Tintas 2')
M=float(input('Metragem a ser pintada (m2): '))

#Cálculos
LT= (M / 6)
FG= (LT * 0.1) + LT

if FG <= 10.8:
        PT2= FG * 25.00
else:    
        PT1= FG * 80.00
        

#Exibir Resultados
#round(a, n): recebe um float e um numero e retorna o float arredondado com este
#numero de casas decimais.
print('Quantidade de litros de tinta:', round(FG,0))
print('Quantidade de latas de tinta (18L):', round(LT,0))
print('Quantidade de latas de tinta (3,6L):', round(LT,0))
print('Preço total R$', round(PT1,0))
print('Preço total R$', round(PT2,0))
