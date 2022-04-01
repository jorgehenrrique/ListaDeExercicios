"""
42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número
negativo.
"""

inter1 = inter2 = inter3 = inter4 = 0
while True:
    intervalo = int(input('Numero: '))
    if intervalo < 0:
        break

    if 0 <= intervalo <= 25:
        inter1 += 1
    elif 26 <= intervalo <= 50:
        inter2 += 1
    elif 51 <= intervalo <= 75:
        inter3 += 1
    elif 76 <= intervalo <= 100:
        inter4 += 1
    else:
        print('Numero fora do intervalo! ')

print(f'Numeros no intervalo [0-25] = {inter1}\n'
      f'Numeros no intervalo [26-50] = {inter2}\n'
      f'Numeros no intervalo [51-75] = {inter3}\n'
      f'Numeros no intervalo [76-100] = {inter4}')
