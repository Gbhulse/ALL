pessoas = list()
dados = list()
tot = 0
cont = 's'
maiorlist = list()
menorlist = list()


while True:
    dados.append(str(input('Qual o nome da pessoa cadastrada? ')))
    dados.append(int(input('Qual a idade da pessoa cadastrada? ')))
    pessoas.append(dados[:])
    dados.clear()
    tot += 1
    cont = str(input('Você Gostaria de continuar? [S/N]')).strip().upper()[0]
    if cont in 'N':
        break

print(f'Foram cadastradas {tot} pessoas')

maiorlist.append(pessoas[0])
menorlist.append(pessoas[0])

for n, c in enumerate(pessoas[1:], start=1):
    if c[1] > maiorlist[0][1]:
        maiorlist = [c]
    elif c[1] == maiorlist[0][1]:
        maiorlist.append(c)

    if c[1] < menorlist[0][1]:
            menorlist = [c]
    elif c[1] == menorlist[0][1]:
            menorlist.append(c)

    """if n == 0: #como eu tinha feito
        maior = c[0]
        menor = c[0]
        maiorlist.append(c)
        menorlist.append(c)
    else:
        if c[1] > maiorlist[1]:
            maiorlist.pop()
            maiorlist.append(c)
        elif c[1] < menorlist[1]:
            menorlist.pop()
            menorlist.append(c)
        elif c[1] == maiorlist[1]:
            maiorlist.append(c)
        elif c[1] == menorlist[1]:
            menorlist.append(c)
"""
    
        
# Exibir os resultados corretamente
print(f'O menor é {menorlist[0][0]} com {menorlist[0][1]} anos', end='')
for p in menorlist[1:]:
    print(f', {p[0]} com {p[1]} anos', end='')

print(f'\nO maior é {maiorlist[0][0]} com {maiorlist[0][1]} anos', end='')
for p in maiorlist[1:]:
    print(f', {p[0]} com {p[1]} anos', end='')

print()


