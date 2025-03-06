temp = []
imp = []
par = []
princ = []

for c in range(0, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        imp.append(valor)
    

imp.sort()
par.sort()

princ.append([imp[:], par[:]])

print(f'{princ}')

