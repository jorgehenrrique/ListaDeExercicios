'''
41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor
dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

valorD = float(input('Valor da divida: '))

juros1 = 0 / 100 * valorD
parcela1 = (valorD + juros1)
valorTt1 = juros1 + valorD

juros3 = 10 / 100 * valorD
parcela3 = (valorD + juros3) / 3
valorTt3 = juros3 + valorD

juros6 = 15 / 100 * valorD
parcela6 = (valorD + juros6) / 6
valorTt6 = juros6 + valorD

juros9 = 20 / 100 * valorD
parcela9 = (valorD + juros9) / 9
valorTt9 = juros9 + valorD

juros12 = 25 / 100 * valorD
parcela12 = (valorD + juros12) / 12
valorTt12 = juros12 + valorD

print('Valor da Divida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
print(f'R$ {valorTt1}        {juros1}            1                       R$ {parcela1:.1f}')
print(f'R$ {valorTt3}        {juros3}          3                       R$ {parcela3:.1f}')
print(f'R$ {valorTt6}        {juros6}          6                       R$ {parcela6:.1f}')
print(f'R$ {valorTt9}        {juros9}          9                       R$ {parcela9:.1f}')
print(f'R$ {valorTt12}        {juros12}          12                      R$ {parcela12:.1f}')
