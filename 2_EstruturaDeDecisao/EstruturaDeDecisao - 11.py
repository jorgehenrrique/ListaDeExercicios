'''
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Informe seu salario: '))


print(f'Salario antes do reajuste: {salario}')
if salario <= 280:
    aumento1 = 20 / 100 * salario
    print(f'Aplicado 20% ao reajuste, valor= {aumento1:.2f}')
    aumento1 += salario
    print('Novo salario: ',aumento1)
elif salario <= 700:
    aumento2 = 15 / 100 * salario
    print(f'Aplicado 15% ao reajuste, valor = {aumento2:.2f}')
    aumento2 += salario
    print('Novo salario: ',aumento2)
elif salario <= 1500:
    aumento3 = 10 / 100 * salario
    print(f'Aplicado 10% ao reajuste, valor = {aumento3:.2f}')
    aumento3 += salario
    print('Novo salario: ',aumento3)
elif salario > 1500:
    aumento4 = 5 / 100 * salario
    print(f'Aplicado 5% ao reajuste, valor = {aumento4:.2f}')
    aumento4 += salario
    print('Novo salario: ',aumento4)