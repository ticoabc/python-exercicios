#Lista 3 - Estruturas de decisão
#Exercício teste

#Autor: Tiago de Freias
#Data atual: 03-Out-22

#Leitura de Variáveis

print ('Exercício 24 - Qual operação ele deseja realizar?'
'\n1 - par ou ímpar'
'\n2 - positivo ou negativo'
'\n3 - inteiro ou decimal'
'\n0 - Sair')

opcao = int(input('Digite sua opção: '))

#q = float(raw_input("Digite sua opção: "))

if opcao==1:
    n=int(input('Digite um número: '))
    if (n%2)==0:
        print('O número digitado é Par')
    else:
        print('O número digitado é ímpar')
elif opcao==0:
    exit()
else:
    print ("Valor invalido")
