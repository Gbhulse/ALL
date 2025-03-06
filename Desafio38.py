n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

if n1<n2:
    print(f'O número {n2} é maior que {n1}')

elif n2<n1:
    print(f'O número {n1} é maior que {n2}')

else:
    print('Os números tem o mesmo valor.')