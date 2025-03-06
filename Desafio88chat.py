from random import randint
from time import sleep

n = int(input('Quantos jogos você quer? '))

for c in range(0, n):
    lista = []
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)

    lista.sort()
    print(f'Jogo {c+1}: {lista}')

print(f'Boa sorte!!')