"""
14. Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e
afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa
que peça uma texto e transforme-o para a grafia leet speak.
"""

texto = input('Um texto: ').lower()

leet = {'a': '4', 'b': '8', 'c': 'C', 'd': 'D', 'e': '3', 'f': 'F', 'g': '9', 'h': 'H', 'i': '1', 'j': 'J', 'k': 'K',
        'l': '1', 'm': 'M', 'n': 'N', 'o': '0', 'p': 'P', 'q': 'Q', 'r': '2', 's': '5', 't': '7', 'u': 'U', 'v': 'V',
        'x': 'X', 'w': 'W', 'z': '2'}

for i in texto:
    if i in leet:
        print(leet[i], end='')
    else:
        print(' ', end='')
