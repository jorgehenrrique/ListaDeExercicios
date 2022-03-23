'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.
'''

area = float(input('Quantos metros quadrados de area a ser pintada? '))

litros = area / 6

if area % 108 == 0:
    latas = area / 108
else:
    latas = int(area / 108) + 1

preco = latas * 80

print('1ª opcao: ')
print(f'Quantidade de latas: {latas:.2f}')
print(f'Preço: {preco:.2f}')

litros = area / 6

if area % 21.6 == 0:
    galoes = area / 21.6
else:
    galoes = int(area / 21.6) + 1

precog = galoes * 25

print('2ª opcao: ')
print(f'Quantidade de galoes: {galoes:.2f}')
print(f'Preço: {precog:.2f}')

# mistura
misturaL = int(litros / 18)
misturaG = int((litros - (misturaL * 18)) / 3.6)

if litros - (misturaL * 18) % 3.6 != 0:
    misturaG += 1

print('3ª opcao: ')
print(f'Mistura: {misturaL} latas e {misturaG} galoes = %.2f' % ((misturaL * 80) + (misturaG * 25)))
