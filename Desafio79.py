n = list()
c = "S"

while True:
    valor = int(input('Digite um valor: '))
    if valor not in n:
        n.append(valor)
        print(f'Valor adicionado com succeso!')
    else:
        print(f'Valor duplicado!')
    c = str(input('Você quer continuar? [s/n]')).upper().strip()[0]
    if c == 'N':
        break

print(f'Você digitou os valores {sorted(n)}')