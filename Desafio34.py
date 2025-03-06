sal = float(input('Digite seu salário: '))

if sal > 1250:
    print(f'O salário será de {(sal*10/100) + sal}')
else:
    print(f'O salário atual será de {(sal*15/100) + sal}')

    
