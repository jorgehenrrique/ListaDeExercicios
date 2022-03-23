'''
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a - o produto do dobro do primeiro com metade do segundo .
b - a soma do triplo do primeiro com o terceiro.
c - o terceiro elevado ao cubo.
'''

n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe outro numero inteiro: '))
nr = int(input('Informe um numero real: '))

calculo1 = (n1 * 2) + (n2 / 2)
print(calculo1)

calculo2 = (n1 * 3) + nr
print(calculo2)

calculo3 = nr ** 3
print(calculo3)
