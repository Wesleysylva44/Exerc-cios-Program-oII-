# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

lista = []
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
print()
for i in range(num1+1,num2):
    lista.append(i)
print(lista)
print()