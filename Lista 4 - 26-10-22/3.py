#Lista 3 - Estruturas sequenciais

#Exercício 3 - Faça um programa que leia e valide as seguintes informações:
        #a. Nome: maior que 3 caracteres;
        #b. Idade: entre 0 e 150;
        #c. Salário: maior que zero;
        #d. Sexo: 'f' ou 'm';
        #e. Estado Civil: 's', 'c', 'v', 'd';

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Constantes e Variáveis
#Leitura de Variáveis
print('Exercício 3 - Validando informações')
nome = input("Qual seu nome [maior que 3 caracteres]: ")
idade = int(input("Sua idade [entre 0 e 150]: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("A situação ta difícil, mas não tem salário negativo: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser s, c, v ou d: ")
