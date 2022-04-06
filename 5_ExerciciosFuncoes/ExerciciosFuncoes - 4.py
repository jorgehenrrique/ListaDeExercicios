"""
4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def pn(x):
    if x > 0:
        print('P')
    else:
        print('N')


n1 = int(input('Um numero: '))
pn(n1)
