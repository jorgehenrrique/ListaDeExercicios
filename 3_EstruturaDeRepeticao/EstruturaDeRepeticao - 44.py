"""
44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

jose = joao = maria = tereza = nulo = branco = 0
voto = total = totalN = totalB = 0
print('Vote para os seguintes candidatos: 1- Jose/ 2- Joao/ 3- Maria/ 4- Tereza/ 5- Nulo/ 6- em Branco/ 0- Encerrar;')
while True:
    voto = int(input('Voto: '))
    if voto == 0:
        break
    if 0 < voto <= 6:
        total += 1

    if voto == 1:
        jose += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        tereza += 1;
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1

totalN = nulo * 100 / total
totalB = branco * 100 / total
print(f'Total de votos = {total}')
print(f'Total de votos candidato 1 - Jose = {jose}\n'
      f'Total de votos candidato 2 - Joao = {joao}\n'
      f'Total de votos candidato 3 - Maria = {maria}\n'
      f'Total de votos candidato 4 - Tereza = {tereza}')
print(f'Total de votos Nulos = {nulo}\n'
      f'Total de votos em Branco = {branco}')
print(f'Porcentagem de votos Nulos = {totalN:.0f}%\n'
      f'Porcentagem de votos em Branco = {totalB:.0f}%')
