"""
45.Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
alunos usarem o programa.
"""
gabarito = [input('Resposta questao 1: '), input('Resposta questao 2: '), input('Resposta questao 3: '),
            input('Resposta questao 4: '), input('Resposta questao 5: '), input('Resposta questao 6: '),
            input('Resposta questao 7: '), input('Resposta questao 8: '), input('Resposta questao 9: '),
            input('Resposta questao 10: ')]  # entrada de gabarito pelo professor
# gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
acertos = []
alunos = media = 0
while True:
    certa = 0
    for i in range(10):
        questao = input(f'Resposta da {i + 1}ª questao: ')
        if questao.lower() == gabarito[i].lower():
            certa += 1
    acertos.append(certa)
    media += certa
    alunos += 1

    encerrar = input('Outro aluno vai utilizar: (s) ou (n): ')
    if encerrar.lower() == 'n':
        break

print(f'\nMaior taxa de acertos: {max(acertos)}')
print(f'Menor taxa de acertos: {min(acertos)}')
print(f'Total de alunos que utilizaram o sistema: {alunos}')
print(f'Media das notas da turma: {media / alunos}\n')

for i in range(alunos):  # bonus
    print(f'O {i + 1}º Aluno acertou: {acertos[i]} questoes; ')
