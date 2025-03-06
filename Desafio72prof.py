cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete')

while True:
    num = int(input('Digite um número entre 0 e 6: '))
    if 0 <= num <= 20:
        break

print(f'Você digitou o número {cont[num]}')

