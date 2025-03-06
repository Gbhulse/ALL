num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 0)
num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print(f'Não achei o valor')

print(f'{num}')
