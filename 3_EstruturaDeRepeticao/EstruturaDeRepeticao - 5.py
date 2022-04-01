'''
5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
'''

anos = 0
while True:
    A = float(input('Populacao pais A: '))
    B = float(input('Populacao pais B: '))
    if A > B:
        print('Ordem de populacao invalida! ')
    else:
        break
while True:
    taxaA = float(input('Taxa de crescimento pais A: '))
    taxaB = float(input('Taxa de crescimento pais B: '))
    if taxaA < taxaB:
        print('Ordem de taxa invalida! ')
    else:
        break
while A <= B:
    A += taxaA / 100 * A
    B += taxaB / 100 * B
    anos += 1

print(f'Levara {anos} anos para o pais A ultrapassar ou igualar a populacao do pais B.')
