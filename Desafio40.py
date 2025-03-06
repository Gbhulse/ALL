#Calculo de média

n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))

med = (n1+n2)/2

if med < 5:
    print(f'Sua média é {med:.2f} e você está reprovado')

elif med >=7:
    print(f'Você está aprovado, Parabéns! Nota final {med:.2f}')
else:
    print(f'Você está de recuperação, pois sua média foi {med:.2f}')