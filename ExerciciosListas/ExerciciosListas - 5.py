# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
PAR = []
IMPARES = []
for i in range(20):
    numeros.append(int(input(f'Informe o {i + 1}º numero: ')))

    if numeros[i] % 2 == 0:
        PAR.append(numeros[i])
    else:
        IMPARES.append(numeros[i])

print(f'Numeros pares: {PAR}\n'
      f'Numeros impares: {IMPARES}\n'
      f'Todos os numeros: {numeros}')
