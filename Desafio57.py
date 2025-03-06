sexo = " "

while sexo not in "MmFf":
    sexo = str(input('Qual o seu sexo [F] ou [M]: \n')).upper()

print(f'Seu dado foi analisado e seu sexo é {sexo}')
