# 16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva
# um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

faixa = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000, 100000]]
posicao = [0] * 9

while True:
    salario = float(input('Valor vendido: '))  # se o valor informado for 0, encerra
    soma = 9 / 100 * salario + 200
    if salario < 1:
        break

    for i in range(len(faixa)):
        if soma > faixa[i][0] and soma < faixa[i][1]:
            posicao[i] += 1

for i in range(len(faixa)):
    print(f'{posicao[i]} vendedores receberam salario no intervalo:  ${faixa[i][0]} - ${faixa[i][1]}')
