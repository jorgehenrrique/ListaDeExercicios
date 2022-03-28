'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogal = ['a', 'e', 'i', 'o', 'u']
letra = input('Informe uma letra: ')

if letra in vogal:
    print(f'A letra: [{letra}] e uma vogal. ')
else:
    print(f'A letra: [{letra}] e uma consoante. ')