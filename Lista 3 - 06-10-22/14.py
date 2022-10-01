#Lista 3 - Estruturas de decisão
#Exercício 14 - Faça um programa que lê as duas notas parciais obtidas
#   por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
    #O algoritmo deve mostrar na tela as notas, a média,
     #o conceito correspondente e a mensagem “APROVADO” se o conceito
        #for A, B ou C ou “REPROVADO” se o conceito for D ou E.

#Autor: Tiago de Freias
#Data atual: 30-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 14 - Média de Aproveitamento / Conceito')
n1=float(input('\nDigite a 1ª Nota: '))
n2=float(input('Digite a 2ª Nota: '))

#Cálculos
m = (n1 + n2) / 2

#Exibir Resultados 
if   m >= 9.0 or m == 10 :
    print(f'\nAprovado A','\nN1:',n1,'\nN2:',n2,'\nMédia:',m)
elif m >= 7.5 and m < 9 :
    print(f'\nAprovado B','\nN1:',n1,'\nN2:',n2,'\nMédia:',m)
elif m >= 6.0 and m < 7.5 :
    print(f'\nAprovado C','\nN1:',n1,'\nN2:',n2,'\nMédia:',m)
elif m >= 4.0 and m < 6 :
    print(f'\nReprovado D','\nN1:',n1,'\nN2:',n2,'\nMédia:',m)
else:
    print(f'\nReprovado E','\nN1:',n1,'\nN2:',n2,'\nMédia:',m)
