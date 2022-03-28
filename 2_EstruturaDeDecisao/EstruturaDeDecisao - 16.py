'''
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
from math import sqrt

a = float(input('Informe o valor de a: '))

if a != 0:
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('Não possui raizes reais')
    else:
        if delta == 0:
            print('Possui apenas uma raiz real')
            x1 = (-b + sqrt(delta)) / 2 * a
            print(f'A raiz de x1 é {x1:.2f}')
        else:
            x1 = (-b + sqrt(delta)) / 2 * a
            x2 = (-b - sqrt(delta)) / 2 * a
            print(f'A raiz de x1 é {x1:.2f}')
            print(f'A raiz de x2 é {x2:.2f}')
else:
    print(f'A equacao nao e de segundo grau a = {a}')
