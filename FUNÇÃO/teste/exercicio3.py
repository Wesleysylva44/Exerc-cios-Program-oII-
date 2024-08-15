# Faça um programa para imprimir:
# 1
# 22
# 333
# .....
# 77777777

def repetição (a):
    for i in range(a+1):
        print(str(i)*i)
repetição (int(input('Digite um número: ')))