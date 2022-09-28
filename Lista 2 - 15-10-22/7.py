#Lista 2 - Estruturas sequenciais
#Exercício 7 - Faça um Programa que calcule a área de um quadrado,
#em seguida mostre o dobro desta área para o usuário.
#Autor: Tiago de Freias
#Data atual: 14-Set-22

#Constantes e Variáveis
Q=0
A=0
D=0

#Leitura de Variáveis
print('Exercício 7 - Área de um quadrado e seu Dobro')
Q=float(input('Valor do lado do quadrado: '))

#Cálculos
A=Q*Q
D=A**2

#Exibir Resultados 
print('Área do quadrado: ', A)
print('Dobro da Área:   ', D)
