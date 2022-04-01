"""
47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
informada (retirar a melhor e a pior media e depois calcular a média com as notas restantes). As notas não são
informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

nome = 0
while True:
    notas = []
    nome = input('Nome do atleta: ')
    if nome == '':
        break

    for i in range(7):
        notas.append(float(input(f'Nota {i + 1}: ')))

    print('\nResultado final: ')
    print(f'Atleta: {nome}')
    print(f'Melhor nota: {max(notas)}')
    print(f'Pior nota: {min(notas)}')

    notas.sort()
    notas.pop(0)
    notas.pop(5)
    media = sum(notas) / 5
    print(f'Media: {media:.2f} m')
