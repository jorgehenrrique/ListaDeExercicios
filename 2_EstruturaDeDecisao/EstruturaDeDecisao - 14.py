'''
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print(f'Nota 1: {n1}\nNota 2: {n2}\nMedia do aluno: {media}')

if media >= 0 and media <= 4:
    conceito = 'e'
elif 4 <= media <= 6:  # opcao igual a de cima, mas de modo simplificado
    conceito = 'd'
elif 6 <= media <= 7.5:
    conceito = 'c'
elif 7.5 <= media <= 9:
    conceito = 'b'
elif 9 <= media <= 10:
    conceito = 'a'

ap = 'abc'
print(f'Conceito: {conceito.title()}')
if conceito in ap:
    print('APROVADO')
else:
    print('REPROVADO')
