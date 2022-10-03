#Lista 3 - Estruturas de decisão
#Exercício 20 - Faça um programa para a leitura de três notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#a)A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
#b)A mensagem "Reprovado", se a média for menor do que 7;
#c)A mensagem "Aprovado com Distinção", se a média for igual a dez.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 20 - Notas parciais 2')
n1=float(input('Digite a 1ª Nota: '))
n2=float(input('Digite a 2ª Nota: '))
n3=float(input('Digite a 3ª Nota: '))

#Cálculos
m = (n1 + n2 + n3) / 3

#Exibir Resultados 
if  m == 10 :
    print('Aluno Aprovado com Distinção!!!')
elif m >= 7 :
    print('Aluno Aprovado!!!')
else:
    print('Aluno Reprovado!!!')
