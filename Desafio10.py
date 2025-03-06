n = int(input('QUantos reais gostaria de comprar os dólares inteiros? '))
dolar = 6.19
n1 = n//dolar
n2 = n%dolar
n3 = n/dolar

print(f'Você terá {n1} dolar e sobrará {n2} reais')
print(f'Caso nao for inteiro vai ficar {n3:.2f} dolares')
