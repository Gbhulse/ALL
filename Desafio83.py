pard = list()
pare = list()

exp = str(input('Digite uma expressão: ')).strip()
for c in exp:
    if c == '(':
        pard.append(c)
    elif c == ')':
        pare.append(c)

a = len(pard)
b = len(pare)

if a == b:
    print(f'Sua expressão é válida')
else:
    print(f'Sua expressão é inválida')


