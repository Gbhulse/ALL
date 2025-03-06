n = list()
cont = 0

while True:
    valor = int(input('Digite um valor que colocarei na lista: '))
    n.append(valor)
    cont += 1
    c = str(input(f'Você quer continuar? [s/n]? ')).upper().strip()[0]
    if c == 'N':
        break

n.sort(reverse = True)
print(f'A lista em ordem decrescente é {n}')

if 5 in n:
    print(f'O valor 5 está na lista!')
else:
    print(f'O VALOR 5 NÃO ESTÁ NA LISTA')