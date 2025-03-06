r = int(input('Qual a razão da sua PA? '))
a1 = int(input('Qual o primeiro termo? '))

for c in range(0, 10):
    print(f'a{c+1} = {a1 + c*r}')