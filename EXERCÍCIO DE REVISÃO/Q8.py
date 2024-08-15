# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
# Escreva um programa que pergunta a situação do usuário (se é idoso, se é
# gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
# prioridade ou não.


situacao = input('Você é uma pessoa idosa, gestante ou PCD? ').upper()
print()
while situacao != 'SIM' and situacao != 'NÃO':
    print('Resposta com sim ou não')
    situacao = input('Você é uma pessoa idosa, gestante ou PCD? ').upper()
    print()
if situacao == 'SIM':
    print('Você tem acesso  a fila de prioridade')
else:
    print('Você não tem acessoa a fila de prioridade')