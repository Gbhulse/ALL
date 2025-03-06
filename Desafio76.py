produtos = ('Pão', 1, 'Molho', 3, 'Vegetais', 10, 'Água', 5, 'Arroz', 2)

for pos, c in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{c:<15}', end= '')
    else:
        print(f'R${c:>5.2f}')
