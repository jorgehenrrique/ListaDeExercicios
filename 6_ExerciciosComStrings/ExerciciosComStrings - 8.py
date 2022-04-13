"""
8. Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

frase = input('Uma frase: ')

compara = compara2 = ''
for spac in frase:
    if ' ' not in spac:
        compara = spac + compara

for i in frase:
    if ' ' not in i:
        compara2 += i

if compara2.lower() == compara.lower():
    print(f'{frase} e palindromo!')
else:
    print('Nao e palindromo!')

# Outra maneira ===================

frase2 = frase.lower()
frase2 = frase2.replace(' ', '')

if frase2 == frase2[::-1]:
    print(f'{frase} e Palindromo!')
else:
    print('Nao e um Palindromo!')
