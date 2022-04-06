"""
11. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
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
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')


def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28


dataExtenso('25/9/2022')
dataExtenso('29/02/2021')
