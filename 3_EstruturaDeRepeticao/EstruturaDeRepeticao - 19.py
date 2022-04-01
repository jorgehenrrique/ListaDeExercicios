'''
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

conjunto = int(input('Quantos numeros deseja fornecer: '))

menor = 10000
maior = soma = 0
while conjunto > 0:
    conjunto -= 1
    while True:
        valor = int(input('Informe um valor: '))
        if 0 <= valor <= 1000:
            break
        else:
            print('Valor inválido, insira novamente! ')

    soma += valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

print(f'Maior valor: {maior}\n'
      f'Menor valor: {menor}\n'
      f'Soma dos valores: {soma}')
