n = (input('Qual o seu nome completo? '))
n1 = n.upper()
n2 = n.lower()
n3 = len(n) - len(" ")
n4 = n.split()
n5 = n4[0]
n6 = len(n5)

print(f'O seu nome em letra Maiúscula é: {n1}')
print(f'O seu nome em letra minuscula é: {n2}')
print(f'O seu nome tem {n3} letras')
print(f'O seu nome sem sobrenome tem {n6} letras')