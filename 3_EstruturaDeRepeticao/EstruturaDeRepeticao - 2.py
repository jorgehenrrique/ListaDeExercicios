'''
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    usuario = input('Nome de usuario: ')
    senha = input('Senha: ')

    if usuario == senha:
        print('Erro, senha igual ao nome de usuario, tente novamente')
    else:
        break
