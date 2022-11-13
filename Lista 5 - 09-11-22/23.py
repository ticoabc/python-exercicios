#Exercício 23 - A ACME Inc., uma empresa de 500 funcionários, está tendo
#problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver
#este problema, o Administrador de Rede precisa saber qual o espaço ocupado
#pelos usuários, e identificar os usuários com maior espaço ocupado.
#Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte
#arquivo, chamado "usuarios.txt":

#Autor: Tiago de Freias
#Data atual: 13-Nov-22

print('Exercício 23 - Usuários com maior espaço ocupado \n')

# Abre o arquivo para leitura
arquivo = open('usuarios.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

usuarios = []
espacos = []
total = 0
for l in linhas:
    linha = l.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))
total = sum(espacos)

# Abre o arquivo para escrita
arquivoRelatorio = open('relatorio.txt', 'w')
arquivoRelatorio.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arquivoRelatorio.write(
    '------------------------------------------------------------------------')
arquivoRelatorio.write('\nNr.  Usuario        Espaco utilizado     %% do uso')

for i in range(0, len(usuarios)):
    espacoMB = espacos[i] / (1024.0 * 1024.0)
    percentualUso = espacos[i] / total
    arquivoRelatorio.write('\n%d   -   %s   -   %.2f MB   -   %.2f%%' %
                       (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))

arquivoRelatorio.write('\n\nEspaco total ocupado: %.2f MB' %
                   (total / (1024.0 * 1024.0)))
arquivoRelatorio.write('\n\nEspaco medio ocupado: %.2f MB' %
                   (total / len(usuarios) / (1024.0 * 1024.0)))
# Fecha o arquivo
arquivoRelatorio.close()
