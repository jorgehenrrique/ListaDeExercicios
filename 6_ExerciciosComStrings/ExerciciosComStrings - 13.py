"""
13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada
com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
informando se o usuário ganhou ou perdeu o jogo.
"""
import random


def aleatorio(frase):
    frase_ale = random.choice(frase)
    return frase_ale


arquivo = open('11-jogodaforca.txt')
linhas = arquivo.readlines()
arquivo.close()

palavra = aleatorio(linhas).strip()
palavra2 = ''.join(random.sample(palavra, len(palavra)))
print(palavra2)

tentativas = 6
while True:
    print('Tentativas: ', tentativas)
    print(palavra2)
    resposta = input('Que palavra e essa? : ')
    if resposta == palavra:
        print('Voce acertou a palavra: ', palavra)
        break
    else:
        if tentativas == 1:
            print(f'Vece perdeu, a palavra era: {palavra}')
            break
        tentativas -= 1
