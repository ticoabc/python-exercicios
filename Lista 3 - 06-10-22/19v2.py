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

print('Exercício 19v2 - Quantidade de centenas, dezenas e unidades')

#Lógica cálculos e exibição de resultados
num = int(input('Digite um numero inteiro positivo: '))
# Extraindo a unidade
unt = num % 10
# Eliminando a unidade de nosso número
num = (num - unt)/10
# Extraindo a dezena
dez = num % 10
# Eliminando a dezena do número original, fica a centena
num = (num - dez)/10
cent = num
# Fazendo ser inteiros
dez = int(dez)
cent = int(cent)
print(cent,'centena(s),',dez,'dezena(s) e',unt,'unidade(s)')
