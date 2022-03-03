# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
# aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
# armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
# cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
# 
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

def percentual(numero_opcoes, total_opcoes):
    return numero_opcoes * 100 / total_opcoes


cont = 0
opcoes = [0] * 7
print('Qual o melhor Sistema Operacional para uso em servidores? ')
print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro ')
so = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
while True:
    numero = int(input('Valor 1 - 6: '))
    if numero > 6:
        print('Informe um valor valido: 1 - 6, ou 0 para sair ')
    if numero == 0:
        break
    if numero < 7:
        opcoes[numero - 1] = opcoes[numero - 1] + 1
        cont += 1

print('\nSistema Operacional \tVotos \t % ')
print('-------------------  \t----- \t ----')
maior = 0
for i in range(len(opcoes)):
    if opcoes[i] > 0:
        print(f'{so[i]}             \t\t{opcoes[i]} \t\t {percentual(opcoes[i], cont):.0f}% ')
        if maior < opcoes[i]:
            posicao_i = i
            maior = opcoes[i]

mais_votos = max(opcoes)
print('-------------------  \t----- \t ----')
print(f'Total               \t{cont} \n')

print(f'O Sistema Operacional mais votado foi o {so[posicao_i]}, com {mais_votos} votos, correspondendo a '
      f'{percentual(opcoes[posicao_i], cont):.0f}% dos votos.')
