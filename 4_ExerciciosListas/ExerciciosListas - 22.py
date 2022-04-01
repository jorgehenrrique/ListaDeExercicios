"""
22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar
deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
necessita troca do cabo ou conector;
quebrado ou inutilizado
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

def percentual(quantidade, total):
    return quantidade * 100 / total


mouses = [0] * 4
mouse_situacao = ['necessita de esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector',
                  'quebrado ou inutilizado']
cont = 0
print('Qual a situacao do mouse? ')
while True:
    situacao = int(input('1- Necessita de esfera\n2- necessita de limpeza\n'
                         '3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n: '))
    if situacao < 1:
        break
    if situacao > 4:
        print('Informe outra opcao')
    else:
        mouses[situacao - 1] += 1
        cont += 1

print(f'Quantidade de mouses: {cont}\n')
print('Situacao                        \t\t\t\tQuantidade       \t\tPercintual')
for i in range(len(mouses)):
    print(
        f'{i + 1}- {mouse_situacao[i]}                 \t\t\t\t{mouses[i]}           '
        f'\t\t{percentual(mouses[i], cont):.0f}%')
