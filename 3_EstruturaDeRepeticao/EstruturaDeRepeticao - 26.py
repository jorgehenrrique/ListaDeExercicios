'''
26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
'''

eleitores = int(input('Numero de eleitores: '))

voto = eleito = A = B = C = 0
print('Entre com as opcoes: A, B ou C, para votar')
for i in range(1, eleitores+1):
    voto = input(f'{i}º Voto: A, B ou C ')
    if voto.lower() == 'a':
        A += 1
    elif voto.lower() == 'b':
        B += 1
    elif voto.lower() == 'c':
        C += 1

if A > B and A > C:
    eleito = 'A'
elif B > C:
    eleito = 'B'
else:
    eleito = 'C'

print(f'Numero total de votos para cada candidato: \n'
      f'Candidato A: {A}\n'
      f'Candidato B: {B}\n'
      f'Candidato C: {C}\n'
      f'Candidato eleito: {eleito}')