# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

print('As resposta só devem ser respondida com S ou N')
print()
lista = ['Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ','Já trabalhou com a vítima? ']

resposta = 0
for i in lista:
    r = input(i).upper()
    print()
    while r != 'S' and r != 'N':#Confere se a resposta está correta, caso nao esteja irá repetir a pergunta!
        print()
        print('Resposta errada, responde com S ou N')
        print()
        r = input(i).upper()
    if r == 'S':
        resposta += 1
    elif r == 'N':
        True
if resposta == 2:
    print('Suspeito!')
elif resposta ==3 or resposta ==4:
    print('Cúmplice!')
elif resposta == 5:
    print('Assasino!')
else:
    print('Inocente!')
