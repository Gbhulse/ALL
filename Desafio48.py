soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        print(f'O {c} é divisível por 3!')

print(f'A soma total é de {soma}')