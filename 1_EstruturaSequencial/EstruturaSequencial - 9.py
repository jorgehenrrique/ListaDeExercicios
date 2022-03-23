'''
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temperaturaF = float(input('Informe a temperatura em Fahrenheit: '))

celsius = 5 * ((temperaturaF - 32) / 9)

print(f'Temperatura em graus Celsius: {celsius:.1f}')
