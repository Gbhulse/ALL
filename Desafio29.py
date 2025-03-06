vel = float(input('Qual a velocidade que o carro passou em km/h? '))

if vel <= 80:
    print(f'Você não recebeu nenhuma multa.')

else:
    multa = (vel - 80)*7
    print(f' Você foi multado por ultrapassar 80km/h, voce passou a {vel} e sua multa é de R${multa}')