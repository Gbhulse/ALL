n = int(input('Digite um número: '))

cont = 0
soma = 0

while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Diga mais um número, digite 999 para encerrar: '))

print(f'A soma do número é {soma} e você falou {cont} números')
