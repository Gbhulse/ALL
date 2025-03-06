lista = []
alunos = list()
while True:
    while True:
        nome = str(input('Nome: '))
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        lista = [nome, n1, n2]
        alunos.append(lista[:])
        lista.clear()
        cont = str(input('Você quer continuar[S/N]'))
        if cont in 'nN':
            break
    while True:
        for l, c in enumerate(alunos):
            print(f'{l}, {c[0]:^20}, {((c[1]+c[2])/2):^20}')
        cont2 = int(input('Você quer saber a nota de qual aluno? Escreva pelo número: 999 par finalizar '))
        if cont2 == 999:
            break
        if cont2 != 999:
            print(f'A nota do aluno {alunos[cont2][0]} é {alunos[cont2][1]} e {alunos[cont2][2]}')
    break




