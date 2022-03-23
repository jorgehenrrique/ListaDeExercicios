'''
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
'''

ganha_hora = float(input('Quanto ganha por hora? '))
horas_trabalha = int(input('Quantas horas trabalhou no mes? '))

total = horas_trabalha * ganha_hora

print(f'Salario do mes: {total}')
