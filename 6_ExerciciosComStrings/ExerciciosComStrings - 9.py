"""
9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
"""

while True:
    cpf = input('Infome o CPF no formato xxx.xxx.xxx-xx: ')

    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    if cpf.isdigit() and len(cpf) == 11:
        print('CPF valido!:')
        break
    else:
        print('CPF invalido:')
