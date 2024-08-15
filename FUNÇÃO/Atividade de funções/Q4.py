# Crie um programa de câmbio. Nesse programa adicione funções que
# valor_realizem conversões de valor_real para dólar, valor_real para euro e valor_real para peso
# argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
# 1,00 valor_real = 0,18 dólar para Estados Unidos;
# 1,00 valor_real = 0,16 euro para Portugal;
# 1,00 valor_real = 165,38 peso para Argentina;

def EstadosUnidos (valor_real):
    conversao_dolar = valor_real * 0.18
    print(f'A conversão de {valor_real} R$ em dolar é {conversao_dolar}$')

def Portugal (valor_real):
    conversao_euro = valor_real * 0.16
    print(f'A conversão de {valor_real} R$ em euro é {conversao_euro}')

def Argentino (valor_real):
    conversao_peso = valor_real*165,38
    print(f'A conversão de {valor_real} R$ em peso é {conversao_peso}')

nome_pais = input('Qual o nome do pais que você irá viajar: ').upper()
lista = ['ESTADOS UNIDOS','PORTUGAL','ARGENTINA']
while nome_pais not in lista:
    nome_pais = input('Qual o nome do pais que você irá viajar: ')

valor_real = float(input('Qual o valor em real: '))

if nome_pais == 'ESTADOS UNIDOS':
    EstadosUnidos(valor_real)
elif nome_pais == 'PORTUGAL':
    Portugal(valor_real)
elif nome_pais == 'ARGENTINA':
    Argentino(valor_real)




