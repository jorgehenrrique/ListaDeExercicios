"""
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vet1 = []
vet2 = []
vet3 = []
for i in range(10):
    vet1.append(int(input(f'Informe o {i + 1}º numero do vetor um: ')))
    vet2.append(int(input(f'Informe o {i + 1}º numero do vetor dois: ')))
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet3)
