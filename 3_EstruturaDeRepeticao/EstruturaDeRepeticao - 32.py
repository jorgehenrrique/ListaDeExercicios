'''
32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída
deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

num = int(input('Fatorial de: '))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(fatorial)
