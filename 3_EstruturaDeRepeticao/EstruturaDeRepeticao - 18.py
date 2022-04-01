'''
18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

conjunto = int(input('Quantos numeros deseja fornecer: '))

menor = 10000
maior = soma = 0
while conjunto > 0:
    conjunto -= 1
    valor = int(input('Informe um valor: '))
    soma += valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

print(f'Maior valor: {maior}\n'
      f'Menor valor: {menor}\n'
      f'Soma dos valores: {soma}')
