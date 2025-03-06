vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
reset = "\033[0m"

saque = int(input('Qual valor você quer sacar? '))
c = c1 = c2 = c3 = 0
while True:
    while saque >= 50:
        saque = saque - 50
        c += 1
    while saque >= 20:
        saque = saque - 20
        c1 += 1
    while saque >= 10:
        saque = saque - 10
        c2 += 1
    while saque >= 1:
        saque = saque - 1
        c3 += 1
    if saque == 0:
        break

print(f"""
{verde}São {c} notas de 50{reset}
{azul}{c1} notas de 20{reset}
{vermelho}{c2} notas de 10{reset}
{amarelo}{c3} notas de 1{reset}
""")

