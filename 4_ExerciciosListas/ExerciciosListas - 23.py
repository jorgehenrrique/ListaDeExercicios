"""
23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também
deverá ser feito através de uma função, que será chamada pelo programa principal.
"""

def conversao(bytes):
    return bytes / 1024 / 1024


def percentual(bytes, total):
    return bytes * 100 / total


arquivo = open('usuarios.txt')
linhas = arquivo.readlines()  # ler todas as linhs e jogar em uma lista
arquivo.close()

lista = []
for linha in linhas:  # passa por todas as linhas e adiciona cada usuario e, seu espaco em disco, em nova lista
    lista.append(linha.split())

n = soma = cont = 0
for i in lista:
    soma += int(lista[n][1])
    cont += 1
    n += 1

n = 0
# =============EXIBINDO O TEXTO QUE SERA GRAVADO=============
print('\nACME Inc.               Uso do espaço em disco pelos usuários')
print('------------------------------------------------------------------------')
print('Nr.  Usuário         Espaço utilizado      % do uso\n')

for i in range(len(lista)):
    print(
        f'{i + 1}  \t{lista[n][0]}   \t\t   {conversao(int(lista[n][1])):.2f} MB   \t\t   '
        f'{percentual(int(lista[n][1]), soma):.2f}%')
    n += 1

print(f'\nEspaco total ocupado: {conversao(soma):.2f} MB')
print(f'Espaco medio ocupado: {conversao(soma) / cont:.2f} MB')

# =============GRAVANDO TEXTO EM DISCO=============
relatorio = open("relatorio.txt", "w")  # cria o arquivo de texto
relatorio.write('\nACME Inc.               Uso do espaço em disco pelos usuários\n')  # escreve no arquivo criado acima
relatorio.write('------------------------------------------------------------------------\n')
relatorio.write('Nr.  Usuário       Espaço utilizado      % do uso\n\n')
n = 0
for i in range(len(lista)):
    relatorio.write(
        f'{i + 1}  {lista[n][0]}   \t   {conversao(int(lista[n][1])):.2f} MB   \t\t   '
        f'{percentual(int(lista[n][1]), soma):.2f}%\n')
    n += 1

relatorio.write(f'\nEspaco total ocupado: {conversao(soma):.2f} MB\n')
relatorio.write(f'Espaco medio ocupado: {conversao(soma) / cont:.2f} MB')

relatorio.close()  # fecha o arquivo


# ====DESENVOLVIMENTO TESTE ETC====
'''
def conversao(bytes):
    return bytes / 1024 / 1024
    # kb =  bytes / 1024
    # return kb / 1024


def percentual(bytes, total):
    return bytes * 100 / total


arquivo = open('usuarios.txt')
linhas = arquivo.readlines()  # ler todas as linhs e jogar em uma lista

lista = []
for linha in linhas:  # passa por todas as linhas e adiciona cada usuario e, seu espaco em disco em nova lista
    lista.append(linha.split())

n = soma = cont = 0
# usuarios = []  # criar nova lista so de usuarios caso preciso
# espaco = []  # criar nova lista so de espaco em disco, se necessario
for i in lista:
    # usuarios.append(lista[n][0])  # criar nova lista so de usuarios caso preciso
    # espaco.append(lista[n][1])  # criar nova lista so de espaco em disco, se necessario
    soma += int(lista[n][1])
    cont += 1
    n += 1

n2 = 0
# =============EXIBINDO O  TEXTO QUE SERA GRAVADO=============
print('\nACME Inc.               Uso do espaço em disco pelos usuários')
print('------------------------------------------------------------------------')
print('Nr.  Usuário         Espaço utilizado      % do uso\n')

for i in range(len(lista)):
    print(
        f'{i + 1}  \t{lista[n2][0]}   \t\t   {conversao(int(lista[n2][1])):.2f} MB   \t\t   {percentual(int(lista[n2][1]), soma):.2f}%')
    n2 += 1

print(f'\nEspaco total ocupado: {conversao(soma):.2f} MB')
print(f'Espaco medio ocupado: {conversao(soma) / cont:.2f} MB')

# =============GRAVANDO TEXTO EM DISCO=============

relatorio = open("relatorio.txt", "w")  # cria o arquivo de texto, o "w" cria ou substitui um arquivo existente
relatorio.write('\nACME Inc.               Uso do espaço em disco pelos usuários\n')  # escreve no arquivo criado acima
relatorio.write('------------------------------------------------------------------------\n')
relatorio.write('Nr.  Usuário         Espaço utilizado      % do uso\n')
n2 = 0
for i in range(len(lista)):
    relatorio.write(
        f'{i + 1}  \t{lista[n2][0]}   \t\t   {conversao(int(lista[n2][1])):.2f} MB   \t\t   {percentual(int(lista[n2][1]), soma):.2f}%')
    n2 += 1

relatorio.write(f'\nEspaco total ocupado: {conversao(soma):.2f} MB\n')
relatorio.write(f'Espaco medio ocupado: {conversao(soma) / cont:.2f} MB')

relatorio.close()  # fechar o arquivo no final'''
