#Lista 2 - Estruturas sequenciais

#Exercício 15 - Faça um Programa que pergunte quanto você ganha por hora
#e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que
#são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$
    #Obs.: Salário Bruto - Descontos = Salário Líquido.

#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
HT=0
H=0
IRPF=0
INSS=0
SNDC=0
ST=0
SL=0
#Leitura de Variáveis
print('Exercício 15 - Cálculo de salário com descontos')
HT=float(input('Valor da hora trabalhada: '))
H=float(input('Total de horas trabalhadas no mês: '))

#Cálculos
ST=(HT*H)
IRPF=ST * 0.11
INSS=ST * 0.08
SNDC=ST * 0.05
SL=ST-(IRPF+INSS+SNDC)

#Exibir Resultados 
print('+ Salário Bruto Mensal R$: ', ST)
print('- IR (11%)R$: ', IRPF)
print('- INSS (8%)R$: ', INSS)
print('- Sindicato (5%)R$: ', SNDC)
print('= Salário Líquido R$: ', SL)
