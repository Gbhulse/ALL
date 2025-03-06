n = list()
for c in range(0,5):
    valor = int(input('Digite um valor que irei adicionar: '))
    if c == 0:
        print('Adicionei o seu primeiro valor a lista!')
        n.append(valor)
    else:
        for s, k in enumerate(n):
            if valor > k:
                n.insert(s + 1, valor)
                print(f'Adicionei na posição {s+1} o seu valor')
                break
            elif valor < k:
                n.insert(s, valor)
                print(f'Adicionei na posição {s} o seu valor!')
                break
            else:
                n.insert(s, valor)
                print(f'Já tem um número repetido, mas adicionei na posição {s} o seu valor! ')
                break

print(f'Sua lista ficou {n}')