import math

ca = int(input('Qual o valor do cateto adjacente: '))
co = int(input('Qual o valor do cateto oposto: '))

h = math.hypot(ca, co)

print(f'O Valor da hipotenusa caso fosse um triângulo retângulo é: {h}')