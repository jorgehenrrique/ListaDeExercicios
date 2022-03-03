''''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, 
faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada 
para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, 
correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado,
o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve 
fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: 
o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, 
o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''

def percentual(numero_votos, total_votos):
    return numero_votos * 100 / total_votos


cont = 0
votos = [0] * 24
print('Enquete: Quem foi o melhor jogador? ')
while True:
    numero = int(input('Numero do jogador (0=fim): '))
    if numero > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair! ')
    if numero == 0:
        break
    if numero < 24:
        votos[numero] = votos[numero] + 1
        cont += 1

resultado_votos = []
soma = maior = 0

print('\nResultado da votacao: \n')
print(f'Foram computados {cont} votos. \n')
print('Jogador \tVotos \t Percentual % ')
for i in range(len(votos)):
    if votos[i] > 0:
        print(f'{i} \t\t\t{votos[i]} \t\t\t {percentual(votos[i], cont):.1f}% ')
        if maior < votos[i]:
            melhor_jogador = i
            maior = votos[i]

mais_votos = max(votos)
print(mais_votos)
print(f'O melhor jogador foi o número {melhor_jogador}, com {mais_votos} votos, correspondendo a '
      f'{percentual(votos[melhor_jogador], cont):.0f}% do total de votos.')

w = open("resultado.txt", "w")  # cria o arquivo
w.write(f'O melhor jogador foi o número {melhor_jogador}, com {mais_votos} votos, correspondendo a '
        f'{percentual(votos[melhor_jogador], cont):.0f}% do total de votos.')  # grava no arquivo
w.close()  # fecha o arquivo


# DESENVOLVIMENTO TESTE ETC
# def percentual(numero_votos, total_votos):
#     return numero_votos * 100 / total_votos
# 
# print(percentual(5, 50))
# cont = 0
# votos = [0] * 23
# while True:
#     numero = int(input('Informe um valor entre 1 e 23 ou 0 para sair! '))
#     if numero > 23:
#         print('Valor inválido, informe outro valor: ')
#     if numero == 0:
#         break
#     votos[numero] = votos[numero] + 1
#     cont += 1
# 
# print(votos)
# resultado_votos = []
# soma = maior = 0
# for i in range(len(votos)):
#     if votos[i] > 0:
#         print(f'O jogador {i}, obteve {votos[i]} votos.')
#         resultado_votos.append(i)
#         if maior < votos[i]:
#             melhor_jogador = i
#             maior = votos[i]
# 
# print(resultado_votos)
# print(melhor_jogador)
# print(f'Foram computados {cont} votos. ')
# print('Jogador \tVotos \t Percentual % ')
# for i in range(len(votos)):
#     if votos[i] > 0:
#         print(f'{i} \t\t\t{votos[i]} \t\t\t {percentual(votos[i], cont):.2f}')
# 
# mais_votos = max(votos)
# print(mais_votos)
# print(f'O melhor jogador foi o número {melhor_jogador}, com {mais_votos} votos, correspondendo a {percentual(votos[melhor_jogador], cont):.2f} do total de votos.')
# 
# w = open("resultado.txt", "w") # cria um arquivo "w" para escrita
# w.write(f'O melhor jogador foi o número {melhor_jogador}, com {mais_votos} votos, correspondendo a {percentual(votos[melhor_jogador], cont):.2f} do total de votos.') # escreveu no arquivo
# 
# w.close() # fechar o arquivo, depois de ler gravar etc
