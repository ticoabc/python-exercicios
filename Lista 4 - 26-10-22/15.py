#Lista 3 - Estruturas sequenciais

#Exercício 15 - A série de Fibonacci é formada pela
                #seqüência 1,1,2,3,5,8,13,21,34,55,...
                    #Faça um programa capaz de gerar a série até o n−ésimo termo.
        
#Autor: Tiago de Freias
#Data atual: 26-Out-22

#Leitura de Variáveis

print('Exercício 15 - A série de Fibonacci...')
ultimo = 1
penultimo = 1
count = 1
print(ultimo)
print(penultimo)
while count <= 9:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)
