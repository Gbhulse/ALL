jogador = {}
part = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    part.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = part[:]
jogador['total'] = sum(part)
print('-=' * 30)        

    

