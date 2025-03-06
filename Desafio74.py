from random import randint

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)

t = (a, b, c, d, e)
f = sorted(t)

print(f'Os valores sorteados são {t}')
print(f'O menor é {f[0]}')
print(f'O maior é {f[-1]}')
print(f'O maior valor é {max(t)}')
print(f'O menor valor é {min(t)}')
