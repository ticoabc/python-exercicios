#Lista 3 - Estruturas de decisão
#Exercício 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Constantes e Variáveis

#Leitura de Variáveis
print('Exercício 4 - Vogal ou Consoante ?')
l=str(input('Digite uma Letra: ').upper())


#Exibir Resultados 
if  l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
    print('A letra digitada é Vogal')
else:
    print('A letra digitada é Consoante')
