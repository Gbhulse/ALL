nome = str(input('Qual o nome da cidade? '))
n = nome.upper().strip()

print(f'A cidade começa com santo? {'SANTO' == n[:5]}')