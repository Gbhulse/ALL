a = int(input('Diga um número: '))
b = int(input('Diga outro número: '))
c = int(input('último número: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior número é o {maior} e o menor é o \33[4;34m {menor}\33[4;35;41m')