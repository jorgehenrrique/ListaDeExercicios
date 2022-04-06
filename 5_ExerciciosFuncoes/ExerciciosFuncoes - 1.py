"""
1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def linhas():
    l = int(input('Ate que linha deve repetir? '))
    for i in range(l + 1):
        for j in range(i):
            print(f'{i}', end=' ')
        print()


linhas()
