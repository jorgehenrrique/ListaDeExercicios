# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vet = []
for i in range(10):
    vet.append(float(input(f'Informe o {i + 1}º numero: ')))

vet.reverse()
print(vet)
