casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos será o pagamento? '))

pres = casa/(anos*12)

# Verificar se a prestação é menor ou igual a 30% do salário
if pres <= 0.3 * sal:
    print(f'Sua compra está aprovada! O valor da prestação será de R${pres:.2f} por mês, durante {anos} anos.')
else:
    print(f'Sua compra não foi aprovada. A prestação mensal seria de R${pres:.2f}, '
          f'e excede 30% do seu salário (R${sal:.2f}).')