'''
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é
R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

# alcool <= 20l == 3% litro
# alcool > 20l == 5% litro
# gasolina <= 20l == 4% litro
# galosina > 20l == 6% litro
# litro gasolina == 2.50
# litro alcool == 1.90

litroVen = int(input('Numero de litros vendidos: '))
tipoCombus = input('Tipo de combustivel, A-alcool ou G-gasolina: ')

valorA = 1.90
valorG = 2.50
desconto = valor = pagar = 0
if tipoCombus.lower() == 'a':
    if litroVen <= 20:
        valor = litroVen * valorA
        desconto = 3 / 100 * valor
        pagar = valor - desconto
    else:
        valor = litroVen * valorA
        desconto = 5 / 100 * valor
        pagar = valor - desconto
elif tipoCombus.lower() == 'g':
    if litroVen <= 20:
        valor = litroVen * valorG
        desconto = 4 / 100 * valor
        pagar = valor - desconto
    else:
        valor = litroVen * valorG
        desconto = 6 / 100 * valor
        pagar = valor - desconto

print(f'Valor total: {valor}')
print(f'Desconto de: {desconto}')
print(f'Total a pagar = {pagar}')
