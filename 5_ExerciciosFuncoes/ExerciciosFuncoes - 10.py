"""
10. Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este
é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto,
se tirar um 7 antes de tirar este Ponto novamente.
"""
from random import randint


def craps():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado = dado1 + dado2
    print(dado)
    if dado == 7 or dado == 11:
        print('Natural: Ganhou! ')
    elif dado == 2 or dado == 3 or dado == 12:
        print('Craps: Perdeu! ')
    if dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 10:
        print('Fez Ponto! ')
        ponto = dado
        while dado != 7:
            dado = randint(2, 12)
            if dado == 7:
                print('Tirou 7, perdeu! ')
            if dado == ponto:
                print(f'Repetiu o ponto: {ponto}, GANHOU!')
                break


craps()
