"""
51. Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

"""

num = int(input('Quantidade de termos: '))

n = m = 1
listan = []
listam = []
print('S = ', end='')
for i in range(1, num):
    print(f'{n} / {m} + ', end='')
    listan.append(n)
    listam.append(m)
    n += 1
    m += 2

print(f'{n} / {m} = {sum(listan)} / {sum(listam)}')
print(f'Soma da serie: {sum(listan) + sum(listam):.2f}')
