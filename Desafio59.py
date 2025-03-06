n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

op = 0
maior = 0

while op != 5:
    op = int(input('Digite uma opção com número, você quer que eu some os valores[1], multiplique[2], que fale qual o maior [3], quer novos números[4] ou quer sair do programa[5]: \n'))
    if op == 1:
        print(f'A soma dos números é de {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação é {n1*n2}')
    elif op == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número é o {maior}')
        elif n2 > n1:
            maior = n2
            print(f'O maior número é o {maior}')
        else:
            print(f'Os números são iguais')
    elif op == 4:
        n1 = int(input('Digite o novo valor para n1: '))
        n2 = int(input('Digite o novo valor para n2: '))
        