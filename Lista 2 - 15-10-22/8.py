#Lista 2 - Estruturas sequenciais
#Exercício 8 - Faça um Programa que pergunte
#quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
#em seguida mostre o dobro desta área para o usuário.
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
HT=0
H=0
ST=0

#Leitura de Variáveis
print('Exercício 8 - Cálculo de salário')
HT=float(input('Valor da hora trabalhada: '))
H=float(input('Total de horas trabalhadas no mês: '))

#Cálculos
ST=(HT*H)

#Exibir Resultados 
print('Salário Mensal: ', ST)
