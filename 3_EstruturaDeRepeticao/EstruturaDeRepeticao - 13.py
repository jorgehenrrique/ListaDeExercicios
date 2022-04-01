'''
13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem.
'''

base = int(input('Numero base: '))
expoente = int(input('Numero expoente: '))

resul = 0
for i in range(expoente):
    resul += (base * base)

print(resul)
