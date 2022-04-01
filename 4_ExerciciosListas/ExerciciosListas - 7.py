# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


numeros = []
soma = 0
multi = 1
for i in range(5):
    numeros.append(int(input(f'Informe o {i + 1}º numero: ')))
    soma += numeros[i]
    multi *= numeros[i]

print(f'Numeros: {numeros} \n'
      f'Soma: {soma} \n'
      f'Multiplicacao: {multi}')
