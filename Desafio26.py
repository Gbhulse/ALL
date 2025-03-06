nome = input('Qual seu nome completo? ').strip().upper()
cont = nome.count('A')
cont2 = nome.rfind('A')
cont3 = nome.find('A')

print(f' A letra A aparece {cont} vezes')
print(f' A letra A TERMINA no contador {cont2}')
print(f'A letra A começa no contador {cont3}')