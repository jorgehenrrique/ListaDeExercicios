''''
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
'''

p1 = float(input('Preco do primeiro produto: '))
p2 = float(input('Preco do segundo produto: '))
p3 = float(input('Preco do terceiro produto: '))

if p1 < p2 and p1 < p3:
    print(f'Compre o produto um por R$ {p1}')
elif p2 < p3:
    print(f'Maior o produto dois por R$ {p2}')
else:
    print(f'Maior o produto tres por R$ {p3}')