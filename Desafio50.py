a = 0
b = 0

for c in range(0, 6):
    b = int(input('Digite um número: '))
    if b % 2 == 0:
        print(f'{b} é par')
        a += b
    
print(f'A soma total dos pares foi de {a}')

