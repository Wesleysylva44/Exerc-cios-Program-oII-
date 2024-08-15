#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

lista1 = ['A','E','I','O','U']
lista2 = ['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
letra = input('Digite uma letra: ').upper()#SERVER PARA TRANSFORMA A LETRA EM MAISCULO
print()

for i in lista1:
     if letra == i:
         print(f'A letra {letra} é uma vogal')

for i in lista2:
    if letra == i:
        print(f'A letra {letra} e uma consoante')

else:
    print(f'Digite uma letra, POR FAVOR!')