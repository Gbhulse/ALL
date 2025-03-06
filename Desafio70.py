soma = 0
con = 0
menor = 0
name = " "
while True:
    nome = str(input('Qual o nome do produto?\n'))
    preço = float(input('Quanto você gastou no produto?\n'))
    cont = str(input('Quer continuar? [S]ou[N]')).upper().strip()[0]

    if con == 0:
       menor = preço
       name = nome
    
    if preço < menor:
        menor = preço
        name = nome
       
    soma += preço

    if preço > 1000:
        con += 1

    if cont in "N":
        break

print(f'O total Gasto é de R${soma}\n{con} produtos custam mais que R$1000\nO produto mais barato é {name} que custa {menor}')



