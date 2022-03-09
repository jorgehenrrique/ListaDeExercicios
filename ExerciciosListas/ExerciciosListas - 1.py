# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vet = []
for i in range(5):
    vet.append(int(input(f'Informe o {i + 1}º numero: ')))

print(vet)
