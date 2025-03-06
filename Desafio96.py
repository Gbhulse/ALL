def área(a, b):
    print('-=-'*30)
    total = a * b
    print(f' A área de um terreno de largura {a} e comprimento {b} é de {total}')

print('Controle de Terrenos')
a = float(input('Qual a largura do seu terreno? '))
b = float(input('Qual o Comprimento? '))

área(a, b)