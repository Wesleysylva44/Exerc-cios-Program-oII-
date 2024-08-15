def soma (valor1,valor2):
    resultado = valor1+valor2
    print(resultado)

def subtracao (valor1,valor2):
    resultado = valor1-valor2
    print(resultado)

def multiplicacao (valor1,valor2):
    resultado = valor1*valor2
    print(resultado)

def divisao (valor1,valor2):
    resultado = valor1/valor2
    print(resultado)

def calculadora ():
    valor1 = float(input('Digite o 1º número: '))
    operador = input('Digite a operação: ')

    while operador != '+' and operador != '-' and operador != '*' and operador != '/':
        operador = input('Digite a operação: ')
    valor2 = float(input('Digite o 2º número: '))
    if operador == '+':
        soma(valor1,valor2)
    if operador == '-':
        subtracao(valor1,valor2)
    if operador == '*':
        multiplicacao(valor1,valor2)
    if operador == '/':
        divisao(valor1,valor2)   
calculadora()


