import random

player = int(input('Escolha um número de 0 a 5: '))
computer = random.randint(0, 5)

if player == computer:
    print(f'Você venceu, parabéns! Vocês escolheram o mesmo número')

else:
    print(f'Você perdeu! Tente Novamente, você escolheu {player} e o computador {computer}')



