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
ht = 220

print('Exercício 12 - Folha de Pagamento')
s = float(input('\nDigite o valor da hota trabalhada R$: '))
sb = s * ht

#Lógica cálculos

if  sb <= 900.0:
    irpf = 0
elif sb > 900.0 and sb <= 1500.0:
    irpf = 0.05
elif sb > 1500.0 and sb <= 2500.0:
    irpf = 0.1
else:
    irpf = 0.2

desc_irpf = sb * irpf
desc_inss = sb * 0.1
desc_fgts = sb * 0.11
tot_desct = desc_irpf + desc_inss
sl = sb - tot_desct

#Exibição de Resultados

print('\nSalário Bruto......... R$:', sb) 
print('(-) IR (5%)............R$:', desc_irpf)
print('(-) INSS (10%).........R$:', desc_inss)
print('FGTS (11%).............R$:', desc_fgts)
print('Total de descontos.....R$:', tot_desct)
print('Salário Liquido........R$:', sl)
