# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []
vogal = 'aeiou'
consoante = []
for i in range(10):
    caracteres.append(input(f'Informe o {i + 1}º caractere: '))

    if caracteres[i] not in vogal:
        consoante.append(caracteres[i])

print(f'Foram lidas {len(consoante)} consoantes. ')
print(f'Consoantes: {consoante}')
