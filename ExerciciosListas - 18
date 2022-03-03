def percentual(numero_votos, total_votos):
    return numero_votos * 100 / total_votos


cont = 0
votos = [0] * 23
print('Enquete: Quem foi o melhor jogador? ')
while True:
    numero = int(input('Numero do jogador (0=fim): '))
    if numero > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair! ')
    if numero == 0:
        break
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




# DESENVOLVIMENTO DO PROGRAMA
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
