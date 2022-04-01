'''
11. Altere o programa anterior para mostrar no final a soma dos números.
'''

num1 = int(input('1º numero: '))
num2 = int(input('2º numero: '))

soma = 0
for i in range(num1 + 1, num2):
    print(i, end=' ')
    soma += i

print(f'\nSoma: {soma}')
