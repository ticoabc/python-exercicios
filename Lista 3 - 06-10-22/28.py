#Lista 3 - Estruturas de decisão
#Exercício 28 - . Escreva um programa que peça o tipo e a quantidade de carne
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da
#compra: tipo e quantidade de carne, preço total, tipo de pagamento,
#valor do desconto e valor a pagar.

#Autor: Tiago de Freias
#Data atual: 04-Out-22

#Leitura de Variáveis

print('Exercício 28 - Hipermercado Tabajara')
print("1- Filé Duplo\n2- Alcatra\n3- Picanha\n")
tipo = int(input("Digite o tipo carne desejada: "))
quantidade = float(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1/ SIM - 2/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
        
if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco
    

print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço.......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)


