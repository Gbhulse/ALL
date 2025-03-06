num = ('Zero,', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

n = 11

while n > 10 or n < 0:
    n = int(input('Digite o número entre 0 a 10: '))
    
print(f'{num[n]}')