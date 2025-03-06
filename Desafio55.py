menor = 9999999999999999999999999999999999999999999999999999999
maior = 0

for c in range(0,5):
    pessoa = float(input('Qual o seu peso? '))
    if pessoa > maior:
        maior = pessoa
    elif pessoa < menor:
        menor = pessoa

print(f' Quem pesa mais é o que está com {maior}kg e o que pesa menos está com {menor}')
