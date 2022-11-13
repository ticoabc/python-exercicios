#Lista 5 - Listas
#Exercício 20 - As Organizações Tabajara resolveram dar um abono aos seus
#colaboradores em reconhecimento ao bom resultado alcançado durante o ano
#que passou. Para isto contratou você para desenvolver a aplicação que servirá
#como uma projeção de quanto será gasto com o pagamento deste abono.

#Autor: Tiago de Freias
#Data atual: 13-Nov-22

print('Exercício 20 - Abono aos seus colaboradores\n')

print('Digite 0 para encerrar o programa')
salarios = [] 
while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    salarios.append(salario)

print('Projeção de Gastos com Abono')
print('============================')

print('Salário - Abono')
colab, abonos, minimo = 0, 0, 0
maior = 0
for s in salarios:
    abono = (salario * 20) / 100
    colab +=1
    if abono < 100:
        abono = 100
        minimo += 1
    if abono > maior:
        maior = abono
    abonos += abono
    print('R$ %.2f - R$ %.2f' % (s, abono))

#print('Foram processados %d colaboradores' % (sum(colab)))
print('Foram processados %d colaboradores' % colab)
print('Total gasto com abonos: R$ %.2f' % abonos)
print('Valor mínimo pago a %d colaboradores' % minimo)
print('Maior valor de abono pago: R$ %.2f' % maior)
