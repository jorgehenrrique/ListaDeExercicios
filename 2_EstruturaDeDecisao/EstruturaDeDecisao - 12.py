'''
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
 mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_h = int(input('Valor da hora trabalhada: '))
horas_t = float(input('Quantidade de horas trabalhadas: '))

salario = horas_t * valor_h
print(f'Salario Bruto: ({valor_h} * {horas_t})   \t\t   : R$ {salario:.2f}')

IR = INSS = FGTS = salario_liq = total_desc = 0
if salario <= 900:
    INSS = 10 / 100 * salario
    FGTS = 11 / 100 * salario
    total_desc = INSS
    salario_liq = salario - total_desc
elif salario <= 1500:
    IR = 5 / 100 * salario
    INSS = 10 / 100 * salario
    FGTS = 11 / 100 * salario
    total_desc = IR + INSS
    salario_liq = salario - total_desc
elif salario <= 2500:
    IR = 10 / 100 * salario
    INSS = 10 / 100 * salario
    FGTS = 11 / 100 * salario
    total_desc = IR + INSS
    salario_liq = salario - total_desc
elif salario > 2500:
    IR = 20 / 100 * salario
    INSS = 10 / 100 * salario
    FGTS = 11 / 100 * salario
    total_desc = IR + INSS
    salario_liq = salario - total_desc

print(f'(-) IR (5%)    \t\t                   : R$ {IR:.2f}')
print(f'(-) INSS ( 10%)   \t\t                : R$ {INSS:.2f}')
print(f'FGTS (11%)   \t\t                     : R$ {FGTS:.2f}')
print(f'Total de descontos   \t\t             : R$ {total_desc:.2f}')
print(f'Salário Liquido   \t\t                : R$ {salario_liq:.2f}')
