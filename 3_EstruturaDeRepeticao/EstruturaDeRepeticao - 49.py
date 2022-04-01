"""
49. Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""

num = int(input('Quantidade de termos: '))

n1 = n2 = 1
listan1 = []
listan2 = []
print('S = ', end='')
for i in range(1, num):
    print(f'{n1} / {n2} + ', end='')
    listan1.append(n1)
    listan2.append(n2)
    n1 += 1
    n2 += 2

print(f'{n1} / {n2} = {sum(listan1)} / {sum(listan2)}')
print(f'Soma da serie: {sum(listan1) / sum(listan2):.2f}')
