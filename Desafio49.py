#Tabuada

player = int(input('Você quer a tabuada de qual número? '))

print(f'TABUADA DO {player}')
for c in range(0, 11):
    print(f'{c}x{player} = {c*player}')

print(f'Fim do Programa')
