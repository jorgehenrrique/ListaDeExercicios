'''
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).
'''

n = int(input('Informe o valor inteiro: '))

if n % 2 == 0:
    print('Numero: Par')
else:
    print('Numero: Impar')