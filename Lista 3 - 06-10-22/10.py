#Lista 3 - Estruturas de decisão
#Exercício 10 - Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
print('Exercício 10 - Em que turno você estuda?')
t=str(input('Digite M-matutino ou V-Vespertino ou N- Noturno: ').upper())

#Lógica e Exibição de Resultados
if t == 'M':
    print('Bom Dia!')
elif t == 'V':
    print('Boa Tarde!')
elif t == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
