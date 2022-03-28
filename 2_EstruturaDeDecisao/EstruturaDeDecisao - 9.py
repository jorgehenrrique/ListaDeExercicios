'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
        meio = n2
    else:
        menor = n2
        meio = n3
elif n2 > n3 and n2 > n1:
    maior = n2
    if n3 > n1:
        menor = n1
        meio = n3
    else:
        menor = n3
        meio = n1
else:
    maior = n3
    if n2 > n1:
        menor = n1
        meio = n2
    else:
        menor = n2
        meio = n1

print('Ordem decrescente: ', maior, meio, menor)