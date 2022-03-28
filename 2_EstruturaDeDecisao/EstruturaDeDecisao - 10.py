'''
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Em que turno voce estuda, Matutino, Vespertino ou Noturno?\n'
              'Responda com: M, V ou N ')

if turno.lower() == 'm':
    print('Bom Dia!')
elif turno.lower() == 'v':
    print('Boa Tarde!')
elif turno.lower() == 'n':
    print('Boa Noite!')
else:
    print('Valor Inválido!')