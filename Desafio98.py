from time import sleep

def contador():
    for c in range(0, 11):
        print(f'{c} -> ', end=(''))
        sleep(0.2)

    print('')

    for c in range(10, -1, -1):
        print(f'{c} -> ', end = (''))
        sleep(0.2)
    
    print('')
    print('FIM')
    print('Agora é sua vez de personalizar a contagem! ')

    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))

    if c == 0:
        print('Passo 0 é inválido. Vamos ajustar para 1 ou -1 automaticamente.')
        if a < b:
            c = 1
        else:
            c = -1

     
    if a > b and c > 0:
        c = -c
    
    print(f'Contagem de {a} até {b} de {c} em {c}')
    
    for d in range(a, b + (1 if a < b else -1), c):
        print(f'{d} -> ', end=(''))
        
    print('FIM')

    print('Acabou o programa!')


contador()
