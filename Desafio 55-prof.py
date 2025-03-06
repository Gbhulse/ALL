maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input(f'Qual o peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso é {maior} e o menor é {menor}')
