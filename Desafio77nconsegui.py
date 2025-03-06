words = ('Maquina', 'Tio', 'Amigo', 'Filho', 'Excelente', 'Urso', 'Urubu', 'Uva')

for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end = " ")
    for letra in p:
        if letra.lower() in 'AaEeIiOoUu':
            print(letra, end = " ")