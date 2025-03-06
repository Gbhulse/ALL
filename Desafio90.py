
alunos = {}
turma = []

while True:
    alunos['Nome'] = str(input('Nome: '))
    alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
    if alunos['Média'] >= 7:
        alunos['Situação'] = 'Aprovado'
    elif 5 <= alunos['Média'] < 7:
        alunos['Situação'] = 'Recuperação'
    else:
        alunos['Situação'] = 'Reprovado'
    turma.append(alunos.copy())
    alunos.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)

for i in turma:
    for k, v in i.items():
        print(f'{k} é igual a {v}')
    print('-=' * 30)
