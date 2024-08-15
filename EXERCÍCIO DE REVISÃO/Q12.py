# Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

quantidade = int(input('Digite a qauntidade de números que você irá inserir: '))
lista = []
print()
for i in range(quantidade):
    num = int(input(f'Insira o {i+1}º número: '))
    lista.append(num)

menor = min(lista)
maior = max(lista)
soma = sum(lista)
soma1 = menor+maior
print()
print(f'O menor número inserido foi: {menor}')
print(f'O maior número inserido foi: {maior}')
print(f'A soma de todos os números inseridos é: {soma}')
print(f'A soma do menor e maior número inserido é: {soma1}')
print()