# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

M = 'matutino'
V = 'vespertino'
N = 'noturno'

turno = input('M= Matutino, V= Vespertino ou N= Noturno. Qual turno você estuda: ').upper()#SERVER PARA TRANSFORMA A LETRA EM MAISCULO
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Invalido!')