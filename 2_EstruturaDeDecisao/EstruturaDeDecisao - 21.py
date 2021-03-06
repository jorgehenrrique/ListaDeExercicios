'''
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de
10, uma nota de 5 e quatro notas de 1.
'''

saque = int(input('Informe o valor do saque, de 10 a 600: '))

cem = int(saque / 100)
saque = saque - (cem*100)

cinquenta = int(saque/50)
saque = saque - (cinquenta*50)

dez = int(saque/10)
saque = saque % 10  # outra alternativa, o resto da divisao

cinco = int(saque/5)
saque = saque % 5

um = saque

print(f'Notas R$100,00 = {cem}')
print(f'Notas R$ 50,00 = {cinquenta}')
print(f'Notas R$ 10,00 = {dez}')
print(f'Notas R$  5,00 = {cinco}')
print(f'Notas R$  1,00 = {um:.0f}')