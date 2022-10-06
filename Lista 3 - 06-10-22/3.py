#Lista 3 - Estruturas de decisão
#Exercício 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M" ou “O”.
#Conforme a letra escrever: F - Feminino, M - Masculino, O - (Outros Gênero).

#Autor: Tiago de Freias
#Data atual: 28-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 3 - Gênero?')
g=str(input('Digite uma Letra [F - M - O]: ').upper())


#Exibir Resultados
if  g == 'F':
    print('O gênero digitado é Feminino')
elif g == 'M':
    print('O gênero digitado é Masculino')
else:
    print('O gênero digitado é Outros')
