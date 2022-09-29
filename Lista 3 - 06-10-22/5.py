#Lista 3 - Estruturas de decisão
#Exercício 5 - Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#a)A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#b)A mensagem "Reprovado", se a média for menor do que sete;
#c)A mensagem "Aprovado com Distinção", se a média for igual a dez.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 5 - Notas parciais')
n1=float(input('Digite a 1ª Nota: '))
n2=float(input('Digite a 2ª Nota: '))

#Cálculos
m = (n1 + n2) / 2

#Exibir Resultados 
if  m == 10 :
    print('Aluno Aprovado com Distinção!!!')
elif m >= 7 :
    print('Aluno Aprovado!!!')
else:
    print('Aluno Reprovado!!!')
