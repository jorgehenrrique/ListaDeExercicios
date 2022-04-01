# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vet1 = []
vet2 = []
vet3 = []
vet4 = []
for i in range(10):
    vet1.append(int(input(f'Informe o {i + 1}º numero do vetor um: ')))
    vet2.append(int(input(f'Informe o {i + 1}º numero do vetor dois: ')))
    vet3.append(int(input(f'Informe o {i + 1}º numero do vetor tres: ')))
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])

print(vet4)
