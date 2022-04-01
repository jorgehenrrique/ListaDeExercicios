'''
22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
'''

num = int(input('Um numero: '))

i = 1
cont = 0
while i <= num:
    if num % i == 0:
        cont += 1
    i += 1
print('Divisivel por: ', cont)

if cont <= 2:
    print(f'{num} e primo')
else:
    print(f'{num} nao e primo')
    print('Numeros divisiveis')
    x = 1
    while x <= num:
        if num % x == 0:
            print(x, end=', ')
        x += 1
