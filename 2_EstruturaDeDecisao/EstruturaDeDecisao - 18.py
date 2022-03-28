'''
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

dia = int(input('Informe um dia: '))
mes = int(input('Informe um mes: '))
ano = int(input('Informe um ano: '))

if 0 < dia <= 31:
    if 0 < mes <= 12:
        if ano >= 0:
            print(f'Data válida: {dia}/{mes}/{ano}')
        else:
            print('Data invalida! ')
    else:
        print('Data invalida! ')
else:
    print('Data invalida! ')
