#Lista 3 - Estruturas de decisão
#Exercício 11 - Faça um programa que recebe o salário de um colaborador e o
#reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo): aumento de 20%
#salários entre R$ 280,00 e R$ 700,00: aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
#salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

#Autor: Tiago de Freias
#Data atual: 29-Set-22

#Leitura de Variáveis
p1 = 0.2
p2 = 0.15
p3 = 0.10
p4 = 0.05

print('Exercício 11 - Salário e Reajuste')
s = float(input('Digite o valor do salário R$: '))

#Lógica cálculos e Exibição de Resultados
if  s <= 280.0:
    r = s * p1
    ns = r + s
    print('salário antes do reajuste R$:', s)
    print('percentual de aumento aplicado:', p1*100,'%')
    print('o valor do aumento R$:', r)
    print('o novo salário, após o aumento R$:', ns)
    
elif s >= 280.0 and s <= 700.0:
     r = s * p2
     ns = r + s
     print('salário antes do reajuste R$:', s)
     print('percentual de aumento aplicado:', p2*100,'%')
     print('o valor do aumento R$:', r)
     print('o novo salário, após o aumento R$:', ns)
     
elif s >= 700.0 and s <= 1500.0:
     r = s * p3
     ns = r + s
     print('salário antes do reajuste R$:', s)
     print('percentual de aumento aplicado:', p3*100,'%')
     print('o valor do aumento R$:', r)
     print('o novo salário, após o aumento R$:', ns)
     
else:
     r = s * p4
     ns = r + s
     print('salário antes do reajuste R$:', s)
     print('percentual de aumento aplicado:', p4*100,'%')
     print('o valor do aumento R$:', r)
     print('o novo salário, após o aumento R$:', ns)




