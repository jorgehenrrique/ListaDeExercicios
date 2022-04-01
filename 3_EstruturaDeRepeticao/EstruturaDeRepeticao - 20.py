'''
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
'''

while True:
    while True:
        num = int(input('Um numero: '))
        if 0 < num < 16:
            break
        else:
            print('Numero invalido! ')

    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i

    print(fatorial)
    con = input('Continuar? s ou n: ')
    if con.lower() != 's':
        break
