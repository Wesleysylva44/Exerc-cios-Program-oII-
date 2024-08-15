# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número para saber se ele é primo: '))
contador = 0
for i in range(2,num):
    if num % i == 0:
        contador += 1
if contador >0:
    print(f'O número {num} não é primo!')
else:
    print(f'O número {num} é primo!')
