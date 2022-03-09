# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
media_maior = []
media = 0
for i in range(10):
    for l in range(4):
        nota = float(input(f'Informe a {l + 1}ª nota do {i + 1}º aluno: '))
        media += nota

    media = media / 4
    notas.append(media)
    nota = 0
    media = 0
    if notas[i] >= 7:
        media_maior.append(notas[i])

print(f'Sao {len(media_maior)} alunos com media maior ou igual a 7. \n'
      f'Medias: {media_maior}')
