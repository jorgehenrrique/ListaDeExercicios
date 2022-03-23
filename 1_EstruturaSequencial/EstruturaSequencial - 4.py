'''
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

media = 0
for i in range(4):
    n = float(input(f'Informa a {i + 1}ª nota: '))
    media += n

print(f'Media: {media / 4}')
