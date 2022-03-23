'''
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a - Para homens: (72.7*h) - 58
b - Para mulheres: (62.1*h) - 44.7
'''

h = float(input('Informe a altura: '))

pi = (72.7 * h) - 58
pi2 = (62.1 * h) - 44.7

print(f'Peso ideal para homens: {pi:.2f}')
print(f'Peso ideal para mulheres: {pi2:.2f}')
