cont = soma = 0
while True:
    n = int(input('[999] para parar, Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'Seguinte, a soma dos números foi de {soma} e você escreveu {cont} números')

