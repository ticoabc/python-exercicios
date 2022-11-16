#Lista 3 - Estruturas sequenciais

#Exercício 12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada
    #de qualquer número inteiro entre 1 a 10. O usuário deve informar de
    #qual numero ele deseja ver a tabuada.
    #A saída deve ser conforme o exemplo abaixo:
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 12 - Gerador de tabuada')

n = int(input("digite um numero de 1 a 10: "))
cont = 1

while cont <= 10:
    tab = n * cont
    print(n, "X", cont, "=", tab)
    cont = cont + 1
