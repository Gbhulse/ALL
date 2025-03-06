def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print(s)

def contador(*núm):
    for valor in núm:
        print(f'{valor}')
    

soma(4, 5)

contador(2, 1, 7)
contador(8, 4)



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 5, 7, 23, 6]
dobra(valores)

def sum(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


sum(5,2)
