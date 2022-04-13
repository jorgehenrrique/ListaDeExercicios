"""
5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F
"""

nome = input('Um nome: ')

cont = len(nome)
for i in nome:
    print(nome[0:cont].upper())
    cont -= 1
