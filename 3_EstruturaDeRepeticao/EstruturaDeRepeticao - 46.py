"""
46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
nome = maior = 0
melhor = ''
while True:
    saltos = []
    nome = input('Nome do atleta: ')
    if nome == '':
        break

    for i in range(5):
        saltos.append(float(input(f'Distancia do {i + 1}ª salto: ')))

    print(f'\nAtleta: {nome}\n')
    for i in range(len(ordem)):
        print(f'{ordem[i]} Salto: {saltos[i]} m ')

    print(f'\nMelhor salto: {max(saltos)}')
    print(f'Pior salto: {min(saltos)}')

    saltos.sort()
    saltos.pop(0)
    saltos.pop(3)
    media = sum(saltos) / 3
    print(f'Media dos demais saltos: {media:.1f} m')

    if media > maior:
        maior = media
        melhor = nome

print('\nResultado final: ')
print(f'{melhor}: {maior:.1f} m')