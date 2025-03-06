lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 4.00)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end = '')
    else:
        print(f'R${lista[pos]:>5.2f}')
    