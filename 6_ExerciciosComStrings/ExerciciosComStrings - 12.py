"""
12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso
deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
separador.
Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

print('Valida e corrige numero de telefone')
num = input('Telefone: ')

num = num.replace('-', '')
if len(num) < 8:
    print('Telefone possui 7 digitos. Vou acrescentar o digito tres na frente.')
    num = '3' + num

num2 = ''
cont = 0
if '-' not in num:
    for i in num:
        cont += 1
        num2 += i
        if cont == 4:
            num2 += '-'

print(f'Telefone corrigido sem formatacao: {num}')
print(f'Telefone corrigido com formatacao: {num2}')
