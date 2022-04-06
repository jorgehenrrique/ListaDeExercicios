"""
9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def reverso(numero):
    numero = str(numero)
    print("Número invertido: ", numero[:: -1])


n = int(input('Informe um numero: '))
reverso(n)
