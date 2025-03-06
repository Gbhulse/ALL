temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))[0]
    if resp in 'Nn':
        break

print(f'Os dados foram {princ}')
print(f'Foram cadastrados {len(princ)}')
print(f'O maior peso foi de {maior}')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')


                
    