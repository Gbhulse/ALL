lista = []
alunos = list()

# Entrada de dados dos alunos
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista = [nome, n1, n2]
    alunos.append(lista[:])  # Armazena uma cópia da lista
    lista.clear()

    cont = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break

# Exibição formatada dos alunos
print("\n" + "=" * 40)
print(f"{'N°':<5}{'Nome':<20}{'Média':>10}")
print("=" * 40)

for i, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i:<5}{aluno[0]:<20}{media:>10.2f}")

print("=" * 40)

# Consulta de notas individuais
while True:
    cont2 = int(input('\nVocê quer saber a nota de qual aluno? Digite o número (999 para finalizar): '))
    
    if cont2 == 999:
        break
    
    if 0 <= cont2 < len(alunos):  # Verifica se o índice existe na lista
        print(f"\nNotas de {alunos[cont2][0]}:")
        print(f"Nota 1: {alunos[cont2][1]:.2f}")
        print(f"Nota 2: {alunos[cont2][2]:.2f}")
    else:
        print("Aluno não encontrado! Digite um número válido.")

print("\nPrograma finalizado. 🎉")
