# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
salario = float(input('Qual o seu salário? '))
sexo = input('F(Feminino) M(Masculino). Qual seu sexo? ').upper()
estado = input('S,C,V,D. Qual seu estado civil? ').upper()

cont = len(nome)

while cont < 4:
    nome = input('Qual o seu nome? ')
    if cont >3:
        break

while idade > 151:
    idade = int(input('Qual sua idade? '))
    if idade > 0 and idade <= 150:
        break

while salario <=0:
    salario = float(input('Qual o seu salário? '))
    if salario >0:
        break

while sexo != 'F' and sexo != 'M':
    sexo = input('F(Feminino) M(Masculino). Qual seu sexo? ').upper()
    if sexo == 'F' and sexo == 'M':
        break

while estado != 'S' and estado != 'C' and estado != 'V' and estado != 'D':
    estado = input('S,C,V,D. Qual seu estado civil? ').upper()
    if estado == 'S' and estado != 'C' and estado != 'V' and estado != 'D':
        break