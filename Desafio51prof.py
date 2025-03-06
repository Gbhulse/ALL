p = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
dec = p + (10)*r
b = 0
for c in range(p, dec, r):
    b = b + 1
    print(f'O primeiro termo é {p} e o A{b} é {c}')
