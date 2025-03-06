valor = int(input('Qual o valor a ser pago do produto? '))
n = int(input('Você quer pagar o valor no [1] pix, [2] cartão a vista, [3] cartão em 2x ou [4] cartão 3x? '))

if n == 1:
    print(f'Irá ficar no valor de R${valor - (valor*0.1)}')
elif n == 2:
    print(f'Irá ficar no valor de R${valor - (valor*0.05)})')
elif n == 3:
    print(f'Irá ficar no valor de R${valor}')
else:
    print(f'Ficará no valor de R${valor + (valor*0.3)}')