#Lista 5 - Listas
#Exercício 17 - Em uma competição de salto em distância cada atleta tem direito
#a três saltos. O resultado do atleta será determinado pela média dos três
#valores restantes. Você deve fazer um programa que receba o nome e 4s três
#distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
#os saltos e a média dos saltos. O programa deve ser encerrado quando não
#for informado o nome do atleta.
#A saída do programa deve ser conforme o exemplo abaixo:

    #1.	Atleta: Rodrigo Curvêllo
    #2.	Primeiro Salto: 6.5 m
    #3.	Segundo Salto: 6.1 m
    #4.	Terceiro Salto: 6.2 m
    #5. Resultado final:
    #6. Atleta: Rodrigo Curvêllo
    #7. Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    #8.	Média dos saltos: 5.9 m

#Autor: Tiago de Freias
#Data atual: 11-Nov-22

print('Exercício 17 - Salto em distância \n')

while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    saltos = []
    for i in range(1, 4):
        saltos.append(float(input('Digite o valor do %dº salto: ' % i)))

    media = sum(saltos) / 3
    print('Resultado final:')
    print('Atleta: %s' % nome)
    print('Saltos: %.1f - %.1f - %.1f ' %(saltos[0], saltos[1], saltos[2]))
    print('Média dos saltos: %.1f m' % media)
