"""
24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
"""

import random


def aleatorio():
    return random.randint(1, 6)


lances = [0] * 6
for i in range(100):
    x = aleatorio()
    lances[x - 1] = lances[x - 1] + 1

for i in range(len(lances)):
    print(f'O {i + 1} teve {lances[i]} lances ')
