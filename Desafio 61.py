n = int(input('Diga o número que falarei sua PA até 10: '))
r = int(input('Qual sua razão: '))

a = 1
print(f'o A1 então é {n}')
while a != 10:
    n = n + r
    print(f'O A{a+1} = {n}')
    a += 1
