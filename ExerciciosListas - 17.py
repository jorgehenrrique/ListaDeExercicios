while True:
    media = 0
    atleta = input('Atleta: ')
    if atleta == '':
        break
    x = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
    saltos = []
    for i in range(5):
        saltos.append(float(input(f'{x[i]} Salto: ')))
        media += saltos[i]
    media = media / 5
    print()
    print('Resultado final: ')
    print(f'Atleta: {atleta}')
    print(f'Saltos: {saltos}')
    print(f'Media dos saltos: {media} m')
    print()
