tupla = ()
cont = 0
pares = ()

for c in range(0, 4):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        cont = cont + 1
        pares = pares + (num,)
    tupla = tupla + (num,)
    
print(f'{tupla}')


print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor três foi digitrado na {tupla.index(3)+1}º Posição')
else:
    print(f'O número três não está presente.')
print(f'Tem {cont} números pares que são {pares} ')