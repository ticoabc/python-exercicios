#Lista 3 - Estruturas de decisão
#Exercício 19 - Faça um Programa que leia um número inteiro menor que 1000
#e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros.
#Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades; 12 = 1 dezena e 2 unidades.
#Testar com:
            #326, 300, 100, 320, 310,305, 301, 101, 311, 111,
                #25, 20, 10, 21, 11, 1, 7 e 16.

#Autor: Tiago de Freias
#Data atual: 02-Out-22

#Leitura de Variáveis
num=0
print('Exercício 19 - Quantidade de centenas, dezenas e unidades')
num = int(input('Digite um número: '))

#Lógica cálculos e exibição de resultados
while num<=10:
    print(num)
    num += 1
