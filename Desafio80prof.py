n = list()
for c in range(0,5):
    valor = int(input('Digite um valor que irei adicionar: '))
    if c == 0 or valor > n[-1]:
        print('Adicionei o seu primeiro valor na ultima posição da lista!')
        n.append(valor)
    else:
        pos = 0
        while pos < len(n):
            if valor <= n[pos]:
                n.insert(pos , valor)
                break
            pos += 1

print(f'Os valores são {n}')
