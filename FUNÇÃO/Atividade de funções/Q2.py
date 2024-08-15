# Faça um programa que calcule a área de um terreno e imprima na tela

def calcular(comprimento,largura):
    valor_da_area = comprimento * largura
    print(f'A Área do terrono é: {valor_da_area}')
    print()
comprimento = float(input('Qual o comprimentos da área: '))
largura = float(input('Qual a largura da área: '))
print()
calcular(comprimento,largura)