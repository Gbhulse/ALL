lista = []
sal = 0

def maior(*núm):
    lista.clear()
    for valor in núm:
        print('O valores foram {valor}', end = '')
        lista.append(valor)
    print("FIM\n")
    sal = max(lista) if len(lista) > 0 else 0
    print(f'Ao todo foram {len(lista)} valores ')
    if len(lista) > 0:
        print(f'O MAIOR VALOR É {sal}')
    else:
        print('O MAIOR VALOR É 0')


maior(3, 1, 5, 6, 10, 100, 43)
maior()
    
    

