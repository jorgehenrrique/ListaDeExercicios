'''
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''

nota = int(input('Informe uma nota de 0 a 10: '))

while True:
    if nota < 0 or nota > 10:
        print('Valor inválido! ')
        nota = int(input('Informe uma nota de 0 a 10: '))
    else:
        break