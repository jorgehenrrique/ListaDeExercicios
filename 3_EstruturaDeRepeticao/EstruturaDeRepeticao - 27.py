'''
27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

turmas = int(input('Informe a quantidade de turmas: '))

media = 0
for i in range(1, turmas + 1):
    turma = int(input(f'Quantidade de alunos da turma {i}: '))
    if turma > 40:
        print('Limite de alunos por turma é 40! ')
    else:
        media += turma

media = media / turmas
print(f'Media de alunos por turma = {media:.0f}')
