n = list()
par = list()
impar = list()

while True:
    valor = int(input('Digite um valor: '))
    n.append(valor)
    cont = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break



for k, v in enumerate(n):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'A lista completa é {n}')
print(f'A lista de pares é {par}')
print(f'A lista de impar é {impar}')

