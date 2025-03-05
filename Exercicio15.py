d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos Km você rodou? '))

dias = d*60
km = k*0.15

total = dias + km

print(f'Valor total de R${total}')