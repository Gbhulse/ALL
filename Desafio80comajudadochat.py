n = list()
for c in range(0,5):
    valor = int(input('Digite um valor que irei adicionar: '))
    if c == 0 or valor > n[-1]:
        print('Adicionei o seu primeiro valor na ultima posição da lista!')
        n.append(valor)
    else:
        for s, k in enumerate(n):
            if valor <= k:
                n.insert(s, valor)
                print(f'Adicionei na posição {s} o seu valor')
                break
            

print(f'Sua lista ficou {n}')