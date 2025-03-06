p = float(input('Qual distância você percorreu em km? '))

if p <= 200:
    custo = 0.5 * p
    print(f'Você fez até 200km, então seu custo será de {custo}')

else:
    custo2 = 0.45 * p
    print(f'Você percorreu mais de 200km, seu custo será de R${custo2}')