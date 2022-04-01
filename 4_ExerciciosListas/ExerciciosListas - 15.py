"""
15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
"""

notas = []
soma = cont = acima = abaixo = 0
while True:
    nota = float(input('Informa um valor: '))
    if nota < 0:
        break
    else:
        notas.append(nota)
    soma += nota
    cont += 1

print(len(notas))  # Mostre a quantidade de valores que foram lidos;
print(notas)  # Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
notas.reverse()  # inverte

for nota in notas:  # Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    print(nota)

print(soma)  # Calcule e mostre a soma dos valores;
media = soma / cont
print(media)  # Calcule e mostre a média dos valores;

for valor in notas:
    if valor > media:
        acima += 1
    if valor < 7:
        abaixo += 1

print(acima)  # Calcule e mostre a quantidade de valores acima da média calculada;
print(abaixo)  # Calcule e mostre a quantidade de valores abaixo de sete;
print('Programa encerrado! ')  # Encerre o programa com uma mensagem;
