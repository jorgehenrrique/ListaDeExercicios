"""
43. O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser
encerrado.
"""

parar = ''
codigo0 = codigo1 = codigo2 = codigo3 = codigo4 = codigo5 = 0
somaTotal = soma0 = soma1 = soma2 = soma3 = soma4 = soma5 = 0
while True:
    codigo = int(input('Codigo do item: '))
    qtdd = int(input('Quantidade: '))

    if codigo == 100:
        codigo0 += qtdd
        soma0 = codigo0 * 1.20
    elif codigo == 101:
        codigo1 += qtdd
        soma1 = codigo1 * 1.30
    elif codigo == 102:
        codigo2 += qtdd
        soma2 = codigo2 * 1.50
    elif codigo == 103:
        codigo3 += qtdd
        soma3 = codigo3 * 1.20
    elif codigo == 104:
        codigo4 += qtdd
        soma4 = codigo4 * 1.30
    elif codigo == 105:
        codigo5 += qtdd
        soma5 = codigo5 * 1.0
    else:
        print('Codigo invalido!')

    parar = input('Encerrar pedido: (s) ou (n)? ')
    if parar.lower() == 's':
        break

somaTotal = soma0 + soma1 + soma2 + soma3 + soma4 + soma5
print(f'Item 100, preco: {soma0:.2f}    quantidade: {codigo0}\n'
      f'Item 101, preco: {soma1:.2f}    quantidade: {codigo1}\n'
      f'Item 102, preco: {soma2:.2f}    quantidade: {codigo2}\n'
      f'Item 103, preco: {soma3:.2f}    quantidade: {codigo3}\n'
      f'Item 104, preco: {soma4:.2f}    quantidade: {codigo4}\n'
      f'Item 105, Preco: {soma5:.2f}    quantidade: {codigo5}')
print(f'Total do pedido: {somaTotal:.2f}')
