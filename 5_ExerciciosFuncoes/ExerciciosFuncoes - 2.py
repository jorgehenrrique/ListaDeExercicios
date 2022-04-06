"""
2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def linhas2():
    l = int(input('Ate que linha deve repetir? '))
    for i in range(l + 1):
        for j in range(i):
            print(f'{j + 1}', end=' ')
        print()


linhas2()
