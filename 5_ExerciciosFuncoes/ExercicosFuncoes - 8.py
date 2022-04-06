"""
8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def quantidade(numeros):
    digitos = len(str(numeros))
    print(f'Quantidade de caracteres: {digitos}')


n = int(input('Informe um numero: '))
quantidade(n)
