'''
24. Faça um programa que calcule o mostre a média aritmética de N notas.
'''

n = int(input('Quantas notas deseja fornecer? '))

media = 0
for i in range(1, n + 1):
    nota = float(input(f'Informe a {i}ª nota: '))
    media += nota

media = media / n
print(f'Media das notas fornecidas: {media:.2f}')
