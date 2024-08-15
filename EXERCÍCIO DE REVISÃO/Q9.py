#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e
#voltando a pedir as informações.


usuario = input('Digite seu nome de usuário: ')
senha = input('Diite sua senha: ')

while usuario == senha:
    print('ERRO!')
    print()
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Diite sua senha: ')
    
    if usuario == senha:
        continue
    else:
        break
print('Login Efetuado')
