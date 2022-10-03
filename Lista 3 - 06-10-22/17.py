#Lista 3 - Estruturas de decisão
#Exercício 17 - Faça um Programa que peça um número correspondente a um
    #determinado ano e em seguida informe se este ano é ou não bissexto.

#Autor: Tiago de Freias
#Data atual: 02-Out-22

#Leitura de Variáveis

print('Exercício 17 - Ano Bissexto ? \n')
year = int(input('Digite o ano no formato [ex: 1982]: '))

#Lógica cálculos e exibição de resultados

#Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto:
    #por exemplo, 1988, 1992 e 1996 são anos bissextos.
#No entanto, ainda há um pequeno erro que deve ser contabilizado.
    #Para eliminar esse erro, o calendário gregoriano estipula que um ano
        #que é uniformemente divisível por 100 (por exemplo, 1900) é um ano
            #bissexto apenas se também é igualmente divisível por 400.

if year %400==0 or year %4==0 and year %100 !=0:

    print('O ano digitado é bissexto')
else:
    print('O ano digitado não é bissexto')
