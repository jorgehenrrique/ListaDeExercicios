"""
3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def soma(a, b, c):
    total = a + b + c
    return total


n1 = int(input('Um numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
print(soma(n1, n2, n3))
