'''
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma = media = 0
for i in range(5):
    num = int(input('Um numero: '))
    soma += num

media = soma / 5
print(f'Soma: {soma} Media: {media}')
