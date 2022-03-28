'''
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
'''
# se comprar > 8kg or valor total > 25R$ == - 10% desconto
# morango <= 5kg == 2.50 morango > 5kg == 2.20
# maca <= 5 kg == 1.80 maca > 5kg == 1.50

morangos = float(input('Quantidade em Kg de Morangos: '))
macas = float(input('Quantidade em Kg de Macas: '))
desconto = valorMo = pagar = valorMa = valortt = 0
pesott = morangos + macas

if morangos <= 5:
    valorMo = morangos * 2.50
elif morangos > 5:
    valorMo = morangos * 2.20
if macas <= 5:
    valorMa = macas * 1.80
elif macas > 5:
    valorMa = macas * 1.50

valortt = valorMo + valorMa

if pesott > 8 or valortt > 25:
    desconto = 10 / 100 * valortt
    pagar = valortt - desconto
    print(f'Valor total: {valortt:.2f}\n'
          f'Valor do desconto: {desconto:.2f}\n'
          f'Valor a pagar: {pagar:.2f}\n')
else:
    print(f'Valor a pagar: {valortt:.2f}')
