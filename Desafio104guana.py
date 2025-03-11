def leiain(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! DIGITE UM NÚMERO VÁLIDO\033[m")
        if ok:
            break
    return valor

n = leiain('DIGITE UM NÚMERO: ')
print(f'Voicê acavbou de digiotar o número {n}')