#Número primo

a = int(input('Vamos verificar se o número é primo: '))

soma = 0

for c in range (1, a+1):
    if a % c == 0:
        print(f'O número é divisivel por {c}')
        soma += 1

if soma == 2:
    print(f'Seu número é primo : {a}')

else:
    print(f'Seu número {a} não é primo')