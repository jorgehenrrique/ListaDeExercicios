'''
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

T_arquivo = float(input('Tamanho do arquivo em MB: '))
ve_Mbps = float(input('Velocidade de internet em Mbps: '))

ve_MB = ve_Mbps / 8
tempo_down = T_arquivo / ve_MB

if tempo_down > 60:
    tempo_minutos = tempo_down / 60
    print(f'O arquivo sera baixado em: {tempo_minutos:.0f} minutos')
else:
    print(f'O arquivo sera baixado em: {tempo_down:.0f} segundos')
