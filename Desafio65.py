res = " "
soma = 0
cont = 0
maior = 0
menor = 0

while res not in "nN":
    n = float(input('Fale um valor: '))
    if cont == 0:
        maior = n
        menor = n
    soma = soma + n
    cont = cont + 1
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    res = str(input('Você quer continuar? [S] ou [N]'))

print(f'A média dos valores é {soma/cont}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')

