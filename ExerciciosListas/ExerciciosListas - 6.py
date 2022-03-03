# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num 
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual 
# a 7.0.

def alunos(n):  # soma das 4 notas, n vezes
    soma = 0
    notas = []
    for i in range(n):
        for x in range(4):
            recebe = float(input(f'Informa a {x + 1}a nota do aluno {i + 1}: '))
            soma += recebe
        soma = soma / 4
        notas.append(soma)  # soma das notas armazenado na lista
        soma = 0
    return notas


media = alunos(3)  # Efetuar a funcao de media de 4 notas nx, 10x
media_maior = []
cont = 0
print('Todas as medias: ',media)
for l in range(len(media)):
    if media[l] >= 7.0:
        media_maior.append(media[l])
        cont += 1
print(f'Numero de alunos com media maior ou igual a 7.0: {cont}, medias dos alunos: {media_maior}')