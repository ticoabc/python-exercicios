#Lista 3 - Estruturas de decisão
#Exercício 12 - Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
#(conforme tabela) e 3% para o Sindicato e que o FGTS corresponde a 11%.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220): R$ 1100,00
#(-) IR (5%): R$   55,00  
#(-) INSS (10%): R$ 110,00
#FGTS (11%): R$ 121,00
#Total de descontos: R$ 165,00
#Salário Liquido: R$ 935,00

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
h=220
desc_inss=0.10
desc_fgts=0.11


print('Exercício 12 - Folha de Pagamento')
s = float(input('Digite o valor da hota trabalhada R$: '))

#Lógica cálculos e Exibição de Resultados
if  s <= 900.0:
    sb = s * h
    inss = sb * desc_inss
    fgts = sb * desc_fgts
    tot_desc = inss + fgts
    sl = sb - tot_desc
    
    print('Salário Bruto R$:', sb)
    print('(-) IR (5%):', 'Isento')
    print('(-) INSS (10%) R$:', inss)
    print('FGTS (11%) R$:', fgts)
    print('Total de descontos R$:', tot_desc)
    print('Salário Liquido R$:', sl)
     
elif:
     r = s * p4
     ns = r + s
     print('salário antes do reajuste R$:', s)
     print('percentual de aumento aplicado:', p4*100,'%')
     print('o valor do aumento R$:', r)
     print('o novo salário, após o aumento R$:', ns)




