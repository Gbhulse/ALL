
media = 0
velho = 0
cont = 0
name = ""

for c in range(0,4):
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = int(input('Qual seu sexo? F[1] ou M[2]'))
    media = media + idade
    if idade > velho and sexo == 2:
        name = nome
        velho = idade
    elif idade < 20 and sexo == 1:
        cont = cont + 1


print(f'A media de idade é de {media/4} , o homem mais velho é o {name} e tem {cont} mulheres com menos de 20 anos')