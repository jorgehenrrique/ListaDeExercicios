"""
1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""


def validaip(endIp):
    faixa = endIp.split('.')
    for i in faixa:
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True


ip_arquivo = open("1_enderecoip.txt", "r")
lista_de_linhas = ip_arquivo.readlines()
ip_arquivo.close()

validos = []
invalidos = []
for ip in lista_de_linhas:
    if validaip(ip) is True:
        validos.append(ip)
    else:
        invalidos.append(ip)

saida_arquivo = open('1_endereco_saida.txt', 'w')
saida_arquivo.write('[Enderecos validos:]\n')

for i in range(len(validos)):
    saida_arquivo.write(validos[i])

saida_arquivo.write('\n[Enderecos invalidos:]\n')

for i in range(len(invalidos)):
    saida_arquivo.write(invalidos[i])
saida_arquivo.close()
