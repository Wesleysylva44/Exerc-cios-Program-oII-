# Crie uma função que receba um número indeterminado de valores inteiros e depois apresente a soma deles na tela.
# Use: def nome_da_funcao (*parametro):

def soma_valores(*valores):
    total = sum(valores)
    print(f'A soma dos valores é: {total}')

soma_valores(50,100,150)
soma_valores(200,120,10)