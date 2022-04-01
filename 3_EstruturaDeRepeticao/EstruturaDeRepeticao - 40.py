'''
40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

maior_indice = menor_indice = media_veiculos = media_acidentes = nveiculos = cidadeMenorindice = cidadeMaiorindice = 0
cont = 0
for i in range(5):
    codigo_cidade = int(input('Codigo da cidade: '))
    n_veiculos_passeio = int(input('Numero de veiculos de passeio: '))
    n_acidentesCvitimas = int(input('Numero de acidentes com vitimas: '))

    if i == 0:
        menor_indice = n_acidentesCvitimas
        cidadeMenorindice = codigo_cidade

    if n_acidentesCvitimas > maior_indice:
        maior_indice = n_acidentesCvitimas
        cidadeMaiorindice = codigo_cidade
    if n_acidentesCvitimas < menor_indice:
        menor_indice = n_acidentesCvitimas
        cidadeMenorindice = codigo_cidade

    media_veiculos += n_veiculos_passeio
    if n_veiculos_passeio < 2000:
        media_acidentes += n_acidentesCvitimas
        cont += 1

nveiculos = media_veiculos / 5
media_acidentes = media_acidentes / cont

print(f'Maior indice de acidentes de transito: {maior_indice}, na cidade: {cidadeMaiorindice}\n'
      f'Menor indice de acidentes de transito: {menor_indice}, na cidade: {cidadeMenorindice}\n')
print(f'Media de veiculos das 5 cidades: {nveiculos:.2f}')
print(f'Media de acidentes de transito em cidades com menos de 2.000 veiculos de passeio: {media_acidentes:.2f}')
