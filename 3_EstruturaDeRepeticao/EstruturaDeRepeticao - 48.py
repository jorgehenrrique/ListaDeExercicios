"""
48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

num = input('Informe um numero inteiro: ')
print('Numero inverso: ', num[:: -1])
