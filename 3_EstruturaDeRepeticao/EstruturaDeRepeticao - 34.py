'''
34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
ou não um número primo.
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
