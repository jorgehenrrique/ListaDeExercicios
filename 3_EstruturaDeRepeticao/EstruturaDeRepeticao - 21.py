'''
21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.
'''

num = int(input('Um numero: '))

i = 1
cont = 0
while i <= num:
    if num % i == 0:
        cont += 1
    i += 1

if cont == 2:
    print(f'{num} e primo')
else:
    print(f'{num} nao e primo')
