'''
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('Responda com (s) ou (n): ')
perguntas = [input('Telefonou para a vítima?'), input('Esteve no local do crime?'), input('Mora perto da vítima?'),
             input('Devia para a vítima?'), input('Já trabalhou com a vítima?')]

s = 0
for i in range(5):
    if 's' in perguntas[i].lower():
        s += 1

if s == 2:
    print('Suspeita')
elif 3 <= s <= 4:
    print('Cúmplice')
elif s == 5:
    print('Assassino')
else:
    print('Inocente')