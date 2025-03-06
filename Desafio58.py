from random import randint

computador = randint(0, 10)
contador = 1

player = int(input('Advinhe o número que estou pensando: '))

while player != computador:
    player = int(input('Tente de novo: '))
    contador += 1

print(f'Você acertou depois de {contador} rodadas o número {computador}')