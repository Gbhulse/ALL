p = int(input('Primeiro termo: '))
r = int(input('Razão'))
termo = p
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}')
        termo += r
        cont += 1
    mais = int(input('Quantos termos a mais queres mostrar? '))
print('FIM')


'''n = int(input('Diga o número que falarei sua PA até 10: '))
r = int(input('Qual sua razão: '))

termos = int(input('Quantos termos você quer saber?: '))

a = 1
print(f'o A1 então é {n}')
while a != termos:
    n = n + r
    print(f'O A{a+1} = {n}')
    a += 1
    if a == (termos - 1):
        termos = int(input('Você quer saber mais quantos termos: '))'''