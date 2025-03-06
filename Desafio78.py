valor = list()

for c in range(0,5):
    valor.append(int(input(f'Digite um valor na posição {c}: ')))
    
print(f'Você digitou os valores {valor}')

maior = max(valor)
menor = min(valor)

for v, n in enumerate(valor):
    if n == maior:
        print(f' valor {maior} está na posição {v}')
    elif n == menor:
        print(f' O valor {menor} está na posição {v}')

     