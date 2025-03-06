#Fatorial

n = int(input('Digite um número inteiro que eu direi seu fatorial: '))
n2 = n
fato = 1
while n2 > 1:
    fato = fato*(n2)
    n2 = n2 - 1
print(f'O fatorial é: {fato}')

fato = 1
for c in range(1, n + 1):
    fato = fato*c

print(f'O fatorial é: {fato}')