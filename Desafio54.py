from datetime import datetime

maior = 0
soma = 0
menor = 0

for c in range(0, 7):
    ano = int(input('Qual o ano do seu nascimento?\n '))
    maior = datetime.today().year
    if maior - ano >= 21:
        soma = soma + 1
    else:
        menor = menor + 1

print(f'Desses {c+1} participantes, {soma} são maior de idade e {menor} são menor de idade')


