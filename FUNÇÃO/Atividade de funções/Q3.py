#  Faça um programa que receba três números do usuário, e identifique o maior
# através de uma função e o menor número através de outra função.
lista = []
for i in range(3):
    numero = int(input(f'Digite o {i+1}º número: '))
    lista.append(numero) 

def maior (numero):
   print(f'O menor número digitado foi: {min(lista)}') 

def menor (numero):
    print(f'O maior número digitado foi: {max(lista)}')

maior (lista)
menor(lista)