#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data_inserida = input('Digite uma data no formato dd/mm/aaaa')
dia,mes,ano = map(int,data_inserida.split('/'))

if mes < 1 or mes > 12:
    print('Data inválida. O mês deve está entre 1 e 12 ')
if mes in [1,3,5,7,8,9,10,12]:
     max_dias = 31
elif mes in [4,6,9,11]:
     max_dias = 30
elif ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0):
     max_dias = 29
     
     if dia < 1 and dia > 31:
          print('Data inválida. O dia inserido não é valido para o mês informado')
     else:
          print('Data válida')
          