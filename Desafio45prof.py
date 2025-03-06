from random import randint

# Opções disponíveis
itens = ('Pedra', 'Papel', 'Tesoura')

# Computador faz sua escolha aleatória
computador = randint(0, 2)

# Jogador faz sua escolha
print("[0] PEDRA\n[1] PAPEL\n[2] TESOURA")
jogador = int(input("Qual sua Jogada? "))

# Validando a entrada do jogador
if jogador < 0 or jogador > 2:
    print("Jogada inválida! Escolha entre 0, 1 ou 2.")
else:
    print(f"\nO computador escolheu {itens[computador]}")
    print(f"Você escolheu {itens[jogador]}")

    # Lógica do jogo
    if computador == jogador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("Você venceu!")
    else:
        print("Você perdeu!")
