'''
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''
# se comprar no cartao tbjra  == - 5% desconto
# file dupli <= 5kg == 4.90 file duplo > 5kg == 5.80
# alcatra <= 5 kg == 5.90 alcatra > 5kg == 6.80
# picanha <= 5kg == 6.90 picanha > 5kg == 7.80

tipo = int(input('Qual tipo de carne vai comprar?\n'
                 '1 - File duplo\n'
                 '2 - Alcatra\n'
                 '3 - Picanha\n'
                 'Opcao 1, 2 ou 3: '))
quantidade = float(input('Quantidade em Kg de carne: '))
pagamento = input('Qual tipo de pagamento?\n'
                  '(C) Cartao Tabajara ou (O) Outro: ')
desconto = valor = pagar = 0

if tipo == 1:
    if quantidade <= 5:
        valor = quantidade * 4.90
    elif quantidade > 5:
        valor = quantidade * 5.80
    print("\nTipo de carne escolhida: File duplo")
elif tipo == 2:
    if quantidade <= 5:
        valor = quantidade * 5.90
    elif quantidade > 5:
        valor = quantidade * 6.80
    print("\nTipo de carne escolhida: Alcatra")
elif tipo == 3:
    if quantidade <= 5:
        valor = quantidade * 6.90
    elif quantidade > 5:
        valor = quantidade * 7.80
    print("\nTipo de carne escolhida: Picanha")
else:
    print('\nTipo inexistente! ')

if pagamento.lower() == 'c':
    desconto = 5 / 100 * valor
    pagar = valor - desconto
    print(f'Quantidade de carne: {quantidade}Kg\n'
          f'Valor total: R${valor:.2f}\n'
          f'Tipo de pagamento: Cartao Tabajara\n'
          f'Valor do desconto: {desconto:.2f}\n'
          f'Valor a pagar: R${pagar:.2f}\n')
else:
    print(f'Quantidade de carne: {quantidade}Kg\n'
          f'Valor total: R${valor:.2f}\n'
          f'Tipo de pagamento: Outro\n'
          f'Valor do desconto: Sem desconto\n'
          f'Valor a pagar: R${valor:.2f}\n')
