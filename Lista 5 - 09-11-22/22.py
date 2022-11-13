#Exercício 22 - Sua organização acaba de contratar um estagiário para trabalhar
#no Suporte de Informática, com a intenção de fazer um levantamento nas
#sucatas encontradas nesta área.
#A primeira tarefa dele é testar todos
#os cerca de 200 mouses que se encontram lá, testando e anotando o estado
#de cada um deles, para verificar o que se pode aproveitar deles.

#Autor: Tiago de Freias
#Data atual: 13-Nov-22

print('Exercício 22 - Suporte de Informática \n')

problemas = [0] * 4
print('''   1- necessita da esfera
            2- necessita de limpeza
            3- necessita troca do cabo ou conector
            4- quebrado ou inutilizado ''')
while True:
    identificacao = int(input('Identificação: '))
    if identificacao == 0:
        break
    problema = int(input('Digite o número do problema: '))
    problemas[problema - 1] = problemas[problema - 1] + 1

print('Situação                               Quantidade       Percentual')
total = sum(problemas)
print('1- necessita da esfera                      %d              %.1f%%' % (problemas[0],  (100 * problemas[0]) / total))
print('2- necessita de limpeza                     %d              %.1f%%' % (problemas[1], (100 * problemas[1]) / total))
print('3- necessita troca do cabo ou conector      %d              %.1f%%' % (problemas[2], (100 * problemas[2]) / total))
print('4- quebrado ou inutilizado                  %d              %.1f%%' % (problemas[3], (100 * problemas[3]) / total))
