# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
# a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

media = 0
for mes in range(len(meses)):
    temperaturas.append(float(input(f'Informe a temperatura media de {meses[mes]}: ')))
    media += temperaturas[mes]

media = media / len(temperaturas)

print(f'\nTemperaturas acima da média anual {media:.2f}: \n')
for temp in range(len(temperaturas)):
    if temperaturas[temp] > media:
        print(f'{temp + 1} - {meses[temp]}: {temperaturas[temp]:.2f}')
