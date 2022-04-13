"""
4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
"""

str1 = input('Um nome: ')

nome = ''
for i in str1:
    nome += i
    print(nome.upper())
