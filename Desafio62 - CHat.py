n = int(input('Diga o número que falarei sua PA até 10: '))
r = int(input('Qual sua razão: '))
termos = int(input('Quantos termos você quer saber?: '))

a = 1
total_termos = termos  # Mantém controle do total de termos desejados inicialmente

print(f'O A1 é {n}')
while a < total_termos:  # Loop enquanto `a` for menor que o total de termos desejados
    n = n + r
    print(f'O A{a+1} = {n}')
    a += 1

    # Pergunta se o usuário quer mais termos quando atingir o limite inicial
    if a == total_termos:
        extra = int(input('Você quer saber mais quantos termos? (Digite 0 para parar): '))
        if extra > 0:
            total_termos += extra  # Atualiza o número total de termos