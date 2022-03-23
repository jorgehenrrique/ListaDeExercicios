'''
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

15 x 1,8 = 27 + 32 = 59 ºF
'''

temperaturaC = float(input('Informe a temperatura em Celcius: '))

fahrenheit = temperaturaC * 1.8 + 32

print(f'Temperatura em graus Celsius: {fahrenheit:.1f}')
