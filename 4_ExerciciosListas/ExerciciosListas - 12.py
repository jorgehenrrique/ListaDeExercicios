"""
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos.
"""

idades = [9, 10, 11, 12, 13, 14, 14, 15, 16, 15, 15, 18, 15, 18, 14, 17, 14, 16, 13, 12, 10, 15, 8, 14, 14, 17, 16, 12,
          12, 11]
alturas = [1.45, 1.50, 1.56, 1.57, 1.59, 1.61, 1.68, 1.70, 1.68, 1.67, 1.54, 1.73, 1.69, 1.49, 1.78, 1.80, 1.66, 1.58,
           1.66, 1.70, 1.69, 1.71, 1.66, 1.54, 1.63, 1.72, 1.63, 1.56, 1.61, 1.5]

media = altura_inferior = 0
for i in alturas:
    media += i

media = media / len(alturas)

for i in range(len(alturas)):
    if idades[i] > 13:
        if alturas[i] < media:
            altura_inferior += 1

print(f'Sao {altura_inferior} alunos com altura inferior a media de alturas. ')
