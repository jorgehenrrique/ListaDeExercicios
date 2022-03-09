# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.


idades = []
alturas = []
for i in range(5):
    idades.append(float(input(f'Informe a idade da {i + 1}ª pessoa: ')))
    alturas.append((float(input(f'Informe a altura da {i + 1}ª pessoa: '))))

print('Ordem lida: ')
print(f'Idades: {idades}\n'
      f'Alturas: {alturas}')

print('Ordem inversa: ')
idades.reverse()
alturas.reverse()
print(f'Idades: {idades}\n'
      f'Alturas: {alturas}')
