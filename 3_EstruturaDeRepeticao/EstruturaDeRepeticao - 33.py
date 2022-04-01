'''
33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
'''

print('Digite: (0) para parar ')
menor = 100
maior = media = cont = 0
while True:
    temperatura = float(input('Informe a temperatura: '))
    if temperatura <= 0:
        break
    if temperatura > maior:
        maior = temperatura
    elif temperatura < menor:
        menor = temperatura
    cont += 1
    media += temperatura

media = media / cont
print(f'Menor temperatura: {menor:.2f}\n'
      f'Temperatura media: {media:.2f}\n'
      f'Maior temperatura: {maior:.2f}')
