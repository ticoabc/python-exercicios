#Lista 2 - Estruturas sequenciais
#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

#Autor: Tiago de Freias
#Data atual: 28-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 18 - Velocidade de Download')
arq=float(input('Informe o tamanho do arquivo em MB: '))
vel=float(input('Informe a velocidade de sua internet (em MBp/s): '))

#Cálculos
tmp = (arq / vel)

#Exibir Resultados 
print('Tempo aproximado de download: %.2f Segundos ' %(tmp))
print('Tempo aproximado de download: %.2f Minutos ' %(tmp / 60))
