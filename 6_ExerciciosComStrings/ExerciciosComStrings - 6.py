"""
6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
nome do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""


def dataExtenso(data):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
             ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
             ['outubro', 31], ['novembro', 30], ['dezembro', 31]]

    data = data.split('/')
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f'Voce nasceu em {dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')


def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28


DataNasci = input('Informe a data de nascimento, ex: 29/10/1973: ')
dataExtenso(DataNasci)
