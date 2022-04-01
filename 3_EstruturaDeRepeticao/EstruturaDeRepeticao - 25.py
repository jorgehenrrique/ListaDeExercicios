'''
25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
'''

n = int(input('Quantas idades deseja fornecer? '))

media = 0
for i in range(1, n + 1):
    idade = int(input(f'Informe a {i}ª idade: '))
    media += idade

media = media / n
if 0 <= media <= 25:
    print(f'Media: {media:.0f}, Turma jovem!')
elif 26 <= media <= 60:
    print(f'Media: {media:.0f}, Turma adulta!')
elif media > 60:
    print(f'Media: {media:.0f}, Turma idosa!')