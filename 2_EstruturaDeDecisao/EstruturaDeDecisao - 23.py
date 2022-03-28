'''
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
'''

n = float(input('Informe um numero: '))

if n == round(n):  # opcao um, funcao de arrendondamento
    print('Metodo round:')
    print("Inteiro")
else:
    print("Decimal")

if n == int(n):  # opcao dois
    print('Metodo tipo:')
    print('Inteiro')
else:
    print('Decimal')

if n % 1 == 0: # opcao tres
    print('Metodo resto:')
    print("Inteiro")
else:
    print("Decimal")