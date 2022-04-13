"""
11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
import random


def aleatorio(frase):
    # frase_ale = frase[random.randint(0, len(frase) - 1)].upper().strip()
    frase_ale = random.choice(frase)
    return frase_ale


arquivo = open('11-jogodaforca.txt')
linhas = arquivo.readlines()
arquivo.close()

palavra = aleatorio(linhas).upper().strip()

cont = erro = cont3 = 0
frasel = ['_'] * len(palavra)
while True:
    letra = input('Digite uma letra: ').upper()
    if letra in palavra:
        for l in palavra:
            cont += 1
            if l == letra:
                if l == frasel[cont - 1]:
                    print('Repetido')
                else:
                    frasel[cont - 1] = l
                    cont3 += 1
        if cont3 == len(palavra):
            print(f'Voce ganhou! palavra: {palavra}')
            break
        cont = 0
        print(f'A palavra e: {frasel}')
    else:
        erro += 1
        if erro < 6:
            print(f'Voce errou pela {erro} vez. Tente de novo! ')
        else:
            print(f'Perdeu! palavra era: {palavra}')
            break
