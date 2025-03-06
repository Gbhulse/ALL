a = int(input('Digite a primeira reta, vamos ver se irá formam um retângulo: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if (a+b>c) and (a+c>b) and (b+c>a):
    print(f'Formará um triangulo')
    if (a==b or b==c or a==c) and not a==b==c:
        print('O triangulo é Isosceles')
    elif a != b != c != a: #Tem que botar a de novo pq não é inclusivo
        print('O trinagulo é escaleno')
    elif a==b==c:
        print('O triangulo é equilátero')
else:
    print(f'Não formará um triângulo!')