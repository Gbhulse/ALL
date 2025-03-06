from random import randint

cont = soma = 0

while True:
    pc = randint(1, 10)
    player = int(input('Digite um número: \n'))
    escolha = str(input('Você quer PAR[P] ou ÍMPAR[I]\n')).strip().upper()[0]
    soma = pc + player
    cont = cont + 1
    if escolha == "P":
        if soma % 2 == 0:
            print(f'Você acertou, deu {soma}')
        elif soma % 2 != 0:
            print(f'VOCÊ PERDEU, TENTE NOVAMENTE!, deu {soma}')
            break
    
    if escolha == "I":
        if soma % 2 == 0:
            print(f'Você perdeu, jovem, deu {soma}')
            break
        elif soma % 2 != 0:
            print(f'Você ganhou, deu {soma}')
        
    

print(f'Você jogou {cont} tentativas :)')





    