soma = 0
cont_sex = 0
cont_m = 0

while True:
    sexo = " "
    cont = " "
    idade = int(input('Qual sua idade?\n '))
    while sexo not in "fFmM":
        sexo = str(input('Qual o seu sexo? [M] OU [F]\n')).upper().strip()[0]
    while cont not in "SsnN":
        cont = str(input('Você quer continuar? [S] OU [N]\n')).strip().upper()[0]
    if idade > 18:
        soma = soma + 1
    if sexo == "M":
        cont_sex = cont_sex + 1
    if sexo == "F" and idade < 20:
        cont_m += 1
    if cont in "N":
        break

print(f'foram cadastradas {soma} pessoas com mais de 18 anos \nForam cadastrados {cont_sex} homens\n Foram cadastrados {cont_m} mulheres com menos de 20 anos')