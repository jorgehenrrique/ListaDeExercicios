'''
37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
'''

malto = mbaixo = mgordo = mmagro = cmalto = cmbaixo = cmgordo = cmmagro = 0
maltura = mpeso = i = 0
while True:
    codigo = int(input('Informe seu codigo: '))
    if codigo <= 0:
        break
    altura = float(input('Informe a altura: '))
    peso = float(input('Informe o peso: '))

    if i == 0:
        mbaixo = altura
        mmagro = peso
        cmbaixo = codigo
        cmmagro = codigo
    i += 1

    if altura > malto:
        malto = altura
        cmalto = codigo
    if altura < mbaixo:
        mbaixo = altura
        cmbaixo = codigo
    if peso > mgordo:
        mgordo = peso
        cmgordo = codigo
    if peso < mmagro:
        mmagro = peso
        cmmagro = codigo

    maltura += altura
    mpeso += peso

maltura = maltura / i
mpeso = mpeso / i

print(f'Cliente mais alto, codigo: {cmalto}, altura: {malto}\n'
      f'Cliente mais baixo, codigo: {cmbaixo}, altura: {mbaixo}\n'
      f'Media das alturas: {maltura:.2f}')
print(f'Cliente mais gordo, codigo: {cmgordo}, peso: {mgordo}\n'
      f'Cliente mais magro, codigo: {cmmagro}, peso: {mmagro}\n'
      f'Media dos pesos: {mpeso:.2f}')
