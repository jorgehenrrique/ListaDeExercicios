'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
n3 = int(input('Informe o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'Maior numero: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior numero: {n2}')
else:
    print(f'Maior numero: {n3}')