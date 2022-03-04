# 21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
# litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
# e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
# execução do programa.
# Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

def litros_p_distancia(distancia, consumo_carro):  # calcula a quantidade de litros do percurso
    return distancia / consumo_carro


def preco_p_km(valor_litro, consumo_carro, distancia):  # calcula o preco do percurso
    return valor_litro / consumo_carro * distancia


print('\nComparativo de Consumo de Combustivel\n')
veiculos = []
consumo = []

preco_gasolina = 2.25
percorrer_distancia = 1000

for i in range(5):
    print(f'Veiculo {i + 1}')
    veiculos.append(input('Nome: '))
    consumo.append(float(input('Km por litro: ')))

print('\nRelatorio Final')
for v in range(len(veiculos)):
    print(f'{v + 1} - {veiculos[v]}                      \t\t-\t  {consumo[v]} \t -'
          f' {litros_p_distancia(percorrer_distancia, consumo[v]):.1f} litros - RS '
          f'{preco_p_km(preco_gasolina, consumo[v], percorrer_distancia):.2f}')

menor_consumo = max(consumo)  # max obtem o maior valor, que é o veliculo mais economico
menor_consumo = consumo.index(menor_consumo)  # index obtem o indice desse valor acima
print(f'O menor consumo é do {veiculos[menor_consumo]}.')
