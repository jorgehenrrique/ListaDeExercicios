"""
7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor deprestação
e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo
do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valorPagamento(prestacao, dias):
    if dias <= 0:
        return prestacao
    else:
        multa = 3 / 100 * prestacao
        for i in range(dias):
            multa = multa + (0.1 / 100 * prestacao)
        total = multa + prestacao
        return total


prestacoes = []
while True:
    valor_p = float(input(' Valor da prestacao: '))
    if valor_p <= 0:
        break
    n_dias = int(input('Numero de dias em atraso: '))
    prestacoes.append(valorPagamento(valor_p, n_dias))

print(f'Relatorio do ria: \n'
      f'Quantidade de prestaçoes pagas no dia: {len(prestacoes)}\n'
      f'Valor total de prestacoes pagas: {sum(prestacoes)}\n'
      f'Prestacoes: {prestacoes}')
