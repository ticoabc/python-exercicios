#Lista 5 - Listas
#Exercício 18 - Qual o melhor jogador após cada jogo?

#Autor: Tiago de Freias
#Data atual: 13-Nov-22

print('Exercício 18 - Enquete: Quem foi o melhor jogador?\n')

jogadores = [0] * 23

while True:
    while True:
        numero = int(input('Digite o número do jogador(0=fim): '))
        if numero > 23 or numero < 0:
            print('Número inválido.')
        else:
            break
    if numero == 0:
        break
    jogadores[numero-1] = jogadores[numero-1] + 1

print('Total de votos: %d' % (sum(jogadores)))
cont = 1
melhor = 0
perc, votos = 0, 0
for j in jogadores:
    print('Jogador %d - votos: %d' % (cont, j))
    print('Percentual %.2f' % ((j * 100) / sum(jogadores)))
    cont += 1

    if j > melhor:
        melhor = cont
        perc = (j * 100) / sum(jogadores)
        votos = j

print('Melhor jogador: %d' % melhor)
