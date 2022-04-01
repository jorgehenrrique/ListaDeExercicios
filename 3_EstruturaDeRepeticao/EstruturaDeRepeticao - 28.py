'''
28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

quantidade = int(input('Informe a quantidade de CDs adquiridos: '))

cd = media = total = 0
for i in range(1, quantidade + 1):
    cd = float(input(f'Informe o valor do {i}º CD: '))
    media += cd

total = media
media = media / quantidade

print(f'Valor total gasto: {total:.2f}\n'
      f'Media de valor por CD: {media:.2f}')
