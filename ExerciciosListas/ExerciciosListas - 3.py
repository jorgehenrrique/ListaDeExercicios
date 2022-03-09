# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
for i in range(4):
    notas.append(float(input(f'Informe a {i + 1}ª nota: ')))

media = sum(notas) / len(notas)
print(f'Notas: {notas} \nMedia das notas: {media:.2f}')
