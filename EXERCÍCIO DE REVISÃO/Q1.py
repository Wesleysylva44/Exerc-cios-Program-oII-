# Crie um programa em Python que peça dois números ao usuário. Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão, exponenciação e resto da divisão do primeiro número pelo segundo.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
print(f'Soma: {num1+num2}')
print(f'Subtração: {num1-num2}')
print(f'Multiplicação: {num1*num2}')
print(f'Divisão: {num1/num2}')
print(f'Exponenciação: {num1**num2}')
print(f'Resto da divisão: {num1%num2}')