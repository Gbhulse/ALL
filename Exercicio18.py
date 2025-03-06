import math

a = int(input('Qual o valor do ângulo, darei o sen e o cos: '))

rad = math.radians(a)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)

print(f'O avlot do seno é de : {sen} e do cosseno é de: {cos}')
