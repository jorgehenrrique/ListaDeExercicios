'''
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
 a - salário bruto.
 b - quanto pagou ao INSS.
 c - quanto pagou ao sindicato.
 d - o salário líquido.
 e - calcule os descontos e o salário líquido, conforme a tabela abaixo:

 + Salário Bruto : R$
 - IR (11%) : R$
 - INSS (8%) : R$
 - Sindicato ( 5%) : R$
 = Salário Liquido : R$
 Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganha_hora = float(input('Quanto ganha por hora? '))
horas_trabalho = int(input('Quantas horas trabalhou no mes? '))

salario = ganha_hora * horas_trabalho

IR = 11 / 100 * salario

INSS = 8 / 100 * salario

sindicato = 5 / 100 * salario

print(f'Salario bruto: {salario}')
print(f'Pagou de INSS: {INSS}')
print(f'Pagou ao sindicato: {sindicato}')

salario_l = salario - IR - INSS - sindicato
print(f'Salario liquido: {salario_l}')

