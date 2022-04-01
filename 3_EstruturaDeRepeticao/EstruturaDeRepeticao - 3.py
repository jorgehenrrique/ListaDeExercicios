'''
3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    nome = input('Nome: ')
    if len(nome) < 3:
        print('Nome invalido, tente novamente! ')
    else:
        break
while True:
    idade = int(input('Idade: '))
    if idade < 0 or idade > 150:
        print('Idade inválida, tente novamente! ')
    else:
        break
while True:
    salario = float(input('Salario: '))
    if salario < 0:
        print('Salario invalido, tente novamente! ')
    else:
        break
while True:
    sexo = input('Sexo: ')
    if sexo.lower() not in 'fm':
        print('Sexo invalido, tente novamente! ')
    else:
        break
while True:
    estadocv = input('Estado Civil: ')
    if estadocv.lower() not in 'scvd':
        print('Estado Civil invalido, tente novamente! ')
    else:
        break
