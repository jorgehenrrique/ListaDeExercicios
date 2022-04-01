'''
39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas.
'''

alunomalto = alunombaixo = numeromalto = numerombaixo = 0
for i in range(10):
    numero = int(input(f'Informe o numero do aluno {i + 1}: '))
    altura = float(input(f'Informe a altura do aluno {i + 1}: '))

    if i == 0:
        alunombaixo = altura
        numerombaixo = numero

    if altura > alunomalto:
        alunomalto = altura
        numeromalto = numero
    if altura < alunombaixo:
        alunombaixo = altura
        numerombaixo = numero

print(f'Aluno mais alto: {alunomalto}, numero: {numeromalto}\n'
      f'Aluno mais baixo: {alunombaixo}, numero: {numerombaixo}')
