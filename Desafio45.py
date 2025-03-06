# JOKENPO
from random import randint

# Escolha do computador
pc = randint(1, 3)
# Entrada do jogador
player = int(input('Escolha se você quer PEDRA[1], PAPEL[2] OU TESOURA[3]\n'))

# Validação da entrada
if player not in [1, 2, 3]:
    print("Escolha inválida! Tente novamente com 1 (PEDRA), 2 (PAPEL) ou 3 (TESOURA).")
else:
    # Traduzindo números para palavras
    opcoes = {1: "PEDRA", 2: "PAPEL", 3: "TESOURA"}
    print(f"Você escolheu: {opcoes[player]}")
    print(f"O computador escolheu: {opcoes[pc]}")

    # Lógica do jogo
    if pc == player:
        print('Vocês empataram')
    else:
        if pc == 1 and player == 2:  # Computador Pedra, Jogador Papel
            print('Você venceu! Jogou PAPEL e o PC jogou PEDRA ')
        elif pc == 2 and player == 1:  # Computador Papel, Jogador Pedra
            print('Você perdeu! Jogou PEDRA e o PC jogou PAPEL')
        elif pc == 1 and player == 3:  # Computador Pedra, Jogador Tesoura
            print('Você perdeu! Jogou TESOURA e o PC jogou PEDRA')
        elif pc == 2 and player == 3:  # Computador Papel, Jogador Tesoura
            print('Você venceu! Jogou TESOURA e o PC jogou PAPEL')
        elif pc == 3 and player == 1:  # Computador Tesoura, Jogador Pedra
            print('Você venceu! Jogou PEDRA e o PC jogou TESOURA')
        elif pc == 3 and player == 2:  # Computador Tesoura, Jogador Papel
            print('Você perdeu! Jogou PAPEL e o PC jogou TESOURA')
