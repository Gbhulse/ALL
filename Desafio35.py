a = int(input('Digite a primeira reta, vamos ver se irá formam um retângulo: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if (a+b>c) and (a+c>b) and (b+c>a):
    print(f'Formará um triangulo')
else:
    print(f'Não formará um triângulo!')