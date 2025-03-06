n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))

if n1 > n2 < n3 and n1 != n2 != n3:
    if n1 > n3:
        print(f' O menor número é o {n2} e o maior {n1}')
    else:
        print(f'O menor número é o {n2} e o maior é o {n3}')

elif n2 > n1 < n3 and n1 != n2 != n3:
    if n2 > n3:
        print(f'O menor número é o {n1} e o maior {n2}')
    else:
        print(f'O menor número é o {n1} e o maior é o {n3}')

if n1 > n3 < n2 and n1 != n2 != n3:
    if n1 > n2:
        print(f'O número {n3} é o menor e o {n1} é o maior')
    else:
        print(f'O número {n3} é o menor e o número {n2} é o maior')

else:
    print(f'Você escreveu dois números repetidos, reinicie o programa.')