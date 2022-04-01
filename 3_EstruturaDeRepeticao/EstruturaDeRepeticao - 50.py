"""
50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

num = int(input('Quantidade de termos: '))

h1 = 1
n1 = 2
listah1 = []
listan1 = []
print('H = 1 + ', end='')
for i in range(1, num -1):
    print(f'{h1} / {n1} + ', end='')
    listah1.append(h1)
    listan1.append(n1)
    n1 += 1

listah1.append(1)
print(f'{h1} / {n1} = {sum(listah1)} / {sum(listan1)}')
print(f'Valor de H / N termos: {sum(listah1) / sum(listan1):.2f}')
