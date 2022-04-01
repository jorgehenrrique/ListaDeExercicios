"""
20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor
mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
impostos ou outras particularidades.
Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do
abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
. O salário de cada funcionário, juntamente com o valor do abono;
. O número total de funcionário processados;
. O valor total a ser gasto com o pagamento do abono;
. O número de funcionário que receberá o valor mínimo de 100 reais;
. O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
      Os valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

print('\nProjeção de Gastos com Abono\n============================\n')
salarios = []
cont = 0
while True:
    slr = float(input('Salario: '))
    if slr == 0:
        break
    else:
        salarios.append(slr)
    cont += 1

abono = []
valor_minimo = soma_acumula = 0
for salario in salarios:
    if salario <= 500:
        abono.append(100)
        valor_minimo += 1
    elif salario > 500:
        soma = 20 / 100 * salario
        abono.append(soma)
        soma = 0

print('\nSalario      \t- Abono')
for i in range(len(salarios)):
    print(f'RS {salarios[i]:.2f}       - RS {abono[i]:.2f}')
    soma_acumula += abono[i]

print(f'\nForam processados {cont} colaboradores')
print(f'Total gasto com abonos: R$ {soma_acumula:.2f}')
print(f'Valor mínimo pago a {valor_minimo} colaboradores')
print(f'Maior valor de abono pago: R$ {max(abono):.2f}')
