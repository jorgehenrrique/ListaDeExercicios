'''
35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
'''

n = int(input('Digite um numero: '))

for i in range(1, n + 1):
    cont = 0
    for y in range(1, i + 1):
        if i % y == 0:
            cont += 1

    if cont <= 2:
        print(f'{i} E numero primo')
