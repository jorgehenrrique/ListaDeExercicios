'''
14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.
'''

par = impar = 0
for i in range(10):
    num = int(input(f'{i + 1}º numero:'))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Numeros pares: {par}, numeros impares: {impar}')
