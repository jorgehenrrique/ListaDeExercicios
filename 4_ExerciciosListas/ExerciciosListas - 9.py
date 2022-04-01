"""
9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
do vetor.
"""

numeros = []
for i in range(10):
    numeros.append(int(input(f'Informe o {i + 1}º numero: ')))

for num in numeros:
    print(f'{num}ˆ2 = {num**2}')
