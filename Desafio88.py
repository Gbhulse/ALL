from random import randint, sample
import time


n = int(input('Quantos jogos da megasena você quer que eu faça? '))
for c in range(0, n):
    lista = sample(range(1, 61), 6)
    lista.sort()
    print(f'Jogo {c+1}: {lista}')
    time.sleep(1)


