"""
2. Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
usuário pode digitar letras maiúsculas ou minúsculas.
"""

str1 = input('Um nome: ')

nome = ''
for i in str1:
    nome = i.upper() + nome

print(nome)