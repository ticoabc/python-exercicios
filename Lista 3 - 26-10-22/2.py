#Lista 3 - Estruturas sequenciais

#Exercício 2 - Faça um programa que leia um nome de usuário e a sua senha e
    #não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
        #e voltando a pedir as informações.

#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Constantes e Variáveis
#Leitura de Variáveis

print('Exercício 2 - Cadastro de usuário')

print("Cadastro de usuário:")
usuario=str(input("usuário: "))
senha=str(input("senha: "))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário: "))
	senha=str(input("senha: "))
else:
	print("cadastrado efetuado com sucesso")
