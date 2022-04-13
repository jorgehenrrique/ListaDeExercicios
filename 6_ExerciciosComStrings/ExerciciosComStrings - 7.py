"""
7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.
"""

frase = input('Uma frase: ')

spac = ' '
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
cont_espaco = conta = conte = conti = conto = contu = 0
for letra in frase:
    if spac in letra:
        cont_espaco += 1
    if a in letra:
        conta += 1
    if e in letra:
        conte += 1
    if i in letra:
        conti += 1
    if o in letra:
        conto += 1
    if u in letra:
        contu += 1

print(f'Tem {cont_espaco} espacos em branco na frase: {frase}')
print(f'Aparecem a: {conta} vezes\n'
      f'Aparecem e: {conte} vezes\n'
      f'Aparecem i: {conti} vezes\n'
      f'Aparecem o: {conto} vezes\n'
      f'Aparecem u: {contu} vezes')

# Outra maneira

spaco = frase.count(' ')
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

print(f'Tem {spaco} espacos em branco na frase: {frase}')
print(f'Aparecem a: {a} vezes\n'
      f'Aparecem e: {e} vezes\n'
      f'Aparecem i: {i} vezes\n'
      f'Aparecem o: {o} vezes\n'
      f'Aparecem u: {u} vezes')
