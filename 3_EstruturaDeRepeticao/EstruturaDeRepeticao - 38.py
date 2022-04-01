'''
38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o
 usuário digite o salário inicial do funcionário.
'''

salario = int(input('Digite o salário do funcionário: '))
ano = 1996
porcentagem = 1.5/100
salario_1 = salario
while ano <= 2022:
    salario = salario + porcentagem * salario_1
    ano += 1
    porcentagem += porcentagem
print(f'Salario atual: {salario:.2f}')
