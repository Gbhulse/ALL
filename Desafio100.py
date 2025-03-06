from random import randint

def gerar_list(lst):
    while len(lst) < 5:
        lst.append(randint(0, 100))

    soma = 0  # Inicializa dentro da função

    for c in lst:
        if c % 2 == 0:
            soma += c

    print(lst)
    print(soma)

# Criando lista vazia fora da função
lista = []

# Chama a função passando a lista
gerar_list(lista)