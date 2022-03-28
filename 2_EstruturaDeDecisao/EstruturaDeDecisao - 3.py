'''
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.
'''

caractere = input('Digite uma letra F ou M: ')

if caractere.lower() == 'f':
    print('Feminino')
elif caractere.lower() == 'm':
    print('Masculino')
else:
    print('Sexo invalido!')